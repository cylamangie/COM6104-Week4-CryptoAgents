from fastmcp import MCPServer, Tool
import requests

def get_bitcoin_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    data = response.json()
    return f"The current price of Bitcoin (BTC) is ${float(data['price']):,.2f} USD."

server = MCPServer("bitcoin")
server.add_tool(Tool("get_bitcoin_price", get_bitcoin_price))

if __name__ == "__main__":
    server.run()
