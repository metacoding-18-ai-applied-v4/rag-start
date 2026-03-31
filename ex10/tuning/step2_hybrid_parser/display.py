"""step2 — Rich 기반 하이브리드 파싱 결과 출력."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_page_result(result: dict, page_num: int) -> None:
    """단일 페이지 하이브리드 파싱 결과를 출력한다."""
    # TODO: result에서 strategy, char_count, text 추출
    # TODO: strategy에 따라 색상 결정 (ocr=yellow, vision=green, 기타=cyan)
    # TODO: 페이지 번호, 전략, 글자 수, 200자 미리보기 출력
    pass


def show_summary(results: list[dict], pdf_name: str, strategy_name: str) -> None:
    """전체 페이지 결과를 요약 테이블로 출력한다."""
    # TODO: Rich Table 생성 (페이지/전략/글자 수/미리보기 4컬럼)
    # TODO: 각 페이지 결과를 행으로 추가 (전략별 색상)
    # TODO: 전략 분포 요약 출력 (ocr: N/total, vision: N/total)
    pass
