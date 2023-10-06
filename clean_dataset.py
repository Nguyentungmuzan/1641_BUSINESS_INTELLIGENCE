import pandas as pd

# Load the data from the Excel file
df = pd.read_excel("Updated_Spotify_data.xlsx")

# # Filter out rows with the word "None"
# df = df[~df.applymap(lambda x: x == "None" if isinstance(x, str) else False).any(axis=1)]

# Filter out rows with the word "None"
df = df[~(df == "None").any(axis=1)]

# Filter out rows with "Others" in the Gender column
df = df[df['Gender'] != "Others"]

# # Extract the month from 'account_creation_date' and 'last_activity_date' columns and convert to numeric format
# df['account_creation_date'] = df['account_creation_date'].astype(str).str.split('-').str[1].astype(int)
# df['last_activity_date'] = df['last_activity_date'].astype(str).str.split('-').str[1].astype(int)

# Extract the day from 'account_creation_date' and 'last_activity_date' columns and convert to numeric format
df['account_creation_date'] = df['account_creation_date'].astype(str).str.split('-').str[2].astype(int)
df['last_activity_date'] = df['last_activity_date'].astype(str).str.split('-').str[2].astype(int)

# Export the cleaned data to an Excel file
df.to_excel("Clean_Updated_Spotify_data.xlsx", index=False)

