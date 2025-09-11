import os, hashlib, base64

def hash_senha(s: str) -> str:
    salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac("sha256", s.encode(), salt, 100_000)
    return "pbkdf2$%s$%s" % (base64.b64encode(salt).decode(), base64.b64encode(dk).decode())

def verificar_senha(clara: str, armazenada: str) -> bool:
    try:
        scheme, b64_salt, b64_hash = armazenada.split("$", 2)
        if scheme != "pbkdf2": return False
        salt = base64.b64decode(b64_salt.encode())
        esperado = base64.b64decode(b64_hash.encode())
        calc = hashlib.pbkdf2_hmac("sha256", clara.encode(), salt, 100_000)
        return hashlib.compare_digest(calc, esperado)
    except Exception:
        return False
