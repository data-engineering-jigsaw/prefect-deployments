import requests
from prefect.server.schemas.schedules import IntervalSchedule
from prefect import flow, task

@task
def find_receipts(name):
    url = "https://data.texas.gov/resource/naix-2893.json"
    response = requests.get(url, params = {'taxpayer_name': name})
    return response.json()[:1]

@flow
def get_restaurants(url: str):
    receipts = find_receipts(url)
    return receipts

get_restaurants("HONDURAS MAYA CAFE & BAR LLC")

# if __name__ == "__main__":
#     get_restaurants.serve(
#         name="get-restaurants-deployment",
#         schedule=IntervalSchedule(interval=120),
#         parameters={'url': "HONDURAS MAYA CAFE & BAR LLC"}
#         )
    

