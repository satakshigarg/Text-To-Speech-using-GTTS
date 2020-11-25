from gtts import gTTS
import os

file = open("test.py", "r")
myText = file.read().replace("\n", " ")

language = "en"

speech = gTTS(text = myText, lang = language, slow = False)

speech.save("speech.mp3")
file.close()
os.system("start speech.mp3")
