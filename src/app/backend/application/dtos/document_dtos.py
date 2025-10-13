from dataclasses import dataclass


@dataclass
class DocumentFileDTO:
    filename: str
    content: bytes


@dataclass
class AddDocumentsResponseDTO:
    total_pages: int
    total_chunks: int
