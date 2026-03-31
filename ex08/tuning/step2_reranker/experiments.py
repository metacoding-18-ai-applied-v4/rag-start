"""리랭킹 실험 유틸리티 및 실행기."""

from __future__ import annotations

import copy
import time

from .data import SAMPLE_DOCUMENTS
from .display import console, print_comparison_tables
from .reranker import create_reranker


# ── 실험 유틸리티 ────────────────────────────────────────────────
def simulate_initial_retrieval(
    query: str, documents: list[dict], top_k: int = 10
) -> list[dict]:
    """초기 벡터 검색 결과를 시뮬레이션합니다."""
    # TODO: documents를 deepcopy한 뒤, 쿼리 단어와 문서 단어의 교집합에 따라
    #       bonus = 0.05 * 교집합 크기를 기존 score에 더합니다 (최대 1.0).
    #       score 내림차순 정렬 후 상위 top_k개를 반환합니다.
    pass


def compare_before_after_reranking(
    query: str, initial_results: list[dict], reranked_results: list[dict]
) -> dict:
    """리랭킹 전후 순위를 비교합니다."""
    # TODO: {"query": query, "before": [...], "after": [...]} 형태의 딕셔너리를 생성합니다.
    #       before: 각 문서의 {rank, id, score, content_preview(40자+...)}
    #       after: 각 문서의 {rank, id, score(cross_encoder_score), content_preview}
    pass


def calculate_rank_change(before: list[dict], after: list[dict]) -> list[dict]:
    """리랭킹 전후 순위 변화를 계산합니다."""
    # TODO: before와 after의 id별 rank를 비교하여 순위 변화(before_rank - after_rank)를 계산합니다.
    #       반환 형식: [{"문서 ID", "리랭킹 전 순위", "리랭킹 후 순위", "순위 변화"}, ...]
    pass


# ── 메인 실험 ────────────────────────────────────────────────────
def run_reranker_experiment(max_queries: int | None = None) -> None:
    """리랭커 실험 전체를 실행합니다.

    Args:
        max_queries: 실행할 최대 쿼리 수 (None이면 전체).
    """
    # TODO: create_reranker()로 리랭커를 생성합니다.
    #       test_queries = ["연차 신청 절차는 어떻게 됩니까", "재택근무 신청 조건", "출장비 정산 기한"]
    #       각 쿼리에 대해:
    #         1) simulate_initial_retrieval()로 초기 검색 (top_k=10)
    #         2) reranker.rerank()로 리랭킹 (top_k=5), 시간 측정
    #         3) compare_before_after_reranking()으로 전후 비교
    #         4) print_comparison_tables()로 출력
    #       마지막에 리랭킹 효과 요약 메시지를 출력합니다.
    pass
