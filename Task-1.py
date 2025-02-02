import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Set environment variables for PySpark
os.environ['PYSPARK_PYTHON'] = 'python'  # Set to your Python executable
os.environ['PYSPARK_DRIVER_PYTHON'] = 'python'  # Set to your Python executable
os.environ['HADOOP_HOME'] = 'C:/path/to/winutils'  # Set this if you have winutils.exe

# Initialize Spark session
spark = SparkSession.builder \
    .appName("NYC Taxi Zone Analysis") \
    .getOrCreate()

# Set log level to ERROR to avoid unnecessary logs
spark.sparkContext.setLogLevel("ERROR")

# Load the dataset (use raw string or forward slashes)
file_path = r"W:\CODETECH\taxi_zone_lookup.csv"  # Use raw string to avoid escape sequence issues
try:
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")
    spark.stop()
    exit()

# Print schema and show data
print("Schema of the dataset:")
df.printSchema()

print("First 5 rows of the dataset:")
df.show(5)

# Perform basic analysis
print("\nBasic Analysis:")

# 1. Total number of records
total_records = df.count()
print(f"Total number of records: {total_records}")

# 2. Count of zones in each borough
borough_zone_count = df.groupBy("Borough").agg(count("*").alias("Zone_Count")).orderBy(col("Zone_Count").desc())
print("\nNumber of zones in each borough:")
borough_zone_count.show()

# 3. List of unique service zones
service_zones = df.select("service_zone").distinct()
print("\nUnique service zones:")
service_zones.show()

# 4. Count of zones in each service zone
service_zone_count = df.groupBy("service_zone").agg(count("*").alias("Zone_Count")).orderBy(col("Zone_Count").desc())
print("\nNumber of zones in each service zone:")
service_zone_count.show()

# Stop the Spark session
spark.stop()
print("Spark session stopped.")