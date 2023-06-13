from datetime import datetime, timedelta

import requests
import os

from bs4 import BeautifulSoup

from football.model.MatchesModel import Matches


class FootballApi:
    football_url = os.getenv('FOOTBALL.API.URL')

    def __init__(self):
        pass

    def get_competitions(self):
        headers = {'Referer': 'https://www.google.com'}

        response = requests.get(self.football_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        matches = []

        table_row = soup.find_all('tr')

        for table_data in table_row:
            results = table_data.text.split('\n')

            match = Matches(
                results[1].strip(),
                [
                    self._format_date(results[2].split(' ')[0].split('/')),
                    self._format_time(results[2].split(' ')[1]),
                ],
                results[6].strip(),
                results[8].strip() if results[8].strip() != '' else 'error',
            )

            matches.append(match.json())
        return matches

    def _format_date(self, date):
        return datetime(2023, int(date[0]), int(date[1])).strftime('%Y-%m-%d')

    def _format_time(self, time):
        return (datetime.strptime(time, '%H:%M') - timedelta(hours=4)).strftime('%H:%M')

    def _check_how_many_pages(self):
        number_of_pages = []
        response = requests.get(self.football_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        pages = soup.find_all('ul', {'class': 'pagination'})

        for page in pages:
            for x in page.text.split('\n'):
                if x.strip() != '':
                    if x.strip().isdigit() and not None:
                        number_of_pages.append(int(x))

        return max(number_of_pages)
