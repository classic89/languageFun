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
  language = readFile("iso_language_codes.json")
  return iso_code[language]

def getLanguagefor(code):
  language = readFile("language_to_codes.json")
  return language[code]

def changeToSpanish(phrase):
  print("To Español")
  mySentence = TextBlob(phrase)
  return mySentence.translate(to=getCodefor("español"))

def change(phrase, toLanguage):
  mySentence = TextBlob(phrase)
  return mySentence.translate(to=getCodefor(toLanguage))

mySentence = TextBlob('I love you')
originalcode = mySentence.detect_language()
print(originalcode)
print(getLanguagefor(originalcode))

# print("From "+getLanguagefor(originalcode)+": "+mySentence)
# changeToSpanish('I love you')
# listOfLanguages = [ "indonesia", "bahasa melayu", "tagalog", "vietnamese"]
# for each_language in listOfLanguages:
#   print("To "+each_language+" "": "+change(original, each_language))