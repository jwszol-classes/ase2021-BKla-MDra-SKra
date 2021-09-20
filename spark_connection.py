from pyspark.sql import SparkSession, functions  
import pyspark.sql.functions as F
from pyspark.sql.types import DoubleType, TimestampType
import matplotlib.pyplot as plt
import numpy as np
import boto3	# Amazon's aws library for python 3

year_range = (2019, 2020)
month_range = ((5, 12), (1, 5))
colors = ("yellow", "green")

def get_path(color, year, month):
    return f"s3n://nyc-tlc/trip data/{color}_tripdata_{year}-{month}.csv"

def get_avg_speed_dict():
    avg_speed = {c: [] for c in colors}

    for color in colors:
        for i in range(len(year_range)):
            year = year_range[i]
            for m in range(month_range[i][0], month_range[i][1]+1):
                month = "0" + str(m) if m<10 else str(m)
                path = get_path(color, year, month)
                print(f"color: {color}")
                print(f"year: {year}")
                print(f"month: {month}")
                print(f"path: {path}")
                avg_speed[color].append(calc_speed(path))
    return avg_speed


def calc_speed(path):
    spark = SparkSession.builder.appName("spark_connection").getOrCreate()

    if "green" in path:
        df = (
            spark.read.option("delimiter", ",")
            .csv(
                path,
                header=True,
            )
            .select("lpep_pickup_datetime", "lpep_dropoff_datetime", "trip_distance")
        )
        df = df.withColumnRenamed("lpep_pickup_datetime", "pickup")
        df = df.withColumnRenamed("lpep_dropoff_datetime", "dropoff")
        df = df.withColumnRenamed("trip_distance", "distance")
    else:
        df = (
            spark.read.option("delimiter", ",")
            .csv(
                path,
                header=True,
            )
            .select("tpep_pickup_datetime", "tpep_dropoff_datetime", "trip_distance")
        )
        df = df.withColumnRenamed("tpep_pickup_datetime", "pickup")
        df = df.withColumnRenamed("tpep_dropoff_datetime", "dropoff")
        df = df.withColumnRenamed("trip_distance", "distance")

    # Convert columns to appropriate datatypes and SI metrics
    df = df.withColumn("distance", df["distance"].cast(DoubleType()))
    df = df.withColumn("distance", df["distance"]*1.60934) # miles to km
    df = df.withColumn("pickup", df["pickup"].cast(TimestampType()))
    df = df.withColumn("dropoff", df["dropoff"].cast(TimestampType()))

    # Get time of taxi rides in km/h
    df = df.withColumn("time_s", df["dropoff"].cast("long")- df["pickup"].cast("long"))
    df = df.withColumn("time_h",df["time_s"]/3600)

    # Remove outliers
    df = df.filter(df["distance"] > 0)
    df = df.filter(df["distance"] < 50)
    df = df.filter(df["time_h"] > 0)
    df = df.filter(df["time_h"] < 5)

    # Get speed and remove outliers
    df = df.withColumn("speed_km_h",df["distance"]/df["time_h"])
    df = df.filter(df["speed_km_h"] < 80)

    # Get average speed
    avg_speed = df.groupBy().avg("speed_km_h").collect()[0]
    return avg_speed[0]


def plot_avg_speed(avg_speed_dict):
    labels = ["may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "jan", "feb", "mar", "apr", "may"]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    print(len(avg_speed_dict["green"]))
    print(len(avg_speed_dict["yellow"]))
    bar1 = ax.bar(x - width/2, avg_speed_dict["green"], width, label="Green Taxi speed", color = "green")
    bar2 = ax.bar(x + width/2, avg_speed_dict["yellow"], width, label="Yellow Taxi speed", color = "yellow")
    #Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("Avarage speed")
    ax.set_title("Avarage speed of taxis each moth")
    ax.set_xticks(x)

    ax.set_xticklabels(labels)
    ax.legend()

    ax.bar_label(bar1, padding=3)
    ax.bar_label(bar2, padding=3)

    fig.tight_layout()

    plt.show()

    plt.savefig("taxi_chart.png")
    # create a connection to s3
    s3 = boto3.resource("s3")

    # you need a bucket, make one and put its name here
    bucket = "firstbucketseba"

    image_name = "taxi_chart.png"
    plt.savefig(image_name)

    # upload image to aws s3
    # warning, the ACL here is set to public-read
    img_data = open(image_name, "rb")
    s3.Bucket(bucket).put_object(Key=image_name, Body=img_data,
                                 ContentType="image/png", ACL="public-read")

    # Generate the URL to get 'key-name' from 'bucket-name'
    url = "http://" + bucket + ".s3.amazonaws.com/" + image_name
    print(url)


if __name__ == "__main__":
    avg_speed_dict = get_avg_speed_dict()
    plot_avg_speed(avg_speed_dict)
