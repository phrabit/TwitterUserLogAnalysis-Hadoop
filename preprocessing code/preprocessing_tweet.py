import pandas as pd
import json
import glob

# Get a list of all .txt files in the directory
txt_files = glob.glob('/Users/juseung/Documents/twitterUserLogs/*.txt')

# Initialize an empty list to hold all extracted dataframes
extracted_dfs = []
i=1
# Loop through all .txt files and extract their data
for file in txt_files:
    with open(file, 'r') as f:
        if i<506:
            data = json.load(f)
            data_df = pd.DataFrame(data['data'])

            # Extract 'created_at', 'tweet_count', and 'followers_count' from the 'data' DataFrame
            extracted_df = data_df[['created_at']].copy()
            extracted_df['tweet_count'] = data_df['public_metrics'].apply(lambda x: x['tweet_count'])
            extracted_df['followers_count'] = data_df['public_metrics'].apply(lambda x: x['followers_count'])

            # Check if 'location' exists, if not fill with 'Not Available'
            if 'location' not in data_df.columns:
                data_df['location'] = 'Not Available'

            # Select only necessary columns and create a new DataFrame
            extracted_df['location'] = data_df['location']

            # Append extracted data to the extracted_dfs list
            extracted_dfs.append(extracted_df)
            
        else:
            # Extract 'created_at', 'tweet_count', and 'followers_count' from the 'data' DataFrame
            extracted_df = data_df[['created_at']].copy()
            extracted_df['tweet_count'] = data_df['public_metrics'].apply(lambda x: x['tweet_count'])
            extracted_df['followers_count'] = data_df['public_metrics'].apply(lambda x: x['followers_count'])

            # Check if 'location' exists, if not fill with 'Not Available'
            if 'location' not in data_df.columns:
                data_df['location'] = 'Not Available'

            # Select only necessary columns and create a new DataFrame
            extracted_df['location'] = data_df['location']

            # Append extracted data to the extracted_dfs list
            extracted_dfs.append(extracted_df)

    
    print(i)
    i+=1
    

# Concatenate all extracted DataFrames into one
all_data_df = pd.concat(extracted_dfs, ignore_index=True)
#all_data_df.dropna(subset=['location'], inplace=True)
# Display the final DataFrame
print(all_data_df)
# Save the DataFrame as a CSV file
all_data_df.to_csv('/Users/juseung/Documents/extracted_data.csv', index=False)
