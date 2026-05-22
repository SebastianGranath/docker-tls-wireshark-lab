# TLS / mTLS Learning Lab (Open Source)

An open-source, hands-on lab for exploring TCP, TLS, and mTLS by
capturing, inspecting, and decrypting real traffic.

## Features

-   Plain TCP (`PLAINTEXT`)
-   TLS (`TLS`)
-   Mutual TLS (`MTLS`)
-   Auto-generated certificates
-   Browser-based Wireshark GUI
-   TLS session key logging (`sslkeys.log`)
-   Docker Compose setup
-   Guided exercises

## Quick Start

``` bash
docker compose up --build
```

Open Wireshark:

`http://localhost:3000`

Generate traffic:

``` bash
docker exec -it tlslabdemo-client-1 python client.py
```

Filter:

``` text
tcp.port == 8443
```

## Learning Goals

-   Understand TCP handshakes
-   Inspect TLS handshakes and certificates
-   Compare plaintext, TLS, and mTLS
-   Decrypt TLS with session keys
-   Understand forward secrecy

## Contributing

PRs, experiments, and improvements are welcome.

## License

MIT
