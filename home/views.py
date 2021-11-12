from typing import no_type_check
from django.shortcuts import render
from django.http import HttpResponse, request
from django.urls.conf import path
from .models import DoanhThu, SoLuongKhach, Setting
import json
from django.core import serializers
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, session, redirect, url_for, escape, request

admin = None
botname = None
data_doanhthu = None
data_soluongkhach = None

def index(request):
    return render(request, 'pages/suggestions.html', {'botname' : botname, 'admin' : admin})

def solieu(request):
    return render(request, 'pages/home.html', {'guests' : json.dumps(data_soluongkhach), 
    'revenue' : json.dumps(data_doanhthu), 'botname' : botname, 'admin' : admin})



def get_bot_response(request):
    userInput=request.GET.get('msg')
    return HttpResponse(str(chatbot.get_response(userInput)))


def data_type_handling(data):
    tmpJson = serializers.serialize("json", data)
    tmpObj = json.loads(tmpJson)

    for i in range(len(tmpObj)):
        tmpObj[i] = tmpObj[i]["fields"]
    return tmpObj


def __init__():
    global admin,botname, data_doanhthu, data_soluongkhach
    
    setting = data_type_handling(Setting.objects.all())
    admin = setting[0]['admin']
    botname = setting[0]['botname']
    data_doanhthu = data_type_handling(DoanhThu.objects.all())
    data_soluongkhach = data_type_handling(SoLuongKhach.objects.all())

khoitao = __init__()

chatbot = ChatBot(botname, 
	#storage_adapter='chatterbot.storage.SQLStorageAdapter',
	logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Tôi không hiểu.',
            'maximum_similarity_threshold': 0.8
        },
        {
            "import_path": "chatterbot.logic.MathematicalEvaluation",

        },
        {
            "import_path": "chatterbot.logic.UnitConversion",

        },
        {
            "import_path": "profanity_adapter.ProfanityAdapter",

        },
        {
            "import_path": "chat.Chat",

        },
        
        {
            "import_path": "huongdandulich.HuongDan",

        },
        {
            "import_path": "kieu_du_lich.Kieu",

        }
    ],
)