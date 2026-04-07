"""ex07 LangChain Agent 구성."""

import logging
import os
import time

from dotenv import load_dotenv

from .cache import response_cache
from .monitoring import langfuse_monitor, token_tracker
from .tools import get_leave_balance, get_sales_sum, list_employees, search_documents
from .router import QueryRouter
from .llm_factory import build_llm
from .agent_helpers import build_rag_chain, classify_route
from ._agent_utils import build_agent_executor, run_with_retry

load_dotenv()

logger = logging.getLogger(__name__)

# --- 시스템 프롬프트 ---
SYSTEM_PROMPT = """당신은 사내 AI 비서입니다.
사내 인사(HR) 시스템과 문서를 연결하여 직원들의 업무 질문에 정확하게 답변합니다.

[보유 도구]
- list_employees: 직원 목록 조회 (부서 필터 가능)
- get_leave_balance: 특정 직원의 휴가 잔여 일수 조회
- get_sales_sum: 부서별 또는 전체 매출 합계 조회
- search_documents: 사내 규정·가이드·정책 문서 검색

[도구 사용 원칙]
1. 직원 이름이나 부서가 포함된 질문 → list_employees 또는 get_leave_balance 사용
2. 매출·실적 관련 질문 → get_sales_sum 사용
3. 규정·정책·절차에 관한 질문 → search_documents 사용
4. 복합 질문(예: "홍길동의 휴가와 연차 규정") → 여러 도구를 순서대로 호출
5. 도구가 필요 없는 일상 대화 → 직접 답변

답변은 항상 한국어로 작성하고, 출처가 있을 경우 함께 표시하십시오.
"""


class ConnectHRAgent:
    """사내 AI 비서 에이전트."""

    def __init__(self):
        """ConnectHRAgent를 초기화합니다."""
        logger.info("[ConnectHRAgent] 초기화 시작...")

        # TODO: LLM·Router·도구·RAG체인·AgentExecutor를 조립한다
        #   build_llm() → QueryRouter(llm) → tools 리스트 → build_rag_chain(llm)
        #   → build_agent_executor(llm, tools, SYSTEM_PROMPT)
        pass

    def run(self, query, chat_history=None, use_cache=True):
        """사용자 질문을 처리하고 답변을 반환합니다."""
        start_time = time.time()
        logger.info("[ConnectHRAgent] 질문 수신: %s", query[:80])

        # TODO: ① 캐시 조회 → ② classify_route()로 경로 결정 ("rag" / "agent")

        # TODO: ③ 경로별 실행 — RAG이면 rag_chain.invoke(), 아니면 run_with_retry()

        # TODO: ④ 후처리 — token_tracker.record() + langfuse_monitor.trace() + response_cache.set() → 결과 반환
        pass


# --- 싱글톤 인스턴스 ---
_agent_instance = None


def get_agent():
    """ConnectHRAgent 싱글톤 인스턴스를 반환합니다."""
    global _agent_instance
    if _agent_instance is None:
        _agent_instance = ConnectHRAgent()
    return _agent_instance
