"""step1 — Rich 기반 결과 출력."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_parse_result(result: dict, strategy: str, pdf_name: str) -> None:
    """파싱 결과를 Rich Panel로 출력한다."""
    # TODO: result에서 text 추출, 글자 수 계산, 300자 미리보기 생성
    # TODO: Rich Panel로 파일명/전략/글자수/미리보기 출력
    pass


def show_comparison(ocr_result: dict, vllm_result: dict, pdf_name: str) -> None:
    """OCR vs Vision LLM 비교 테이블을 출력한다."""
    # TODO: Rich Table 생성 (항목 / OCR / Vision LLM 3컬럼)
    # TODO: 글자 수, 줄 수, 표 감지(| 개수), 미리보기 행 추가
    # TODO: console.print(table)
    pass
