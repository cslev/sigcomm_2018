#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# calgen.py: script to parse a Google spreadsheet containing the schedule
# for an event and creates an ICS file to import into Google calendar or other
# calendar applications. This script imports the "calendar_generator" file,
# which contains the class that parses the spreadsheet information and
# generates the actual ICS file structure.
#
# This code was inspired by the "proggen.py" script
# Author: Rodolfo S. Antunes (rsantunes@inf.ufrgs.br)
#

from __future__ import print_function
import httplib2
import os
import codecs
from htmlentitydefs import codepoint2name

import argparse
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from calendar_generator import CalendarGenerator
from calendar_generator import DuplicateUidError

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Sigcomm16'
SPREADSHEETID = '1AK4VdEuogGTaFRLia8Ef-AaZdAJOu5AxE7KAA1Nj7tU'
COLUMN_RANGE = 'A2:K' # note we assume the header row to be present !!!

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-sigcomm16.json')
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args([])
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + credential_path)
    return credentials

def main(outdir, wsnames):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    result = service.spreadsheets().get(
        spreadsheetId=SPREADSHEETID).execute()

    sheets = result.get('sheets', [])

    if len(sheets)==0:
        print('No worksheets found.')
    else:
        for ws in sheets:
            # do selected worksheets only
            if (len(wsnames)>0 and not ws['properties']['title'] in wsnames):
                continue

            # Note we assume the header row to be present !!!
            rangeName = '%s!%s'%(ws['properties']['title'],COLUMN_RANGE)
            result = service.spreadsheets().values().get(
                spreadsheetId=SPREADSHEETID, range=rangeName).execute()
            values = result.get('values', [])
            # Instantiate the Calendar Generator Class and invoke the
            # method that parses the entire worksheet data.
            calgen = CalendarGenerator()
            try:
                print ('Processing spreadsheet {}...'.format(ws['properties']['title']))
                calgen.ParseWorksheet(ws['properties']['title'], values, outdir)
            except DuplicateUidError as exc:
                print ('ERROR:')
                print (exc)
                print ('Please, fix the values on the spreadsheet before continuing.')
                sys.exit (1)

    print("Done!")

if __name__ == '__main__':
    import sys
    if (len(sys.argv)<=1):
        print('Usage: python %s <outputdir> [worksheet names]'%sys.argv[0])  
        sys.exit(1)

    outdir = sys.argv[1]
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    main(outdir, sys.argv[2:])

