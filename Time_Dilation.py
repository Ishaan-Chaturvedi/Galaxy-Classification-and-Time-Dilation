c = 299792458
G = 6.674010551359E-11
M = 5.972E24
R = 6.371E6
v = 460

Q = int(input()) # no. of test cases
for i in range(Q):
    r = float(input())
    sr = (1-(G * M)/(r * c ** 2 )) ** (0.5)
    gr = (1- (2* G * M)/(r * c ** 2)) ** (0.5)
    t = ( 86400/((sr) + (gr) - 1) ) * ( (sr) + (gr) - (1-((460/c)**2))** (0.5)- (1 - ((2*G*M)/(R*c**(2))))**(0.5))
    print("{:e}".format(round(t, 5)))
    

