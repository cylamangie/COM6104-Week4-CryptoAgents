import asyncio
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

async def run_agent():
    client = MultiServerMCPClient(
        {
            "bitcoin": {   # must match the server name above
                "transport": "http",
                "url": "http://127.0.0.1:40000/mcp",
            }
        }
    )

    tools = await client.get_tools()

    llm = ChatOllama(model="qwen3", temperature=0)

    sys_prompt = """You are a helpful and accurate Qwen3 AI assistant deployed locally via Ollama.
    You are provided a tool to lookup the latest price of bitcoin (BTC).
    Use it only when necessary."""

    agent = create_agent(model=llm, tools=tools, system_prompt=sys_prompt)

    query = "What is the price of bitcoin now?"
    response = await agent.ainvoke({"messages": [{"role": "user", "content": query}]})
    print(response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(run_agent())
