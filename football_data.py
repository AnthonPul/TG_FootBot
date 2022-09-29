from FB_base import *


class FSSoccer(FlashScore):
    def __init__(self):
        FlashScore.__init__(self)
        self.url = "http://www.flashscore.com/"
        self.standingsurls = ""

    def find_team(self, query):
        q = query.lower()

        results = []
        soup = BeautifulSoup(self.fetch_page(self.url))
        leagues = soup.findAll('table', {'class': 'soccer'})

        # first try to search in league name
        for league in leagues:
            thead = league.find('thead')
            name = thead.find('span', {'class': 'country_part'}).text.strip() + thead.find('span', {
                'class': 'tournament_part'}).text.strip()
            name_lc = name.lower()
            if q in name_lc:
                matches = league.find('tbody').findAll('tr')
                for match in matches:
                    home = match.find('td', {'class': 'team-home'}).text.strip()
                    away = match.find('td', {'class': 'team-away'}).text.strip()
                    score = match.find('td', {'class': 'score'}).text.strip()
                    matchtimer = match.find('td', {'class': 'timer'}).text.strip()

                    if not matchtimer:  # match has not started
                        matchstatus = match.find('td', {'class': 'time'}).text.strip()
                    elif matchtimer == "Finished":  # match finished
                        matchstatus = "FT"
                    else:  # any other case
                        matchstatus = matchtimer

                    item = home + " " + score + " " + away + " " + matchstatus
                    results.append(item.replace(u'\xa0', u' '))  # replace the non-space break character with space

        # then search in team name
        for league in leagues:
            matches = league.find('tbody').findAll('tr')
            for match in matches:
                home = match.find('td', {'class': 'team-home'}).text.strip()
                home_lc = home.lower()
                away = match.find('td', {'class': 'team-away'}).text.strip()
                away_lc = away.lower()
                if (q in home_lc) or (q in away_lc):  # we have a match
                    score = match.find('td', {'class': 'score'}).text.strip()
                    matchtimer = match.find('td', {'class': 'timer'}).text.strip()

                    if not matchtimer:  # match has not started
                        matchstatus = match.find('td', {'class': 'time'}).text.strip()
                    elif matchtimer == "Finished":  # match finished
                        matchstatus = "FT"
                    else:  # any other case
                        matchstatus = matchtimer

                    item = home + " " + score + " " + away + " " + matchstatus
                    results.append(item.replace(u'\xa0', u' '))  # replace the non-space break character with space
        return results



