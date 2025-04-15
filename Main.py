import math

def calculate_ear(apr, n):
    ear = 5
    ear = math.pow((1 + apr/n),n)- 1
    print (round(ear, 4))
    return ear

def calculate_pv_annuity(C, r, t):
    pv = C / r * (1 - 1 / math.pow(1 + r, t))

    return pv

apr = 0.15
n = 12

calculate_ear(apr, n)
print(round(calculate_pv_annuity(1000, 0.01, 3), 4))