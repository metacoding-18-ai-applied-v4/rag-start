"""step3 — Rich 기반 평가 결과 출력."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_summary(eval_result: dict) -> None:
    """전체 평가 요약을 출력한다."""
    # TODO: eval_result["summary"]에서 지표 추출
    # TODO: Rich Table 생성 (지표/값 2컬럼)
    # TODO: 질문 수, K 값, 문서 수, Precision@K, Recall@K, MRR, Hallucination Rate 행 추가
    pass


def show_category_stats(eval_result: dict) -> None:
    """카테고리별 평가 결과를 출력한다."""
    # TODO: eval_result["category_stats"]에서 카테고리별 통계 추출
    # TODO: Rich Table 생성 (카테고리/질문 수/Avg Precision/Avg Recall 4컬럼)
    # TODO: 카테고리 정렬 후 행 추가
    pass


def show_question_details(eval_result: dict, limit: int = 10) -> None:
    """개별 질문 평가 결과를 출력한다."""
    # TODO: eval_result["question_results"]에서 질문별 결과 추출
    # TODO: Rich Table 생성 (ID/카테고리/질문/P@K/R@K/검색소스 6컬럼)
    # TODO: limit 개수만큼 행 추가
    pass


def show_comparison(results: list[dict]) -> None:
    """K 값에 따른 비교 결과를 출력한다."""
    # TODO: Rich Table 생성 (K/Precision@K/Recall@K/MRR/Hallucination 5컬럼)
    # TODO: 각 K 값별 결과를 행으로 추가
    pass
