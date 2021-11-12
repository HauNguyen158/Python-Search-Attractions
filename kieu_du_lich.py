from chatterbot.logic import LogicAdapter
from flask import Flask, render_template, request
from chatterbot.conversation import Statement
import requests
from datetime import date, timedelta
import json
import crawl_diadiem as baibien

class Kieu(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        ().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['chùa', 'di tích', 'biển']
        if any(x in statement.text for x in words):
            baibien.set_Tinh("None")
            baibien.set_Kieu(str(statement))
            return True
        else:
            words = baibien.lay_Tinh()
            if any(x in statement.text for x in words):
                baibien.set_Tinh(str(statement))
                return True
            else:
                return False

    def process(self, input_statement, additional_response_selection_parameters):
        
        if baibien.get_Tinh() == "None":
            output = '{"type" : "text", "data" : "' + "Bạn muốn tìm ở tỉnh(thành phố) nào ạ ?" + '"}'
      
            response_statement = Statement(text=output)
        else:
            kieu = baibien.get_Kieu()
         

            if kieu == "biển":
                output = baibien.Lay_DS_Bien(str(input_statement))
            if kieu == "di tích":
                output = baibien.Lay_Di_Tich(str(input_statement))
            if kieu == "chùa":
                output = baibien.Lay_DS_Chua(str(input_statement))

            t = '{"type" : "table", "data" : ["'
            for i in range(len(output)):
                t += output[i] + '","'
            t = t[:len(t) - 2]
            t = t + "]}"
    
            response_statement = Statement(text=t)


        response_statement.confidence = 1
        return response_statement


