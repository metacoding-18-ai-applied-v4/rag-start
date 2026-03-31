"""
ex04 VectorDB 구축 파이프라인 메인 오케스트레이터.

Step 1 (Python 파싱) → Step 2 (청킹 + 임베딩 + ChromaDB 저장) → Step 3 (CLI 검증)
세 단계를 순서대로 또는 선택적으로 실행합니다.

실행 예시:
    # 전체 파이프라인 실행
    python src/main.py

    # Step 1만 실행 (Python 파싱 테스트)
    python src/main.py --step 1

    # 문서 디렉토리 변경
    python src/main.py --docs-dir ./custom_docs
"""

import argparse
import sys
import time
from pathlib import Path

# src/ 디렉토리를 파이썬 경로에 추가 (모듈 임포트 지원)
sys.path.insert(0, str(Path(__file__).parent))

from chunker import chunk_all_documents, DEFAULT_CHUNK_SIZE, DEFAULT_OVERLAP
from extractor import extract_all_from_directory
from store import (
    DEFAULT_CHROMA_DIR,
    DEFAULT_COLLECTION_NAME,
    DEFAULT_EMBEDDING_MODEL,
    store_chunks_to_chroma,
)

# 기본 경로 설정
BASE_DIR = Path(__file__).parent.parent
DEFAULT_DOCS_DIR = str(BASE_DIR / "data" / "docs")
DEFAULT_MARKDOWN_DIR = str(BASE_DIR / "data" / "markdown")


def _rel_path(path_str: str) -> str:
    """절대 경로를 프로젝트 기준 상대 경로로 변환합니다."""
    # TODO: Path.relative_to()로 BASE_DIR 기준 상대 경로 반환, 실패 시 원본 반환
    pass


# =====================================================================
# === INPUT ===
# docs_dir: 문서 디렉토리 경로 (data/docs/)
# steps: 실행할 Step 번호 리스트 ([1], [2], [1,2])
# =====================================================================


def save_results_as_markdown(
    results: list[dict], markdown_dir: str = DEFAULT_MARKDOWN_DIR
) -> None:
    """추출 결과를 마크다운 파일로 저장합니다.

    파싱된 텍스트를 data/markdown/에 .md 파일로 저장합니다.
    임베딩 품질 향상과 사람이 파싱 결과를 확인하는 용도로 사용됩니다.

    Args:
        results: extractor.extract_all_from_directory() 반환값
        markdown_dir: 마크다운 파일 저장 디렉토리
    """
    # TODO: markdown_dir 디렉토리 생성 후, results 각 항목을 .md 파일로 저장
    # - 파일 헤더(파일명, 형식, 글자 수) + 본문 텍스트 구성
    # - 각 result의 pages에서 텍스트를 추출하여 마크다운으로 작성
    pass


def step1_python_parsing(docs_dir: str) -> list[dict]:
    """Step 1: Python 라이브러리로 문서 텍스트를 추출합니다.

    pypdf, python-docx, openpyxl을 사용하여 docs_dir 내의 모든
    PDF, DOCX, XLSX 파일에서 텍스트를 추출합니다.

    Args:
        docs_dir: 문서 파일이 저장된 디렉토리 경로

    Returns:
        문서 추출 결과 딕셔너리 리스트
    """
    # TODO: extract_all_from_directory()로 문서 추출 → 결과 출력 → 마크다운 저장
    pass


def step2_embed_and_store(
    python_results: list[dict],
    chroma_dir: str,
    collection_name: str,
    embedding_model_name: str,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    overlap: int = DEFAULT_OVERLAP,
) -> dict:
    """Step 2: 추출 결과를 청킹 후 임베딩하여 ChromaDB에 저장합니다.

    Step 1(Python 파싱) 결과를 청킹하고 ko-sroberta-multitask 임베딩
    모델로 벡터를 생성하여 ChromaDB에 영속 저장합니다.

    Args:
        python_results: Step 1 추출 결과 리스트
        chroma_dir: ChromaDB 저장 디렉토리 경로
        collection_name: ChromaDB 컬렉션명
        embedding_model_name: 임베딩 모델 HuggingFace ID
        chunk_size: 텍스트 청크 최대 문자 수
        overlap: 청크 간 오버랩 문자 수

    Returns:
        store_chunks_to_chroma() 반환값 딕셔너리
    """
    # TODO: chunk_all_documents()로 청킹 → store_chunks_to_chroma()로 ChromaDB 저장
    pass


def parse_arguments() -> argparse.Namespace:
    """CLI 인수를 파싱합니다.

    Returns:
        파싱된 인수 네임스페이스
    """
    parser = argparse.ArgumentParser(
        description="ex04 VectorDB 구축 파이프라인 — 문서를 파싱, 청킹, 임베딩하여 ChromaDB에 저장합니다.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
실행 예시:
  python src/main.py                     # 전체 파이프라인 (Step 1+2)
  python src/main.py --step 1            # Python 파싱만 테스트
  python src/main.py --step 1 2          # 전체 실행
        """,
    )

    parser.add_argument(
        "--step",
        type=int,
        nargs="+",
        choices=[1, 2],
        default=[1, 2],
        help="실행할 Step 번호 (기본값: 1 2 — 전체 실행)",
    )
    parser.add_argument(
        "--docs-dir",
        type=str,
        default=DEFAULT_DOCS_DIR,
        help="문서 디렉토리 경로 (기본값: data/docs)",
    )
    parser.add_argument(
        "--chroma-dir",
        type=str,
        default=DEFAULT_CHROMA_DIR,
        help=f"ChromaDB 저장 경로 (기본값: {DEFAULT_CHROMA_DIR})",
    )
    parser.add_argument(
        "--collection",
        type=str,
        default=DEFAULT_COLLECTION_NAME,
        help=f"ChromaDB 컬렉션명 (기본값: {DEFAULT_COLLECTION_NAME})",
    )
    parser.add_argument(
        "--embedding-model",
        type=str,
        default=DEFAULT_EMBEDDING_MODEL,
        help=f"임베딩 모델 HuggingFace ID (기본값: {DEFAULT_EMBEDDING_MODEL})",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=DEFAULT_CHUNK_SIZE,
        help=f"텍스트 청크 최대 문자 수 (기본값: {DEFAULT_CHUNK_SIZE})",
    )
    parser.add_argument(
        "--overlap",
        type=int,
        default=DEFAULT_OVERLAP,
        help=f"청크 간 오버랩 문자 수 (기본값: {DEFAULT_OVERLAP})",
    )

    return parser.parse_args()


def main() -> None:
    """ex04 VectorDB 구축 파이프라인 메인 진입점.

    1. argparse로 실행 옵션 파싱
    2. 선택된 Step 순서대로 실행
    3. 최종 결과 요약 출력
    """
    args = parse_arguments()

    steps_to_run = sorted(set(args.step))

    # === PROCESS: Step 1 — Python 파싱 ===
    # TODO: 1 in steps_to_run이면 step1_python_parsing 실행

    # === PROCESS: Step 2 — 청킹 + 임베딩 + ChromaDB 저장 ===
    # TODO: 2 in steps_to_run이면 step2_embed_and_store 실행
    #       (Step 1 결과가 없으면 Step 1을 먼저 자동 실행)

    # === OUTPUT: 파이프라인 완료 요약 ===
    # TODO: 총 소요 시간 출력 + 다음 단계(cli_search.py) 안내


if __name__ == "__main__":
    main()
