###### Enums ######
DHCP_OPTION_DATA_TYPE = {
    "DhcpByteOption": 0,
    "DhcpWordOption": 1,
    "DhcpDWordOption": 2,
    "DhcpDWordDWordOption": 3,
    "DhcpIpAddressOption": 4,
    "DhcpStringDataOption": 5,
    "DhcpBinaryDataOption": 6,
    "DhcpEncapsulatedDataOption": 7,
    "DhcpIpv6AddressOption": 8,
}
DHCP_OPTION_DATA_TYPE_INV = {
    0: "DhcpByteOption",
    1: "DhcpWordOption",
    2: "DhcpDWordOption",
    3: "DhcpDWordDWordOption",
    4: "DhcpIpAddressOption",
    5: "DhcpStringDataOption",
    6: "DhcpBinaryDataOption",
    7: "DhcpEncapsulatedDataOption",
    8: "DhcpIpv6AddressOption",
}
DHCP_SUBNET_ELEMENT_TYPE = {
    "DhcpIpRanges": 0,
    "DhcpSecondaryHosts": 1,
    "DhcpReservedIps": 2,
    "DhcpExcludedIpRanges": 3,
    "DhcpIpUsedClusters": 4,
    "DhcpIpRangesDhcpOnly": 5,
    "DhcpIpRangesDhcpBootp": 6,
    "DhcpIpRangesBootpOnly": 7,
}
DHCP_SUBNET_ELEMENT_TYPE_INV = {
    0: "DhcpIpRanges",
    1: "DhcpSecondaryHosts",
    2: "DhcpReservedIps",
    3: "DhcpExcludedIpRanges",
    4: "DhcpIpUsedClusters",
    5: "DhcpIpRangesDhcpOnly",
    6: "DhcpIpRangesDhcpBootp",
    7: "DhcpIpRangesBootpOnly",
}
DHCP_SEARCH_INFO_TYPE = {
    "DhcpClientIpAddress": 0,
    "DhcpClientHardwareAddress": 1,
    "DhcpClientName": 2,
}
DHCP_SEARCH_INFO_TYPE_INV = {
    0: "DhcpClientIpAddress",
    1: "DhcpClientHardwareAddress",
    2: "DhcpClientName",
}
DHCP_OPTION_SCOPE_TYPE = {
    "DhcpDefaultOptions": 0,
    "DhcpGlobalOptions": 1,
    "DhcpSubnetOptions": 2,
    "DhcpReservedOptions": 3,
    "DhcpMScopeOptions": 4,
}
DHCP_OPTION_SCOPE_TYPE_INV = {
    0: "DhcpDefaultOptions",
    1: "DhcpGlobalOptions",
    2: "DhcpSubnetOptions",
    3: "DhcpReservedOptions",
    4: "DhcpMScopeOptions",
}
DHCP_SUBNET_ELEMENT_TYPE_V6 = {
    "Dhcpv6IpRanges": 0,
    "Dhcpv6ReservedIps": 1,
    "Dhcpv6ExcludedIpRanges": 2,
}
DHCP_SUBNET_ELEMENT_TYPE_V6_INV = {
    0: "Dhcpv6IpRanges",
    1: "Dhcpv6ReservedIps",
    2: "Dhcpv6ExcludedIpRanges",
}
DHCP_SEARCH_INFO_TYPE_V6 = {
    "Dhcpv6ClientIpAddress": 0,
    "Dhcpv6ClientDUID": 1,
    "Dhcpv6ClientName": 2,
}
DHCP_SEARCH_INFO_TYPE_V6_INV = {
    0: "Dhcpv6ClientIpAddress",
    1: "Dhcpv6ClientDUID",
    2: "Dhcpv6ClientName",
}
DHCP_OPTION_SCOPE_TYPE6 = {
    "DhcpDefaultOptions6": 0,
    "DhcpScopeOptions6": 1,
    "DhcpReservedOptions6": 2,
    "DhcpGlobalOptions6": 3,
}
DHCP_OPTION_SCOPE_TYPE6_INV = {
    0: "DhcpDefaultOptions6",
    1: "DhcpScopeOptions6",
    2: "DhcpReservedOptions6",
    3: "DhcpGlobalOptions6",
}
DHCP_OPTION_TYPE = {
    "DhcpUnaryElementTypeOption": 0,
    "DhcpArrayTypeOption": 1,
}
DHCP_OPTION_TYPE_INV = {
    0: "DhcpUnaryElementTypeOption",
    1: "DhcpArrayTypeOption",
}
DHCP_FILTER_LIST_TYPE = {
    "Deny": 0,
    "Allow": 1,
}
DHCP_FILTER_LIST_TYPE_INV = {
    0: "Deny",
    1: "Allow",
}
QuarantineStatus = {
    "NOQUARANTINE": 0,
    "RESTRICTEDACCESS": 1,
    "DROPPACKET": 2,
    "PROBATION": 3,
    "EXEMPT": 4,
    "DEFAULTQUARSETTING": 5,
    "NOQUARINFO": 6,
}
QuarantineStatus_INV = {
    0: "NOQUARANTINE",
    1: "RESTRICTEDACCESS",
    2: "DROPPACKET",
    3: "PROBATION",
    4: "EXEMPT",
    5: "DEFAULTQUARSETTING",
    6: "NOQUARINFO",
}
DHCP_SUBNET_STATE = {
    "DhcpSubnetEnabled": 0,
    "DhcpSubnetDisabled": 1,
    "DhcpSubnetEnabledSwitched": 2,
    "DhcpSubnetDisabledSwitched": 3,
    "DhcpSubnetInvalidState": 4,
}
DHCP_SUBNET_STATE_INV = {
    0: "DhcpSubnetEnabled",
    1: "DhcpSubnetDisabled",
    2: "DhcpSubnetEnabledSwitched",
    3: "DhcpSubnetDisabledSwitched",
    4: "DhcpSubnetInvalidState",
}
DHCP_FORCE_FLAG = {
    "DhcpFullForce": 0,
    "DhcpNoForce": 1,
}
DHCP_FORCE_FLAG_INV = {
    0: "DhcpFullForce",
    1: "DhcpNoForce",
}
DHCP_POL_ATTR_TYPE = {
    "DhcpAttrHWAddr": 0,
    "DhcpAttrOption": 1,
    "DhcpAttrSubOption": 2,
}
DHCP_POL_ATTR_TYPE_INV = {
    0: "DhcpAttrHWAddr",
    1: "DhcpAttrOption",
    2: "DhcpAttrSubOption",
}
DHCP_POL_COMPARATOR = {
    "DhcpCompEqual": 0,
    "DhcpCompNotEqual": 1,
    "DhcpCompBeginsWith": 2,
    "DhcpCompNotBeginWith": 3,
}
DHCP_POL_COMPARATOR_INV = {
    0: "DhcpCompEqual",
    1: "DhcpCompNotEqual",
    2: "DhcpCompBeginsWith",
    3: "DhcpCompNotBeginWith",
}
DHCP_POL_LOGIC_OPER = {
    "DhcpLogicalOr": 0,
    "DhcpLogicalAnd": 1,
}
DHCP_POL_LOGIC_OPER_INV = {
    0: "DhcpLogicalOr",
    1: "DhcpLogicalAnd",
}
DHCP_ATTRIB_ID = {
    "DHCP_ATTRIB_BOOL_IS_ROGUE": 0x01,
    "DHCP_ATTRIB_BOOL_IS_DYNBOOTP": 0x02,
    "DHCP_ATTRIB_BOOL_IS_PART_OF_DSDC": 0x03,
    "DHCP_ATTRIB_BOOL_IS_BINDING_AWARE": 0x04,
    "DHCP_ATTRIB_BOOL_IS_ADMIN": 0x05,
    "DHCP_ATTRIB_ULONG_RESTORE_STATUS": 0x06,
}
DHCP_ATTRIB_ID_INV = {
    0x01: "DHCP_ATTRIB_BOOL_IS_ROGUE",
    0x02: "DHCP_ATTRIB_BOOL_IS_DYNBOOTP",
    0x03: "DHCP_ATTRIB_BOOL_IS_PART_OF_DSDC",
    0x04: "DHCP_ATTRIB_BOOL_IS_BINDING_AWARE",
    0x05: "DHCP_ATTRIB_BOOL_IS_ADMIN",
    0x06: "DHCP_ATTRIB_ULONG_RESTORE_STATUS",
}
DHCP_SCAN_FLAG = {
    "DhcpRegistryFix": 0,
    "DhcpDatabaseFix": 1,
}
DHCP_SCAN_FLAG_INV = {
    0: "DhcpRegistryFix",
    1: "DhcpDatabaseFix",
}
FSM_STATE = {
    "NO_STATE": 0,
    "INIT": 1,
    "NORMAL": 2,
    "STARTUP": 3,
    "COMMUNICATION_INT": 4,
    "PARTNER_DOWN": 5,
    "POTENTIAL_CONFLICT": 6,
    "CONFLICT_DONE": 7,
    "RESOLUTION_INT": 8,
    "RECOVER": 9,
    "RECOVER_WAIT": 10,
    "RECOVER_DONE": 11,
    "PAUSED": 12,
    "SHUTDOWN": 13,
}
FSM_STATE_INV = {
    0: "NO_STATE",
    1: "INIT",
    2: "NORMAL",
    3: "STARTUP",
    4: "COMMUNICATION_INT",
    5: "PARTNER_DOWN",
    6: "POTENTIAL_CONFLICT",
    7: "CONFLICT_DONE",
    8: "RESOLUTION_INT",
    9: "RECOVER",
    10: "RECOVER_WAIT",
    11: "RECOVER_DONE",
    12: "PAUSED",
    13: "SHUTDOWN",
}
DHCP_FAILOVER_MODE = {
    "LoadBalance": 0,
    "HotStandby": 1,
}
DHCP_FAILOVER_MODE_INV = {
    0: "LoadBalance",
    1: "HotStandby",
}
DHCP_FAILOVER_SERVER = {
    "PrimaryServer": 0,
    "SecondaryServer": 1,
}
DHCP_FAILOVER_SERVER_INV = {
    0: "PrimaryServer",
    1: "SecondaryServer",
}

###################

###### Types ######
DHCP_CONST_WCHAR_PTR = WCHAR_PTR
DHCP_IP_ADDRESS = DWORD
LPDHCP_IP_ADDRESS = Ptr("<I", DHCP_IP_ADDRESS())
DHCP_IP_MASK = DWORD
DHCP_OPTION_ID = DWORD
DHCP_CONST_DHCP_IP_ADDRESS = DHCP_IP_ADDRESS
DHCP_CONST_LPWSTR = LPWSTR
DHCP_RESUME_HANDLE = DWORD
DHCP_RESUME_HANDLE_PTR = Ptr("<I", DHCP_RESUME_HANDLE())
DHCP_CONST_BOOL = BOOL
BYTE__MAX_PATTERN_LENGTH_ = Array(BYTE, 255)
_DHCP_FIELDS_TO_SET_ = DWORD
_DHCP_SERVER_USE_RPC_FLAGS_ = DWORD
_DHCP_DEBUG_FLAGS_ = DWORD
_CLIENT_TYPE_FLAGS_ = BYTE
_V5_ADDRESS_STATE_ = BYTE
_FILTER_STATUS_FLAGS_ = DWORD

class DHCP_ADDR_PATTERN(MemStruct):
    fields = [
        ("MatchHWType", BOOL()),
        ("HWType", BYTE()),
        ("IsWildcard", BOOL()),
        ("Length", BYTE()),
        ("Pattern", BYTE__MAX_PATTERN_LENGTH_()),
    ]

DHCP_ADDR_PATTERN_PTR = Ptr("<I", DHCP_ADDR_PATTERN())
LPDHCP_ADDR_PATTERN = Ptr("<I", DHCP_ADDR_PATTERN())

class DHCP_IPV6_ADDRESS(MemStruct):
    fields = [
        ("HighOrderBits", ULONGLONG()),
        ("LowOrderBits", ULONGLONG()),
    ]

LPDHCP_IPV6_ADDRESS = Ptr("<I", DHCP_IPV6_ADDRESS())

class DHCP_IP_RANGE_V6(MemStruct):
    fields = [
        ("StartAddress", DHCP_IPV6_ADDRESS()),
        ("EndAddress", DHCP_IPV6_ADDRESS()),
    ]

DHCP_IP_RANGE_V6_PTR = Ptr("<I", DHCP_IP_RANGE_V6())

class DHCP_BINARY_DATA(MemStruct):
    fields = [
        ("DataLength", DWORD()),
        # Length is `DataLength`
        ("Data", BYTE_PTR()),
    ]

DHCP_CLIENT_UID = DHCP_BINARY_DATA
DHCP_CLIENT_UID_PTR = Ptr("<I", DHCP_CLIENT_UID())

class DHCP_IP_RESERVATION_V6(MemStruct):
    fields = [
        ("ReservedIpAddress", DHCP_IPV6_ADDRESS()),
        ("ReservedForClient", DHCP_CLIENT_UID_PTR()),
        ("InterfaceId", DWORD()),
    ]

DHCP_IP_RESERVATION_V6_PTR = Ptr("<I", DHCP_IP_RESERVATION_V6())

class DHCP_IP_RANGE(MemStruct):
    fields = [
        ("StartAddress", DHCP_IP_ADDRESS()),
        ("EndAddress", DHCP_IP_ADDRESS()),
    ]

DHCP_IP_RANGE_PTR = Ptr("<I", DHCP_IP_RANGE())
LPDHCP_IP_RANGE = Ptr("<I", DHCP_IP_RANGE())
DHCP_OPTION_DATA_TYPE = UINT

class DWORD_DWORD(MemStruct):
    fields = [
        ("DWord1", DWORD()),
        ("DWord2", DWORD()),
    ]

DHCP_OPTION_ELEMENT_UNION = Union([
    ("ByteOption", BYTE),
    ("WordOption", WORD),
    ("DWordOption", DWORD),
    ("DWordDWordOption", DWORD_DWORD),
    ("IpAddressOption", DHCP_IP_ADDRESS),
    ("StringDataOption", LPWSTR),
    ("BinaryDataOption", DHCP_BINARY_DATA),
    ("EncapsulatedDataOption", DHCP_BINARY_DATA),
    ("Ipv6AddressDataOption", LPWSTR),
])

class DHCP_OPTION_DATA_ELEMENT(MemStruct):
    fields = [
        ("OptionType", DHCP_OPTION_DATA_TYPE()),
        ("Element", DHCP_OPTION_ELEMENT_UNION()),
    ]

LPDHCP_OPTION_DATA_ELEMENT = Ptr("<I", DHCP_OPTION_DATA_ELEMENT())

class DHCP_BOOTP_IP_RANGE(MemStruct):
    fields = [
        ("StartAddress", DHCP_IP_ADDRESS()),
        ("EndAddress", DHCP_IP_ADDRESS()),
        ("BootpAllocated", ULONG()),
        ("MaxBootpAllowed", ULONG()),
    ]

