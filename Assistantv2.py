from gtts import gTTS
import os
import time
from playsound import playsound


def speak(sentence):
    tts = gTTS(text=sentence,lang='en')
    file = 'sentence.mp3'
    tts.save(file)
    playsound(file)
    time.sleep(0.2)
    
def initial():
    in_sen = 'Hello, I am assistant of Ruslan'
    speak(in_sen)
    chat_sen = 'Tell your name:'
    speak(chat_sen)
    name = input('You: ')
    chat_sen = f'Welcome {name}, how can i help you'
    speak(chat_sen)
    if name == 'neri':
        chat_sen = 'Oh my godd, You are neribala '
        speak(chat_sen)
        chat_sen = 'Refrigerator repairmen'
        speak(chat_sen)
    chat_sen = 'Do you wanna chat more'
    speak(chat_sen)    
    chat_sen = input('You: ')
    if chat_sen == 'yes':
        chat(name)
    else:
        chat_sen = 'Ok maybe next time, bye bye'
        speak(chat_sen)
def chat(name):
    chat_sen =  f'my dear {name},how are you ?'
    speak(chat_sen)
    chat_sen = input('You: ')
    if chat_sen == 'good':
        chat_sen = 'I wanna see you every time like this ))'
        speak(chat_sen)
    else:
        chat_sen = 'Why??, Can i do something for you?'
        speak(chat_sen)
        chat_sen = input('You: ')
        if chat_sen == 'no':
            speak('Byeee')

initial()