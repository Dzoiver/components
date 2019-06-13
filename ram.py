class Memory:
    def __init__(self):
        self.memory_type = '0'
        self.ddr1 = 'NULL'
        self.ddr2 = 'NULL'
        self.ddr3 = 'NULL'
        self.ddr4 = 'NULL'
        self.ddr5 = 'NULL'

    def set_ram(self, ddr1, ddr2, ddr3, ddr4):
        print('set_ram: ' + str(ddr1.get()))
        if ddr1.get() == 1:
            self.ddr1 = 'ddr1'
            print('self.ddr1: ' + self.ddr1)
        if ddr2.get() == 1:
            self.ddr2 = 'ddr2'
        if ddr3.get() == 1:
            self.ddr3 = 'ddr3'
        if ddr4.get() == 1:
            self.ddr4 = 'ddr4'