DHCP_BOOTP_IP_RANGE_PTR = Ptr("<I", DHCP_BOOTP_IP_RANGE())

class DHCP_HOST_INFO(MemStruct):
    fields = [
        ("IpAddress", DHCP_IP_ADDRESS()),
        ("NetBiosName", LPWSTR()),
        ("HostName", LPWSTR()),
    ]

DHCP_HOST_INFO_PTR = Ptr("<I", DHCP_HOST_INFO())

class DHCP_IP_CLUSTER(MemStruct):
    fields = [
        ("ClusterAddress", DHCP_IP_ADDRESS()),
        ("ClusterMask", DWORD()),
    ]

DHCP_IP_CLUSTER_PTR = Ptr("<I", DHCP_IP_CLUSTER())

class DHCP_IP_RESERVATION_V4(MemStruct):
    fields = [
        ("ReservedIpAddress", DHCP_IP_ADDRESS()),
        ("ReservedForClient", DHCP_CLIENT_UID_PTR()),
        ("bAllowedClientTypes", _CLIENT_TYPE_FLAGS_()),
    ]

DHCP_IP_RESERVATION_V4_PTR = Ptr("<I", DHCP_IP_RESERVATION_V4())
DHCP_SUBNET_ELEMENT_UNION_V5 = Union([
    ("IpRange", DHCP_BOOTP_IP_RANGE_PTR),
    ("SecondaryHost", DHCP_HOST_INFO_PTR),
    ("ReservedIp", DHCP_IP_RESERVATION_V4_PTR),
    ("ExcludeIpRange", DHCP_IP_RANGE_PTR),
    ("IpUsedCluster", DHCP_IP_CLUSTER_PTR),
])
DHCP_SUBNET_ELEMENT_TYPE = UINT

class DHCP_SUBNET_ELEMENT_DATA_V5(MemStruct):
    fields = [
        ("ElementType", DHCP_SUBNET_ELEMENT_TYPE()),
        ("Element", DHCP_SUBNET_ELEMENT_UNION_V5()),
    ]

DHCP_CONST_DHCP_SUBNET_ELEMENT_DATA_V5_PTR = Ptr("<I", DHCP_SUBNET_ELEMENT_DATA_V5())
DHCP_SEARCH_INFO_TYPE = UINT
DHCP_CLIENT_SEARCH_UNION = Union([
    ("ClientIpAddress", DHCP_IP_ADDRESS),
    ("ClientHardwareAddress", DHCP_CLIENT_UID),
    ("ClientName", LPWSTR),
])

class DHCP_SEARCH_INFO(MemStruct):
    fields = [
        ("SearchType", DHCP_SEARCH_INFO_TYPE()),
        ("SearchInfo", DHCP_CLIENT_SEARCH_UNION()),
    ]

LPDHCP_SEARCH_INFO = Ptr("<I", DHCP_SEARCH_INFO())
DHCP_CONST_DHCP_SEARCH_INFO_PTR = Ptr("<I", DHCP_SEARCH_INFO())

class DHCP_RESERVED_SCOPE(MemStruct):
    fields = [
        ("ReservedIpAddress", DHCP_IP_ADDRESS()),
        ("ReservedIpSubnetAddress", DHCP_IP_ADDRESS()),
    ]

DHCP_OPTION_SCOPE_UNION = Union([
    ("DefaultScopeInfo", PVOID),
    ("GlobalScopeInfo", PVOID),
    ("SubnetScopeInfo", DHCP_IP_ADDRESS),
    ("ReservedScopeInfo", DHCP_RESERVED_SCOPE),
    ("MScopeInfo", LPWSTR),
])
DHCP_OPTION_SCOPE_TYPE = UINT

class DHCP_OPTION_SCOPE_INFO(MemStruct):
    fields = [
        ("ScopeType", DHCP_OPTION_SCOPE_TYPE()),
        ("ScopeInfo", DHCP_OPTION_SCOPE_UNION()),
    ]

LPDHCP_OPTION_SCOPE_INFO = Ptr("<I", DHCP_OPTION_SCOPE_INFO())
DHCP_CONST_DHCP_OPTION_SCOPE_INFO_PTR = Ptr("<I", DHCP_OPTION_SCOPE_INFO())

class DHCP_OPTION_DATA(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Elements", LPDHCP_OPTION_DATA_ELEMENT()),
    ]

LPDHCP_OPTION_DATA = Ptr("<I", DHCP_OPTION_DATA())
DHCP_CONST_DHCP_OPTION_DATA_PTR = Ptr("<I", DHCP_OPTION_DATA())

class DHCP_OPTION_VALUE(MemStruct):
    fields = [
        ("OptionID", DHCP_OPTION_ID()),
        ("Value", DHCP_OPTION_DATA()),
    ]

DHCP_OPTION_VALUE_PTR = Ptr("<I", DHCP_OPTION_VALUE())
LPDHCP_OPTION_VALUE = Ptr("<I", DHCP_OPTION_VALUE())
LPDHCP_OPTION_VALUE_PTR = Ptr("<I", LPDHCP_OPTION_VALUE())

class DHCP_OPTION_VALUE_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Values", LPDHCP_OPTION_VALUE()),
    ]

LPDHCP_OPTION_VALUE_ARRAY = Ptr("<I", DHCP_OPTION_VALUE_ARRAY())
LPDHCP_OPTION_VALUE_ARRAY_PTR = Ptr("<I", LPDHCP_OPTION_VALUE_ARRAY())
DHCP_CONST_DHCP_OPTION_VALUE_ARRAY_PTR = Ptr("<I", DHCP_OPTION_VALUE_ARRAY())

class _DHCP_ALL_OPTION_VALUES_s_(MemStruct):
    fields = [
        ("ClassName", LPWSTR()),
        ("VendorName", LPWSTR()),
        ("IsVendor", BOOL()),
        ("OptionsArray", LPDHCP_OPTION_VALUE_ARRAY()),
    ]

_DHCP_ALL_OPTION_VALUES_s_PTR_ = Ptr("<I", _DHCP_ALL_OPTION_VALUES_s_())

class DHCP_ALL_OPTION_VALUES(MemStruct):
    fields = [
        ("Flags", DWORD()),
        ("NumElements", DWORD()),
        ("Options", _DHCP_ALL_OPTION_VALUES_s_PTR_()),
    ]

LPDHCP_ALL_OPTION_VALUES_PTR = Ptr("<I", DHCP_ALL_OPTION_VALUES())

class DHCP_IP_RESERVATION(MemStruct):
    fields = [
        ("ReservedIpAddress", DHCP_IP_ADDRESS()),
        ("ReservedForClient", DHCP_CLIENT_UID_PTR()),
    ]

DHCP_IP_RESERVATION_PTR = Ptr("<I", DHCP_IP_RESERVATION())
DHCP_SUBNET_ELEMENT_UNION = Union([
    ("IpRange", DHCP_IP_RANGE_PTR),
    ("SecondaryHost", DHCP_HOST_INFO_PTR),
    ("ReservedIp", DHCP_IP_RESERVATION_PTR),
    ("ExcludeIpRange", DHCP_IP_RANGE_PTR),
    ("IpUsedCluster", DHCP_IP_CLUSTER_PTR),
])

class DHCP_SUBNET_ELEMENT_DATA(MemStruct):
    fields = [
        ("ElementType", DHCP_SUBNET_ELEMENT_TYPE()),
        ("Element", DHCP_SUBNET_ELEMENT_UNION()),
    ]

LPDHCP_SUBNET_ELEMENT_DATA = Ptr("<I", DHCP_SUBNET_ELEMENT_DATA())
DHCP_CONST_DHCP_SUBNET_ELEMENT_DATA_PTR = Ptr("<I", DHCP_SUBNET_ELEMENT_DATA())
DHCP_SUBNET_ELEMENT_TYPE_V6 = UINT
DHCP_SUBNET_ELEMENT_UNION_V6 = Union([
    ("IpRange", DHCP_IP_RANGE_V6_PTR),
    ("ReservedIp", DHCP_IP_RESERVATION_V6_PTR),
    ("ExcludeIpRange", DHCP_IP_RANGE_V6_PTR),
])

class DHCP_SUBNET_ELEMENT_DATA_V6(MemStruct):
    fields = [
        ("ElementType", DHCP_SUBNET_ELEMENT_TYPE_V6()),
        ("Element", DHCP_SUBNET_ELEMENT_UNION_V6()),
    ]

LPDHCP_SUBNET_ELEMENT_DATA_V6 = Ptr("<I", DHCP_SUBNET_ELEMENT_DATA_V6())
DHCP_SEARCH_INFO_TYPE_V6 = UINT
DHCP_CLIENT_SEARCH_UNION_V6 = Union([
    ("ClientIpAddress", DHCP_IPV6_ADDRESS),
    ("ClientDUID", DHCP_CLIENT_UID),
    ("ClientName", LPWSTR),
])

class DHCP_SEARCH_INFO_V6(MemStruct):
    fields = [
        ("SearchType", DHCP_SEARCH_INFO_TYPE_V6()),
        ("SearchInfo", DHCP_CLIENT_SEARCH_UNION_V6()),
    ]

LPDHCP_SEARCH_INFO_V6 = Ptr("<I", DHCP_SEARCH_INFO_V6())
DHCP_CONST_DHCP_SEARCH_INFO_V6_PTR = Ptr("<I", DHCP_SEARCH_INFO_V6())

class DHCP_RESERVED_SCOPE6(MemStruct):
    fields = [
        ("ReservedIpAddress", DHCP_IPV6_ADDRESS()),
        ("ReservedIpSubnetAddress", DHCP_IPV6_ADDRESS()),
    ]

DHCP_OPTION_SCOPE_TYPE6 = UINT
DHCP_OPTION_SCOPE_UNION6 = Union([
    ("DefaultScopeInfo", PVOID),
    ("SubnetScopeInfo", DHCP_IPV6_ADDRESS),
    ("ReservedScopeInfo", DHCP_RESERVED_SCOPE6),
])

class DHCP_OPTION_SCOPE_INFO6(MemStruct):
    fields = [
        ("ScopeType", DHCP_OPTION_SCOPE_TYPE6()),
        ("ScopeInfo", DHCP_OPTION_SCOPE_UNION6()),
    ]

LPDHCP_OPTION_SCOPE_INFO6 = Ptr("<I", DHCP_OPTION_SCOPE_INFO6())
LPDHCP_OPTION_SCOPE_INFO6_PTR = Ptr("<I", LPDHCP_OPTION_SCOPE_INFO6())
DHCP_OPTION_TYPE = UINT

class DHCP_OPTION(MemStruct):
    fields = [
        ("OptionID", DHCP_OPTION_ID()),
        ("OptionName", LPWSTR()),
        ("OptionComment", LPWSTR()),
        ("DefaultValue", DHCP_OPTION_DATA()),
        ("OptionType", DHCP_OPTION_TYPE()),
    ]

LPDHCP_OPTION = Ptr("<I", DHCP_OPTION())
LPDHCP_OPTION_PTR = Ptr("<I", LPDHCP_OPTION())
DHCP_CONST_DHCP_OPTION_PTR = Ptr("<I", DHCP_OPTION())

class DHCP_OPTION_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Options", LPDHCP_OPTION()),
    ]

LPDHCP_OPTION_ARRAY = Ptr("<I", DHCP_OPTION_ARRAY())
LPDHCP_OPTION_ARRAY_PTR = Ptr("<I", LPDHCP_OPTION_ARRAY())

class _DHCP_ALL_OPTIONS_s_(MemStruct):
    fields = [
        ("Option", DHCP_OPTION()),
        ("VendorName", LPWSTR()),
        ("ClassName", LPWSTR()),
    ]

_DHCP_ALL_OPTIONS_s_PTR_ = Ptr("<I", _DHCP_ALL_OPTIONS_s_())

class DHCP_ALL_OPTIONS(MemStruct):
    fields = [
        ("Flags", DWORD()),
        ("NonVendorOptions", LPDHCP_OPTION_ARRAY()),
        ("NumVendorOptions", DWORD()),
        ("VendorOptions", _DHCP_ALL_OPTIONS_s_PTR_()),
    ]

LPDHCP_ALL_OPTIONS = Ptr("<I", DHCP_ALL_OPTIONS())
LPDHCP_ALL_OPTIONS_PTR = Ptr("<I", LPDHCP_ALL_OPTIONS())
DHCP_FILTER_LIST_TYPE = UINT

class DHCP_FILTER_ADD_INFO(MemStruct):
    fields = [
        ("AddrPatt", DHCP_ADDR_PATTERN()),
        ("Comment", LPWSTR()),
        ("ListType", DHCP_FILTER_LIST_TYPE()),
    ]

DHCP_FILTER_ADD_INFO_PTR = Ptr("<I", DHCP_FILTER_ADD_INFO())

class DHCP_FILTER_RECORD(MemStruct):
    fields = [
        ("AddrPatt", DHCP_ADDR_PATTERN()),
        ("Comment", LPWSTR()),
    ]

LPDHCP_FILTER_RECORD = Ptr("<I", DHCP_FILTER_RECORD())

class DATE_TIME(MemStruct):
    fields = [
        ("dwLowDateTime", DWORD()),
        ("dwHighDateTime", DWORD()),
    ]


class DHCP_CLASS_INFO(MemStruct):
    fields = [
        ("ClassName", LPWSTR()),
        ("ClassComment", LPWSTR()),
        ("ClassDataLength", DWORD()),
        ("IsVendor", BOOL()),
        ("Flags", DWORD()),
        ("ClassData", LPBYTE()),
    ]

LPDHCP_CLASS_INFO = Ptr("<I", DHCP_CLASS_INFO())
LPDHCP_CLASS_INFO_PTR = Ptr("<I", LPDHCP_CLASS_INFO())

class DHCP_CLIENT_INFO(MemStruct):
    fields = [
        ("ClientIpAddress", DHCP_IP_ADDRESS()),
        ("SubnetMask", DHCP_IP_MASK()),
        ("ClientHardwareAddress", DHCP_CLIENT_UID()),
        ("ClientName", LPWSTR()),
        ("ClientComment", LPWSTR()),
        ("ClientLeaseExpires", DATE_TIME()),
        ("OwnerHost", DHCP_HOST_INFO()),
    ]

DHCP_CONST_DHCP_CLIENT_INFO_PTR = Ptr("<I", DHCP_CLIENT_INFO())
LPDHCP_CLIENT_INFO = Ptr("<I", DHCP_CLIENT_INFO())
LPDHCP_CLIENT_INFO_PTR = Ptr("<I", LPDHCP_CLIENT_INFO())

