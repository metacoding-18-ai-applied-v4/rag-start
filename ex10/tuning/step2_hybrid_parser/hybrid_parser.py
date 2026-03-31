"""step2 — 하이브리드 파싱 전략 구현.

OCR 텍스트 길이가 임계값 미만이면 Vision LLM으로 전환한다.
텍스트 레이어 우선 전략도 제공한다.
"""

import base64
import io
import os
from pathlib import Path

import fitz  # PyMuPDF
import httpx
import numpy as np
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

MIN_TEXT_LENGTH = int(os.getenv("MIN_TEXT_LENGTH", "50"))
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
VISION_MODEL = os.getenv("VISION_MODEL", "qwen2.5vl:7b")
VISION_PROVIDER = os.getenv("VISION_PROVIDER", "ollama")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_VISION_MODEL = os.getenv("OPENAI_VISION_MODEL", "gpt-4o-mini")
VISION_TIMEOUT = int(os.getenv("VISION_TIMEOUT", "600"))


# ---------------------------------------------------------------------------
# 하이브리드 전략 1: OCR → Vision LLM fallback
# ---------------------------------------------------------------------------

def process_image_hybrid(
    page: fitz.Page,
    dpi: int = 150,
    threshold: int | None = None,
    vision_model: str | None = None,
) -> dict:
    """OCR 텍스트가 임계값 이상이면 OCR 결과를, 아니면 Vision LLM으로 전환한다."""
    # TODO: threshold 기본값 설정 (MIN_TEXT_LENGTH)
    # TODO: _ocr_page로 OCR 수행
    # TODO: OCR 텍스트 길이가 threshold 이상이면 OCR 결과 반환
    #   {"strategy": "ocr", "text": ..., "char_count": ...}
    # TODO: 미만이면 _vision_page로 Vision LLM 전환
    #   {"strategy": "vision", "text": ..., "char_count": ...}
    pass


# ---------------------------------------------------------------------------
# 하이브리드 전략 2: 텍스트 레이어 → Vision LLM fallback
# ---------------------------------------------------------------------------

def process_image_textlayer(
    page: fitz.Page,
    dpi: int = 150,
    vision_model: str | None = None,
) -> dict:
    """PDF 텍스트 레이어가 있으면 사용, 없으면 Vision LLM으로 전환한다."""
    # TODO: page.get_text()로 텍스트 레이어 추출
    # TODO: 텍스트가 있으면 text_layer 전략으로 반환
    #   {"strategy": "text_layer", "text": ..., "char_count": ...}
    # TODO: 없으면 _vision_page로 Vision LLM 전환
    #   {"strategy": "vision", "text": ..., "char_count": ...}
    pass


# ---------------------------------------------------------------------------
# 내부 헬퍼
# ---------------------------------------------------------------------------

def _ocr_page(page: fitz.Page, dpi: int = 150) -> str:
    """페이지를 이미지로 렌더링한 뒤 EasyOCR로 텍스트를 추출한다."""
    import easyocr

    # TODO: EasyOCR Reader 생성 (한국어+영어, GPU 비활성)
    # TODO: 페이지를 pixmap으로 렌더링 → PIL Image → numpy array
    # TODO: reader.readtext로 OCR 수행 후 텍스트 결합 반환
    pass


def _vision_page(
    page: fitz.Page,
    dpi: int = 150,
    model: str | None = None,
) -> str:
    """페이지를 이미지로 렌더링한 뒤 Vision LLM에 전달한다."""
    # TODO: 페이지를 pixmap으로 렌더링 → PNG bytes → base64 인코딩
    # TODO: VISION_PROVIDER에 따라 Ollama 또는 OpenAI 호출
    pass


def _call_ollama_vision(img_b64: str, model: str | None = None) -> str:
    """Ollama Vision API를 호출한다."""
    # TODO: OLLAMA_BASE_URL/api/generate 엔드포인트에 POST
    # TODO: model, prompt(문서 분석 지시), images 전달
    # TODO: 응답에서 response 텍스트 추출
    # TODO: 실패 시 에러 메시지 문자열 반환
    pass


def _call_openai_vision(img_b64: str) -> str:
    """OpenAI Vision API를 fallback으로 호출한다."""
    # TODO: OpenAI Chat Completions API에 POST
    # TODO: text + image_url(base64) 멀티모달 메시지 전달
    # TODO: 응답에서 content 텍스트 추출
    # TODO: 실패 시 에러 메시지 문자열 반환
    pass
