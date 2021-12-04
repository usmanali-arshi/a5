#!/usr/bin/env python3
import ssl
import argparse
from pathlib import Path
import socket

FILE_DIR: Path = Path(__file__).parent.resolve()
HOST: str = "localhost"


def create_ssl_context(cert_file: str) -> ssl.SSLContext:
    # TODO: Create an SSL context for the server side. You need to load your certificate.
    return ctx


def create_server_socket(host_ip: str, host_port: int) -> socket.socket:
    # TODO: Create a TCP server socket that is configured correctly.
    return bindsocket


def wait_for_ssl_connection(ssl_context: ssl.SSLContext, server_socket: socket.socket) -> ssl.SSLSocket:
    # TODO: Wait for an SSL connection and wrap the new socket in an SSL context.
    # Hint: You should call accept here.
    return conn_stream


def launch_server(server_port: int, cert_file: str) -> bytes:
    # TODO: Use the helper functions to create an SSL server.
    print("Received client SSL message %s", data)
    # TODO: Do not forget to close the socket.
    return data


def main(args):
    launch_server(args.server_port, args.cert_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--server-port",
        default="8000",
        type=int,
        help="The port the server will listen on.",
    )
    parser.add_argument(
        "-c",
        "--cert-file",
        default="cert.pem",
        type=str,
        help="The certificate file the server will use for SSL.",
    )
    # Parse options and process argv
    arguments = parser.parse_args()
    main(arguments)
