

def calc(path):
    with open(path, 'r', encoding='UTF-8') as f:
        line_list = f.readlines()
        theta = []
        dBi = []
        for line in line_list[2:]:
            line = ' '.join(line.split())
            theta.append(float(line.split(' ')[0]))
            dBi.append(float(line.split(' ')[2]))

        main_lobe_mag = max(dBi)
        index = dBi.index(max(dBi))

        for i in range(index):
            if dBi[i] > main_lobe_mag - 3:
                theta1 = theta[i - 1]
                break

        for i in range(index):
            if dBi[i + index] < main_lobe_mag - 3:
                theta2 = theta[i + index - 1]
                break

        main_angular_3dB = abs(theta2) + abs(theta1)

    return theta, dBi, main_angular_3dB