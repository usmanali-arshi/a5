#!/usr/bin/env python3
import ssl
import argparse
import socket
from pathlib import Path

FILE_DIR: Path = Path(__file__).parent.resolve()
HOST: str = "localhost"


def create_ssl_context() -> ssl.SSLContext:
    # TODO: Create an SSL context. Do not forget to disable security properties.
    return ctx


def create_client_ssl_socket(ctx: ssl.SSLContext, host_ip: str) -> ssl.SSLSocket:
    # TODO: Wrap the socket using the SSL context.
    return client_socket


def launch_client(server_port: int) -> None:
    # TODO: Create an SSL context.
    ctx = create_ssl_context()
    # TODO: Create an SSL client socket.
    client_socket = create_client_ssl_socket(ctx, HOST)
    # TODO: Connect to the server and send an encrypted SSL message.
    msg = b"This message is encrypted with SSL."
    # TODO: Do not forget to close the socket.


def main(args):
    launch_client(args.server_port)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--server-port",
        default="8000",
        type=int,
        help="The port the client will connect to.",
    )
    # Parse options and process argv
    arguments = parser.parse_args()
    main(arguments)
