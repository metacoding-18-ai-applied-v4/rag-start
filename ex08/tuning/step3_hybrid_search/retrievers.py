"""BM25Retriever / VectorRetriever / EnsembleRetriever 클래스."""

from __future__ import annotations

import sys

from .data import EMBEDDING_MODEL
from .display import console


# ── BM25Retriever ────────────────────────────────────────────────
class BM25Retriever:
    """BM25 키워드 기반 검색기."""

    def __init__(self, documents: list[str], metadatas: list[dict] | None = None):
        self.documents = documents
        self.metadatas = metadatas or [{} for _ in documents]
        self.bm25 = self._build_index(documents)

    def _build_index(self, documents: list[str]):
        """BM25 인덱스를 빌드합니다."""
        # TODO: rank_bm25.BM25Okapi를 import합니다.
        #       각 문서를 소문자 변환 + split()으로 토큰화하여 BM25Okapi 인덱스를 생성합니다.
        #       ImportError 시 에러 메시지 출력 후 sys.exit(1)
        pass

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        """BM25 로 문서를 검색합니다."""
        # TODO: 쿼리를 토큰화하여 self.bm25.get_scores()로 점수를 계산합니다.
        #       점수 내림차순으로 상위 top_k개를 선택합니다.
        #       반환 형식: [{"content", "score", "metadata", "retriever_type": "bm25"}, ...]
        pass


# ── VectorRetriever ──────────────────────────────────────────────
class VectorRetriever:
    """벡터 기반 시맨틱 검색기."""

    def __init__(
        self,
        documents: list[str],
        metadatas: list[dict] | None = None,
        model_name: str = EMBEDDING_MODEL,
    ):
        self.documents = documents
        self.metadatas = metadatas or [{} for _ in documents]
        self.model = self._load_model(model_name)
        self.embeddings = self._embed_documents(documents)

    def _load_model(self, model_name: str):
        """임베딩 모델을 로드합니다."""
        # TODO: sentence_transformers.SentenceTransformer를 import하여 모델을 로드합니다.
        #       ImportError 시 에러 메시지 출력 후 sys.exit(1)
        pass

    def _embed_documents(self, documents: list[str]):
        """문서 임베딩을 사전 계산합니다."""
        # TODO: self.model.encode(documents, convert_to_numpy=True)로 임베딩을 생성합니다.
        pass

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        """코사인 유사도 기반 검색을 수행합니다."""
        # TODO: 쿼리를 임베딩하고 self.embeddings와의 코사인 유사도를 계산합니다.
        #       상위 top_k개를 선택합니다.
        #       반환 형식: [{"content", "score", "metadata", "retriever_type": "vector"}, ...]
        pass


# ── EnsembleRetriever ────────────────────────────────────────────
class EnsembleRetriever:
    """BM25 + Vector 검색 결합 앙상블 검색기."""

    def __init__(
        self,
        bm25_retriever: BM25Retriever,
        vector_retriever: VectorRetriever,
        alpha: float = 0.5,
    ):
        """alpha: Vector 가중치 (0.0 = BM25만, 1.0 = Vector만)."""
        self.bm25_retriever = bm25_retriever
        self.vector_retriever = vector_retriever
        self.alpha = alpha

    @staticmethod
    def _normalize_scores(results: list[dict]) -> list[dict]:
        """검색 점수를 0~1 범위로 정규화합니다."""
        # TODO: results가 비어있으면 그대로 반환합니다.
        #       min/max 점수를 구해 (score - min) / (max - min)으로 정규화합니다.
        #       score_range가 0이면 모든 normalized_score를 1.0으로 설정합니다.
        pass

    def search(self, query: str, top_k: int = 5, fetch_k: int = 10) -> list[dict]:
        """하이브리드 검색을 수행합니다."""
        # TODO: BM25와 Vector 각각 fetch_k개씩 검색 후 정규화합니다.
        #       문서 content를 키로 하여 bm25_score와 vector_score를 합칩니다.
        #       hybrid_score = alpha * vector_score + (1 - alpha) * bm25_score
        #       hybrid_score 내림차순 정렬 후 상위 top_k개를 반환합니다.
        pass
