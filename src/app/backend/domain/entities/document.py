class Document:
    def __init__(self, page_content, metadata):
        self.page_content = page_content
        self.metadata = metadata

class DocumentChunk:
    def __init__(self, content, metadata):
        self.content = content
        self.metadata = metadata