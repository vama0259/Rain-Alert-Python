import requests
from twilio.rest import Client

api_key = "9145fbe28d580cb16021243f33460e3a"
api_endPoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = "AC55b063fcdf65e922f40efdf5ec004ef1"
auth_token = "01dede0729bc1ffab0485c4c3d8a92bc"

parameters = {
    "lat":13.082680,
    "lon":80.270721,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(url = api_endPoint, params= parameters)

weather_data = response.json()

weather_slice = weather_data["hourly"][:12]
will_rain = False
for weather_datas in weather_slice:
    condition_code = weather_datas["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hello Mc",
        from_='+18066033454',
        to='+917728848272'
    )
    print(message.sid)