import argparse
import joblib

# import numpy as np


def main():
    # Creamos un objeto ArgumentParser con una descripción
    parser = argparse.ArgumentParser(description="Ejemplo de uso de argparse")

    # Agregamos un argumento opcional para la edad del usuario
    parser.add_argument("--in_dataset_filename", type=str)

    parser.add_argument("--out_dataset_filename", type=str)

    # Parseamos los argumentos de la línea de comandos
    args = parser.parse_args()

    # Accedemos a los argumentos y los utilizamos
    in_name = args.in_dataset_filename
    out_name = args.out_dataset_filename

    df = joblib.load(in_name)
    joblib.dump(df["prob arr"], out_name)


if __name__ == "__main__":
    main()
