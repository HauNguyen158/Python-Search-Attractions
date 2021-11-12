from chatterbot.logic import LogicAdapter
from flask import Flask, render_template, request
from chatterbot.conversation import Statement
import requests
from datetime import date, timedelta
import json
import crawl_diadiem as baibien

timdiachi = 0
text = ""
class HuongDan(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        ().__init__(chatbot, **kwargs)


    def can_process(self, statement):
        global timdiachi
        timdiachi = 0
    
        words = ['ở', 'đâu']
        if all(x in statement.text.split() for x in words):
            timdiachi = 1
            return True
        else:
            words =['tìm']
            if all(x in statement.text.split() for x in words):
                timdiachi = 2
                global text
                text = statement.text
                text = text[4:]
                return True
            else:
                return False

    def process(self, input_statement, additional_response_selection_parameters):
        if(timdiachi == 2):
            l = baibien.Lay_Hinh_Anh(text)
            data = '{"type" : "tt", "data" : [{"img" :['
            for i in range(len(l)):
                data += '"' + l[i] + '",'

            data = data[:len(data) - 1]
            data += '], "wiki" :['
            l = baibien.Lay_Thong_Tin(text)
            for i in range(5):
                data += '"' + l[i] + '",'

            data = data[:len(data) - 1]
            data += "]}]}"
  
            response_statement = Statement(text=data)
    
        if(timdiachi == 0):
            list_baibien = baibien.crawlData_Bien().split("\n")
            data = '{"type" : "list-dd" , "data" : ['
           
            img  = [[] for index in range(1, 10)] 
            
            for i in range(len(list_baibien)-1):
                
                data += ('{"name" : "' + list_baibien[i] + '","link" : [')
                img[i] = baibien.Lay_Hinh_Anh(list_baibien[i])
                
                for j in range(3):
                    data += '"' + img[i][j] + '",'
                   
                
                data = data[:len(data) - 1]
                data += "]},"
                
            data = data[:len(data)-1]
            data += "]}"
           
            

            response_statement = Statement(text=data)
        if(timdiachi == 0):
        
            response_statement = Statement(text={"a" : "dây là a", "b" : "đây là b"})


        response_statement.confidence = 1
        return response_statement


