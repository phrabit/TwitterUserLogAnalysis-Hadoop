# TwitterUserLogAnalysis-Hadoop
2022 ITM DB_WEB Hadoop Project - User analysis from Twitter log data

## Introduction

- Team5
> Data Collecting : Emilie Greeker
> 
> Data Engineering : Jooseung Lee
> 
> Data Analysis : Suho Lee ✌️
> 
> Web : Jaeyou Lee


- Term
> 2022 1st semester of ITM Programme
> 05/01 ~ 05/31

- Got an A+ grade on this lecture and high score on project as well 💯


## ✅ Collecting log data from twitter

- Original Plan
>  Flume : Connection and Storage
>  Flume Client And Agent
>  Obstacles

- New Plan
> Combination with C#
>
> Microsoft.Net.Http

- API testing with Postman

![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/edfd1a38-e59c-4bb4-abc5-11c41ed99404)

- C# Script

> Flume Client Substitute
> 
> Quick and Effective collection
>
> ![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/33cf35c5-e207-4aee-8ad2-132c8221efea)

- Result of log data collection

> 1018 user log data files
>
> 1,000,000 user log data in JSON format.
>
> ![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/d2425d15-335e-47e7-b183-dd74f19f7804)


## ✅ Hadoop Clustering with GCP VM instances

> 1. Name Node
>
> 2. Resource Manager
>
> 3. Worker Nodes
>
> ![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/851f6c72-6ba3-4a5f-87e9-c61a97700dbd)

### Installation

hadoop / Java /Setting Environment Variables

### Start Spark
- Used to start the Spark master on the name node. 
![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/75344f87-d06a-4cde-84ce-7e4555e2a0f7)


- Used to start a Spark worker on each worker node.
![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/3d829506-4c15-42c0-9110-e2e42532ca78)


### load
> local - worker node3 instance local - put HDFS

![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/ec52db89-73ad-432e-b6d4-6a9d071a141f)


### PySpark
- Result of Pyspark(Partitioned) => Bringing out to local

![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/237244ac-d4e5-48df-8f77-28ef76ab18f8)

![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/1447db88-5695-43ef-ad54-ffd5ce33515e)

![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/1037c05a-4e2a-46a9-ab32-bee6da5687bd)


---

## ✅ Data Analysis

<strong>1. Average ‘Tweet count’ by time of day</strong>

Based on the analysis of Twitter log data, which indicates that most users upload tweets between 20:00 PM and 24:00 PM.

- Optimal Timing: 
> it is recommended to schedule important or high-engagement tweets during this time frame.

- Targeted Content:
> Analyzing the type of content that performs well during this time period can provide insights for creating targeted content

- Engage with Users:
> Monitor relevant hashtags, join conversations, and respond to user queries or comments in real-time.

![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/cc945fa1-0c99-4194-86f9-795f02b880a6)


<strong>2. tweet_count and followers_count</strong>

It was found that most users had a value of 0 in tweet_count and followers_count. This is followed by users with a value of 1-10, followed by users with a value of 100 or greater.

- Targeting new users:
> Users with a tweet_count and followers_count of 0 are identified as users who are not yet actively tweeting or have many followers.

- Build a small community:
> Users with a tweet_count and followers_count of 1-10 have already posted a few tweets and have a small number of followers. A small community can be formed through communication and interaction with these users.

- Target influential users: 
> you can encourage their support and sharing through collaboration, partnership, brand mention, etc.

![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/ce098b5d-f02b-4490-a542-bb65d56cc339)


<strong>3. Location Analysis</strong>

> prepare to make heat-map for each continent
> Before done, Location should be converted into 'latitude' and longitude' based on location

![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/c984c20a-7f16-416b-b2c1-220168528e98)


<strong>4. User Language Data Analysis</strong>

> Using word-cloud

![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/26bcbb12-6031-4653-9795-6fcbb919db11)

---

### ✅ Web by using 'Flutter' & 'Firebase'

![image](https://github.com/phrabit/TwitterUserLogAnalysis-Hadoop/assets/70180003/12e83588-2f77-438c-9ce8-c53d4b2f057c)


