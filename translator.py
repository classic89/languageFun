import json
from textblob import TextBlob


def readFile(filename):
  readFile = open(filename)
  contents = readFile.read()
  readFile.close()
  dictionary = {}
  dictionary = json.loads(contents)
  return dictionary

def getCodefor(language):
  iso_code = readFile("language_to_codes.json")
  return iso_code[language]

def change(phrase, toLanguage):
  mySentence = TextBlob(phrase)
  return mySentence.translate(to=getCodefor(toLanguage))

mySentence = TextBlob('I love you')
originalcode = mySentence.detect_language()

print("From English"+": "+str(mySentence))

listOfLanguages = [ "italiano", "español", "français", "deutsch"]
for each_language in listOfLanguages:
  print(str(change('In', each_language))+" "+each_language.capitalize()+" : "+str(change('I love you', each_language)))