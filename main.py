import os

import dotenv
from dotenv import load_dotenv
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

pixel_data = {
    "date": "20250323",
    "quantity": "1",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response)