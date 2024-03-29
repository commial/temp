###### Enums ######
CONFIGRET = {
    "CR_SUCCESS": 0x00000000,
    "CR_DEFAULT": 0x00000001,
    "CR_OUT_OF_MEMORY": 0x00000002,
    "CR_INVALID_POINTER": 0x00000003,
    "CR_INVALID_FLAG": 0x00000004,
    "CR_INVALID_DEVNODE": 0x00000005,
    "CR_INVALID_RES_DES": 0x00000006,
    "CR_INVALID_LOG_CONF": 0x00000007,
    "CR_INVALID_ARBITRATOR": 0x00000008,
    "CR_INVALID_NODELIST": 0x00000009,
    "CR_DEVNODE_HAS_REQS": 0x0000000A,
    "CR_INVALID_RESOURCEID": 0x0000000B,
    "CR_DLVXD_NOT_FOUND": 0x0000000C,
    "CR_NO_SUCH_DEVNODE": 0x0000000D,
    "CR_NO_MORE_LOG_CONF": 0x0000000E,
    "CR_NO_MORE_RES_DES": 0x0000000F,
    "CR_ALREADY_SUCH_DEVNODE": 0x00000010,
    "CR_INVALID_RANGE_LIST": 0x00000011,
    "CR_INVALID_RANGE": 0x00000012,
    "CR_FAILURE": 0x00000013,
    "CR_NO_SUCH_LOGICAL_DEV": 0x00000014,
    "CR_CREATE_BLOCKED": 0x00000015,
    "CR_NOT_SYSTEM_VM": 0x00000016,
    "CR_REMOVE_VETOED": 0x00000017,
    "CR_APM_VETOED": 0x00000018,
    "CR_INVALID_LOAD_TYPE": 0x00000019,
    "CR_BUFFER_SMALL": 0x0000001A,
    "CR_NO_ARBITRATOR": 0x0000001B,
    "CR_NO_REGISTRY_HANDLE": 0x0000001C,
    "CR_REGISTRY_ERROR": 0x0000001D,
    "CR_INVALID_DEVICE_ID": 0x0000001E,
    "CR_INVALID_DATA": 0x0000001F,
    "CR_INVALID_API": 0x00000020,
    "CR_DEVLOADER_NOT_READY": 0x00000021,
    "CR_NEED_RESTART": 0x00000022,
    "CR_NO_MORE_HW_PROFILES": 0x00000023,
    "CR_DEVICE_NOT_THERE": 0x00000024,
    "CR_NO_SUCH_VALUE": 0x00000025,
    "CR_WRONG_TYPE": 0x00000026,
    "CR_INVALID_PRIORITY": 0x00000027,
    "CR_NOT_DISABLEABLE": 0x00000028,
    "CR_FREE_RESOURCES": 0x00000029,
    "CR_QUERY_VETOED": 0x0000002A,
    "CR_CANT_SHARE_IRQ": 0x0000002B,
    "CR_NO_DEPENDENT": 0x0000002C,
    "CR_SAME_RESOURCES": 0x0000002D,
    "CR_NO_SUCH_REGISTRY_KEY": 0x0000002E,
    "CR_INVALID_MACHINENAME": 0x0000002F,
    "CR_REMOTE_COMM_FAILURE": 0x00000030,
    "CR_MACHINE_UNAVAILABLE": 0x00000031,
    "CR_NO_CM_SERVICES": 0x00000032,
    "CR_ACCESS_DENIED": 0x00000033,
    "CR_CALL_NOT_IMPLEMENTED": 0x00000034,
    "CR_INVALID_PROPERTY": 0x00000035,
    "CR_DEVICE_INTERFACE_ACTIVE": 0x00000036,
    "CR_NO_SUCH_DEVICE_INTERFACE": 0x00000037,
    "CR_INVALID_REFERENCE_STRING": 0x00000038,
    "CR_INVALID_CONFLICT_LIST": 0x00000039,
    "CR_INVALID_INDEX": 0x0000003A,
    "CR_INVALID_STRUCTURE_SIZE": 0x0000003B,
}
CONFIGRET_INV = {
    0x00000000: "CR_SUCCESS",
    0x00000001: "CR_DEFAULT",
    0x00000002: "CR_OUT_OF_MEMORY",
    0x00000003: "CR_INVALID_POINTER",
    0x00000004: "CR_INVALID_FLAG",
    0x00000005: "CR_INVALID_DEVNODE",
    0x00000006: "CR_INVALID_RES_DES",
    0x00000007: "CR_INVALID_LOG_CONF",
    0x00000008: "CR_INVALID_ARBITRATOR",
    0x00000009: "CR_INVALID_NODELIST",
    0x0000000A: "CR_DEVNODE_HAS_REQS",
    0x0000000B: "CR_INVALID_RESOURCEID",
    0x0000000C: "CR_DLVXD_NOT_FOUND",
    0x0000000D: "CR_NO_SUCH_DEVNODE",
    0x0000000E: "CR_NO_MORE_LOG_CONF",
    0x0000000F: "CR_NO_MORE_RES_DES",
    0x00000010: "CR_ALREADY_SUCH_DEVNODE",
    0x00000011: "CR_INVALID_RANGE_LIST",
    0x00000012: "CR_INVALID_RANGE",
    0x00000013: "CR_FAILURE",
    0x00000014: "CR_NO_SUCH_LOGICAL_DEV",
    0x00000015: "CR_CREATE_BLOCKED",
    0x00000016: "CR_NOT_SYSTEM_VM",
    0x00000017: "CR_REMOVE_VETOED",
    0x00000018: "CR_APM_VETOED",
    0x00000019: "CR_INVALID_LOAD_TYPE",
    0x0000001A: "CR_BUFFER_SMALL",
    0x0000001B: "CR_NO_ARBITRATOR",
    0x0000001C: "CR_NO_REGISTRY_HANDLE",
    0x0000001D: "CR_REGISTRY_ERROR",
    0x0000001E: "CR_INVALID_DEVICE_ID",
    0x0000001F: "CR_INVALID_DATA",
    0x00000020: "CR_INVALID_API",
    0x00000021: "CR_DEVLOADER_NOT_READY",
    0x00000022: "CR_NEED_RESTART",
    0x00000023: "CR_NO_MORE_HW_PROFILES",
    0x00000024: "CR_DEVICE_NOT_THERE",
    0x00000025: "CR_NO_SUCH_VALUE",
    0x00000026: "CR_WRONG_TYPE",
    0x00000027: "CR_INVALID_PRIORITY",
    0x00000028: "CR_NOT_DISABLEABLE",
    0x00000029: "CR_FREE_RESOURCES",
    0x0000002A: "CR_QUERY_VETOED",
    0x0000002B: "CR_CANT_SHARE_IRQ",
    0x0000002C: "CR_NO_DEPENDENT",
    0x0000002D: "CR_SAME_RESOURCES",
    0x0000002E: "CR_NO_SUCH_REGISTRY_KEY",
    0x0000002F: "CR_INVALID_MACHINENAME",
    0x00000030: "CR_REMOTE_COMM_FAILURE",
    0x00000031: "CR_MACHINE_UNAVAILABLE",
    0x00000032: "CR_NO_CM_SERVICES",
    0x00000033: "CR_ACCESS_DENIED",
    0x00000034: "CR_CALL_NOT_IMPLEMENTED",
    0x00000035: "CR_INVALID_PROPERTY",
    0x00000036: "CR_DEVICE_INTERFACE_ACTIVE",
    0x00000037: "CR_NO_SUCH_DEVICE_INTERFACE",
    0x00000038: "CR_INVALID_REFERENCE_STRING",
    0x00000039: "CR_INVALID_CONFLICT_LIST",
    0x0000003A: "CR_INVALID_INDEX",
    0x0000003B: "CR_INVALID_STRUCTURE_SIZE",
}
_LogicalConfigFlags_ = {
    "BASIC_LOG_CONF": 0x00000000,
    "FILTERED_LOG_CONF": 0x00000001,
    "ALLOC_LOG_CONF": 0x00000002,
    "BOOT_LOG_CONF": 0x00000003,
    "FORCED_LOG_CONF": 0x00000004,
    "OVERRIDE_LOG_CONF": 0x00000005,
    "PRIORITY_EQUAL_FIRST": 0x00000008,
}
_LogicalConfigFlags__INV = {
    0x00000000: "BASIC_LOG_CONF",
    0x00000001: "FILTERED_LOG_CONF",
    0x00000002: "ALLOC_LOG_CONF",
    0x00000003: "BOOT_LOG_CONF",
    0x00000004: "FORCED_LOG_CONF",
    0x00000005: "OVERRIDE_LOG_CONF",
    0x00000008: "PRIORITY_EQUAL_FIRST",
}
_CmProblemNumber_ = {
    "CM_PROB_NOT_CONFIGURED": 0x00000001,
    "CM_PROB_DEVLOADER_FAILED": 0x00000002,
    "CM_PROB_OUT_OF_MEMORY": 0x00000003,
    "CM_PROB_ENTRY_IS_WRONG_TYPE": 0x00000004,
    "CM_PROB_LACKED_ARBITRATOR": 0x00000005,
    "CM_PROB_BOOT_CONFIG_CONFLICT": 0x00000006,
    "CM_PROB_FAILED_FILTER": 0x00000007,
    "CM_PROB_DEVLOADER_NOT_FOUND": 0x00000008,
    "CM_PROB_INVALID_DATA": 0x00000009,
    "CM_PROB_FAILED_START": 0x0000000A,
    "CM_PROB_LIAR": 0x0000000B,
    "CM_PROB_NORMAL_CONFLICT": 0x0000000C,
    "CM_PROB_NOT_VERIFIED": 0x0000000D,
    "CM_PROB_NEED_RESTART": 0x0000000E,
    "CM_PROB_REENUMERATION": 0x0000000F,
    "CM_PROB_PARTIAL_LOG_CONF": 0x00000010,
    "CM_PROB_UNKNOWN_RESOURCE": 0x00000011,
    "CM_PROB_REINSTALL": 0x00000012,
    "CM_PROB_REGISTRY": 0x00000013,
    "CM_PROB_VXDLDR": 0x00000014,
    "CM_PROB_WILL_BE_REMOVED": 0x00000015,
    "CM_PROB_DISABLED": 0x00000016,
    "CM_PROB_DEVLOADER_NOT_READY": 0x00000017,
    "CM_PROB_DEVICE_NOT_THERE": 0x00000018,
    "CM_PROB_MOVED": 0x00000019,
    "CM_PROB_TOO_EARLY": 0x0000001A,
    "CM_PROB_NO_VALID_LOG_CONF": 0x0000001B,
    "CM_PROB_FAILED_INSTALL": 0x0000001C,
    "CM_PROB_HARDWARE_DISABLED": 0x0000001D,
    "CM_PROB_CANT_SHARE_IRQ": 0x0000001E,
    "CM_PROB_FAILED_ADD": 0x0000001F,
    "CM_PROB_DISABLED_SERVICE": 0x00000020,
    "CM_PROB_TRANSLATION_FAILED": 0x00000021,
    "CM_PROB_NO_SOFTCONFIG": 0x00000022,
    "CM_PROB_BIOS_TABLE": 0x00000023,
    "CM_PROB_IRQ_TRANSLATION_FAILED": 0x00000024,
    "CM_PROB_FAILED_DRIVER_ENTRY": 0x00000025,
    "CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD": 0x00000026,
    "CM_PROB_DRIVER_FAILED_LOAD": 0x00000027,
    "CM_PROB_DRIVER_SERVICE_KEY_INVALID": 0x00000028,
    "CM_PROB_LEGACY_SERVICE_NO_DEVICES": 0x00000029,
    "CM_PROB_DUPLICATE_DEVICE": 0x0000002A,
    "CM_PROB_FAILED_POST_START": 0x0000002B,
    "CM_PROB_HALTED": 0x0000002C,
    "CM_PROB_PHANTOM": 0x0000002D,
    "CM_PROB_SYSTEM_SHUTDOWN": 0x0000002E,
    "CM_PROB_HELD_FOR_EJECT": 0x0000002F,
    "CM_PROB_DRIVER_BLOCKED": 0x00000030,
    "CM_PROB_REGISTRY_TOO_LARGE": 0x00000031,
    "CM_PROB_SETPROPERTIES_FAILED": 0x00000032,
    "CM_PROB_WAITING_ON_DEPENDENCY": 0x00000033,
    "CM_PROB_UNSIGNED_DRIVER": 0x00000034,
}
_CmProblemNumber__INV = {
    0x00000001: "CM_PROB_NOT_CONFIGURED",
    0x00000002: "CM_PROB_DEVLOADER_FAILED",
    0x00000003: "CM_PROB_OUT_OF_MEMORY",
    0x00000004: "CM_PROB_ENTRY_IS_WRONG_TYPE",
    0x00000005: "CM_PROB_LACKED_ARBITRATOR",
    0x00000006: "CM_PROB_BOOT_CONFIG_CONFLICT",
    0x00000007: "CM_PROB_FAILED_FILTER",
    0x00000008: "CM_PROB_DEVLOADER_NOT_FOUND",
    0x00000009: "CM_PROB_INVALID_DATA",
    0x0000000A: "CM_PROB_FAILED_START",
    0x0000000B: "CM_PROB_LIAR",
    0x0000000C: "CM_PROB_NORMAL_CONFLICT",
    0x0000000D: "CM_PROB_NOT_VERIFIED",
    0x0000000E: "CM_PROB_NEED_RESTART",
    0x0000000F: "CM_PROB_REENUMERATION",
    0x00000010: "CM_PROB_PARTIAL_LOG_CONF",
    0x00000011: "CM_PROB_UNKNOWN_RESOURCE",
    0x00000012: "CM_PROB_REINSTALL",
    0x00000013: "CM_PROB_REGISTRY",
    0x00000014: "CM_PROB_VXDLDR",
    0x00000015: "CM_PROB_WILL_BE_REMOVED",
    0x00000016: "CM_PROB_DISABLED",
    0x00000017: "CM_PROB_DEVLOADER_NOT_READY",
    0x00000018: "CM_PROB_DEVICE_NOT_THERE",
    0x00000019: "CM_PROB_MOVED",
    0x0000001A: "CM_PROB_TOO_EARLY",
    0x0000001B: "CM_PROB_NO_VALID_LOG_CONF",
    0x0000001C: "CM_PROB_FAILED_INSTALL",
    0x0000001D: "CM_PROB_HARDWARE_DISABLED",
    0x0000001E: "CM_PROB_CANT_SHARE_IRQ",
    0x0000001F: "CM_PROB_FAILED_ADD",
    0x00000020: "CM_PROB_DISABLED_SERVICE",
    0x00000021: "CM_PROB_TRANSLATION_FAILED",
    0x00000022: "CM_PROB_NO_SOFTCONFIG",
    0x00000023: "CM_PROB_BIOS_TABLE",
    0x00000024: "CM_PROB_IRQ_TRANSLATION_FAILED",
    0x00000025: "CM_PROB_FAILED_DRIVER_ENTRY",
    0x00000026: "CM_PROB_DRIVER_FAILED_PRIOR_UNLOAD",
    0x00000027: "CM_PROB_DRIVER_FAILED_LOAD",
    0x00000028: "CM_PROB_DRIVER_SERVICE_KEY_INVALID",
    0x00000029: "CM_PROB_LEGACY_SERVICE_NO_DEVICES",
    0x0000002A: "CM_PROB_DUPLICATE_DEVICE",
    0x0000002B: "CM_PROB_FAILED_POST_START",
    0x0000002C: "CM_PROB_HALTED",
    0x0000002D: "CM_PROB_PHANTOM",
    0x0000002E: "CM_PROB_SYSTEM_SHUTDOWN",
    0x0000002F: "CM_PROB_HELD_FOR_EJECT",
    0x00000030: "CM_PROB_DRIVER_BLOCKED",
    0x00000031: "CM_PROB_REGISTRY_TOO_LARGE",
    0x00000032: "CM_PROB_SETPROPERTIES_FAILED",
    0x00000033: "CM_PROB_WAITING_ON_DEPENDENCY",
    0x00000034: "CM_PROB_UNSIGNED_DRIVER",
}
PPNP_VETO_TYPE = {
    "PNP_VetoTypeUnknown": 0,
    "PNP_VetoLegacyDevice": 1,
    "PNP_VetoPendingClose": 2,
    "PNP_VetoWindowsApp": 3,
    "PNP_VetoWindowsService": 4,
    "PNP_VetoOutstandingOpen": 5,
    "PNP_VetoDevice": 6,
    "PNP_VetoDriver": 7,
    "PNP_VetoIllegalDeviceRequest": 8,
    "PNP_VetoInsufficientPower": 9,
    "PNP_VetoNonDisableable": 10,
    "PNP_VetoLegacyDriver": 11,
    "PNP_VetoInsufficientRights": 12,
}
PPNP_VETO_TYPE_INV = {
    0: "PNP_VetoTypeUnknown",
    1: "PNP_VetoLegacyDevice",
    2: "PNP_VetoPendingClose",
    3: "PNP_VetoWindowsApp",
    4: "PNP_VetoWindowsService",
    5: "PNP_VetoOutstandingOpen",
    6: "PNP_VetoDevice",
    7: "PNP_VetoDriver",
    8: "PNP_VetoIllegalDeviceRequest",
    9: "PNP_VetoInsufficientPower",
    10: "PNP_VetoNonDisableable",
    11: "PNP_VetoLegacyDriver",
    12: "PNP_VetoInsufficientRights",
}
_CM_DRP_ = {
    "CM_DRP_DEVICEDESC": 0x00000001,
    "CM_DRP_HARDWAREID": 0x00000002,
    "CM_DRP_COMPATIBLEIDS": 0x00000003,
    "CM_DRP_UNUSED0": 0x00000004,
    "CM_DRP_SERVICE": 0x00000005,
    "CM_DRP_UNUSED1": 0x00000006,
    "CM_DRP_UNUSED2": 0x00000007,
    "CM_DRP_CLASS": 0x00000008,
    "CM_DRP_CLASSGUID": 0x00000009,
    "CM_DRP_DRIVER": 0x0000000A,
    "CM_DRP_CONFIGFLAGS": 0x0000000B,
    "CM_DRP_MFG": 0x0000000C,
    "CM_DRP_FRIENDLYNAME": 0x0000000D,
    "CM_DRP_LOCATION_INFORMATION": 0x0000000E,
    "CM_DRP_PHYSICAL_DEVICE_OBJECT_NAME": 0x0000000F,
    "CM_DRP_CAPABILITIES": 0x00000010,
    "CM_DRP_UI_NUMBER": 0x00000011,
    "CM_DRP_UPPERFILTERS": 0x00000012,
    "CM_DRP_LOWERFILTERS": 0x00000013,
    "CM_DRP_BUSTYPEGUID": 0x00000014,
    "CM_DRP_LEGACYBUSTYPE": 0x00000015,
    "CM_DRP_BUSNUMBER": 0x00000016,
    "CM_DRP_ENUMERATOR_NAME": 0x00000017,
    "CM_DRP_SECURITY": 0x00000018,
    "CM_DRP_SECURITY_SDS": 0x00000019,
    "CM_DRP_DEVTYPE": 0x0000001A,
    "CM_DRP_EXCLUSIVE": 0x0000001B,
    "CM_DRP_CHARACTERISTICS": 0x0000001C,
    "CM_DRP_ADDRESS": 0x0000001D,
    "CM_DRP_UI_NUMBER_DESC_FORMAT": 0x0000001E,
    "CM_DRP_DEVICE_POWER_DATA": 0x0000001F,
    "CM_DRP_REMOVAL_POLICY": 0x00000020,
    "CM_DRP_REMOVAL_POLICY_HW_DEFAULT": 0x00000021,
    "CM_DRP_REMOVAL_POLICY_OVERRIDE": 0x00000022,
    "CM_DRP_INSTALL_STATE": 0x00000023,
    "CM_DRP_LOCATION_PATHS": 0x00000024,
    "CM_DRP_BASE_CONTAINERID": 0x00000025,
}
_CM_DRP__INV = {
    0x00000001: "CM_DRP_DEVICEDESC",
    0x00000002: "CM_DRP_HARDWAREID",
    0x00000003: "CM_DRP_COMPATIBLEIDS",
    0x00000004: "CM_DRP_UNUSED0",
    0x00000005: "CM_DRP_SERVICE",
    0x00000006: "CM_DRP_UNUSED1",
    0x00000007: "CM_DRP_UNUSED2",
    0x00000008: "CM_DRP_CLASS",
    0x00000009: "CM_DRP_CLASSGUID",
    0x0000000A: "CM_DRP_DRIVER",
    0x0000000B: "CM_DRP_CONFIGFLAGS",
    0x0000000C: "CM_DRP_MFG",
    0x0000000D: "CM_DRP_FRIENDLYNAME",
    0x0000000E: "CM_DRP_LOCATION_INFORMATION",
    0x0000000F: "CM_DRP_PHYSICAL_DEVICE_OBJECT_NAME",
    0x00000010: "CM_DRP_CAPABILITIES",
    0x00000011: "CM_DRP_UI_NUMBER",
    0x00000012: "CM_DRP_UPPERFILTERS",
    0x00000013: "CM_DRP_LOWERFILTERS",
    0x00000014: "CM_DRP_BUSTYPEGUID",
    0x00000015: "CM_DRP_LEGACYBUSTYPE",
    0x00000016: "CM_DRP_BUSNUMBER",
    0x00000017: "CM_DRP_ENUMERATOR_NAME",
    0x00000018: "CM_DRP_SECURITY",
    0x00000019: "CM_DRP_SECURITY_SDS",
    0x0000001A: "CM_DRP_DEVTYPE",
    0x0000001B: "CM_DRP_EXCLUSIVE",
    0x0000001C: "CM_DRP_CHARACTERISTICS",
    0x0000001D: "CM_DRP_ADDRESS",
    0x0000001E: "CM_DRP_UI_NUMBER_DESC_FORMAT",
    0x0000001F: "CM_DRP_DEVICE_POWER_DATA",
    0x00000020: "CM_DRP_REMOVAL_POLICY",
    0x00000021: "CM_DRP_REMOVAL_POLICY_HW_DEFAULT",
    0x00000022: "CM_DRP_REMOVAL_POLICY_OVERRIDE",
    0x00000023: "CM_DRP_INSTALL_STATE",
    0x00000024: "CM_DRP_LOCATION_PATHS",
    0x00000025: "CM_DRP_BASE_CONTAINERID",
}
_CM_CRP_ = {
    "CM_CRP_UPPERFILTERS": 0x00000012,
    "CM_CRP_LOWERFILTERS": 0x00000013,
    "CM_CRP_SECURITY": 0x00000018,
    "CM_CRP_SECURITY_SDS": 0x00000019,
    "CM_CRP_DEVTYPE": 0x0000001A,
    "CM_CRP_EXCLUSIVE": 0x0000001B,
    "CM_CRP_CHARACTERISTICS": 0x0000001C,
}
_CM_CRP__INV = {
    0x00000012: "CM_CRP_UPPERFILTERS",
    0x00000013: "CM_CRP_LOWERFILTERS",
    0x00000018: "CM_CRP_SECURITY",
    0x00000019: "CM_CRP_SECURITY_SDS",
    0x0000001A: "CM_CRP_DEVTYPE",
    0x0000001B: "CM_CRP_EXCLUSIVE",
    0x0000001C: "CM_CRP_CHARACTERISTICS",
}
REGDISPOSITION = {
    "RegDisposition_OpenAlways": 0x00000000,
    "RegDisposition_OpenExisting": 0x00000001,
}
REGDISPOSITION_INV = {
    0x00000000: "RegDisposition_OpenAlways",
    0x00000001: "RegDisposition_OpenExisting",
}
CM_NOTIFY_FILTER_TYPE = {
    "CM_NOTIFY_FILTER_TYPE_DEVICEINTERFACE": 0,
    "CM_NOTIFY_FILTER_TYPE_DEVICEHANDLE": 1,
    "CM_NOTIFY_FILTER_TYPE_DEVICEINSTANCE": 2,
}
CM_NOTIFY_FILTER_TYPE_INV = {
    0: "CM_NOTIFY_FILTER_TYPE_DEVICEINTERFACE",
    1: "CM_NOTIFY_FILTER_TYPE_DEVICEHANDLE",
    2: "CM_NOTIFY_FILTER_TYPE_DEVICEINSTANCE",
}

