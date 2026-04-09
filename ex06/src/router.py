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
        # TODO: classify_query — 3단계로 질문 분류 (키워드 → 스키마 → LLM)
        pass

    # ------------------------------------------------------------------
    # 3. 내부 구현 메서드
    # ------------------------------------------------------------------

    def _step1_rule_based(self, query):
        """규칙 기반 키워드 매칭으로 경로를 결정한다."""
        # TODO: _step1_rule_based — 키워드 매칭으로 경로 결정
        pass

    def _step2_schema_based(self, query):
        """DB 스키마 컬럼명 매칭으로 경로를 결정한다."""
        # TODO: _step2_schema_based — DB 컬럼명 매칭으로 경로 결정
        pass

    def _step3_llm_based(self, query):
        """LLM에게 질문 분류를 위임한다."""
        # TODO: _step3_llm_based — LLM에게 질문 분류 위임
        pass
