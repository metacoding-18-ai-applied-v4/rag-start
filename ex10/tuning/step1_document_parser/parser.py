"""step1 — OCR 파싱과 Vision LLM 파싱 구현."""

import io
from pathlib import Path

import fitz  # PyMuPDF
import numpy as np
from PIL import Image

from ._parser_utils import call_vision_llm


# ---------------------------------------------------------------------------
# OCR 파싱
# ---------------------------------------------------------------------------

def parse_pdf_ocr(pdf_path: str | Path, dpi: int = 150) -> dict:
    """EasyOCR 기반 PDF 파싱. 페이지별 이미지를 OCR로 텍스트 추출한다."""
    import easyocr

    # TODO: EasyOCR Reader 생성 (한국어+영어, GPU 비활성)
    # TODO: PDF를 페이지별로 순회하며:
    #   1) 페이지를 이미지로 렌더링 (get_pixmap)
    #   2) PIL Image → numpy array 변환
    #   3) reader.readtext로 OCR 수행
    #   4) 결과 텍스트를 리스트에 수집
    # TODO: {"text": 전체 텍스트} 반환
    pass


# ---------------------------------------------------------------------------
# Vision LLM 파싱
# ---------------------------------------------------------------------------

def parse_pdf_vllm(pdf_path: str | Path, dpi: int = 150) -> dict:
    """Vision LLM 기반 PDF 파싱. 페이지 이미지를 LLM에게 보내 텍스트를 추출한다."""
    # TODO: PDF를 페이지별로 순회하며:
    #   1) 페이지를 PNG로 렌더링/저장
    #   2) call_vision_llm으로 이미지 분석 (_parser_utils에서 import)
    #   3) 임시 이미지 파일 삭제
    #   4) 결과 텍스트를 리스트에 수집
    # TODO: {"text": 전체 텍스트} 반환
    pass
