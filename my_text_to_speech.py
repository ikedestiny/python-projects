import pyttsx3

text_speech = pyttsx3.init()

speech = input("What do you want to convert: ")
file_name = input("What do you wnat to save the file as, add .mp3: ")

text_speech.setProperty("rate", 150)
text_speech.save_to_file(speech, file_name)


text_speech.say(speech)
text_speech.runAndWait()



"""
 RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


VOLUME
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

VOICE
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

Saving Voice to a file
 On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()
"""
