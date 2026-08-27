import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-3,3,1000)

x1 = np.zeros_like(t)
x1[(t<2) & (1<t)]=0
x1[(t<1) & (0<t)]=2
x1[(t<0) & (-1<t)]=2
x1[(t<-1) & (-2<t)]=1


x2 = np.zeros_like(t)
x2[(t<2) & (1<t)]=2
x2[(t<1) & (0<t)]=1
x2[(t<0) & (-2<t)]=-1
x2[(t<-2) & (-3<t)]=2

x3_addition = x1 + x2
x3_multip = x1*x2

plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)          
plt.plot(t, x1)
plt.title("x1(t)")
plt.grid(True)

plt.subplot(4, 1, 2)          
plt.plot(t, x2)
plt.title("x2(t)")
plt.grid(True)

plt.subplot(4,1,3)
plt.plot(t,x3_addition)
plt.title("Addition Of Continous Signal")
plt.grid(True)

plt.subplot(4,1,4)
plt.plot(t,x3_multip)
plt.title("Multiplication Of Continous Signal")
plt.grid(True)


plt.tight_layout()   
plt.show()
