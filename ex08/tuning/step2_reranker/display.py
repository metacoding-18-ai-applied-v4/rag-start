"""Rich Console / Table 출력 유틸리티."""

from rich.console import Console
from rich.table import Table

console = Console()


def print_comparison_tables(comparison: dict) -> None:
    """리랭킹 전후 비교 테이블을 출력합니다."""
    # TODO: comparison["query"]를 출력합니다.
    #       "리랭킹 전 (Vector Search 순위)" 테이블을 생성합니다.
    #         - 컬럼: 순위, 문서 ID, Vector 점수, 내용 미리보기
    #         - comparison["before"][:5]의 각 항목을 행으로 추가합니다.
    #       "리랭킹 후 (Cross-Encoder 순위)" 테이블을 생성합니다.
    #         - 컬럼: 순위, 문서 ID, CE 점수, 내용 미리보기
    #         - comparison["after"]의 각 항목을 행으로 추가합니다.
    #       두 테이블을 console.print()로 출력합니다.
    pass
