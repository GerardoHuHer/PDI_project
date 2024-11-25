'''
 Código del algoritmo de la división.
'''

def division(a: int, b: int) -> tuple:
    if b == 0:
        return (0,0)
    abs = lambda x: x if x >= 0 else x * -1
    if a == 0:
        quotient = 0
        remainder = 0
    else:
        r = abs(a)
        q = 0
        while r >= b:
            r = r - b
            q = q + 1
        if a > 0: 
            quotient = q
            remainder = r
        elif r ==0:
            quotient = -q
            remainder = 0
        else:
            quotient = -q - 1
            remainder = b - r
        return (q, r)
    
if __name__ == "__main__":
    quotient, remainder = division(10, 5)
    print(f"Cociente: {quotient} \nResiduo: {remainder}")