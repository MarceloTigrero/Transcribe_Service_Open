# adapters/transcriber_adapter.py
from domain.ports.transcriber_port import TranscriberPort
import whisper

class WhisperAdapter(TranscriberPort):
    def __init__(self, model='tiny'):
        self.model = whisper.load_model(model)
    
    def transcribe(self, audio_path: str, language: str) -> str:
        return self.model.transcribe(audio_path, language=language)['text']
