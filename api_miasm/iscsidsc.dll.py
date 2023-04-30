ISCSI_AUTH_TYPES = {
    "ISCSI_NO_AUTH_TYPE": 0,
    "ISCSI_CHAP_AUTH_TYPE": 1,
    "ISCSI_MUTUAL_CHAP_AUTH_TYPE": 2,
}
ISCSI_AUTH_TYPES_INV = {
    0: "ISCSI_NO_AUTH_TYPE",
    1: "ISCSI_CHAP_AUTH_TYPE",
    2: "ISCSI_MUTUAL_CHAP_AUTH_TYPE",
}
ISCSI_DIGEST_TYPES = {
    "ISCSI_DIGEST_TYPE_NONE": 0,
    "ISCSI_DIGEST_TYPE_CRC32C": 1,
}
ISCSI_DIGEST_TYPES_INV = {
    0: "ISCSI_DIGEST_TYPE_NONE",
    1: "ISCSI_DIGEST_TYPE_CRC32C",
}
ISDSC_STATUS = {
    "ISDSC_NON_SPECIFIC_ERROR": 0xEFFF0001,
    "ISDSC_LOGIN_FAILED": 0xEFFF0002,
    "ISDSC_CONNECTION_FAILED": 0xEFFF0003,
    "ISDSC_INITIATOR_NODE_ALREADY_EXISTS": 0xEFFF0004,
    "ISDSC_INITIATOR_NODE_NOT_FOUND": 0xEFFF0005,
    "ISDSC_TARGET_MOVED_TEMPORARILY": 0xEFFF0006,
    "ISDSC_TARGET_MOVED_PERMANENTLY": 0xEFFF0007,
    "ISDSC_INITIATOR_ERROR": 0xEFFF0008,
    "ISDSC_AUTHENTICATION_FAILURE": 0xEFFF0009,
    "ISDSC_AUTHORIZATION_FAILURE": 0xEFFF000A,
    "ISDSC_NOT_FOUND": 0xEFFF000B,
    "ISDSC_TARGET_REMOVED": 0xEFFF000C,
    "ISDSC_UNSUPPORTED_VERSION": 0xEFFF000D,
    "ISDSC_TOO_MANY_CONNECTIONS": 0xEFFF000E,
    "ISDSC_MISSING_PARAMETER": 0xEFFF000F,
    "ISDSC_CANT_INCLUDE_IN_SESSION": 0xEFFF0010,
    "ISDSC_SESSION_TYPE_NOT_SUPPORTED": 0xEFFF0011,
    "ISDSC_TARGET_ERROR": 0xEFFF0012,
    "ISDSC_SERVICE_UNAVAILABLE": 0xEFFF0013,
    "ISDSC_OUT_OF_RESOURCES": 0xEFFF0014,
    "ISDSC_CONNECTION_ALREADY_EXISTS": 0xEFFF0015,
    "ISDSC_SESSION_ALREADY_EXISTS": 0xEFFF0016,
    "ISDSC_INITIATOR_INSTANCE_NOT_FOUND": 0xEFFF0017,
    "ISDSC_TARGET_ALREADY_EXISTS": 0xEFFF0018,
    "ISDSC_DRIVER_BUG": 0xEFFF0019,
    "ISDSC_INVALID_TEXT_KEY": 0xEFFF001A,
    "ISDSC_INVALID_SENDTARGETS_TEXT": 0xEFFF001B,
    "ISDSC_INVALID_SESSION_ID": 0xEFFF001C,
    "ISDSC_SCSI_REQUEST_FAILED": 0xEFFF001D,
    "ISDSC_TOO_MANY_SESSIONS": 0xEFFF001E,
    "ISDSC_SESSION_BUSY": 0xEFFF001F,
    "ISDSC_TARGET_MAPPING_UNAVAILABLE": 0xEFFF0020,
    "ISDSC_ADDRESS_TYPE_NOT_SUPPORTED": 0xEFFF0021,
    "ISDSC_LOGON_FAILED": 0xEFFF0022,
    "ISDSC_SEND_FAILED": 0xEFFF0023,
    "ISDSC_TRANSPORT_ERROR": 0xEFFF0024,
    "ISDSC_VERSION_MISMATCH": 0xEFFF0025,
    "ISDSC_TARGET_MAPPING_OUT_OF_RANGE": 0xEFFF0026,
    "ISDSC_TARGET_PRESHAREDKEY_UNAVAILABLE": 0xEFFF0027,
    "ISDSC_TARGET_AUTHINFO_UNAVAILABLE": 0xEFFF0028,
    "ISDSC_TARGET_NOT_FOUND": 0xEFFF0029,
    "ISDSC_LOGIN_USER_INFO_BAD": 0xEFFF002A,
    "ISDSC_TARGET_MAPPING_EXISTS": 0xEFFF002B,
    "ISDSC_HBA_SECURITY_CACHE_FULL": 0xEFFF002C,
    "ISDSC_INVALID_PORT_NUMBER": 0xEFFF002D,
    "ISDSC_OPERATION_NOT_ALL_SUCCESS": 0xAFFF002E,
    "ISDSC_HBA_SECURITY_CACHE_NOT_SUPPORTED": 0xEFFF002F,
    "ISDSC_IKE_ID_PAYLOAD_TYPE_NOT_SUPPORTED": 0xEFFF0030,
    "ISDSC_IKE_ID_PAYLOAD_INCORRECT_SIZE": 0xEFFF0031,
    "ISDSC_TARGET_PORTAL_ALREADY_EXISTS": 0xEFFF0032,
    "ISDSC_TARGET_ADDRESS_ALREADY_EXISTS": 0xEFFF0033,
    "ISDSC_NO_AUTH_INFO_AVAILABLE": 0xEFFF0034,
    "ISDSC_NO_TUNNEL_OUTER_MODE_ADDRESS": 0xEFFF0035,
    "ISDSC_CACHE_CORRUPTED": 0xEFFF0036,
    "ISDSC_REQUEST_NOT_SUPPORTED": 0xEFFF0037,
    "ISDSC_TARGET_OUT_OF_RESORCES": 0xEFFF0038,
    "ISDSC_SERVICE_DID_NOT_RESPOND": 0xEFFF0039,
    "ISDSC_ISNS_SERVER_NOT_FOUND": 0xEFFF003A,
    "ISDSC_OPERATION_REQUIRES_REBOOT": 0xAFFF003B,
    "ISDSC_NO_PORTAL_SPECIFIED": 0xEFFF003C,
    "ISDSC_CANT_REMOVE_LAST_CONNECTION": 0xEFFF003D,
    "ISDSC_SERVICE_NOT_RUNNING": 0xEFFF003E,
    "ISDSC_TARGET_ALREADY_LOGGED_IN": 0xEFFF003F,
    "ISDSC_DEVICE_BUSY_ON_SESSION": 0xEFFF0040,
    "ISDSC_COULD_NOT_SAVE_PERSISTENT_LOGIN_DATA": 0xEFFF0041,
    "ISDSC_COULD_NOT_REMOVE_PERSISTENT_LOGIN_DATA": 0xEFFF0042,
    "ISDSC_PORTAL_NOT_FOUND": 0xEFFF0043,
    "ISDSC_INITIATOR_NOT_FOUND": 0xEFFF0044,
    "ISDSC_DISCOVERY_MECHANISM_NOT_FOUND": 0xEFFF0045,
    "ISDSC_IPSEC_NOT_SUPPORTED_ON_OS": 0xEFFF0046,
    "ISDSC_PERSISTENT_LOGIN_TIMEOUT": 0xEFFF0047,
    "ISDSC_SHORT_CHAP_SECRET": 0xAFFF0048,
    "ISDSC_EVALUATION_PEROID_EXPIRED": 0xEFFF0049,
    "ISDSC_INVALID_CHAP_SECRET": 0xEFFF004A,
    "ISDSC_INVALID_TARGET_CHAP_SECRET": 0xEFFF004B,
    "ISDSC_INVALID_INITIATOR_CHAP_SECRET": 0xEFFF004C,
    "ISDSC_INVALID_CHAP_USER_NAME": 0xEFFF004D,
    "ISDSC_INVALID_LOGON_AUTH_TYPE": 0xEFFF004E,
    "ISDSC_INVALID_TARGET_MAPPING": 0xEFFF004F,
    "ISDSC_INVALID_TARGET_ID": 0xEFFF0050,
    "ISDSC_INVALID_ISCSI_NAME": 0xEFFF0051,
    "ISDSC_INCOMPATIBLE_ISNS_VERSION": 0xEFFF0052,
    "ISDSC_FAILED_TO_CONFIGURE_IPSEC": 0xEFFF0053,
    "ISDSC_BUFFER_TOO_SMALL": 0xEFFF0054,
    "ISDSC_INVALID_LOAD_BALANCE_POLICY": 0xEFFF0055,
    "ISDSC_INVALID_PARAMETER": 0xEFFF0056,
    "ISDSC_DUPLICATE_PATH_SPECIFIED": 0xEFFF0057,
    "ISDSC_PATH_COUNT_MISMATCH": 0xEFFF0058,
    "ISDSC_INVALID_PATH_ID": 0xEFFF0059,
    "ISDSC_MULTIPLE_PRIMARY_PATHS_SPECIFIED": 0xEFFF005A,
    "ISDSC_NO_PRIMARY_PATH_SPECIFIED": 0xEFFF005B,
    "ISDSC_DEVICE_ALREADY_PERSISTENTLY_BOUND": 0xEFFF005C,
    "ISDSC_DEVICE_NOT_FOUND": 0xEFFF005D,
    "ISDSC_DEVICE_NOT_ISCSI_OR_PERSISTENT": 0xEFFF005E,
    "ISDSC_DNS_NAME_UNRESOLVED": 0xEFFF005F,
    "ISDSC_NO_CONNECTION_AVAILABLE": 0xEFFF0060,
    "ISDSC_LB_POLICY_NOT_SUPPORTED": 0xEFFF0061,
    "ISDSC_REMOVE_CONNECTION_IN_PROGRESS": 0xEFFF0062,
    "ISDSC_INVALID_CONNECTION_ID": 0xEFFF0063,
    "ISDSC_CANNOT_REMOVE_LEADING_CONNECTION": 0xEFFF0064,
    "ISDSC_RESTRICTED_BY_GROUP_POLICY": 0xEFFF0065,
    "ISDSC_ISNS_FIREWALL_BLOCKED": 0xEFFF0066,
}
ISDSC_STATUS_INV = {
    0xEFFF0001: "ISDSC_NON_SPECIFIC_ERROR",
    0xEFFF0002: "ISDSC_LOGIN_FAILED",
    0xEFFF0003: "ISDSC_CONNECTION_FAILED",
    0xEFFF0004: "ISDSC_INITIATOR_NODE_ALREADY_EXISTS",
    0xEFFF0005: "ISDSC_INITIATOR_NODE_NOT_FOUND",
    0xEFFF0006: "ISDSC_TARGET_MOVED_TEMPORARILY",
    0xEFFF0007: "ISDSC_TARGET_MOVED_PERMANENTLY",
    0xEFFF0008: "ISDSC_INITIATOR_ERROR",
    0xEFFF0009: "ISDSC_AUTHENTICATION_FAILURE",
    0xEFFF000A: "ISDSC_AUTHORIZATION_FAILURE",
    0xEFFF000B: "ISDSC_NOT_FOUND",
    0xEFFF000C: "ISDSC_TARGET_REMOVED",
    0xEFFF000D: "ISDSC_UNSUPPORTED_VERSION",
    0xEFFF000E: "ISDSC_TOO_MANY_CONNECTIONS",
    0xEFFF000F: "ISDSC_MISSING_PARAMETER",
    0xEFFF0010: "ISDSC_CANT_INCLUDE_IN_SESSION",
    0xEFFF0011: "ISDSC_SESSION_TYPE_NOT_SUPPORTED",
    0xEFFF0012: "ISDSC_TARGET_ERROR",
    0xEFFF0013: "ISDSC_SERVICE_UNAVAILABLE",
    0xEFFF0014: "ISDSC_OUT_OF_RESOURCES",
    0xEFFF0015: "ISDSC_CONNECTION_ALREADY_EXISTS",
    0xEFFF0016: "ISDSC_SESSION_ALREADY_EXISTS",
    0xEFFF0017: "ISDSC_INITIATOR_INSTANCE_NOT_FOUND",
    0xEFFF0018: "ISDSC_TARGET_ALREADY_EXISTS",
    0xEFFF0019: "ISDSC_DRIVER_BUG",
    0xEFFF001A: "ISDSC_INVALID_TEXT_KEY",
    0xEFFF001B: "ISDSC_INVALID_SENDTARGETS_TEXT",
    0xEFFF001C: "ISDSC_INVALID_SESSION_ID",
    0xEFFF001D: "ISDSC_SCSI_REQUEST_FAILED",
    0xEFFF001E: "ISDSC_TOO_MANY_SESSIONS",
    0xEFFF001F: "ISDSC_SESSION_BUSY",
    0xEFFF0020: "ISDSC_TARGET_MAPPING_UNAVAILABLE",
    0xEFFF0021: "ISDSC_ADDRESS_TYPE_NOT_SUPPORTED",
    0xEFFF0022: "ISDSC_LOGON_FAILED",
    0xEFFF0023: "ISDSC_SEND_FAILED",
    0xEFFF0024: "ISDSC_TRANSPORT_ERROR",
    0xEFFF0025: "ISDSC_VERSION_MISMATCH",
    0xEFFF0026: "ISDSC_TARGET_MAPPING_OUT_OF_RANGE",
    0xEFFF0027: "ISDSC_TARGET_PRESHAREDKEY_UNAVAILABLE",
    0xEFFF0028: "ISDSC_TARGET_AUTHINFO_UNAVAILABLE",
    0xEFFF0029: "ISDSC_TARGET_NOT_FOUND",
    0xEFFF002A: "ISDSC_LOGIN_USER_INFO_BAD",
    0xEFFF002B: "ISDSC_TARGET_MAPPING_EXISTS",
    0xEFFF002C: "ISDSC_HBA_SECURITY_CACHE_FULL",
    0xEFFF002D: "ISDSC_INVALID_PORT_NUMBER",
    0xAFFF002E: "ISDSC_OPERATION_NOT_ALL_SUCCESS",
    0xEFFF002F: "ISDSC_HBA_SECURITY_CACHE_NOT_SUPPORTED",
    0xEFFF0030: "ISDSC_IKE_ID_PAYLOAD_TYPE_NOT_SUPPORTED",
    0xEFFF0031: "ISDSC_IKE_ID_PAYLOAD_INCORRECT_SIZE",
    0xEFFF0032: "ISDSC_TARGET_PORTAL_ALREADY_EXISTS",
    0xEFFF0033: "ISDSC_TARGET_ADDRESS_ALREADY_EXISTS",
    0xEFFF0034: "ISDSC_NO_AUTH_INFO_AVAILABLE",
    0xEFFF0035: "ISDSC_NO_TUNNEL_OUTER_MODE_ADDRESS",
    0xEFFF0036: "ISDSC_CACHE_CORRUPTED",
    0xEFFF0037: "ISDSC_REQUEST_NOT_SUPPORTED",
    0xEFFF0038: "ISDSC_TARGET_OUT_OF_RESORCES",
    0xEFFF0039: "ISDSC_SERVICE_DID_NOT_RESPOND",
    0xEFFF003A: "ISDSC_ISNS_SERVER_NOT_FOUND",
    0xAFFF003B: "ISDSC_OPERATION_REQUIRES_REBOOT",
    0xEFFF003C: "ISDSC_NO_PORTAL_SPECIFIED",
    0xEFFF003D: "ISDSC_CANT_REMOVE_LAST_CONNECTION",
    0xEFFF003E: "ISDSC_SERVICE_NOT_RUNNING",
    0xEFFF003F: "ISDSC_TARGET_ALREADY_LOGGED_IN",
    0xEFFF0040: "ISDSC_DEVICE_BUSY_ON_SESSION",
    0xEFFF0041: "ISDSC_COULD_NOT_SAVE_PERSISTENT_LOGIN_DATA",
    0xEFFF0042: "ISDSC_COULD_NOT_REMOVE_PERSISTENT_LOGIN_DATA",
    0xEFFF0043: "ISDSC_PORTAL_NOT_FOUND",
    0xEFFF0044: "ISDSC_INITIATOR_NOT_FOUND",
    0xEFFF0045: "ISDSC_DISCOVERY_MECHANISM_NOT_FOUND",
    0xEFFF0046: "ISDSC_IPSEC_NOT_SUPPORTED_ON_OS",
    0xEFFF0047: "ISDSC_PERSISTENT_LOGIN_TIMEOUT",
    0xAFFF0048: "ISDSC_SHORT_CHAP_SECRET",
    0xEFFF0049: "ISDSC_EVALUATION_PEROID_EXPIRED",
    0xEFFF004A: "ISDSC_INVALID_CHAP_SECRET",
    0xEFFF004B: "ISDSC_INVALID_TARGET_CHAP_SECRET",
    0xEFFF004C: "ISDSC_INVALID_INITIATOR_CHAP_SECRET",
    0xEFFF004D: "ISDSC_INVALID_CHAP_USER_NAME",
    0xEFFF004E: "ISDSC_INVALID_LOGON_AUTH_TYPE",
    0xEFFF004F: "ISDSC_INVALID_TARGET_MAPPING",
    0xEFFF0050: "ISDSC_INVALID_TARGET_ID",
    0xEFFF0051: "ISDSC_INVALID_ISCSI_NAME",
    0xEFFF0052: "ISDSC_INCOMPATIBLE_ISNS_VERSION",
    0xEFFF0053: "ISDSC_FAILED_TO_CONFIGURE_IPSEC",
    0xEFFF0054: "ISDSC_BUFFER_TOO_SMALL",
    0xEFFF0055: "ISDSC_INVALID_LOAD_BALANCE_POLICY",
    0xEFFF0056: "ISDSC_INVALID_PARAMETER",
    0xEFFF0057: "ISDSC_DUPLICATE_PATH_SPECIFIED",
    0xEFFF0058: "ISDSC_PATH_COUNT_MISMATCH",
    0xEFFF0059: "ISDSC_INVALID_PATH_ID",
    0xEFFF005A: "ISDSC_MULTIPLE_PRIMARY_PATHS_SPECIFIED",
    0xEFFF005B: "ISDSC_NO_PRIMARY_PATH_SPECIFIED",
    0xEFFF005C: "ISDSC_DEVICE_ALREADY_PERSISTENTLY_BOUND",
    0xEFFF005D: "ISDSC_DEVICE_NOT_FOUND",
    0xEFFF005E: "ISDSC_DEVICE_NOT_ISCSI_OR_PERSISTENT",
    0xEFFF005F: "ISDSC_DNS_NAME_UNRESOLVED",
    0xEFFF0060: "ISDSC_NO_CONNECTION_AVAILABLE",
    0xEFFF0061: "ISDSC_LB_POLICY_NOT_SUPPORTED",
    0xEFFF0062: "ISDSC_REMOVE_CONNECTION_IN_PROGRESS",
    0xEFFF0063: "ISDSC_INVALID_CONNECTION_ID",
    0xEFFF0064: "ISDSC_CANNOT_REMOVE_LEADING_CONNECTION",
    0xEFFF0065: "ISDSC_RESTRICTED_BY_GROUP_POLICY",
    0xEFFF0066: "ISDSC_ISNS_FIREWALL_BLOCKED",
}
TARGET_INFORMATION_CLASS = {
    "ProtocolType": 0,
    "TargetAlias": 1,
    "DiscoveryMechanisms": 2,
    "PortalGroups": 3,
    "PersistentTargetMappings": 4,
    "InitiatorName": 5,
    "TargetFlags": 6,
    "LoginOptions": 7,
}
TARGET_INFORMATION_CLASS_INV = {
    0: "ProtocolType",
    1: "TargetAlias",
    2: "DiscoveryMechanisms",
    3: "PortalGroups",
    4: "PersistentTargetMappings",
    5: "InitiatorName",
    6: "TargetFlags",
    7: "LoginOptions",
}
DEVICE_TYPE = {
    "FILE_DEVICE_BEEP": 0x00000001,
    "FILE_DEVICE_CD_ROM": 0x00000002,
    "FILE_DEVICE_CD_ROM_FILE_SYSTEM": 0x00000003,
    "FILE_DEVICE_CONTROLLER": 0x00000004,
    "FILE_DEVICE_DATALINK": 0x00000005,
    "FILE_DEVICE_DFS": 0x00000006,
    "FILE_DEVICE_DISK": 0x00000007,
    "FILE_DEVICE_DISK_FILE_SYSTEM": 0x00000008,
    "FILE_DEVICE_FILE_SYSTEM": 0x00000009,
    "FILE_DEVICE_INPORT_PORT": 0x0000000a,
    "FILE_DEVICE_KEYBOARD": 0x0000000b,
    "FILE_DEVICE_MAILSLOT": 0x0000000c,
    "FILE_DEVICE_MIDI_IN": 0x0000000d,
    "FILE_DEVICE_MIDI_OUT": 0x0000000e,
    "FILE_DEVICE_MOUSE": 0x0000000f,
    "FILE_DEVICE_MULTI_UNC_PROVIDER": 0x00000010,
    "FILE_DEVICE_NAMED_PIPE": 0x00000011,
    "FILE_DEVICE_NETWORK": 0x00000012,
    "FILE_DEVICE_NETWORK_BROWSER": 0x00000013,
    "FILE_DEVICE_NETWORK_FILE_SYSTEM": 0x00000014,
    "FILE_DEVICE_NULL": 0x00000015,
    "FILE_DEVICE_PARALLEL_PORT": 0x00000016,
    "FILE_DEVICE_PHYSICAL_NETCARD": 0x00000017,
    "FILE_DEVICE_PRINTER": 0x00000018,
    "FILE_DEVICE_SCANNER": 0x00000019,
    "FILE_DEVICE_SERIAL_MOUSE_PORT": 0x0000001a,
    "FILE_DEVICE_SERIAL_PORT": 0x0000001b,
    "FILE_DEVICE_SCREEN": 0x0000001c,
    "FILE_DEVICE_SOUND": 0x0000001d,
    "FILE_DEVICE_STREAMS": 0x0000001e,
    "FILE_DEVICE_TAPE": 0x0000001f,
    "FILE_DEVICE_TAPE_FILE_SYSTEM": 0x00000020,
    "FILE_DEVICE_TRANSPORT": 0x00000021,
    "FILE_DEVICE_UNKNOWN": 0x00000022,
    "FILE_DEVICE_VIDEO": 0x00000023,
    "FILE_DEVICE_VIRTUAL_DISK": 0x00000024,
    "FILE_DEVICE_WAVE_IN": 0x00000025,
    "FILE_DEVICE_WAVE_OUT": 0x00000026,
    "FILE_DEVICE_8042_PORT": 0x00000027,
    "FILE_DEVICE_NETWORK_REDIRECTOR": 0x00000028,
    "FILE_DEVICE_BATTERY": 0x00000029,
    "FILE_DEVICE_BUS_EXTENDER": 0x0000002a,
    "FILE_DEVICE_MODEM": 0x0000002b,
    "FILE_DEVICE_VDM": 0x0000002c,
    "FILE_DEVICE_MASS_STORAGE": 0x0000002d,
    "FILE_DEVICE_SMB": 0x0000002e,
    "FILE_DEVICE_KS": 0x0000002f,
    "FILE_DEVICE_CHANGER": 0x00000030,
    "FILE_DEVICE_SMARTCARD": 0x00000031,
    "FILE_DEVICE_ACPI": 0x00000032,
    "FILE_DEVICE_DVD": 0x00000033,
    "FILE_DEVICE_FULLSCREEN_VIDEO": 0x00000034,
    "FILE_DEVICE_DFS_FILE_SYSTEM": 0x00000035,
    "FILE_DEVICE_DFS_VOLUME": 0x00000036,
    "FILE_DEVICE_SERENUM": 0x00000037,
    "FILE_DEVICE_TERMSRV": 0x00000038,
    "FILE_DEVICE_KSEC": 0x00000039,
    "FILE_DEVICE_FIPS": 0x0000003A,
    "FILE_DEVICE_INFINIBAND": 0x0000003B,
    "FILE_DEVICE_VMBUS": 0x0000003E,
    "FILE_DEVICE_CRYPT_PROVIDER": 0x0000003F,
    "FILE_DEVICE_WPD": 0x00000040,
    "FILE_DEVICE_BLUETOOTH": 0x00000041,
    "FILE_DEVICE_MT_COMPOSITE": 0x00000042,
    "FILE_DEVICE_MT_TRANSPORT": 0x00000043,
    "FILE_DEVICE_BIOMETRIC": 0x00000044,
    "FILE_DEVICE_PMI": 0x00000045,
}
DEVICE_TYPE_INV = {
    0x00000001: "FILE_DEVICE_BEEP",
    0x00000002: "FILE_DEVICE_CD_ROM",
    0x00000003: "FILE_DEVICE_CD_ROM_FILE_SYSTEM",
    0x00000004: "FILE_DEVICE_CONTROLLER",
    0x00000005: "FILE_DEVICE_DATALINK",
    0x00000006: "FILE_DEVICE_DFS",
    0x00000007: "FILE_DEVICE_DISK",
    0x00000008: "FILE_DEVICE_DISK_FILE_SYSTEM",
    0x00000009: "FILE_DEVICE_FILE_SYSTEM",
    0x0000000a: "FILE_DEVICE_INPORT_PORT",
    0x0000000b: "FILE_DEVICE_KEYBOARD",
    0x0000000c: "FILE_DEVICE_MAILSLOT",
    0x0000000d: "FILE_DEVICE_MIDI_IN",
    0x0000000e: "FILE_DEVICE_MIDI_OUT",
    0x0000000f: "FILE_DEVICE_MOUSE",
    0x00000010: "FILE_DEVICE_MULTI_UNC_PROVIDER",
    0x00000011: "FILE_DEVICE_NAMED_PIPE",
    0x00000012: "FILE_DEVICE_NETWORK",
    0x00000013: "FILE_DEVICE_NETWORK_BROWSER",
    0x00000014: "FILE_DEVICE_NETWORK_FILE_SYSTEM",
    0x00000015: "FILE_DEVICE_NULL",
    0x00000016: "FILE_DEVICE_PARALLEL_PORT",
    0x00000017: "FILE_DEVICE_PHYSICAL_NETCARD",
    0x00000018: "FILE_DEVICE_PRINTER",
    0x00000019: "FILE_DEVICE_SCANNER",
    0x0000001a: "FILE_DEVICE_SERIAL_MOUSE_PORT",
    0x0000001b: "FILE_DEVICE_SERIAL_PORT",
    0x0000001c: "FILE_DEVICE_SCREEN",
    0x0000001d: "FILE_DEVICE_SOUND",
    0x0000001e: "FILE_DEVICE_STREAMS",
    0x0000001f: "FILE_DEVICE_TAPE",
    0x00000020: "FILE_DEVICE_TAPE_FILE_SYSTEM",
    0x00000021: "FILE_DEVICE_TRANSPORT",
    0x00000022: "FILE_DEVICE_UNKNOWN",
    0x00000023: "FILE_DEVICE_VIDEO",
    0x00000024: "FILE_DEVICE_VIRTUAL_DISK",
    0x00000025: "FILE_DEVICE_WAVE_IN",
    0x00000026: "FILE_DEVICE_WAVE_OUT",
    0x00000027: "FILE_DEVICE_8042_PORT",
    0x00000028: "FILE_DEVICE_NETWORK_REDIRECTOR",
    0x00000029: "FILE_DEVICE_BATTERY",
    0x0000002a: "FILE_DEVICE_BUS_EXTENDER",
    0x0000002b: "FILE_DEVICE_MODEM",
    0x0000002c: "FILE_DEVICE_VDM",
    0x0000002d: "FILE_DEVICE_MASS_STORAGE",
    0x0000002e: "FILE_DEVICE_SMB",
    0x0000002f: "FILE_DEVICE_KS",
    0x00000030: "FILE_DEVICE_CHANGER",
    0x00000031: "FILE_DEVICE_SMARTCARD",
    0x00000032: "FILE_DEVICE_ACPI",
    0x00000033: "FILE_DEVICE_DVD",
    0x00000034: "FILE_DEVICE_FULLSCREEN_VIDEO",
    0x00000035: "FILE_DEVICE_DFS_FILE_SYSTEM",
    0x00000036: "FILE_DEVICE_DFS_VOLUME",
    0x00000037: "FILE_DEVICE_SERENUM",
    0x00000038: "FILE_DEVICE_TERMSRV",
    0x00000039: "FILE_DEVICE_KSEC",
    0x0000003A: "FILE_DEVICE_FIPS",
    0x0000003B: "FILE_DEVICE_INFINIBAND",
    0x0000003E: "FILE_DEVICE_VMBUS",
    0x0000003F: "FILE_DEVICE_CRYPT_PROVIDER",
    0x00000040: "FILE_DEVICE_WPD",
    0x00000041: "FILE_DEVICE_BLUETOOTH",
    0x00000042: "FILE_DEVICE_MT_COMPOSITE",
    0x00000043: "FILE_DEVICE_MT_TRANSPORT",
    0x00000044: "FILE_DEVICE_BIOMETRIC",
    0x00000045: "FILE_DEVICE_PMI",
}
IKE_AUTHENTICATION_METHOD = {
    "IKE_AUTHENTICATION_PRESHARED_KEY_METHOD": 1,
}
IKE_AUTHENTICATION_METHOD_INV = {
    1: "IKE_AUTHENTICATION_PRESHARED_KEY_METHOD",
}
IKE_IDENTIFICATION_PAYLOAD_TYPE = {
    "ID_IPV4_ADDR": 1,
    "ID_FQDN": 2,
    "ID_USER_FQDN": 3,
    "ID_IPV6_ADDR": 5,
}
IKE_IDENTIFICATION_PAYLOAD_TYPE_INV = {
    1: "ID_IPV4_ADDR",
    2: "ID_FQDN",
    3: "ID_USER_FQDN",
    5: "ID_IPV6_ADDR",
}

