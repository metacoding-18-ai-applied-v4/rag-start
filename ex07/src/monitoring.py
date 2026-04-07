"""ex07 구조화된 로깅 및 Langfuse 모니터링."""

import logging
import time
from datetime import datetime, timezone

from ._monitoring_utils import (
    format_json_record,
    calculate_cost,
    token_summary,
    token_recent,
    init_langfuse,
    langfuse_trace,
    langfuse_flush,
)


# --- JSON 구조화 로그 포맷터 ---
class JsonFormatter(logging.Formatter):
    """로그 레코드를 JSON 형식으로 직렬화하는 포맷터."""

    def __init__(self, fmt_keys=None):
        """JsonFormatter를 초기화합니다."""
        super().__init__()
        self.fmt_keys = fmt_keys or []

    def format(self, record):
        """LogRecord를 JSON 문자열로 변환합니다."""
        return format_json_record(record, self.fmt_keys)


def setup_logging(level="INFO", use_json=True, log_file=None):
    """애플리케이션 로깅 시스템을 설정합니다."""
    # TODO: 루트 로거 설정 (레벨 변환 + 핸들러 구성) → use_json이면 JsonFormatter 사용 → log_file 핸들러 추가
    pass


# --- 토큰 사용량 추적기 ---
class TokenTracker:
    """LLM API 호출별 토큰 사용량을 추적합니다."""

    # 간략한 비용 기준 (달러/1000토큰, 참고용)
    COST_PER_1K_TOKENS = {
        "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
        "gpt-4o": {"input": 0.005, "output": 0.015},
        "deepseek-r1:8b": {"input": 0.0, "output": 0.0},  # 로컬 모델: 무료
        "llama3.1:8b": {"input": 0.0, "output": 0.0},  # 로컬 모델: 무료
    }

    def __init__(self):
        """TokenTracker를 초기화합니다."""
        self._records = []
        self._total_input_tokens = 0
        self._total_output_tokens = 0
        self._logger = logging.getLogger(__name__)

    def record(self, model, input_tokens, output_tokens, operation="chat", latency_ms=0.0):
        """토큰 사용량을 기록합니다."""
        # TODO: calculate_cost()로 비용 계산 → 레코드 딕셔너리 저장 → 누적 토큰 수 업데이트
        pass

    def summary(self):
        """누적 토큰 사용량 요약을 반환합니다."""
        # TODO: token_summary(self)를 호출하여 결과를 반환한다
        pass

    def recent(self, n=5):
        """최근 n개의 호출 기록을 반환합니다."""
        return token_recent(self, n)


# --- Langfuse 래퍼 ---
class LangfuseMonitor:
    """Langfuse LLM 모니터링 도구 연동 래퍼."""

    def __init__(self):
        """LangfuseMonitor를 초기화합니다."""
        self._logger = logging.getLogger(__name__)
        self.enabled = False
        self._client = None
        init_langfuse(self)

    def trace(self, name, input_data, output_data, metadata=None):
        """LLM 호출 추적 기록을 Langfuse에 전송합니다."""
        langfuse_trace(self, name, input_data, output_data, metadata)

    def flush(self):
        """대기 중인 Langfuse 이벤트를 즉시 전송합니다."""
        langfuse_flush(self)


# --- 싱글톤 인스턴스 ---
token_tracker = TokenTracker()
langfuse_monitor = LangfuseMonitor()
