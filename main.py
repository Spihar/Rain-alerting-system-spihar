import requests
from twilio.rest import Client

account_sid ='_'
auth_token='_'
client=Client(account_sid,auth_token)


api_key = '_'
url = 'https://api.openweathermap.org/data/2.5/forecast'
lat = 13.082680
lon = 80.270721


data = {
    'lat': lat,
    'lon': lon,
    'appid': api_key,
    'cnt': 3,
    'units': 'metric'
}
response = requests.get(url=url, params=data)
print(response.url)
print(response)
weather_data = response.json()
#print(weather_data)
weather_id=[]
for i in range(0,3):
    weather_id.append(weather_data['list'][i]['weather'][0]["id"])
print(weather_id)
umbrella=False
for j in weather_id:
    if j<800:
        umbrella=True
    else:
        pass
print(umbrella)
if umbrella:
    message=client.messages.create(
        body="take an ambrella",
        from_="+14159093031",
        to="+917989029388"
    )
print(message.body)

