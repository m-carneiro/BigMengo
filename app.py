from flask import Flask
from flask_restful import Api

from football.services.football import FootballCompetitions, FootballMatches
from google.services.google import GoogleTest, GoogleCalendarEvents, GoogleFootballIntegration

app = Flask(__name__)
api = Api(app)

api.add_resource(FootballCompetitions, '/football/competitions')
api.add_resource(FootballMatches, '/football/matches')

api.add_resource(GoogleTest, '/google/test')
api.add_resource(GoogleCalendarEvents, '/google/events')

api.add_resource(GoogleFootballIntegration, '/google/football/all')

if __name__ == '__main__':
    app.run(debug=True)
