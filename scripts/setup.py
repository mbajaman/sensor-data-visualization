# Script to add API token and create a .env file
from utility import create_file

print("This script will help you add your API tokens and create a .env file for you.\n")
print("It will also help you configure files to help setup your Docker containers")

def prompt_user(prompt, default):
    user_input = input(f"{prompt} [{default}]: ")
    # Return the user's input if they provide one, otherwise return the default
    return user_input if user_input.strip() else default

PYCNO_API_TOKEN = prompt_user("Enter Pycno API Token (Required): ", "N/A")
INFLUXDB_TOKEN = prompt_user("Enter InfluxDB API Token (Required): ", "N/A")

file_content = "PYCNO_API_TOKEN=" + PYCNO_API_TOKEN + "\n"
file_content += "INFLUXDB_TOKEN=" + INFLUXDB_TOKEN + "\n"

create_file(".env", "", file_content)

INFLUXDB_ADMIN_USERNAME = prompt_user("Enter admin username", "admin")
INFLUXDB_ADMIN_PASSWORD = prompt_user("Enter admin username", "password")
INFLUXDB_ADMIN_TOKEN = prompt_user("Enter admin username", "MyInitialAdminToken0==")

create_file(".env.influxdb2-admin-username", "../db/env/", INFLUXDB_ADMIN_USERNAME)
create_file(".env.influxdb2-admin-password", "../db/env/", INFLUXDB_ADMIN_PASSWORD)
create_file(".env.influxdb2-admin-token", "../db/env/", INFLUXDB_ADMIN_TOKEN)

