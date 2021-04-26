import json
cosas = {} 

def translate(word):
  print(cosas[word])

def addWords(): 
  x = input("Let\'s add to the dictionary. Give me a word. ")
  y = input("Give me a definition. ")
  cosas[x] = y
  fileWriter = open("spanishdictionary.json", "w")
  fileWriter.write(str(cosas))
  fileWriter.close()

def readFile():
  readFile1 = open("spanishdictionary.json")
  contents1 = readFile1.read()
  readFile1.close()
  # Manipulating a string
  # print(type(contents1))
  # print("contents1: "+contents1)
  # contents1 = str(contents1).replace("'", '"')
  # print(type(contents1))
  # cosas = contents1
  #Saves Locally here:
  cosas = json.loads(contents1)
  print("Type:"+str(type(cosas)))
  print("Cosas: "+str(cosas))

print("Hello")
# myFile = open("spanishdictionary.json")
# myContents = myFile.read()
# myFile.close()
# 
print(cosas)

# newWord = input("Give me another word. ")
# translate(newWord)
# readFile()

cosas["seeds"] = "semillas"
# print(cosas)

# addWords()
readFile() 
