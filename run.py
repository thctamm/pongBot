#!/usr/bin/env python3
from insults import InsultGenerator
from pongBot import PongBot

def main():
    engine = InsultGenerator()
    bot = PongBot()
    inp = input("")
    while inp != "q":
        if inp == 'a':
            bot.left()
        elif inp == 'd':
            bot.right()
        elif inp == 'w' or inp == 's':
            bot.shoot()
            engine.insult()
        inp = input("")

if __name__ == "__main__":
    main()