class DHCP_CLIENT_INFO_V4(MemStruct):
    fields = [
        ("ClientIpAddress", DHCP_IP_ADDRESS()),
        ("SubnetMask", DHCP_IP_MASK()),
        ("ClientHardwareAddress", DHCP_CLIENT_UID()),
        ("ClientName", LPWSTR()),
        ("ClientComment", LPWSTR()),
        ("ClientLeaseExpires", DATE_TIME()),
        ("OwnerHost", DHCP_HOST_INFO()),
        ("bClientType", _CLIENT_TYPE_FLAGS_()),
    ]

DHCP_CONST_DHCP_CLIENT_INFO_V4_PTR = Ptr("<I", DHCP_CLIENT_INFO_V4())
LPDHCP_CLIENT_INFO_V4_PTR = Ptr("<I", DHCP_CLIENT_INFO_V4())
QuarantineStatus = UINT

class DHCP_CLIENT_INFO_VQ(MemStruct):
    fields = [
        ("ClientIpAddress", DHCP_IP_ADDRESS()),
        ("SubnetMask", DHCP_IP_MASK()),
        ("ClientHardwareAddress", DHCP_CLIENT_UID()),
        ("ClientName", LPWSTR()),
        ("ClientComment", LPWSTR()),
        ("ClientLeaseExpires", DATE_TIME()),
        ("OwnerHost", DHCP_HOST_INFO()),
        ("bClientType", _CLIENT_TYPE_FLAGS_()),
        ("AddressState", _V5_ADDRESS_STATE_()),
        ("Status", QuarantineStatus()),
        ("ProbationEnds", DATE_TIME()),
        ("QuarantineCapable", BOOL()),
    ]

LPDHCP_CLIENT_INFO_VQ = Ptr("<I", DHCP_CLIENT_INFO_VQ())
LPDHCP_CLIENT_INFO_VQ_PTR = Ptr("<I", LPDHCP_CLIENT_INFO_VQ())
DHCP_SUBNET_STATE = UINT

class DHCP_SUBNET_INFO(MemStruct):
    fields = [
        ("SubnetAddress", DHCP_IP_ADDRESS()),
        ("SubnetMask", DHCP_IP_MASK()),
        ("SubnetName", LPWSTR()),
        ("SubnetComment", LPWSTR()),
        ("PrimaryHost", DHCP_HOST_INFO()),
        ("SubnetState", DHCP_SUBNET_STATE()),
    ]

DHCP_CONST_DHCP_SUBNET_INFO_PTR = Ptr("<I", DHCP_SUBNET_INFO())
LPDHCP_SUBNET_INFO = Ptr("<I", DHCP_SUBNET_INFO())
LPDHCP_SUBNET_INFO_PTR = Ptr("<I", LPDHCP_SUBNET_INFO())

class DHCP_SUBNET_INFO_VQ(MemStruct):
    fields = [
        ("SubnetAddress", DHCP_IP_ADDRESS()),
        ("SubnetMask", DHCP_IP_MASK()),
        ("SubnetName", LPWSTR()),
        ("SubnetComment", LPWSTR()),
        ("PrimaryHost", DHCP_HOST_INFO()),
        ("SubnetState", DHCP_SUBNET_STATE()),
        ("QuarantineOn", DWORD()),
        ("Reserved1", DWORD()),
        ("Reserved2", DWORD()),
        ("Reserved3", INT64()),
        ("Reserved4", INT64()),
    ]

DHCP_CONST_DHCP_SUBNET_INFO_VQ_PTR = Ptr("<I", DHCP_SUBNET_INFO_VQ())
LPDHCP_SUBNET_INFO_VQ = Ptr("<I", DHCP_SUBNET_INFO_VQ())
LPDHCP_SUBNET_INFO_VQ_PTR = Ptr("<I", LPDHCP_SUBNET_INFO_VQ())
DHCP_FORCE_FLAG = UINT

class DHCP_CLASS_INFO_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Classes", LPDHCP_CLASS_INFO()),
    ]

LPDHCP_CLASS_INFO_ARRAY = Ptr("<I", DHCP_CLASS_INFO_ARRAY())
LPDHCP_CLASS_INFO_ARRAY_PTR = Ptr("<I", LPDHCP_CLASS_INFO_ARRAY())

class DHCP_FILTER_ENUM_INFO(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("pEnumRecords", LPDHCP_FILTER_RECORD()),
    ]

LPDHCP_FILTER_ENUM_INFO = Ptr("<I", DHCP_FILTER_ENUM_INFO())
LPDHCP_FILTER_ENUM_INFO_PTR = Ptr("<I", LPDHCP_FILTER_ENUM_INFO())

class DHCPDS_SERVER(MemStruct):
    fields = [
        ("Version", DWORD()),
        ("ServerName", LPWSTR()),
        ("ServerAddress", DWORD()),
        ("Flags", DWORD()),
        ("State", DWORD()),
        ("DsLocation", LPWSTR()),
        ("DsLocType", DWORD()),
    ]

LPDHCPDS_SERVER = Ptr("<I", DHCPDS_SERVER())
LPDHCP_SERVER_INFO = Ptr("<I", DHCPDS_SERVER())

class DHCPDS_SERVERS(MemStruct):
    fields = [
        ("Flags", DWORD()),
        ("NumElements", DWORD()),
        ("Servers", LPDHCPDS_SERVER()),
    ]

LPDHCP_SERVER_INFO_ARRAY = Ptr("<I", DHCPDS_SERVERS())
LPDHCP_SERVER_INFO_ARRAY_PTR = Ptr("<I", LPDHCP_SERVER_INFO_ARRAY())

class DHCP_CLIENT_INFO_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Clients", LPDHCP_CLIENT_INFO_PTR()),
    ]

LPDHCP_CLIENT_INFO_ARRAY = Ptr("<I", DHCP_CLIENT_INFO_ARRAY())
LPDHCP_CLIENT_INFO_ARRAY_PTR = Ptr("<I", LPDHCP_CLIENT_INFO_ARRAY())

class DHCP_CLIENT_INFO_V5(MemStruct):
    fields = [
        ("ClientIpAddress", DHCP_IP_ADDRESS()),
        ("SubnetMask", DHCP_IP_MASK()),
        ("ClientHardwareAddress", DHCP_CLIENT_UID()),
        ("ClientName", LPWSTR()),
        ("ClientComment", LPWSTR()),
        ("ClientLeaseExpires", DATE_TIME()),
        ("OwnerHost", DHCP_HOST_INFO()),
        ("bClientType", _CLIENT_TYPE_FLAGS_()),
        ("AddressState", _V5_ADDRESS_STATE_()),
    ]

LPDHCP_CLIENT_INFO_V5 = Ptr("<I", DHCP_CLIENT_INFO_V5())
LPDHCP_CLIENT_INFO_V5_PTR = Ptr("<I", LPDHCP_CLIENT_INFO_V5())

class DHCP_CLIENT_INFO_ARRAY_V5(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Clients", LPDHCP_CLIENT_INFO_V5_PTR()),
    ]

LPDHCP_CLIENT_INFO_ARRAY_V5 = Ptr("<I", DHCP_CLIENT_INFO_ARRAY_V5())
LPDHCP_CLIENT_INFO_ARRAY_V5_PTR = Ptr("<I", LPDHCP_CLIENT_INFO_ARRAY_V5())

class DHCP_CLIENT_INFO_ARRAY_VQ(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Clients", LPDHCP_CLIENT_INFO_VQ_PTR()),
    ]

LPDHCP_CLIENT_INFO_ARRAY_VQ = Ptr("<I", DHCP_CLIENT_INFO_ARRAY_VQ())
LPDHCP_CLIENT_INFO_ARRAY_VQ_PTR = Ptr("<I", LPDHCP_CLIENT_INFO_ARRAY_VQ())

class DHCP_CLIENT_FILTER_STATUS_INFO(MemStruct):
    fields = [
        ("ClientIpAddress", DHCP_IP_ADDRESS()),
        ("SubnetMask", DHCP_IP_MASK()),
        ("ClientHardwareAddress", DHCP_CLIENT_UID()),
        ("ClientName", LPWSTR()),
        ("ClientComment", LPWSTR()),
        ("ClientLeaseExpires", DATE_TIME()),
        ("OwnerHost", DHCP_HOST_INFO()),
        ("bClientType", _CLIENT_TYPE_FLAGS_()),
        ("AddressState", _V5_ADDRESS_STATE_()),
        ("Status", QuarantineStatus()),
        ("ProbationEnds", DATE_TIME()),
        ("QuarantineCapable", BOOL()),
        ("FilterStatus", _FILTER_STATUS_FLAGS_()),
    ]

LPDHCP_CLIENT_FILTER_STATUS_INFO = Ptr("<I", DHCP_CLIENT_FILTER_STATUS_INFO())
LPDHCP_CLIENT_FILTER_STATUS_INFO_PTR = Ptr("<I", LPDHCP_CLIENT_FILTER_STATUS_INFO())

class DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Clients", LPDHCP_CLIENT_FILTER_STATUS_INFO_PTR()),
    ]

LPDHCP_CLIENT_FILTER_STATUS_INFO_ARRAY = Ptr("<I", DHCP_CLIENT_FILTER_STATUS_INFO_ARRAY())
LPDHCP_CLIENT_FILTER_STATUS_INFO_ARRAY_PTR = Ptr("<I", LPDHCP_CLIENT_FILTER_STATUS_INFO_ARRAY())

class DHCP_SUBNET_ELEMENT_INFO_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Elements", LPDHCP_SUBNET_ELEMENT_DATA()),
    ]

LPDHCP_SUBNET_ELEMENT_INFO_ARRAY = Ptr("<I", DHCP_SUBNET_ELEMENT_INFO_ARRAY())
LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_PTR = Ptr("<I", LPDHCP_SUBNET_ELEMENT_INFO_ARRAY())

class DHCP_IP_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Elements", LPDHCP_IP_ADDRESS()),
    ]

LPDHCP_IP_ARRAY = Ptr("<I", DHCP_IP_ARRAY())
LPDHCP_IP_ARRAY_PTR = Ptr("<I", LPDHCP_IP_ARRAY())

class DHCP_FILTER_GLOBAL_INFO(MemStruct):
    fields = [
        ("EnforceAllowList", BOOL()),
        ("EnforceDenyList", BOOL()),
    ]

DHCP_FILTER_GLOBAL_INFO_PTR = Ptr("<I", DHCP_FILTER_GLOBAL_INFO())

class SCOPE_MIB_INFO_V5(MemStruct):
    fields = [
        ("Subnet", DHCP_IP_ADDRESS()),
        ("NumAddressesInuse", DWORD()),
        ("NumAddressesFree", DWORD()),
        ("NumPendingOffers", DWORD()),
    ]

LPSCOPE_MIB_INFO_V5 = Ptr("<I", SCOPE_MIB_INFO_V5())

class DHCP_MIB_INFO_V5(MemStruct):
    fields = [
        ("Discovers", DWORD()),
        ("Offers", DWORD()),
        ("Requests", DWORD()),
        ("Acks", DWORD()),
        ("Naks", DWORD()),
        ("Declines", DWORD()),
        ("Releases", DWORD()),
        ("ServerStartTime", DATE_TIME()),
        ("QtnNumLeases", DWORD()),
        ("QtnPctQtnLeases", DWORD()),
        ("QtnProbationLeases", DWORD()),
        ("QtnNonQtnLeases", DWORD()),
        ("QtnExemptLeases", DWORD()),
        ("QtnCapableClients", DWORD()),
        ("QtnIASErrors", DWORD()),
        ("DelayedOffers", DWORD()),
        ("ScopesWithDelayedOffers", DWORD()),
        ("Scopes", DWORD()),
        ("ScopeInfo", LPSCOPE_MIB_INFO_V5()),
    ]

LPDHCP_MIB_INFO_V5 = Ptr("<I", DHCP_MIB_INFO_V5())
LPDHCP_MIB_INFO_V5_PTR = Ptr("<I", LPDHCP_MIB_INFO_V5())

class DHCP_BIND_ELEMENT(MemStruct):
    fields = [
        ("Flags", ULONG()),
        ("fBoundToDHCPServer", BOOL()),
        ("AdapterPrimaryAddress", DHCP_IP_ADDRESS()),
        ("AdapterSubnetAddress", DHCP_IP_ADDRESS()),
        ("IfDescription", LPWSTR()),
        ("IfIdSize", ULONG()),
        ("IfId", LPBYTE()),
    ]

LPDHCP_BIND_ELEMENT = Ptr("<I", DHCP_BIND_ELEMENT())

class DHCP_BIND_ELEMENT_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Elements", LPDHCP_BIND_ELEMENT()),
    ]

LPDHCP_BIND_ELEMENT_ARRAY = Ptr("<I", DHCP_BIND_ELEMENT_ARRAY())
LPDHCP_BIND_ELEMENT_ARRAY_PTR = Ptr("<I", LPDHCP_BIND_ELEMENT_ARRAY())

class DHCP_SUPER_SCOPE_TABLE_ENTRY(MemStruct):
    fields = [
        ("SubnetAddress", DHCP_IP_ADDRESS()),
        ("SuperScopeNumber", DWORD()),
        ("NextInSuperScope", DWORD()),
        ("SuperScopeName", LPWSTR()),
    ]

LPDHCP_SUPER_SCOPE_TABLE = Ptr("<I", DHCP_SUPER_SCOPE_TABLE_ENTRY())
LPDHCP_SUPER_SCOPE_TABLE_PTR = Ptr("<I", LPDHCP_SUPER_SCOPE_TABLE())

class DHCP_SERVER_CONFIG_INFO_VQ(MemStruct):
    fields = [
        ("APIProtocolSupport", _DHCP_SERVER_USE_RPC_FLAGS_()),
        ("DatabaseName", LPWSTR()),
        ("DatabasePath", LPWSTR()),
        ("BackupPath", LPWSTR()),
        ("BackupInterval", DWORD()),
        ("DatabaseLoggingFlag", DWORD()),
        ("RestoreFlag", DWORD()),
        ("DatabaseCleanupInterval", DWORD()),
        ("DebugFlag", _DHCP_DEBUG_FLAGS_()),
        ("dwPingRetries", DWORD()),
        ("cbBootTableString", DWORD()),
        ("wszBootTableString", WCHAR_PTR()),
        ("fAuditLog", BOOL()),
        ("QuarantineOn", BOOL()),
        ("QuarDefFail", DWORD()),
        ("QuarRuntimeStatus", BOOL()),
    ]

LPDHCP_SERVER_CONFIG_INFO_VQ = Ptr("<I", DHCP_SERVER_CONFIG_INFO_VQ())
LPDHCP_SERVER_CONFIG_INFO_VQ_PTR = Ptr("<I", LPDHCP_SERVER_CONFIG_INFO_VQ())

