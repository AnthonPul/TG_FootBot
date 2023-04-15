from requests_html import AsyncHTMLSession
from collections import defaultdict
import pandas as pd
from IPython.display import display


url = 'https://www.flashscore.com/football/spain/laliga/results/'

asession = AsyncHTMLSession()

async def get_scores():
    r = await asession.get(url)
    await r.html.arender()
    return r

results = asession.run(get_scores)
results = results[0]

times = results.html.find("div.event__time")
home_teams = results.html.find("div.event__participant.event__participant--home")
home_score = results.html.find("div.event__score.event__score--home")
away_score = results.html.find("div.event__score.event__score--away")
away_teams = results.html.find("div.event__participant.event__participant--away")
#event_part = results.html.find("div.event__part")


dict_res_laliga = defaultdict(list)

for ind in range(len(times)):
    dict_res_laliga['times'].append(times[ind].text),
    dict_res_laliga['home_teams'].append(home_teams[ind].text),
    dict_res_laliga['home_score'].append(home_score[ind].text),
    dict_res_laliga['away_score'].append(away_score[ind].text),
    dict_res_laliga['away_teams'].append(away_teams[ind].text),
    #dict_res_laliga['event_part'].append(event_part[ind].text)

df_res_laliga = pd.DataFrame(dict_res_laliga)
df_res_laliga_short = df_res_laliga.loc[[0,1,2,3,4,5,6,7,8,9,10]]
#display(df_res_laliga.loc[[0,1,2,3,4,5,6,7,8,9,10]].to_string())