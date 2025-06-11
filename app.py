from flask import Flask,jsonify,request
from matches import teamapi,teamvsteam,players,team_details,batter_details,bowler_details
import json



app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/api/teams')
def teams():
    teams = teamapi()
    return jsonify(teams)

@app.route('/api/teamvsteam')
def teamvsteamres():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = teamvsteam(team1,team2)
    return jsonify(response)
    
@app.route('/api/manofMatch')
def manofmatch():
    team1 = request.args.get('team')
    response = players(team1)
    return jsonify(response)

@app.route('/api/teamDetails',methods = ['GET'])
def get_team_details():
    team = request.args.get('team')
    response = team_details(team)
    return response

@app.route('/api/batsmanDetail',methods=['GET'])
def get_batsman_details():
    batsman_detail = request.args.get("playerName")
    response = batter_details(batsman_detail)
    return response


@app.route("/api/bowlersDetail",methods=['GET'])
def get_bowlers_details():
    bowler_detail = request.args.get("playerName")
    response = bowler_details(bowler_detail)
    return response


app.run(debug=True)


