from dotenv import load_dotenv
from pathlib import Path

import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

load_dotenv(Path(".env"))

def initialize_connection() -> InfluxDBClient:
    token = os.getenv("INFLUXDB_TOKEN")
    org = "docs"
    url = "http://localhost:8086"

    write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    return write_client