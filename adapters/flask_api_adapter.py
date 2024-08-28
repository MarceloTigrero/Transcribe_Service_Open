# adapters/flask_api_adapter.py
from flask import Flask, request, jsonify, send_file
from domain.transcription_service import TranscriptionService
import tempfile
import os
import logging

try:
    from adapters.transcriber_adapter import WhisperAdapter
    from adapters.storage_adapter import PDFStorageAdapter
except ImportError as e:
    logging.error(f"Error importing adapters: {e}")
    raise


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Dependencias
transcriber_adapter = WhisperAdapter(model='tiny')
storage_adapter = PDFStorageAdapter()
service = TranscriptionService(transcriber=transcriber_adapter, storage=storage_adapter)

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    audio_file = request.files['file']
    language = request.form.get('language')
    output_format = request.form.get('format', 'txt')

    # Crear archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".opus") as temp_audio:
        temp_audio.write(audio_file.read())
        audio_path = temp_audio.name

    try:
        # Guardar la transcripción en un archivo temporal
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{output_format}") as temp_output:
            output_file = temp_output.name
            service.transcribe_and_store(audio_path, language, output_file)
            logging.info(f"Archivo transcrito guardado en: {output_file}")
        
        # Verificar que el archivo existe antes de enviarlo
        if os.path.exists(output_file):
            return send_file(output_file, as_attachment=True)
        else:
            return jsonify({'error': 'Error al generar el archivo transcrito.'}), 500
    
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 500
    
    finally:
        # Eliminar archivos temporales
        if os.path.exists(audio_path):
            os.remove(audio_path)
        if os.path.exists(output_file):
            os.remove(output_file)
