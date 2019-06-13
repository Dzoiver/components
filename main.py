import window_search
import cpu
import result
import gpu
import motherboard
import ram
import powerunit
import ssd, hdd

cpu1 = cpu.Cpu()
gpu1 = gpu.Gpu()
motherboard1 = motherboard.Motherboard()
ram1 = ram.Memory()
storage1 = ssd.Storage()
powerunit1 = powerunit.Powerunit()

search1 = window_search.Search(cpu1, gpu1, ram1, powerunit1, storage1, motherboard1)
search1.render()
if search1.isAllright:
    print("dada" + str(gpu1.get_vram()))
    gpu1.allright = True
    result1 = result.Result(cpu1, cpu1.get_manufacturer(), gpu1.get_vram(), gpu1.vram2, gpu1.vram3, gpu1.vram4, gpu1.vram5, gpu1.vram6, gpu1.vram7, ram1, storage1)
    result1.render()

