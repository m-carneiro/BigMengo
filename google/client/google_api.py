import json
import logging

from beautiful_date import *
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.serializers.event_serializer import EventSerializer

from football.client.football_api import FootballApi


class CalendarApi:
    def __init__(self):
        pass

    def get_all_events(self):
        google_calender = self._google_authenticated()
        all_events = google_calender.get_events()
        events = []

        for event in all_events:
            events.append(str(event))

        return events

    def get_all_calendars(self):
        google_calender = self._google_authenticated()
        all_calendars = google_calender.get_calendar_list()
        calendars = []

        for calendar in all_calendars:
            calendars.append(str(calendar))

        return calendars

    def _google_authenticated(self):
        return GoogleCalendar(credentials_path='client_secret.json')

    def add_all_events(self):
        all_matches = FootballApi().get_competitions()
        google_calendar = self._google_authenticated()
        flamengo_color = '11'  # red

        for match in all_matches:
            date = BeautifulDate(
                month=int(match['date_time'][0].split('-')[1]),
                day=int(match['date_time'][0].split('-')[2]),
                year=int(match['date_time'][0].split('-')[0])
            )[int(match['date_time'][1].split(':')[0]):int(match['date_time'][1].split(':')[1])]

            event = Event(
                f"{match['competition']} |{match['home_team']} x {match['away_team']}",
                date,
                date + 2 * hours,
                color_id=flamengo_color,
                minutes_before_popup_reminder=15
            )
            print(f'Adding event: {event}')

            event = google_calendar.add_event(event)
            EventSerializer.to_json(event)
