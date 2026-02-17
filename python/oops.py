class collection:
    def __init__(self,name,xp):
        self.name=name
        self.xp=xp
    def speed(self):
        speed=self.xp*100
        mark= speed//1000
        if speed>100:
            print("MARK",mark)
        else:
            print("through it in trash ")
    
delta=collection("elt",100)
delta.speed()