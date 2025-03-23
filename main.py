import os

import dotenv
from dotenv import load_dotenv
import requests

load_dotenv()

USERNAME = "rafaelnacle"
TOKEN = os.getenv("TOKEN")

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
    "id": "drawing",
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