class DHCP_SERVER_CONFIG_INFO_V4(MemStruct):
    fields = [
        ("APIProtocolSupport", _DHCP_SERVER_USE_RPC_FLAGS_()),
        ("DatabaseName", LPWSTR()),
        ("DatabasePath", LPWSTR()),
        ("BackupPath", LPWSTR()),
        ("BackupInterval", DWORD()),
        ("DatabaseLoggingFlag", DWORD()),
        ("RestoreFlag", DWORD()),
        ("DatabaseCleanupInterval", DWORD()),
        ("DebugFlag", _DHCP_DEBUG_FLAGS_()),
        ("dwPingRetries", DWORD()),
        ("cbBootTableString", DWORD()),
        ("wszBootTableString", WCHAR_PTR()),
        ("fAuditLog", BOOL()),
    ]

LPDHCP_SERVER_CONFIG_INFO_V4 = Ptr("<I", DHCP_SERVER_CONFIG_INFO_V4())
LPDHCP_SERVER_CONFIG_INFO_V4_PTR = Ptr("<I", LPDHCP_SERVER_CONFIG_INFO_V4())
DHCP_RESUME_IPV6_HANDLE = DHCP_IPV6_ADDRESS
DHCP_RESUME_IPV6_HANDLE_PTR = Ptr("<I", DHCP_RESUME_IPV6_HANDLE())

class DHCP_CLASS_INFO_V6(MemStruct):
    fields = [
        ("ClassName", LPWSTR()),
        ("ClassComment", LPWSTR()),
        ("ClassDataLength", DWORD()),
        ("IsVendor", BOOL()),
        ("EnterpriseNumber", DWORD()),
        ("Flags", DWORD()),
        ("ClassData", LPBYTE()),
    ]

LPDHCP_CLASS_INFO_V6 = Ptr("<I", DHCP_CLASS_INFO_V6())

class DHCP_SUBNET_INFO_V6(MemStruct):
    fields = [
        ("SubnetAddress", DHCP_IPV6_ADDRESS()),
        ("Prefix", ULONG()),
        ("Preference", USHORT()),
        ("SubnetName", LPWSTR()),
        ("SubnetComment", LPWSTR()),
        ("State", DWORD()),
        ("ScopeId", DWORD()),
    ]

LPDHCP_SUBNET_INFO_V6 = Ptr("<I", DHCP_SUBNET_INFO_V6())
LPDHCP_SUBNET_INFO_V6_PTR = Ptr("<I", LPDHCP_SUBNET_INFO_V6())

class DHCP_CLASS_INFO_ARRAY_V6(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Classes", LPDHCP_CLASS_INFO_V6()),
    ]

LPDHCP_CLASS_INFO_ARRAY_V6 = Ptr("<I", DHCP_CLASS_INFO_ARRAY_V6())
LPDHCP_CLASS_INFO_ARRAY_V6_PTR = Ptr("<I", LPDHCP_CLASS_INFO_ARRAY_V6())

class DHCPV6_IP_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Elements", LPDHCP_IPV6_ADDRESS()),
    ]

LPDHCPV6_IP_ARRAY = Ptr("<I", DHCPV6_IP_ARRAY())
LPDHCPV6_IP_ARRAY_PTR = Ptr("<I", LPDHCPV6_IP_ARRAY())

class DHCP_HOST_INFO_V6(MemStruct):
    fields = [
        ("IpAddress", DHCP_IPV6_ADDRESS()),
        ("NetBiosName", LPWSTR()),
        ("HostName", LPWSTR()),
    ]


class DHCP_CLIENT_INFO_V6(MemStruct):
    fields = [
        ("ClientIpAddress", DHCP_IPV6_ADDRESS()),
        ("ClientDUID", DHCP_CLIENT_UID()),
        ("AddressType", DWORD()),
        ("IAID", DWORD()),
        ("ClientName", LPWSTR()),
        ("ClientComment", LPWSTR()),
        ("ClientValidLeaseExpires", DATE_TIME()),
        ("ClientPrefLeaseExpires", DATE_TIME()),
        ("OwnerHost", DHCP_HOST_INFO_V6()),
    ]

LPDHCP_CLIENT_INFO_V6 = Ptr("<I", DHCP_CLIENT_INFO_V6())
LPDHCP_CLIENT_INFO_V6_PTR = Ptr("<I", LPDHCP_CLIENT_INFO_V6())
DHCP_CONST_LPDHCP_CLIENT_INFO_V6 = Ptr("<I", DHCP_CLIENT_INFO_V6())

class DHCP_CLIENT_INFO_ARRAY_V6(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Clients", LPDHCP_CLIENT_INFO_V6_PTR()),
    ]

LPDHCP_CLIENT_INFO_ARRAY_V6 = Ptr("<I", DHCP_CLIENT_INFO_ARRAY_V6())
LPDHCP_CLIENT_INFO_ARRAY_V6_PTR = Ptr("<I", LPDHCP_CLIENT_INFO_ARRAY_V6())

class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Elements", LPDHCP_SUBNET_ELEMENT_DATA_V6()),
    ]

LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V6 = Ptr("<I", DHCP_SUBNET_ELEMENT_INFO_ARRAY_V6())
LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V6_PTR = Ptr("<I", LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V6())

class SCOPE_MIB_INFO_V6(MemStruct):
    fields = [
        ("Subnet", DHCP_IPV6_ADDRESS()),
        ("NumAddressesInuse", ULONGLONG()),
        ("NumAddressesFree", ULONGLONG()),
        ("NumPendingAdvertises", ULONGLONG()),
    ]

LPSCOPE_MIB_INFO_V6 = Ptr("<I", SCOPE_MIB_INFO_V6())

class DHCP_MIB_INFO_V6(MemStruct):
    fields = [
        ("Solicits", DWORD()),
        ("Advertises", DWORD()),
        ("Requests", DWORD()),
        ("Renews", DWORD()),
        ("Rebinds", DWORD()),
        ("Replies", DWORD()),
        ("Confirms", DWORD()),
        ("Declines", DWORD()),
        ("Releases", DWORD()),
        ("Informs", DWORD()),
        ("ServerStartTime", DATE_TIME()),
        ("Scopes", DWORD()),
        ("ScopeInfo", LPSCOPE_MIB_INFO_V6()),
    ]

LPDHCP_MIB_INFO_V6 = Ptr("<I", DHCP_MIB_INFO_V6())
LPDHCP_MIB_INFO_V6_PTR = Ptr("<I", LPDHCP_MIB_INFO_V6())

class DHCPV6_BIND_ELEMENT(MemStruct):
    fields = [
        ("Flags", ULONG()),
        ("fBoundToDHCPServer", BOOL()),
        ("AdapterPrimaryAddress", DHCP_IPV6_ADDRESS()),
        ("AdapterSubnetAddress", DHCP_IPV6_ADDRESS()),
        ("IfDescription", LPWSTR()),
        ("IpV6IfIndex", DWORD()),
        ("IfIdSize", ULONG()),
        ("IfId", LPBYTE()),
    ]

LPDHCPV6_BIND_ELEMENT = Ptr("<I", DHCPV6_BIND_ELEMENT())

class DHCPV6_BIND_ELEMENT_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Elements", LPDHCPV6_BIND_ELEMENT()),
    ]

LPDHCPV6_BIND_ELEMENT_ARRAY = Ptr("<I", DHCPV6_BIND_ELEMENT_ARRAY())
LPDHCPV6_BIND_ELEMENT_ARRAY_PTR = Ptr("<I", LPDHCPV6_BIND_ELEMENT_ARRAY())

class DHCP_SERVER_CONFIG_INFO_V6(MemStruct):
    fields = [
        ("UnicastFlag", BOOL()),
        ("RapidCommitFlag", BOOL()),
        ("PreferredLifetime", DWORD()),
        ("ValidLifetime", DWORD()),
        ("T1", DWORD()),
        ("T2", DWORD()),
        ("PreferredLifetimeIATA", DWORD()),
        ("ValidLifetimeIATA", DWORD()),
        ("fAuditLog", BOOL()),
    ]

LPDHCP_SERVER_CONFIG_INFO_V6 = Ptr("<I", DHCP_SERVER_CONFIG_INFO_V6())
LPDHCP_SERVER_CONFIG_INFO_V6_PTR = Ptr("<I", LPDHCP_SERVER_CONFIG_INFO_V6())
DHCP_POL_ATTR_TYPE = UINT
DHCP_POL_COMPARATOR = UINT
DHCP_POL_LOGIC_OPER = UINT

class DHCP_POL_COND(MemStruct):
    fields = [
        ("ParentExpr", DWORD()),
        ("Type", DHCP_POL_ATTR_TYPE()),
        ("OptionID", DWORD()),
        ("SubOptionID", DWORD()),
        ("VendorName", LPWSTR()),
        ("Operator", DHCP_POL_COMPARATOR()),
        # Length is `ValueLength`
        ("Value", LPBYTE()),
        ("ValueLength", DWORD()),
    ]

LPDHCP_POL_COND = Ptr("<I", DHCP_POL_COND())

class DHCP_POL_COND_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Elements", LPDHCP_POL_COND()),
    ]

LPDHCP_POL_COND_ARRAY = Ptr("<I", DHCP_POL_COND_ARRAY())

class DHCP_POL_EXPR(MemStruct):
    fields = [
        ("ParentExpr", DWORD()),
        ("Operator", DHCP_POL_LOGIC_OPER()),
    ]

LPDHCP_POL_EXPR = Ptr("<I", DHCP_POL_EXPR())

class DHCP_POL_EXPR_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Elements", LPDHCP_POL_EXPR()),
    ]

LPDHCP_POL_EXPR_ARRAY = Ptr("<I", DHCP_POL_EXPR_ARRAY())

class DHCP_IP_RANGE_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Elements", LPDHCP_IP_RANGE()),
    ]

LPDHCP_IP_RANGE_ARRAY = Ptr("<I", DHCP_IP_RANGE_ARRAY())

class DHCP_POLICY(MemStruct):
    fields = [
        ("PolicyName", LPWSTR()),
        ("IsGlobalPolicy", BOOL()),
        ("Subnet", DHCP_IP_ADDRESS()),
        ("ProcessingOrder", DWORD()),
        ("Conditions", LPDHCP_POL_COND_ARRAY()),
        ("Expressions", LPDHCP_POL_EXPR_ARRAY()),
        ("Ranges", LPDHCP_IP_RANGE_ARRAY()),
        ("Description", LPWSTR()),
        ("Enabled", BOOL()),
    ]

LPDHCP_POLICY = Ptr("<I", DHCP_POLICY())
LPDHCP_POLICY_PTR = Ptr("<I", LPDHCP_POLICY())
DHCP_ATTRIB_ID = UINT
DHCP_ATTRIB_ID___ = Ptr("<I", DHCP_ATTRIB_ID())

class DHCP_SERVER_SPECIFIC_STRINGS(MemStruct):
    fields = [
        ("DefaultVendorClassName", LPWSTR()),
        ("DefaultUserClassName", LPWSTR()),
    ]

LPDHCP_SERVER_SPECIFIC_STRINGS = Ptr("<I", DHCP_SERVER_SPECIFIC_STRINGS())
LPDHCP_SERVER_SPECIFIC_STRINGS_PTR = Ptr("<I", LPDHCP_SERVER_SPECIFIC_STRINGS())
DHCP_SCAN_FLAG = UINT

class DHCP_SCAN_ITEM(MemStruct):
    fields = [
        ("IpAddress", DHCP_IP_ADDRESS()),
        ("ScanFlag", DHCP_SCAN_FLAG()),
    ]

DHCP_SCAN_ITEM_PTR = Ptr("<I", DHCP_SCAN_ITEM())

class DHCP_SCAN_LIST(MemStruct):
    fields = [
        ("NumScanItems", DWORD()),
        ("ScanItems", DHCP_SCAN_ITEM_PTR()),
    ]

LPDHCP_SCAN_LIST = Ptr("<I", DHCP_SCAN_LIST())
LPDHCP_SCAN_LIST_PTR = Ptr("<I", LPDHCP_SCAN_LIST())

class DHCP_CLIENT_INFO_ARRAY_V4(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Clients", LPDHCP_CLIENT_INFO_V4_PTR()),
    ]

LPDHCP_CLIENT_INFO_ARRAY_V4 = Ptr("<I", DHCP_CLIENT_INFO_ARRAY_V4())
LPDHCP_CLIENT_INFO_ARRAY_V4_PTR = Ptr("<I", LPDHCP_CLIENT_INFO_ARRAY_V4())
DHCP_SUBNET_ELEMENT_UNION_V4 = Union([
    ("IpRange", DHCP_IP_RANGE_PTR),
    ("SecondaryHost", DHCP_HOST_INFO_PTR),
    ("ReservedIp", DHCP_IP_RESERVATION_V4_PTR),
    ("ExcludeIpRange", DHCP_IP_RANGE_PTR),
    ("IpUsedCluster", DHCP_IP_CLUSTER_PTR),
])

class DHCP_SUBNET_ELEMENT_DATA_V4(MemStruct):
    fields = [
        ("ElementType", DHCP_SUBNET_ELEMENT_TYPE()),
        ("Element", DHCP_SUBNET_ELEMENT_UNION_V4()),
    ]

LPDHCP_SUBNET_ELEMENT_DATA_V4 = Ptr("<I", DHCP_SUBNET_ELEMENT_DATA_V4())
DHCP_CONST_DHCP_SUBNET_ELEMENT_DATA_V4_PTR = Ptr("<I", DHCP_SUBNET_ELEMENT_DATA_V4())

class DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Elements", LPDHCP_SUBNET_ELEMENT_DATA_V4()),
    ]

LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V4 = Ptr("<I", DHCP_SUBNET_ELEMENT_INFO_ARRAY_V4())
LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V4_PTR = Ptr("<I", LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V4())

class DHCP_IP_RESERVATION_INFO(MemStruct):
    fields = [
        ("ReservedIpAddress", DHCP_IP_ADDRESS()),
        ("ReservedForClient", DHCP_CLIENT_UID()),
        ("ReservedClientName", LPWSTR()),
        ("ReservedClientDesc", LPWSTR()),
        ("bAllowedClientTypes", _CLIENT_TYPE_FLAGS_()),
        ("fOptionsPresent", BYTE()),
    ]

LPDHCP_IP_RESERVATION_INFO = Ptr("<I", DHCP_IP_RESERVATION_INFO())
LPDHCP_IP_RESERVATION_INFO_PTR = Ptr("<I", LPDHCP_IP_RESERVATION_INFO())

class DHCP_RESERVATION_INFO_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Elements", LPDHCP_IP_RESERVATION_INFO_PTR()),
    ]

LPDHCP_RESERVATION_INFO_ARRAY = Ptr("<I", DHCP_RESERVATION_INFO_ARRAY())
LPDHCP_RESERVATION_INFO_ARRAY_PTR = Ptr("<I", LPDHCP_RESERVATION_INFO_ARRAY())

class DHCP_POLICY_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Elements", LPDHCP_POLICY()),
    ]

LPDHCP_POLICY_ARRAY = Ptr("<I", DHCP_POLICY_ARRAY())
LPDHCP_POLICY_ARRAY_PTR = Ptr("<I", LPDHCP_POLICY_ARRAY())

