import hashlib

def hash_and_print(algorithm, string):
    result = algorithm(string.encode())
    hex_digest = result.hexdigest()
    print(f"The Hexadecimal Equivalent to {algorithm.__name__} is:")
    print(hex_digest)
    print("\r")

def SHA1(string):
    hash_and_print(hashlib.sha1, string)

def SHA224(string):
    hash_and_print(hashlib.sha224, string)

def SHA256(string):
    hash_and_print(hashlib.sha256, string)

def SHA384(string):
    hash_and_print(hashlib.sha384, string)

def SHA512(string):
    hash_and_print(hashlib.sha512, string)

def SHA3_224(string):
    hash_and_print(hashlib.sha3_224, string)

def SHA3_256(string):
    hash_and_print(hashlib.sha3_256, string)

def SHA3_384(string):
    hash_and_print(hashlib.sha3_384, string)

def SHA3_512(string):
    hash_and_print(hashlib.sha3_512, string)

def Blake2b(string):
    hash_and_print(hashlib.blake2b, string)

def Blake2s(string):
    hash_and_print(hashlib.blake2s, string)

def SHAKE_128(string):
    result = hashlib.shake_128(string.encode())
    print(f"The Hexadecimal Equivalent to SHAKE_128 is:")
    print(result.hexdigest(25))
    print("\r")

def SHAKE_256(string):
    result = hashlib.shake_256(string.encode())
    print(f"The Hexadecimal Equivalent to SHAKE_256 is:")
    print(result.hexdigest(25))
    print("\r")

def MD5(string):
    hash_and_print(hashlib.md5, string)
