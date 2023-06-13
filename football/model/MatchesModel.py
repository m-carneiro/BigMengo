
class Matches:
    def __init__(self, competition, date_time, home_team, away_team):
        self.competition = competition
        self.date_time = date_time
        self.home_team = home_team
        self.away_team = away_team

    def json(self):
        return {
            'competition': self.competition,
            'date_time': self.date_time,
            'home_team': self.home_team,
            'away_team': self.away_team
        }
