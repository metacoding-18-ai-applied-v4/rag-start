"""ex07 응답 캐시 및 임베딩 캐시."""

import logging
import os
import time
from pathlib import Path

from ._cache_utils import (
    make_response_key,
    response_cache_stats,
    response_cache_clear,
    embedding_get,
    embedding_set,
    embedding_cache_stats,
)

logger = logging.getLogger(__name__)

# --- 기본 설정 상수 ---
DEFAULT_RESPONSE_TTL = 3600        # 응답 캐시 TTL (초): 1시간
DEFAULT_EMBEDDING_CACHE_DIR = "./outputs/embedding_cache"
DEFAULT_RESPONSE_CACHE_MAX_SIZE = 1000  # 최대 캐시 항목 수


class ResponseCache:
    """TTL 기반 인메모리 응답 캐시."""

    def __init__(self, ttl=DEFAULT_RESPONSE_TTL, max_size=DEFAULT_RESPONSE_CACHE_MAX_SIZE):
        """ResponseCache를 초기화합니다."""
        self.ttl = ttl
        self.max_size = max_size
        self._store = {}
        self._hits = 0
        self._misses = 0
        logger.info("[ResponseCache] 초기화 완료 (TTL: %d초, 최대 크기: %d)", ttl, max_size)

    def get(self, query, context=""):
        """캐시에서 응답을 조회합니다 (TTL 만료 체크)."""
        # TODO: make_response_key()로 키 생성 → _store 조회 → 만료 체크 → 히트/미스 카운트
        pass

    def set(self, query, value, context=""):
        """캐시에 응답을 저장합니다 (max_size 초과 시 LRU 정리)."""
        # TODO: make_response_key()로 키 생성 → 크기 초과 시 오래된 항목 제거 → (value, expires_at) 저장
        pass

    def clear(self):
        """만료된 캐시 항목을 제거합니다."""
        return response_cache_clear(self)

    def stats(self):
        """캐시 통계를 반환합니다."""
        return response_cache_stats(self)


class EmbeddingCache:
    """로컬 파일 기반 임베딩 캐시."""

    def __init__(self, cache_dir=DEFAULT_EMBEDDING_CACHE_DIR):
        """EmbeddingCache를 초기화합니다."""
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._hits = 0
        self._misses = 0
        logger.info("[EmbeddingCache] 초기화 완료 (캐시 디렉토리: %s)", self.cache_dir)

    def get_or_compute(self, text, compute_fn):
        """캐시 히트면 반환, 미스면 compute_fn으로 계산 후 저장합니다."""
        # TODO: embedding_get()으로 조회 → 히트면 반환 / 미스면 compute_fn(text) → embedding_set()
        pass

    def stats(self):
        """캐시 통계를 반환합니다."""
        return embedding_cache_stats(self)


# --- 싱글톤 인스턴스 ---
response_cache = ResponseCache(
    ttl=int(os.getenv("CACHE_TTL", str(DEFAULT_RESPONSE_TTL))),
    max_size=int(os.getenv("CACHE_MAX_SIZE", str(DEFAULT_RESPONSE_CACHE_MAX_SIZE))),
)
