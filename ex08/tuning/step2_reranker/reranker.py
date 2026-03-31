"""CrossEncoderReranker, SimpleReranker, create_reranker."""

from __future__ import annotations

import sys

from .data import CROSS_ENCODER_MODEL
from .display import console


# ── CrossEncoderReranker ─────────────────────────────────────────
class CrossEncoderReranker:
    """Cross-Encoder 기반 리랭커."""

    def __init__(self, model_name: str = CROSS_ENCODER_MODEL):
        self.model_name = model_name
        self.model = None
        self._load_model()

    def _load_model(self) -> None:
        """Cross-Encoder 모델을 로드합니다."""
        # TODO: sentence_transformers.CrossEncoder를 import하여 self.model에 할당합니다.
        #       - ImportError 시 에러 메시지 출력 후 sys.exit(1)
        #       - 기타 Exception 시 에러 메시지 출력 후 raise
        pass

    def rerank(self, query: str, documents: list[dict], top_k: int = 5) -> list[dict]:
        """검색 결과를 Cross-Encoder 로 재정렬합니다."""
        # TODO: self.model이 None이면 documents[:top_k]를 그대로 반환합니다.
        #       (query, doc["content"]) 쌍을 만들어 model.predict()로 점수를 계산합니다.
        #       각 문서에 "cross_encoder_score" 키를 추가하고, 점수 내림차순 정렬 후
        #       상위 top_k개를 반환합니다.
        pass


# ── SimpleReranker (폴백) ────────────────────────────────────────
class SimpleReranker:
    """Cross-Encoder 없이 동작하는 키워드 매칭 기반 리랭커."""

    def rerank(self, query: str, documents: list[dict], top_k: int = 5) -> list[dict]:
        """키워드 일치율로 문서를 재정렬합니다."""
        # TODO: 쿼리 단어 집합과 각 문서 단어 집합의 교집합 비율을
        #       "cross_encoder_score"로 부여합니다.
        #       점수 내림차순 정렬 후 상위 top_k개를 반환합니다.
        pass


def create_reranker(use_simple: bool = False):
    """환경에 따라 적절한 리랭커를 생성합니다."""
    # TODO: use_simple=True이면 SimpleReranker()를 반환합니다.
    #       아니면 sentence_transformers import 시도 후 CrossEncoderReranker()를 반환합니다.
    #       ImportError 시 SimpleReranker()로 폴백합니다.
    pass
