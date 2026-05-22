import os
import ssl
import socket

HOST = "0.0.0.0"
PORT = 8443

print("Server MODE raw:", os.environ.get("MODE"))
MODE = os.getenv("MODE", "TLS").upper()

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen()

print(f"Starting server in mode={MODE}")
print(f"Listening on {HOST}:{PORT}")

while True:
    conn, addr = sock.accept()

    print("Connection from:", addr)

    if MODE == "PLAINTEXT":
        tls_conn = conn

    else:
        context = ssl.create_default_context(
            ssl.Purpose.CLIENT_AUTH
        )

        context.load_cert_chain(
            "/certs/server.crt",
            "/certs/server.key"
        )

        context.load_verify_locations(
            "/certs/ca.crt"
        )

        if MODE == "MTLS":
            context.verify_mode = ssl.CERT_REQUIRED
            print("mTLS: client cert required")

        else:
            context.verify_mode = ssl.CERT_NONE
            print("TLS: server auth only")

        tls_conn = context.wrap_socket(
            conn,
            server_side=True
        )

    data = tls_conn.recv(4096)

    print("Received:", data)

    try:
        print(
            "TLS version:",
            tls_conn.version()
        )
        print(
            "Cipher:",
            tls_conn.cipher()
        )
    except:
        print("Plain TCP")

    tls_conn.send(
        b"hello from server"
    )

    tls_conn.close()