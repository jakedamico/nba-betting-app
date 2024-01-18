from nba_api.stats.static import teams

from spreadsheetConverter import dataframe_to_excel

# Find teams by full name.
allTeams = teams.find_teams_by_full_name('cav')