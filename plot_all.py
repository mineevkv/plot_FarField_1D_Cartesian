from plot_functions import calc
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111)


theta, dBi, angular_3dB = calc('stage2/f230_phi0.txt')
plt.plot(theta, dBi, color='b', label='30 mm $\\theta_{-3 \, dB} = ' + str(angular_3dB) + '\\degree$')

theta, dBi, angular_3dB = calc('stage1/f230_phi0.txt')
plt.plot(theta, dBi, color='r', label='40 mm $\\theta_{-3 \, dB} = ' + str(angular_3dB) + '\\degree$')

theta, dBi, angular_3dB = calc('stage3/f230_phi0.txt')
plt.plot(theta, dBi, color='g', label='60 mm $\\theta_{-3 \, dB} = ' + str(angular_3dB) + '\\degree$')

ax.legend()
ax.grid(which = "major", linewidth = 1)
ax.grid(which = "minor", linewidth = 0.2)
ax.minorticks_on()


ax.set_xlim(-30, 30)
ax.set_ylim(-15, 45)
ax.set_title(r'$f$ = 230 GHz, $\varphi = 0\degree$')
ax.set_xlabel(r'$\theta$, degree')
ax.set_ylabel('dBi')
plt.show()
fig.savefig('all/phi0.png', dpi=300)


fig = plt.close()
fig = plt.figure()
ax = fig.add_subplot(111)

theta, dBi, angular_3dB = calc('stage2/f230_phi90.txt')
plt.plot(theta, dBi, color='b', label='30 mm $\\theta_{-3 \, dB} = ' + str(angular_3dB) + '\\degree$')

theta, dBi, angular_3dB = calc('stage1/f230_phi90.txt')
plt.plot(theta, dBi, color='r', label='40 mm $\\theta_{-3 \, dB} = ' + str(angular_3dB) + '\\degree$')

theta, dBi, angular_3dB = calc('stage3/f230_phi90.txt')
plt.plot(theta, dBi, color='g', label='60 mm $\\theta_{-3 \, dB} = ' + str(angular_3dB) + '\\degree$')

ax.legend()
ax.grid(which = "major", linewidth = 1)
ax.grid(which = "minor", linewidth = 0.2)
ax.minorticks_on()


ax.set_xlim(-30, 30)
ax.set_ylim(-15, 45)
ax.set_title(r'$f$ = 230 GHz, $\varphi = 90\degree$')
ax.set_xlabel(r'$\theta$, degree')
ax.set_ylabel('dBi')
plt.show()
fig.savefig('all/phi90.png', dpi=300)