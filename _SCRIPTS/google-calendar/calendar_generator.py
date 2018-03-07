#!/usr/bin/python
# coding=utf-8

#
# CalendarGenerator class: parses a Google spreasheet containing the schedule
# for an event and creates an ICS file to import into Google calendar or other
# calendar applications.
#
# This code was inspired by the "proggen.py" script
# Author: Rodolfo S. Antunes (rsantunes@inf.ufrgs.br)
#

from icalendar import Calendar, Event, vText
from datetime import datetime as dt
from datetime import date
from hashlib import md5
import os

# spreadsheet header field names
COL_TYPE = 0
COL_TIME = 1
COL_ROOM = 2
COL_TITLE = 3
COL_CHAIR_SPKR_AUTHOR_DESC = 4
COL_KEYNT_ABSTRACT = 5
COL_SPKR_BIO = 6
COL_PHOTO_URL = 7
COL_FNAME = 8
COL_SLIDES = 9
COL_UID = 10

EVENT_FULL_NAME = dict(gaia='GAIA Workshop:', hotmiddlebox='HotMiddlebox Workshop:', qoe='Internet-QoE Workshop:', lancomm='LANCOMM Workshop:', netpl='NetPL Workshop:', sigcomm='SIGCOMM:', demos='SIGCOMM Demos:', posters='SIGCOMM Posters:', maintrackposters='SIGCOMM Main Track Posters:', idemos='SIGCOMM Industrial Demos:', tutorials='Tutorial:',breaks='')

PARTICIPANT_TYPE = dict(Talks='Speaker(s)', Keynote='Speaker(s)', Papers='Author(s)', Demos='Author(s)', Posters='Author(s)')

class DuplicateUidError(Exception):
   def __init__(self, uid, existing, duplicate):
      self.uid = uid
      self.existing = existing
      self.duplicate = duplicate
      return
   def __str__(self):
      return 'The UID {}, used in the event "{}", is also used on the event "{}"!'.format(self.uid, self.duplicate, self.existing)

