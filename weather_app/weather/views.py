from django.shortcuts import render
import json
import urllib.request
# Create your views here.
def index(request):
    city=''
    data={}
    if request.method=='POST':
        city=request.POST['city']
        if city!="":
            try:
                res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=bd7dbddd9cf36d611f60bee9f43c62ad').read()
                json_data=json.loads(res)
                data={
                    "country_code":str(json_data['sys']['country']),
                    "coordinate":str(json_data['coord']['lon'])+" "+ str(json_data['coord']['lat']),
                    "temp":round(float(json_data['main']['temp'])-273.15,2),
                    "pressure":str(json_data['main']['pressure']),
                    "humidity":str(json_data['main']['humidity']),
                    "clouds":str(json_data['clouds']['all'])
                }
            except urllib.error.HTTPError:
                data = {
                "error": "Does not exist!"
            }
    return render(request,'index.html',{'city':city,'data':data})