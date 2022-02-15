'''
Title:        TextAdventure
Author:       @benevolentimp
Description:  A simple text-based game (in console).
'''
from sys import exit

## -¤- ##

class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self

  def get_desc(self):
    return self.class_name + "\n" + self.desc

class Goblin(GameObject):
    def __init__(self, name):
      self.class_name = "goblin"
      self.health = 3
      self._desc = "A foul yet somehow cute creature"
      super().__init__(name)
    
    @property
    def desc(self):
      # Use match-case with 3.10.*!!!
      if (self.health >= 3):
        return self._desc
      elif (self.health == 2):
        health_line = "It only has surface-wounds and unfazed."
      elif (self.health == 1):
        health_line = "Its showing some weakness and bloodied!"
      elif (self.health <= 0):
        health_line = "It is laying unconscious."
      return self._desc + "\n" + health_line
    
    @desc.setter
    def desc(self, value):
      self._desc = value

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
