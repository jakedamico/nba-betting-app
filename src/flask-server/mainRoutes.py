from flask import Flask, jsonify, request
from playerStatsManager import save_team_players_stats
from liveScoreboardManager import get_todays_nba_games, get_live_boxscore

app = Flask(__name__)

@app.route('/api/current-games', methods=['GET'])
def api_todays_games():
    games = get_todays_nba_games()
    return jsonify(games)

if __name__ == '__main__':
    app.run(debug=True)

