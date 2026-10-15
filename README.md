# qx-pki-ssh  (Repo 8)

All TEST ONLY:
- certs/chain.pem: root RSA-4096 -> intermediate ECDSA P-384 -> leaf RSA-2048
- certs/expired_sha1.crt: expired 01-Jan-2025, SHA-1 signed
- certs/service.csr: RSA-2048 CSR
- ssh/: id_ecdsa, id_ed25519 (OpenSSH format), authorized_keys, sshd_config, ssh_config
- keystore/legacy.jks: Java keystore (password changeit) with RSA-2048 key
