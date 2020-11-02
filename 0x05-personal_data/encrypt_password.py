#!/usr/bin/env python3
"""
Encrypt and validate passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return a salted, hashed password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if a password is valid
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
