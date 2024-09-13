# English Learning Game for Kids (KIDSIZZ)

Este proyecto es una aplicación interactiva para niños diseñada para ayudarles a aprender conceptos básicos del inglés, como colores, números, animales y preguntas de gramática. La aplicación utiliza la cámara para detectar las manos del usuario, lo que permite seleccionar las respuestas sin necesidad de un teclado o ratón. Es un juego didáctico y divertido que fomenta el aprendizaje interactivo.

## Características

- **Aprendizaje de conceptos básicos**: Incluye cuestionarios sobre animales, colores, números y preguntas gramaticales.
- **Interacción mediante la cámara**: Los usuarios pueden seleccionar respuestas utilizando gestos de la mano detectados por la cámara.
- **Evaluación instantánea**: Muestra los resultados al finalizar cada cuestionario, con un mensaje motivador en función del puntaje.
- **Visuales llamativos**: Pantallas de bienvenida y mensajes finales con imágenes y mensajes personalizados.
  
## Requisitos del Sistema

- Python 3.x
- Librerías de Python:
  - `cv2` (OpenCV)
  - `cvzone`
  - `numpy`
  - `tkinter`
  - `csv`
  
## Instalación

1. **Clona este repositorio**:
    ```bash
    git clone https://github.com/tu-usuario/english-learning-game.git
    cd english-learning-game
    ```

2. **Instala las dependencias**:
    ```bash
    pip install opencv-python-headless
    pip install cvzone
    pip install numpy
    ```

3. **Configura la cámara**:
    Asegúrate de que la cámara de tu computadora esté funcionando, ya que se utiliza para interactuar con el juego.

## Uso

1. **Inicia la aplicación**:
    ```bash
    python main.py
    ```

2. **Pantalla de bienvenida**: La aplicación comenzará mostrando una pantalla de bienvenida. Presiona cualquier tecla para seleccionar un archivo CSV con preguntas.

3. **Selección de juego**: Podrás seleccionar entre diferentes cuestionarios:
    - Animales
    - Colores
    - Números
    - Preguntas gramaticales

4. **Responder preguntas**: Utiliza los gestos de tu mano para seleccionar la respuesta correcta. El cursor seguirá tu dedo índice y detectará cuando hagas una selección.

5. **Resultados**: Al finalizar el cuestionario, se mostrará una pantalla con tu puntaje y un mensaje motivador según el resultado obtenido.

## Archivos CSV de Preguntas

Los archivos CSV contienen las preguntas y respuestas para cada cuestionario. Cada fila representa una pregunta con sus respectivas opciones y la respuesta correcta. Aquí hay un ejemplo del formato:

```csv
Pregunta, Opción 1, Opción 2, Opción 3, Opción 4, Respuesta
"What color is the sky?", "Blue", "Red", "Green", "Yellow", 1
