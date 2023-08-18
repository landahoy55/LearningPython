# Loaded variable 'df' from URI: c:\Users\qo19921\LearningPython\Wrangler\all_matches.csv
import pandas as pd
df = pd.read_csv(r"c:\Users\qo19921\LearningPython\Wrangler\all_matches.csv")

# Rename column 'venue' to 'stadium'
df = df.rename(columns={'venue': 'stadium'})

# Replace missing values with "" in column: 'player_dismissed'
df = df.fillna({'player_dismissed': ""})

# Replace all instances of "null" with "Not out" in column: 'player_dismissed'
df['player_dismissed'] = df['player_dismissed'].str.replace("null", "Not out", case=False, regex=False)

# Replace missing values with "Not out" in column: 'wicket_type'
df = df.fillna({'wicket_type': "Not out"})

# Performed 1 aggregation grouped on column: 'match_id'
df = df.groupby(['match_id']).agg(noballs_count=('noballs', 'count')).reset_index()

# Sort by column: 'noballs_count' (ascending)
df = df.sort_values(['noballs_count'])

# Sort by column: 'noballs_count' (descending)
df = df.sort_values(['noballs_count'], ascending=[False])