###################

###### Types ######
DEVINSTID = TCHAR_PTR
LOG_CONF = DWORD_PTR
PLOG_CONF = Ptr("<I", LOG_CONF())
DEVINST = DWORD
PDEVINST = Ptr("<I", DWORD())
RES_DES = DWORD_PTR
PRES_DES = Ptr("<I", RES_DES())
HMACHINE = HANDLE
PHMACHINE = Ptr("<I", HMACHINE())
CONFLICT_LIST = ULONG_PTR
PCONFLICT_LIST = Ptr("<I", CONFLICT_LIST())
RANGE_LIST = DWORD_PTR
PRANGE_LIST = Ptr("<I", RANGE_LIST())
DEVNODE = DWORD
RANGE_ELEMENT = DWORD_PTR
PRANGE_ELEMENT = Ptr("<I", RANGE_ELEMENT())
PCM_NOTIFY_CALLBACK = LPVOID
HCMNOTIFICATION = HANDLE
PHCMNOTIFICATION = Ptr("<I", HCMNOTIFICATION())
WCHAR__MAX_DEVICE_ID_LEN_ = Array(WCHAR, 200)
PRIORITY = ULONG
PPRIORITY = Ptr("<I", PRIORITY())
RESOURCEID = ULONG
PRESOURCEID = Ptr("<I", RESOURCEID())
CONFIGRET = DWORD
_CM_CDMASK_ = ULONG
_CM_CDFLAGS_ = ULONG

