import pytest
from fastapi.testclient import TestClient
from chat_with_qwq import app, get_chat_model, ChatRequest, stream_response
from unittest.mock import patch, MagicMock
from langchain.schema import AIMessage

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def mock_chat_model():
    mock_model = MagicMock()
    mock_model.stream.return_value = [
        AIMessage(content="THINKING:\n1. Test thought\n\nANSWER:\nTest response")
    ]
    return mock_model

def test_chat_request_model():
    request = ChatRequest(message="test message")
    assert request.message == "test message"

@patch('chat_with_qwq.get_chat_model')
def test_chat_stream_endpoint(mock_get_chat_model, client, mock_chat_model):
    # Setup mock
    mock_get_chat_model.return_value = (mock_chat_model, "test system prompt")
    
    # Test the endpoint
    response = client.post("/chat/stream", json={"message": "test message"})
    
    assert response.status_code == 200
    assert response.headers['content-type'].startswith('text/event-stream')
    
    # Check if the response contains our mock data
    content = b''.join(response.iter_bytes())
    assert b"THINKING" in content
    assert b"Test thought" in content
    assert b"ANSWER" in content
    assert b"Test response" in content

def test_get_chat_model():
    model, system_prompt = get_chat_model()
    assert model is not None
    assert isinstance(system_prompt, str)
    assert "THINKING:" in system_prompt
    assert "ANSWER:" in system_prompt

@pytest.mark.asyncio
async def test_stream_response():
    async for chunk in stream_response("test message"):
        assert isinstance(chunk, str)
        # Break after first chunk as we just want to test the generator works
        break 