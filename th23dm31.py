import scipy.interpolate    
import numpy as np  
import matplotlib.pyplot as plt
import matplotlib as mpl

N = 500 #number of points for plotting/interpolation    
x, y, z = np.genfromtxt(r'th23dm31.dat', unpack=True)
xll = x.min();  xul = x.max();  yll = y.min();  yul = y.max(); zll=z.min(); zul=z.max()

plt.figure(1, figsize=(10,10.0))


xi = np.linspace(xll, xul, N)
yi = np.linspace(yll, yul, N)
zi = scipy.interpolate.griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')



contours = plt.contour(xi, yi, zi, levels=(2.3, 6.18, 11.83), colors=('orange','red','violet'))
plt.clabel(contours, inline=True, fontsize=14)
image=plt.imshow(zi, extent=[xll, xul, yll, yul], origin='lower',aspect=(xul-xll)/(yul-yll), norm = mpl.colors.Normalize(vmin=0.,vmax=12.0), cmap=plt.cm.Blues_r)
clb=plt.colorbar(image,fraction=0.045, pad=0.045)
clb.set_label(r'$\chi^{2}}$', labelpad=-40, y=1.05,rotation=0,fontsize=18)
plt.ylabel(r'$\Delta m_{31}^{2}$ eV$^2$',fontsize=20)
plt.xlabel(r'$\theta_{23}$ $\degree$',fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.tick_params(axis='both', which='minor', labelsize=16)
plt.title(r'$\Delta m_{31}^{2}-\theta_{23}$', fontsize=22)
plt.tight_layout()
plt.savefig('theta23dm.pdf')
plt.show()

