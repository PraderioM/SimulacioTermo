from matplotlib import pyplot as plt
from pylab import savefig
from scipy.optimize import curve_fit
from numpy import arange

f=lambda x, N, b, a: x/(N-b*x)+a*x/(N**2)
g=lambda T, x, N, b, a: x*T/(N-2*b*x)+a*x/(N**2)

d=8*[[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8]]
T=8*[[0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3]]
P=[]
errP=[]
Colors=['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'gray']

P.append([-0.001,-0.041,-0.114,-0.228,-0.359,-0.594,-1.022,-1.084])
P.append([-0.003,-0.002,-0.11,-0.187,-0.401,-0.538,-0.969,-0.504])
P.append([0.01,-0.028,-0.082,-0.192,-0.3,-0.525,-0.664,0.012])
P.append([0.025,-0.005,-0.053,-0.142,-0.252,-0.45,-0.321,0.523])
P.append([0.047,0.026,-0.018,-0.078,-0.203,-0.277,0.014,1.001])
P.append([0.063,0.054,0.021,-0.031,-0.11,-0.062,0.351,1.486])
P.append([0.077,0.091,0.068,0.033,0.018,0.143,0.678,1.949])
P.append([0.091,0.122,0.119,0.116,0.143,0.352,0.973,2.406])

errP.append([0.016,0.039,0.061,0.084,0.12,0.153,0.159,0.143])
errP.append([0.016,0.016,0.061,0.089,0.11,0.154,0.147,0.161])
errP.append([0.015,0.036,0.063,0.078,0.121,0.163,0.142,0.171])
errP.append([0.016,0.035,0.061,0.083,0.102,0.129,0.153,0.184])
errP.append([0.012,0.032,0.059,0.082,0.103,0.127,0.161,0.206])
errP.append([0.01,0.031,0.054,0.082,0.106,0.144,0.173,0.218])
errP.append([0.01,0.029,0.053,0.08,0.108,0.145,0.188,0.233])
errP.append([0.011,0.03,0.055,0.084,0.117,0.153,0.196,0.239])

P1=[[ P[i][j] for i in range(8)] for j in range(8)]
errP1=[[ errP[i][j] for i in range(8)] for j in range(8)]


for i in range(8):
	plt.errorbar(d[i],P[i], yerr=errP[i], fmt='o', color=Colors[i])

plt.xlabel('densidad reducida')
plt.ylabel('presion reducida')

curvas=[]
Label=['T=0.6', 'T=0.7', 'T=0.8', 'T=0.9', 'T=1.0', 'T=1.1', 'T=1.2', 'T=1.3']
N=[7.4, 9, 10.4, 11, 11.4, 14.6, 8.5, 10]
b=[6.4, 9, 12, 13, 13.6, 17.7, 10.3, 12.2]
a=[-80, -98, -120, -115, -86, -65, -8, 15]
X=arange(d[0][0], d[0][-1], 0.01)
j=0
for i in range(8):
	aux, =plt.plot(X, [x/(N[i]-b[i]*x)+a[i]*x/(N[i]**2) for x in X], label=Label[i], color=Colors[i])
	curvas.append(aux)	

plt.legend(curvas, Label, loc=2)
plt.savefig('Isotermas.png')
plt.clf()



for i in range(8):
	plt.errorbar(T[i],P1[i], yerr=errP1[i], fmt='o', color=Colors[i])

plt.xlabel('temperatura reducida')
plt.ylabel('presion reducida')

curvas=[]
Label=['p=0.1', 'p=0.2', 'p=0.3', 'p=0.4', 'p=0.5', 'p=0.6', 'p=0.7', 'p=0.8']
X=arange(T[0][0], T[0][-1], 0.01)
j=0
for i in range(8):
	try:
		FitValues, Covariance=curve_fit(g ,T[i],P1[i], p0=[0.1, 500, 2498, -20000])
		aux, =plt.plot(X, [g(x, *FitValues) for x in X], label=Label[i], color=Colors[i])
		curvas.append(aux)
	except:
		del Label[i-j]
		j+=1
		pass

plt.legend(curvas, Label, loc=2)
plt.savefig('Isodensas.png')
plt.clf()