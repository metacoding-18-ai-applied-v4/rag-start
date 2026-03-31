"""step3 — 평가 실행 로직.

벡터DB를 구축하고, 테스트 질문으로 검색을 수행한 뒤, 평가 지표를 계산한다.
"""

import json
import os
from pathlib import Path

import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv

from .metrics import (
    calculate_mrr,
    calculate_precision_at_k,
    calculate_recall_at_k,
    estimate_hallucination_rate,
)

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
CHROMA_DIR = DATA_DIR / "chroma_db"
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")


# ---------------------------------------------------------------------------
# 벡터DB 구축
# ---------------------------------------------------------------------------

def build_vectordb(collection_name: str = "eval_documents") -> chromadb.Collection:
    """data/docs 폴더의 문서를 파싱하여 ChromaDB 컬렉션에 저장한다."""
    # TODO: ChromaDB PersistentClient 생성 (CHROMA_DIR 경로)
    # TODO: 기존 컬렉션 삭제 후 재생성 (cosine space)
    # TODO: data/docs 폴더의 PDF를 순회하며 텍스트 추출
    # TODO: 페이지별로 id, document, metadata를 수집
    # TODO: collection.add()로 벡터DB에 저장
    # TODO: collection 반환
    pass


def _extract_pdf_text(pdf_path: Path) -> list[str]:
    """PDF에서 페이지별 텍스트를 추출한다."""
    # TODO: PyMuPDF로 PDF 열기
    # TODO: 각 페이지의 get_text() 결과를 리스트로 반환
    pass


# ---------------------------------------------------------------------------
# 검색 수행
# ---------------------------------------------------------------------------

def search_collection(
    collection: chromadb.Collection,
    query: str,
    k: int = 5,
) -> dict:
    """컬렉션에서 질문에 대해 상위 K개 결과를 검색한다."""
    # TODO: collection.query()로 검색 수행
    # TODO: 결과에서 id, text, source, page, distance 추출
    # TODO: {"query": ..., "retrieved": [...], "sources": [...]} 반환
    pass


# ---------------------------------------------------------------------------
# LLM 답변 생성
# ---------------------------------------------------------------------------

def generate_answer(query: str, context_docs: list[str]) -> str:
    """검색된 컨텍스트를 기반으로 LLM 답변을 생성한다."""
    # TODO: context_docs를 합쳐서 프롬프트 구성
    # TODO: Ollama API로 답변 생성
    # TODO: 실패 시 에러 메시지 문자열 반환
    pass


# ---------------------------------------------------------------------------
# 평가 실행
# ---------------------------------------------------------------------------

def load_test_questions() -> list[dict]:
    """test_questions.json을 로드한다."""
    # TODO: DATA_DIR / "test_questions.json" 경로에서 JSON 로드
    # TODO: questions 키의 리스트 반환 (파일 없으면 빈 리스트)
    pass


def run_evaluation(k: int = 3, generate_answers: bool = False) -> dict:
    """전체 평가 파이프라인을 실행한다.

    1. 벡터DB 구축
    2. 테스트 질문 로드
    3. 각 질문에 대해 검색 수행
    4. 평가 지표 계산
    """
    # TODO: 1) build_vectordb()로 벡터DB 구축
    # TODO: 2) load_test_questions()로 질문 로드 (없으면 에러 dict 반환)
    # TODO: 3) 각 질문에 대해:
    #   - search_collection으로 검색
    #   - generate_answers가 True면 generate_answer로 답변 생성
    #   - calculate_precision_at_k, calculate_recall_at_k 계산
    #   - question_results에 결과 기록
    # TODO: 4) 전체 평균 precision, recall, MRR, hallucination rate 집계
    # TODO: 5) 카테고리별 통계 집계
    # TODO: {"summary": {...}, "category_stats": {...}, "question_results": [...]} 반환
    pass
