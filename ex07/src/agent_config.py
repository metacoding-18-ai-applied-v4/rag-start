"""ex07 LangChain Agent 구성."""

import logging
import os
import time

from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from .cache import response_cache
from .monitoring import langfuse_monitor, token_tracker
from .tools import get_leave_balance, get_sales_sum, list_employees, search_documents
from .router import QueryRouter
from .llm_factory import build_llm
from .agent_helpers import build_rag_chain, classify_route

load_dotenv()

logger = logging.getLogger(__name__)

# --- 설정 상수 ---
AGENT_MAX_ITERATIONS = 10   # Agent 최대 반복 횟수
AGENT_TIMEOUT_SECONDS = 60  # Agent 실행 최대 대기 시간 (초)
RETRY_MAX_ATTEMPTS = 3      # 최대 재시도 횟수
RETRY_DELAY_SECONDS = 2.0   # 재시도 간격 (초)

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

        self.llm = build_llm()
        self._router = QueryRouter(llm=self.llm)
        self.tools = [list_employees, get_leave_balance, get_sales_sum, search_documents]
        self.rag_chain = build_rag_chain(self.llm)

        self.agent_executor = self._build_agent_executor()

        logger.info(
            "[ConnectHRAgent] 초기화 완료 (도구 수: %d, RAG 체인: %s)",
            len(self.tools),
            "활성" if self.rag_chain else "비활성",
        )

    def _build_agent_executor(self):
        """AgentExecutor를 구성합니다."""
        try:
            # TODO: 프롬프트 템플릿을 정의한다 (system + chat_history + input + agent_scratchpad)
            # TODO: Tool Calling Agent를 생성한다
            # TODO: AgentExecutor를 래핑한다 (운영 설정: max_iterations, timeout, 중간 단계 반환 포함)
            pass
        except Exception as exc:
            logger.error("[ConnectHRAgent] AgentExecutor 구성 실패: %s", exc)
            return None

    def _run_with_retry(self, query, chat_history=None):
        """재시도 로직이 포함된 Agent 실행 메서드."""
        # TODO: RETRY_MAX_ATTEMPTS만큼 반복하며 agent_executor.invoke()를 시도한다
        # TODO: 성공하면 결과를 반환한다
        # TODO: 실패하면 RETRY_DELAY_SECONDS만큼 대기 후 재시도한다
        # TODO: 모든 재시도 실패 시 에러 메시지 딕셔너리를 반환한다
        pass

    def run(self, query, chat_history=None, use_cache=True):
        """사용자 질문을 처리하고 답변을 반환합니다."""
        start_time = time.time()

        logger.info("[ConnectHRAgent] 질문 수신: %s", query[:80])

        # TODO: ① 캐시 조회 — use_cache가 True이면 response_cache.get()으로 캐시된 응답을 확인한다

        # TODO: ② Router로 경로 결정 — classify_route()로 "rag" 또는 "agent" 경로를 결정한다

        # TODO: ③ 경로별 실행
        #   - "rag" 경로이고 rag_chain이 있으면 → rag_chain.invoke()로 문서 검색 응답 생성
        #   - RAG 실패 시 → _run_with_retry()로 Agent 폴백
        #   - 그 외 → _run_with_retry()로 Agent 실행

        # TODO: ④ 토큰 사용량 기록 — token_tracker.record()로 모델, 토큰 수, 지연시간 기록

        # TODO: ⑤ Langfuse 추적 전송 — langfuse_monitor.trace()로 입출력 및 메타데이터 전송

        # TODO: ⑥ 캐시 저장 — use_cache가 True이면 response_cache.set()으로 응답 캐시

        # TODO: 처리 완료 로그 출력 후 result를 반환한다
        pass


# --- 싱글톤 인스턴스 ---
_agent_instance = None


def get_agent():
    """ConnectHRAgent 싱글톤 인스턴스를 반환합니다."""
    global _agent_instance
    if _agent_instance is None:
        _agent_instance = ConnectHRAgent()
    return _agent_instance