def iscsidsc_AddISNSServer(jitter, get_str, set_str):
    """
    ISDSC_STATUS AddISNSServer(
        PTCHAR Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddISNSServerA(jitter):
    iscsidsc_AddISNSServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_AddISNSServerW(jitter):
    iscsidsc_AddISNSServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_AddIScsiConnection(jitter, get_str, set_str):
    """
    ISDSC_STATUS AddIScsiConnection(
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId,
        PVOID Reserved,
        ULONG InitiatorPortNumber,
        PISCSI_TARGET_PORTAL TargetPortal,
        ISCSI_SECURITY_FLAGS SecurityFlags,
        PISCSI_LOGIN_OPTIONS LoginOptions,
        ULONG KeySize,
        PCHAR Key,
        PISCSI_UNIQUE_CONNECTION_ID ConnectionId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "Reserved", "InitiatorPortNumber", "TargetPortal", "SecurityFlags", "LoginOptions", "KeySize", "Key", "ConnectionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddIScsiConnectionA(jitter):
    iscsidsc_AddIScsiConnection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_AddIScsiConnectionW(jitter):
    iscsidsc_AddIScsiConnection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_AddIScsiSendTargetPortal(jitter, get_str, set_str):
    """
    ISDSC_STATUS AddIScsiSendTargetPortal(
        PTCHAR InitiatorName,
        ULONG InitiatorPortNumber,
        PISCSI_LOGIN_OPTIONS LoginOptions,
        ISCSI_SECURITY_FLAGS SecurityFlags,
        PISCSI_TARGET_PORTAL Portal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "InitiatorPortNumber", "LoginOptions", "SecurityFlags", "Portal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddIScsiSendTargetPortalA(jitter):
    iscsidsc_AddIScsiSendTargetPortal(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_AddIScsiSendTargetPortalW(jitter):
    iscsidsc_AddIScsiSendTargetPortal(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_AddIScsiStaticTarget(jitter, get_str, set_str):
    """
    ISDSC_STATUS AddIScsiStaticTarget(
        PTCHAR TargetName,
        PTCHAR TargetAlias,
        ISCSI_TARGET_FLAGS TargetFlags,
        BOOLEAN Persist,
        PISCSI_TARGET_MAPPING Mappings,
        PISCSI_LOGIN_OPTIONS LoginOptions,
        PISCSI_TARGET_PORTAL_GROUP PortalGroup
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TargetName", "TargetAlias", "TargetFlags", "Persist", "Mappings", "LoginOptions", "PortalGroup"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddIScsiStaticTargetA(jitter):
    iscsidsc_AddIScsiStaticTarget(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_AddIScsiStaticTargetW(jitter):
    iscsidsc_AddIScsiStaticTarget(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_AddPersistentIScsiDevice(jitter, get_str, set_str):
    """
    ISDSC_STATUS AddPersistentIScsiDevice(
        PTCHAR VolumePath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VolumePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddPersistentIScsiDeviceA(jitter):
    iscsidsc_AddPersistentIScsiDevice(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_AddPersistentIScsiDeviceW(jitter):
    iscsidsc_AddPersistentIScsiDevice(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_AddRadiusServer(jitter, get_str, set_str):
    """
    ISDSC_STATUS AddRadiusServer(
        PWCHAR Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddRadiusServerA(jitter):
    iscsidsc_AddRadiusServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_AddRadiusServerW(jitter):
    iscsidsc_AddRadiusServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ClearPersistentIScsiDevices(jitter):
    """
    ISDSC_STATUS ClearPersistentIScsiDevices()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetDevicesForIScsiSession(jitter, get_str, set_str):
    """
    ISDSC_STATUS GetDevicesForIScsiSession(
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId,
        ULONG* DeviceCount,
        PISCSI_DEVICE_ON_SESSION Devices
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "DeviceCount", "Devices"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetDevicesForIScsiSessionA(jitter):
    iscsidsc_GetDevicesForIScsiSession(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_GetDevicesForIScsiSessionW(jitter):
    iscsidsc_GetDevicesForIScsiSession(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_GetIScsiIKEInfo(jitter, get_str, set_str):
    """
    ISDSC_STATUS GetIScsiIKEInfo(
        PTCHAR InitiatorName,
        ULONG PortNumber,
        PULONG Reserved,
        PIKE_AUTHENTICATION_INFORMATION AuthInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "PortNumber", "Reserved", "AuthInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetIScsiIKEInfoA(jitter):
    iscsidsc_GetIScsiIKEInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_GetIScsiIKEInfoW(jitter):
    iscsidsc_GetIScsiIKEInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_GetIScsiInitiatorNodeName(jitter, get_str, set_str):
    """
    ISDSC_STATUS GetIScsiInitiatorNodeName(
        PTCHAR InitiatorNodeName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorNodeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetIScsiInitiatorNodeNameA(jitter):
    iscsidsc_GetIScsiInitiatorNodeName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_GetIScsiInitiatorNodeNameW(jitter):
    iscsidsc_GetIScsiInitiatorNodeName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_GetIScsiSessionList(jitter, get_str, set_str):
    """
    ISDSC_STATUS GetIScsiSessionList(
        ULONG* BufferSize,
        ULONG* SessionCount,
        PISCSI_SESSION_INFO SessionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferSize", "SessionCount", "SessionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetIScsiSessionListA(jitter):
    iscsidsc_GetIScsiSessionList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_GetIScsiSessionListW(jitter):
    iscsidsc_GetIScsiSessionList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_GetIScsiTargetInformation(jitter, get_str, set_str):
    """
    ISDSC_STATUS GetIScsiTargetInformation(
        PTCHAR TargetName,
        PTCHAR DiscoveryMechanism,
        TARGET_INFORMATION_CLASS InfoClass,
        PULONG BufferSize,
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TargetName", "DiscoveryMechanism", "InfoClass", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetIScsiTargetInformationA(jitter):
    iscsidsc_GetIScsiTargetInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_GetIScsiTargetInformationW(jitter):
    iscsidsc_GetIScsiTargetInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_GetIScsiVersionInformation(jitter):
    """
    ISDSC_STATUS GetIScsiVersionInformation(
        PISCSI_VERSION_INFO VersionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VersionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_LoginIScsiTarget(jitter, get_str, set_str):
    """
    ISDSC_STATUS LoginIScsiTarget(
        PTCHAR TargetName,
        BOOLEAN IsInformationalSession,
        PTCHAR InitiatorName,
        ULONG InitiatorPortNumber,
        PISCSI_TARGET_PORTAL TargetPortal,
        ISCSI_SECURITY_FLAGS SecurityFlags,
        PISCSI_TARGET_MAPPING Mappings,
        PISCSI_LOGIN_OPTIONS LoginOptions,
        ULONG KeySize,
        PCHAR Key,
        BOOLEAN IsPersistent,
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId,
        PISCSI_UNIQUE_CONNECTION_ID UniqueConnectionId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TargetName", "IsInformationalSession", "InitiatorName", "InitiatorPortNumber", "TargetPortal", "SecurityFlags", "Mappings", "LoginOptions", "KeySize", "Key", "IsPersistent", "UniqueSessionId", "UniqueConnectionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_LoginIScsiTargetA(jitter):
    iscsidsc_LoginIScsiTarget(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_LoginIScsiTargetW(jitter):
    iscsidsc_LoginIScsiTarget(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_LogoutIScsiTarget(jitter):
    """
    ISDSC_STATUS LogoutIScsiTarget(
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RefreshISNSServer(jitter, get_str, set_str):
    """
    ISDSC_STATUS RefreshISNSServer(
        PTCHAR Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RefreshISNSServerA(jitter):
    iscsidsc_RefreshISNSServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RefreshISNSServerW(jitter):
    iscsidsc_RefreshISNSServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RefreshIScsiSendTargetPortal(jitter, get_str, set_str):
    """
    ISDSC_STATUS RefreshIScsiSendTargetPortal(
        PTCHAR InitiatorInstance,
        ULONG InitiatorPortNumber,
        PISCSI_TARGET_PORTAL Portal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorInstance", "InitiatorPortNumber", "Portal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RefreshIScsiSendTargetPortalA(jitter):
    iscsidsc_RefreshIScsiSendTargetPortal(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RefreshIScsiSendTargetPortalW(jitter):
    iscsidsc_RefreshIScsiSendTargetPortal(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RemoveISNSServer(jitter, get_str, set_str):
    """
    ISDSC_STATUS RemoveISNSServer(
        PTCHAR Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveISNSServerA(jitter):
    iscsidsc_RemoveISNSServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RemoveISNSServerW(jitter):
    iscsidsc_RemoveISNSServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RemoveIScsiConnection(jitter):
    """
    ISDSC_STATUS RemoveIScsiConnection(
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId,
        PISCSI_UNIQUE_CONNECTION_ID UniqueConnectionId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "UniqueConnectionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveIScsiPersistentTarget(jitter, get_str, set_str):
    """
    ISDSC_STATUS RemoveIScsiPersistentTarget(
        PTCHAR InitiatorInstance,
        ULONG InitiatorPortNumber,
        PTCHAR TargetName,
        PISCSI_TARGET_PORTAL Portal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorInstance", "InitiatorPortNumber", "TargetName", "Portal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveIScsiPersistentTargetA(jitter):
    iscsidsc_RemoveIScsiPersistentTarget(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RemoveIScsiPersistentTargetW(jitter):
    iscsidsc_RemoveIScsiPersistentTarget(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RemoveIScsiSendTargetPortal(jitter, get_str, set_str):
    """
    ISDSC_STATUS RemoveIScsiSendTargetPortal(
        PTCHAR InitiatorInstance,
        ULONG InitiatorPortNumber,
        PISCSI_TARGET_PORTAL Portal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorInstance", "InitiatorPortNumber", "Portal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveIScsiSendTargetPortalA(jitter):
    iscsidsc_RemoveIScsiSendTargetPortal(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RemoveIScsiSendTargetPortalW(jitter):
    iscsidsc_RemoveIScsiSendTargetPortal(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RemoveIScsiStaticTarget(jitter, get_str, set_str):
    """
    ISDSC_STATUS RemoveIScsiStaticTarget(
        PTCHAR TargetName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TargetName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveIScsiStaticTargetA(jitter):
    iscsidsc_RemoveIScsiStaticTarget(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RemoveIScsiStaticTargetW(jitter):
    iscsidsc_RemoveIScsiStaticTarget(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RemovePersistentIScsiDevice(jitter, get_str, set_str):
    """
    ISDSC_STATUS RemovePersistentIScsiDevice(
        PTCHAR VolumePath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VolumePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemovePersistentIScsiDeviceA(jitter):
    iscsidsc_RemovePersistentIScsiDevice(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RemovePersistentIScsiDeviceW(jitter):
    iscsidsc_RemovePersistentIScsiDevice(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RemoveRadiusServer(jitter, get_str, set_str):
    """
    ISDSC_STATUS RemoveRadiusServer(
        PTCHAR Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveRadiusServerA(jitter):
    iscsidsc_RemoveRadiusServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RemoveRadiusServerW(jitter):
    iscsidsc_RemoveRadiusServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportActiveIScsiTargetMappings(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportActiveIScsiTargetMappings(
        PULONG BufferSize,
        PULONG MappingCount,
        PISCSI_TARGET_MAPPING Mappings
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferSize", "MappingCount", "Mappings"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportActiveIScsiTargetMappingsA(jitter):
    iscsidsc_ReportActiveIScsiTargetMappings(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportActiveIScsiTargetMappingsW(jitter):
    iscsidsc_ReportActiveIScsiTargetMappings(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportISNSServerList(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportISNSServerList(
        PULONG BufferSizeInChar,
        PTCHAR Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferSizeInChar", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportISNSServerListA(jitter):
    iscsidsc_ReportISNSServerList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportISNSServerListW(jitter):
    iscsidsc_ReportISNSServerList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportIScsiInitiatorList(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportIScsiInitiatorList(
        ULONG* BufferSize,
        PTCHAR Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiInitiatorListA(jitter):
    iscsidsc_ReportIScsiInitiatorList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportIScsiInitiatorListW(jitter):
    iscsidsc_ReportIScsiInitiatorList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportIScsiPersistentLogins(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportIScsiPersistentLogins(
        ULONG* Count,
        PPERSISTENT_ISCSI_LOGIN_INFO PersistentLoginInfo,
        PULONG BufferSizeInBytes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Count", "PersistentLoginInfo", "BufferSizeInBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiPersistentLoginsA(jitter):
    iscsidsc_ReportIScsiPersistentLogins(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportIScsiPersistentLoginsW(jitter):
    iscsidsc_ReportIScsiPersistentLogins(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportIScsiSendTargetPortals(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportIScsiSendTargetPortals(
        PULONG PortalCount,
        PISCSI_TARGET_PORTAL_INFO PortalInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortalCount", "PortalInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiSendTargetPortalsA(jitter):
    iscsidsc_ReportIScsiSendTargetPortals(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportIScsiSendTargetPortalsW(jitter):
    iscsidsc_ReportIScsiSendTargetPortals(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportIScsiSendTargetPortalsEx(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportIScsiSendTargetPortalsEx(
        PULONG PortalCount,
        PULONG PortalInfoSize,
        PISCSI_TARGET_PORTAL_INFO_EX PortalInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortalCount", "PortalInfoSize", "PortalInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiSendTargetPortalsExA(jitter):
    iscsidsc_ReportIScsiSendTargetPortalsEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportIScsiSendTargetPortalsExW(jitter):
    iscsidsc_ReportIScsiSendTargetPortalsEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportIScsiTargets(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportIScsiTargets(
        BOOLEAN ForceUpdate,
        PULONG BufferSize,
        PTCHAR Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ForceUpdate", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiTargetsA(jitter):
    iscsidsc_ReportIScsiTargets(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportIScsiTargetsW(jitter):
    iscsidsc_ReportIScsiTargets(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportIScsiTargetPortals(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportIScsiTargetPortals(
        PWCHAR InitiatorName,
        PWCHAR TargetName,
        PUSHORT TargetPortalTag,
        PULONG ElementCount,
        PISCSI_TARGET_PORTAL Portals
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "TargetName", "TargetPortalTag", "ElementCount", "Portals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiTargetPortalsA(jitter):
    iscsidsc_ReportIScsiTargetPortals(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportIScsiTargetPortalsW(jitter):
    iscsidsc_ReportIScsiTargetPortals(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportPersistentIScsiDevices(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportPersistentIScsiDevices(
        PULONG BufferSizeInChar,
        PTCHAR Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferSizeInChar", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportPersistentIScsiDevicesA(jitter):
    iscsidsc_ReportPersistentIScsiDevices(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportPersistentIScsiDevicesW(jitter):
    iscsidsc_ReportPersistentIScsiDevices(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportRadiusServerList(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportRadiusServerList(
        PULONG BufferSizeInChar,
        PTCHAR Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferSizeInChar", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportRadiusServerListA(jitter):
    iscsidsc_ReportRadiusServerList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportRadiusServerListW(jitter):
    iscsidsc_ReportRadiusServerList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_SendScsiInquiry(jitter):
    """
    ISDSC_STATUS SendScsiInquiry(
        PISCSI_UNIQUE_SESSION_ID* UniqueSessionId,
        ULONGLONG Lun,
        UCHAR EvpdCmddt,
        UCHAR PageCode,
        PUCHAR* ScsiStatus,
        PULONG* ReponseSize,
        PUCHAR ReponseBuffer,
        PULONG* SenseSize,
        PUCHAR SenseBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "Lun", "EvpdCmddt", "PageCode", "ScsiStatus", "ReponseSize", "ReponseBuffer", "SenseSize", "SenseBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SendScsiReadCapacity(jitter):
    """
    ISDSC_STATUS SendScsiReadCapacity(
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId,
        ULONGLONG Lun,
        PUCHAR* ScsiStatus,
        PULONG* ResponseSize,
        PUCHAR ResponseBuffer,
        PULONG* SenseSize,
        PUCHAR SenseBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "Lun", "ScsiStatus", "ResponseSize", "ResponseBuffer", "SenseSize", "SenseBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SendScsiReportLuns(jitter):
    """
    ISDSC_STATUS SendScsiReportLuns(
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId,
        PUCHAR* ScsiStatus,
        PULONG* ResponseSize,
        PUCHAR ResponseBuffer,
        PULONG* SenseSize,
        PUCHAR SenseBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "ScsiStatus", "ResponseSize", "ResponseBuffer", "SenseSize", "SenseBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiGroupPresharedKey(jitter):
    """
    ISDSC_STATUS SetIScsiGroupPresharedKey(
        ULONG KeyLength,
        PUCHAR Key,
        BOOLEAN Persist
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyLength", "Key", "Persist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiIKEInfo(jitter, get_str, set_str):
    """
    ISDSC_STATUS SetIScsiIKEInfo(
        PTCHAR InitiatorName,
        ULONG PortNumber,
        PIKE_AUTHENTICATION_INFORMATION AuthInfo,
        BOOLEAN Persist
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "PortNumber", "AuthInfo", "Persist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiIKEInfoA(jitter):
    iscsidsc_SetIScsiIKEInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_SetIScsiIKEInfoW(jitter):
    iscsidsc_SetIScsiIKEInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_SetIScsiInitiatorCHAPSharedSecret(jitter):
    """
    ISDSC_STATUS SetIScsiInitiatorCHAPSharedSecret(
        ULONG SharedSecretLength,
        PUCHAR SharedSecret
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SharedSecretLength", "SharedSecret"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiInitiatorRADIUSSharedSecret(jitter):
    """
    ISDSC_STATUS SetIScsiInitiatorRADIUSSharedSecret(
        ULONG SharedSecretLength,
        PUCHAR SharedSecret
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SharedSecretLength", "SharedSecret"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiInitiatorNodeName(jitter, get_str, set_str):
    """
    ISDSC_STATUS SetIScsiInitiatorNodeName(
        PTCHAR InitiatorNodeName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorNodeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiInitiatorNodeNameA(jitter):
    iscsidsc_SetIScsiInitiatorNodeName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_SetIScsiInitiatorNodeNameW(jitter):
    iscsidsc_SetIScsiInitiatorNodeName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_SetIScsiTunnelModeOuterAddress(jitter, get_str, set_str):
    """
    ISDSC_STATUS SetIScsiTunnelModeOuterAddress(
        PTCHAR InitiatorName,
        ULONG InitiatorPortNumber,
        PTCHAR DestinationAddress,
        PTCHAR OuterModeAddress,
        BOOLEAN Persist
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "InitiatorPortNumber", "DestinationAddress", "OuterModeAddress", "Persist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiTunnelModeOuterAddressA(jitter):
    iscsidsc_SetIScsiTunnelModeOuterAddress(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_SetIScsiTunnelModeOuterAddressW(jitter):
    iscsidsc_SetIScsiTunnelModeOuterAddress(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_SetupPersistentIScsiDevices(jitter):
    """
    ISDSC_STATUS SetupPersistentIScsiDevices()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
