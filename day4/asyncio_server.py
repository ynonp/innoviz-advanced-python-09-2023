import asyncio
import logging

async def client_connected_handler(reader, writer):
    line = await reader.readline()
    writer.write(line.upper())
    await writer.drain()
    writer.close()

async def tcp_echo_server():
    print("Starting a server")
    server = await asyncio.start_server(client_connected_handler, port='9191')
    await server.serve_forever()

logging.basicConfig(level=logging.DEBUG)
asyncio.run(tcp_echo_server(), debug=True)

