import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from fastapi.testclient import TestClient
from main import app
from rag_indexing import (
    split_into_paragraphs,
    split_into_sentences,
    clear_indexes,
    get_index_counts,
)

client = TestClient(app)


def test_split_paragraphs_long_text():
    text = "word " * 600
    paras = split_into_paragraphs(text)
    assert all(len(p.split()) <= 500 for p in paras)
    assert sum(len(p.split()) for p in paras) == 600


def test_split_sentences_long_sentence():
    text = " ".join(["word"] * 90) + "."
    sents = split_into_sentences(text)
    assert all(len(s.split()) <= 30 for s in sents)
    assert sum(len(s.split()) for s in sents) == 90


def test_index_endpoint():
    clear_indexes()
    resp = client.post("/api/index", json={"text": "This is a test. Another one!"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"
    counts = data["counts"]
    assert counts["documents"] == 1
    assert counts["paragraphs"] >= 1
    assert counts["sentences"] == 2
