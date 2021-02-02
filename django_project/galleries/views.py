from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
# Create your views here.
def test(request):
    print(request)
    print(request.GET)
    API_ENDPOINT = "https://slack.com/api/oauth.v2.access"
    # your API key here 
    code = request.GET['code']
    print(code)
    arr = code.split('.')
    my_id = arr[0] + '' + arr[1]
    # data to be sent to api 
    data = {
        'client-id':my_id,
        'client-secret':'13aab9293bf240766f0c4a367bf51dae',
        'code':code, 
        'redirect_uri':'http://localhost:8000/django/test' 
            } 
    
    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = data) 
    print(r.text)
    return HttpResponse("Done!")

@csrf_exempt
def image(request):
    print(request.POST)
    print(request.POST['img'])
    image = request.POST['img']
    print(type(image))
    print(image)
    return HttpResponse("Received")
    
