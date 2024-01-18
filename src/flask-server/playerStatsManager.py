from nba_api.stats.endpoints import playercareerstats, commonteamroster
from nba_api.stats.static import teams as teamsStatic
from spreadsheetConverter import dataframe_to_excel

def get_team_players(team_name):
    """Returns a DataFrame of players for the specified team."""
    nba_teams = teamsStatic.find_teams_by_full_name(team_name)
    if not nba_teams:
        print("Team not found")
        return None

    team_id = nba_teams[0]['id']
    roster = commonteamroster.CommonTeamRoster(team_id=team_id)
    return roster.get_data_frames()[0]

def get_player_career_stats(player_id, player_name):
    """Saves the career stats of a player to an Excel file."""
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    filename = f'{player_name}_career_stats.xlsx'
    dataframe_to_excel(career.get_data_frames()[0], filename)
    print(f"Saved {filename}")

def save_team_players_stats(team_name):
    """Retrieves and saves career stats for all players in a team."""
    team_players = get_team_players(team_name)
    if team_players is not None:
        for _, player in team_players.iterrows():
            player_id = player['PLAYER_ID']
            player_name = player['PLAYER']
            get_player_career_stats(player_id, player_name)
