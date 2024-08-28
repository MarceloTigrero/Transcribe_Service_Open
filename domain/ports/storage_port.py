# domain/ports/storage_port.py
from abc import ABC, abstractmethod

class StoragePort(ABC):
    @abstractmethod
    def save(self, transcription: str, output_path: str) -> None:
        pass
