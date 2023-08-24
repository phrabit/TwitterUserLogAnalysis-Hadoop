import os
import pandas as pd
import json

users = ["BarackObama", "Christiano", "ElonMusk", "justinbieber","katyperry","KimKardashian","ladygaga","rihanna","ShawnMendes","taylorswift13"]

# Initialize an empty DataFrame to hold all extracted languages
all_data_df = pd.DataFrame()

# List all .txt files in the directory
for user in users:
    txt_files = [f for f in os.listdir(f'/Users/juseung/Documents/twitter_logdata/User_Mention_timeline/{user}') if f.endswith('.txt')]
    print(txt_files)

    # Loop through each file
    for file in txt_files:
        # Read the JSON file into a DataFrame
        with open(os.path.join(f'/Users/juseung/Documents/twitter_logdata/User_Mention_timeline/{user}', file)) as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                continue

        # Extract the language from each entry in the JSON data
        for entry in data['data']:
            lang = entry['lang']

            # Append the language to the overall DataFrame
            all_data_df = all_data_df.append({'lang': lang}, ignore_index=True)
all_data_df.to_csv('/Users/juseung/Documents/lang_result.csv', index=False)
# Print the accumulated DataFrame of languages
print(all_data_df)
