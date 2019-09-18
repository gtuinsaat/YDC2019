# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:00:44 2019

@author: ufuky
"""

import math
import numpy as np
import matplotlib.pyplot as plt

pi = math.pi

# - Baslangic kosullari
u0=0.1;#[m] - Basglangic yer degistirmesi u(t=0)
v0=5.0;#[m/s] - Baslangic hizi v(t=0)

# - Dinamik ozellikler
Tn=0.5;#[s] - Titresim periyodu
wn=2*pi/Tn;#[rad/s] - Acisal frekans

print("wn=" + str(wn)+"[rad/s]")

# - Sekil parametreleri
numCycs=4;#[-] - Cevrim sayisi
plotDt=Tn/30;#[-] - Sekil icin zaman adimi suresi
fntSz=20;#[pt] - Sekil eksen font buyuklugu

# - Hesaplarin basglangici
t=np.arange(0,numCycs*Tn+plotDt,plotDt)

ut1=u0*np.cos(wn*t)
ut2=v0/wn*np.sin(wn*t)
ut=ut1+ut2;

# - Cizimin baslangici
plt.plot(t,ut1,'k-',linewidth=2,label='1. Terim')
plt.plot(t,ut2,'r-',linewidth=2,label='2. Terim')
plt.plot(t,ut,'g-',linewidth=2,label='Toplam')

ax0=plt.gca();
ax0.grid(True)
ax0.legend(fontsize=fntSz);
ax0.set_xlabel('Zaman, t [s]',fontsize=fntSz)
ax0.set_ylabel('Yer degistirme, u(t) [m]',fontsize=fntSz)
ax0.tick_params(labelsize=fntSz)
ax0.set_xlim(t[0],t[-1])
ax0.set_title('Tn='+str(Tn)+'[s], u(0)='+str(u0)+'[m], v(0)=' \
              +str(v0)+'[m/s]'  ,fontsize=fntSz)











