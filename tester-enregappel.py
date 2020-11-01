#!/usr/bin/python3	


import asyncio

async def handle_echo(reader, writer): 

	couchdb_reader, couchdb_writer = await asyncio.open_connection(
		'127.0.0.1', 
		5984 
	) 
	couchdb_writer.write( 
		( 
			f"HEAD {url.path or '/'} HTTP/1.0\r\n"
			f"Host: {url.hostname}\r\n"
			f"\r\n" 
		)
	)

	print(f'Send: {message!r}')
	writer.write(message.encode())

	data = await reader.read(100)
	print(f'Received: {data.decode()!r}')

	print('Close the connection')
	writer.close()



	data = await reader.read(100)
	message = data.decode()
	addr = writer.get_extra_info('peername')

	print(f"Received {message!r} from {addr!r}")

	print(f"Send: {message!r}")
	writer.write(data)
	await writer.drain()

	print("Close the connection")
	writer.close()




async def main():
	server = await asyncio.start_server(
		handle_echo, 
		'127.0.0.1', 
		8888 
	)

	print(f'Serving on {server.sockets[0].getsockname()}')

	async with server:
		await server.serve_forever()



asyncio.run(main())




