"""
This module stores constants used in packet-level data processing for ease of maintenance.
"""
LOG_ERROR = True
LOG_FILE = "parser_errors.log"
TLS_TYPE = {20: "CHANGE_CIPHER_SPEC", 21: "ALERT", 22: "HANDSHAKE", 23: "APPLICATION_DATA"}
TLS_VERSION = {769: "1.0", 770: "1.1", 771: "1.2", 772: "1.3"}
MONGODB_SERVER = "mongodb://localhost:27017/"
IP_SRC = 0
IP_DST = 1
IP_EITHER = 2
