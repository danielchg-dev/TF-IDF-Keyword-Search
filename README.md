# Motor de Búsqueda TF-IDF para Reglamento académico

## Objetivo del Proyecto

Construir un motor de búsqueda que permita encontrar artículos específicos del reglamento universitario (sobre becas, faltas disciplinarias, cancelaciones, etc.) utilizando **TF-IDF** para priorizar los fragmentos más relevantes.

El algoritmo TF-IDF (Term Frequency-Inverse Document Frequency) calcula la importancia de una palabra en un documento respecto a una colección completa de documentos, permitiendo identificar qué artículos son más relevantes para una búsqueda dada.

---

## Componentes del Proyecto

### 1. Dataset: Artículos del Reglamento
Se incluyen 10 artículos del reglamento simulando documentos reales sobre:
- Formación académica
- Créditos académicos
- Períodos académicos
- Admisión de estudiantes
- Homologación de asignaturas

### 2. Funciones Implementadas

#### `calcular_tf(palabra, documento)`
Calcula el **Term Frequency (TF)** de una palabra en un documento.
```
TF = frecuencia_palabra / total_palabras_documento
```
- **Entrada**: palabra (str), documento (str)
- **Salida**: float entre 0 y 1

#### `calcular_idf(palabra, documentos)`
Calcula el **Inverse Document Frequency (IDF)** de una palabra.
```
IDF = log(Total_Documentos / Documentos_con_la_palabra)
```
- **Entrada**: palabra (str), lista de documentos (list)
- **Salida**: float (logaritmo natural)

#### `calcular_score_final(consulta, documento)`
Calcula el **Score TF-IDF final** sumando el TF-IDF de cada palabra en la consulta.
```
Score_Final = Σ (TF × IDF) para cada palabra de la consulta
```
- **Entrada**: consulta (str), documento (str)
- **Salida**: float (puntuación total)

---

## Cómo Ejecutar el Proyecto

### Requisitos
- Python 3.7+
- NumPy

### Instalación
```bash
pip install numpy
```

### Ejecución
```bash
python app.py
```

---

## Ejemplo de Uso

El script busca el término ingresado por consola y muestra un ranking de documentos ordenados por relevancia:

```
Ingrese el término a buscar: Consejo
IDF para el término 'Consejo': 1.2040
 1 - Documento: Artículo 3: El número de créditos de cada asignatura es definido por el Consejo Académico.: TF-IDF = 0.0803
 2 - Documento: Artículo 6: El Consejo Académico puede establecer diferentes períodos académicos como semestre, trimestre o anualidad.: TF-IDF = 0.0803
 3 - Documento: Artículo 10: La institución selecciona estudiantes sin discriminación, bajo criterios definidos por el Consejo Académico.: TF-IDF = 0.0803
 4 - Documento: Artículo 1: Los programas de pregrado deben garantizar formación científica, tecnológica, humanística y ética con enfoque en solución de problemas actuales.: TF-IDF = 0.0000
 5 - Documento: Artículo 2: Un crédito académico equivale a 48 horas de trabajo del estudiante, incluyendo actividades con docente e independientes.: TF-IDF = 0.0000
 6 - Documento: Artículo 4: Los créditos académicos se calculan dividiendo por 48 el total de horas requeridas para el aprendizaje.: TF-IDF = 0.0000
 7 - Documento: Artículo 5: La institución distingue entre créditos obligatorios y electivos según la naturaleza del programa.: TF-IDF = 0.0000
 8 - Documento: Artículo 7: Cada período académico tiene duración definida en semanas según normativa institucional.: TF-IDF = 0.0000
 9 - Documento: Artículo 11: Los aspirantes deben cumplir requisitos como formulario, diploma, examen de Estado, identificación y pago de inscripción.: TF-IDF = 0.0000
 10 - Documento: Artículo 22: Las asignaturas son homologables si cumplen al menos el 80% de equivalencia en contenido y tienen nota mínima aprobatoria.: TF-IDF = 0.0000
```

---

## Ejemplos de ejecución
<img width="1851" height="409" alt="image" src="https://github.com/user-attachments/assets/6c3e1ccc-3be6-442b-97e5-a85c65c3171f" />
<img width="1861" height="390" alt="image" src="https://github.com/user-attachments/assets/c2e7875a-80e2-402f-9b40-1ca49601c8f4" />
<img width="1843" height="384" alt="image" src="https://github.com/user-attachments/assets/2533274c-423c-4f78-bc66-b525b87bfb32" />

---
## Interpretación de Resultados

- **Score TF-IDF alto**: El documento es muy relevante para la búsqueda
- **Score TF-IDF bajo o cero**: El documento es poco o no relevante
- **IDF alto**: El término es raro (aparece en pocos documentos)
- **IDF bajo**: El término es común (aparece en muchos documentos)

---

## Estructura del Código

```
app.py
├── Importar numpy
├── Dataset (10 artículos del reglamento)
├── Función: calcular_tf()
├── Función: calcular_idf()
├── Función: calcular_score_final()
├── Búsqueda y ranking
└── Visualización de resultados
```

---

## Autores
- Daniel Felipe Chávez González
- Rodrigo Muñoz Andrade
