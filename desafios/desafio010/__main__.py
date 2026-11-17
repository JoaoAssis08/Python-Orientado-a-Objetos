from Transportes import *

dist = 10

def main():
    entrega = Drone(dist)
    print(f"Frete de {type(entrega).__name__} em {entrega.distancia}Km = {entrega.calc_frete()}")

if __name__ == "__main__":
    main()
