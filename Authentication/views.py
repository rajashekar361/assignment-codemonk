from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Authentication.models import Details
from Authentication.serializers import SignUpSerializer
from datetime import date
import hashlib
import datetime

from djangoproject.settings import JWT_SECRET_KEY
# Create your views here.


@csrf_exempt
def SignUpApi(request):
    if request.method == "POST":
        SignUp_data = JSONParser().parse(request)
        SignUp_data['createdAt'] = date.today().strftime('%Y-%m-%d')
        SignUp_data['modifiedAt'] = None
        SignUp_data['Pwd'] = hashlib.sha1(
            SignUp_data['Pwd'].encode()).hexdigest()
        print(SignUp_data)
        SignUp_data_serializer = SignUpSerializer(data=SignUp_data)
        if SignUp_data_serializer.is_valid():
            SignUp_data_serializer.save()
            return JsonResponse("Signup successful", safe=False)
        return JsonResponse("Signup failed", safe=False)
    else:
        return JsonResponse("Wrong method(Try POST)", safe=False)


@csrf_exempt
def LoginApi(request):
    if request.method == "GET":
        Data = JSONParser().parse(request)
        Org_data = Details.objects.get(Email=Data['Email'])
        Data_deSerailzer = SignUpSerializer(Org_data)
        if (Data_deSerailzer.data['Pwd'] == hashlib.sha1(Data['Pwd'].encode()).hexdigest()):
                #token = jwt.encode({'user': Data['Email'], 'exp': datetime.datetime.utcnow(         ) + datetime.timedelta(minutes=30)}, JWT_SECRET_KEY)
            return JsonResponse("Successfull", safe=False)
        return JsonResponse("Invalid Credentials", safe=False)
    else:
        return JsonResponse("Wrong method(Try GET)", safe=False)
