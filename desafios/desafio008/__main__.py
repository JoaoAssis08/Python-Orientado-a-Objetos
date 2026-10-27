from classes import Quadrado, Circulo

def main():
    p1 = Quadrado(12)
    print(f"Perímetro = {p1.perimetro():.1f}")
    print(f"Area = {p1.area():.2f}")

    p2 = Circulo(5)
    print(f"Perímetro = {p2.perimetro():.1f}")
    print(f"Area = {p2.area():.2f}")

if __name__ == "__main__":
    main()