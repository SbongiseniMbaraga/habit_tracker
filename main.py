import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "thekingofheroessbo"
USERNAME = "sbo"
GRAPH_ID = "graph1"

user_params = {
    "token": "thekingofheroessbo",
    "username": "sbo",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#creates new account (done)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#create pixel
pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

#yesterdays date
today = datetime(year=2021, month=3, day=28)

post_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.74",
}

# response = requests.post(url=pixel_creation, json=post_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)