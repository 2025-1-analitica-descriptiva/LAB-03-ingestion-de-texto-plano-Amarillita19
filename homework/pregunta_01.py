"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd  # type: ignore #ignore type

def pregunta_01():
  """
  Construya y retorne un dataframe de Pandas a partir del archivo
  'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

  - El dataframe tiene la misma estructura que el archivo original.
  - Los nombres de las columnas deben ser en minusculas, reemplazando los
  espacios por guiones bajos.
  - Las palabras clave deben estar separadas por coma y con un solo
  espacio entre palabra y palabra.


  """
  with open("files/input/clusters_report.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.readlines()

  inicio_datos = 4  # Índice donde comienzan los datos
  lineas_datos = contenido[inicio_datos:]

  lista_filas = []
  fila_temp = []

  for linea in lineas_datos:
        if linea.strip():  # Si la línea no está vacía, la añadimos a la fila temporal
            fila_temp.append(linea.strip())
        else:
            if fila_temp:  # Cuando encontramos una línea vacía, consolidamos la fila y la almacenamos
                lista_filas.append(" ".join(fila_temp))
                fila_temp = []

  datos_procesados = []
  for fila in lista_filas:
        elementos = fila.split()
        id_cluster = int(elementos[0])
        total_palabras = int(elementos[1])
        porcentaje_palabras = float(elementos[2].replace(",", "."))
        palabras_clave = (
            " ".join(elementos[3:])
            .replace(" ,", ",")
            .replace(", ", ", ")
            .strip("%")
            .rstrip(".")
            .strip()
        )
        datos_procesados.append([id_cluster, total_palabras, porcentaje_palabras, palabras_clave])

  df_resultado = pd.DataFrame(datos_procesados, columns=[
        "cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"
    ])

  return df_resultado
# Prueba la función
print(pregunta_01())