#!/usr/bin/env python3
"""
Return the log message obfuscated
"""

import re
import logging
import csv
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize RedactingFormatter
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter values in incoming log records
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Return the log message obfuscated
    """
    for f in fields:
        message = re.sub(f'(?<={f}=)[^{separator}]*', redaction, message)
    return message


def get_logger() -> logging.Logger:
    """Return a logging.Logger object
    """
    log = logging.getLogger('user_data')
    log.setLevel(logging.INFO)
    log.propagate = False
    handler = logging.StreamHandler()
    hander.setFormatter(RedactingFormatter(PII_FIELDS))
    log.addHandler(handler)
    return log
