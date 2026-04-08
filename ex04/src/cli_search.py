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

import sys
from pathlib import Path

# store.py를 같은 src/ 디렉토리에서 임포트
sys.path.insert(0, str(Path(__file__).parent))

from _search_utils import (
    print_search_result,
    parse_arguments,
    SEPARATOR,
)
from store import search_chroma


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
    pass


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

    if args.query:
        # TODO: 단일 쿼리 모드 — run_single_query() 호출
        pass
    else:
        # TODO: 대화형 반복 검색 모드 — run_interactive_mode() 호출
        pass


if __name__ == "__main__":
    main()
