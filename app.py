from vpython import sphere, rate, vector, color

class Sphere:
    def __init__(self, pos):
        self.pos = pos
        self.sphere = sphere(pos = pos, color = color.red)
        
    def update(self):
        self.sphere.pos.z += 0.1

class GameRenderer:
    def __init__(self):
        self.animated = False 
        self.objects = []
        self.k = 0
        self.n = 0

    def addObject(self, xpos):
        self.objects.append(Sphere(vector(xpos, 0, 0)))

    def start(self):
        if not(self.animated):
            self.animated = True
    
    def update(self):
        while self.animated:
            rate(30)
            for object in self.objects:
                object.update()
        
            if self.k % 20 == 0:
                self.addObject(-3 + (self.n) % 6)
            self.n += 1
            self.k += 1
            if self.k == 120:
                break
    
    def stop(self):
        if self.animated:
            self.animated = False
        

renderer = GameRenderer()
renderer.addObject(0)
renderer.start()
renderer.update()
renderer.stop()