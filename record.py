import sounddevice as sd

fs= 44100
duration=10
sd.default.samplerate = fs
myrecording=sd.rec(int(duration*fs),channels=2)
#rec returns immediatly and continue recording at the background  we use wait to return as sooon as the recording is finished
sd.wait()
print('recording is finished!')
