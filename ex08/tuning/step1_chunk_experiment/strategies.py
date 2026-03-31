"""청킹 전략 — Fixed-size / Recursive Character / Semantic."""

from rich.console import Console

console = Console()


def fixed_size_chunking(text: str, chunk_size: int = 500, overlap: int = 100) -> list[str]:
    """고정 크기 청킹을 수행합니다.

    Args:
        text: 분할할 원본 텍스트.
        chunk_size: 청크 하나의 최대 글자 수.
        overlap: 인접 청크 간 겹치는 글자 수.

    Returns:
        분할된 청크 리스트.
    """
    # TODO: start=0부터 시작하여 text를 chunk_size 단위로 잘라 리스트에 추가합니다.
    #       - 각 청크는 text[start:end]이며, 공백만 있는 청크는 건너뜁니다.
    #       - 다음 시작 위치는 end - overlap 입니다.
    #       - 텍스트 끝에 도달하면 루프를 종료합니다.
    pass


def recursive_character_chunking(
    text: str, chunk_size: int = 500, overlap: int = 100
) -> list[str]:
    """재귀적 문자 분할 청킹을 수행합니다.

    LangChain RecursiveCharacterTextSplitter 를 사용하며,
    패키지가 없으면 fixed_size_chunking 으로 폴백합니다.

    Args:
        text: 분할할 원본 텍스트.
        chunk_size: 청크 하나의 최대 글자 수.
        overlap: 인접 청크 간 겹치는 글자 수.

    Returns:
        분할된 청크 리스트.
    """
    # TODO: langchain_text_splitters.RecursiveCharacterTextSplitter를 import합니다.
    #       - separators: ["\n\n", "\n", "。", ".", " ", ""]
    #       - ImportError 시 fixed_size_chunking으로 폴백합니다.
    pass


def semantic_chunking(
    text: str,
    embedding_model: str = "jhgan/ko-sroberta-multitask",
    percentile: int = 70,
) -> list[str]:
    """의미 단위 기반 시맨틱 청킹을 수행합니다.

    LangChain SemanticChunker + HuggingFace 임베딩을 사용합니다.
    패키지가 없으면 recursive_character_chunking 으로 폴백합니다.

    Args:
        text: 분할할 원본 텍스트.
        embedding_model: HuggingFace 임베딩 모델 이름.
        percentile: 시맨틱 분할 임계값 백분위.

    Returns:
        분할된 청크 리스트.
    """
    # TODO: HuggingFaceEmbeddings + SemanticChunker를 사용하여 시맨틱 청킹합니다.
    #       - breakpoint_threshold_type="percentile"
    #       - breakpoint_threshold_amount=percentile
    #       - ImportError 시 recursive_character_chunking으로 폴백합니다.
    pass
