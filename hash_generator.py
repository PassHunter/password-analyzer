import hashlib

def generate_hashes(password):
    return {
        'MD5': hashlib.md5(password.encode()).hexdigest(),
        'SHA-1': hashlib.sha1(password.encode()).hexdigest(),
        'SHA-256': hashlib.sha256(password.encode()).hexdigest(),
        'SHA-512': hashlib.sha512(password.encode()).hexdigest()
    }
