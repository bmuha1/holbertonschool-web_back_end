#!/usr/bin/env python3
"""
BasicAuth class to manage API authentication
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class to manage API authentication
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Return the Base64 part of the Authorization header
        """
        if (isinstance(authorization_header, str) and
                authorization_header.startswith('Basic ')):
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Return the decoded value of a Base64 string
        """
        try:
            return base64.b64decode(
                base64_authorization_header.encode('utf-8')).decode('utf-8')
        except Exception:
            return
