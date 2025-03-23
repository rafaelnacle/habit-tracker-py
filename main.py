import os

import dotenv
from dotenv import load_dotenv
import requests

load_dotenv()
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.getenv("TOKEN")

user_params = {
    "token": TOKEN,
    "username": "rafaelnacle",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

requests.post(url=pixela_endpoint, json=user_params)