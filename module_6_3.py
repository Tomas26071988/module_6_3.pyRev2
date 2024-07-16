class Horse:
    def __init__(self):
        self.x_distance = 0      # пройденный путь
        self.sound = 'Frrr'      # звук, который издает лошадь
        super().__init__()
    def run(self, dx:int):
        self.x_distance += dx

class Eagle:
    def __init__(self):
        self.y_distance = 0      # пройденный путь
        self.sound = 'I train, eat, sleep, and repeat'      # звук, который издает орел

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self,dx,dy):
        self.run (dx)
        self.fly(dy)


    def get_poss(self):
        return {self.x_distance, self.y_distance}

    def voice(self):
        print(self.sound)



p1 = Pegasus()
print(p1.get_poss())

p1.move(10, 15)
print(p1.get_poss())
p1.move(-5, 20)
print(p1.get_poss())

p1.voice()

