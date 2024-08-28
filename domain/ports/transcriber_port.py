# domain/ports/transcriber_port.py
from abc import ABC, abstractmethod

class TranscriberPort(ABC):
    @abstractmethod
    def transcribe(self, audio_path: str, language: str) -> str:
        pass
