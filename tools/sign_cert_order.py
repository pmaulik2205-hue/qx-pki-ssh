"""R4-11 HOP 3 of 3: PKI tool in qx-pki-ssh -> qx_mid (qx-polyglot-services) -> qx_core (qx-evasion-lab) = ECDSA P-256."""
from qx_mid.order_signing import sign_order


def sign_certificate_order(order_id: str) -> bytes:
    return sign_order(order_id.encode())
