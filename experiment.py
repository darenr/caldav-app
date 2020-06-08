import os
import caldav
from datetime import datetime, timedelta

def get_weeks_events():

    client = caldav.DAVClient(os.getenv('CALDAV_URL'), username=os.getenv('CALDAV_USERNAME'), password=os.getenv('CALDAV_PASSWORD'))

    principal = client.principal()

    today = datetime.now()
    next_5_days = today + timedelta(days=5)

    for calendar in principal.calendars():
        # events = calendar.events()
        events = calendar.date_search(
            start=today, end=next_5_days,
            expand=True)
        for event in sorted(events, key=lambda x: x.instance.vevent.dtstart.value):
            start_event = event.instance.vevent.dtstart.value
            end_event = event.instance.vevent.dtend.value

            print(f'{start_event.strftime("%m/%d/%Y, %H:%M")}-{end_event.strftime("%H:%M")} - {event.vobject_instance.vevent.summary.value}')
