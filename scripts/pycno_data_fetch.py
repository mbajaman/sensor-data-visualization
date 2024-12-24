import os
import requests

from dotenv import load_dotenv
from pathlib import Path
from utility import print_response

load_dotenv(Path(".env"))

API_TOKEN = os.getenv("PYCNO_API_TOKEN")

def all_sensors():
    url = "https://portal.pycno.co.uk/api/v2/data/nodelist.json?TK={}".format(API_TOKEN)
    response = requests.get(url)
    print_response(response)

def single_sensor(sensor_id):
    url = "https://portal.pycno.co.uk/api/v2/data/no/{}.json?TK={}".format(sensor_id, API_TOKEN)
    response = requests.get(url)
    print_response(response)

# TODO: Collect more paremeters for more dashboards
def time_series_data(sensor_id):
    url = "https://portal.pycno.co.uk/api/v2/data/1?TK={}&UID={}&TEMP&start=2017-01-10T22:10:29.140Z&end=2024-11-17T05:00:08.493Z".format(API_TOKEN, sensor_id)
    response = requests.get(url)
    print_response(response)


def main():
    # all_sensors()
    # single_sensor("K05DA3533565051138534")
    time_series_data("K05DA3533565051138534")
    return

if __name__ == "__main__":
    main()