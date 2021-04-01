class Dog: 

    def __init__(self):
        self.flag_bark = True

    def cutSungdae(self):
        self.flag_bark = False


class Bird: 

    def __init__(self):
        self.idx_fly = 0

    def training(self):
        self.idx_fly += 1

    def trainging_hard(self, power):
        self.idx_fly += power

class GaeSae(Dog, Bird):
    
    def __init__(self):
        Dog.__init__(self)
        Bird.__init__(self)
        self.flag_kill = True
        # pass
    def useKill(self):
        self.flag_kill = False
    
    
if __name__ =='__main__' :
    gs = GaeSae()
    print(gs.flag_bark)
    print(gs.idx_fly)
    
    gs.cutSungdae()
    gs.trainging_hard(3)
    gs.trainging_hard(4)
    print(gs.flag_bark)
    print(gs.idx_fly)
    