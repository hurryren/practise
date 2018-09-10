from django.shortcuts import render
from .models import Message
from django.http import HttpResponse
# Create your views here.


def get_message(request):
    return render(request,'msg.html')


def get_content(request):

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        o_message = Message()
        o_message.name = name
        o_message.email = email
        o_message.text = message

        o_message.save()
        return HttpResponse('<h2>保存成功！</h2>')
    else:
        return render(request, 'msg.html')