class CONFLICT_DETAILS(MemStruct):
    fields = [
        ("CD_ulSize", ULONG()),
        ("CD_ulMask", _CM_CDMASK_()),
        ("CD_dnDevInst", DEVINST()),
        ("CD_rdResDes", RES_DES()),
        ("CD_ulFlags", _CM_CDFLAGS_()),
        ("CD_szDescription", TCHAR__MAX_PATH_()),
    ]

PCONFLICT_DETAILS = Ptr("<I", CONFLICT_DETAILS())
_CM_Locate_DevNode_Flags_ = ULONG
_CsConfigFlags_ = ULONG
_CsConfigFlags_PTR_ = Ptr("<I", _CsConfigFlags_())
_LogicalConfigFlags_ = ULONG
_CmProblemNumber_ = ULONG
_CmProblemNumber_PTR_ = Ptr("<I", _CmProblemNumber_())
PPNP_VETO_TYPE = UINT
_CM_ADD_RANGE_FLAGS_ = ULONG
_CM_ADD_ID_FLAGS_ = ULONG
_CM_ENUMERATE_CLASSES_FLAGS_ = ULONG
_CM_DRP_ = ULONG
_CM_CRP_ = ULONG
_CM_GETIDLIST_FLAGS_ = ULONG
_CM_GET_DEVICE_INTERFACE_LIST_FLAGS_ = ULONG
_CM_REENUMERATE_FLAGS_ = ULONG
_CM_SET_DEVNODE_PROBLEM_FLAGS_ = ULONG
_CM_SETUP_DEVNODE_FLAGS_ = ULONG
_CM_CREATE_DEVNODE_FLAGS_ = ULONG
_CM_DELETE_CLASS_FLAGS_ = ULONG
_CM_DISABLE_FLAGS_ = ULONG
_CM_CLASS_PROPERTY_FLAGS_ = ULONG
_CM_CUSTOMDEVPROP_FLAGS_ = ULONG
REGDISPOSITION = UINT
_CM_OPEN_CLASS_KEY_FLAGS_ = ULONG
_CM_REGISTRY_FLAGS_ = ULONG
_CM_QUERY_ARBITRATOR_FLAGS_ = ULONG
_CM_REGISTER_DEVICE_DRIVER_FLAGS_ = ULONG
_CM_DETECT_FLAGS_ = ULONG
_CM_SET_HW_PROF_FLAGS_ = ULONG
_CM_REMOVE_FLAGS_ = ULONG
_CM_HWPI_FLAGS_ = DWORD

class HWPROFILEINFO(MemStruct):
    fields = [
        ("HWPI_ulHWProfile", ULONG()),
        ("HWPI_szFriendlyName", TCHAR__MAX_PROFILE_LEN_()),
        ("HWPI_dwFlags", _CM_HWPI_FLAGS_()),
    ]

PHWPROFILEINFO = Ptr("<I", HWPROFILEINFO())
CM_NOTIFY_FILTER_TYPE = UINT
_CM_NOTIFY_FILTER_FLAGS_ = DWORD

class _CM_NOTIFY_FILTER_u_s1_(MemStruct):
    fields = [
        ("ClassGuid", GUID()),
    ]


class _CM_NOTIFY_FILTER_u_s2_(MemStruct):
    fields = [
        ("hTarget", HANDLE()),
    ]


class _CM_NOTIFY_FILTER_u_s3_(MemStruct):
    fields = [
        ("InstanceId", WCHAR__MAX_DEVICE_ID_LEN_()),
    ]

_CM_NOTIFY_FILTER_u_ = Union([
    ("DeviceInterface", _CM_NOTIFY_FILTER_u_s1_),
    ("DeviceHandle", _CM_NOTIFY_FILTER_u_s2_),
    ("DeviceInstance", _CM_NOTIFY_FILTER_u_s3_),
])

class CM_NOTIFY_FILTER(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("Flags", _CM_NOTIFY_FILTER_FLAGS_()),
        ("FilterType", CM_NOTIFY_FILTER_TYPE()),
        ("Reserved", DWORD()),
        ("u", _CM_NOTIFY_FILTER_u_()),
    ]

PCM_NOTIFY_FILTER = Ptr("<I", CM_NOTIFY_FILTER())
_DN_FLAGS_ = ULONG
_DN_FLAGS_PTR_ = Ptr("<I", _DN_FLAGS_())

###################

###### Functions ######