class DHCPV6_STATELESS_SCOPE_STATS(MemStruct):
    fields = [
        ("SubnetAddress", DHCP_IPV6_ADDRESS()),
        ("NumStatelessClientsAdded", ULONGLONG()),
        ("NumStatelessClientsRemoved", ULONGLONG()),
    ]

LPDHCPV6_STATELESS_SCOPE_STATS = Ptr("<I", DHCPV6_STATELESS_SCOPE_STATS())

class DHCPV6_STATELESS_STATS(MemStruct):
    fields = [
        ("NumScopes", DWORD()),
        ("ScopeStats", LPDHCPV6_STATELESS_SCOPE_STATS()),
    ]

LPDHCPV6_STATELESS_STATS = Ptr("<I", DHCPV6_STATELESS_STATS())
LPDHCPV6_STATELESS_STATS_PTR = Ptr("<I", LPDHCPV6_STATELESS_STATS())

class DHCPV6_STATELESS_PARAMS(MemStruct):
    fields = [
        ("Status", BOOL()),
        ("PurgeInterval", DWORD()),
    ]

LPDHCPV6_STATELESS_PARAMS = Ptr("<I", DHCPV6_STATELESS_PARAMS())
LPDHCPV6_STATELESS_PARAMS_PTR = Ptr("<I", LPDHCPV6_STATELESS_PARAMS())

class DHCP_OPTION_LIST(MemStruct):
    fields = [
        ("NumOptions", DWORD()),
        ("Options", DHCP_OPTION_VALUE_PTR()),
    ]

LPDHCP_OPTION_LIST = Ptr("<I", DHCP_OPTION_LIST())
LPDHCP_OPTION_LIST_PTR = Ptr("<I", LPDHCP_OPTION_LIST())

class DHCP_SERVER_CONFIG_INFO(MemStruct):
    fields = [
        ("APIProtocolSupport", _DHCP_SERVER_USE_RPC_FLAGS_()),
        ("DatabaseName", LPWSTR()),
        ("DatabasePath", LPWSTR()),
        ("BackupPath", LPWSTR()),
        ("BackupInterval", DWORD()),
        ("DatabaseLoggingFlag", DWORD()),
        ("RestoreFlag", DWORD()),
        ("DatabaseCleanupInterval", DWORD()),
        ("DebugFlag", _DHCP_DEBUG_FLAGS_()),
    ]

LPDHCP_SERVER_CONFIG_INFO = Ptr("<I", DHCP_SERVER_CONFIG_INFO())
LPDHCP_SERVER_CONFIG_INFO_PTR = Ptr("<I", LPDHCP_SERVER_CONFIG_INFO())
_DHCP_ATTRIB_TYPE_ = ULONG
_DHCP_ATTRIB_u_ = Union([
    ("DhcpAttribBool", BOOL),
    ("DhcpAttribUlong", ULONG),
])

class DHCP_ATTRIB(MemStruct):
    fields = [
        ("DhcpAttribId", DHCP_ATTRIB_ID()),
        ("DhcpAttribType", _DHCP_ATTRIB_TYPE_()),
        (None, _DHCP_ATTRIB_u_()),
    ]

LPDHCP_ATTRIB = Ptr("<I", DHCP_ATTRIB())
LPDHCP_ATTRIB_PTR = Ptr("<I", LPDHCP_ATTRIB())

class DHCP_ATTRIB_ARRAY(MemStruct):
    fields = [
        ("NumElements", ULONG()),
        ("DhcpAttribs", LPDHCP_ATTRIB()),
    ]

LPDHCP_ATTRIB_ARRAY = Ptr("<I", DHCP_ATTRIB_ARRAY())
LPDHCP_ATTRIB_ARRAY_PTR = Ptr("<I", LPDHCP_ATTRIB_ARRAY())
FSM_STATE = UINT
DHCP_FAILOVER_MODE = UINT
DHCP_FAILOVER_SERVER = UINT

class DHCP_FAILOVER_RELATIONSHIP(MemStruct):
    fields = [
        ("PrimaryServer", DHCP_IP_ADDRESS()),
        ("SecondaryServer", DHCP_IP_ADDRESS()),
        ("Mode", DHCP_FAILOVER_MODE()),
        ("ServerType", DHCP_FAILOVER_SERVER()),
        ("State", FSM_STATE()),
        ("PrevState", FSM_STATE()),
        ("Mclt", DWORD()),
        ("SafePeriod", DWORD()),
        ("RelationshipName", LPWSTR()),
        ("PrimaryServerName", LPWSTR()),
        ("SecondaryServerName", LPWSTR()),
        ("pScopes", LPDHCP_IP_ARRAY()),
        ("Percentage", BYTE()),
        ("SharedSecret", LPWSTR()),
    ]

LPDHCP_FAILOVER_RELATIONSHIP = Ptr("<I", DHCP_FAILOVER_RELATIONSHIP())
LPDHCP_FAILOVER_RELATIONSHIP_PTR = Ptr("<I", LPDHCP_FAILOVER_RELATIONSHIP())

class DHCP_FAILOVER_RELATIONSHIP_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("pRelationships", LPDHCP_FAILOVER_RELATIONSHIP()),
    ]

LPDHCP_FAILOVER_RELATIONSHIP_ARRAY = Ptr("<I", DHCP_FAILOVER_RELATIONSHIP_ARRAY())
LPDHCP_FAILOVER_RELATIONSHIP_ARRAY_PTR = Ptr("<I", LPDHCP_FAILOVER_RELATIONSHIP_ARRAY())

class DHCPV4_FAILOVER_CLIENT_INFO(MemStruct):
    fields = [
        ("ClientIpAddress", DHCP_IP_ADDRESS()),
        ("SubnetMask", DHCP_IP_MASK()),
        ("ClientHardwareAddress", DHCP_CLIENT_UID()),
        ("ClientName", LPWSTR()),
        ("ClientComment", LPWSTR()),
        ("ClientLeaseExpires", DATE_TIME()),
        ("OwnerHost", DHCP_HOST_INFO()),
        ("bClientType", _CLIENT_TYPE_FLAGS_()),
        ("AddressState", _V5_ADDRESS_STATE_()),
        ("Status", QuarantineStatus()),
        ("ProbationEnds", DATE_TIME()),
        ("QuarantineCapable", BOOL()),
        ("SentPotExpTime", DWORD()),
        ("AckPotExpTime", DWORD()),
        ("RecvPotExpTime", DWORD()),
        ("StartTime", DWORD()),
        ("CltLastTransTime", DWORD()),
        ("LastBndUpdTime", DWORD()),
        ("BndMsgStatus", DWORD()),
        ("PolicyName", LPWSTR()),
        ("Flags", BYTE()),
    ]

LPDHCPV4_FAILOVER_CLIENT_INFO = Ptr("<I", DHCPV4_FAILOVER_CLIENT_INFO())
LPDHCPV4_FAILOVER_CLIENT_INFO_PTR = Ptr("<I", LPDHCPV4_FAILOVER_CLIENT_INFO())

class DHCP_FAILOVER_STATISTICS(MemStruct):
    fields = [
        ("NumAddr", DWORD()),
        ("AddrFree", DWORD()),
        ("AddrInUse", DWORD()),
        ("PartnerAddrFree", DWORD()),
        ("ThisAddrFree", DWORD()),
        ("PartnerAddrInUse", DWORD()),
        ("ThisAddrInUse", DWORD()),
    ]

LPDHCP_FAILOVER_STATISTICS = Ptr("<I", DHCP_FAILOVER_STATISTICS())
LPDHCP_FAILOVER_STATISTICS_PTR = Ptr("<I", LPDHCP_FAILOVER_STATISTICS())

class DHCP_CLIENT_INFO_PB(MemStruct):
    fields = [
        ("ClientIpAddress", DHCP_IP_ADDRESS()),
        ("SubnetMask", DHCP_IP_MASK()),
        ("ClientHardwareAddress", DHCP_CLIENT_UID()),
        ("ClientName", LPWSTR()),
        ("ClientComment", LPWSTR()),
        ("ClientLeaseExpires", DATE_TIME()),
        ("OwnerHost", DHCP_HOST_INFO()),
        ("bClientType", _CLIENT_TYPE_FLAGS_()),
        ("AddressState", _V5_ADDRESS_STATE_()),
        ("Status", QuarantineStatus()),
        ("ProbationEnds", DATE_TIME()),
        ("QuarantineCapable", BOOL()),
        ("FilterStatus", _FILTER_STATUS_FLAGS_()),
        ("PolicyName", LPWSTR()),
    ]

LPDHCP_CLIENT_INFO_PB = Ptr("<I", DHCP_CLIENT_INFO_PB())
LPDHCP_CLIENT_INFO_PB_PTR = Ptr("<I", LPDHCP_CLIENT_INFO_PB())
DHCP_CONST_LPDHCP_CLIENT_INFO_PB = Ptr("<I", DHCP_CLIENT_INFO_PB())

class DHCP_CLIENT_INFO_PB_ARRAY(MemStruct):
    fields = [
        ("NumElements", DWORD()),
        ("Clients", LPDHCP_CLIENT_INFO_PB_PTR()),
    ]

LPDHCP_CLIENT_INFO_PB_ARRAY = Ptr("<I", DHCP_CLIENT_INFO_PB_ARRAY())
LPDHCP_CLIENT_INFO_PB_ARRAY_PTR = Ptr("<I", LPDHCP_CLIENT_INFO_PB_ARRAY())

class _DHCP_ALL_OPTION_VALUES_PB_s_(MemStruct):
    fields = [
        ("PolicyName", LPWSTR()),
        ("VendorName", LPWSTR()),
        ("IsVendor", BOOL()),
        ("OptionsArray", LPDHCP_OPTION_VALUE_ARRAY()),
    ]

_DHCP_ALL_OPTION_VALUES_PB_s_PTR_ = Ptr("<I", _DHCP_ALL_OPTION_VALUES_PB_s_())

class DHCP_ALL_OPTION_VALUES_PB(MemStruct):
    fields = [
        ("Flags", DWORD()),
        ("NumElements", DWORD()),
        ("Options", _DHCP_ALL_OPTION_VALUES_PB_s_PTR_()),
    ]

LPDHCP_ALL_OPTION_VALUES_PB = Ptr("<I", DHCP_ALL_OPTION_VALUES_PB())
LPDHCP_ALL_OPTION_VALUES_PB_PTR = Ptr("<I", LPDHCP_ALL_OPTION_VALUES_PB())

###################

###### Functions ######

