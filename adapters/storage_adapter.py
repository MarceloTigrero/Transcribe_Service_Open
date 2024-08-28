# adapters/storage_adapter.py
from domain.ports.storage_port import StoragePort
from fpdf import FPDF

class PDFStorageAdapter(StoragePort):
    def save(self, transcription: str, output_path: str):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(200, 10, transcription)
        pdf.output(output_path)
