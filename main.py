import speech_recognition as sr
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source: 
        if ask: 
            alexa_speak(ask)         
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        
        except sr.UnknownValueError:
            alexa_speak('Lo siento, no te entendí')
        except sr.UnknownValueError:
            alexa_speak('Lo siento, error de conexión')
        return voice_data

def alexa_speak(audio_string):
    tts = gTTS(text=audio_string, lang='es')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'Lola' in voice_data:
        buscar = record_audio('¿Qué memes necesitas buscar?')
        url = 'https://es.memedroid.com/search?query=' + buscar
        webbrowser.get().open(url)
        alexa_speak('Es lo que encontre para: ' + buscar)
    if 'Termina' in voice_data:
        exit()
    
time.sleep(1)
alexa_speak('¿Como te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
    alexa_speak('Gracias líder supremo')
    exit()