"""ex06 — MCP 도구 모듈."""

# LangChain 도구 데코레이터
from langchain_core.tools import tool

from src.db_helper import run_query, DB_ERROR_MSG, get_vectorstore, parse_and_chunk_docs


# ---------------------------------------------------------------------------
# MCP 도구 정의
# ---------------------------------------------------------------------------

@tool
def leave_balance(emp_no: str) -> dict:
    """직원의 연차 잔여 일수를 조회한다."""
    # TODO: leave_balance — 사번/이름으로 연차 조회
    pass


@tool
def sales_sum(dept: str = "", start_date: str = "", end_date: str = "") -> dict:
    """부서별 또는 전체 매출 합계를 조회한다."""
    # TODO: sales_sum — 부서별 매출 합계 조회
    pass


@tool
def list_employees(dept: str = "", name: str = "") -> dict:
    """직원의 기초 정보(부서, 직급, 입사일 등) 범용 목록을 조회한다.
    특정 직원의 입사일이나 기본 정보가 궁금할 때에는 name(이름)에 직원이름을 넣어 검색한다."""
    # TODO: list_employees — 직원 목록 조회
    pass


@tool
def search_documents(query: str, k: int = 3) -> dict:
    """사내 문서에서 관련 내용을 벡터 검색한다."""
    # TODO: search_documents — 벡터 검색으로 관련 문서 조회
    pass


# ---------------------------------------------------------------------------
# 도구 목록 (에이전트에 전달)
# ---------------------------------------------------------------------------

ALL_TOOLS = [leave_balance, sales_sum, list_employees, search_documents]
