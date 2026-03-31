"""step3_hybrid_search CLI 진입점.

사용법:
    python -m tuning.step3_hybrid_search
    python -m tuning.step3_hybrid_search --max-queries 1
"""

from __future__ import annotations

import argparse

from .experiments import run_hybrid_search_experiment


def main(argv: list[str] | None = None) -> None:
    """CLI 메인 함수."""
    # TODO: ArgumentParser를 생성하고 --max-queries (int, default=None) 인자를 추가합니다.
    #       args를 파싱한 뒤 run_hybrid_search_experiment(max_queries=args.max_queries)를 호출합니다.
    pass


if __name__ == "__main__":
    main()
