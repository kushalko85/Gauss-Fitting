# Import required packages
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import csv
import sys


# Function to calculate the Gaussian with constants a, b, and c
def func(x, a, b, c, d, e, f):
    y = a * np.exp(-np.power(x - b, 2) / (2 * np.power(c, 2))) + d * np.exp(-np.power(x - e, 2) / (2 * np.power(f, 2)))
    return y


# import data
csv_file = 'PTCDA/data PTCDI.csv'

Energy = []
Counts_1 = []
Counts_2 = []
Counts_3 = []
Counts_4 = []
Counts_5 = []

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        Energy.append(row.get('Energy'))
        Counts_1.append(row.get('1ps'))
        Counts_2.append(row.get('10ps'))
        Counts_3.append(row.get('30ps'))
        Counts_4.append(row.get('100ps'))
        Counts_5.append(row.get('280ps'))

# print(Energy)
Energy = list(map(float, Energy))
Counts_1 = list(map(float, Counts_1))
Counts_2 = list(map(float, Counts_2))
Counts_3 = list(map(float, Counts_3))
Counts_4 = list(map(float, Counts_4))
Counts_5 = list(map(float, Counts_5))

# Normalise
Counts_1 = [float(i) / sum(Counts_1) for i in Counts_1]
Counts_2 = [float(j) / sum(Counts_2) for j in Counts_2]
Counts_3 = [float(k) / sum(Counts_3) for k in Counts_3]
Counts_4 = [float(l) / sum(Counts_4) for l in Counts_4]
Counts_5 = [float(m) / sum(Counts_5) for m in Counts_5]


# fit data
################################
parameters_1, covariance_1 = curve_fit(func, Energy, Counts_1, absolute_sigma=True, bounds=(
    [0.0000001, 2.499999999, 0.085, 0.00000001, 2.6099999999999, 0.1101], [1, 2.5000000000001, 0.08500000001, 1, 2.610000001, 0.114]))
parameters_2, covariance_2 = curve_fit(func, Energy, Counts_2, absolute_sigma=True, bounds=(
    [0.0000001, 2.499999999, 0.085, 0.00000001, 2.6099999999999, 0.1101], [1, 2.50000000000019, 0.08500000001, 1, 2.610000001, 0.114]))
parameters_3, covariance_3 = curve_fit(func, Energy, Counts_3, absolute_sigma=True, bounds=(
    [0.0000001, 2.499999999, 0.085, 0.00000001, 2.6099999999999, 0.1101], [1, 2.5000000000001, 0.08500000001, 1, 2.610000001, 0.114]))
parameters_4, covariance_4 = curve_fit(func, Energy, Counts_4, absolute_sigma=True, bounds=(
    [0.0000001, 2.499999999, 0.085, 0.00000001, 2.6099999999999, 0.1101], [1, 2.5000000000001, 0.08500000001, 1, 2.610000001, 0.114]))
parameters_5, covariance_5 = curve_fit(func, Energy, Counts_5, absolute_sigma=True, bounds=(
    [0.0000001, 2.499999999, 0.085, 0.00000001, 2.6099999999999, 0.1101], [1, 2.5000000000001, 0.08500000001, 1, 2.610000001, 0.114]))

fit_A1 = parameters_1[0]
fit_B1 = parameters_1[1]
fit_C1 = parameters_1[2]
fit_D1 = parameters_1[3]
fit_E1 = parameters_1[4]
fit_F1 = parameters_1[5]

fit_A2 = parameters_2[0]
fit_B2 = parameters_2[1]
fit_C2 = parameters_2[2]
fit_D2 = parameters_2[3]
fit_E2 = parameters_2[4]
fit_F2 = parameters_2[5]

fit_A3 = parameters_3[0]
fit_B3 = parameters_3[1]
fit_C3 = parameters_3[2]
fit_D3 = parameters_3[3]
fit_E3 = parameters_3[4]
fit_F3 = parameters_3[5]

