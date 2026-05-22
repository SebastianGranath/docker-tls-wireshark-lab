#!/bin/sh
[ -f /certs/ca.crt ] && exit 0
apk add --no-cache openssl
openssl genrsa -out /certs/ca.key 4096
openssl req -x509 -new -nodes -key /certs/ca.key -days 365 -out /certs/ca.crt -subj "/CN=MyLabCA"
for n in server client; do openssl genrsa -out /certs/$n.key 2048; openssl req -new -key /certs/$n.key -out /certs/$n.csr -subj "/CN=$n"; openssl x509 -req -in /certs/$n.csr -CA /certs/ca.crt -CAkey /certs/ca.key -CAcreateserial -out /certs/$n.crt -days 365; done
