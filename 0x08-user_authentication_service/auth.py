#!/usr/bin/env python3
"""
Auth methods
"""
import bcrypt


def _hash_password(password: str) -> str:
    """
    Return a salted hash of the input password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
