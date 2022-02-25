"""
Title:        TextAdventure
Author:       @benevolentimp
Description:  A simple text-based game (in console).
"""
from sys import exit

from classes.entities import GameObject, Goblin


## -¤- ##


## -¤- ##

def get_input():
    # Here split() divides input into words:
    command = input(": ").split()
    verb_word = command[0]

    # Use match-case with 3.10.*!!!
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))


### -¤- ###

def say(noun):
    return 'you said "{}"'.format(noun)


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return "There is no {} here.".format(noun)


def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health = thing.health - 1
            if thing.health <= 0:
                msg = "You killed the goblin!"
            else:
                msg = "You hit the {}".format(thing.class_name)
    else:
        msg = "There is no {} here".format(thing.class_name)
    return msg


### -¤- ###

verb_dict = {
    "say": say,
    "examine": examine,
    "hit": hit
}

goblin = Goblin("Bobby")

iterator = 1
while iterator == 1:
    try:
        get_input()
    except KeyboardInterrupt:
        print("Exiting...")
        exit()
