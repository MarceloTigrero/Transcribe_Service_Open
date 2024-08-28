# domain/transcription_service.py
class TranscriptionService:
    def __init__(self, transcriber, storage):
        self.transcriber = transcriber
        self.storage = storage
    
    def transcribe_and_store(self, audio_path: str, language: str, output_path: str):
        transcription = self.transcriber.transcribe(audio_path, language)
        self.storage.save(transcription, output_path)
