"""ex06 — 질문 라우팅 모듈."""

import json
import os
import re

# ---------------------------------------------------------------------------
# 1. 라우팅 판단 기준 키워드 정의
# ---------------------------------------------------------------------------

# 정형 데이터(DB) 관련 키워드 — 숫자/통계/명단 조회
STRUCTURED_KEYWORDS = [
    "잔여", "잔량", "연차", "휴가", "남은", "몇 일", "며칠",
    "매출", "합계", "총액", "금액", "얼마", "실적",
    "목록", "명단", "직원", "사원", "리스트", "조회",
    "통계", "평균", "부서별", "합산", "입사일", "날짜"
]

# 비정형 데이터(문서) 관련 키워드 — 절차/정책/안내
# 주의: "알려줘", "뭐야" 같은 범용 요청 접미사는 제외한다.
#       이런 표현은 모든 질문에 붙을 수 있어 판별력이 없다.
UNSTRUCTURED_KEYWORDS = [
    "절차", "방법", "어떻게", "규정", "정책", "기준",
    "온보딩", "입사 안내", "가이드", "매뉴얼",
    "복지", "혜택", "보안", "출장", "비용",
    "설명해", "무엇인가", "어떤가",
]

# DB 스키마 컬럼/테이블명 — Step 2 매칭 대상
SCHEMA_TERMS = {
    # leave_balance 테이블
    "remaining_days": "structured",
    "used_days": "structured",
    "total_days": "structured",
    # sales 테이블
    "amount": "structured",
    "total_amount": "structured",
    "revenue": "structured",
    # employees 테이블
    "emp_no": "structured",
    "department": "structured",
    "hire_date": "structured",
}


class QueryRouter:
    """질문 유형 분류기."""

    def __init__(self, llm=None):
        """라우터를 초기화한다."""
        self._llm = llm

    # ------------------------------------------------------------------
    # 2. 공개 인터페이스
    # ------------------------------------------------------------------

    def classify_query(self, query):
        """질문을 분석하여 처리 경로를 반환한다."""
        # TODO: Step 1 — 규칙 기반 키워드 매칭을 시도한다
        # TODO: Step 2 — DB 스키마 컬럼명 매칭을 시도한다
        # TODO: Step 3 — LLM 판단 (폴백)을 시도한다
        # TODO: 기본값 — 모든 단계에서 결정되지 않으면 "unstructured"를 반환한다
        pass

    # ------------------------------------------------------------------
    # 3. 내부 구현 메서드
    # ------------------------------------------------------------------

    def _step1_rule_based(self, query):
        """규칙 기반 키워드 매칭으로 경로를 결정한다."""
        # TODO: STRUCTURED_KEYWORDS와 UNSTRUCTURED_KEYWORDS 각각의 히트 수를 센다
        # TODO: 양쪽 모두 히트 시 — 한 쪽이 2배 이상 우세하면 그 쪽, 아니면 "hybrid"
        # TODO: 한 쪽만 히트 시 — 해당 경로 반환
        # TODO: 히트 없으면 None 반환
        pass

    def _step2_schema_based(self, query):
        """DB 스키마 컬럼명 매칭으로 경로를 결정한다."""
        # TODO: SCHEMA_TERMS 딕셔너리를 순회하며 query에 포함된 컬럼명을 찾는다
        # TODO: 매칭되면 해당 경로 반환, 없으면 None 반환
        pass

    def _step3_llm_based(self, query):
        """LLM에게 질문 분류를 위임한다."""
        # TODO: 프롬프트를 구성하여 LLM에게 structured/unstructured/hybrid 중 하나를 JSON으로 반환하도록 요청한다
        # TODO: 응답에서 <think> 태그를 제거하고 JSON을 파싱한다
        # TODO: 유효한 route 값이면 반환, 실패 시 None 반환
        pass
