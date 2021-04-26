import json
from textblob import TextBlob

def readFile(filename):
  readFile = open(filename)
  contents = readFile.read()
  readFile.close()
  dictionary = {}
  dictionary = json.loads(contents)
  return dictionary

def getLanguagefor(code):
  language = readFile("isoCodes_to_language.json")
  return language[code]

mySentence = TextBlob('I love you')
originalcode = mySentence.detect_language()
print("From "+getLanguagefor(originalcode))