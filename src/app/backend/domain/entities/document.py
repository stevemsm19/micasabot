from typing import Dict, Any, Optional

class Document:
    def __init__(self, page_content: str, metadata: Dict[str, Any]):
        self.page_content = page_content
        self.metadata = metadata

class DocumentChunk:
    def __init__(self, content: str, metadata: Dict[str, Any], score: Optional[float] = None):
        self.content = content
        self.metadata = metadata
        self.score = score