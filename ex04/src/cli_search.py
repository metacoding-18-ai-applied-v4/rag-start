"""
ChromaDB에서 쿼리를 입력받아 관련 청크를 검색하는 CLI 검증 도구.

터미널에서 직접 질문을 입력하여 ChromaDB에 저장된 문서를 검색하고
관련 텍스트 근거, 출처 파일명, 페이지 번호, 유사도 점수,
이미지 캡처본 경로를 출력합니다.

사용법:
    python src/cli_search.py
    python src/cli_search.py --query "연차 사용 규정"
    python src/cli_search.py --top-k 3

종료: 'quit' 또는 'exit' 입력
"""

import argparse
import os
import sys
from pathlib import Path

# store.py를 같은 src/ 디렉토리에서 임포트
sys.path.insert(0, str(Path(__file__).parent))

from store import (
    DEFAULT_CHROMA_DIR,
    DEFAULT_COLLECTION_NAME,
    DEFAULT_EMBEDDING_MODEL,
    search_chroma,
)


# =====================================================================
# === INPUT ===
# query: 사용자 입력 검색 쿼리 문자열
# top_k: 반환할 검색 결과 수
# chroma_dir: ChromaDB 저장 디렉토리 경로
# =====================================================================

SEPARATOR = "=" * 60


def format_distance_as_similarity(distance: float) -> float:
    """코사인 거리를 백분율 유사도로 변환합니다.

    ChromaDB cosine 공간에서 distance 범위는 0(완전 일치)~2(완전 반대)입니다.
    직관적인 유사도 표현을 위해 (1 - distance/2) * 100 으로 변환합니다.

    Args:
        distance: ChromaDB 반환 코사인 거리 (0.0 ~ 2.0)

    Returns:
        유사도 백분율 (float, 0.0 ~ 100.0)
    """
    # TODO: (1 - distance/2) * 100 공식으로 유사도 백분율 계산
    pass


def _similarity_bar(pct: float, width: int = 20) -> str:
    """유사도 백분율을 시각적 프로그레스 바로 변환합니다."""
    # TODO: pct에 비례하여 '█'과 '░'로 width 길이의 바 생성
    pass


def _clean_text(text: str, max_len: int = 200) -> str:
    """청크 텍스트를 읽기 쉽게 정리합니다.

    연속 공백과 불필요한 줄바꿈을 제거하고 최대 길이를 제한합니다.
    """
    # TODO: 연속 공백/줄바꿈 정리 → max_len 초과 시 잘라내기
    pass


def print_search_result(result: dict) -> None:
    """단일 검색 결과를 터미널에 이모지와 함께 출력합니다.

    Args:
        result: store.search_chroma() 반환 리스트의 개별 원소 딕셔너리
    """
    # TODO: result에서 rank, text, distance, metadata를 꺼내어
    #       유사도 변환 → 순위/출처/텍스트/이미지 경로를 터미널에 출력
    pass


def run_single_query(
    query: str,
    top_k: int,
    chroma_dir: str,
    collection_name: str,
    embedding_model_name: str,
) -> None:
    """단일 쿼리를 실행하고 결과를 터미널에 출력합니다.

    Args:
        query: 검색 쿼리 텍스트
        top_k: 반환할 최대 결과 수
        chroma_dir: ChromaDB 저장 디렉토리 경로
        collection_name: ChromaDB 컬렉션명
        embedding_model_name: 임베딩 모델 HuggingFace ID
    """
    # TODO: search_chroma()로 검색 실행 → 결과를 print_search_result()로 출력
    pass


def run_interactive_mode(
    top_k: int,
    chroma_dir: str,
    collection_name: str,
    embedding_model_name: str,
) -> None:
    """대화형 CLI 모드로 반복 검색을 실행합니다.

    사용자가 'quit' 또는 'exit'를 입력할 때까지
    쿼리를 반복해서 입력받아 검색 결과를 출력합니다.

    Args:
        top_k: 반환할 최대 결과 수
        chroma_dir: ChromaDB 저장 디렉토리 경로
        collection_name: ChromaDB 컬렉션명
        embedding_model_name: 임베딩 모델 HuggingFace ID
    """
    # TODO: while 루프로 input() 반복 → run_single_query() 호출
    #       'quit'/'exit'/'q' 입력 시 종료
    pass


def parse_arguments() -> argparse.Namespace:
    """CLI 인수를 파싱합니다.

    Returns:
        파싱된 인수 네임스페이스
    """
    parser = argparse.ArgumentParser(
        description="ChromaDB 벡터 검색 CLI 도구 — 사내 문서에서 관련 근거를 검색합니다.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
  python src/cli_search.py
  python src/cli_search.py --query "연차 사용 기준"
  python src/cli_search.py --query "비밀번호 정책" --top-k 3
  python src/cli_search.py --chroma-dir ./custom_db
        """,
    )

    parser.add_argument(
        "--query",
        type=str,
        default=None,
        help="검색 쿼리 (미지정 시 대화형 모드 실행)",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="반환할 최대 검색 결과 수 (기본값: 5)",
    )
    parser.add_argument(
        "--chroma-dir",
        type=str,
        default=DEFAULT_CHROMA_DIR,
        help=f"ChromaDB 저장 디렉토리 경로 (기본값: {DEFAULT_CHROMA_DIR})",
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

    return parser.parse_args()


def main() -> None:
    """CLI 검색 도구 메인 진입점.

    --query 인수가 주어지면 단일 쿼리 모드,
    그렇지 않으면 대화형 반복 검색 모드로 실행합니다.
    """
    args = parse_arguments()

    # ChromaDB 존재 여부 사전 확인
    chroma_path = Path(args.chroma_dir)
    if not chroma_path.exists():
        print(f"ChromaDB 디렉토리를 찾을 수 없습니다: {args.chroma_dir}")
        print("먼저 main.py를 실행하여 문서를 색인하십시오:")
        print("  python src/main.py")
        sys.exit(1)

    # === PROCESS ===
    if args.query:
        # TODO: 단일 쿼리 모드 — run_single_query() 호출
        pass
    else:
        # TODO: 대화형 반복 검색 모드 — run_interactive_mode() 호출
        pass


if __name__ == "__main__":
    main()
