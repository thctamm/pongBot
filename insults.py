from numpy.random import choice
import random
import os
from bingtts import Translator
import requests

class InsultGenerator:
    def __init__(self):
        self.translator = Translator('299c8e517ce048588823a0bda3b4279a')

    def insult(self):
        formats = [self.steve, self.taunt, self.yoMama, self.robot]
        diss = choice(formats, 1, p=[0.20, 0.35, 0.15, 0.30])[0]()
        output = None
        while not output:
            try:
                output = self.translator.speak(diss, "en-US", "Male", "riff-16khz-16bit-mono-pcm")
            except Exception as e:
                print(e)
        with open("file.wav", "wb") as f:
            f.write(output)
        os.system('aplay ./file.wav')

    def taunt(self):
        start = ['Eat grass', 'Get wrecked', 'Bite me', 'Suck on that', 'Go make me a sandwich', 'Take a hike']
        adj_one = ["Lazy", "Stupid", "Insecure", "Idiotic", "Slimy", "Smelly", "Pompous", "Communist", "Pie-eating", "Elitist", "Drug-loving", "Butterface", "Tone deaf", "Ugly", "Creepy"]
        adj_two = ["turd", "butt", "fart", "nut", "Yale", "puke"]
        noun = ["Steve", "pilot", "canoe", "captain", "pirate", "hammer", "knob", "box", "jockey", "waffle", "goblin", "blossum", "biscuit", "clown", "socket", "monster", "hound", "dragon", "balloon"]
        return random.choice(start) + " you " + random.choice(adj_one) + " " + random.choice(adj_two) + " " + random.choice(noun)

    def yoMama(self):
        r = requests.get('http://api.yomomma.info/')
        return r.json()['joke']

    def steve(self):
        verbs = ['make weird Winnie the Pooh Halloween costumes', 'Steve', 'suck', 'throw', 'aim', 'drunk', 'play pong', 'Maintain the safety and wellbeing of countless Harvard John A. Paulson Scool of Engineering and Applied Sciences students in the Active Learning Labs through well run and organized safety training sessions.....']

        return 'You {} like Steve'.format(random.choice(verbs))

    def robot(self):
        verbs = ['Lick', 'Suck on', 'Bite', 'Grease', 'Eat']
        adjs = ['rusty', 'shiny', 'electric', 'robotic', 'mechanical']
        nouns = ['CPU', 'screws', 'ass', '20-80s', 'servos', 'micro-controller', 'gears']
        return random.choice(verbs) + ' my ' + random.choice(adjs) + ' ' + random.choice(nouns)
