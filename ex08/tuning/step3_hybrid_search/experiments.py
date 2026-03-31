"""실험 실행기 — alpha 파라미터 실험 및 하이브리드 검색 데모."""

from __future__ import annotations

from rich.table import Table

from .data import SAMPLE_DOCUMENTS, SAMPLE_METADATAS
from .display import console, print_hybrid_demo
from .retrievers import BM25Retriever, EnsembleRetriever, VectorRetriever


# ── alpha 실험 ───────────────────────────────────────────────────
def run_alpha_experiment(
    bm25: BM25Retriever,
    vector: VectorRetriever,
    test_queries: list[str],
) -> list[dict]:
    """alpha 파라미터(0.0 ~ 1.0) 별 검색 결과를 비교합니다."""
    # TODO: alphas=[0.0, 0.3, 0.5, 0.7, 1.0]에 대해 각 alpha로 EnsembleRetriever를 생성합니다.
    #       각 쿼리에 대해 search(top_k=5)를 실행하고 평균 반환 수를 계산합니다.
    #       alpha=0.0이면 "BM25만", alpha=1.0이면 "Vector만", 그 외 "혼합"
    #       반환 형식: [{"alpha", "구성", "BM25 가중치", "Vector 가중치", "평균 반환 수", "추천"}, ...]
    pass


# ── 메인 실험 ────────────────────────────────────────────────────
def run_hybrid_search_experiment(*, max_queries: int | None = None) -> None:
    """하이브리드 검색 전체 실험을 실행합니다."""
    # TODO: BM25Retriever와 VectorRetriever를 SAMPLE_DOCUMENTS, SAMPLE_METADATAS로 초기화합니다.
    #       1. run_alpha_experiment()로 alpha 파라미터 실험 → Rich Table로 출력
    #       2. alpha=0.5 EnsembleRetriever로 데모 쿼리 "연차 신청 절차와 승인 방법" 검색
    #          → print_hybrid_demo()로 출력
    #       마지막에 하이브리드 검색 권장 설정 메시지를 출력합니다.
    pass
