#!/usr/bin/python3
#from datetime import datetime
from multiprocessing import Pool
from matplotlib import pyplot as plt
import numpy as np

#start_time = datetime.now()
x = np.linspace(0,50,1000) #x_0
fact = np.linspace(0,5,960) #num frames
f = lambda x: np.sin(x**.9)
g = lambda x: np.cos(2*x + np.sqrt(x))
area = x*30
#evaluate f(x) and g(x) here once, then slice them for each frame in make_image
fx = f(x)
gx = g(x)

def make_image(inp = (1,0.5)):
    i,ff = inp
    #i = index of fact (from enumerate)
    x_adjust = np.append(x[i:], x[:i])[:40]
    fx_adjust = np.append(fx[i:], fx[:i])[:40]
    gx_adjust = np.append(gx[i:], gx[:i])[:40]
    plt.figure(i)
    plt.scatter(fx_adjust, gx_adjust, s=area, c=x_adjust, cmap='coolwarm')
    #plt.scatter(f(x_adjust), g(x_adjust), s=area, c=x_adjust, cmap='coolwarm', edgecolors='face')
    plt.title("Snake Movie: g(x) vs f(x)")
    plt.xlabel('f(x)')
    plt.ylabel('g(x)')
    plt.xlim(-1.05, 1.05) #so the snake can have some room to move :)
    plt.ylim(-1.05, 1.05)
    plt.savefig('snake'+str(i).zfill(6)+".png")
    plt.close(i)
    
p = Pool(6)
p.map(make_image,enumerate(fact))
#print("time: ", datetime.now()-start_time)