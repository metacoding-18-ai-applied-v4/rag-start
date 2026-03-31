"""Rich 테이블 출력 유틸리티."""

from __future__ import annotations

from typing import TYPE_CHECKING

from rich.console import Console
from rich.table import Table

if TYPE_CHECKING:
    from .retrievers import EnsembleRetriever

console = Console()


def print_hybrid_demo(ensemble: EnsembleRetriever, query: str) -> None:
    """하이브리드 검색 데모 결과를 출력합니다."""
    # TODO: ensemble.search(query, top_k=5)로 검색합니다.
    #       Table(title=f"하이브리드 검색 결과 (alpha={ensemble.alpha})")을 생성합니다.
    #       컬럼: 순위, BM25 점수, Vector 점수, Hybrid 점수, 내용 미리보기(50자+...)
    #       결과를 행으로 추가하고 console.print(table)로 출력합니다.
    pass
