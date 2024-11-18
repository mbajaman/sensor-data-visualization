# File to create line protocol output for importing data into influxdb

import json

from influxdb_client.client.exceptions import InfluxDBError

from connect_influxdb import initialize_connection
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS

write_client = initialize_connection()
bucket = "pycno_sensors"

points = [] # Array to store all point objects

with open("test-data/K05DA3533565051138534_TEMP.json", "r") as json_file:
    data = json.load(json_file)[0]

for time, value in data["values"]:
    # FOR DEBUG
    # print("Time: " + str(time) + " | Temp: " + str(value) + "\n")
    point = (
        Point("sensor")
        .tag("sensor_id", str("K05DA3533565051138534"))
        .field("temperature", float(value))
        .time(time * 1_000_000)
    )
    points.append(point)

with write_client.write_api(write_options=SYNCHRONOUS) as writer:
    try:
        writer.write(bucket="pycno_sensors", record=points)
        print(f"Imported {len(points)} points successfully")
    except InfluxDBError as e:
        print(e)