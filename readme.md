docker build -t transcribe-service .
docker run -p 5000:5000 transcribe-service


file: selecciona un archivo .opus, .mp3, etc.
model: tiny, base, small, medium, large (opcional).
language: especifica un lenguaje como es para español (opcional).
format: txt o pdf (opcional).


Explicación de la Estructura
application/: Contiene los servicios que implementan la lógica de la aplicación. Aquí se encuentran las reglas de negocio y casos de uso. Ejemplos:

transcription_service.py: Lógica relacionada con la transcripción de audios.
conversion_service.py: Lógica relacionada con la conversión de formatos de audio.
domain/: Define los modelos y las entidades del dominio. Aquí colocas las clases que representan conceptos principales en tu sistema:

transcription.py: Entidad que representa una transcripción.
audio_file.py: Entidad que representa un archivo de audio.
infrastructure/: Contiene la interacción con tecnologías externas y frameworks. Por ejemplo:

transcription_controller.py: Controlador que maneja las solicitudes HTTP (Flask).
opus_converter.py: Implementación de conversión de archivos .opus a otros formatos.
flask_app.py: Configuración e inicialización de Flask.
shared/: Coloca las utilidades compartidas, como manejo de excepciones y funciones comunes.

exceptions.py: Manejo de errores y excepciones personalizadas.
utils.py: Funciones comunes y de ayuda.
tests/: Carpetas para las pruebas unitarias de los servicios. Aquí puedes verificar que los servicios funcionan como se espera independientemente de la infraestructura.



TranscriptionService y ConversionService: Se encargan de manejar la lógica del negocio en torno a la transcripción y conversión de archivos de audio.
Transcription y AudioFile: Modelos que representan las entidades clave dentro del dominio de la aplicación.
TranscriptionController: Controlador responsable de manejar las solicitudes HTTP para la transcripción.
OpusConverter: Clase responsable de la conversión de archivos .opus a .wav.
FlaskApp: Archivo principal para configurar e iniciar la aplicación Flask.
Exceptions: Manejo centralizado de excepciones específicas de la aplicación.
Utils: Funciones de utilidad, como eliminación de archivos temporales.
Tests: Plantillas de pruebas unitarias para verificar la funcionalidad de los servicios.


https://github.com/MarceloTigrero/Transcribe_Service_Open

---------------------CREACION-------------------
git init
git add .
git commit -m "Primer commit"
gh auth login
gh repo create Transcribe_Service_Open --public --source=. --remote=origin
git push -u origin master
---------------------SUBIR-------------------
git status
git add . o' git add nombre_del_archivo
git commit -m "Descripción de los cambios"
git push o' git push origin nombre_de_la_rama




