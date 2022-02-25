'''
Title:        Gameobjects
Author:       @benevolentimp
Description:  Here are classes for these.
'''


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
