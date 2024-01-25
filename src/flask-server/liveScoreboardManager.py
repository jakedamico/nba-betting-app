from flask import jsonify
from datetime import datetime, timezone
from dateutil import parser
from nba_api.live.nba.endpoints import scoreboard, boxscore

def get_todays_nba_games():
    """
    Fetches NBA games for the current day and returns a list of dictionaries 
    with each game's details including id, home team, away team, and time.
    """
    todays_games_list = []
    f = "{gameId}: {awayTeam} vs. {homeTeam} @ {gameTimeLTZ}" 

    try:
      board = scoreboard.ScoreBoard()
      print("ScoreBoardDate: " + board.score_board_date)
      games = board.games.get_dict()
      for game in games:
         gameTimeLTZ = parser.parse(game["gameTimeUTC"]).replace(tzinfo=timezone.utc).astimezone(tz=None)
         game_info = {
            "gameId": game['gameId'],
            "awayTeam": game['awayTeam']['teamName'],
            "homeTeam": game['homeTeam']['teamName'],
            "gameTimeLTZ": gameTimeLTZ,
            "gameStatusText": game['gameStatusText'],
            "gameClock": game['gameClock'],
            "currentQuarter": game['period'],
            "homeTeamScore": game['homeTeam']['score'],
            "awayTeamScore": game['awayTeam']['score']
         }
         todays_games_list.append(game_info)
         print(f.format(**game_info))
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    return todays_games_list

def get_live_boxscore(game_id):
    """
    Fetches the live box score for a given NBA game using its game ID.
    """
    try:
        live_boxscore_data = boxscore.BoxScore(game_id=game_id)
        # Assuming we want to print the box score stats
        return live_boxscore_data.game.get_dict()
    except Exception as e:
        print(f"An error occurred while fetching the live box score: {e}")