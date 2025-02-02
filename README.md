# Data_Analysis
*COMPANY* : CODTECH IT SOLUTIONS
*NAME* : JASVANTH VARMA MUPPALA
*INTERN ID* : CT08ORY
*DOMAIN* : DATA ANALYSIS
*DURATION* : 4 WEEKS
*MENTOR* : NEELA SANTOSH

PROJECT DESCRIPTION : NYC TAXI ZONE ANALYSIS USING PYSPARK 

This project demonstrates how to perform data analysis on a large dataset using PySpark, a powerful distributed computing framework. The dataset used in this project is the NYC Taxi Zone Lookup dataset, which contains information about taxi zones in New York City, including their location IDs, boroughs, zone names, and service zones.

The project is implemented in Python using VS Code as the development environment. Below is a detailed description of the project, its objectives, and the steps performed in the code.

What is the Project About?
The goal of this project is to:

1) Load and analyze the NYC Taxi Zone Lookup dataset using PySpark.

2) Perform basic data analysis to derive insights about the dataset.

3) Demonstrate how PySpark can be used to handle large datasets efficiently in a distributed computing environment.

What Does the Code Do?
The code performs the following tasks:

1. Environment Setup
Sets up the necessary environment variables for PySpark to work correctly on a Windows system.

Initializes a SparkSession, which is the entry point for using PySpark.

2. Loading the Dataset
Loads the dataset (taxi_zone_lookup.csv) into a PySpark DataFrame.

Uses a try-except block to handle errors during dataset loading.

3. Data Exploration
Prints the schema of the dataset to understand its structure.

Displays the first 5 rows of the dataset to get a glimpse of the data.

4. Data Analysis
Total Records: Counts the total number of records in the dataset.

Zones per Borough: Groups the data by Borough and counts the number of zones in each borough.

Unique Service Zones: Lists all unique values in the service_zone column.

Zones per Service Zone: Groups the data by service_zone and counts the number of zones in each service zone.

5. Stopping the Spark Session
Stops the Spark session to release resources after the analysis is complete.

Technologies and Tools Used
PySpark: A Python API for Apache Spark, used for distributed data processing.

Python: The programming language used to write the script.

VS Code: The integrated development environment (IDE) used for writing and running the code.

CSV Dataset: The NYC Taxi Zone Lookup dataset, which is a structured file containing taxi zone information.

Key Features of the Project
Scalability: PySpark allows the analysis to scale to large datasets by distributing the workload across multiple nodes in a cluster.

Ease of Use: The code is written in Python, making it accessible to data analysts and engineers familiar with the language.

Error Handling: The script includes error handling to ensure smooth execution even if issues arise (e.g., incorrect file paths).

Insights: The analysis provides valuable insights into the distribution of taxi zones across boroughs and service zones.
