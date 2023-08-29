from plot_functions import calc
import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_subplot(111)
#
#
# theta, dBi, angular_3dB = calc('30GHz_Horn_Lens/f30_phi0_horn.txt')
# plt.plot(theta, dBi, color='b', label='Horn: $\\theta_{-3 \, dB} = 32.6\\degree$')
#
# theta, dBi, angular_3dB = calc('30GHz_Horn_Lens/f30_phi0_lensOpt.txt')
# plt.plot(theta, dBi, color='r', label='Lens: $\\theta_{-3 \, dB} = 9.5\\degree$')
#
# ax.legend()
# ax.grid(which = "major", linewidth = 1)
# ax.grid(which = "minor", linewidth = 0.2)
# ax.minorticks_on()
#
#
# ax.set_xlim(-90, 90)
# ax.set_ylim(-20, 30)
# ax.set_title(r'$f_{0} = 30$ GHz $\varphi = 0\degree$')
# ax.set_xlabel(r'$\theta$, degree')
# ax.set_ylabel('dBi')
# plt.show()
# fig.savefig('30GHz_Horn_Lens/phi0.png', dpi=300)
#
# fig = plt.close()
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
#
#
# theta, dBi, angular_3dB = calc('30GHz_Horn_Lens/f30_phi90_horn.txt')
# plt.plot(theta, dBi, color='b', label='Horn: $\\theta_{-3 \, dB} = 25.3\\degree$')
#
# theta, dBi, angular_3dB = calc('30GHz_Horn_Lens/f30_phi90_lensOpt.txt')
# plt.plot(theta, dBi, color='r', label='Lens: $\\theta_{-3 \, dB} = 10.0\\degree$')
#
# ax.legend()
# ax.grid(which = "major", linewidth = 1)
# ax.grid(which = "minor", linewidth = 0.2)
# ax.minorticks_on()
#
#
# ax.set_xlim(-90, 90)
# ax.set_ylim(-20, 30)
# ax.set_title(r'$f_{0} = 30$ GHz $\varphi = 90\degree$')
# ax.set_xlabel(r'$\theta$, degree')
# ax.set_ylabel('dBi')
# plt.show()
# fig.savefig('30GHz_Horn_Lens/phi90.png', dpi=300)
#
# fig = plt.close()

fig = plt.figure()
ax = fig.add_subplot(111)


theta, dBi, angular_3dB = calc('30GHz_Horn_Lens/f28_phi90_lensOpt.txt')
plt.plot(theta, dBi, color='b', label='28 GHz: $\\theta_{-3 \, dB} = 10.6\\degree$')

theta, dBi, angular_3dB = calc('30GHz_Horn_Lens/f30_phi90_lensOpt.txt')
plt.plot(theta, dBi, color='r', label='30 GHz $\\theta_{-3 \, dB} = 10.0\\degree$')

theta, dBi, angular_3dB = calc('30GHz_Horn_Lens/f32_phi90_lensOpt.txt')
plt.plot(theta, dBi, color='g', label='32 GHz $\\theta_{-3 \, dB} = 9.5\\degree$')

ax.legend()
ax.grid(which = "major", linewidth = 1)
ax.grid(which = "minor", linewidth = 0.2)
ax.minorticks_on()


ax.set_xlim(-90, 90)
ax.set_ylim(-20, 30)
ax.set_title(r'$\varphi = 90\degree$')
ax.set_xlabel(r'$\theta$, degree')
ax.set_ylabel('dBi')
plt.show()
fig.savefig('30GHz_Horn_Lens/all_lensOpt_phi90.png', dpi=300)

fig = plt.close()

fig = plt.figure()
ax = fig.add_subplot(111)


theta, dBi, angular_3dB = calc('30GHz_Horn_Lens/f28_phi0_lensOpt.txt')
plt.plot(theta, dBi, color='b', label='28 GHz: $\\theta_{-3 \, dB} = 10.1\\degree$')

theta, dBi, angular_3dB = calc('30GHz_Horn_Lens/f30_phi0_lensOpt.txt')
plt.plot(theta, dBi, color='r', label='30 GHz $\\theta_{-3 \, dB} = 9.5\\degree$')

theta, dBi, angular_3dB = calc('30GHz_Horn_Lens/f32_phi0_lensOpt.txt')
plt.plot(theta, dBi, color='g', label='32 GHz $\\theta_{-3 \, dB} = 8.9\\degree$')

ax.legend()
ax.grid(which = "major", linewidth = 1)
ax.grid(which = "minor", linewidth = 0.2)
ax.minorticks_on()


ax.set_xlim(-90, 90)
ax.set_ylim(-20, 30)
ax.set_title(r'$\varphi = 0\degree$')
ax.set_xlabel(r'$\theta$, degree')
ax.set_ylabel('dBi')
plt.show()
fig.savefig('30GHz_Horn_Lens/all_lensOpt_phi0.png', dpi=300)

fig = plt.close()