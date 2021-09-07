from pyspark.sql import SparkSession

if __name__ == "__main__":
    
    session = SparkSession.builder.appName("spark_connection").getOrCreate()
    dataFrameReader = session.read
    
    responses = dataFrameReader \
        .option("header", "true") \
        .option("inferSchema", value=True) \
        .csv("s3n://nyc-tlc/trip data/yellow_tripdata_2019-05.csv")

    print(" --- our schema --- ")
    responses.printSchema()