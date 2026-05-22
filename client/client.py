import os
import ssl
import socket
import time

print("Client MODE raw:", os.environ.get("MODE"))
MODE = os.getenv("MODE", "TLS").upper()

HOST = "server"
PORT = 8443

time.sleep(3)

print(f"Client mode={MODE}")

sock = socket.create_connection(
    (HOST, PORT)
)

if MODE == "PLAINTEXT":

    conn = sock

else:

    ctx = ssl.create_default_context(
        ssl.Purpose.SERVER_AUTH,
        cafile="/certs/ca.crt"
    )

    ctx.keylog_filename = "/tmp/sslkeys.log"

    if MODE == "MTLS":

        ctx.load_cert_chain(
            "/certs/client.crt",
            "/certs/client.key"
        )

        print(
            "mTLS: sending client cert"
        )

    conn = ctx.wrap_socket(
        sock,
        server_hostname="server"
    )

print("Sending message")

conn.send(
    b"secret message"
)

resp = conn.recv(4096)

print("Response:", resp)

try:
    print(
        "TLS version:",
        conn.version()
    )
    print(
        "Cipher:",
        conn.cipher()
    )
except:
    print("Plain TCP")

conn.close()