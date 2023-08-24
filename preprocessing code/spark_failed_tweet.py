from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import explode

# Initialize SparkSession
spark = SparkSession.builder.master('yarn').getOrCreate()

# Define users
users = ["BarackObama", "Christiano", "ElonMusk", "justinbieber","katyperry","KimKardashian","ladygaga","rihanna","ShawnMendes","taylorswift13"]

# Initialize an empty list to hold all extracted languages
all_langs = []

# Loop through each user
for user in users:
    # Loop through each log file
    for i in range(1, 6):
        file_path = f'hdfs://10.178.0.2:9000/logdata2/{user}/log{i}.txt'
        
        # Read the JSON file into a DataFrame
        df = spark.read.json(file_path)

        # Check if 'data' is in the DataFrame's columns
        if 'data' in df.columns:
            # Extract the language from each entry in the JSON data
            langs = df.select(explode(df.data.lang).alias("lang"))

            # Append the languages to the overall list
            all_langs += [row['lang'] for row in langs.collect()]

# Convert the list of languages to a DataFrame
df_langs = spark.createDataFrame([Row(lang=l) for l in all_langs])

# Write the DataFrame to a CSV file
df_langs.write.csv('hdfs://10.178.0.2:9000/result/extracted_lang_data.csv', mode='overwrite', header=True)

# Print the DataFrame of languages
df_langs.show()


"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
import os 

# Create Spark session
spark = SparkSession.builder.appName('twitterUserLogs').master('yarn').getOrCreate()

# Path to your directory
path = "hdfs://10.178.0.2:9000/logdata/"

# Initialize an empty DataFrame to hold all extracted DataFrames
all_data_df = None

# Iterate over files
for i in range(1, 506):
    # Get file name
    file_name = f'log.{i}.txt' if i != 1 else 'log.1.txt'
    
    # Load the file into a DataFrame
    df = spark.read.json(os.path.join(path, file_name))
    
    # Filter out non-null corrupt records
    df = df.filter(df._corrupt_record.isNull())

    # Cache the DataFrame
    df.cache()
    
    if 'data' in df.columns:
        # Explode the 'data' column
        df = df.select(explode(df.data).alias('data')).select('data.*')
        
        # Explode 'public_metrics' column
        df = df.select('*', 'public_metrics.*').drop('public_metrics')
        
    # Append to the all_data_df
    if all_data_df is None:
        all_data_df = df
    else:
        all_data_df = all_data_df.union(df)

# Fill null values with an empty string
all_data_df = all_data_df.na.fill('')

# Select the required columns
selected_columns = ["created_at", "followers_count", "tweet_count","location"]
output_df = all_data_df.select(selected_columns)

# Write the output DataFrame to a CSV file
output_df.write.csv("hdfs://10.178.0.2:9000/result/extracted_data.csv", mode='overwrite', header=True)
"""