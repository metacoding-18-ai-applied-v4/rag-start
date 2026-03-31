"""ex07 구조화된 로깅 및 Langfuse 모니터링."""

import json
import logging
import os
import time
from datetime import datetime, timezone


# --- JSON 구조화 로그 포맷터 ---
class JsonFormatter(logging.Formatter):
    """로그 레코드를 JSON 형식으로 직렬화하는 포맷터."""

    def __init__(self, fmt_keys=None):
        """JsonFormatter를 초기화합니다."""
        super().__init__()
        self.fmt_keys = fmt_keys or []

    def format(self, record):
        """LogRecord를 JSON 문자열로 변환합니다."""
        # TODO: timestamp, level, logger, message를 포함한 딕셔너리를 구성한다
        # TODO: fmt_keys에 해당하는 추가 필드를 포함한다
        # TODO: exc_info가 있으면 exception 필드를 추가한다
        # TODO: json.dumps()로 직렬화하여 반환한다
        pass


def setup_logging(level="INFO", use_json=True, log_file=None):
    """애플리케이션 로깅 시스템을 설정합니다."""
    # TODO: 문자열 레벨을 숫자로 변환한다 (유효하지 않으면 ValueError)
    # TODO: 루트 로거 레벨을 설정하고 기존 핸들러를 제거한다
    # TODO: use_json이 True이면 JsonFormatter, 아니면 일반 Formatter를 사용한다
    # TODO: 콘솔 핸들러를 추가한다
    # TODO: log_file이 지정되면 파일 핸들러도 추가한다
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
        # TODO: COST_PER_1K_TOKENS에서 모델별 비용 테이블을 가져온다
        # TODO: input/output 토큰 기반으로 비용(USD)을 계산한다
        # TODO: timestamp, model, operation, 토큰 수, 비용, latency를 레코드로 저장한다
        # TODO: 누적 토큰 수를 업데이트한다
        pass

    def summary(self):
        """누적 토큰 사용량 요약을 반환합니다."""
        # TODO: total_calls, total_input/output_tokens, total_cost_usd, avg_latency_ms를 딕셔너리로 반환한다
        pass

    def recent(self, n=5):
        """최근 n개의 호출 기록을 반환합니다."""
        # TODO: _records에서 마지막 n개를 반환한다
        pass


# --- Langfuse 래퍼 ---
class LangfuseMonitor:
    """Langfuse LLM 모니터링 도구 연동 래퍼."""

    def __init__(self):
        """LangfuseMonitor를 초기화합니다."""
        self._logger = logging.getLogger(__name__)
        self.enabled = False
        self._client = None
        self._init_langfuse()

    def _init_langfuse(self):
        """Langfuse 클라이언트를 초기화합니다."""
        # TODO: 환경변수에서 LANGFUSE_PUBLIC_KEY와 LANGFUSE_SECRET_KEY를 읽는다
        # TODO: 키가 없으면 안내 메시지 로깅 후 리턴한다
        # TODO: Langfuse 클라이언트를 생성하고 enabled를 True로 설정한다
        # TODO: langfuse 패키지 미설치 시 ImportError를 처리한다
        pass

    def trace(self, name, input_data, output_data, metadata=None):
        """LLM 호출 추적 기록을 Langfuse에 전송합니다."""
        # TODO: enabled가 False이면 리턴한다
        # TODO: _client.trace()로 name, input, output, metadata를 전송한다
        # TODO: 실패 시 경고 로그를 남긴다
        pass

    def flush(self):
        """대기 중인 Langfuse 이벤트를 즉시 전송합니다."""
        # TODO: enabled가 False이면 리턴한다
        # TODO: _client.flush()를 호출한다
        pass


# --- 싱글톤 인스턴스 ---
token_tracker = TokenTracker()
langfuse_monitor = LangfuseMonitor()
