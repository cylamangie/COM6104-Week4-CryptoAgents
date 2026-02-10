# Conversational AI Lab – Week 4
COM6104 Week 4 lab — Bitcoin agent, MCP integration, and workflow graphs using LangChain + Ollama

## 📌 Overview
This project explores the use of **LangChain**, **Ollama**, and the **Qwen3 model** to build agents that interact with real-time data and workflows.  
It demonstrates how conversational AI can integrate external tools, handle crypto-related queries, and follow structured workflows.

> 📝 **Note**: This is the **fourth lab assignment** for **COM6104 – Topics in Data Science and Artificial Intelligence**.

---

## 🎯 Motivation
AI agents are most powerful when they can:
- Access **real-time data** (e.g., Bitcoin price).
- Integrate with external tools via **LangChain MCP**.
- Follow **workflow graphs** for structured decision-making.

This lab showcases these capabilities through practical exercises.

---

## ⚙️ Exercises Implemented
- **Exercise 1: Bitcoin Agent (Basic)**  
  - Fetches the current Bitcoin price using the Binance API.  
  - Simulates a simple chatbot interaction.

- **Exercise 1 (LLM version): Bitcoin Agent using LangChain**  
  - Uses `ChatOllama` with Qwen3.  
  - Integrates a tool to check BTC price only when needed.

- **Exercise 2: Bitcoin Agent using MCP**  
  - Includes both server (`p253572_bitcoin_mcp_agent.py`) and client (`p253572_agent_using_mcp.py`).  
  - Demonstrates tool integration with asynchronous workflows.

- **Exercise 3: Workflow Graph**  
  - Builds a state graph to detect whether user queries are crypto/finance-related.  
  - Routes queries to appropriate responses using conditional edges.

---

## 📊 Sample Outputs
| Exercise   | Example Input | Example Output |
|------------|---------------|----------------|
| Bitcoin Agent | "What is the price of bitcoin now?" | *The current price of Bitcoin (BTC) is $43,210.12 USD.* |
| Workflow Graph | "Who are you?" | *Invalid topic.* |

---

## 🚀 How to Run
```bash
pip install -r requirements.txt
python week4_lab.py
```
For MCP server/client:
```bash
python p253572_bitcoin_mcp_agent.py   # start server
python p253572_agent_using_mcp.py     # run client agent
```

## 📚 Course Context
Completed as part of COM6104 – Topics in Data Science and Artificial Intelligence at The Hang Seng University of Hong Kong.

## 💡 Reflection
This lab helped me understand how conversational AI can integrate with external APIs, use LangChain MCP for tool orchestration, and follow structured workflows.
It highlights the importance of combining real-time data access with workflow logic to build reliable AI agents.

## 📚 Acknowledgements
Parts of this code were adapted from COM6104 lab materials provided by the instructor.
This repository is licensed under the MIT License, which permits reuse and modification with proper attribution.
