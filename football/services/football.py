from flask_restful import Resource
from football.client.football_api import FootballApi


class FootballCompetitions(Resource):

    def get(self):
        pass


class FootballMatches(Resource):

    def get(self):
        matches = FootballApi().get_competitions()

        return matches, 200
