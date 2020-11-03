#!/usr/bin/env python3
"""
Class to manage API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return False
        """
        if not path or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        return not path in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Return None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None
        """
        return None
