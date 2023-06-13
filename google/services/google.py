from flask_restful import Resource
from google.client.google_api import CalendarApi


class GoogleTest(Resource):
    def get(self):
        try:
            calendars = CalendarApi().get_all_calendars()
        except ConnectionError or Exception:
            return {'message': 'Connection error'}, 500
        return calendars, 200


class GoogleCalendarEvents(Resource):
    def get(self):
        try:
            events = CalendarApi().get_all_events()
        except ConnectionError or Exception:
            return {'message': 'Connection error'}, 500
        return events, 200


class GoogleFootballIntegration(Resource):
    def get(self):
        try:
            events = CalendarApi().add_all_events()
        except ConnectionError or Exception:
            return {'message': 'Connection error'}, 500
        return events, 200