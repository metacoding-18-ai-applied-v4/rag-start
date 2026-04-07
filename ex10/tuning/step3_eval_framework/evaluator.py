"""step3 — 평가 실행 로직.

벡터DB를 구축하고, 테스트 질문으로 검색을 수행한 뒤, 평가 지표를 계산한다.
"""

from ._eval_utils import (
    build_vectordb,
    generate_answer,
    load_test_questions,
    search_collection,
)
from .metrics import (
    calculate_mrr,
    calculate_precision_at_k,
    calculate_recall_at_k,
    estimate_hallucination_rate,
)


def run_evaluation(k: int = 3, generate_answers: bool = False) -> dict:
    """전체 평가 파이프라인을 실행한다.

    1. 벡터DB 구축
    2. 테스트 질문 로드
    3. 각 질문에 대해 검색 수행
    4. 평가 지표 계산

    Hints:
        - build_vectordb() → ChromaDB 컬렉션
        - load_test_questions() → [{"query": ..., "relevant_sources": [...], ...}, ...]
        - search_collection(collection, query, k) → {"sources": [...], "retrieved": [...]}
        - generate_answer(query, context_docs) → str  (generate_answers=True일 때만)
        - calculate_precision_at_k(retrieved_sources, relevant, k) → float
        - calculate_recall_at_k(retrieved_sources, relevant, k) → float
        - calculate_mrr(all_retrieved_sources, all_relevant_sources) → float
        - estimate_hallucination_rate(all_answers, all_contexts) → float
    """
    # TODO: 1) build_vectordb()로 벡터DB 구축
    # TODO: 2) load_test_questions()로 질문 로드 (없으면 {"error": "..."} 반환)
    # TODO: 3) 각 질문에 대해:
    #   - search_collection으로 검색
    #   - generate_answers가 True면 generate_answer로 답변 생성
    #     (False면 q.get("expected_answer", "") 사용)
    #   - calculate_precision_at_k, calculate_recall_at_k 계산
    #   - question_results에 결과 기록
    # TODO: 4) 전체 평균 precision, recall, MRR, hallucination rate 집계
    # TODO: 5) 카테고리별 통계 집계
    # TODO: {"summary": {...}, "category_stats": {...}, "question_results": [...]} 반환
    pass
