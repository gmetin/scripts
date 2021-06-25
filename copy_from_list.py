import numpy as np
import subprocess

path = "/gpfs02/work/metin/birth/central_nozfire/"
l = np.loadtxt(path+"list_all_clean.txt",usecols=(0),dtype=str)

l_in = [path+i.split("/")[0]+"/deltaLOGN_"+i.split("_")[1] for i in l]

exe = "cp"

for i in l_in:
    arg1 = i
    arg2 = "DENSFIELDS/"+i.split("/")[-2]+"_"+i.split("_")[-1]
    subprocess.Popen([exe,arg1,arg2])
