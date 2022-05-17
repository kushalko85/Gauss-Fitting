# Import required packages
import numpy as np
from scipy.optimize import curve_fit
import csv


#################
# Function to calculate the Gaussian with constants a, b, and c
def func(x, a, d):
    y = a * np.exp(-np.power(x - 2.29, 2) / (2 * np.power(0.17, 2))) + d * np.exp(
        -np.power(x - 2.49, 2) / (2 * np.power(0.12, 2)))
    return y


######## import data
csv_file = 'data PTCDI amp.csv'

Energy = []
Counts_1 = []
Counts_2 = []
Counts_3 = []
Counts_4 = []
Counts_5 = []
Counts_6 = []
Counts_7 = []
Counts_8 = []
Counts_9 = []
Counts_10 = []
Counts_11 = []
Counts_12 = []
Counts_13 = []
Counts_14 = []
Counts_15 = []
Counts_16 = []
Counts_17 = []
Counts_18 = []
Counts_19 = []
Counts_20 = []

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        Energy.append(row.get('Energy'))
        Counts_1.append(row.get('2'))
        Counts_2.append(row.get('10'))
        Counts_3.append(row.get('20'))
        Counts_4.append(row.get('40'))
        Counts_5.append(row.get('60'))
        Counts_6.append(row.get('80'))
        Counts_7.append(row.get('100'))
        Counts_8.append(row.get('120'))
        Counts_9.append(row.get('140'))
        Counts_10.append(row.get('160'))
        Counts_11.append(row.get('180'))
        Counts_12.append(row.get('200'))
        Counts_13.append(row.get('220'))
        Counts_14.append(row.get('240'))
        Counts_15.append(row.get('260'))
        Counts_16.append(row.get('280'))
        Counts_17.append(row.get('300'))
        Counts_18.append(row.get('1'))
        Counts_19.append(row.get('4'))
        Counts_20.append(row.get('3'))

# print(Energy)
Energy = list(map(float, Energy))
Counts_1 = list(map(float, Counts_1))
Counts_2 = list(map(float, Counts_2))
Counts_3 = list(map(float, Counts_3))
Counts_4 = list(map(float, Counts_4))
Counts_5 = list(map(float, Counts_5))
Counts_6 = list(map(float, Counts_6))
Counts_7 = list(map(float, Counts_7))
Counts_8 = list(map(float, Counts_8))
Counts_9 = list(map(float, Counts_9))
Counts_10 = list(map(float, Counts_10))
Counts_11 = list(map(float, Counts_11))
Counts_12 = list(map(float, Counts_12))
Counts_13 = list(map(float, Counts_13))
Counts_14 = list(map(float, Counts_14))
Counts_15 = list(map(float, Counts_15))
Counts_16 = list(map(float, Counts_16))
Counts_17 = list(map(float, Counts_17))
Counts_18 = list(map(float, Counts_18))
Counts_19 = list(map(float, Counts_19))
Counts_20 = list(map(float, Counts_20))

# Normalise
Counts_1 = [float(i) / sum(Counts_1) for i in Counts_1]
Counts_2 = [float(j) / sum(Counts_2) for j in Counts_2]
Counts_3 = [float(k) / sum(Counts_3) for k in Counts_3]
Counts_4 = [float(l) / sum(Counts_4) for l in Counts_4]
Counts_5 = [float(m) / sum(Counts_5) for m in Counts_5]
Counts_6 = [float(n) / sum(Counts_6) for n in Counts_6]
Counts_7 = [float(o) / sum(Counts_7) for o in Counts_7]
Counts_8 = [float(p) / sum(Counts_8) for p in Counts_8]
Counts_9 = [float(q) / sum(Counts_9) for q in Counts_9]
Counts_10 = [float(r) / sum(Counts_10) for r in Counts_10]
Counts_11 = [float(s) / sum(Counts_11) for s in Counts_11]
Counts_12 = [float(t) / sum(Counts_12) for t in Counts_12]
Counts_13 = [float(u) / sum(Counts_13) for u in Counts_13]
Counts_14 = [float(v) / sum(Counts_14) for v in Counts_14]
Counts_15 = [float(w) / sum(Counts_15) for w in Counts_15]
Counts_16 = [float(a) / sum(Counts_16) for a in Counts_16]
Counts_17 = [float(b) / sum(Counts_17) for b in Counts_17]
Counts_18 = [float(c) / sum(Counts_18) for c in Counts_18]
Counts_19 = [float(d) / sum(Counts_19) for d in Counts_19]
Counts_20 = [float(e) / sum(Counts_20) for e in Counts_20]

# print(Energy)

