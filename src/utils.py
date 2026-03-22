"""Utility helpers."""
import hashlib

def hash_value(val: str) -> str:
    return hashlib.sha256(val.encode()).hexdigest()
