from genericpath import isdir
import psutil
import time
from memorpy import *
import os
import shutil
class ProcessManager():
    process1 = None
    Mem1 = None
    def __init__(self,pid):
       self.process1 = psutil.Process(pid)
       self.Mem1 = MemWorker(pid=pid)

    def suspend(self):
        try:
           self.process1.suspend()
        except psutil.NoSuchProcess:
            print("[-] this pid not exist !")
        except psutil.AcessDenied:
            print("[-] your accesed process refuse this request maybe you not administrator ?")
        except Exception as e:
            print("[-] this error thats why not processing your request : "+str(e))


    def resume(self):
        try:
            self.process1.resume()
        except Exception as e:
            print("[-] this error thats why not processing your request : "+str(e))
    
    def get_cpu_percent(self,interval=1.0):
        if self.process1 is None:
            return 0.0
        try:
            return self.process1.cpu_percent(interval)
        except:
            return 0.0

    def get_memory_mb(self):
        if self.process1 is None:
            return 0
        try:
            return self.process1.memory_info().rss / (1024 * 1024) 
        except :
            return 0

    def dumpitwithpattern(self,pattern,ext):
        result = self.Mem1.umem_search(pattern)
        list1 = list(result)
        print("[+] Suspending process")
        self.suspend()
        print("[+] Dumping process with pattern")
        print("[+] Founded "+str(len(list1)))
        dirname1 = self.process1.name().replace(".","_")+"_dumps"
        if os.path.exists(dirname1):
            if os.path.isdir(dirname1):
                shutil.rmtree(dirname1)


        os.makedirs(dirname1)

        for data1 in list1:
            fname = hex(data1.value).replace("L","")+ext
            tamyol1 = os.path.join(dirname1,fname.replace("0x",""))
            with open(tamyol1,"wb") as f:
                while True:
                    try:
                        gelen = data1.read(4096)
                        if not gelen:
                            print("[+]"+tamyol1+" saved !")
                            f.close()
                            break
                        f.write(gelen)
                        data1 += 4096
                    except :
                        print("[+]"+tamyol1+" saved !")
                        f.close()
        print("[+] Resuming process")
        self.resume()
        print("[+] Process completed !")
                    

             


   
class ProcessLister():
     def get_process(self):
       for k in psutil.process_iter(["pid","name"]):
           u = k.info
           print(str(u["pid"])+" "+u["name"])

