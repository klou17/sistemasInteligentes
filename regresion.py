import numpy as np #manipular valores numericos
import matplotlib.pyplot as plt #para graficos

# x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# y=[1,2,2,4,5,4,6,4,6,7,9,10,11,12,10]

x=[2,3,5,7,8]
y=[14,20,32,42,44]

n = len(x) #cantidad de datos
x = np.array(x)
y = np.array(y)

sumx = sum(x)
sumy = sum(y)
sumx2 = sum(x*x)
sumy2 = sum(y*y)
sumxy = sum(x*y)
promx =  sumx/n
promy =  sumy/n

m = (sumx*sumy - n*sumxy)/(sumx**2 - n*sumx2)
b = promy - m*promx

sigmax = np.sqrt(sumx2/n - promx**2)
sigmay = np.sqrt(sumy2/n - promy**2)
sigmaxy = sumxy/n - promx*promy
R2 = (sigmaxy/(sigmax*sigmay))**2

print("f(x) = ",m,"x +",b)
print("R2 = ",R2)

plt.plot(x, y, 'o', label='Datos')
plt.plot(x, m*x +b, label='Ajuste')

plt.xlabel('x')
plt.ylabel('y')

plt.title('Regresión Lineal')
plt.grid()
plt.legend(loc=4)
plt.show()