fit_A4 = parameters_4[0]
fit_B4 = parameters_4[1]
fit_C4 = parameters_4[2]
fit_D4 = parameters_4[3]
fit_E4 = parameters_4[4]
fit_F4 = parameters_4[5]

fit_A5 = parameters_5[0]
fit_B5 = parameters_5[1]
fit_C5 = parameters_5[2]
fit_D5 = parameters_5[3]
fit_E5 = parameters_5[4]
fit_F5 = parameters_5[5]

m1 = (fit_B1 + fit_B2 + fit_B3 + fit_B4 + fit_B5) / 5
m2 = (fit_E1 + fit_E3 + fit_E4 + fit_E2 + fit_E5) / 5
m3 = (fit_C1 + fit_C2 + fit_C3 + fit_C4 + fit_C5) / 5
m4 = (fit_F1 + fit_F2 + fit_F3 + fit_F4 + fit_F5) / 5
print(m1, m2, m3, m4)

fit_y1 = func(Energy, fit_A1, fit_B1, fit_C1, fit_D1, fit_E1, fit_F1)
fit_y2 = func(Energy, fit_A2, fit_B2, fit_C2, fit_D2, fit_E2, fit_F2)
fit_y3 = func(Energy, fit_A3, fit_B3, fit_C3, fit_D3, fit_E3, fit_F3)
fit_y4 = func(Energy, fit_A4, fit_B4, fit_C4, fit_D4, fit_E4, fit_F4)
fit_y5 = func(Energy, fit_A5, fit_B5, fit_C5, fit_D5, fit_E5, fit_F5)

R1 = fit_A1 / (fit_A1 + fit_D1)
R2 = fit_A2 / (fit_A2 + fit_D2)
R3 = fit_A3 / (fit_A3 + fit_D3)
R4 = fit_A4 / (fit_A4 + fit_D4)
R5 = fit_A5 / (fit_A5 + fit_D5)

#####write lists to txt file
textfile = open("PTCDA/Output/280ps-msf_file.txt", "w")
for element in fit_y5:
    textfile.write(str(element) + "\n")
textfile.close()


textfile = open("PTCDA/Output/100ps-msf_file.txt", "w")
for element in fit_y4:
    textfile.write(str(element) + "\n")
textfile.close()


textfile = open("PTCDA/Output/30ps-msf_file.txt", "w")
for element in fit_y3:
    textfile.write(str(element) + "\n")
textfile.close()


textfile = open("PTCDA/Output/10ps-msf_file.txt", "w")
for element in fit_y2:
    textfile.write(str(element) + "\n")
textfile.close()

textfile = open("PTCDA/Output/1ps-msf_file.txt", "w")
for element in fit_y1:
    textfile.write(str(element) + "\n")
textfile.close()

#############################

plt.plot(Energy, Counts_1, 'ro', label='data_1')
plt.plot(Energy, Counts_2, 'yo', label='data_2')
plt.plot(Energy, Counts_3, 'go', label='data_3')
plt.plot(Energy, Counts_4, 'bo', label='data_4')
plt.plot(Energy, Counts_5, 'ko', label='data_5')
plt.plot(Energy, fit_y1, 'r-', label='fit1')
plt.plot(Energy, fit_y2, 'y-', label='fit2')
plt.plot(Energy, fit_y3, 'g-', label='fit3')
plt.plot(Energy, fit_y4, 'b-', label='fit4')
plt.plot(Energy, fit_y5, 'k-', label='fit5')
plt.legend()
plt.savefig("PTCDA/Output/free-msf_fit.png")
plt.show()

original_stdout = sys.stdout
with open('PTCDA/Output/parameters-msf-ratio.txt', 'w') as f:
    sys.stdout = f  # Change the standard output to the file we created.
    print('Parameters =', parameters_1, parameters_2, parameters_3, parameters_4, parameters_5)
    print('Ratios =', R1, R2, R3, R4, R5)
    print('averages = ', m1, m2, m3, m4)
    sys.stdout = original_stdout
