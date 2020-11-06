#!/usr/bin/env python3
""" Main 101
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth(None, None))
print(a.require_auth(None, []))
print(a.require_auth("/api/v1/status/", []))
print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))

excluded_paths = ["/api/v1/stat*"]

print("Require auth with stars:")
print(a.require_auth("/api/v1/users", excluded_paths))
print(a.require_auth("/api/v1/status", excluded_paths))
print(a.require_auth("/api/v1/stats", excluded_paths))
