import voice_listener
import activities
import pyttsx3


while(True):
    audio = voice_listener.listen()
    if audio != False:
        if voice_listener.isActive(audio):
            activities.check_activities(audio)
