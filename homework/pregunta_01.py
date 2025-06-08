"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


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
    import pandas as pd
    import re
    
    # Read the file
    with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Split content into lines
    lines = content.split('\n')
    
    # Find the start of data (after the header and separator line)
    data_start = 0
    for i, line in enumerate(lines):
        if '---' in line:
            data_start = i + 1
            break
    
    # Extract data
    clusters = []
    cantidad_palabras = []
    porcentaje = []
    palabras_clave = []
    
    current_cluster = None
    current_keywords = []
    
    for line in lines[data_start:]:
        line = line.strip()
        if not line:
            continue
            
        # Check if line starts with a cluster number
        cluster_match = re.match(r'^\s*(\d+)\s+(\d+)\s+([\d,]+)\s*%\s*(.*)', line)
        if cluster_match:
            # If we have a previous cluster, save it
            if current_cluster is not None:
                clusters.append(current_cluster)
                cantidad_palabras.append(current_cantidad)
                porcentaje.append(current_porcentaje)
                # Clean and format keywords
                keywords_text = ' '.join(current_keywords)
                keywords_text = re.sub(r'\s+', ' ', keywords_text)  # Replace multiple spaces with single space
                keywords_text = re.sub(r'\s*,\s*', ', ', keywords_text)  # Normalize comma spacing
                keywords_text = keywords_text.strip().rstrip(',').rstrip('.')
                palabras_clave.append(keywords_text)
            
            # Start new cluster
            current_cluster = int(cluster_match.group(1))
            current_cantidad = int(cluster_match.group(2))
            current_porcentaje = float(cluster_match.group(3).replace(',', '.'))
            current_keywords = [cluster_match.group(4)]
        else:
            # Continuation of keywords
            if current_cluster is not None:
                current_keywords.append(line)
    
    # Don't forget the last cluster
    if current_cluster is not None:
        clusters.append(current_cluster)
        cantidad_palabras.append(current_cantidad)
        porcentaje.append(current_porcentaje)
        # Clean and format keywords
        keywords_text = ' '.join(current_keywords)
        keywords_text = re.sub(r'\s+', ' ', keywords_text)  # Replace multiple spaces with single space
        keywords_text = re.sub(r'\s*,\s*', ', ', keywords_text)  # Normalize comma spacing
        keywords_text = keywords_text.strip().rstrip(',').rstrip('.')
        palabras_clave.append(keywords_text)
    
    # Create DataFrame
    df = pd.DataFrame({
        'cluster': clusters,
        'cantidad_de_palabras_clave': cantidad_palabras,
        'porcentaje_de_palabras_clave': porcentaje,
        'principales_palabras_clave': palabras_clave
    })
    
    return df
