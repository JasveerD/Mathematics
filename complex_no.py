# input the 2 complex numbers as two different lists
# the first element of the list is the real coefficient and the second element is the imaginary coefficient

def iproduct(a, b):
    real = a[0] * b[0] - (a[1] * b[1])
    imaginary = a[0] * b[1] + (a[1] * b[0])
    print(str(real) + ' + ' + str(imaginary) + '𝒊')
    return (real, imaginary)

def fac(n):
    result = 1
    for i in range(1, n):
        result = result * i
    return result

def sumAP(a, d, n):
    sum = n/2 * (2*a + (n-1)*d)
    return sum

