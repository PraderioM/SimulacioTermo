from math import log
from matplotlib import pyplot as plt
from pylab import savefig
from scipy.stats import linregress as linreg

T=[1,1.05,1.1,1.15,1.2,1.25]
T = [(t-1.32)/1.32 for t in T]
lT= [log(abs(t)) for t in T]
dg=[0.7, 0.65, 0.65, 0.6, 0.58, 0.52]
ldg= [log(abs(x)) for x in dg]
dl=[0.05, 0.05, 0.05, 0.1, 0.1, 0.18]
ldl = [log(abs(x)) for x in dl]

plt.plot(lT,ldg, 'ro')
lr=linreg(lT,ldg)
plt.plot(lT, [lr.slope*x+lr.intercept for x in lT], 'k')
plt.title('Exponente critico gas')
plt.xlabel('log(|tau|)')
plt.ylabel('log(|d|)')
plt.savefig('expcritgas.png')
plt.clf()

kg=lr.intercept
data = open('data.txt', 'w')
s='El exponente critico calculado a partir del gas es \n{}\n'.format(kg)
data.write(s)


plt.plot(lT,ldl, 'ro')
lr=linreg(lT,ldl)
plt.plot(lT, [lr.slope*x+lr.intercept for x in lT], 'k')
plt.title('Exponente critico liquido')
plt.xlabel('log(|tau|)')
plt.ylabel('log(|d|)')
plt.savefig('expcritliquid.png')
plt.clf()

kl=lr.intercept
s='El exponente critico calculado a partir del liquido es \n{}\n'.format(kl)
data.write(s)


s='La media de ambos valores es \n{}\n'.format((kl+kg)/2)
data.write(s)




data.write('\\begin{table}\n\t\\centering\n\t\\begin{tabular}{|c|c|c|c|c|c|}\n\t\t\\hline\n\t')
data.write('$\\tau$ & $d(\\tau)$ gas & $d(\\tau)$ liquido & $\\log(|\\tau|)$ & $\\log(|d(\\tau)|)$ gas & $\\log(|d(\\tau)|)$ liquido\\\\\n\t\t\\hline\n\t')
for i in range(len(T)):
	s='\t${0:.2}$ & ${1:.2}$ & ${2:.2}$ & ${3:.2}$ & ${4:.2}$ & ${5:.2}$'.format(T[i], dg[i], dl[i], lT[i], ldg[i], ldl[i])
	s+='\\\\\n\t\t\\hline\n\t'
	data.write(s)

data.write('\\end{tabular}\n\\caption{Valores de temperatura deucida, densidades i logaritmos de sus valores absolutos para el estado gaseoso y el estado liquido}\n\\label{tab:dens}\n\\end{table}')


data.close()