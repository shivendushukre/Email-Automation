from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Detail
import urllib.request
import json


def SendMail(request):

    if request.method == 'POST':
        data = request.POST
        email = data['email']
        rname = data['name']
        city = data['city']
        user = Detail(email=email, receiver_name=rname, city=city)
        user.save()
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city+'&units=metric&appid=20f2f953dcae98493703f7e98b404ae4').read()

        # convert  json file into python dictionary
        list_of_data = json.loads(source)
        # getting temp from the dictionary
        temp = str(list_of_data['main']['temp'])

        if int(float(temp)) < 15:
            emoji = '\U0001F976'
        if int(float(temp)) < 30 and int(float(temp)) > 15:
            emoji = '\U0001F642'
        if int(float(temp)) >= 30:
            emoji = '\U0001F975'
        # mail contents
        subject = f'Hi {rname}, interested in our services'
        msg = f'Temperature of the city is {temp} {emoji}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subject, msg, email_from,
                  recipient_list, fail_silently=False)

        return HttpResponse('Email Sent')
    return render(request, 'app/index.html')
