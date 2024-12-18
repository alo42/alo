def euclidian_alg(a, b):
    if b > a:
        temp = a
        a = b
        b = temp
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b

def decrypt():
    a = input('Enter the first key:')
    b = input('Enter the second key:')
    key1 = int(a, 16)
    key2 = int(b, 16)
    factor1 = euclidian_alg(key1, key2)
    factor2 = key1/factor1
    factor3 = key2/factor1
    maxim = max(factor1, factor2, factor3)
    print(maxim)

decrypt()