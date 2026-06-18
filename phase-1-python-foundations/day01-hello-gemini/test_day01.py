"""
Unit tests for Day 1 codebase.

Architectural detail: We use unittest.mock to mock API responses so tests
can be executed locally and fast without requiring active billing, API keys, or internet requests.
"""

from unittest.mock import MagicMock, patch
from main import call_gemini, call_openai

@patch('main.gemini_model')
def test_call_gemini(mock_gemini_model):
    # Setup mock response metadata and structure matching Google SDK
    mock_resp = MagicMock()
    mock_resp.text = "Hello, this is a mock Gemini answer."
    mock_resp.usage_metadata.total_token_count = 42
    mock_gemini_model.generate_content.return_value = mock_resp

    # Execute
    res = call_gemini("Test Prompt")

    # Assert
    assert res["text"] == "Hello, this is a mock Gemini answer."
    assert res["latency_s"] >= 0.0
    assert res["tokens"] == 42
    mock_gemini_model.generate_content.assert_called_once_with("Test Prompt")

@patch('main.openai_client')
def test_call_openai(mock_openai_client):
    # Setup mock response metadata and structure matching OpenAI client
    mock_choice = MagicMock()
    mock_choice.message.content = "Hello, this is a mock OpenAI answer."
    mock_resp = MagicMock()
    mock_resp.choices = [mock_choice]
    mock_resp.usage.total_tokens = 55
    mock_openai_client.chat.completions.create.return_value = mock_resp

    # Execute
    res = call_openai("Test Prompt")

    # Assert
    assert res["text"] == "Hello, this is a mock OpenAI answer."
    assert res["latency_s"] >= 0.0
    assert res["tokens"] == 55
