# Motor de Búsqueda TF-IDF para Reglamento académico

## Objetivo del Proyecto

Construir un motor de búsqueda que permita encontrar artículos específicos del reglamento (sobre becas, faltas disciplinarias, cancelaciones, etc.) utilizando **TF-IDF** para priorizar los fragmentos más relevantes.

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

El script busca el término **"futuro"** y muestra un ranking de documentos ordenados por relevancia:

```
IDF para el término 'futuro': 0.1823

 1 - Documento: Artículo 6: El Consejo Académico puede establecer diferentes períodos académicos como semestre, trimestre o anualidad.: TF-IDF = 0.0182
 2 - Documento: Artículo 22: Las asignaturas son homologables si cumplen al menos el 80% de equivalencia en contenido y tienen nota mínima aprobatoria.: TF-IDF = 0.0000
 ...
```

---

## Proceso Implementado

### Paso 1: Dataset Sugerido ✓
Se seleccionaron 10 textos cortos del reglamento que simulan artículos completos sobre:
- Programas de pregrado
- Créditos académicos
- Períodos académicos
- Admisión de estudiantes
- Homologación de asignaturas

### Paso 2: Funciones Implementadas ✓
Se crearon tres funciones principales:
1. **Calcular TF**: frecuencia_palabra / total_palabras_doc
2. **Calcular IDF**: log(Total_Docs / Docs_con_la_palabra)
3. **Calcular Score Final**: Suma del TF-IDF de cada palabra de la consulta

### Paso 3: Búsquedas y Resultados ✓
Se ejecutan búsquedas y se documenta:
- El **IDF** del término buscado
- El **ranking de documentos** ordenados por TF-IDF
- La **relevancia** de cada artículo para la consulta

---

## Interpretación de Resultados

- **Score TF-IDF alto**: El documento es muy relevante para la búsqueda
- **Score TF-IDF bajo o cero**: El documento es poco o no relevante
- **IDF alto**: El término es raro (aparece en pocos documentos)
- **IDF bajo**: El término es común (aparece en muchos documentos)

---

## Estructura del Código

```
a.py
├── Importar numpy
├── Dataset (10 artículos del reglamento)
├── Función: calcular_tf()
├── Función: calcular_idf()
├── Función: calcular_score_final()
├── Búsqueda y ranking
└── Visualización de resultados
```

---

## Autor
Proyecto de búsqueda TF-IDF para reglamento académico