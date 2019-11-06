from poodle import Object, schedule

class Capactiy(Object):
    Cap : int

class WaterLevel(Object):
    Water: int

class Jug(Capactiy, WaterLevel):
    name : str

    def __str__ (self):
        return self.name

class World(Object):
    one:bool
    onetest : int

W = World()
W.one = False
W.onetest = 1

A = Jug()
A.Cap = 12
A.Water = 0
A.name = "Jug12"

B = Jug()
B.Cap = 8
B.Water = 0
B.name = "Jug8"

C = Jug()
C.Cap = 3
C.Water = 0
C.name = "Jug3"

def FillJug(jug:Jug):
    assert jug.Water < jug.Cap
    jug.Water = jug.Cap
    return f'fill up {jug.name}'

def EmptyJug(jug: Jug):
    assert jug.Water > 0
    jug.Water = 0
    return f'empty {Jug.name}'

def Check(jug: Jug, world: World):
    assert jug.Water == world.onetest
    world.one = True
    return 'got one Water'

def PoorCase1(jug1: Jug, jug2: Jug):
    assert jug1.Cap > jug2.Cap
    assert jug1.Water > 0
    assert jug2.Water < jug2.Cap
    assert jug1.Water <= (jug2.Cap - jug2.Water)
    jug2.Water += jug1.Water
    jug1.Water = 0
    return f'pour {jug1.name} to {jug2.name}'

def PoorCase2(jug1: Jug, jug2: Jug):
    assert jug1.Cap > jug2.Cap
    assert jug1.Water > 0
    assert jug2.Water < jug2.Cap
    assert jug1.Water > (jug2.Cap - jug2.Water)
    jug2.Water = jug2.Cap
    jug1.Water -= (jug2.Cap - jug2.Water)
    return f'pour {jug1.name} to {jug2.name}'

print('\n'.join(x() for x in schedule(methods=[FillJug, EmptyJug, Check, PoorCase1, PoorCase2], space=[A, B, C, D, W], goal= lambda: W.one == True)))
