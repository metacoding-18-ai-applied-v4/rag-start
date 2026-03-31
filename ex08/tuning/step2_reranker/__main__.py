"""step2_reranker CLI 진입점.

사용법:
    python -m tuning.step2_reranker
    python -m tuning.step2_reranker --max-queries 1
"""

from __future__ import annotations

import argparse
import sys

from .experiments import run_reranker_experiment


def build_parser() -> argparse.ArgumentParser:
    """argparse 파서를 생성합니다."""
    # TODO: ArgumentParser를 생성하고 --max-queries (int, default=None) 인자를 추가합니다.
    pass


def main(argv: list[str] | None = None) -> None:
    """CLI 메인 함수."""
    # TODO: build_parser()로 파서 생성 → args 파싱
    #       → run_reranker_experiment(max_queries=args.max_queries) 호출
    pass


if __name__ == "__main__":
    main()
