import requests
import pandas as pd
import json

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/iccstanding/team/matchtype/1"

headers = {
	"X-RapidAPI-Key": "b028ebca0emshfe16e247a04eb73p123347jsn1dce6a0470f3",
	"X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
}

df = pd.DataFrame()
response = requests.get(url, headers=headers)
response_json = response.json()

# # Load JSON data into a DataFrame
# df = pd.json_normalize(response_json['values'], sep='_')

# # Headers for the DataFrame
# headers = ['Rank', 'Code', 'Country', 'Value']

# Creating DataFrame
df = pd.DataFrame(df, columns=headers)

df.to_csv("cricketdata.csv")