#!/usr/bin/env python3
from langchain_ollama import ChatOllama
from langchain.schema import SystemMessage, HumanMessage

def chat_with_qwq():
    model = ChatOllama(
        model="qwq",
        temperature=0.7
    )
    
    system_prompt = """Organize your response in exactly this format:

    THINKING:
    1. [brief thought]
    2. [brief thought]
    3. [brief thought]
    (maximum 5 steps)

    ANSWER:
    [your final answer]"""
    
    return model, system_prompt

if __name__ == "__main__":
    model, system_prompt = chat_with_qwq()
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content="Write a Python function that calculates the Fibonacci sequence")
    ]
    
    # Stream the response
    for chunk in model.stream(messages):
        print(chunk.content, end="", flush=True)
  