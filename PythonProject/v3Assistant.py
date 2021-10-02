import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
# r = sr.Recognizer()

def speak(sentence) -> None :
    tts = gTTS(sentence,lang='en')
    file = 'demo.mp3'
    tts.save(file)
    playsound(file)

speak('hello')