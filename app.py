import numpy as np

documents = [
"Artículo 1: Los programas de pregrado deben garantizar formación científica, tecnológica, humanística y ética con enfoque en solución de problemas actuales.",
"Artículo 2: Un crédito académico equivale a 48 horas de trabajo del estudiante, incluyendo actividades con docente e independientes.",
"Artículo 3: El número de créditos de cada asignatura es definido por el Consejo Académico.",
"Artículo 4: Los créditos académicos se calculan dividiendo por 48 el total de horas requeridas para el aprendizaje.",
"Artículo 5: La institución distingue entre créditos obligatorios y electivos según la naturaleza del programa.",
"Artículo 6: El Consejo Académico puede establecer diferentes períodos académicos como semestre, trimestre o anualidad.",
"Artículo 7: Cada período académico tiene duración definida en semanas según normativa institucional.",
"Artículo 10: La institución selecciona estudiantes sin discriminación, bajo criterios definidos por el Consejo Académico.",
"Artículo 11: Los aspirantes deben cumplir requisitos como formulario, diploma, examen de Estado, identificación y pago de inscripción.",
"Artículo 22: Las asignaturas son homologables si cumplen al menos el 80% de equivalencia en contenido y tienen nota mínima aprobatoria."
]

# Función para calcular TF: frecuencia_palabra / total_palabras_doc
def calcular_tf(palabra, documento):
    total_palabras = len(documento.split())
    frecuencia = documento.count(palabra)
    return frecuencia / total_palabras if total_palabras > 0 else 0

# Función para calcular IDF: log(Total_Docs / Docs_con_la_palabra)
def calcular_idf(palabra, documentos):
    total_docs = len(documentos)
    docs_con_palabra = sum(1 for doc in documentos if palabra in doc)
    return np.log(total_docs / docs_con_palabra) if docs_con_palabra > 0 else 0

# Función para calcular Score Final: suma del TF-IDF de cada palabra
def calcular_score_final(consulta, documento):
    palabras = consulta.split()
    score = 0
    for palabra in palabras:
        tf = calcular_tf(palabra, documento)
        idf = calcular_idf(palabra, documents)
        score += tf * idf
    return score

# Solicitar palabra de búsqueda
termino_buscado = input("Ingrese el término a buscar: ")
idf = calcular_idf(termino_buscado, documents)
print(f"IDF para el término '{termino_buscado}': {idf:.4f}")

# Calcular TF-IDF para cada documento
scores = []
for i, doc in enumerate(documents):
    tf = calcular_tf(termino_buscado, doc)
    tf_idf = tf * idf
    scores.append((i+1, tf_idf, doc))

scores.sort(key=lambda x: x[1], reverse=True)

# Mostrar resultados
for i, (doc_id, tf_idf, doc) in enumerate(scores, 1):
    print(f" {i} - Documento: {doc}: TF-IDF = {tf_idf:.4f}")