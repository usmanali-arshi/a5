#!/usr/bin/env python3
import ssl
import argparse
from pathlib import Path
import socket

FILE_DIR: Path = Path(__file__).parent.resolve()
HOST: str = "localhost"


def create_ssl_context(cert_file: str) -> ssl.SSLContext:
    # TODO: Create an SSL context for the server side. You need to load your certificate.

    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.load_cert_chain(certfile="cert")
    # ctx.check_hostname=False
    # ctx.verify_mode=ssl.CERT_NONE

    # bindsocket = socket.socket()
    # bindsocket.bind(('myaddr.mydomain.com', 10023))
    # bindsocket.listen(5)
    return ctx


def create_server_socket(host_ip: str, host_port: int) -> socket.socket:
    # TODO: Create a TCP server socket that is configured correctly.
    bindsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bindsocket.bind((host_ip, host_port))
    bindsocket.listen(5)

    return bindsocket


def wait_for_ssl_connection(ssl_context: ssl.SSLContext, server_socket: socket.socket) -> ssl.SSLSocket:
    # TODO: Wait for an SSL connection and wrap the new socket in an SSL context.
    
    # while True:
    newsocket, fromaddr = server_socket.accept()
    conn_stream = ssl_context.wrap_socket(newsocket, server_side=True)
    

    # Hint: You should call accept here.
    return conn_stream


def launch_server(server_port: int, cert_file: str) -> bytes:
    # TODO: Use the helper functions to create an SSL server.
    ssl _cxt = create_ssl_context(cert_file)
    server_sock = create_server_socket(HOST, 10023)
    while True:
        conStream = wait_for_ssl_connection(ssl_cxt, server_sock)
        try:
            data =conStream.recv(1024)
            while data:
                data = conStream.recv(1024)
        finally:
            conStream.shutdown(socket.SHUT_RDWR)
            conStream.close()



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
