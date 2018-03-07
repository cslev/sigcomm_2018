calgen.py -- sigcomm script for generating an ical calendar file for google calendar, with support to event add + update
             Author: Rodolfo S. Antunes (rsantunes@inf.ufrgs.br)

python calgen.py <output_dir> <spreadsheet list>

Dependencies: This script requires the icalendar python module -- just run "pip install icalendar"
              To setup the Google Spreadsheet API and credentials, follow the steps in https://developers.google.com/sheets/quickstart/python


Description: This script generates an .ical file for each sheet passed in the list above. As currently implemented, this script generates calendar entries only for "session" and "social". The entry types "talk", "poster", "demo", "disc", and "keynote" are added as session items of the last added calendar entry. The date of the calendar entry is the last "day" entry type read. Entries without time info will be registered as full-day.

One important aspect of this script is the data added to column COL_UID of each sheet. It is used to keep control of calendar entries, and make sure that any changes to an event in the sheet are updated to its respective calendar entry on Google calendar. This string id needs to be unique and cannot be repeated (e.g. reused from an event previously deleted), to avoid calendar inconsistencies, specially for those people who are subscribed to the calendar or just copied some specific event to their own calendar.

The expected format for the program sheet is: "COL_TIME  COL_ROOM  COL_TITLE  COL_CHAIR_SPKR_AUTHOR_DESC  COL_KEYNT_ABSTRACT  COL_SPKR_BIO  COL_PHOTO_URL  COL_FNAME  COL_SLIDES  COL_UID"

Example:

          python calgen.py ../sigcomm16web.master/scripts/google-calendar/calendar/ netpl lancomm sigcomm posters demos maintrackposters idemos gaia hotmiddlebox qoe tutorials breaks

Instead of uploading ical files one by one, you can upload a single .ical file containing all the program. In order to join all calendars in a single file (of course, run on the same dir the .ical files are placed; full-conf.ics file in the folder will be overwritten), run the following:

rm -f full-conf.ics; printf "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//My calendar product//mxm.dk//\n" > full-conf; cat * | egrep -v "VCALENDAR|VERSION:2.0|PRODID" >> full-conf; echo "END:VCALENDAR" >> full-conf; mv full-conf full-conf.ics;

