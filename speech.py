#!/usr/bin/env python3
from insults import InsultGenerator
from pongBot import PongBot
import speech_recognition as sr

def main():
    engine = InsultGenerator()
    bot = PongBot()
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print ("say someting")
            audio = r.listen(source, phrase_time_limit=3)

        try:
            text = r.recognize_google(audio)
            if 'left' in text:
                bot.left()
            elif 'right' in text:
                bot.right()
            elif 'shoot' in text:
                bot.shoot()
                engine.insult()
            elif 'suck' in text:
                engine.insult()

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    main()
