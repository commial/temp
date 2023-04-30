###### Enums ######
StatusCode = {
    "STATUS_NO_ERROR": 0,
    "STATUS_UNSPECIFIED_FAILURE": 1,
    "STATUS_NO_BINDING": 3,
    "STATUS_NOPREFIX_AVAIL": 6,
}
StatusCode_INV = {
    0: "STATUS_NO_ERROR",
    1: "STATUS_UNSPECIFIED_FAILURE",
    3: "STATUS_NO_BINDING",
    6: "STATUS_NOPREFIX_AVAIL",
}

###################

###### Types ######

class DHCPV6CAPI_CLASSID(MemStruct):
    fields = [
        ("Flags", ULONG()),
        ("Data", LPBYTE()),
        ("nBytesData", ULONG()),
    ]

LPDHCPV6CAPI_CLASSID = Ptr("<I", DHCPV6CAPI_CLASSID())

class DHCPV6CAPI_PARAMS(MemStruct):
    fields = [
        ("Flags", ULONG()),
        ("OptionId", ULONG()),
        ("IsVendor", BOOL()),
        ("Data", LPBYTE()),
        ("nBytesData", DWORD()),
    ]

LPDHCPV6CAPI_PARAMS = Ptr("<I", DHCPV6CAPI_PARAMS())

class DHCPV6CAPI_PARAMS_ARRAY(MemStruct):
    fields = [
        ("nParams", ULONG()),
        ("Params", LPDHCPV6CAPI_PARAMS()),
    ]

StatusCode = UINT

class DHCPV6Prefix(MemStruct):
    fields = [
        ("prefix", UCHAR__16_()),
        ("prefixLength", DWORD()),
        ("preferredLifeTime", DWORD()),
        ("validLifeTime", DWORD()),
        ("status", StatusCode()),
    ]

LPDHCPV6Prefix = Ptr("<I", DHCPV6Prefix())

class DHCPV6PrefixLeaseInformation(MemStruct):
    fields = [
        ("nPrefixes", DWORD()),
        ("prefixArray", LPDHCPV6Prefix()),
        ("iaid", DWORD()),
        ("T1", time_t()),
        ("T2", time_t()),
        ("MaxLeaseExpirationTime", time_t()),
        ("LastRenewalTime", time_t()),
        ("status", StatusCode()),
        ("ServerId", LPBYTE()),
        ("ServerIdLen", DWORD()),
    ]

LPDHCPV6PrefixLeaseInformation = Ptr("<I", DHCPV6PrefixLeaseInformation())

###################

###### Functions ######

def dhcpcsvc6_Dhcpv6CApiCleanup(jitter):
    """
    VOID Dhcpv6CApiCleanup()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc6_Dhcpv6CApiInitialize(jitter):
    """
    [ERROR_CODE] Dhcpv6CApiInitialize(
        LPDWORD Version
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Version"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc6_Dhcpv6RequestParams(jitter):
    """
    [ERROR_CODE] Dhcpv6RequestParams(
        BOOL forceNewInform,
        LPVOID reserved,
        LPWSTR adapterName,
        LPDHCPV6CAPI_CLASSID classId,
        DHCPV6CAPI_PARAMS_ARRAY recdParams,
        LPBYTE buffer,
        LPDWORD pSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["forceNewInform", "reserved", "adapterName", "classId", "recdParams", "buffer", "pSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc6_Dhcpv6ReleasePrefix(jitter):
    """
    [ERROR_CODE] Dhcpv6ReleasePrefix(
        LPWSTR adapterName,
        LPDHCPV6CAPI_CLASSID classId,
        LPDHCPV6PrefixLeaseInformation prefixleaseInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["adapterName", "classId", "prefixleaseInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc6_Dhcpv6RenewPrefix(jitter):
    """
    [ERROR_CODE] Dhcpv6RenewPrefix(
        LPWSTR adapterName,
        LPDHCPV6CAPI_CLASSID classId,
        LPDHCPV6PrefixLeaseInformation prefixleaseInfo,
        DWORD pdwTimeToWait,
        DWORD bValidatePrefix
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["adapterName", "classId", "prefixleaseInfo", "pdwTimeToWait", "bValidatePrefix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc6_Dhcpv6RequestPrefix(jitter):
    """
    [ERROR_CODE] Dhcpv6RequestPrefix(
        LPWSTR adapterName,
        LPDHCPV6CAPI_CLASSID classId,
        LPDHCPV6PrefixLeaseInformation prefixleaseInfo,
        DWORD pdwTimeToWait
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["adapterName", "classId", "prefixleaseInfo", "pdwTimeToWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