class CalendarGenerator:
   INPUT_DATE_FORMAT = '%A, %B %d, %Y, %I:%M%p'
   INPUT_DATE_FORMAT_FULLDAY = '%A, %B %d, %Y'
   UID_SUFFIX = '@Sigcomm2016'

   def __init__(self):
      self.cal = Calendar()
      self.cal.add('prodid', '-//My calendar product//mxm.dk//')
      self.cal.add('version', '2.0')
      self.current_event = None
      self.processing_event = False
      self.current_description = dict(Talks=u"", Papers=u"", Posters=u"", Demos=u"", Chair=u"", Tutorial=u"", Discussion=u"", Keynote=u"")
      self.uid_control = dict()
      return

   def ToIcal(self):
      return self.cal.to_ical()

   def Day(self, date_string):
      self.current_date = date_string
      return

   def GenerateUid(self, event_title, uid, session_title):
      if uid in self.uid_control:
         raise DuplicateUidError(uid, self.uid_control[uid], session_title)
      else:
         self.uid_control[uid] = session_title
         uid_string = '{}-{}@{}'.format(uid, event_title, self.UID_SUFFIX)
         return md5(uid_string).hexdigest()

   def ResetSummary(self):
      description = ""
      if len(self.current_description['Chair']) > 0:
         description += u'Chair(s): {}\n\n'.format(self.current_description['Chair'])
      if len(self.current_description['Tutorial']) > 0:
         description += u'Presenter(s): {}\n\n'.format(self.current_description['Tutorial'])
      for ik in ['Papers', 'Talks', 'Demos', 'Posters']:
         if len(self.current_description[ik]) > 0:
            description += u'{}: {}\n\n'.format(ik, self.current_description[ik])
      if len(self.current_description['Discussion']) > 0:
         description += u'{}'.format(self.current_description['Discussion'])
      elif len(self.current_description['Keynote']) > 0:
         description += u'{}'.format(self.current_description['Keynote'])
      else:
         description = description[:-2]
      self.current_event.add('description', description)
      self.current_description = dict(Talks=u"", Papers=u"", Posters=u"", Demos=u"", Chair=u"", Tutorial=u"", Discussion=u"", Keynote=u"")
      return

   def ProcessDuration(self, duration):
      if len(duration) > 0:
         session_duration = duration.split('-')
         session_start = dt.strptime(self.current_date + ', ' + session_duration[0].strip(), self.INPUT_DATE_FORMAT)
         session_end = None
         if len(session_duration) > 1:
            session_end = dt.strptime(self.current_date + ', ' + session_duration[1].strip(), self.INPUT_DATE_FORMAT)
         return (session_start, session_end)
      else:
         session_day = dt.strptime(self.current_date, self.INPUT_DATE_FORMAT_FULLDAY).date()
         return (session_day, session_day)

   def Session(self, event_title, duration, title, location, uid, chair='', nodescription=False):
      if self.processing_event:
         self.FinishSession()
      new_event = Event()
      new_event.add( 'uid', self.GenerateUid(event_title, uid, title) )
      print_title = EVENT_FULL_NAME[event_title]
      new_event.add( 'summary', '{} {}'.format(print_title, title) )
      new_event.add( 'location', location )
      session_time = self.ProcessDuration(duration)
      new_event.add('dtstart', session_time[0])
      if session_time[1] != None:
         new_event.add('dtend', session_time[1])
      if nodescription:
         self.cal.add_component(new_event)
      else:
         self.current_event = new_event
         self.current_description['Chair'] = chair.strip()
         self.processing_event = True
      return

   def Tutorial(self, event_title, duration, title, location, uid, presenter='', nodescription=False):
      if self.processing_event:
         self.FinishSession()
      new_event = Event()
      new_event.add( 'uid', self.GenerateUid(event_title, uid, title) )
      print_title = EVENT_FULL_NAME[event_title]
      new_event.add( 'summary', '{} {}'.format(print_title, title) )
      new_event.add( 'location', location )
      session_time = self.ProcessDuration(duration)
      new_event.add('dtstart', session_time[0])
      if session_time[1] != None:
         new_event.add('dtend', session_time[1])
      if nodescription:
         self.cal.add_component(new_event)
      else:
         self.current_event = new_event
         self.current_description['Tutorial'] = presenter.strip()
         self.processing_event = True
      return

   def FinishSession(self):
      self.ResetSummary()
      self.cal.add_component(self.current_event)
      self.processing_event = False
      return

   def SessionItem(self, itemtype, session_item_title, authors=''):
      if len(authors) > 0:
         self.current_description[itemtype] += u'\n\n* Title: {} – {}: {}'.format(session_item_title, PARTICIPANT_TYPE[itemtype], authors)
      else:
         self.current_description[itemtype] += u'* {}'.format(session_item_title)
      return

   def SessionKeynote(self, session_keynote_title, author, abstract, shortbio):
      aux_session = u'* Keynote Title:\n{}\n\n'.format(session_keynote_title)
      aux_session += u'Speaker:\n{}\n\n'.format(author)
      aux_session += (u'Abstract:\n{}\n\n'.format(abstract) if len(abstract) > 0 else "")
      aux_session += (u'Speaker Bio:\n{}\n\n'.format(shortbio) if len(shortbio) > 0 else "")
      self.current_description['Keynote'] += aux_session
      return

   def ParseWorksheet(self, event_title, values, outdir):
      for raw_row in values:
         row = [x.strip() for x in raw_row]

         if row[COL_TYPE] == 'day':
            self.Day(row[COL_TIME])
            
         elif row[COL_TYPE] == 'session':
            event_type = row[COL_TYPE]
            time_info = (row[COL_TIME] if len(row)> COL_TIME else "")
            title_info = (row[COL_TITLE] if len(row)> COL_TITLE else "")
            room_info = ('Room: {}'.format(row[COL_ROOM]) if len(row)> COL_ROOM else "")
            uid_info = (row[COL_UID] if len(row)> COL_UID else "")
            chair_info = (row[COL_CHAIR_SPKR_AUTHOR_DESC] if len(row)> COL_CHAIR_SPKR_AUTHOR_DESC else "")
            self.Session(event_title, time_info, title_info, room_info, uid_info, chair=chair_info)
            
         elif row[COL_TYPE] == 'tutorial':
            event_type = row[COL_TYPE]
            time_info = (row[COL_TIME] if len(row)> COL_TIME else "")
            title_info = (row[COL_TITLE] if len(row)> COL_TITLE else "")
            room_info = ('Room: {}'.format(row[COL_ROOM]) if len(row)> COL_ROOM else "")
            uid_info = (row[COL_UID] if len(row)> COL_UID else "")
            presenter_info = (row[COL_CHAIR_SPKR_AUTHOR_DESC] if len(row)> COL_CHAIR_SPKR_AUTHOR_DESC else "")
            self.Tutorial(event_title, time_info, title_info, room_info, uid_info, presenter=presenter_info)
            
         elif row[COL_TYPE] == 'social':
            event_type = row[COL_TYPE]
            time_info = (row[COL_TIME] if len(row)> COL_TIME else "")
            title_info = (row[COL_TITLE] if len(row)> COL_TITLE else "")
            room_info = (row[COL_ROOM] if len(row)> COL_ROOM else "")
            uid_info = (row[COL_UID] if len(row)> COL_UID else "")
            self.Session(event_title, time_info, title_info, room_info, uid_info, nodescription=True)
            
         elif row[COL_TYPE] == 'talk':
            title_info = (row[COL_TITLE] if len(row)> COL_TITLE else "")
            chair_info = (row[COL_CHAIR_SPKR_AUTHOR_DESC] if len(row)> COL_CHAIR_SPKR_AUTHOR_DESC else "")
            self.SessionItem('Talks', title_info, chair_info)
            
         elif row[COL_TYPE] == 'paper':
            title_info = (row[COL_TITLE] if len(row)> COL_TITLE else "")
            chair_info = (row[COL_CHAIR_SPKR_AUTHOR_DESC] if len(row)> COL_CHAIR_SPKR_AUTHOR_DESC else "")
            self.SessionItem('Papers', title_info, chair_info)
            
         elif row[COL_TYPE] == 'poster':
            title_info = (row[COL_TITLE] if len(row)> COL_TITLE else "")
            chair_info = (row[COL_CHAIR_SPKR_AUTHOR_DESC] if len(row)> COL_CHAIR_SPKR_AUTHOR_DESC else "")
            self.SessionItem('Posters', title_info, chair_info)
            
         elif row[COL_TYPE] == 'demo':
            title_info = (row[COL_TITLE] if len(row)> COL_TITLE else "")
            chair_info = (row[COL_CHAIR_SPKR_AUTHOR_DESC] if len(row)> COL_CHAIR_SPKR_AUTHOR_DESC else "")
            self.SessionItem('Demos', title_info, chair_info)
            
         elif row[COL_TYPE] == 'disc':
            title_info = (row[COL_TITLE] if len(row)> COL_TITLE else "")
            self.SessionItem('Discussion', title_info)
            
         elif row[COL_TYPE] == 'keynote':
            title_info = (row[COL_TITLE] if len(row)> COL_TITLE else "")
            speaker_info = (row[COL_CHAIR_SPKR_AUTHOR_DESC] if len(row)> COL_CHAIR_SPKR_AUTHOR_DESC else "")
            keynote_abstract_info = (row[COL_KEYNT_ABSTRACT] if len(row)> COL_KEYNT_ABSTRACT else "")
            speaker_bio_info = (row[COL_SPKR_BIO] if len(row)> COL_SPKR_BIO else "")
            self.SessionKeynote(title_info, speaker_info, keynote_abstract_info, speaker_bio_info)
            
      if self.processing_event:
         self.FinishSession()
      with open( os.path.join(outdir, event_title+'.ics'), 'w' ) as arq:
         arq.write( self.ToIcal() )
      return
