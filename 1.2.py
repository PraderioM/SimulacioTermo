from visual import *
from visual.graph import *
from random import random

# A model of an ideal gas with hard-sphere collisions
# Program uses numpy arrays for high speed computations

# Bruce Sherwood

win=500

Natoms = 100  # change this to have more or fewer atoms

# Typical values
L = 1. # container is a cube L on a side
gray = (0.7,0.7,0.7) # color of edges of container
Matom = 4E-3/6E23 # helium mass
Ratom = 0.03 # wildly exaggerated size of helium atom
k = 1.4E-23 # Boltzmann constant
T = 300. # around room temperature
dt = 1E-5

scene = display(title="Gas", width=win, height=win, x=0, y=0,
                center=(L/2.,L/2.,L/2.))

deltav = 100. # binning for v histogram
vdist = gdisplay(x=0, y=win, ymax = Natoms*deltav/1000.,
             width=win, height=0.6*win, xtitle='v', ytitle='dN')
theory = gcurve(color=color.cyan)

dv = 10.
for v in arange(0.,3001.+dv,dv): # theoretical prediction
    theory.plot(pos=(v,
        (deltav/dv)*Natoms*4.*pi*((Matom/(2.*pi*k*T))**1.5)
                     *exp((-0.5*Matom*v**2)/(k*T))*v**2*dv))

observation = ghistogram(bins=arange(0.,3000.,deltav),
                        accumulate=1, average=1, color=color.red)

xaxis = curve(pos=[(0,0,0), (L,0,0)], color=gray)
yaxis = curve(pos=[(0,0,0), (0,L,0)], color=gray)
zaxis = curve(pos=[(0,0,0), (0,0,L)], color=gray)
xaxis2 = curve(pos=[(L,L,L), (0,L,L), (0,0,L), (L,0,L)], color=gray)
yaxis2 = curve(pos=[(L,L,L), (L,0,L), (L,0,0), (L,L,0)], color=gray)
zaxis2 = curve(pos=[(L,L,L), (L,L,0), (0,L,0), (0,L,L)], color=gray)

Atoms = []
##colors = [color.red, color.green, color.blue,
##          color.yellow, color.cyan, color.magenta]
poslist = []
plist = []
mlist = []
rlist = []


Lmin = 1.1*Ratom
Lmax = L-Lmin
x = Lmin+(Lmax-Lmin)*random()
y = Lmin+(Lmax-Lmin)*random()
z = Lmin+(Lmax-Lmin)*random()
r = Ratom

##  Atoms = Atoms+[sphere(pos=(x,y,z), radius=r, color=colors[i % 6])]
Atoms.append(sphere(pos=(x,y,z), radius=r, color=color.yellow,
                    make_trail=True, retain=100))
mass = Matom*r**3/Ratom**3
pavg = sqrt(2.*mass*1.5*k*T) # average kinetic energy p**2/(2mass) = (3/2)kT
theta = pi*random()
phi = 2*pi*random()
px = pavg*sin(theta)*cos(phi)
py = pavg*sin(theta)*sin(phi)
pz = pavg*cos(theta)
poslist.append((x,y,z))
plist.append((px,py,pz))
mlist.append(mass)
rlist.append(r)

for i in range(1,Natoms):
    Lmin = 1.1*Ratom
    Lmax = L-Lmin
    x = Lmin+(Lmax-Lmin)*random()
    y = Lmin+(Lmax-Lmin)*random()
    z = Lmin+(Lmax-Lmin)*random()
    r = Ratom

##  Atoms[0].trail_object.radius = 1
    Atoms.append(sphere(pos=(x,y,z), radius=r, color=color.cyan))
    mass = Matom*r**3/Ratom**3
    pavg = sqrt(2.*mass*1.5*k*T) # average kinetic energy p**2/(2mass) = (3/2)kT
    theta = pi*random()
    phi = 2*pi*random()
    px = pavg*sin(theta)*cos(phi)
    py = pavg*sin(theta)*sin(phi)
    pz = pavg*cos(theta)
    poslist.append((x,y,z))
    plist.append((px,py,pz))
    mlist.append(mass)
    rlist.append(r)

pos = array(poslist)
p = array(plist)
m = array(mlist)
m.shape = (Natoms,1) # Numeric Python: (1 by Natoms) vs. (Natoms by 1)
radius = array(rlist)

pos = pos+(p/m)*(dt/2.) # initial half-step

k=47
while True:
    k+=1
    if k==2500:
        x=raw_input('Continue?')#this stops the display and allow us to make a screenshoot at fixed time.
        if x=='n':
            break
        k=0
    rate(50)
    observation.plot(data=mag(p/m))

    # Update all positions
    pos = pos+(p/m)*dt
 
    # Bounce off walls
    outside = less_equal(pos,Ratom) # walls closest to origin
    p1 = p*outside
    p = p-p1+abs(p1) # force p component inward
    outside = greater_equal(pos,L-Ratom) # walls farther from origin
    p1 = p*outside
    p = p-p1-abs(p1) # force p component inward

    # Update positions of display objects
    for i in range(Natoms):
        Atoms[i].pos = pos[i]