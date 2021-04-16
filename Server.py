import socket
import threading
from CommandParser import CommandParser


class Server:
    """
    This class listens to and handles all the incoming client connections.
    Supports multiple concurrent clients.

    ...

    Attributes
    ----------
    port : int
        This attribute represents the port, server is listening at.
    socket : socket
        A socket object that listens to the incoming connections and initiates a separate thread
        for each of the incoming client connections.


    Methods
    -------
    listen()
        This method listens to incoming client connections and spins off each client
        with a new thread.

    ClientThread()
        This method is run as a thread. It handles all the network operations
        between the client and the server.

    """

    def __init__(self, port):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def listen(self):
        """
        Listens to incoming client connection.

        Parameters
        ----------
        None

        Returns
        ------
        Doesn't return until the program is shutdown.
        """
        self.socket.bind(('localhost', self.port))
        self.socket.listen(10)
        print("TelnetServer listening at port: " + str(self.port))
        while True:
            clientSocket, _ = self.socket.accept()
            clientThread = threading.Thread(target=self.ClientThread, args=([clientSocket]))
            clientThread.start()
            print("A client just connected.")

    def ClientThread(self, clientSocket):
        """
        Handles network I/O with the client.

        Parameters
        ----------
        clientSocket : socket
            The socket object that is connected to the remote client's socket.

        Returns
        ------
        Doesn't return anything. Stops when client issues stop command.
        """
        commandParser = CommandParser()
        while True:
            try:
                command = clientSocket.recv(4096)
                command = command.decode()
                response = commandParser.parseCommand(command)
                if response == "Stop":
                    clientSocket.sendall("\nThank you for using our telnet server. Bye.\n".encode())
                    clientSocket.close()
                    break
                clientSocket.sendall((str(response)+"\n").encode())
            except:
                clientSocket.sendall("\nOops! something went wrong with the connection.\n".encode())
