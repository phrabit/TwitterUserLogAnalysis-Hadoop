from pyspark.sql import SparkSession
from pyspark.sql.functions import explode

# Initialize SparkSession
spark = SparkSession.builder.master('yarn').getOrCreate()

# Define users
users = ["BarackObama", "Christiano", "ElonMusk", "justinbieber","katyperry","KimKardashian","ladygaga","rihanna","ShawnMendes","taylorswift13"]

# Create an empty DataFrame to hold all extracted languages
all_langs = spark.createDataFrame(spark.sparkContext.emptyRDD(), "string").toDF("lang")

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

            # Union the language DataFrame with the overall DataFrame
            all_langs = all_langs.union(langs)

# Write the DataFrame to a CSV file
all_langs.write.csv('hdfs://10.178.0.2:9000/result/extracted_lang_data.csv', mode='overwrite', header=True)

# Print the DataFrame of languages
all_langs.show()