#################################
# plt.scatter(Energy, Counts)
##################################
# fit data
################################
parameters_1, covariance_1 = curve_fit(func, Energy, Counts_1, absolute_sigma=True,
                                       bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_2, covariance_2 = curve_fit(func, Energy, Counts_2, absolute_sigma=True,
                                       bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_3, covariance_3 = curve_fit(func, Energy, Counts_3, absolute_sigma=True,
                                       bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_4, covariance_4 = curve_fit(func, Energy, Counts_4, absolute_sigma=True,
                                       bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_5, covariance_5 = curve_fit(func, Energy, Counts_5, absolute_sigma=True,
                                       bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_6, covariance_6 = curve_fit(func, Energy, Counts_6, absolute_sigma=True,
                                       bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_7, covariance_7 = curve_fit(func, Energy, Counts_7, absolute_sigma=True,
                                       bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_8, covariance_8 = curve_fit(func, Energy, Counts_8, absolute_sigma=True,
                                       bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_9, covariance_9 = curve_fit(func, Energy, Counts_9, absolute_sigma=True,
                                       bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_10, covariance_10 = curve_fit(func, Energy, Counts_10, absolute_sigma=True,
                                         bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_11, covariance_11 = curve_fit(func, Energy, Counts_11, absolute_sigma=True,
                                         bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_12, covariance_12 = curve_fit(func, Energy, Counts_12, absolute_sigma=True,
                                         bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_13, covariance_13 = curve_fit(func, Energy, Counts_13, absolute_sigma=True,
                                         bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_14, covariance_14 = curve_fit(func, Energy, Counts_14, absolute_sigma=True,
                                         bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_15, covariance_15 = curve_fit(func, Energy, Counts_15, absolute_sigma=True,
                                         bounds=([0.0000001, 0.00000000001], [1, 1]))
parameters_16, covariance_16 = curve_fit(func, Energy, Counts_16, absolute_sigma=True,
                                         bounds=([0.0000000001, 0.0000000001], [1, 1]))
parameters_17, covariance_17 = curve_fit(func, Energy, Counts_17, absolute_sigma=True,
                                         bounds=([0.0000000001, 0.0000000001], [1, 1]))
parameters_18, covariance_18 = curve_fit(func, Energy, Counts_18, absolute_sigma=True,
                                         bounds=([0.0000000001, 0.0000000001], [1, 1]))
parameters_19, covariance_19 = curve_fit(func, Energy, Counts_19, absolute_sigma=True,
                                         bounds=([0.0000000001, 0.0000000001], [1, 1]))
parameters_20, covariance_20 = curve_fit(func, Energy, Counts_20, absolute_sigma=True,
                                         bounds=([0.0000000001, 0.0000000001], [1, 1]))

fit_A1 = parameters_1[0]
fit_D1 = parameters_1[1]
fit_A2 = parameters_2[0]
fit_D2 = parameters_2[1]
fit_A3 = parameters_3[0]
fit_D3 = parameters_3[1]

fit_A4 = parameters_4[0]
fit_D4 = parameters_4[1]
fit_A5 = parameters_5[0]
fit_D5 = parameters_5[1]
fit_A6 = parameters_6[0]
fit_D6 = parameters_6[1]

fit_A7 = parameters_7[0]
fit_D7 = parameters_7[1]
fit_A8 = parameters_8[0]
fit_D8 = parameters_8[1]
fit_A9 = parameters_9[0]
fit_D9 = parameters_9[1]

fit_A10 = parameters_10[0]
fit_D10 = parameters_10[1]
fit_A11 = parameters_11[0]
fit_D11 = parameters_11[1]
fit_A12 = parameters_12[0]
fit_D12 = parameters_12[1]

fit_A13 = parameters_13[0]
fit_D13 = parameters_13[1]
fit_A14 = parameters_14[0]
fit_D14 = parameters_14[1]
fit_A15 = parameters_15[0]
fit_D15 = parameters_15[1]

fit_A16 = parameters_16[0]
fit_D16 = parameters_16[1]
fit_A17 = parameters_17[0]
fit_D17 = parameters_17[1]
fit_A18 = parameters_18[0]
fit_D18 = parameters_18[1]

fit_A19 = parameters_19[0]
fit_D19 = parameters_19[1]
fit_A20 = parameters_20[0]
fit_D20 = parameters_20[1]

# plt.plot(fit_y5)
# plt.plot(Counts_10)

print(fit_A1, fit_A2, fit_A3, fit_A4, fit_A5, fit_A6, fit_A7, fit_A8, fit_A9, fit_A10, fit_A11, fit_A12, fit_A13,
      fit_A14, fit_A15, fit_A16, fit_A17, fit_A18, fit_A19, fit_A20)
print(fit_D1, fit_D2, fit_D3, fit_D4, fit_D5, fit_D6, fit_D7, fit_D8, fit_D9, fit_D10, fit_D11, fit_D12, fit_D13,
      fit_D14, fit_D15, fit_D16, fit_D17, fit_D18, fit_D19, fit_D20)
# print(fit_A1,fit_A2,fit_A3,fit_A4,fit_A5,fit_A6,fit_A7,fit_A8,fit_A9,fit_A10,fit_A11,fit_A12,fit_A13,fit_A14,fit_A15)
# print(fit_D1,fit_D2,fit_D3,fit_D4,fit_D5,fit_D6,fit_D7,fit_D8,fit_D9,fit_D10,fit_D11,fit_D12,fit_D13,fit_D14,fit_D15)
# print(fit_B1,fit_B2,fit_B3,fit_B4,fit_B5,fit_B6,fit_B7,fit_B8,fit_B9,fit_B10,fit_B11,fit_B12,fit_B13,fit_B14,fit_B15)
# print(fit_E1,fit_E2,fit_E3,fit_E4,fit_E5,fit_E6,fit_E7,fit_E8,fit_E9,fit_E10,fit_E11,fit_E12,fit_E13,fit_E14,fit_E15)
###########################