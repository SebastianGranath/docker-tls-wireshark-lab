# TLS / mTLS Learning Lab — Step-by-step PM

## Initial setup

1. Open `.env` (or create one)

Choose mode:

```env
MODE=PLAINTEXT
```

or:

```env
MODE=TLS
```

or:

```env
MODE=MTLS
```

2. Start the lab:

```bash
docker compose up --build -d
```

Verify containers:

```bash
docker ps
```

Expected:

- server → Up
- client → Up (or sleeping)
- wireshark → Up
- certs → Exited (0)

---

## Capture traffic

3. Open Wireshark GUI:

```text
http://localhost:3000
```

4. Start capture on:

Try:

```text
vEthernet (WSL)
```

or:

```text
docker0
```

or:

```text
br-*
```

depending on host OS.

5. Add filter:

```text
tcp.port == 8443
```

---

## Generate traffic

6. Trigger client manually:

```bash
docker exec -it tlslabdemo-client-1 python client.py
```

Observe:

- server logs
- client logs
- Wireshark packets

---

## Inspect TCP

7. Identify:

Packet 1:

```text
SYN
```

Packet 2:

```text
SYN, ACK
```

Packet 3:

```text
ACK
```

Discuss:

TCP 3-way handshake completed.

---

## Inspect TLS

(Only if MODE=TLS or MODE=MTLS)

8. Locate:

```text
Client Hello
Server Hello
Certificate
Application Data
```

Inspect:

- TLS version
- Cipher suite
- Extensions
- Certificate chain

---

## Decrypt TLS traffic

9. Confirm key log exists:

Host:

```bash
ls logs
```

Expected:

```text
sslkeys.log
```

10. In Wireshark:

Go:

```text
Edit
→ Preferences
→ Protocols
→ TLS
→ (Pre)-Master-Secret log filename
```

Set:

```text
/logs/sslkeys.log
```

11. Reload capture:

```text
Ctrl + R
```

Observe:

Encrypted:

```text
Application Data
```

becomes:

```text
secret message
```

---

## Compare modes

12. Change `.env`:

Plain TCP:

```env
MODE=PLAINTEXT
```

Rebuild:

```bash
docker compose up --build -d
```

Capture:

Observe:

Plaintext visible directly.

---

13. Change:

```env
MODE=TLS
```

Capture:

Observe:

- Certificate exchange
- Encrypted payload

---

14. Change:

```env
MODE=MTLS
```

Capture:

Observe additional handshake:

```text
Certificate Request
Client Certificate
Certificate Verify
```

Compare against TLS.

---

## Advanced experiments

15. Force TLS1.2 and compare with TLS1.3

Observe:
- Different handshake
- Different cipher negotiation

---

16. Break trust intentionally

Examples:
- Remove CA from client
- Use wrong cert
- Expire cert

Observe failures:
```text
certificate verify failed
```

---

17. Attempt decryption using only:
```text
server.crt
```
or:
```text
server.key
```

Question:
Why does decryption fail for TLS1.3?

Explore:
- ECDHE
- Forward secrecy
- Session keys vs certificates
---

18. Document findings:

For each mode:
- Handshake packets
- Encryption behavior
- Certificate usage
- Decryption method
- Failure modes