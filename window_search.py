import tkinter

class Search:
    def __init__(self, cpu, gpu, ram, powerunit, storage, motherboard):
        # VARS
        self.label_width = 15
        self.top_padding_inside_block = 45
        self.left_padding_inside_block = 7
        self.isAllright = False
        self.gpu = gpu
        self.ram = ram
        self.storage = storage
        # self.var = tkinter.IntVar()

        self.manufacturers = [
            ("AMD", 1),
            ("Intel", 2)
        ]

        self.WIDTH = 810
        self.HEIGHT = 700
        self.frame_HEIGHT = 200
        self.frame_WIDTH = 405
        self.window = tkinter.Tk()
        self.var = tkinter.StringVar(value='1')
        self.checkvar1 = tkinter.IntVar()
        self.checkvar2 = tkinter.IntVar()
        self.checkvar3 = tkinter.IntVar()
        self.checkvar4 = tkinter.IntVar()
        self.checkvar5 = tkinter.IntVar()
        self.checkvar6 = tkinter.IntVar()
        self.checkvar7 = tkinter.IntVar()

        self.memorycheckvar1 = tkinter.IntVar()
        self.memorycheckvar2 = tkinter.IntVar()

        self.canvas = tkinter.Canvas(self.window, height=self.HEIGHT, width=self.WIDTH)

        self.ddr1 = tkinter.IntVar()
        self.ddr2 = tkinter.IntVar()
        self.ddr3 = tkinter.IntVar()
        self.ddr4 = tkinter.IntVar()

        self.button = tkinter.Button(self.window, height=3, width=10, text='Search', command=lambda: self.destroy(cpu, self.var))

        self.frame_gpu = tkinter.Frame(self.window, bg="blue", height=self.frame_HEIGHT, width=self.frame_WIDTH)
        self.frame_motherboard = tkinter.Frame(self.window, bg="blue", height=self.frame_HEIGHT, width=self.frame_WIDTH)
        self.frame_cpu = tkinter.Frame(self.window, bg="royal blue", height=self.frame_HEIGHT, width=self.frame_WIDTH)
        self.frame_memory = tkinter.Frame(self.window, bg="blue", height=self.frame_HEIGHT, width=self.frame_WIDTH)
        self.frame_storage = tkinter.Frame(self.window, bg="royal blue", height=self.frame_HEIGHT, width=self.frame_WIDTH)
        self.frame_power = tkinter.Frame(self.window, bg="royal blue", height=self.frame_HEIGHT, width=self.frame_WIDTH)

        self.mb = tkinter.Menubutton(self.frame_memory, text='Memory type', relief=tkinter.RAISED, width=17)
        self.mb.menu = tkinter.Menu(self.mb, tearoff=0)
        self.mb['menu'] = self.mb.menu

        self.mb.menu.add_checkbutton(label='ddr1', variable=self.ddr1, command=lambda: self.menu_click)
        self.mb.menu.add_checkbutton(label='ddr2', variable=self.ddr2, command=lambda: self.menu_click)
        self.mb.menu.add_checkbutton(label='ddr3', variable=self.ddr3, command=lambda: self.menu_click)
        self.mb.menu.add_checkbutton(label='ddr4', variable=self.ddr4, command=lambda: self.menu_click)

        self.entry_gpu_memory_type = tkinter.Entry(self.frame_gpu, width=40)
        self.entry_gpu_memory_capacity = tkinter.Entry(self.frame_gpu, width=40)
        self.entry_gpu_memory_frequency = tkinter.Entry(self.frame_gpu, width=40)
        self.entry_gpu_bus = tkinter.Entry(self.frame_gpu, width=40)
        self.entry_gpu_processor_frequency = tkinter.Entry(self.frame_gpu, width=40)

        self.checkbutton_gpu_512 = tkinter.Checkbutton(self.frame_gpu,
                                                       text='512 MB',
                                                       variable=self.checkvar1,
                                                       onvalue=1,
                                                       offvalue=0,
                                                       command=lambda: self.checkcommand(self.checkvar1, self.checkvar2, self.checkvar3, self.checkvar4, self.checkvar5, self.checkvar6, self.checkvar7))
        self.checkbutton_memory1 = tkinter.Checkbutton(self.frame_storage, text='500 GB', variable=self.memorycheckvar1, onvalue=1, offvalue=0, command=lambda: self.memorycheck_command(self.memorycheckvar1, self.memorycheckvar2))
        self.checkbutton_memory2 = tkinter.Checkbutton(self.frame_storage, text='1 TB', variable=self.memorycheckvar2,
                                                       onvalue=1, offvalue=0,
                                                       command=lambda: self.memorycheck_command(self.memorycheckvar1,
                                                                                                 self.memorycheckvar2))

        self.checkbutton_gpu_1 = tkinter.Checkbutton(self.frame_gpu,
                                                        text='1 GB',
                                                        variable=self.checkvar2,
                                                        onvalue=1,
                                                        offvalue=0,
                                                     command=lambda: self.checkcommand(self.checkvar1, self.checkvar2, self.checkvar3,self.checkvar4,self.checkvar5,self.checkvar6,self.checkvar7))
        self.checkbutton_gpu_2 = tkinter.Checkbutton(self.frame_gpu,
                                                        text='2 GB',
                                                        variable=self.checkvar3,
                                                        onvalue=1,
                                                        offvalue=0,
                                                     command=lambda: self.checkcommand(self.checkvar1, self.checkvar2, self.checkvar3,self.checkvar4,self.checkvar5,self.checkvar6,self.checkvar7))
        self.checkbutton_gpu_3 = tkinter.Checkbutton(self.frame_gpu,
                                                        text='3 GB',
                                                        variable=self.checkvar4,
                                                        onvalue=1,
                                                        offvalue=0,
                                                     command=lambda: self.checkcommand(self.checkvar1, self.checkvar2, self.checkvar3,self.checkvar4,self.checkvar5,self.checkvar6,self.checkvar7))
        self.checkbutton_gpu_4 = tkinter.Checkbutton(self.frame_gpu,
                                                        text='4 GB',
                                                        variable=self.checkvar5,
                                                        onvalue=1,
                                                        offvalue=0,
                                                     command=lambda: self.checkcommand(self.checkvar1, self.checkvar2, self.checkvar3,self.checkvar4,self.checkvar5,self.checkvar6,self.checkvar7))
        self.checkbutton_gpu_6 = tkinter.Checkbutton(self.frame_gpu,
                                                      text='6 GB',
                                                      variable=self.checkvar6,
                                                      onvalue=1,
                                                      offvalue=0,
                                                     command=lambda: self.checkcommand(self.checkvar1, self.checkvar2, self.checkvar3,self.checkvar4,self.checkvar5,self.checkvar6,self.checkvar7))
        self.checkbutton_gpu_8 = tkinter.Checkbutton(self.frame_gpu,
                                                      text='8 GB',
                                                      variable=self.checkvar7,
                                                      onvalue=1,
                                                      offvalue=0,
                                                     command=lambda: self.checkcommand(self.checkvar1, self.checkvar2, self.checkvar3,self.checkvar4,self.checkvar5,self.checkvar6,self.checkvar7))

        self.label_gpu_name = tkinter.Label(self.frame_gpu, text='GPU')

        self.label_gpu_memory_type = tkinter.Label(self.frame_gpu, text='Memory type', width=self.label_width)
        self.label_gpu_memory_capacity = tkinter.Label(self.frame_gpu, text='Memory capacity', width=self.label_width)
        self.label_gpu_memory_frequency = tkinter.Label(self.frame_gpu, text='Memory frequency', width=self.label_width)
        self.label_gpu_bus = tkinter.Label(self.frame_gpu, text='Bus capacity', width=self.label_width)
        self.label_gpu_processor_frequency = tkinter.Label(self.frame_gpu, text='Processor frequency', width=self.label_width)

        self.entry_cpu_socket = tkinter.Entry(self.frame_cpu, width=40)
        self.entry_cpu_cache = tkinter.Entry(self.frame_cpu, width=40)
        self.entry_cpu_cores = tkinter.Entry(self.frame_cpu, width=40)
        self.entry_cpu_frequency = tkinter.Entry(self.frame_cpu, width=40)

        self.radiobutton_cpu_manufacturer = tkinter.Radiobutton(self.frame_cpu,
                                                                variable=self.var,
                                                                text='AMD',
                                                                value='AMD',
                                                                command=lambda: self.selection(self.var, cpu))
        self.radiobutton_cpu_manufacturer2 = tkinter.Radiobutton(self.frame_cpu,
                                                                 variable=self.var,
                                                                 text='Intel',
                                                                 value='Intel',
                                                                 command=lambda: self.selection(self.var, cpu))

        self.label_cpu_name = tkinter.Label(self.frame_cpu, text='CPU')

        self.label_cpu_manufacturer = tkinter.Label(self.frame_cpu, text='Manufacturer', width=self.label_width)
        self.label_cpu_socket = tkinter.Label(self.frame_cpu, text='Socket', width=self.label_width)
        self.label_cpu_cache = tkinter.Label(self.frame_cpu, text='Cache capacity', width=self.label_width)
        self.label_cpu_cores = tkinter.Label(self.frame_cpu, text='Cores amount', width=self.label_width)
        self.label_cpu_frequency = tkinter.Label(self.frame_cpu, text='Processor frequency', width=self.label_width)

        self.label_motherboard_name = tkinter.Label(self.frame_motherboard, text='Motherboard')

        self.label_mb_memory_slots = tkinter.Label(self.frame_motherboard, text='Memory slots', width=self.label_width)
        self.label_mb_pci = tkinter.Label(self.frame_motherboard, text='PCI amount', width=self.label_width)

        self.entry_mb_memory_slots = tkinter.Entry(self.frame_motherboard, width=40)
        self.entry_mb_pci = tkinter.Entry(self.frame_motherboard, width=40)

        self.label_memory_name = tkinter.Label(self.frame_memory, text='RAM')

        self.label_memory_type = tkinter.Label(self.frame_memory, text='Type', width=self.label_width)
        self.label_memory_capacity = tkinter.Label(self.frame_memory, text='Capacity', width=self.label_width)
        self.label_memory_frequency = tkinter.Label(self.frame_memory, text='Frequency', width=self.label_width)

        self.entry_memory_type = tkinter.Entry(self.frame_memory, width=40)
        self.entry_memory_capacity = tkinter.Entry(self.frame_memory, width=40)
        self.entry_memory_frequency = tkinter.Entry(self.frame_memory, width=40)

        self.label_storage_name = tkinter.Label(self.frame_storage, text='Storage')

        self.label_storage_capacity = tkinter.Label(self.frame_storage, text='Capacity', width=self.label_width)
        self.label_storage_interface = tkinter.Label(self.frame_storage, text='Interface', width=self.label_width)

        self.entry_storage_capacity = tkinter.Entry(self.frame_storage, width=40)
        self.entry_storage_interface = tkinter.Entry(self.frame_storage, width=40)

    def render(self):
        self.canvas.pack()

        self.button.place(x=375, y=25)

        self.label_gpu_name.place(relx=0.5, y=5)

        self.entry_gpu_memory_type.place(x=115+self.left_padding_inside_block, y=0+self.top_padding_inside_block)
        self.checkbutton_gpu_512.place(x=115+self.left_padding_inside_block, y=25+self.top_padding_inside_block)
        self.checkbutton_gpu_1.place(x=180 + self.left_padding_inside_block, y=25 + self.top_padding_inside_block)
        self.checkbutton_gpu_2.place(x=230 + self.left_padding_inside_block, y=25 + self.top_padding_inside_block)
        self.checkbutton_gpu_3.place(x=280 + self.left_padding_inside_block, y=25 + self.top_padding_inside_block)
        self.checkbutton_gpu_4.place(x=115 + self.left_padding_inside_block, y=50 + self.top_padding_inside_block)
        self.checkbutton_gpu_6.place(x=165 + self.left_padding_inside_block, y=50 + self.top_padding_inside_block)
        self.checkbutton_gpu_8.place(x=215 + self.left_padding_inside_block, y=50 + self.top_padding_inside_block)
        self.entry_gpu_memory_frequency.place(x=115 + self.left_padding_inside_block, y=75 + self.top_padding_inside_block)
        self.entry_gpu_bus.place(x=115 + self.left_padding_inside_block, y=100 + self.top_padding_inside_block)
        self.entry_gpu_processor_frequency.place(x=115 + self.left_padding_inside_block, y=125 + self.top_padding_inside_block)

        self.label_gpu_memory_type.place(x=0+self.left_padding_inside_block, y=0+self.top_padding_inside_block)
        self.label_gpu_memory_capacity.place(x=0+self.left_padding_inside_block, y=25+self.top_padding_inside_block)
        self.label_gpu_memory_frequency.place(x=0+self.left_padding_inside_block, y=75+self.top_padding_inside_block)
        self.label_gpu_bus.place(x=0+self.left_padding_inside_block, y=100+self.top_padding_inside_block)
        self.label_gpu_processor_frequency.place(x=0+self.left_padding_inside_block, y=125+self.top_padding_inside_block)

        self.label_cpu_name.place(relx=0.5, y=5)

        self.label_cpu_manufacturer.place(x=0 + self.left_padding_inside_block, y=0+self.top_padding_inside_block)
        self.label_cpu_socket.place(x=0 + self.left_padding_inside_block, y=25 + self.top_padding_inside_block)
        self.label_cpu_cache.place(x=0 + self.left_padding_inside_block, y=50 + self.top_padding_inside_block)
        self.label_cpu_cores.place(x=0 + self.left_padding_inside_block, y=75 + self.top_padding_inside_block)
        self.label_cpu_frequency.place(x=0 + self.left_padding_inside_block, y=100 + self.top_padding_inside_block)
        self.radiobutton_cpu_manufacturer.place(x=115+self.left_padding_inside_block, y=0+self.top_padding_inside_block)
        self.radiobutton_cpu_manufacturer2.place(x=170 + self.left_padding_inside_block, y=0 + self.top_padding_inside_block)
        self.entry_cpu_cache.place(x=115+self.left_padding_inside_block, y=25+self.top_padding_inside_block)
        self.entry_cpu_socket.place(x=115 + self.left_padding_inside_block, y=50 + self.top_padding_inside_block)
        self.entry_cpu_cores.place(x=115 + self.left_padding_inside_block, y=75 + self.top_padding_inside_block)
        self.entry_cpu_frequency.place(x=115 + self.left_padding_inside_block, y=100 + self.top_padding_inside_block)

        self.label_motherboard_name.place(relx=0.5, y=5)

        self.label_mb_memory_slots.place(x=0+self.left_padding_inside_block, y=0+self.top_padding_inside_block)
        self.label_mb_pci.place(x=0+self.left_padding_inside_block, y=25+self.top_padding_inside_block)

        self.entry_mb_memory_slots.place(x=115+self.left_padding_inside_block, y=0+self.top_padding_inside_block)
        self.entry_mb_pci.place(x=115+self.left_padding_inside_block, y=25+self.top_padding_inside_block)

        self.label_memory_name.place(relx=0.5, y=5)

        self.mb.place(x=0+self.left_padding_inside_block, y=0+self.top_padding_inside_block)
        self.label_memory_frequency.place(x=0 + self.left_padding_inside_block, y=25 + self.top_padding_inside_block)
        self.label_memory_capacity.place(x=0 + self.left_padding_inside_block, y=50 + self.top_padding_inside_block)

        self.entry_memory_capacity.place(x=115+self.left_padding_inside_block, y=0+self.top_padding_inside_block)
        self.entry_memory_frequency.place(x=115 + self.left_padding_inside_block, y=25 + self.top_padding_inside_block)
        self.entry_memory_type.place(x=115 + self.left_padding_inside_block, y=50 + self.top_padding_inside_block)

        self.label_storage_name.place(relx=0.5, y=5)

        self.label_storage_capacity.place(x=0+self.left_padding_inside_block, y=0+self.top_padding_inside_block)
        self.label_storage_interface.place(x=0+self.left_padding_inside_block, y=25+self.top_padding_inside_block)

        # self.entry_storage_capacity.place(x=115+self.left_padding_inside_block, y=0+self.top_padding_inside_block)
        self.checkbutton_memory1.place(x=115+self.left_padding_inside_block, y=0+self.top_padding_inside_block)
        self.checkbutton_memory2.place(x=180+self.left_padding_inside_block, y=0+self.top_padding_inside_block)
        self.entry_storage_interface.place(x=115+self.left_padding_inside_block, y=25+self.top_padding_inside_block)

        self.frame_cpu.place(x=0, y=100)
        self.frame_motherboard.place(x=self.frame_WIDTH, y=100)
        self.frame_gpu.place(x=0, y=300)
        self.frame_storage.place(x=self.frame_WIDTH, y=300)
        self.frame_power.place(x=0, y=500)
        self.frame_memory.place(x=self.frame_WIDTH, y=500)

        self.window.mainloop()

    def destroy(self, cpu, var):
        self.isAllright = True

        self.ram.set_ram(self.ddr1, self.ddr2, self.ddr3, self.ddr4)

        print('Search: ' + str(self.ddr1.get()))
        self.gpu.set_vram(self.checkvar1, self.checkvar2, self.checkvar3,
                          self.checkvar4, self.checkvar5, self.checkvar6, self.checkvar7)
        print(self.checkvar1, self.checkvar2, self.checkvar3, self.checkvar4, self.checkvar5, self.checkvar6, self.checkvar7)
        self.window.destroy()

    def selection(self, var, cpu):
        print(var.get())
        cpu.set_manufacturer(var.get())

    def checkcommand(self, checkvar1, checkvar2, checkvar3, checkvar4, checkvar5, checkvar6, checkvar7):
        print(checkvar1.get())
        vram_list = []
        if checkvar1.get() == 1:
            vram_list.append('512')
        else:
            vram_list.append('0')
        if checkvar2.get() == 1:
            vram_list.append('1')
        else:
            vram_list.append('0')
        if checkvar3.get() == 1:
            vram_list.append('2')
        else:
            vram_list.append('0')
        if checkvar4.get() == 1:
            vram_list.append('3')
        else:
            vram_list.append('0')
        if checkvar5.get() == 1:
            vram_list.append('4')
        else:
            vram_list.append('0')
        if checkvar6.get() == 1:
            vram_list.append('6')
        else:
            vram_list.append('0')
        if checkvar7.get() == 1:
            vram_list.append('8')
        else:
            vram_list.append('0')
        print("checkcommand: " + str(vram_list[0]))
        self.gpu.set_vram(vram_list[0], vram_list[1], vram_list[2], vram_list[3], vram_list[4], vram_list[5], vram_list[6])

    def menu_click(self):
        print('lol')

    def memorycheck_command(self, x1, x2):
        self.storage.set_storage(x1, x2)
        print('hey hey')

