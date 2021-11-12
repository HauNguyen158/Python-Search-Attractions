from chatterbot.logic import LogicAdapter
from nltk.util import pr
import talk as talk

class Chat(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        ().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        
        if talk.bow(statement.text):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
    
        output = talk.getResponse(input_statement)
        
        output = ""
  
        response_statement=Statement(output)


        response_statement.confidence = 1
        return response_statement
