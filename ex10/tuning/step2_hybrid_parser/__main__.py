"""step2 — 하이브리드 파싱 CLI.

Usage:
    python -m tuning.step2_hybrid_parser --step 2-1          # OCR→Vision 하이브리드
    python -m tuning.step2_hybrid_parser --step 2-2          # 텍스트레이어→Vision
    python -m tuning.step2_hybrid_parser --step all          # 둘 다 + 비교
    python -m tuning.step2_hybrid_parser --step all --pdf ./data/docs/test.pdf --threshold 80
"""

import argparse
import sys
import time
from pathlib import Path

import fitz  # PyMuPDF
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


def run_step_2_1(pdf_path: Path, threshold: int) -> list[dict]:
    """Step 2-1: OCR → Vision LLM 하이브리드 파싱."""
    from .display import show_page_result, show_summary
    from .hybrid_parser import process_image_hybrid

    console.print("[bold]Step 2-1: 하이브리드 파싱 (OCR → Vision)[/bold]")
    console.print(f"  대상: {pdf_path.name}  |  임계값: {threshold}자")

    # TODO: PDF를 fitz로 열어 페이지별 순회
    # TODO: 각 페이지에 process_image_hybrid 적용 (threshold 전달)
    # TODO: show_page_result로 페이지별 결과 출력
    # TODO: 총 소요 시간 출력 + show_summary로 요약 출력
    # TODO: results 리스트 반환
    pass


def run_step_2_2(pdf_path: Path) -> list[dict]:
    """Step 2-2: 텍스트 레이어 → Vision LLM 파싱."""
    from .display import show_page_result, show_summary
    from .hybrid_parser import process_image_textlayer

    console.print("[bold]Step 2-2: 텍스트 레이어 → Vision 파싱[/bold]")
    console.print(f"  대상: {pdf_path.name}")

    # TODO: PDF를 fitz로 열어 페이지별 순회
    # TODO: 각 페이지에 process_image_textlayer 적용
    # TODO: show_page_result로 페이지별 결과 출력
    # TODO: 총 소요 시간 출력 + show_summary로 요약 출력
    # TODO: results 리스트 반환
    pass


def main() -> None:
    parser = argparse.ArgumentParser(description="Step 2: 하이브리드 파싱 전략")
    parser.add_argument(
        "--step",
        choices=["2-1", "2-2", "all"],
        default="all",
        help="실행할 스텝 (2-1: OCR→Vision, 2-2: TextLayer→Vision, all: 둘 다)",
    )
    parser.add_argument("--pdf", type=str, default=None, help="테스트 PDF 경로")
    parser.add_argument("--threshold", type=int, default=50, help="OCR 텍스트 임계값 (기본: 50)")

    args = parser.parse_args()

    # TODO: _find_pdf로 PDF 경로 확인 (없으면 sys.exit(1))
    # TODO: --step에 따라 run_step_2_1, run_step_2_2 실행
    pass



if __name__ == "__main__":
    main()
