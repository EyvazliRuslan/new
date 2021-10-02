from gtts import gTTS
import os


tts = gTTS(text='Hi my world',lang='en')
tts.save('hello.mp3')
os.system('hello.mp3')