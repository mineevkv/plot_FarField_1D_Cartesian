from plot_functions import calc
import matplotlib.pyplot as plt

lens_diameter = 30

fig = plt.figure()
ax = fig.add_subplot(111)


theta, dBi, angular_3dB = calc('stage2/f220_phi0.txt')
plt.plot(theta, dBi, color='b', label='220 GHz $\\theta_{-3 \, dB} = ' + str(angular_3dB) + '\\degree$')

theta, dBi, angular_3dB = calc('stage2/f230_phi0.txt')
plt.plot(theta, dBi, color='r', label='230 GHz $\\theta_{-3 \, dB} = ' + str(angular_3dB) + '\\degree$')

theta, dBi, angular_3dB = calc('stage2/f240_phi0.txt')
plt.plot(theta, dBi, color='g', label='240 GHz $\\theta_{-3 \, dB} = ' + str(angular_3dB) + '\\degree$')

ax.legend()
ax.grid(which = "major", linewidth = 1)
ax.grid(which = "minor", linewidth = 0.2)
ax.minorticks_on()


ax.set_xlim(-30, 30)
ax.set_ylim(-10, 40)
ax.set_title(r'$D_{lens} = $' + str(lens_diameter) + r'$ \,mm;\, \varphi = 0\degree$')
ax.set_xlabel(r'$\theta$, degree')
ax.set_ylabel('dBi')
plt.show()
fig.savefig('stage2/phi0.png', dpi=300)

fig = plt.close()
fig = plt.figure()

ax = fig.add_subplot(111)

theta, dBi, angular_3dB = calc('stage2/f220_phi90.txt')
plt.plot(theta, dBi, color='b', label='220 GHz $\\theta_{-3 \,dB} = ' + str(angular_3dB) + '\\degree$')

theta, dBi, angular_3dB = calc('stage2/f230_phi90.txt')
plt.plot(theta, dBi, color='r', label='230 GHz $\\theta_{-3 \,dB} = ' + str(angular_3dB) + '\\degree$')

theta, dBi, angular_3dB = calc('stage2/f240_phi90.txt')
plt.plot(theta, dBi, color='g', label='240 GHz $\\theta_{-3 \,dB} = ' + str(angular_3dB) + '\\degree$')

ax.legend()
plt.grid()
ax.grid(which = "major", linewidth = 1)
ax.grid(which = "minor", linewidth = 0.2)
ax.minorticks_on()

ax.set_xlim(-30, 30)
ax.set_ylim(-10, 40)
ax.set_title(r'$D_{lens} = $' + str(lens_diameter) + r'$ \,mm;\, \varphi = 90\degree$')
ax.set_xlabel(r'$\theta$, degree')
ax.set_ylabel('dBi')
plt.show()

fig.savefig('stage2/phi90.png', dpi=300)
