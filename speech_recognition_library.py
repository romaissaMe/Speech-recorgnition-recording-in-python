# -*- coding: utf-8 -*-
"""speech-recognition-library.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w6CpmL8ZdV0XhafvQSxtEJSUDW6Iw_ha
"""

!pip install pyttsx3

!pip install SpeechRecognition

import speech_recognition as sr

r=sr.Recognizer()

#the context manager reads the file and store the content into harvard audiofile instance
harvard = sr.AudioFile('/audio_files_harvard.wav')

with harvard as source:
  #The record() method records the data from the entire file into an AudioData instance
  #The adjust_for_ambient_noise() method reads the first second of the file stream and calibrates the recognizer to the noise level of the audio
  r.adjust_for_ambient_noise(source,duration=0.5)
  audio = r.record(source)

#invoke google recognizer API
r.recognize_google(audio)

#The record() method with durtion attribute when used inside a with block, always moves ahead in the file stream
with harvard as source:
     audio1 = r.record(source, duration=3)
     audio2 = r.record(source, duration=2)

r.recognize_google(audio1),r.recognize_google(audio2)

#recognize_google() returns a dictionary with the key 'alternative' that points to a list of possible transcripts when ading show all instead of returning the most likely transcription
harvard = sr.AudioFile('/audio_files_harvard.wav')

with harvard as source:
  r.adjust_for_ambient_noise(source,duration=0.5)
  audio = r.record(source)
 
r.recognize_google(audio,show_all=True)

!pip install PyAudio

with sr.Microphone() as source2:
  print('silence ...')
  r.adjust_for_ambient_noise(source2)
  print('speak please!')
  audio2=r.listen(source2)
  text=r.recognize_google(audio2)
  print(text.lower())