#!/usr/bin/env python3
from random import random
import socket
import argparse
from pathlib import Path
from sys import base_exec_prefix
from typing import Tuple

FILE_DIR: Path = Path(__file__).parent.resolve()
HOST: str = "localhost"


# TODO: Choose a P value that is shared with the client.
P: int = 23


def calculate_shared_secret(g: int, secret: int, p: int) -> int:
    # TODO: Calculate the shared secret and return it
    calculation = (g**secret) %p 
    return calculation


def exchange_base_number(sock: socket.socket) -> int:
    # TODO: Wait for a client message that sends a base number.
    # while True:
    (comm_socket, client_addr) = sock.accept()
    proposal = comm_socket.recv(1024)
    proposal = int.from_bytes(proposal, 'big')
        # try:
        #     data =comm_socket.recv(1024)
        #     while data:
        #         data = conStream.recv(1024)

    # TODO: Return a message that the base number has been received.
    print("base number has been received")
    return proposal


def launch_server(server_port: int) -> Tuple[int, int, int]:
    # TODO: Create a server socket. can be UDP or TCP.
    tcp_sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    tcp_sock_server.bind((HOST, server_port))

    tcp_sock_server.listen(5)

    
    x = exchange_base_number(tcp_sock_server)



    

    # TODO: Wait for the client to propose a base for the key exchange.
    print("Base int is %s" % x)
    # TODO: Wait for the nonce computed by the client.how?

    y = random.randint(1,100)
    public_key = calculate_shared_secret(x, y, P)
    tcp_sock_server.send(public_key.to_bytes(4, 'big'))

    rx_int = tcp_sock_server.recv(1024)
    rx_int = int.from_bytes(rx_int, 'big')
    # TODO: Also reply to the client.
    
    print("Int received from peer is %s" % rx_int)
    
    # TODO: Compute the shared secret using the secret number.
    secret = calculate_shared_secret(rx_int, y, P)
    print("Y is %s" % y)
    print("Shared secret is %s" % secret)
    # TODO: Do not forget to close the socket.
    # TODO: Return the base number, the secret integer, and the shared secret
    base = x
    secret_integer = y
    shared_secret = secret
    return base, secret_integer, shared_secret


def main(args):
    launch_server(args.server_port)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--server-port",
        default="8000",
        type=int,
        help="The port the server will listen on.",
    )
    # Parse options and process argv
    arguments = parser.parse_args()
    main(arguments)
