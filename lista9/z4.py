import numpy as np
import matplotlib.pyplot as plt

jez = ['Python','C','C++','Java','C#','VB','JS','SQL','Assembly','PHP','Swift','Go','R','CVB','MATLAB','Ruby','Delphi','Rust','Perl','Scratch']
pro = [16.36,16.26,12.91,12.21,5.73,4.64,2.87,2.50,1.60,1.39,1.20,1.14,1.04,0.98,0.91,0.80,0.73,0.61,0.59,0.58]

a = np.arange(len(jez))

plt.bar(a,pro)
plt.xticks(a, jez)
plt.ylabel("Popularność")
plt.xlabel("Języki")
plt.title("Popularność języków programowania")
plt.show()