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


# newWord = input("Give me another word. ")
# translate(newWord)
# readFile()

cosas["seeds"] = "semillas"
# print(cosas)

# addWords()
readFile() 
