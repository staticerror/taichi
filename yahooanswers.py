import urllib
import urllib2
from xml.dom import minidom

def parseQuestion(ques):            
    ques_ = {}
    for node in ques.childNodes:
        if node.nodeType == node.ELEMENT_NODE and not node.nodeName == 'Answers' :
            ques_.update(__getData(node.toxml()))
    return ques_

def __getData(node):
    i = node.find('>')
    j = node.rfind('<')
    k = node.find(' ')
    return {node[1:i]:node[i+1:j]}    

class Answers:

    def __init__(self):
        self.appid = 'YahooDemo'
    
    def questionSearch(self, params):
        """Answers questionSearch wrapper"""
        baseUrl = 'http://answers.yahooapis.com/AnswersService/V1/questionSearch?appid='+self.appid+'&'
        finalUrl = baseUrl
        for k, v in params.items():
            finalUrl = finalUrl + urllib.quote(k) +'=' + urllib.quote(v) + '&'
        finalUrl = finalUrl[:len(finalUrl) - 1]
        site = urllib2.urlopen(finalUrl)
        xmlDoc = minidom.parse(site)
        questions = xmlDoc.getElementsByTagName('Question')
        qList = []
        for ques in questions:
            qList.append(parseQuestion(ques))
        answers = xmlDoc.getElementsByTagName('Answers')
        for ans in answers:
            qList.append(parseQuestion(ans))
        return qList
       
    
    def getByCategory(self, params):
        """Answers getByCategory wrapper"""
        baseUrl = 'http://answers.yahooapis.com/AnswersService/V1/getByCategory?appid='+self.appid+'&'
        finalUrl = baseUrl
        for k, v in params.items():
            finalUrl = finalUrl + urllib.quote(k) +'=' + urllib.quote(v) + '&'
        finalUrl = finalUrl[:len(finalUrl) - 1]
        print finalUrl
        site = urllib2.urlopen(finalUrl)
        xmlDoc = minidom.parse(site)
        questions = xmlDoc.getElementsByTagName('Question')
        qList = []
        for ques in questions:
            qList.append(parseQuestion(ques))
        return qList    
    
    def getByUser(self, params):
        """Answers getByUser wrapper"""
        baseUrl = 'http://answers.yahooapis.com/AnswersService/V1/getByUser?appid='+self.appid+'&'
        finalUrl = baseUrl
        for k, v in params.items():
            finalUrl = finalUrl + urllib.quote(k) +'=' + urllib.quote(v) + '&'
        finalUrl = finalUrl[:len(finalUrl) - 1]
        print finalUrl
        site = urllib2.urlopen(finalUrl)
        xmlDoc = minidom.parse(site)
        questions = xmlDoc.getElementsByTagName('Question')
        qList = []
        for ques in questions:
            qList.append(parseQuestion(ques))
        return qList      
   
   
    def getQuestion(self, params):
        """Answers getByUser wrapper"""
        baseUrl = 'http://answers.yahooapis.com/AnswersService/V1/getQuestion?appid='+self.appid+'&'
        finalUrl = baseUrl
        for k, v in params.items():
            finalUrl = finalUrl + urllib.quote(k) +'=' + urllib.quote(v) + '&'
        finalUrl = finalUrl[:len(finalUrl) - 1]
        print finalUrl
        site = urllib2.urlopen(finalUrl)
        xmlDoc = minidom.parse(site)
        questions = xmlDoc.getElementsByTagName('Question')
        qList = []
        for ques in questions:
            qList.append(parseQuestion(ques))
        answers = xmlDoc.getElementsByTagName('Answer')
        for ans in answers:
            qList.append(parseQuestion(ans))        
        return qList   

            
if __name__ == '__main__':
    app = Answers()
    app.appid = "e0U05XjV34HKgxTrrFSZORdBbZPvFdBNR1gx1rd9vsnGc1ph2LjV3kQlUpObW8cSBPc-"
    print app.questionSearch({'query':'cats', 'search_in':'best_answer'})
    #print len(app.getByCategory({'category_id':'396546304'}))
    #print app.getByUser({'user_id':'HPsA6va4aa'})
    #20070331070321AAlyopp
    
