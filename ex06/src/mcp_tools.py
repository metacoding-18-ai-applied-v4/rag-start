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
    # TODO: emp_no가 "E"로 시작하는 사번이면 emp_no로 조회, 아니면 이름으로 LIKE 조회한다
    # TODO: DB 결과가 있으면 첫 번째 행을 반환한다
    # TODO: 결과가 없으면 에러 딕셔너리를 반환한다
    pass


@tool
def sales_sum(dept: str = "", start_date: str = "", end_date: str = "") -> dict:
    """부서별 또는 전체 매출 합계를 조회한다."""
    # TODO: 파라미터 기본값 처리 (start_date 기본 "2024-11-01", end_date 기본 "2024-12-31")
    # TODO: dept가 있으면 부서 필터를 SQL에 추가한다
    # TODO: DB 조회 후 결과가 있으면 grand_total, record_count, top5 등으로 가공하여 반환한다
    # TODO: 결과가 없으면 에러 딕셔너리를 반환한다
    pass


@tool
def list_employees(dept: str = "", name: str = "") -> dict:
    """직원의 기초 정보(부서, 직급, 입사일 등) 범용 목록을 조회한다.
    특정 직원의 입사일이나 기본 정보가 궁금할 때에는 name(이름)에 직원이름을 넣어 검색한다."""
    # TODO: dept, name 조건이 있으면 WHERE절에 LIKE 조건을 추가한다
    # TODO: DB 조회 후 결과가 있으면 employees 리스트와 count를 반환한다
    # TODO: 결과가 없으면 에러 딕셔너리를 반환한다
    pass


@tool
def search_documents(query: str, k: int = 3) -> dict:
    """사내 문서에서 관련 내용을 벡터 검색한다."""
    # TODO: get_vectorstore()로 컬렉션을 가져온다
    # TODO: collection.query()로 벡터 검색을 수행한다
    # TODO: 결과를 content, source, score 형태로 가공하여 반환한다
    # TODO: 실패 시 빈 결과를 반환한다
    pass


# ---------------------------------------------------------------------------
# 도구 목록 (에이전트에 전달)
# ---------------------------------------------------------------------------

ALL_TOOLS = [leave_balance, sales_sum, list_employees, search_documents]
