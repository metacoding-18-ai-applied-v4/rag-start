"""step1 — 문서 파싱 전략 비교 CLI.

Usage:
    python -m tuning.step1_document_parser --step 1-1          # OCR 파싱만
    python -m tuning.step1_document_parser --step 1-2          # Vision LLM 파싱만
    python -m tuning.step1_document_parser --step all          # 둘 다 + 비교
    python -m tuning.step1_document_parser --step all --pdf_path ./data/docs/test.pdf
"""

import argparse
import os
import sys
import time
from pathlib import Path

from rich.console import Console

console = Console()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"


def _find_pdf(pdf_path: str | None) -> Path | None:
    """테스트용 PDF를 찾는다."""
    # TODO: pdf_path가 지정되면 해당 경로의 PDF 반환
    # TODO: 미지정 시 data/docs 폴더에서 첫 번째 PDF 자동 탐색
    # TODO: PDF가 없으면 안내 메시지 출력 후 None 반환
    pass


def run_step_1_1(pdf_path: Path) -> dict | None:
    """Step 1-1: OCR 파싱."""
    from .display import show_parse_result
    from .parser import parse_pdf_ocr

    console.print("[bold]Step 1-1: OCR 파싱 (EasyOCR)[/bold]")
    console.print(f"  대상: {pdf_path.name}")

    # TODO: parse_pdf_ocr로 PDF 파싱 실행 (소요 시간 측정)
    # TODO: show_parse_result로 결과 출력
    # TODO: result 반환
    pass


def run_step_1_2(pdf_path: Path) -> dict | None:
    """Step 1-2: Vision LLM 파싱."""
    from .display import show_parse_result
    from .parser import parse_pdf_vllm

    console.print("[bold]Step 1-2: Vision LLM 파싱[/bold]")
    console.print(f"  대상: {pdf_path.name}")

    # TODO: parse_pdf_vllm으로 PDF 파싱 실행 (소요 시간 측정)
    # TODO: show_parse_result로 결과 출력
    # TODO: result 반환
    pass


def main() -> None:
    parser = argparse.ArgumentParser(description="Step 1: 문서 파싱 전략 비교")
    parser.add_argument(
        "--step",
        choices=["1-1", "1-2", "all"],
        default="all",
        help="실행할 스텝 (1-1: OCR, 1-2: Vision LLM, all: 비교)",
    )
    parser.add_argument("--pdf_path", type=str, default=None, help="테스트 PDF 경로")
    parser.add_argument("--dpi", type=int, default=150, help="렌더링 DPI (기본: 150)")
    parser.add_argument("--timeout", type=int, default=600, help="Vision LLM 타임아웃 (초, 기본: 600)")

    args = parser.parse_args()

    # TODO: _find_pdf로 PDF 경로 확인 (없으면 sys.exit(1))
    # TODO: --timeout을 VISION_TIMEOUT 환경변수로 전달
    # TODO: --step에 따라 run_step_1_1, run_step_1_2 실행
    # TODO: step == "all"이면 둘 다 실행 후 show_comparison으로 비교 출력
    pass



if __name__ == "__main__":
    main()
