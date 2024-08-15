# deamon process and API of Pygit++
# EL DEMONIO
#
# Version: pre-v-0.0.0.01
#
# WARN: DO NOT USE THIS CODE.
# WARN: THIS IS JUST A STARTING POINT OF THE FUTURE
# IMPLEMENATATION PLEASE DO NOT USE THIS CODE
#
# WARN: known problems: (0)


from utils.debug import debug
import asyncio
import subprocess
import socket


class Demonio:
    """
    When you create an instance of this class
    it will automaticly create the server

    TODO: Write docs for the api
    """

    """
    Section:
    expose API
    """

    def __init__(self, verbose=True):
        self.verbose = verbose

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('127.0.0.1', 5666))

        self.server.listen(5)
        debug(self.verbose,
              "Server running on: 127.0.0.1:5666",
              "I"
              )

    async def start_listening(self):
        while True:
            client_socket, client_address = await asyncio.to_thread(
                self.server.accept
            )

            debug(
                self.verbose,
                f"Connection established with {client_address}",
                "I"
            )
            asyncio.create_task(self.handle_client(client_socket))

    async def handle_client(self, client_socket):
        try:
            debug(
                self.verbose,
                "Handler client called",
                "W"
            )
            while True:
                data = await asyncio.to_thread(client_socket.recv, 1024)
                debug(
                    self.verbose,
                    f"Recivied: {data}",
                    "M"
                )

                if not data:
                    break

                response = f"Echo: {data.decode('utf-8')}"

                await asyncio.to_thread(
                    client_socket.sendall, response.encode('utf-8')
                )

        finally:
            client_socket.close()
            debug(
                self.verbose,
                "Connection closed",
                "I"
            )


if __name__ == "__main__":
    demonio = Demonio()
    asyncio.run(demonio.start_listening())
