#!/usr/bin/env python3
"""
A module for hashing and validating passwords using the bcrypt algorithm.
"""
import bcrypt

def hash_password(password: str) -> bytes:
    """
    Hashes a password using the bcrypt algorithm.

    Args:
        password: The password to hash.

    Returns:
        A salted, hashed password as a byte string.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against a hashed password.

    Args:
        hashed_password: The hashed password to compare against.
        password: The plain text password to validate.

    Returns:
        True if the password matches the hashed password, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)