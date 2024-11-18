from connect_influxdb import initialize_connection

import requests
import os

from utility import print_response
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env"))
API_TOKEN = os.getenv("INFLUXDB_TOKEN")

headers = {"Content-Type": "application/json", "Authorization" : "Token " + API_TOKEN}

data = {
    "start": "2020-01-01T00:00:00.00Z",
    "stop": "2025-01-01T00:00:00.00Z",
}

url = "http://localhost:8086/api/v2/delete?org=docs\u0026bucket=pycno_sensors"

response = requests.post(url, headers=headers, json=data)

print("Status Code", response.status_code)