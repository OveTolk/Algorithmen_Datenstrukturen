# Dieses Programm berechnet interativ die Potenz einer Zahl

def potenz(basis, exponent):
    zahl = basis
    for i in range(1, exponent):
        basis = basis * zahl
    return basis

def main():
    basis = int(input("Bitte geben Sie die Basis ein: "))
    exponent = int(input("Bitte geben Sie den Exponenten ein: "))
    print("Die Potenz von", basis, "hoch", exponent, "ist", potenz(basis, exponent))

main()