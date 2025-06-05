import logging
import re
from typing import List, Dict
import numpy as np
import faiss

logger = logging.getLogger(__name__)

EMBED_DIM = 384

# Initialize in-memory FAISS indexes
try:
    document_index = faiss.IndexFlatL2(EMBED_DIM)
    paragraph_index = faiss.IndexFlatL2(EMBED_DIM)
    sentence_index = faiss.IndexFlatL2(EMBED_DIM)
    logger.info("[PHASE 2] DB Instances initialized")
except Exception as e:
    logger.error("[PHASE 2 ERROR] Failed to init indexes: %s", e)
    document_index = paragraph_index = sentence_index = None

# Store metadata for verification/tests
_document_texts: List[str] = []
_paragraph_texts: List[str] = []
_sentence_texts: List[str] = []

def split_into_paragraphs(text: str) -> List[str]:
    paragraphs = [p.strip() for p in re.split(r"\n\n+", text.strip()) if p.strip()]
    result = []
    for para in paragraphs:
        words = para.split()
        while len(words) > 500:
            result.append(" ".join(words[:500]))
            words = words[500:]
        if words:
            result.append(" ".join(words))
    return result


def split_into_sentences(text: str) -> List[str]:
    raw_sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    result = []
    for sent in raw_sentences:
        words = sent.split()
        while len(words) > 30:
            result.append(" ".join(words[:30]))
            words = words[30:]
        if words:
            result.append(" ".join(words))
    return [s for s in result if s]


def embed_text_chunks(chunks: List[str]) -> List[np.ndarray]:
    vectors = []
    for chunk in chunks:
        # Dummy embedding: hash-based seed for determinism in tests
        seed = abs(hash(chunk)) % (2 ** 32)
        rng = np.random.default_rng(seed)
        vectors.append(rng.random(EMBED_DIM, dtype=np.float32))
    return vectors


def index_text_block(text: str) -> None:
    document_chunks = [text]
    paragraph_chunks = split_into_paragraphs(text)
    sentence_chunks = split_into_sentences(text)

    logger.info("[PHASE 2] Splitting input: %d document, %d paragraphs, %d sentences", len(document_chunks), len(paragraph_chunks), len(sentence_chunks))

    doc_vectors = embed_text_chunks(document_chunks)
    para_vectors = embed_text_chunks(paragraph_chunks)
    sent_vectors = embed_text_chunks(sentence_chunks)

    for vec, chunk in zip(doc_vectors, document_chunks):
        document_index.add(np.array([vec]))
        _document_texts.append(chunk)

    for vec, chunk in zip(para_vectors, paragraph_chunks):
        paragraph_index.add(np.array([vec]))
        _paragraph_texts.append(chunk)

    for vec, chunk in zip(sent_vectors, sentence_chunks):
        sentence_index.add(np.array([vec]))
        _sentence_texts.append(chunk)

    logger.info("[PHASE 2] Added vectors to indexes")


def get_index_counts() -> Dict[str, int]:
    return {
        "documents": document_index.ntotal if document_index else 0,
        "paragraphs": paragraph_index.ntotal if paragraph_index else 0,
        "sentences": sentence_index.ntotal if sentence_index else 0,
    }

def get_index_sample() -> Dict[str, List[str]]:
    return {
        "documents": _document_texts[:5],
        "paragraphs": _paragraph_texts[:5],
        "sentences": _sentence_texts[:5],
    }


def clear_indexes() -> None:
    global document_index, paragraph_index, sentence_index
    document_index.reset()
    paragraph_index.reset()
    sentence_index.reset()
    _document_texts.clear()
    _paragraph_texts.clear()
    _sentence_texts.clear()
