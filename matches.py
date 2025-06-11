import pandas as pd
import numpy as np
import json

ipl_matches = r"D:\python\flaskapicreation\matches.csv"
matches = pd.read_csv(ipl_matches)

matches.rename(index ={'Rising Pune Supergiant':'Rising Pune Supergiants'},inplace=True)
matches.replace({'team1': {'Rising Pune Supergiant': 'Rising Pune Supergiants'},
                 'team2': {'Rising Pune Supergiant': 'Rising Pune Supergiants'}}, inplace=True)
matches.replace({
'team1':{'Royal Challengers Bengaluru':'Royal Challengers Bangalore'},
'team2':{'Royal Challengers Bengaluru':'Royal Challengers Bangalore'}
},inplace=True)
matches.replace({'team1':{'Delhi Capitals':'Deccan Chargers'},
                 'teams2':{'Delhi Capitals':'Deccan Chargers'}},inplace=True)
matches.replace({'team1':{'Delhi Daredevils':'Deccan Chargers'},
                'team2':{'Delhi Daredevils':'Deccan Chargers'}},inplace=True)
matches.replace({'team1':{'Gujarat Lions':'Gujarat Titans'},
                'team2':{'Gujarat Lions':'Gujarat Titans'}},inplace=True)
matches.replace({'team1':{'Delhi Capitals':'Deccan Chargers'},
                'team2':{'Delhi Capitals':'Deccan Chargers'}},inplace=True)
teams = set(list(matches['team1'])+list(matches['team2']))
matches.replace({'}winner':{'Delhi Capitals':'Deccan Chargers'}},inplace=True)

def teamapi():
    teams = list(set(list(matches['team1'])+list(matches['team2'])))
    team_dict = {"teams": teams}
    print(team_dict)
    return team_dict

def teamvsteam(team1,team2):
    team1 = team1
    team2 = team2
    print(team1)
    print(team2)
    temp_df = matches[((matches['team1']==team1) & (matches['team2']==team2))  | ((matches['team1']==team2) & (matches['team2']==team1))]
    total_matches = temp_df.shape[0]
    matches_won_team1 = temp_df['winner'].value_counts()[team1]
    matches_won_team2 = temp_df['winner'].value_counts()[team2]
    draws = total_matches - (matches_won_team1+matches_won_team2)
    response = {
        "team1": str(team1),
        "team2": str(team2),
        "total_matches": str(total_matches),
        "matches_won_team1": str(matches_won_team1),
        "matches_won_team2": str(matches_won_team2),
        "draws": str(draws)
    }
    try:
        return response
    except Exception as e:
        return str(e)
    
def players(team1):
    man_of_the_match = list(set(matches[(matches['team1'] == team1) & matches['player_of_match'].notna()]['player_of_match']))
    opponents = list(set(matches[matches['team1'] == team1]['team2']))
    
    return {
        "team": team1,
        "opponent": opponents,
        "man_of_the_match": man_of_the_match


    }

def team_details(team):
    matches = pd.read_csv("matches.csv")
    m = matches[(matches['team1']==team) | (matches['team2']==team)]
    total_matches =len(m)
    matches_won = len(m[m['winner']==team])
    matches_loss = total_matches-matches_won

    return json.dumps({
        "team": team,
        "total_matches": total_matches,
        "matches_won": matches_won,
        "matches_loss": matches_loss,
    })
def batter_details(batter_name):
    matches = pd.read_csv("matches.csv")
    df = pd.read_csv("deliveries.csv")
    p = df.groupby("batter")
    playerofmatch = matches[matches["player_of_match"]==batter_name]
    val = p.get_group(batter_name)
    teams_of_batter = list(set(val["batting_team"]))
    total_match_played =len(val.groupby("match_id"))

    return json.dumps({
        "batter_name": batter_name,
        "no of time player of match": len(playerofmatch),
        "teams of batter": teams_of_batter,
        "total match played": total_match_played
    })

def bowler_details(bowllerName):
    matches = pd.read_csv("matches.csv")
    df = pd.read_csv("deliveries.csv")
    playerofmatch = matches[matches["player_of_match"]==bowllerName]
    p = df.groupby("bowler")
    val = p.get_group(bowllerName)
    if bowllerName in p.groups:
        val = p.get_group(bowllerName)
        total_game_played = len(val.groupby('match_id'))
        bowlers_team = list(set(val["bowling_team"]))
    else:
        return json.dumps({"error": f"{bowllerName} not found in dataset"})


    return json.dumps({
        "bowler_name": bowllerName,
        "no of time player of match": len(playerofmatch),
        "total games played":total_game_played,
        "bowlers_team": bowlers_team    
    })



# val = teamvsteam("Royal Challengers Bangalore","Mumbai Indians")
# print(val)

# val = players('Royal Challengers Bangalore')
# print(val)

# val = team_details('Royal Challengers Bangalore')
# print(val)
# data = bowler_detail("P Kumar")
# print(data)