import tkinter
import sqlite3

class Result:
    def __init__(self, cpu, manufacturer, vram1, vram2, vram3, vram4, vram5, vram6, vram7, ram, storage):
        self.WIDTH = 810
        self.HEIGHT = 700
        self.frame_HEIGHT = 200
        self.frame_WIDTH = 405
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, height=self.HEIGHT, width=self.WIDTH)

        self.scrollbar_cpu = tkinter.Scrollbar(self.window)
        self.scrollbar_gpu = tkinter.Scrollbar(self.window)
        self.scrollbar_motherboard = tkinter.Scrollbar(self.window)
        self.scrollbar_memory = tkinter.Scrollbar(self.window)
        self.scrollbar_storage = tkinter.Scrollbar(self.window)

        self.list_cpu = tkinter.Listbox(self.window, yscrollcommand=self.scrollbar_cpu.set)
        self.list_gpu = tkinter.Listbox(self.window, yscrollcommand=self.scrollbar_gpu.set)
        self.list_motherboard = tkinter.Listbox(self.window, yscrollcommand=self.scrollbar_motherboard.set)
        self.list_memory = tkinter.Listbox(self.window, yscrollcommand=self.scrollbar_memory.set)
        self.list_storage = tkinter.Listbox(self.window, yscrollcommand=self.scrollbar_storage.set)

        self.manufacturer = manufacturer

        conn = sqlite3.connect('venge.db')
        curs = conn.cursor()

        if self.manufacturer == 'NULL':
            curs.execute('SELECT * FROM CPU')
        else:
            curs.execute('SELECT * FROM CPU WHERE manufacturer="{}"'.format(self.manufacturer))
        data_cpu = curs.fetchall()
        for line in data_cpu:
            self.list_cpu.insert(tkinter.END, line,)

        if vram1.get() == 1:
            vram1.set('512')
        if vram2.get() == 1:
            vram2.set('1')
        if vram3.get() == 1:
            vram3.set('2')
        if vram4.get() == 1:
            vram4.set('3')
        if vram5.get() == 1:
            vram5.set('4')
        if vram6.get() == 1:
            vram6.set('6')
        if vram7.get() == 1:
            vram7.set('8')
        print("vram1.get(): " + str(vram1.get()))
        print("vram2.get(): " + str(vram2.get()))
        print("vram3.get(): " + str(vram3.get()))
        print("vram4.get(): " + str(vram4.get()))
        print("vram5.get(): " + str(vram5.get()))
        print("vram6.get(): " + str(vram6.get()))
        print("vram7.get(): " + str(vram7.get()))
        conn.commit()

        curs.execute('SELECT * FROM GPU WHERE vram="{}" OR vram="{}" OR vram="{}" OR vram="{}" OR vram="{}" OR vram="{}" OR vram="{}"'.format(vram1.get(), vram2.get(), vram3.get(), vram4.get(), vram5.get(), vram6.get(), vram7.get()))
        data_gpu = curs.fetchall()
        for line in data_gpu:
            self.list_gpu.insert(tkinter.END, line,)
        print("data_gpu: " + str(data_gpu))

        print('ram.ddr1: ' + ram.ddr1)
        curs.execute('SELECT * FROM MEMORY WHERE MEMORY_TYPE="{}" OR MEMORY_TYPE="{}" OR MEMORY_TYPE="{}" OR MEMORY_TYPE="{}"'.format(ram.ddr1, ram.ddr2, ram.ddr3, ram.ddr4))
        data_ram = curs.fetchall()
        print('data_ram:' + str(data_ram))
        for line in data_ram:
            self.list_memory.insert(tkinter.END, line)

        curs.execute('SELECT * FROM STORAGE WHERE capacity="{}" OR capacity="{}"'.format(storage.capacity1, storage.capacity2))
        data_storage = curs.fetchall()
        for line in data_storage:
            self.list_storage.insert(tkinter.END, line)

        self.label_cpu_manufacturer = tkinter.Label(self.window, text=cpu.get_manufacturer())
        self.label_info = tkinter.Label(self.window, text='Подходящие по запросу комплектующие')
        self.label_cpu = tkinter.Label(self.window, text='CPU')
        self.label_gpu = tkinter.Label(self.window, text='GPU')
        self.label_ram = tkinter.Label(self.window, text='RAM')
        self.label_motherboard = tkinter.Label(self.window, text='Motherboard')
        self.label_powerunit = tkinter.Label(self.window, text='Powerunit')
        self.label_memory = tkinter.Label(self.window, text='Storage')

    def render(self):
        self.canvas.pack()
        self.label_cpu_manufacturer.place(x=50, y=50)
        self.label_cpu.place(x=25, y=675)
        self.label_gpu.place(x=165, y=675)
        self.label_powerunit.place(x=305, y=675)
        self.label_ram.place(x=445, y=675)
        self.label_memory.place(x=585, y=675)
        # self.label_motherboard.place(x=575, y=675)
        self.label_info.place(x=300, y=600)

        self.list_cpu.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.scrollbar_cpu.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.scrollbar_cpu.config(command=self.list_cpu.yview)

        self.list_gpu.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.scrollbar_gpu.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.scrollbar_gpu.config(command=self.list_gpu.yview)

        self.list_motherboard.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.scrollbar_motherboard.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.scrollbar_motherboard.config(command=self.list_cpu.yview)

        self.list_memory.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.scrollbar_memory.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.scrollbar_memory.config(command=self.list_memory.yview)

        self.list_storage.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.scrollbar_storage.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.scrollbar_storage.config(command=self.list_storage.yview)



        self.window.mainloop()
