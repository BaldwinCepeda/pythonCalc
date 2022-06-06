import math


print('Ovix interest rate')
print(
    'Please insert the following param {R_optim, U_optim, r_Max, Kink_factor}')

# function parameters
# r_Optim : Target borrow rate at optimal utilization
r_Optim = 1
# u_Optim : Target optimal utilization (typically U_Optim = 0.8)
u_Optim = 0.8
# r_Max : Maximal borrow rate when utilization is 100% (typically R_max = 1)
r_Max = 1
# kink : Kink factor. Larger kink values lead to a sharper rise in rates for u > U_optim.
kink = 2
# U : Utilization of the lending pool. (Borrow/supply)
Utilization = 0


# r_Optim / U_optim function
def ru_OptimDiv(r_Optim, u_Optim):
    return r_Optim/u_Optim


#r_max - ru_OptimDivision
def maxMinru(rMax, r_Optim, u_Optim):
    return rMax - ru_OptimDiv(r_Optim, u_Optim)


# main function
def interest_Rate(util):
    print(ru_OptimDiv(25, 5) * util + (maxMinru(2, 1, 1) * pow(util, kink)))
    print("Ovix interest rate--------DATA-------")


# input params below
interest_Rate(2)