def cfgmgr32_CM_Add_Empty_Log_Conf(jitter):
    """
    CONFIGRET CM_Add_Empty_Log_Conf(
        PLOG_CONF plcLogConf,
        DEVINST dnDevInst,
        PRIORITY Priority,
        [LogicalConfigFlags] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plcLogConf", "dnDevInst", "Priority", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Add_Empty_Log_Conf_Ex(jitter):
    """
    CONFIGRET CM_Add_Empty_Log_Conf_Ex(
        PLOG_CONF plcLogConf,
        DEVINST dnDevInst,
        PRIORITY Priority,
        [LogicalConfigFlags] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plcLogConf", "dnDevInst", "Priority", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Add_ID(jitter, get_str, set_str):
    """
    CONFIGRET CM_Add_ID(
        DEVINST dnDevInst,
        PTSTR pszID,
        [CM_ADD_ID_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "pszID", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Add_IDA(jitter):
    cfgmgr32_CM_Add_ID(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Add_IDW(jitter):
    cfgmgr32_CM_Add_ID(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Add_ID_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Add_ID_Ex(
        DEVINST dnDevInst,
        PTSTR pszID,
        [CM_ADD_ID_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "pszID", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Add_ID_ExA(jitter):
    cfgmgr32_CM_Add_ID_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Add_ID_ExW(jitter):
    cfgmgr32_CM_Add_ID_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Add_Res_Des(jitter):
    """
    CONFIGRET CM_Add_Res_Des(
        PRES_DES prdResDes,
        LOG_CONF lcLogConf,
        RESOURCEID ResourceID,
        PCVOID ResourceData,
        ULONG ResourceLen,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "lcLogConf", "ResourceID", "ResourceData", "ResourceLen", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Add_Res_Des_Ex(jitter):
    """
    CONFIGRET CM_Add_Res_Des_Ex(
        PRES_DES prdResDes,
        LOG_CONF lcLogConf,
        RESOURCEID ResourceID,
        PCVOID ResourceData,
        ULONG ResourceLen,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "lcLogConf", "ResourceID", "ResourceData", "ResourceLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Connect_Machine(jitter, get_str, set_str):
    """
    CONFIGRET CM_Connect_Machine(
        PCTSTR UNCServerName,
        PHMACHINE phMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UNCServerName", "phMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Connect_MachineA(jitter):
    cfgmgr32_CM_Connect_Machine(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Connect_MachineW(jitter):
    cfgmgr32_CM_Connect_Machine(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Delete_Class_Key(jitter):
    """
    CONFIGRET CM_Delete_Class_Key(
        LPGUID ClassGuid,
        [CM_DELETE_CLASS_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_Device_Interface_Key(jitter, get_str, set_str):
    """
    CONFIGRET CM_Delete_Device_Interface_Key(
        LPCTSTR pszDeviceInterface,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_Device_Interface_KeyA(jitter):
    cfgmgr32_CM_Delete_Device_Interface_Key(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Delete_Device_Interface_KeyW(jitter):
    cfgmgr32_CM_Delete_Device_Interface_Key(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Delete_DevNode_Key(jitter):
    """
    CONFIGRET CM_Delete_DevNode_Key(
        DEVNODE dnDevNode,
        ULONG ulHardwareProfile,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevNode", "ulHardwareProfile", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Disable_DevNode(jitter):
    """
    CONFIGRET CM_Disable_DevNode(
        DEVINST dnDevInst,
        [CM_DISABLE_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Disconnect_Machine(jitter):
    """
    CONFIGRET CM_Disconnect_Machine(
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enable_DevNode(jitter):
    """
    CONFIGRET CM_Enable_DevNode(
        DEVINST dnDevInst,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enumerate_Classes(jitter):
    """
    CONFIGRET CM_Enumerate_Classes(
        ULONG ulClassIndex,
        LPGUID ClassGuid,
        [CM_ENUMERATE_CLASSES_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulClassIndex", "ClassGuid", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enumerate_Classes_Ex(jitter):
    """
    CONFIGRET CM_Enumerate_Classes_Ex(
        ULONG ulClassIndex,
        LPGUID ClassGuid,
        [CM_ENUMERATE_CLASSES_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulClassIndex", "ClassGuid", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enumerate_Enumerators(jitter, get_str, set_str):
    """
    CONFIGRET CM_Enumerate_Enumerators(
        ULONG ulEnumIndex,
        PTCHAR Buffer,
        PULONG pulLength,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulEnumIndex", "Buffer", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enumerate_EnumeratorsA(jitter):
    cfgmgr32_CM_Enumerate_Enumerators(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Enumerate_EnumeratorsW(jitter):
    cfgmgr32_CM_Enumerate_Enumerators(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Enumerate_Enumerators_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Enumerate_Enumerators_Ex(
        ULONG ulEnumIndex,
        PTCHAR Buffer,
        PULONG pulLength,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulEnumIndex", "Buffer", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enumerate_Enumerators_ExA(jitter):
    cfgmgr32_CM_Enumerate_Enumerators_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Enumerate_Enumerators_ExW(jitter):
    cfgmgr32_CM_Enumerate_Enumerators_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Free_Log_Conf(jitter):
    """
    CONFIGRET CM_Free_Log_Conf(
        LOG_CONF lcLogConfToBeFreed,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lcLogConfToBeFreed", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Log_Conf_Ex(jitter):
    """
    CONFIGRET CM_Free_Log_Conf_Ex(
        LOG_CONF lcLogConfToBeFreed,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lcLogConfToBeFreed", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Log_Conf_Handle(jitter):
    """
    CONFIGRET CM_Free_Log_Conf_Handle(
        LOG_CONF lcLogConf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lcLogConf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Res_Des(jitter):
    """
    CONFIGRET CM_Free_Res_Des(
        PRES_DES prdResDes,
        RES_DES rdResDes,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "rdResDes", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Res_Des_Ex(jitter):
    """
    CONFIGRET CM_Free_Res_Des_Ex(
        PRES_DES prdResDes,
        RES_DES rdResDes,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "rdResDes", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Res_Des_Handle(jitter):
    """
    CONFIGRET CM_Free_Res_Des_Handle(
        RES_DES rdResDes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rdResDes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Resource_Conflict_Handle(jitter):
    """
    CONFIGRET CM_Free_Resource_Conflict_Handle(
        CONFLICT_LIST clConflictList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clConflictList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Child(jitter):
    """
    CONFIGRET CM_Get_Child(
        PDEVINST pdnDevInst,
        DEVINST dnDevInst,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Child_Ex(jitter):
    """
    CONFIGRET CM_Get_Child_Ex(
        PDEVINST pdnDevInst,
        DEVINST dnDevInst,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_PropertyW(jitter):
    """
    CONFIGRET CM_Get_Class_PropertyW(
        LPCGUID ClassGUID,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE* PropertyType,
        PBYTE PropertyBuffer,
        PULONG PropertyBufferSize,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGUID", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Property_Keys(jitter):
    """
    CONFIGRET CM_Get_Class_Property_Keys(
        LPCGUID ClassGUID,
        DEVPROPKEY* PropertyKeyArray,
        PULONG PropertyKeyCount,
        [CM_CLASS_PROPERTY_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGUID", "PropertyKeyArray", "PropertyKeyCount", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Registry_Property(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Class_Registry_Property(
        LPGUID ClassGuid,
        [CM_CRP] ulProperty,
        PULONG pulRegDataType,
        PVOID Buffer,
        PULONG pulLength,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ulProperty", "pulRegDataType", "Buffer", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Registry_PropertyA(jitter):
    cfgmgr32_CM_Get_Class_Registry_Property(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Registry_PropertyW(jitter):
    cfgmgr32_CM_Get_Class_Registry_Property(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Depth(jitter):
    """
    CONFIGRET CM_Get_Depth(
        PULONG pulDepth,
        DEVINST dnDevInst,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulDepth", "dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Depth_Ex(jitter):
    """
    CONFIGRET CM_Get_Depth_Ex(
        PULONG pulDepth,
        DEVINST dnDevInst,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulDepth", "dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Device_ID(
        DEVINST dnDevInst,
        PTCHAR Buffer,
        ULONG BufferLen,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "Buffer", "BufferLen", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_IDA(jitter):
    cfgmgr32_CM_Get_Device_ID(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_IDW(jitter):
    cfgmgr32_CM_Get_Device_ID(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Device_ID_Ex(
        DEVINST dnDevInst,
        PTCHAR Buffer,
        ULONG BufferLen,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "Buffer", "BufferLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID_ExA(jitter):
    cfgmgr32_CM_Get_Device_ID_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_ExW(jitter):
    cfgmgr32_CM_Get_Device_ID_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Device_ID_List(
        PCTSTR pszFilter,
        PTCHAR Buffer,
        ULONG BufferLen,
        [CM_GETIDLIST_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFilter", "Buffer", "BufferLen", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID_ListA(jitter):
    cfgmgr32_CM_Get_Device_ID_List(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_ListW(jitter):
    cfgmgr32_CM_Get_Device_ID_List(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Device_ID_List_Ex(
        PCTSTR pszFilter,
        PTCHAR Buffer,
        ULONG BufferLen,
        [CM_GETIDLIST_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFilter", "Buffer", "BufferLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID_List_ExA(jitter):
    cfgmgr32_CM_Get_Device_ID_List_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List_ExW(jitter):
    cfgmgr32_CM_Get_Device_ID_List_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List_Size(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Device_ID_List_Size(
        PULONG pulLen,
        PCTSTR pszFilter,
        [CM_GETIDLIST_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulLen", "pszFilter", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID_List_SizeA(jitter):
    cfgmgr32_CM_Get_Device_ID_List_Size(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List_SizeW(jitter):
    cfgmgr32_CM_Get_Device_ID_List_Size(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List_Size_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Device_ID_List_Size_Ex(
        PULONG pulLen,
        PCTSTR pszFilter,
        [CM_GETIDLIST_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulLen", "pszFilter", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID_List_Size_ExA(jitter):
    cfgmgr32_CM_Get_Device_ID_List_Size_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List_Size_ExW(jitter):
    cfgmgr32_CM_Get_Device_ID_List_Size_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_Size(jitter):
    """
    CONFIGRET CM_Get_Device_ID_Size(
        PULONG pulLen,
        DEVINST dnDevInst,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulLen", "dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID_Size_Ex(jitter):
    """
    CONFIGRET CM_Get_Device_ID_Size_Ex(
        PULONG pulLen,
        DEVINST dnDevInst,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulLen", "dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_List(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Device_Interface_List(
        LPGUID InterfaceClassGuid,
        DEVINSTID pDeviceID,
        PTCHAR Buffer,
        ULONG BufferLen,
        [CM_GET_DEVICE_INTERFACE_LIST_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceClassGuid", "pDeviceID", "Buffer", "BufferLen", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_ListA(jitter):
    cfgmgr32_CM_Get_Device_Interface_List(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_ListW(jitter):
    cfgmgr32_CM_Get_Device_Interface_List(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_List_Size(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Device_Interface_List_Size(
        PULONG pulLen,
        LPGUID InterfaceClassGuid,
        DEVINSTID pDeviceID,
        [CM_GET_DEVICE_INTERFACE_LIST_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulLen", "InterfaceClassGuid", "pDeviceID", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_List_SizeA(jitter):
    cfgmgr32_CM_Get_Device_Interface_List_Size(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_List_SizeW(jitter):
    cfgmgr32_CM_Get_Device_Interface_List_Size(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_PropertyW(jitter):
    """
    CONFIGRET CM_Get_Device_Interface_PropertyW(
        LPCWSTR pszDeviceInterface,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE* PropertyType,
        PBYTE PropertyBuffer,
        PULONG PropertyBufferSize,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_Property_KeysW(jitter):
    """
    CONFIGRET CM_Get_Device_Interface_Property_KeysW(
        LPCWSTR pszDeviceInterface,
        DEVPROPKEY* PropertyKeyArray,
        PULONG PropertyKeyCount,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "PropertyKeyArray", "PropertyKeyCount", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_PropertyW(jitter):
    """
    CONFIGRET CM_Get_DevNode_PropertyW(
        DEVINST dnDevInst,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE* PropertyType,
        PBYTE PropertyBuffer,
        PULONG PropertyBufferSize,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Property_Keys(jitter):
    """
    CONFIGRET CM_Get_DevNode_Property_Keys(
        DEVINST dnDevInst,
        DEVPROPKEY* PropertyKeyArray,
        PULONG PropertyKeyCount,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "PropertyKeyArray", "PropertyKeyCount", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Registry_Property(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_DevNode_Registry_Property(
        DEVINST dnDevInst,
        [CM_DRP] ulProperty,
        PULONG pulRegDataType,
        PVOID Buffer,
        PULONG pulLength,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulProperty", "pulRegDataType", "Buffer", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Registry_PropertyA(jitter):
    cfgmgr32_CM_Get_DevNode_Registry_Property(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_DevNode_Registry_PropertyW(jitter):
    cfgmgr32_CM_Get_DevNode_Registry_Property(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_DevNode_Status(jitter):
    """
    CONFIGRET CM_Get_DevNode_Status(
        [DN_FLAGS*] pulStatus,
        [CmProblemNumber*] pulProblemNumber,
        DEVINST dnDevInst,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulStatus", "pulProblemNumber", "dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Status_Ex(jitter):
    """
    CONFIGRET CM_Get_DevNode_Status_Ex(
        [DN_FLAGS*] pulStatus,
        [CmProblemNumber*] pulProblemNumber,
        DEVINST dnDevInst,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulStatus", "pulProblemNumber", "dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_First_Log_Conf(jitter):
    """
    CONFIGRET CM_Get_First_Log_Conf(
        PLOG_CONF plcLogConf,
        DEVINST dnDevInst,
        [LogicalConfigFlags] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plcLogConf", "dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_First_Log_Conf_Ex(jitter):
    """
    CONFIGRET CM_Get_First_Log_Conf_Ex(
        PLOG_CONF plcLogConf,
        DEVINST dnDevInst,
        [LogicalConfigFlags] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plcLogConf", "dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_HW_Prof_Flags(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_HW_Prof_Flags(
        DEVINSTID pDeviceID,
        [CsConfigFlags*] pulValue,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDeviceID", "pulValue", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_HW_Prof_FlagsA(jitter):
    cfgmgr32_CM_Get_HW_Prof_Flags(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_HW_Prof_FlagsW(jitter):
    cfgmgr32_CM_Get_HW_Prof_Flags(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_HW_Prof_Flags_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_HW_Prof_Flags_Ex(
        DEVINSTID pDeviceID,
        ULONG ulHardwareProfile,
        [CsConfigFlags*] pulValue,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDeviceID", "ulHardwareProfile", "pulValue", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_HW_Prof_Flags_ExA(jitter):
    cfgmgr32_CM_Get_HW_Prof_Flags_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_HW_Prof_Flags_ExW(jitter):
    cfgmgr32_CM_Get_HW_Prof_Flags_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Log_Conf_Priority(jitter):
    """
    CONFIGRET CM_Get_Log_Conf_Priority(
        LOG_CONF lcLogConf,
        PPRIORITY pPriority,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lcLogConf", "pPriority", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Log_Conf_Priority_Ex(jitter):
    """
    CONFIGRET CM_Get_Log_Conf_Priority_Ex(
        LOG_CONF lcLogConf,
        PPRIORITY pPriority,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lcLogConf", "pPriority", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Next_Log_Conf(jitter):
    """
    CONFIGRET CM_Get_Next_Log_Conf(
        PLOG_CONF plcLogConf,
        LOG_CONF lcLogConf,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plcLogConf", "lcLogConf", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Next_Log_Conf_Ex(jitter):
    """
    CONFIGRET CM_Get_Next_Log_Conf_Ex(
        PLOG_CONF plcLogConf,
        LOG_CONF lcLogConf,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plcLogConf", "lcLogConf", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Next_Res_Des(jitter):
    """
    CONFIGRET CM_Get_Next_Res_Des(
        PRES_DES prdResDes,
        RES_DES rdResDes,
        RESOURCEID ForResource,
        PRESOURCEID pResourceID,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "rdResDes", "ForResource", "pResourceID", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Next_Res_Des_Ex(jitter):
    """
    CONFIGRET CM_Get_Next_Res_Des_Ex(
        PRES_DES prdResDes,
        RES_DES rdResDes,
        RESOURCEID ForResource,
        PRESOURCEID pResourceID,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "rdResDes", "ForResource", "pResourceID", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Parent(jitter):
    """
    CONFIGRET CM_Get_Parent(
        PDEVINST pdnDevInst,
        DEVINST dnDevInst,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Parent_Ex(jitter):
    """
    CONFIGRET CM_Get_Parent_Ex(
        PDEVINST pdnDevInst,
        DEVINST dnDevInst,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Res_Des_Data(jitter):
    """
    CONFIGRET CM_Get_Res_Des_Data(
        RES_DES rdResDes,
        PVOID Buffer,
        ULONG BufferLen,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rdResDes", "Buffer", "BufferLen", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Res_Des_Data_Ex(jitter):
    """
    CONFIGRET CM_Get_Res_Des_Data_Ex(
        RES_DES rdResDes,
        PVOID Buffer,
        ULONG BufferLen,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rdResDes", "Buffer", "BufferLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Res_Des_Data_Size(jitter):
    """
    CONFIGRET CM_Get_Res_Des_Data_Size(
        PULONG pulSize,
        RES_DES rdResDes,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulSize", "rdResDes", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Res_Des_Data_Size_Ex(jitter):
    """
    CONFIGRET CM_Get_Res_Des_Data_Size_Ex(
        PULONG pulSize,
        RES_DES rdResDes,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulSize", "rdResDes", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Resource_Conflict_Count(jitter):
    """
    CONFIGRET CM_Get_Resource_Conflict_Count(
        CONFLICT_LIST clConflictList,
        PULONG pulCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clConflictList", "pulCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Resource_Conflict_Details(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Resource_Conflict_Details(
        CONFLICT_LIST clConflictList,
        ULONG ulIndex,
        PCONFLICT_DETAILS pConflictDetails
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clConflictList", "ulIndex", "pConflictDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Resource_Conflict_DetailsA(jitter):
    cfgmgr32_CM_Get_Resource_Conflict_Details(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Resource_Conflict_DetailsW(jitter):
    cfgmgr32_CM_Get_Resource_Conflict_Details(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Sibling(jitter):
    """
    CONFIGRET CM_Get_Sibling(
        PDEVINST pdnDevInst,
        DEVINST DevInst,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "DevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Sibling_Ex(jitter):
    """
    CONFIGRET CM_Get_Sibling_Ex(
        PDEVINST pdnDevInst,
        DEVINST DevInst,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "DevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Version(jitter):
    """
    CONFIGRET CM_Get_Version()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Version_Ex(jitter):
    """
    CONFIGRET CM_Get_Version_Ex(
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Is_Dock_Station_Present(jitter):
    """
    CONFIGRET CM_Is_Dock_Station_Present(
        PBOOL pbPresent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbPresent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Is_Dock_Station_Present_Ex(jitter):
    """
    CONFIGRET CM_Is_Dock_Station_Present_Ex(
        PBOOL pbPresent,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbPresent", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Is_Version_Available(jitter):
    """
    CONFIGRET CM_Is_Version_Available(
        WORD wVersion
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Is_Version_Available_Ex(jitter):
    """
    CONFIGRET CM_Is_Version_Available_Ex(
        WORD wVersion,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wVersion", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Locate_DevNode(jitter, get_str, set_str):
    """
    CONFIGRET CM_Locate_DevNode(
        PDEVINST pdnDevInst,
        DEVINSTID pDeviceID,
        [CM_Locate_DevNode_Flags] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "pDeviceID", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Locate_DevNodeA(jitter):
    cfgmgr32_CM_Locate_DevNode(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Locate_DevNodeW(jitter):
    cfgmgr32_CM_Locate_DevNode(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Locate_DevNode_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Locate_DevNode_Ex(
        PDEVINST pdnDevInst,
        DEVINSTID pDeviceID,
        [CM_Locate_DevNode_Flags] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "pDeviceID", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Locate_DevNode_ExA(jitter):
    cfgmgr32_CM_Locate_DevNode_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Locate_DevNode_ExW(jitter):
    cfgmgr32_CM_Locate_DevNode_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Modify_Res_Des(jitter):
    """
    CONFIGRET CM_Modify_Res_Des(
        PRES_DES prdResDes,
        RES_DES rdResDes,
        RESOURCEID ResourceID,
        PCVOID ResourceData,
        ULONG ResourceLen,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "rdResDes", "ResourceID", "ResourceData", "ResourceLen", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Modify_Res_Des_Ex(jitter):
    """
    CONFIGRET CM_Modify_Res_Des_Ex(
        PRES_DES prdResDes,
        RES_DES rdResDes,
        RESOURCEID ResourceID,
        PCVOID ResourceData,
        ULONG ResourceLen,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "rdResDes", "ResourceID", "ResourceData", "ResourceLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Class_Key(jitter, get_str, set_str):
    """
    CONFIGRET CM_Open_Class_Key(
        LPGUID ClassGuid,
        LPCTSTR pszClassName,
        REGSAM samDesired,
        REGDISPOSITION Disposition,
        PHKEY phkClass,
        [CM_OPEN_CLASS_KEY_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "pszClassName", "samDesired", "Disposition", "phkClass", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Class_KeyA(jitter):
    cfgmgr32_CM_Open_Class_Key(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Open_Class_KeyW(jitter):
    cfgmgr32_CM_Open_Class_Key(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Open_Device_Interface_Key(jitter, get_str, set_str):
    """
    CONFIGRET CM_Open_Device_Interface_Key(
        LPCTSTR pszDeviceInterface,
        REGSAM samDesired,
        REGDISPOSITION Disposition,
        PHKEY phkDeviceInterface,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "samDesired", "Disposition", "phkDeviceInterface", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Device_Interface_KeyA(jitter):
    cfgmgr32_CM_Open_Device_Interface_Key(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Open_Device_Interface_KeyW(jitter):
    cfgmgr32_CM_Open_Device_Interface_Key(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Open_DevNode_Key(jitter):
    """
    CONFIGRET CM_Open_DevNode_Key(
        DEVINST dnDevNode,
        REGSAM samDesired,
        ULONG ulHardwareProfile,
        REGDISPOSITION Disposition,
        PHKEY phkDevice,
        [CM_REGISTRY_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevNode", "samDesired", "ulHardwareProfile", "Disposition", "phkDevice", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_And_Remove_SubTree(jitter, get_str, set_str):
    """
    CONFIGRET CM_Query_And_Remove_SubTree(
        DEVINST dnAncestor,
        PPNP_VETO_TYPE pVetoType,
        LPTSTR pszVetoName,
        ULONG ulNameLength,
        [CM_REMOVE_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnAncestor", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_And_Remove_SubTreeA(jitter):
    cfgmgr32_CM_Query_And_Remove_SubTree(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Query_And_Remove_SubTreeW(jitter):
    cfgmgr32_CM_Query_And_Remove_SubTree(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Query_And_Remove_SubTree_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Query_And_Remove_SubTree_Ex(
        DEVINST dnAncestor,
        PPNP_VETO_TYPE pVetoType,
        LPTSTR pszVetoName,
        ULONG ulNameLength,
        [CM_REMOVE_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnAncestor", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_And_Remove_SubTree_ExA(jitter):
    cfgmgr32_CM_Query_And_Remove_SubTree_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Query_And_Remove_SubTree_ExW(jitter):
    cfgmgr32_CM_Query_And_Remove_SubTree_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Query_Resource_Conflict_List(jitter):
    """
    CONFIGRET CM_Query_Resource_Conflict_List(
        PCONFLICT_LIST pclConflictList,
        DEVINST dnDevInst,
        RESOURCEID ResourceID,
        PCVOID ResourceData,
        ULONG ResourceLen,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pclConflictList", "dnDevInst", "ResourceID", "ResourceData", "ResourceLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Reenumerate_DevNode(jitter):
    """
    CONFIGRET CM_Reenumerate_DevNode(
        DEVINST dnDevInst,
        [CM_REENUMERATE_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Reenumerate_DevNode_Ex(jitter):
    """
    CONFIGRET CM_Reenumerate_DevNode_Ex(
        DEVINST dnDevInst,
        [CM_REENUMERATE_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Register_Notification(jitter):
    """
    CONFIGRET CM_Register_Notification(
        PCM_NOTIFY_FILTER pFilter,
        PVOID pContext,
        PCM_NOTIFY_CALLBACK pCallback,
        PHCMNOTIFICATION pNotifyContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFilter", "pContext", "pCallback", "pNotifyContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Request_Device_Eject(jitter, get_str, set_str):
    """
    CONFIGRET CM_Request_Device_Eject(
        DEVINST dnDevInst,
        PPNP_VETO_TYPE pVetoType,
        LPTSTR pszVetoName,
        ULONG ulNameLength,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Request_Device_EjectA(jitter):
    cfgmgr32_CM_Request_Device_Eject(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Request_Device_EjectW(jitter):
    cfgmgr32_CM_Request_Device_Eject(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Request_Device_Eject_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Request_Device_Eject_Ex(
        DEVINST dnDevInst,
        PPNP_VETO_TYPE pVetoType,
        LPTSTR pszVetoName,
        ULONG ulNameLength,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Request_Device_Eject_ExA(jitter):
    cfgmgr32_CM_Request_Device_Eject_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Request_Device_Eject_ExW(jitter):
    cfgmgr32_CM_Request_Device_Eject_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Request_Eject_PC(jitter):
    """
    CONFIGRET CM_Request_Eject_PC()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Request_Eject_PC_Ex(jitter):
    """
    CONFIGRET CM_Request_Eject_PC_Ex(
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_Class_PropertyW(jitter):
    """
    CONFIGRET CM_Set_Class_PropertyW(
        LPCGUID ClassGUID,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE PropertyType,
        CONST PBYTE PropertyBuffer,
        ULONG PropertyBufferSize,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGUID", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_Class_Registry_Property(jitter, get_str, set_str):
    """
    CONFIGRET CM_Set_Class_Registry_Property(
        LPGUID ClassGuid,
        [CM_CRP] ulProperty,
        PCVOID Buffer,
        ULONG ulLength,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ulProperty", "Buffer", "ulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_Class_Registry_PropertyA(jitter):
    cfgmgr32_CM_Set_Class_Registry_Property(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Set_Class_Registry_PropertyW(jitter):
    cfgmgr32_CM_Set_Class_Registry_Property(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Set_Device_Interface_PropertyW(jitter):
    """
    CONFIGRET CM_Set_Device_Interface_PropertyW(
        LPCWSTR pszDeviceInterface,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE PropertyType,
        CONST PBYTE PropertyBuffer,
        ULONG PropertyBufferSize,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Problem(jitter):
    """
    CONFIGRET CM_Set_DevNode_Problem(
        DEVINST dnDevInst,
        [CmProblemNumber] ulProblem,
        [CM_SET_DEVNODE_PROBLEM_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulProblem", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Problem_Ex(jitter):
    """
    CONFIGRET CM_Set_DevNode_Problem_Ex(
        DEVINST dnDevInst,
        [CmProblemNumber] ulProblem,
        [CM_SET_DEVNODE_PROBLEM_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulProblem", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_PropertyW(jitter):
    """
    CONFIGRET CM_Set_DevNode_PropertyW(
        DEVINST dnDevInst,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE PropertyType,
        CONST PBYTE PropertyBuffer,
        ULONG PropertyBufferSize,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Registry_Property(jitter, get_str, set_str):
    """
    CONFIGRET CM_Set_DevNode_Registry_Property(
        DEVINST dnDevInst,
        [CM_DRP] ulProperty,
        PCVOID Buffer,
        ULONG ulLength,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulProperty", "Buffer", "ulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Registry_PropertyA(jitter):
    cfgmgr32_CM_Set_DevNode_Registry_Property(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Set_DevNode_Registry_PropertyW(jitter):
    cfgmgr32_CM_Set_DevNode_Registry_Property(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Setup_DevNode(jitter):
    """
    CONFIGRET CM_Setup_DevNode(
        DEVINST dnDevInst,
        [CM_SETUP_DEVNODE_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Uninstall_DevNode(jitter):
    """
    CONFIGRET CM_Uninstall_DevNode(
        DEVNODE dnDevInst,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Unregister_Notification(jitter):
    """
    CONFIGRET CM_Unregister_Notification(
        HCMNOTIFICATION NotifyContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NotifyContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_WaitNoPendingInstallEvents(jitter):
    """
    [WAIT_RESULT] CM_WaitNoPendingInstallEvents(
        DWORD dwTimeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CMP_WaitNoPendingInstallEvents(jitter):
    """
    [WAIT_RESULT] CMP_WaitNoPendingInstallEvents(
        DWORD dwTimeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Add_Range(jitter):
    """
    CONFIGRET CM_Add_Range(
        DWORDLONG ullStartValue,
        DWORDLONG ullEndValue,
        RANGE_LIST rlh,
        [CM_ADD_RANGE_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ullStartValue", "ullEndValue", "rlh", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Create_DevNode(jitter, get_str, set_str):
    """
    CONFIGRET CM_Create_DevNode(
        PDEVINST pdnDevInst,
        DEVINSTID pDeviceID,
        DEVINST dnParent,
        [CM_CREATE_DEVNODE_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "pDeviceID", "dnParent", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Create_DevNodeA(jitter):
    cfgmgr32_CM_Create_DevNode(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Create_DevNodeW(jitter):
    cfgmgr32_CM_Create_DevNode(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Create_DevNode_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Create_DevNode_Ex(
        PDEVINST pdnDevInst,
        DEVINSTID pDeviceID,
        DEVINST dnParent,
        [CM_CREATE_DEVNODE_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "pDeviceID", "dnParent", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Create_DevNode_ExA(jitter):
    cfgmgr32_CM_Create_DevNode_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Create_DevNode_ExW(jitter):
    cfgmgr32_CM_Create_DevNode_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Create_Range_List(jitter):
    """
    CONFIGRET CM_Create_Range_List(
        PRANGE_LIST prlh,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["prlh", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_Class_Key_Ex(jitter):
    """
    CONFIGRET CM_Delete_Class_Key_Ex(
        LPGUID ClassGuid,
        [CM_DELETE_CLASS_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_DevNode_Key_Ex(jitter):
    """
    CONFIGRET CM_Delete_DevNode_Key_Ex(
        DEVNODE dnDevNode,
        ULONG ulHardwareProfile,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevNode", "ulHardwareProfile", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_Range(jitter):
    """
    CONFIGRET CM_Delete_Range(
        DWORDLONG ullStartValue,
        DWORDLONG ullEndValue,
        RANGE_LIST rlh,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ullStartValue", "ullEndValue", "rlh", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Disable_DevNode_Ex(jitter):
    """
    CONFIGRET CM_Disable_DevNode_Ex(
        DEVINST dnDevInst,
        [CM_DISABLE_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Dup_Range_List(jitter):
    """
    CONFIGRET CM_Dup_Range_List(
        RANGE_LIST rlhOld,
        RANGE_LIST rlhNew,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rlhOld", "rlhNew", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enable_DevNode_Ex(jitter):
    """
    CONFIGRET CM_Enable_DevNode_Ex(
        DEVINST dnDevInst,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Find_Range(jitter):
    """
    CONFIGRET CM_Find_Range(
        PDWORDLONG pullStart,
        DWORDLONG ullStart,
        ULONG ulLength,
        DWORDLONG ullAlignment,
        DWORDLONG ullEnd,
        RANGE_LIST rlh,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pullStart", "ullStart", "ulLength", "ullAlignment", "ullEnd", "rlh", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_First_Range(jitter):
    """
    CONFIGRET CM_First_Range(
        RANGE_LIST rlh,
        PDWORDLONG pullStart,
        PDWORDLONG pullEnd,
        PRANGE_ELEMENT preElement,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rlh", "pullStart", "pullEnd", "preElement", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Range_List(jitter):
    """
    CONFIGRET CM_Free_Range_List(
        RANGE_LIST rlh,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rlh", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Key_Name(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Class_Key_Name(
        LPGUID ClassGuid,
        LPTSTR pszKeyName,
        PULONG pulLength,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "pszKeyName", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Key_NameA(jitter):
    cfgmgr32_CM_Get_Class_Key_Name(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Key_NameW(jitter):
    cfgmgr32_CM_Get_Class_Key_Name(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Key_Name_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Class_Key_Name_Ex(
        LPGUID ClassGuid,
        LPTSTR pszKeyName,
        PULONG pulLength,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "pszKeyName", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Key_Name_ExA(jitter):
    cfgmgr32_CM_Get_Class_Key_Name_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Key_Name_ExW(jitter):
    cfgmgr32_CM_Get_Class_Key_Name_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Name(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Class_Name(
        LPGUID ClassGuid,
        PTSTR Buffer,
        PULONG pulLength,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "Buffer", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_NameA(jitter):
    cfgmgr32_CM_Get_Class_Name(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Class_NameW(jitter):
    cfgmgr32_CM_Get_Class_Name(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Name_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Class_Name_Ex(
        LPGUID ClassGuid,
        PTSTR Buffer,
        PULONG pulLength,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "Buffer", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Name_ExA(jitter):
    cfgmgr32_CM_Get_Class_Name_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Name_ExW(jitter):
    cfgmgr32_CM_Get_Class_Name_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_Alias(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Device_Interface_Alias(
        LPCTSTR pszDeviceInterface,
        LPGUID AliasInterfaceGuid,
        LPTSTR pszAliasDeviceInterface,
        PULONG pulLength,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "AliasInterfaceGuid", "pszAliasDeviceInterface", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_AliasA(jitter):
    cfgmgr32_CM_Get_Device_Interface_Alias(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_AliasW(jitter):
    cfgmgr32_CM_Get_Device_Interface_Alias(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_Alias_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Device_Interface_Alias_Ex(
        LPCTSTR pszDeviceInterface,
        LPGUID AliasInterfaceGuid,
        LPTSTR pszAliasDeviceInterface,
        PULONG pulLength,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "AliasInterfaceGuid", "pszAliasDeviceInterface", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_Alias_ExA(jitter):
    cfgmgr32_CM_Get_Device_Interface_Alias_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_Alias_ExW(jitter):
    cfgmgr32_CM_Get_Device_Interface_Alias_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_List_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Device_Interface_List_Ex(
        LPGUID InterfaceClassGuid,
        DEVINSTID pDeviceID,
        PTCHAR Buffer,
        ULONG BufferLen,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceClassGuid", "pDeviceID", "Buffer", "BufferLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_List_ExA(jitter):
    cfgmgr32_CM_Get_Device_Interface_List_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_List_ExW(jitter):
    cfgmgr32_CM_Get_Device_Interface_List_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_List_Size_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Device_Interface_List_Size_Ex(
        PULONG pulLen,
        LPGUID InterfaceClassGuid,
        DEVINSTID pDeviceID,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulLen", "InterfaceClassGuid", "pDeviceID", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_List_Size_ExA(jitter):
    cfgmgr32_CM_Get_Device_Interface_List_Size_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_List_Size_ExW(jitter):
    cfgmgr32_CM_Get_Device_Interface_List_Size_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_DevNode_Custom_Property(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_DevNode_Custom_Property(
        DEVINST dnDevInst,
        PCTSTR pszCustomPropertyName,
        PULONG pulRegDataType,
        PVOID Buffer,
        PULONG pulLength,
        [CM_CUSTOMDEVPROP_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "pszCustomPropertyName", "pulRegDataType", "Buffer", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Custom_PropertyA(jitter):
    cfgmgr32_CM_Get_DevNode_Custom_Property(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_DevNode_Custom_PropertyW(jitter):
    cfgmgr32_CM_Get_DevNode_Custom_Property(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_DevNode_Custom_Property_ExW(jitter):
    """
    CONFIGRET CM_Get_DevNode_Custom_Property_ExW(
        DEVINST dnDevInst,
        PCTSTR pszCustomPropertyName,
        PULONG pulRegDataType,
        PVOID Buffer,
        PULONG pulLength,
        [CM_CUSTOMDEVPROP_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "pszCustomPropertyName", "pulRegDataType", "Buffer", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Registry_Property_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_DevNode_Registry_Property_Ex(
        DEVINST dnDevInst,
        [CM_DRP] ulProperty,
        PULONG pulRegDataType,
        PVOID Buffer,
        PULONG pulLength,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulProperty", "pulRegDataType", "Buffer", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Registry_Property_ExA(jitter):
    cfgmgr32_CM_Get_DevNode_Registry_Property_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_DevNode_Registry_Property_ExW(jitter):
    cfgmgr32_CM_Get_DevNode_Registry_Property_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Global_State(jitter):
    """
    CONFIGRET CM_Get_Global_State(
        PULONG pulState,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulState", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Global_State_Ex(jitter):
    """
    CONFIGRET CM_Get_Global_State_Ex(
        PULONG pulState,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulState", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Hardware_Profile_Info(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Hardware_Profile_Info(
        ULONG ulIndex,
        PHWPROFILEINFO pHWProfileInfo,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIndex", "pHWProfileInfo", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Hardware_Profile_InfoA(jitter):
    cfgmgr32_CM_Get_Hardware_Profile_Info(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Hardware_Profile_InfoW(jitter):
    cfgmgr32_CM_Get_Hardware_Profile_Info(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Hardware_Profile_Info_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Get_Hardware_Profile_Info_Ex(
        ULONG ulIndex,
        PHWPROFILEINFO pHWProfileInfo,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIndex", "pHWProfileInfo", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Hardware_Profile_Info_ExA(jitter):
    cfgmgr32_CM_Get_Hardware_Profile_Info_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Hardware_Profile_Info_ExW(jitter):
    cfgmgr32_CM_Get_Hardware_Profile_Info_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Intersect_Range_List(jitter):
    """
    CONFIGRET CM_Intersect_Range_List(
        RANGE_LIST rlhOld1,
        RANGE_LIST rlhOld2,
        RANGE_LIST rlhNew,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rlhOld1", "rlhOld2", "rlhNew", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Invert_Range_List(jitter):
    """
    CONFIGRET CM_Invert_Range_List(
        RANGE_LIST rlhOld,
        RANGE_LIST rlhNew,
        DWORDLONG ullMaxValue,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rlhOld", "rlhNew", "ullMaxValue", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Merge_Range_List(jitter):
    """
    CONFIGRET CM_Merge_Range_List(
        RANGE_LIST rlhOld1,
        RANGE_LIST rlhOld2,
        RANGE_LIST rlhNew,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rlhOld1", "rlhOld2", "rlhNew", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Move_DevNode(jitter):
    """
    CONFIGRET CM_Move_DevNode(
        DEVINST dnFromDevInst,
        DEVINST dnToDevInst,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnFromDevInst", "dnToDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Move_DevNode_Ex(jitter):
    """
    CONFIGRET CM_Move_DevNode_Ex(
        DEVINST dnFromDevInst,
        DEVINST dnToDevInst,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnFromDevInst", "dnToDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Next_Range(jitter):
    """
    CONFIGRET CM_Next_Range(
        PRANGE_ELEMENT preElement,
        PDWORDLONG pullStart,
        PDWORDLONG pullEnd,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["preElement", "pullStart", "pullEnd", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Class_Key_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Open_Class_Key_Ex(
        LPGUID ClassGuid,
        LPCTSTR pszClassName,
        REGSAM samDesired,
        REGDISPOSITION Disposition,
        PHKEY phkClass,
        [CM_OPEN_CLASS_KEY_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "pszClassName", "samDesired", "Disposition", "phkClass", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Class_Key_ExA(jitter):
    cfgmgr32_CM_Open_Class_Key_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Open_Class_Key_ExW(jitter):
    cfgmgr32_CM_Open_Class_Key_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Open_DevNode_Key_Ex(jitter):
    """
    CONFIGRET CM_Open_DevNode_Key_Ex(
        DEVINST dnDevNode,
        REGSAM samDesired,
        ULONG ulHardwareProfile,
        REGDISPOSITION Disposition,
        PHKEY phkDevice,
        [CM_REGISTRY_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevNode", "samDesired", "ulHardwareProfile", "Disposition", "phkDevice", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_Arbitrator_Free_Data(jitter):
    """
    CONFIGRET CM_Query_Arbitrator_Free_Data(
        PVOID pData,
        ULONG DataLen,
        DEVINST dnDevInst,
        RESOURCEID ResourceID,
        [CM_QUERY_ARBITRATOR_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pData", "DataLen", "dnDevInst", "ResourceID", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_Arbitrator_Free_Data_Ex(jitter):
    """
    CONFIGRET CM_Query_Arbitrator_Free_Data_Ex(
        PVOID pData,
        ULONG DataLen,
        DEVINST dnDevInst,
        RESOURCEID ResourceID,
        [CM_QUERY_ARBITRATOR_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pData", "DataLen", "dnDevInst", "ResourceID", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_Arbitrator_Free_Size(jitter):
    """
    CONFIGRET CM_Query_Arbitrator_Free_Size(
        PULONG pulSize,
        DEVINST dnDevInst,
        RESOURCEID ResourceID,
        [CM_QUERY_ARBITRATOR_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulSize", "dnDevInst", "ResourceID", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_Arbitrator_Free_Size_Ex(jitter):
    """
    CONFIGRET CM_Query_Arbitrator_Free_Size_Ex(
        PULONG pulSize,
        DEVINST dnDevInst,
        RESOURCEID ResourceID,
        [CM_QUERY_ARBITRATOR_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulSize", "dnDevInst", "ResourceID", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_Remove_SubTree(jitter):
    """
    CONFIGRET CM_Query_Remove_SubTree(
        DEVINST dnAncestor,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnAncestor", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_Remove_SubTree_Ex(jitter):
    """
    CONFIGRET CM_Query_Remove_SubTree_Ex(
        DEVINST dnAncestor,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnAncestor", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Register_Device_Driver(jitter):
    """
    CONFIGRET CM_Register_Device_Driver(
        DEVINST dnDevInst,
        [CM_REGISTER_DEVICE_DRIVER_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Register_Device_Driver_Ex(jitter):
    """
    CONFIGRET CM_Register_Device_Driver_Ex(
        DEVINST dnDevInst,
        [CM_REGISTER_DEVICE_DRIVER_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Register_Device_Interface(jitter, get_str, set_str):
    """
    CONFIGRET CM_Register_Device_Interface(
        DEVINST dnDevInst,
        LPGUID InterfaceClassGuid,
        LPCTSTR pszReference,
        LPTSTR pszDeviceInterface,
        PULONG pulLength,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "InterfaceClassGuid", "pszReference", "pszDeviceInterface", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Register_Device_InterfaceA(jitter):
    cfgmgr32_CM_Register_Device_Interface(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Register_Device_InterfaceW(jitter):
    cfgmgr32_CM_Register_Device_Interface(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Register_Device_Interface_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Register_Device_Interface_Ex(
        DEVINST dnDevInst,
        LPGUID InterfaceClassGuid,
        LPCTSTR pszReference,
        LPTSTR pszDeviceInterface,
        PULONG pulLength,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "InterfaceClassGuid", "pszReference", "pszDeviceInterface", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Register_Device_Interface_ExA(jitter):
    cfgmgr32_CM_Register_Device_Interface_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Register_Device_Interface_ExW(jitter):
    cfgmgr32_CM_Register_Device_Interface_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Run_Detection(jitter):
    """
    CONFIGRET CM_Run_Detection(
        [CM_DETECT_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Run_Detection_Ex(jitter):
    """
    CONFIGRET CM_Run_Detection_Ex(
        [CM_DETECT_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Registry_Property_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Set_DevNode_Registry_Property_Ex(
        DEVINST dnDevInst,
        [CM_DRP] ulProperty,
        PCVOID Buffer,
        ULONG ulLength,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulProperty", "Buffer", "ulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Registry_Property_ExA(jitter):
    cfgmgr32_CM_Set_DevNode_Registry_Property_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Set_DevNode_Registry_Property_ExW(jitter):
    cfgmgr32_CM_Set_DevNode_Registry_Property_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Set_HW_Prof(jitter):
    """
    CONFIGRET CM_Set_HW_Prof(
        ULONG ulHardwareProfile,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulHardwareProfile", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_HW_Prof_Ex(jitter):
    """
    CONFIGRET CM_Set_HW_Prof_Ex(
        ULONG ulHardwareProfile,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulHardwareProfile", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_HW_Prof_Flags(jitter, get_str, set_str):
    """
    CONFIGRET CM_Set_HW_Prof_Flags(
        DEVINSTID pDeviceID,
        ULONG ulConfig,
        ULONG ulValue,
        [CM_SET_HW_PROF_FLAGS] ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDeviceID", "ulConfig", "ulValue", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_HW_Prof_FlagsA(jitter):
    cfgmgr32_CM_Set_HW_Prof_Flags(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Set_HW_Prof_FlagsW(jitter):
    cfgmgr32_CM_Set_HW_Prof_Flags(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Set_HW_Prof_Flags_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Set_HW_Prof_Flags_Ex(
        DEVINSTID pDeviceID,
        ULONG ulConfig,
        ULONG ulValue,
        [CM_SET_HW_PROF_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDeviceID", "ulConfig", "ulValue", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_HW_Prof_Flags_ExA(jitter):
    cfgmgr32_CM_Set_HW_Prof_Flags_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Set_HW_Prof_Flags_ExW(jitter):
    cfgmgr32_CM_Set_HW_Prof_Flags_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Setup_DevNode_Ex(jitter):
    """
    CONFIGRET CM_Setup_DevNode_Ex(
        DEVINST dnDevInst,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Test_Range_Available(jitter):
    """
    CONFIGRET CM_Test_Range_Available(
        DWORDLONG ullStartValue,
        DWORDLONG ullEndValue,
        RANGE_LIST rlh,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ullStartValue", "ullEndValue", "rlh", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Uninstall_DevNode_Ex(jitter):
    """
    CONFIGRET CM_Uninstall_DevNode_Ex(
        DEVNODE dnDevInst,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Unregister_Device_Interface(jitter, get_str, set_str):
    """
    CONFIGRET CM_Unregister_Device_Interface(
        LPCTSTR pszDeviceInterface,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Unregister_Device_InterfaceA(jitter):
    cfgmgr32_CM_Unregister_Device_Interface(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Unregister_Device_InterfaceW(jitter):
    cfgmgr32_CM_Unregister_Device_Interface(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Unregister_Device_Interface_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Unregister_Device_Interface_Ex(
        LPCTSTR pszDeviceInterface,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Unregister_Device_Interface_ExA(jitter):
    cfgmgr32_CM_Unregister_Device_Interface_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Unregister_Device_Interface_ExW(jitter):
    cfgmgr32_CM_Unregister_Device_Interface_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Detect_Resource_Conflict(jitter):
    """
    CONFIGRET CM_Detect_Resource_Conflict(
        DEVINST dnDevInst,
        RESOURCEID ResourceID,
        PCVOID ResourceData,
        ULONG ResourceLen,
        PBOOL pbConflictDetected,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ResourceID", "ResourceData", "ResourceLen", "pbConflictDetected", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Detect_Resource_Conflict_Ex(jitter):
    """
    CONFIGRET CM_Detect_Resource_Conflict_Ex(
        DEVINST dnDevInst,
        RESOURCEID ResourceID,
        PCVOID ResourceData,
        ULONG ResourceLen,
        PBOOL pbConflictDetected,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ResourceID", "ResourceData", "ResourceLen", "pbConflictDetected", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Remove_SubTree(jitter):
    """
    CONFIGRET CM_Remove_SubTree(
        DEVINST dnAncestor,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnAncestor", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Remove_SubTree_Ex(jitter):
    """
    CONFIGRET CM_Remove_SubTree_Ex(
        DEVINST dnAncestor,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnAncestor", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_RestoreAll_DefaultPowerSchemes(jitter):
    """
    CONFIGRET CM_RestoreAll_DefaultPowerSchemes(
        PDWORD Error
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Restore_DefaultPowerScheme(jitter):
    """
    CONFIGRET CM_Restore_DefaultPowerScheme(
        CONST GUID* SchemeGuid,
        PDWORD Error
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SchemeGuid", "Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_ActiveScheme(jitter):
    """
    CONFIGRET CM_Set_ActiveScheme(
        CONST GUID* SchemeGuid,
        PDWORD Error
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SchemeGuid", "Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Apply_PowerScheme(jitter):
    """
    CONFIGRET CM_Apply_PowerScheme()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_PowerScheme(jitter):
    """
    CONFIGRET CM_Delete_PowerScheme(
        CONST GUID* SchemeGuid,
        PDWORD Error
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SchemeGuid", "Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Duplicate_PowerScheme(jitter):
    """
    CONFIGRET CM_Duplicate_PowerScheme(
        CONST GUID* SourceSchemeGuid,
        GUID** DestinationSchemeGuid,
        PDWORD Error
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceSchemeGuid", "DestinationSchemeGuid", "Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Import_PowerScheme(jitter):
    """
    CONFIGRET CM_Import_PowerScheme(
        LPCWSTR ImportFileNamePath,
        GUID** DestinationSchemeGuid,
        PDWORD Error
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImportFileNamePath", "DestinationSchemeGuid", "Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Write_UserPowerKey(jitter):
    """
    CONFIGRET CM_Write_UserPowerKey(
        CONST GUID* SchemeGuid,
        CONST GUID* SubGroupOfPowerSettingsGuid,
        CONST GUID* PowerSettingGuid,
        ULONG AccessFlags,
        ULONG Type,
        UCHAR* Buffer,
        DWORD BufferSize,
        PDWORD Error
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "AccessFlags", "Type", "Buffer", "BufferSize", "Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_Class_Property_ExW(jitter):
    """
    CONFIGRET CM_Set_Class_Property_ExW(
        LPCGUID ClassGUID,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE PropertyType,
        CONST PBYTE PropertyBuffer,
        ULONG PropertyBufferSize,
        [CM_CLASS_PROPERTY_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGUID", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Property_ExW(jitter):
    """
    CONFIGRET CM_Set_DevNode_Property_ExW(
        DEVINST dnDevInst,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE PropertyType,
        CONST PBYTE PropertyBuffer,
        ULONG PropertyBufferSize,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_Device_Interface_Property_ExW(jitter):
    """
    CONFIGRET CM_Set_Device_Interface_Property_ExW(
        LPCWSTR pszDeviceInterface,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE PropertyType,
        CONST PBYTE PropertyBuffer,
        ULONG PropertyBufferSize,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_Device_Interface_Key_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Delete_Device_Interface_Key_Ex(
        LPCTSTR pszDeviceInterface,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_Device_Interface_Key_ExA(jitter):
    cfgmgr32_CM_Delete_Device_Interface_Key_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Delete_Device_Interface_Key_ExW(jitter):
    cfgmgr32_CM_Delete_Device_Interface_Key_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Property_ExW(jitter):
    """
    CONFIGRET CM_Get_Class_Property_ExW(
        LPCGUID ClassGUID,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE* PropertyType,
        PBYTE PropertyBuffer,
        PULONG PropertyBufferSize,
        [CM_CLASS_PROPERTY_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGUID", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Property_Keys_Ex(jitter):
    """
    CONFIGRET CM_Get_Class_Property_Keys_Ex(
        LPCGUID ClassGUID,
        DEVPROPKEY* PropertyKeyArray,
        PULONG PropertyKeyCount,
        [CM_CLASS_PROPERTY_FLAGS] ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGUID", "PropertyKeyArray", "PropertyKeyCount", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Property_ExW(jitter):
    """
    CONFIGRET CM_Get_DevNode_Property_ExW(
        DEVINST dnDevInst,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE* PropertyType,
        PBYTE PropertyBuffer,
        PULONG PropertyBufferSize,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Property_Keys_Ex(jitter):
    """
    CONFIGRET CM_Get_DevNode_Property_Keys_Ex(
        DEVINST dnDevInst,
        DEVPROPKEY* PropertyKeyArray,
        PULONG PropertyKeyCount,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "PropertyKeyArray", "PropertyKeyCount", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_Property_ExW(jitter):
    """
    CONFIGRET CM_Get_Device_Interface_Property_ExW(
        LPCWSTR pszDeviceInterface,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE* PropertyType,
        PBYTE PropertyBuffer,
        PULONG PropertyBufferSize,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_Property_Keys_ExW(jitter):
    """
    CONFIGRET CM_Get_Device_Interface_Property_Keys_ExW(
        LPCWSTR pszDeviceInterface,
        DEVPROPKEY* PropertyKeyArray,
        PULONG PropertyKeyCount,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "PropertyKeyArray", "PropertyKeyCount", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Device_Interface_Key_Ex(jitter, get_str, set_str):
    """
    CONFIGRET CM_Open_Device_Interface_Key_Ex(
        LPCTSTR pszDeviceInterface,
        REGSAM samDesired,
        REGDISPOSITION Disposition,
        PHKEY phkDeviceInterface,
        ULONG ulFlags,
        HMACHINE hMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "samDesired", "Disposition", "phkDeviceInterface", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Device_Interface_Key_ExA(jitter):
    cfgmgr32_CM_Open_Device_Interface_Key_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Open_Device_Interface_Key_ExW(jitter):
    cfgmgr32_CM_Open_Device_Interface_Key_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
