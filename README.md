<div align="center">

```
   ____                   _                     _____                              
  / __ \                 | |                   / ____|                            
 | |  | |_   _  __ _ _ __| |_ _   _ _ __ ___  | (___   ___ _ ____   _____ _ __   
 | |  | | | | |/ _' | '__| __| | | | '_ ' _ \  \___ \ / _ \ '__\ \ / / _ \ '__|  
 | |__| | |_| | (_| | |  | |_| |_| | | | | |   ____) |  __/ |   \ V /  __/ |     
  \___\_\\__,_|\__,_|_|   \__|\__,_|_| |_| |_ |_____/ \___|_|    \_/ \___|_|     
```                                                                                                     

[![Tests](https://github.com/andreivisan/quantum_server/actions/workflows/test.yml/badge.svg)](https://github.com/andreivisan/quantum_server/actions/workflows/test.yml)                                                                                                     

<a href="https://www.buymeacoffee.com/programminglife" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

</div>

## Project Vision & Goals

Quantum Server is the backend component that powers the Quantum CLI tool. It provides a FastAPI-based server that interfaces with Chain of Thought AI models through Ollama and LangChain. The server handles AI interactions and provides a streaming API endpoint for real-time AI responses.

## Key Features

- **Streaming AI Responses**: Real-time streaming of AI responses using Server-Sent Events (SSE)
- **Chain of Thought Processing**: Structured thinking process in AI responses
- **FastAPI Integration**: Modern, fast (high-performance) web framework for building APIs
- **Ollama Integration**: Direct integration with Ollama for local AI model execution
- **LangChain Implementation**: Leveraging LangChain for enhanced AI interactions

## Prerequisites

- [Ollama](https://ollama.ai) (The CLI tool will guide you through the installation)
- QwQ AI model ```ollama pull qwq``` or ```ollama run qwq```
- Python 3.10 or later
- Recommended hardware: 32 GB RAM, and if using MacBook Pro, M1 or above

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/quantum_server.git
cd quantum_server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn chat_with_qwq:app --reload
```

The server will start on `http://localhost:8000`

## API Endpoints

### POST /chat/stream

Streams AI responses for given input messages.

Request body:
```json
{
    "message": "your question here"
}
```

Response: Server-Sent Events stream with AI responses

## Development

To run tests:
```bash
pytest tests/ -v
```

## Contributing

Contributions are welcome! Please check the [CONTRIBUTING](CONTRIBUTING.md) file for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support the Project

If this project helps you speed up your development, you can buy me a coffee to fuel the creation of more features. Please check link above.
