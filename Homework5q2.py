from poodle import Object, schedule, planned
from typing import Set

class Time(Object):
    time:int

class Positions(Object):
    def __str__ (self):
        if not hasattr(self, "locname"): return "unknown"
        return self.locname

class World(Object):
    cost: int
    locations: Set[Positions]

    def __int__ (self):
        return str(self.cost)

class HasPositions(Object):
    at: Positions

class Boat(HasPositions):
    pass

class Person(Time, HasPositions):
    name: str

    def __str__ (self):
        return self.name

p1 = Positions()
p1.locname = "Right"
p2 = Positions()
p2.locname = "Left"

W = World()
W.locations.add(p1)
W.locations.add(p2)
W.cost = 0

A = Person()
A.name = "1"
A.time = 1
A.at = p2

B = Person()
B.name = "2"
B.time = 2
B.at = p2

C = Person()
C.name = "5"
C.time = 5
B.at = p2

D = Person()
D.name = "8"
D.time = 8
D.at = p2

S = Boat()
S.at = p2

def toright(person1: Person,person2: Person, boat:Boat, where:Positions, world:World):
    assert person1.at == boat.at
    assert person2.at == boat.at

    person1.at = where
    person2.at = where
    boat.at = where

    world.cost = world.cost + max(person1.time, person2.time)
    return f"{person1.name} and {person2.name} moved to the Right"

def toleft(person1: Person, boat:Boat, where:Positions,world:World):
    assert person1.at == boat.at

    person1.at = where
    boat.at = where

    world.cost = world.cost + person1.time
    return f"{person1.name} moved to the Left"


print('\n'.join(x() for x in schedule(methods=[toright, toleft], space=[A, B, C, D, S, W, p1, p1], goal= lambda: (A.at == p1 and B.at == p1 and C.at == p1 and D.at == p1))))
