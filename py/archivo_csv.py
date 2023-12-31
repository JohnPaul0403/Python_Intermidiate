#Como crear archivos csv
import os
import csv
import pathlib as pl

def agregar_peliculas(nombre_archivo):
    q = int(input("N. de peliculas: "))
    campos = ["Titulo", "Duracion", "Year"]
    if not pl.Path(nombre_archivo).exists():
        with open(nombre_archivo, "a", newline='') as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=campos)
            writer.writeheader()

    with open(nombre_archivo, "a", newline='') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=campos)
        for i in range(q):
            os.system("clear")
            titulo = input("titulo: ")
            duracion = input("duracion: ")
            year = input("year: ")
            writer.writerow({'Titulo':titulo, 'Duracion':duracion, 'Year':year})

def mostrar_peliculas(nombre_archivo):
    os.system("clear")
    print("     Pelis ")
    
    with open(nombre_archivo, "r", newline='') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for linea in reader:
            for campo, valor in linea.items():
                print(f'{campo}: {valor}')
            print("~"*50)

def main():
    archivo_csv = 'pelis.csv'
    agregar_peliculas(archivo_csv)
    mostrar_peliculas(archivo_csv)

if __name__ == "__main__":
    main()
