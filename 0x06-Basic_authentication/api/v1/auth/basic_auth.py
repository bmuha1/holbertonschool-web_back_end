#!/usr/bin/env python3
"""
BasicAuth class to manage API authentication
"""
from api.v1.auth.auth import Auth


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
