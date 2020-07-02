

# import required libraries
import requests
from lxml import html
# alternatives: BeautifulSoup, Selenium (free and paid)


# Step 2: Make request to url and instantiate a html object
page = requests.get('https://www.premierleague.com/clubs')
help(page)
tree = html.fromstring(page.content)
help(tree)

# Step 3: Inspect the url to understand which field to focus on

# Step 4: Collect links to team info. Then to team squad
#Using the page's CSS classes, extract all links pointing to a team
team_link = tree.cssselect('.indexItem')
# if error: pip install cssselect

# indexItem is the class. what we want is the address of the data for the company 
print(team_link[0].attrib['href'])



# we could go to any of the tabs, e.g. statistics, results, tickets, more
# but let's focus on the squad and collect data for each player
# again, what we have is the address to each club. that is:
'http://www.premierleague.com/'+team_link[0].attrib['href']

# Step 5: Request url of the first team squad (Arsenal)
# let's focus on the squad. to navigate there, simply replace overview with squad:
team_overview_link_sample = 'http://www.premierleague.com/'+team_link[0].attrib['href']
team_squad_link_sample = team_overview_link_sample.replace("overview", "squad")


# Step 6: Inspect web page to understand which object leads to one player. Select first player

# Step 7: Inspect web page to understand how to collect player name and player stats

squadPage_sample = requests.get(team_squad_link_sample)
squadTree_sample = html.fromstring(squadPage_sample.content)

# Step 8: Collect player name and stats
player_object = squadTree_sample.cssselect('.playerOverviewCard')
first_player_object = player_object[0]

player_name_sample = first_player_object.cssselect('.playerCardInfo')[0].cssselect('.name')[0].text_content()

player_stats_sample = first_player_object.cssselect('.squadPlayerStats')[0].cssselect('.info')

for elem in player_stats_sample:
    print(elem.text_content().replace(' ','').replace('\n',''))


country_sample = player_stats_sample[0].text_content().replace(' ','').replace('\n','')
age_sample = int(player_stats_sample[1].text_content().replace(' ','').replace('\n',''))
appearances_sample = int(player_stats_sample[2].text_content().replace(' ','').replace('\n',''))




