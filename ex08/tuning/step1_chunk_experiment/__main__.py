"""step1_chunk_experiment CLI 진입점.

사용법:
    python -m tuning.step1_chunk_experiment --step 1-1
    python -m tuning.step1_chunk_experiment --step 1-3 --percentile 80
    python -m tuning.step1_chunk_experiment --step 1-5 --k 3 --threshold 0.3 --department HR
"""

from __future__ import annotations

import argparse
import sys

from .experiments import (
    run_chunk_size_experiment,
    run_overlap_experiment,
    run_retriever_experiment,
    run_short_doc_experiment,
    run_strategy_comparison,
)


STEP_CHOICES = ["1-1", "1-2", "1-3", "1-4", "1-5"]

STEP_DESCRIPTIONS = {
    "1-1": "청크 크기 실험 (300/500/1000자)",
    "1-2": "오버랩 비율 실험 (10%/20%/30%)",
    "1-3": "청킹 전략 비교 (Fixed vs Recursive vs Semantic)",
    "1-4": "짧은 문서 실험",
    "1-5": "Retriever 파라미터 튜닝 (k/threshold/metadata)",
}


def build_parser() -> argparse.ArgumentParser:
    """argparse 파서를 생성합니다."""
    # TODO: ArgumentParser를 생성하고 --step, --percentile, --k, --threshold,
    #       --department 인자를 추가하여 반환합니다.
    #       - --step: choices=STEP_CHOICES, required=True
    #       - --percentile: int, default=70
    #       - --k: int, default=5
    #       - --threshold: float, default=0.2
    #       - --department: str, default=None
    pass


def main(argv: list[str] | None = None) -> None:
    """CLI 메인 함수."""
    # TODO: build_parser()로 파서 생성 → args 파싱
    #       → args.step 값에 따라 dispatch 딕셔너리에서 적절한 실험 함수를 호출합니다.
    #       dispatch 매핑:
    #         "1-1" → run_chunk_size_experiment(percentile=args.percentile)
    #         "1-2" → run_overlap_experiment()
    #         "1-3" → run_strategy_comparison(percentile=args.percentile)
    #         "1-4" → run_short_doc_experiment(percentile=args.percentile)
    #         "1-5" → run_retriever_experiment(k, threshold, department)
    pass


if __name__ == "__main__":
    main()
