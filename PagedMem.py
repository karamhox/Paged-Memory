from math import inf
from random import randint

id = 0
processes = []
coreMap = [0] * 10
pageSize = 512
pageMask = 4

class Pages:
    def __init__(self, size):
        global id, processes, pageSize
        self.id = id
        self.size = size // 512
        self.pages = self.findFreeMem()
        self.bases = list(i * pageSize for i in self.pages)
        self.boundries = list(i + pageSize - 1 for i in self.bases)

        id += 1
        processes.append(self)


    def findFreeMem(self):
        global coreMap
        pages = []
        for i in range(len(coreMap)):
            if coreMap[i] == 0:
                if len(pages) < self.size:
                    coreMap[i] = 1
                    pages.append(i)
                    continue
                break
                

        return pages
    

    def translateAddr(self, addr):
        addr = addr[2:]
        for i in range(len(self.pages)):
            for j in range(pageMask):
                if not (int(addr[j], 16) == self.pages[i]):
                    break
                
            return int(addr, 16) + self.bases[i], i
        
    
    def checkValidity(self, addr):
        phAddr, page = self.translateAddr(addr)
        if phAddr > self.boundries[page]:
            print("Address out of boundary")
            return
        print(f"{addr}: 0xffeefcfecd")
        return
    
    
    def free(self):
        global processes, coreMap
        for i in range(len(processes)):
            if processes[i] == self:
                for j in range(len(processes[i].pages)):
                    coreMap[processes[i].pages[j]] = 0
                processes.pop(i)
                return
                
    

process1 = Pages(1024)
process2 = Pages(3000)
process3 = Pages(2048)

process1.checkValidity("0x000040")
process2.checkValidity("0x999999999")
process1.checkValidity("0x0000900")

process1.free()
process3.free()

process4 = Pages(4096)
    
    
#Well Done!
                

        
        
                

