"""벡터DB 저장+검색 — ChromaDB에 청크를 넣고 검색하는 핵심 로직.

CH04 핵심: 임베딩 → upsert 저장, 쿼리 → 유사도 검색
"""

from _store_utils import (
    load_embedding_model,
    get_or_create_collection,
    embed_chunks,
    DEFAULT_CHROMA_DIR,
    DEFAULT_COLLECTION_NAME,
    DEFAULT_EMBEDDING_MODEL,
    BATCH_SIZE,
)
import sys
from pathlib import Path
import chromadb
from chromadb.config import Settings


def store_chunks_to_chroma(
    chunks: list[dict],
    chroma_dir: str = DEFAULT_CHROMA_DIR,
    collection_name: str = DEFAULT_COLLECTION_NAME,
    embedding_model_name: str = DEFAULT_EMBEDDING_MODEL,
) -> dict:
    """청크를 임베딩하여 ChromaDB에 저장합니다.

    1. 임베딩 모델 로드 (load_embedding_model)
    2. ChromaDB 클라이언트 + 컬렉션 초기화
    3. 청크 임베딩 계산 (embed_chunks)
    4. 배치 단위로 upsert

    Returns:
        {"collection_name", "chroma_dir", "total_chunks", "collection_count"}
    """
    # TODO: 위 4단계를 순서대로 구현합니다
    #       collection.upsert(ids=..., documents=..., embeddings=..., metadatas=...)
    pass


def search_chroma(
    query: str,
    chroma_dir: str = DEFAULT_CHROMA_DIR,
    collection_name: str = DEFAULT_COLLECTION_NAME,
    embedding_model_name: str = DEFAULT_EMBEDDING_MODEL,
    top_k: int = 5,
) -> list[dict]:
    """ChromaDB에서 쿼리와 유사한 청크를 검색합니다.

    Returns:
        [{"rank", "text", "distance", "metadata"}, ...]
    """
    # TODO: 쿼리 임베딩 → collection.query() → 결과 정리
    #       collection.query(query_embeddings=..., n_results=top_k)
    pass
