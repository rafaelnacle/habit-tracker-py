import os
from dotenv import load_dotenv
from datetime import datetime
import requests

load_dotenv()

USERNAME = "rafaelnacle"
TOKEN = os.getenv("TOKEN")
GRAPH = "drawing"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create the USER
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH,
    "name": "Drawing Graph",
    "unit": "times",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create the graph
# requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# https://pixe.la/v1/users/rafaelnacle/graphs/drawing.html

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

# yesterday = datetime(year=2025, month=3, day=22)
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many times did you draw today? "),
}

# Create a pixel
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "1"
}

# Update quantity
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"

# delete pixel from today
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)