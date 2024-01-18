from flask import Flask, jsonify, request
from playerStatsManager import save_team_players_stats
from liveScoreboardManager import get_todays_nba_games, get_live_boxscore

app = Flask(__name__)

@app.route('/api/current-games', methods=['GET'])
def api_todays_games():
    games = get_todays_nba_games()
    return jsonify(games)

@app.route('/api/live-boxscore/<game_id>', methods=['GET'])
def api_live_boxscore(game_id):
    box_score = get_live_boxscore(game_id)
    return jsonify(box_score)

if __name__ == '__main__':
    app.run(debug=True)