def dhcpsapi_DhcpAddFilterV4(jitter):
    """
    [ERROR_CODE] DhcpAddFilterV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_FILTER_ADD_INFO* AddFilterInfo,
        BOOL ForceFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "AddFilterInfo", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAddServer(jitter):
    """
    [ERROR_CODE] DhcpAddServer(
        DWORD Flags,
        LPVOID IdInfo,
        LPDHCP_SERVER_INFO NewServer,
        LPVOID CallbackFn,
        LPVOID CallbackData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "IdInfo", "NewServer", "CallbackFn", "CallbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAddSubnetElementV5(jitter):
    """
    [ERROR_CODE] DhcpAddSubnetElementV5(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_CONST DHCP_SUBNET_ELEMENT_DATA_V5* AddElementInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "AddElementInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAuditLogGetParams(jitter):
    """
    [ERROR_CODE] DhcpAuditLogGetParams(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        LPWSTR* AuditLogDir,
        DWORD* DiskCheckInterval,
        DWORD* MaxLogFilesSize,
        DWORD* MinSpaceOnDisk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "AuditLogDir", "DiskCheckInterval", "MaxLogFilesSize", "MinSpaceOnDisk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAuditLogSetParams(jitter):
    """
    [ERROR_CODE] DhcpAuditLogSetParams(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        LPWSTR AuditLogDir,
        DWORD DiskCheckInterval,
        DWORD MaxLogFilesSize,
        DWORD MinSpaceOnDisk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "AuditLogDir", "DiskCheckInterval", "MaxLogFilesSize", "MinSpaceOnDisk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateClass(jitter):
    """
    [ERROR_CODE] DhcpCreateClass(
        LPWSTR ServerIpAddress,
        DWORD ReservedMustBeZero,
        LPDHCP_CLASS_INFO ClassInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ClassInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateClientInfo(jitter):
    """
    [ERROR_CODE] DhcpCreateClientInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST DHCP_CLIENT_INFO* ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateClientInfoV4(jitter):
    """
    [ERROR_CODE] DhcpCreateClientInfoV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST DHCP_CLIENT_INFO_V4* ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateClientInfoVQ(jitter):
    """
    [ERROR_CODE] DhcpCreateClientInfoVQ(
        DHCP_CONST WCHAR* ServerIpAddress,
        LPDHCP_CLIENT_INFO_VQ ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateOptionV5(jitter):
    """
    [ERROR_CODE] DhcpCreateOptionV5(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionId,
        LPWSTR ClassName,
        LPWSTR VendorName,
        LPDHCP_OPTION OptionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionId", "ClassName", "VendorName", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateSubnet(jitter):
    """
    [ERROR_CODE] DhcpCreateSubnet(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_CONST DHCP_SUBNET_INFO* SubnetInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateSubnetVQ(jitter):
    """
    [ERROR_CODE] DhcpCreateSubnetVQ(
        WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_CONST DHCP_SUBNET_INFO_VQ* SubnetInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteClass(jitter):
    """
    [ERROR_CODE] DhcpDeleteClass(
        LPWSTR ServerIpAddress,
        DWORD ReservedMustBeZero,
        LPWSTR ClassName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ClassName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteClientInfo(jitter):
    """
    [ERROR_CODE] DhcpDeleteClientInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST DHCP_SEARCH_INFO* ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteFilterV4(jitter):
    """
    [ERROR_CODE] DhcpDeleteFilterV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_ADDR_PATTERN* DeleteFilterInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "DeleteFilterInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteServer(jitter):
    """
    [ERROR_CODE] DhcpDeleteServer(
        DWORD Flags,
        LPVOID IdInfo,
        LPDHCP_SERVER_INFO NewServer,
        LPVOID CallbackFn,
        LPVOID CallbackData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "IdInfo", "NewServer", "CallbackFn", "CallbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteSubnet(jitter):
    """
    [ERROR_CODE] DhcpDeleteSubnet(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_FORCE_FLAG ForceFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteSuperScopeV4(jitter):
    """
    [ERROR_CODE] DhcpDeleteSuperScopeV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST LPWSTR SuperScopeName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SuperScopeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDsCleanup(jitter):
    """
    VOID DhcpDsCleanup()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDsInit(jitter):
    """
    [ERROR_CODE] DhcpDsInit()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumClasses(jitter):
    """
    [ERROR_CODE] DhcpEnumClasses(
        LPWSTR ServerIpAddress,
        DWORD ReservedMustBeZero,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_CLASS_INFO_ARRAY* ClassInfoArray,
        DWORD* nRead,
        DWORD* nTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ResumeHandle", "PreferredMaximum", "ClassInfoArray", "nRead", "nTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumFilterV4(jitter):
    """
    [ERROR_CODE] DhcpEnumFilterV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        LPDHCP_ADDR_PATTERN ResumeHandle,
        DWORD PreferrredMaximum,
        DHCP_FILTER_LIST_TYPE ListType,
        LPDHCP_FILTER_ENUM_INFO* EnumFilterInfo,
        DWORD* ElementsRead,
        DWORD* ElementsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ResumeHandle", "PreferrredMaximum", "ListType", "EnumFilterInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumOptionsV5(jitter):
    """
    [ERROR_CODE] DhcpEnumOptionsV5(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        LPWSTR ClassName,
        LPWSTR VendorName,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_OPTION_ARRAY* Options,
        DWORD* OptionsRead,
        DWORD* OptionsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ClassName", "VendorName", "ResumeHandle", "PreferredMaximum", "Options", "OptionsRead", "OptionsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumOptionValuesV5(jitter):
    """
    [ERROR_CODE] DhcpEnumOptionValuesV5(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        LPWSTR ClassName,
        LPWSTR VendorName,
        LPDHCP_OPTION_SCOPE_INFO ScopeInfo,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_OPTION_VALUE_ARRAY* OptionValues,
        DWORD* OptionsRead,
        DWORD* OptionsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ClassName", "VendorName", "ScopeInfo", "ResumeHandle", "PreferredMaximum", "OptionValues", "OptionsRead", "OptionsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumServers(jitter):
    """
    [ERROR_CODE] DhcpEnumServers(
        DWORD Flags,
        LPVOID IdInfo,
        LPDHCP_SERVER_INFO_ARRAY* Servers,
        LPVOID CallbackFn,
        LPVOID CallbackData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "IdInfo", "Servers", "CallbackFn", "CallbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetClients(jitter):
    """
    [ERROR_CODE] DhcpEnumSubnetClients(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_CLIENT_INFO_ARRAY* ClientInfo,
        DWORD* ClientsRead,
        DWORD* ClientsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetClientsV5(jitter):
    """
    [ERROR_CODE] DhcpEnumSubnetClientsV5(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_CLIENT_INFO_ARRAY_V5* ClientInfo,
        DWORD* ClientsRead,
        DWORD* ClientsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetClientsVQ(jitter):
    """
    [ERROR_CODE] DhcpEnumSubnetClientsVQ(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_CLIENT_INFO_ARRAY_VQ* ClientInfo,
        DWORD* ClientsRead,
        DWORD* ClientsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetClientsFilterStatusInfo(jitter):
    """
    [ERROR_CODE] DhcpEnumSubnetClientsFilterStatusInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_CLIENT_FILTER_STATUS_INFO_ARRAY* ClientInfo,
        DWORD* ClientsRead,
        DWORD* ClientsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetElementsV5(jitter):
    """
    [ERROR_CODE] DhcpEnumSubnetElementsV5(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_SUBNET_ELEMENT_TYPE EnumElementType,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_SUBNET_ELEMENT_INFO_ARRAY* EnumElementInfo,
        DWORD* ElementsRead,
        DWORD* ElementsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "EnumElementType", "ResumeHandle", "PreferredMaximum", "EnumElementInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnets(jitter):
    """
    [ERROR_CODE] DhcpEnumSubnets(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_IP_ARRAY* EnumInfo,
        DWORD* ElementsRead,
        DWORD* ElementsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ResumeHandle", "PreferredMaximum", "EnumInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetAllOptionValues(jitter):
    """
    [ERROR_CODE] DhcpGetAllOptionValues(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        LPDHCP_OPTION_SCOPE_INFO ScopeInfo,
        LPDHCP_ALL_OPTION_VALUES* Values
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ScopeInfo", "Values"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetClassInfo(jitter):
    """
    [ERROR_CODE] DhcpGetClassInfo(
        LPWSTR ServerIpAddress,
        DWORD ReservedMustBeZero,
        LPDHCP_CLASS_INFO PartialClassInfo,
        LPDHCP_CLASS_INFO* FilledClassInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "PartialClassInfo", "FilledClassInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetClientInfo(jitter):
    """
    [ERROR_CODE] DhcpGetClientInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST DHCP_SEARCH_INFO* SearchInfo,
        LPDHCP_CLIENT_INFO* ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SearchInfo", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetClientInfoV4(jitter):
    """
    [ERROR_CODE] DhcpGetClientInfoV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST DHCP_SEARCH_INFO* SearchInfo,
        LPDHCP_CLIENT_INFO_V4* ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SearchInfo", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetClientInfoVQ(jitter):
    """
    [ERROR_CODE] DhcpGetClientInfoVQ(
        DHCP_CONST WCHAR* ServerIpAddress,
        LPDHCP_SEARCH_INFO SearchInfo,
        LPDHCP_CLIENT_INFO_VQ ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SearchInfo", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetFilterV4(jitter):
    """
    [ERROR_CODE] DhcpGetFilterV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_FILTER_GLOBAL_INFO* GlobalFilterInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "GlobalFilterInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetMibInfoV5(jitter):
    """
    [ERROR_CODE] DhcpGetMibInfoV5(
        WCHAR* ServerIpAddress,
        LPDHCP_MIB_INFO_V5* MibInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "MibInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetOptionInfoV5(jitter):
    """
    [ERROR_CODE] DhcpGetOptionInfoV5(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionID,
        LPWSTR ClassName,
        LPWSTR VendorName,
        LPDHCP_OPTION* OptionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetOptionValue(jitter):
    """
    [ERROR_CODE] DhcpGetOptionValue(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_OPTION_ID OptionID,
        DHCP_CONST DHCP_OPTION_SCOPE_INFO* ScopeInfo,
        LPDHCP_OPTION_VALUE* OptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetOptionValueV5(jitter):
    """
    [ERROR_CODE] DhcpGetOptionValueV5(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionID,
        LPWSTR ClassName,
        LPWSTR VendorName,
        LPDHCP_OPTION_SCOPE_INFO ScopeInfo,
        LPDHCP_OPTION_VALUE* OptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetServerBindingInfo(jitter):
    """
    [ERROR_CODE] DhcpGetServerBindingInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        ULONG Flags,
        LPDHCP_BIND_ELEMENT_ARRAY* BindElementsInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "BindElementsInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetSubnetDelayOffer(jitter):
    """
    [ERROR_CODE] DhcpGetSubnetDelayOffer(
        LPWSTR ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        USHORT* TimeDelayInMilliseconds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "TimeDelayInMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetSubnetInfo(jitter):
    """
    [ERROR_CODE] DhcpGetSubnetInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        LPDHCP_SUBNET_INFO* SubnetInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetSubnetInfoVQ(jitter):
    """
    [ERROR_CODE] DhcpGetSubnetInfoVQ(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        LPDHCP_SUBNET_INFO_VQ* SubnetInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetSuperScopeInfoV4(jitter):
    """
    [ERROR_CODE] DhcpGetSuperScopeInfoV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        LPDHCP_SUPER_SCOPE_TABLE* SuperScopeTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SuperScopeTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetVersion(jitter):
    """
    [ERROR_CODE] DhcpGetVersion(
        LPWSTR ServerIpAddress,
        LPDWORD MajorVersion,
        LPDWORD MinorVersion
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "MajorVersion", "MinorVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpModifyClass(jitter):
    """
    [ERROR_CODE] DhcpModifyClass(
        LPWSTR ServerIpAddress,
        DWORD ReservedMustBeZero,
        LPDHCP_CLASS_INFO ClassInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ClassInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveOptionV5(jitter):
    """
    [ERROR_CODE] DhcpRemoveOptionV5(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionID,
        LPWSTR ClassName,
        LPWSTR VendorName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveOptionValueV5(jitter):
    """
    [ERROR_CODE] DhcpRemoveOptionValueV5(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionID,
        LPWSTR ClassName,
        LPWSTR VendorName,
        LPDHCP_OPTION_SCOPE_INFO ScopeInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "ScopeInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveSubnetElementV5(jitter):
    """
    [ERROR_CODE] DhcpRemoveSubnetElementV5(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_CONST DHCP_SUBNET_ELEMENT_DATA_V5* RemoveElementInfo,
        DHCP_FORCE_FLAG ForceFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "RemoveElementInfo", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRpcFreeMemory(jitter):
    """
    VOID DhcpRpcFreeMemory(
        PVOID BufferPointer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferPointer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerGetConfigVQ(jitter):
    """
    [ERROR_CODE] DhcpServerGetConfigVQ(
        DHCP_CONST WCHAR* ServerIpAddress,
        LPDHCP_SERVER_CONFIG_INFO_VQ* ConfigInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerQueryDnsRegCredentials(jitter):
    """
    [ERROR_CODE] DhcpServerQueryDnsRegCredentials(
        LPWSTR ServerIpAddress,
        ULONG UnameSize,
        LPWSTR Uname,
        ULONG DomainSize,
        LPWSTR Domain
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "UnameSize", "Uname", "DomainSize", "Domain"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerRedoAuthorization(jitter):
    """
    [ERROR_CODE] DhcpServerRedoAuthorization(
        LPWSTR ServerIpAddr,
        ULONG dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddr", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerSetConfigV4(jitter):
    """
    [ERROR_CODE] DhcpServerSetConfigV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        [DHCP_FIELDS_TO_SET] FieldsToSet,
        LPDHCP_SERVER_CONFIG_INFO_V4 ConfigInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "FieldsToSet", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerSetConfigVQ(jitter):
    """
    [ERROR_CODE] DhcpServerSetConfigVQ(
        DHCP_CONST WCHAR* ServerIpAddress,
        [DHCP_FIELDS_TO_SET] FieldsToSet,
        LPDHCP_SERVER_CONFIG_INFO_VQ ConfigInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "FieldsToSet", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerSetDnsRegCredentialsV5(jitter):
    """
    [ERROR_CODE] DhcpServerSetDnsRegCredentialsV5(
        LPWSTR ServerIpAddress,
        LPWSTR Uname,
        LPWSTR Domain,
        LPWSTR Password
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Uname", "Domain", "Password"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetClientInfo(jitter):
    """
    [ERROR_CODE] DhcpSetClientInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST DHCP_CLIENT_INFO* ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetClientInfoV4(jitter):
    """
    [ERROR_CODE] DhcpSetClientInfoV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST DHCP_CLIENT_INFO_V4* ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetClientInfoVQ(jitter):
    """
    [ERROR_CODE] DhcpSetClientInfoVQ(
        DHCP_CONST WCHAR* ServerIpAddress,
        LPDHCP_CLIENT_INFO_VQ ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetFilterV4(jitter):
    """
    [ERROR_CODE] DhcpSetFilterV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_FILTER_GLOBAL_INFO* GlobalFilterInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "GlobalFilterInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionInfoV5(jitter):
    """
    [ERROR_CODE] DhcpSetOptionInfoV5(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionID,
        LPWSTR* ClassName,
        LPWSTR* VendorName,
        LPDHCP_OPTION OptionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionValueV5(jitter):
    """
    [ERROR_CODE] DhcpSetOptionValueV5(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionId,
        LPWSTR ClassName,
        LPWSTR VendorName,
        LPDHCP_OPTION_SCOPE_INFO ScopeInfo,
        LPDHCP_OPTION_DATA OptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionId", "ClassName", "VendorName", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetServerBindingInfo(jitter):
    """
    [ERROR_CODE] DhcpSetServerBindingInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        ULONG Flags,
        LPDHCP_BIND_ELEMENT_ARRAY BindElementInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "BindElementInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetSubnetDelayOffer(jitter):
    """
    [ERROR_CODE] DhcpSetSubnetDelayOffer(
        LPWSTR ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        USHORT TimeDelayInMilliseconds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "TimeDelayInMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetSubnetInfo(jitter):
    """
    [ERROR_CODE] DhcpSetSubnetInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_CONST DHCP_SUBNET_INFO* SubnetInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetSubnetInfoVQ(jitter):
    """
    [ERROR_CODE] DhcpSetSubnetInfoVQ(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_CONST DHCP_SUBNET_INFO_VQ* SubnetInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetSuperScopeV4(jitter):
    """
    [ERROR_CODE] DhcpSetSuperScopeV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST DHCP_IP_ADDRESS SubnetAddress,
        DHCP_CONST LPWSTR SuperScopeName,
        DHCP_CONST BOOL ChangeExisting
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SuperScopeName", "ChangeExisting"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAddSubnetElementV6(jitter):
    """
    [ERROR_CODE] DhcpAddSubnetElementV6(
        LPWSTR ServerIpAddress,
        DHCP_IPV6_ADDRESS SubnetAddress,
        LPDHCP_SUBNET_ELEMENT_DATA_V6 AddElementInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "AddElementInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateClassV6(jitter):
    """
    [ERROR_CODE] DhcpCreateClassV6(
        LPWSTR ServerIpAddress,
        DWORD ReservedMustBeZero,
        LPDHCP_CLASS_INFO_V6 ClassInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ClassInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateOptionV6(jitter):
    """
    [ERROR_CODE] DhcpCreateOptionV6(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionId,
        WCHAR* ClassName,
        WCHAR* VendorName,
        LPDHCP_OPTION OptionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionId", "ClassName", "VendorName", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateSubnetV6(jitter):
    """
    [ERROR_CODE] DhcpCreateSubnetV6(
        LPWSTR ServerIpAddress,
        DHCP_IPV6_ADDRESS SubnetAddress,
        LPDHCP_SUBNET_INFO_V6* SubnetInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteClassV6(jitter):
    """
    [ERROR_CODE] DhcpDeleteClassV6(
        LPWSTR ServerIpAddress,
        DWORD ReservedMustBeZero,
        LPWSTR ClassName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ClassName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteClientInfoV6(jitter):
    """
    [ERROR_CODE] DhcpDeleteClientInfoV6(
        LPWSTR ServerIpAddress,
        LPDHCP_SEARCH_INFO_V6 ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteSubnetV6(jitter):
    """
    [ERROR_CODE] DhcpDeleteSubnetV6(
        LPWSTR ServerIpAddress,
        DHCP_IPV6_ADDRESS SubnetAddress,
        DHCP_FORCE_FLAG ForceFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumClassesV6(jitter):
    """
    [ERROR_CODE] DhcpEnumClassesV6(
        LPWSTR ServerIpAddress,
        DWORD ReservedMustBeZero,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_CLASS_INFO_ARRAY_V6* ClassInfoArray,
        DWORD* nRead,
        DWORD* nTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ResumeHandle", "PreferredMaximum", "ClassInfoArray", "nRead", "nTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumOptionsV6(jitter):
    """
    [ERROR_CODE] DhcpEnumOptionsV6(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        WCHAR* ClassName,
        WCHAR* VendorName,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_OPTION_ARRAY* Options,
        DWORD* OptionsRead,
        DWORD* OptionsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ClassName", "VendorName", "ResumeHandle", "PreferredMaximum", "Options", "OptionsRead", "OptionsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumOptionValuesV6(jitter):
    """
    [ERROR_CODE] DhcpEnumOptionValuesV6(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        WCHAR* ClassName,
        WCHAR* VendorName,
        LPDHCP_OPTION_SCOPE_INFO6 ScopeInfo,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_OPTION_VALUE_ARRAY* OptionValues,
        DWORD* OptionsRead,
        DWORD* OptionsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ClassName", "VendorName", "ScopeInfo", "ResumeHandle", "PreferredMaximum", "OptionValues", "OptionsRead", "OptionsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetsV6(jitter):
    """
    [ERROR_CODE] DhcpEnumSubnetsV6(
        LPWSTR ServerIpAddress,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCPV6_IP_ARRAY* EnumInfo,
        DWORD* ElementsRead,
        DWORD* ElementsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ResumeHandle", "PreferredMaximum", "EnumInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetClientsV6(jitter):
    """
    [ERROR_CODE] DhcpEnumSubnetClientsV6(
        LPWSTR ServerIpAddress,
        DHCP_IPV6_ADDRESS SubnetAddress,
        DHCP_RESUME_IPV6_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_CLIENT_INFO_ARRAY_V6* ClientInfo,
        DWORD* ClientsRead,
        DWORD* ClientsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetElementsV6(jitter):
    """
    [ERROR_CODE] DhcpEnumSubnetElementsV6(
        LPWSTR ServerIpAddress,
        DHCP_IPV6_ADDRESS SubnetAddress,
        DHCP_SUBNET_ELEMENT_TYPE_V6 EnumElementType,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V6* EnumElementInfo,
        DWORD* ElementsRead,
        DWORD* ElementsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "EnumElementType", "ResumeHandle", "PreferredMaximum", "EnumElementInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetAllOptionsV6(jitter):
    """
    [ERROR_CODE] DhcpGetAllOptionsV6(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        LPDHCP_ALL_OPTIONS* OptionStruct
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetAllOptionValuesV6(jitter):
    """
    [ERROR_CODE] DhcpGetAllOptionValuesV6(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        LPDHCP_OPTION_SCOPE_INFO6 ScopeInfo,
        LPDHCP_ALL_OPTION_VALUES* Values
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ScopeInfo", "Values"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetClientInfoV6(jitter):
    """
    [ERROR_CODE] DhcpGetClientInfoV6(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST DHCP_SEARCH_INFO_V6* SearchInfo,
        LPDHCP_CLIENT_INFO_V6* ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SearchInfo", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetMibInfoV6(jitter):
    """
    [ERROR_CODE] DhcpGetMibInfoV6(
        DHCP_CONST WCHAR* ServerIpAddress,
        LPDHCP_MIB_INFO_V6* MibInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "MibInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetOptionInfoV6(jitter):
    """
    [ERROR_CODE] DhcpGetOptionInfoV6(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionID,
        WCHAR* ClassName,
        WCHAR* VendorName,
        LPDHCP_OPTION* OptionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetOptionValueV6(jitter):
    """
    [ERROR_CODE] DhcpGetOptionValueV6(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionID,
        WCHAR* ClassName,
        WCHAR* VendorName,
        LPDHCP_OPTION_SCOPE_INFO6* ScopeInfo,
        LPDHCP_OPTION_VALUE OptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetServerBindingInfoV6(jitter):
    """
    [ERROR_CODE] DhcpGetServerBindingInfoV6(
        DHCP_CONST WCHAR* ServerIpAddress,
        ULONG Flags,
        LPDHCPV6_BIND_ELEMENT_ARRAY* BindElementsInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "BindElementsInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetSubnetInfoV6(jitter):
    """
    [ERROR_CODE] DhcpGetSubnetInfoV6(
        LPWSTR ServerIpAddress,
        DHCP_IPV6_ADDRESS SubnetAddress,
        LPDHCP_SUBNET_INFO_V6* SubnetInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpModifyClassV6(jitter):
    """
    [ERROR_CODE] DhcpModifyClassV6(
        LPWSTR ServerIpAddress,
        DWORD ReservedMustBeZero,
        LPDHCP_CLASS_INFO_V6 ClassInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ClassInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveOptionV6(jitter):
    """
    [ERROR_CODE] DhcpRemoveOptionV6(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionID,
        WCHAR* ClassName,
        WCHAR* VendorName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveOptionValueV6(jitter):
    """
    [ERROR_CODE] DhcpRemoveOptionValueV6(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionID,
        WCHAR* ClassName,
        WCHAR* VendorName,
        LPDHCP_OPTION_SCOPE_INFO6 ScopeInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "ScopeInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveSubnetElementV6(jitter):
    """
    [ERROR_CODE] DhcpRemoveSubnetElementV6(
        LPWSTR ServerIpAddress,
        DHCP_IPV6_ADDRESS SubnetAddress,
        LPDHCP_SUBNET_ELEMENT_DATA_V6 RemoveElementInfo,
        DHCP_FORCE_FLAG ForceFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "RemoveElementInfo", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerGetConfigV6(jitter):
    """
    [ERROR_CODE] DhcpServerGetConfigV6(
        DHCP_CONST WCHAR* ServerIpAddress,
        LPDHCP_OPTION_SCOPE_INFO6 ScopeInfo,
        LPDHCP_SERVER_CONFIG_INFO_V6* ConfigInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ScopeInfo", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetClientInfoV6(jitter):
    """
    [ERROR_CODE] DhcpSetClientInfoV6(
        LPWSTR ServerIpAddress,
        LPDHCP_CLIENT_INFO_V6 ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionInfoV6(jitter):
    """
    [ERROR_CODE] DhcpSetOptionInfoV6(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionID,
        WCHAR* ClassName,
        WCHAR* VendorName,
        LPDHCP_OPTION OptionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionValueV6(jitter):
    """
    [ERROR_CODE] DhcpSetOptionValueV6(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionId,
        WCHAR* ClassName,
        WCHAR* VendorName,
        LPDHCP_OPTION_SCOPE_INFO6 ScopeInfo,
        LPDHCP_OPTION_DATA OptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionId", "ClassName", "VendorName", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetServerBindingInfoV6(jitter):
    """
    [ERROR_CODE] DhcpSetServerBindingInfoV6(
        DHCP_CONST WCHAR* ServerIpAddress,
        ULONG Flags,
        LPDHCPV6_BIND_ELEMENT_ARRAY BindElementsInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "BindElementsInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerSetConfigV6(jitter):
    """
    [ERROR_CODE] DhcpServerSetConfigV6(
        DHCP_CONST WCHAR* ServerIpAddress,
        LPDHCP_OPTION_SCOPE_INFO6 ScopeInfo,
        [DHCP_FIELDS_TO_SET] FieldsToSet,
        LPDHCP_SERVER_CONFIG_INFO_V6 ConfigInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ScopeInfo", "FieldsToSet", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetSubnetInfoV6(jitter):
    """
    [ERROR_CODE] DhcpSetSubnetInfoV6(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IPV6_ADDRESS SubnetAddress,
        LPDHCP_SUBNET_INFO_V6 SubnetInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAddSubnetElement(jitter):
    """
    [ERROR_CODE] DhcpAddSubnetElement(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_CONST DHCP_SUBNET_ELEMENT_DATA* AddElementInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "AddElementInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAddSubnetElementV4(jitter):
    """
    [ERROR_CODE] DhcpAddSubnetElementV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_CONST DHCP_SUBNET_ELEMENT_DATA_V4* AddElementInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "AddElementInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateOption(jitter):
    """
    [ERROR_CODE] DhcpCreateOption(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_OPTION_ID OptionID,
        DHCP_CONST DHCP_OPTION* OptionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumOptions(jitter):
    """
    [ERROR_CODE] DhcpEnumOptions(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_OPTION_ARRAY* Options,
        DWORD* OptionsRead,
        DWORD* OptionsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ResumeHandle", "PreferredMaximum", "Options", "OptionsRead", "OptionsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumOptionValues(jitter):
    """
    [ERROR_CODE] DhcpEnumOptionValues(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST DHCP_OPTION_SCOPE_INFO* ScopeInfo,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_OPTION_VALUE_ARRAY* OptionValues,
        DWORD* OptionsRead,
        DWORD* OptionsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ScopeInfo", "ResumeHandle", "PreferredMaximum", "OptionValues", "OptionsRead", "OptionsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetClientsV4(jitter):
    """
    [ERROR_CODE] DhcpEnumSubnetClientsV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_CLIENT_INFO_ARRAY_V4* ClientInfo,
        DWORD* ClientsRead,
        DWORD* ClientsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetElements(jitter):
    """
    [ERROR_CODE] DhcpEnumSubnetElements(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_SUBNET_ELEMENT_TYPE EnumElementType,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_SUBNET_ELEMENT_INFO_ARRAY* EnumElementInfo,
        DWORD* ElementsRead,
        DWORD* ElementsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "EnumElementType", "ResumeHandle", "PreferredMaximum", "EnumElementInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetElementsV4(jitter):
    """
    [ERROR_CODE] DhcpEnumSubnetElementsV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_SUBNET_ELEMENT_TYPE EnumElementType,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V4* EnumElementInfo,
        DWORD* ElementsRead,
        DWORD* ElementsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "EnumElementType", "ResumeHandle", "PreferredMaximum", "EnumElementInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetAllOptions(jitter):
    """
    [ERROR_CODE] DhcpGetAllOptions(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        LPDHCP_ALL_OPTIONS* OptionStruct
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetClientOptions(jitter):
    """
    [ERROR_CODE] DhcpGetClientOptions(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS ClientIpAddress,
        DHCP_IP_MASK ClientSubnetMask,
        LPDHCP_OPTION_LIST* ClientOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientIpAddress", "ClientSubnetMask", "ClientOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetOptionInfo(jitter):
    """
    [ERROR_CODE] DhcpGetOptionInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_OPTION_ID OptionID,
        LPDHCP_OPTION* OptionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetServerSpecificStrings(jitter):
    """
    [ERROR_CODE] DhcpGetServerSpecificStrings(
        DHCP_CONST WCHAR* ServerIpAddress,
        LPDHCP_SERVER_SPECIFIC_STRINGS* ServerSpecificStrings
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ServerSpecificStrings"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetThreadOptions(jitter):
    """
    [ERROR_CODE] DhcpGetThreadOptions(
        LPDWORD pFlags,
        LPVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprAddV4PolicyCondition(jitter):
    """
    [ERROR_CODE] DhcpHlprAddV4PolicyCondition(
        LPDHCP_POLICY Policy,
        DWORD ParentExpr,
        DHCP_POL_ATTR_TYPE Type,
        DWORD OptionID,
        DWORD SubOptionID,
        LPWSTR VendorName,
        DHCP_POL_COMPARATOR Operator,
        LPBYTE Value,
        DWORD ValueLength,
        DWORD* ConditionIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Policy", "ParentExpr", "Type", "OptionID", "SubOptionID", "VendorName", "Operator", "Value", "ValueLength", "ConditionIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprAddV4PolicyExpr(jitter):
    """
    [ERROR_CODE] DhcpHlprAddV4PolicyExpr(
        LPDHCP_POLICY Policy,
        DWORD ParentExpr,
        DHCP_POL_LOGIC_OPER Operator,
        DWORD* ExprIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Policy", "ParentExpr", "Operator", "ExprIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprAddV4PolicyRange(jitter):
    """
    [ERROR_CODE] DhcpHlprAddV4PolicyRange(
        LPDHCP_POLICY Policy,
        LPDHCP_IP_RANGE Range
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Policy", "Range"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprCreateV4Policy(jitter):
    """
    [ERROR_CODE] DhcpHlprCreateV4Policy(
        LPWSTR PolicyName,
        BOOL fGlobalPolicy,
        DHCP_IP_ADDRESS Subnet,
        DWORD ProcessingOrder,
        DHCP_POL_LOGIC_OPER RootOperator,
        LPWSTR Description,
        BOOL Enabled,
        LPDHCP_POLICY* Policy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PolicyName", "fGlobalPolicy", "Subnet", "ProcessingOrder", "RootOperator", "Description", "Enabled", "Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprFreeV4Policy(jitter):
    """
    VOID DhcpHlprFreeV4Policy(
        LPDHCP_POLICY Policy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprIsV4PolicySingleUC(jitter):
    """
    BOOL DhcpHlprIsV4PolicySingleUC(
        LPDHCP_POLICY Policy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprIsV4PolicyValid(jitter):
    """
    [ERROR_CODE] DhcpHlprIsV4PolicyValid(
        LPDHCP_POLICY pPolicy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprIsV4PolicyWellFormed(jitter):
    """
    BOOL DhcpHlprIsV4PolicyWellFormed(
        LPDHCP_POLICY pPolicy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprModifyV4PolicyExpr(jitter):
    """
    [ERROR_CODE] DhcpHlprModifyV4PolicyExpr(
        LPDHCP_POLICY Policy,
        DHCP_POL_LOGIC_OPER Operator
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Policy", "Operator"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprResetV4PolicyExpr(jitter):
    """
    [ERROR_CODE] DhcpHlprResetV4PolicyExpr(
        LPDHCP_POLICY Policy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveOption(jitter):
    """
    [ERROR_CODE] DhcpRemoveOption(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_OPTION_ID OptionID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveOptionValue(jitter):
    """
    [ERROR_CODE] DhcpRemoveOptionValue(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_OPTION_ID OptionID,
        DHCP_CONST DHCP_OPTION_SCOPE_INFO* ScopeInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID", "ScopeInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveSubnetElement(jitter):
    """
    [ERROR_CODE] DhcpRemoveSubnetElement(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_CONST DHCP_SUBNET_ELEMENT_DATA* RemoveElementInfo,
        DHCP_FORCE_FLAG ForceFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "RemoveElementInfo", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveSubnetElementV4(jitter):
    """
    [ERROR_CODE] DhcpRemoveSubnetElementV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_CONST DHCP_SUBNET_ELEMENT_DATA_V4* RemoveElementInfo,
        DHCP_FORCE_FLAG ForceFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "RemoveElementInfo", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpScanDatabase(jitter):
    """
    [ERROR_CODE] DhcpScanDatabase(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DWORD FixFlag,
        LPDHCP_SCAN_LIST* ScanList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "FixFlag", "ScanList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerBackupDatabase(jitter):
    """
    [ERROR_CODE] DhcpServerBackupDatabase(
        LPWSTR ServerIpAddress,
        LPWSTR Path
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerGetConfig(jitter):
    """
    [ERROR_CODE] DhcpServerGetConfig(
        DHCP_CONST WCHAR* ServerIpAddress,
        LPDHCP_SERVER_CONFIG_INFO* ConfigInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerGetConfigV4(jitter):
    """
    [ERROR_CODE] DhcpServerGetConfigV4(
        DHCP_CONST WCHAR* ServerIpAddress,
        LPDHCP_SERVER_CONFIG_INFO_V4* ConfigInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerQueryAttribute(jitter):
    """
    [ERROR_CODE] DhcpServerQueryAttribute(
        LPWSTR ServerIpAddr,
        ULONG dwReserved,
        DHCP_ATTRIB_ID DhcpAttribId,
        LPDHCP_ATTRIB* pDhcpAttrib
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddr", "dwReserved", "DhcpAttribId", "pDhcpAttrib"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerQueryAttributes(jitter):
    """
    [ERROR_CODE] DhcpServerQueryAttributes(
        LPWSTR ServerIpAddr,
        ULONG dwReserved,
        ULONG dwAttribCount,
        DHCP_ATTRIB_ID [] pDhcpAttribs,
        LPDHCP_ATTRIB_ARRAY* pDhcpAttribArr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddr", "dwReserved", "dwAttribCount", "pDhcpAttribs", "pDhcpAttribArr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerRestoreDatabase(jitter):
    """
    [ERROR_CODE] DhcpServerRestoreDatabase(
        LPWSTR ServerIpAddress,
        LPWSTR Path
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerSetConfig(jitter):
    """
    [ERROR_CODE] DhcpServerSetConfig(
        DHCP_CONST WCHAR* ServerIpAddress,
        [DHCP_FIELDS_TO_SET] FieldsToSet,
        LPDHCP_SERVER_CONFIG_INFO ConfigInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "FieldsToSet", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionInfo(jitter):
    """
    [ERROR_CODE] DhcpSetOptionInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_OPTION_ID OptionID,
        DHCP_CONST DHCP_OPTION* OptionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionValue(jitter):
    """
    [ERROR_CODE] DhcpSetOptionValue(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_OPTION_ID OptionID,
        DHCP_CONST DHCP_OPTION_SCOPE_INFO* ScopeInfo,
        DHCP_CONST DHCP_OPTION_DATA* OptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionValues(jitter):
    """
    [ERROR_CODE] DhcpSetOptionValues(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST DHCP_OPTION_SCOPE_INFO* ScopeInfo,
        DHCP_CONST DHCP_OPTION_VALUE_ARRAY* OptionValues
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ScopeInfo", "OptionValues"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionValuesV5(jitter):
    """
    [ERROR_CODE] DhcpSetOptionValuesV5(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        LPWSTR ClassName,
        LPWSTR VendorName,
        LPDHCP_OPTION_SCOPE_INFO ScopeInfo,
        LPDHCP_OPTION_VALUE_ARRAY OptionValues
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ClassName", "VendorName", "ScopeInfo", "OptionValues"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetThreadOptions(jitter):
    """
    [ERROR_CODE] DhcpSetThreadOptions(
        DWORD Flags,
        LPVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverAddScopeToRelationship(jitter):
    """
    [ERROR_CODE] DhcpV4FailoverAddScopeToRelationship(
        LPWSTR ServerIpAddress,
        LPDHCP_FAILOVER_RELATIONSHIP pRelationship
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pRelationship"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverCreateRelationship(jitter):
    """
    [ERROR_CODE] DhcpV4FailoverCreateRelationship(
        LPWSTR ServerIpAddress,
        LPDHCP_FAILOVER_RELATIONSHIP pRelationship
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pRelationship"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverDeleteRelationship(jitter):
    """
    [ERROR_CODE] DhcpV4FailoverDeleteRelationship(
        LPWSTR ServerIpAddress,
        LPWSTR pRelationshipName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pRelationshipName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverDeleteScopeFromRelationship(jitter):
    """
    [ERROR_CODE] DhcpV4FailoverDeleteScopeFromRelationship(
        LPWSTR ServerIpAddress,
        LPDHCP_FAILOVER_RELATIONSHIP pRelationship
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pRelationship"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverEnumRelationship(jitter):
    """
    [ERROR_CODE] DhcpV4FailoverEnumRelationship(
        LPWSTR ServerIpAddress,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD preferredMaximum,
        LPDHCP_FAILOVER_RELATIONSHIP_ARRAY* pRelationship,
        LPDWORD relationshipRead,
        LPDWORD relationshipTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ResumeHandle", "preferredMaximum", "pRelationship", "relationshipRead", "relationshipTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverGetAddressStatus(jitter):
    """
    [ERROR_CODE] DhcpV4FailoverGetAddressStatus(
        LPWSTR ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        LPDWORD pStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "pStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverGetClientInfo(jitter):
    """
    [ERROR_CODE] DhcpV4FailoverGetClientInfo(
        LPWSTR ServerIpAddress,
        DHCP_CONST DHCP_SEARCH_INFO* SearchInfo,
        LPDHCPV4_FAILOVER_CLIENT_INFO* ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SearchInfo", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverGetRelationship(jitter):
    """
    [ERROR_CODE] DhcpV4FailoverGetRelationship(
        LPWSTR ServerIpAddress,
        LPWSTR pRelationshipName,
        LPDHCP_FAILOVER_RELATIONSHIP* pRelationship
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pRelationshipName", "pRelationship"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverGetScopeRelationship(jitter):
    """
    [ERROR_CODE] DhcpV4FailoverGetScopeRelationship(
        LPWSTR ServerIpAddress,
        DHCP_IP_ADDRESS scopeId,
        LPDHCP_FAILOVER_RELATIONSHIP* pRelationship
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "scopeId", "pRelationship"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverGetScopeStatistics(jitter):
    """
    [ERROR_CODE] DhcpV4FailoverGetScopeStatistics(
        LPWSTR ServerIpAddress,
        DHCP_IP_ADDRESS scopeId,
        LPDHCP_FAILOVER_STATISTICS* pStats
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "scopeId", "pStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverGetSystemTime(jitter):
    """
    [ERROR_CODE] DhcpV4FailoverGetSystemTime(
        LPWSTR ServerIpAddress,
        LPDWORD pTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverSetRelationship(jitter):
    """
    [ERROR_CODE] DhcpV4FailoverSetRelationship(
        LPWSTR ServerIpAddress,
        DWORD flags,
        LPDHCP_FAILOVER_RELATIONSHIP pRelationship
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "flags", "pRelationship"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverTriggerAddrAllocation(jitter):
    """
    [ERROR_CODE] DhcpV4FailoverTriggerAddrAllocation(
        LPWSTR ServerIpAddress,
        LPWSTR pFailRelName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pFailRelName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4GetFreeIPAddress(jitter):
    """
    [ERROR_CODE] DhcpV4GetFreeIPAddress(
        LPWSTR ServerIpAddress,
        DHCP_IP_ADDRESS ScopeId,
        DHCP_IP_ADDRESS startIP,
        DHCP_IP_ADDRESS endIP,
        DWORD numFreeAddrReq,
        LPDHCP_IP_ARRAY* IPAddrList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ScopeId", "startIP", "endIP", "numFreeAddrReq", "IPAddrList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4EnumSubnetClients(jitter):
    """
    [ERROR_CODE] DhcpV4EnumSubnetClients(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_CLIENT_INFO_PB_ARRAY* ClientInfo,
        DWORD* ClientsRead,
        DWORD* ClientsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4EnumSubnetReservations(jitter):
    """
    [ERROR_CODE] DhcpV4EnumSubnetReservations(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        DHCP_RESUME_HANDLE* ResumeHandle,
        DWORD PreferredMaximum,
        LPDHCP_RESERVATION_INFO_ARRAY* EnumElementInfo,
        DWORD* ElementsRead,
        DWORD* ElementsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "EnumElementInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4CreateClientInfo(jitter):
    """
    [ERROR_CODE] DhcpV4CreateClientInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST LPDHCP_CLIENT_INFO_PB ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4GetClientInfo(jitter):
    """
    [ERROR_CODE] DhcpV4GetClientInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST DHCP_SEARCH_INFO* SearchInfo,
        LPDHCP_CLIENT_INFO_PB* ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SearchInfo", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4RemoveOptionValue(jitter):
    """
    [ERROR_CODE] DhcpV4RemoveOptionValue(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionID,
        LPWSTR PolicyName,
        LPWSTR VendorName,
        LPDHCP_OPTION_SCOPE_INFO ScopeInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "PolicyName", "VendorName", "ScopeInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4GetAllOptionValues(jitter):
    """
    [ERROR_CODE] DhcpV4GetAllOptionValues(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        LPDHCP_OPTION_SCOPE_INFO ScopeInfo,
        LPDHCP_ALL_OPTION_VALUES_PB* Values
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ScopeInfo", "Values"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4SetOptionValues(jitter):
    """
    [ERROR_CODE] DhcpV4SetOptionValues(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        LPWSTR PolicyName,
        LPWSTR VendorName,
        LPDHCP_OPTION_SCOPE_INFO ScopeInfo,
        LPDHCP_OPTION_VALUE_ARRAY OptionValues
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "PolicyName", "VendorName", "ScopeInfo", "OptionValues"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4SetOptionValue(jitter):
    """
    [ERROR_CODE] DhcpV4SetOptionValue(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionId,
        LPWSTR PolicyName,
        LPWSTR VendorName,
        LPDHCP_OPTION_SCOPE_INFO ScopeInfo,
        LPDHCP_OPTION_DATA OptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionId", "PolicyName", "VendorName", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4GetOptionValue(jitter):
    """
    [ERROR_CODE] DhcpV4GetOptionValue(
        LPWSTR ServerIpAddress,
        DWORD Flags,
        DHCP_OPTION_ID OptionID,
        LPWSTR PolicyName,
        LPWSTR VendorName,
        LPDHCP_OPTION_SCOPE_INFO ScopeInfo,
        LPDHCP_OPTION_VALUE* OptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "PolicyName", "VendorName", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4CreatePolicy(jitter):
    """
    [ERROR_CODE] DhcpV4CreatePolicy(
        LPWSTR ServerIpAddress,
        LPDHCP_POLICY pPolicy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4EnumPolicies(jitter):
    """
    [ERROR_CODE] DhcpV4EnumPolicies(
        LPWSTR ServerIpAddress,
        LPDWORD ResumeHandle,
        DWORD PreferredMaximum,
        BOOL fGlobalPolicy,
        DHCP_IP_ADDRESS SubnetAddress,
        LPDHCP_POLICY_ARRAY* EnumInfo,
        DWORD* ElementsRead,
        DWORD* ElementsTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ResumeHandle", "PreferredMaximum", "fGlobalPolicy", "SubnetAddress", "EnumInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4GetPolicy(jitter):
    """
    [ERROR_CODE] DhcpV4GetPolicy(
        LPWSTR ServerIpAddress,
        BOOL fGlobalPolicy,
        DHCP_IP_ADDRESS SubnetAddress,
        LPWSTR PolicyName,
        LPDHCP_POLICY* Policy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "fGlobalPolicy", "SubnetAddress", "PolicyName", "Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4SetPolicy(jitter):
    """
    [ERROR_CODE] DhcpV4SetPolicy(
        LPWSTR ServerIpAddress,
        DWORD FieldsModified,
        BOOL fGlobalPolicy,
        DHCP_IP_ADDRESS SubnetAddress,
        LPWSTR PolicyName,
        LPDHCP_POLICY Policy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "FieldsModified", "fGlobalPolicy", "SubnetAddress", "PolicyName", "Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4DeletePolicy(jitter):
    """
    [ERROR_CODE] DhcpV4DeletePolicy(
        LPWSTR ServerIpAddress,
        BOOL fGlobalPolicy,
        DHCP_IP_ADDRESS SubnetAddress,
        LPWSTR PolicyName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "fGlobalPolicy", "SubnetAddress", "PolicyName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4SetPolicyEnforcement(jitter):
    """
    [ERROR_CODE] DhcpV4SetPolicyEnforcement(
        LPWSTR ServerIpAddress,
        BOOL fGlobalPolicy,
        DHCP_IP_ADDRESS SubnetAddress,
        BOOL Enable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "fGlobalPolicy", "SubnetAddress", "Enable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4QueryPolicyEnforcement(jitter):
    """
    [ERROR_CODE] DhcpV4QueryPolicyEnforcement(
        LPWSTR ServerIpAddress,
        BOOL fGlobalPolicy,
        DHCP_IP_ADDRESS SubnetAddress,
        BOOL* Enabled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "fGlobalPolicy", "SubnetAddress", "Enabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4AddPolicyRange(jitter):
    """
    [ERROR_CODE] DhcpV4AddPolicyRange(
        LPWSTR ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        LPWSTR PolicyName,
        LPDHCP_IP_RANGE Range
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "PolicyName", "Range"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4RemovePolicyRange(jitter):
    """
    [ERROR_CODE] DhcpV4RemovePolicyRange(
        LPWSTR ServerIpAddress,
        DHCP_IP_ADDRESS SubnetAddress,
        LPWSTR PolicyName,
        LPDHCP_IP_RANGE Range
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "PolicyName", "Range"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV6CreateClientInfo(jitter):
    """
    [ERROR_CODE] DhcpV6CreateClientInfo(
        DHCP_CONST WCHAR* ServerIpAddress,
        DHCP_CONST LPDHCP_CLIENT_INFO_V6 ClientInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV6GetFreeIPAddress(jitter):
    """
    [ERROR_CODE] DhcpV6GetFreeIPAddress(
        LPWSTR ServerIpAddress,
        DHCP_IPV6_ADDRESS ScopeId,
        DHCP_IPV6_ADDRESS startIP,
        DHCP_IPV6_ADDRESS endIP,
        DWORD numFreeAddrReq,
        LPDHCPV6_IP_ARRAY* IPAddrList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ScopeId", "startIP", "endIP", "numFreeAddrReq", "IPAddrList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV6GetStatelessStatistics(jitter):
    """
    [ERROR_CODE] DhcpV6GetStatelessStatistics(
        LPWSTR ServerIpAddress,
        LPDHCPV6_STATELESS_STATS* StatelessStats
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "StatelessStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV6GetStatelessStoreParams(jitter):
    """
    [ERROR_CODE] DhcpV6GetStatelessStoreParams(
        LPWSTR ServerIpAddress,
        BOOL fServerLevel,
        DHCP_IPV6_ADDRESS SubnetAddress,
        LPDHCPV6_STATELESS_PARAMS* Params
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "fServerLevel", "SubnetAddress", "Params"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV6SetStatelessStoreParams(jitter):
    """
    [ERROR_CODE] DhcpV6SetStatelessStoreParams(
        LPWSTR ServerIpAddress,
        BOOL fServerLevel,
        DHCP_IPV6_ADDRESS SubnetAddress,
        DWORD FieldModified,
        LPDHCPV6_STATELESS_PARAMS Params
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "fServerLevel", "SubnetAddress", "FieldModified", "Params"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
