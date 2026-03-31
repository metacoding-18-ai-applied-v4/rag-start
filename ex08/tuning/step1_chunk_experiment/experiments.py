"""실험 실행기 — step 1-1 ~ 1-5.

step 1-1  청크 크기 실험 (300 / 500 / 1000자)
step 1-2  오버랩 비율 실험 (10% / 20% / 30%)
step 1-3  청킹 전략 비교 (Fixed vs Recursive vs Semantic) — 긴 문서
step 1-4  짧은 문서 실험
step 1-5  Retriever 파라미터 튜닝 (k / threshold / metadata)
"""

from __future__ import annotations

import time

from rich.console import Console

from .analysis import analyze_chunks
from .data import SAMPLE_DOCUMENT, SAMPLE_DOCUMENTS, SHORT_DOCUMENT, TEST_QUERIES
from .display import print_experiment_table
from .retriever import InMemoryRetriever, run_k_value_experiment, run_metadata_filter_experiment, run_threshold_experiment
from .strategies import fixed_size_chunking, recursive_character_chunking, semantic_chunking

console = Console()


# ── step 1-1: 청크 크기 실험 ─────────────────────────────────────
def run_chunk_size_experiment(percentile: int = 70) -> None:
    """청크 크기(300 / 500 / 1000자) 별 결과를 비교합니다."""
    # TODO: SAMPLE_DOCUMENT에 대해 chunk_sizes=[300, 500, 1000]으로 fixed_size_chunking을 실행합니다.
    #       - 각 크기별로 overlap = size // 10
    #       - 실행 시간 측정 (time.time())
    #       - analyze_chunks()로 통계 계산
    #       - results 리스트에 {전략, 청크 수, 평균 크기, 최소 크기, 최대 크기, 실행 시간} 딕셔너리 추가
    #       - print_experiment_table("청크 크기별 비교", results) 출력
    pass


# ── step 1-2: 오버랩 비율 실험 ───────────────────────────────────
def run_overlap_experiment() -> None:
    """오버랩 비율(10% / 20% / 30%) 별 결과를 비교합니다."""
    # TODO: SAMPLE_DOCUMENT에 대해 chunk_size=500, overlap_ratios=[0.1, 0.2, 0.3]으로 실험합니다.
    #       - 각 비율별로 overlap = int(chunk_size * ratio)
    #       - analyze_chunks()로 통계 계산
    #       - results에 {오버랩 비율, 오버랩 문자 수, 청크 수, 평균 크기} 추가
    #       - print_experiment_table("오버랩 비율별 비교", results) 출력
    pass


# ── step 1-3: 전략 비교 (긴 문서) ────────────────────────────────
def run_strategy_comparison(percentile: int = 70) -> None:
    """Fixed / Recursive / Semantic 전략을 긴 문서로 비교합니다."""
    # TODO: SAMPLE_DOCUMENT에 대해 3가지 청킹 전략을 순서대로 실행합니다.
    #       1) fixed_size_chunking(text, chunk_size=500, overlap=50)
    #       2) recursive_character_chunking(text, chunk_size=500, overlap=50)
    #       3) semantic_chunking(text, percentile=percentile)
    #       - 각 전략별로 실행 시간 측정 + analyze_chunks() 통계
    #       - results에 {전략, 청크 수, 평균 크기, 실행 시간, 특징} 추가
    #       - print_experiment_table("청킹 전략 비교", results) 출력
    pass


# ── step 1-4: 짧은 문서 실험 ─────────────────────────────────────
def run_short_doc_experiment(percentile: int = 70) -> None:
    """짧은 문서에 각 전략을 적용했을 때 결과를 비교합니다."""
    # TODO: SHORT_DOCUMENT에 대해 3가지 전략을 적용합니다.
    #       - 각 전략별 analyze_chunks() 통계
    #       - results에 {전략, 청크 수, 평균 크기} 추가
    #       - print_experiment_table("짧은 문서 청킹 비교", results) 출력
    #       - 관찰 메시지 출력: 짧은 문서는 청크 수 1로 수렴
    pass


# ── step 1-5: Retriever 파라미터 실험 ────────────────────────────
def run_retriever_experiment(
    k: int = 5,
    threshold: float = 0.2,
    department: str | None = None,
) -> None:
    """k값 / threshold / metadata filter 를 실험합니다."""
    # TODO: InMemoryRetriever(SAMPLE_DOCUMENTS)를 생성합니다.
    #       1. run_k_value_experiment()로 k값 실험 → 테이블 출력
    #       2. run_threshold_experiment()로 threshold 실험 → 테이블 출력
    #       3. run_metadata_filter_experiment()로 메타데이터 필터 실험 → 테이블 출력
    #       - 권장 설정 메시지 출력 (k, threshold, metadata filtering)
    pass
