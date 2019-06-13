class Gpu:
    def __init__(self):
        self.allright = False
        self.gpu_vram = []
        self.vram1 = '0'
        self.vram2 = '0'
        self.vram3 = '0'
        self.vram4 = '0'
        self.vram5 = '0'
        self.vram6 = '0'
        self.vram7 = '0'

    def get_vram(self):
        print(self.vram1)
        return self.vram1

    def set_vram(self, x, x2, x3, x4, x5, x6, x7):
        if self.allright:
            print("set")
            self.vram1.set(x)
        self.vram1 = x
        print("set_vram " + str(self.vram1))
        self.vram2 = x2
        print("set_vram " + str(self.vram2))
        self.vram3 = x3
        print("set_vram " + str(self.vram3))
        self.vram4 = x4
        print("set_vram " + str(self.vram4))
        self.vram5 = x5
        print("set_vram " + str(self.vram5))
        self.vram6 = x6
        print("set_vram " + str(self.vram6))
        self.vram7 = x7
        print("set_vram " + str(self.vram7))
