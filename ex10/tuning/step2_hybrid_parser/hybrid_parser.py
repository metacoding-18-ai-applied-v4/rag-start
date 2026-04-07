"""step2 — 하이브리드 파싱 전략 구현.

OCR 텍스트 길이가 임계값 미만이면 Vision LLM으로 전환한다.
텍스트 레이어 우선 전략도 제공한다.
"""

import os

import fitz  # PyMuPDF

from ._hybrid_utils import ocr_page, vision_page

MIN_TEXT_LENGTH = int(os.getenv("MIN_TEXT_LENGTH", "50"))


# ---------------------------------------------------------------------------
# 하이브리드 전략 1: OCR → Vision LLM fallback
# ---------------------------------------------------------------------------

def process_image_hybrid(
    page: fitz.Page,
    dpi: int = 150,
    threshold: int | None = None,
    vision_model: str | None = None,
) -> dict:
    """OCR 텍스트가 임계값 이상이면 OCR 결과를, 아니면 Vision LLM으로 전환한다.

    Hints:
        - ocr_page(page, dpi) → OCR 텍스트 (str)
        - vision_page(page, dpi, model) → Vision LLM 텍스트 (str)
        - 둘 다 _hybrid_utils에서 import 됨
    """
    # TODO: threshold 기본값 설정 (MIN_TEXT_LENGTH)
    # TODO: ocr_page로 OCR 수행
    # TODO: OCR 텍스트 길이가 threshold 이상이면 OCR 결과 반환
    #   {"strategy": "ocr", "text": ..., "char_count": ...}
    # TODO: 미만이면 vision_page로 Vision LLM 전환
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
    """PDF 텍스트 레이어가 있으면 사용, 없으면 Vision LLM으로 전환한다.

    Hints:
        - page.get_text() → PDF 텍스트 레이어 추출
        - vision_page(page, dpi, model) → Vision LLM 텍스트 (str)
    """
    # TODO: page.get_text()로 텍스트 레이어 추출
    # TODO: 텍스트가 있으면 text_layer 전략으로 반환
    #   {"strategy": "text_layer", "text": ..., "char_count": ...}
    # TODO: 없으면 vision_page로 Vision LLM 전환
    #   {"strategy": "vision", "text": ..., "char_count": ...}
    pass
