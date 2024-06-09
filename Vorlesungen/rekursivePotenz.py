# Dieses Programm berechnet die Potenz einer Zahl rekursiv

def potenz(basis, exponent):
    if exponent == 0:
        return 1
    else:
        return basis * potenz(basis, exponent - 1)
    
def main():
    basis = int(input("Bitte geben Sie die Basis ein: "))
    exponent = int(input("Bitte geben Sie den Exponenten ein: "))
    print("Die Potenz von", basis, "hoch", exponent, "ist", potenz(basis, exponent))

main()