import math

def calculate_ear(apr, n):
    ear = 5
    ear = math.pow((1 + apr/n),n)- 1
    print (round(ear, 4))
    return ear

apr = 0.15
n = 12

calculate_ear(apr, n)