
#customs Module

##i created a mood genterator, that randomize six moods

import random # import the random modules


#created a function:

def mood():
    mood = ["Sad", "Happy", "Relaxed", "Anger", "Joy", "Love"]
    feelings = random.choice(mood)
    print(feelings)


