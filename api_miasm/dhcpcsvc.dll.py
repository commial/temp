###### Enums ######

###################

###### Types ######
IP_ADDR_FAMILY = unsigned_short
IPNG_ADDRESS = Union([
    ("IpAddrV4", DWORD),
    ("IpAddrV6", BYTE__16_),
])

class MCAST_LEASE_REQUEST(MemStruct):
    fields = [
        ("LeaseStartTime", LONG()),
        ("MaxLeaseStartTime", LONG()),
        ("LeaseDuration", DWORD()),
        ("MinLeaseDuration", DWORD()),
        ("ServerAddress", IPNG_ADDRESS()),
        ("MinAddrCount", WORD()),
        ("AddrCount", WORD()),
        ("pAddrBuf", PBYTE()),
    ]

PMCAST_LEASE_REQUEST = Ptr("<I", MCAST_LEASE_REQUEST())

class MCAST_LEASE_RESPONSE(MemStruct):
    fields = [
        ("LeaseStartTime", LONG()),
        ("LeaseEndTime", LONG()),
        ("ServerAddress", IPNG_ADDRESS()),
        ("AddrCount", WORD()),
        ("pAddrBuf", PBYTE()),
    ]

PMCAST_LEASE_RESPONSE = Ptr("<I", MCAST_LEASE_RESPONSE())

class MCAST_SCOPE_CTX(MemStruct):
    fields = [
        ("ScopeID", IPNG_ADDRESS()),
        ("Interface", IPNG_ADDRESS()),
        ("ServerID", IPNG_ADDRESS()),
    ]

PMCAST_SCOPE_CTX = Ptr("<I", MCAST_SCOPE_CTX())

class MCAST_SCOPE_ENTRY(MemStruct):
    fields = [
        ("ScopeCtx", MCAST_SCOPE_CTX()),
        ("LastAddr", IPNG_ADDRESS()),
        ("TTL", DWORD()),
        ("ScopeDesc", UNICODE_STRING()),
    ]

PMCAST_SCOPE_ENTRY = Ptr("<I", MCAST_SCOPE_ENTRY())

class DHCPCAPI_CLASSID(MemStruct):
    fields = [
        ("Flags", ULONG()),
        ("Data", LPBYTE()),
        ("nBytesData", ULONG()),
    ]

LPDHCPCAPI_CLASSID = Ptr("<I", DHCPCAPI_CLASSID())

class DHCPAPI_PARAMS(MemStruct):
    fields = [
        ("Flags", ULONG()),
        ("OptionId", ULONG()),
        ("IsVendor", BOOL()),
        ("Data", LPBYTE()),
        ("nBytesData", DWORD()),
    ]

LPDHCPCAPI_PARAMS = Ptr("<I", DHCPAPI_PARAMS())

class DHCPCAPI_PARAMS_ARRAY(MemStruct):
    fields = [
        ("nParams", ULONG()),
        ("Params", LPDHCPCAPI_PARAMS()),
    ]


class MCAST_CLIENT_UID(MemStruct):
    fields = [
        ("ClientUID", LPBYTE()),
        ("ClientUIDLength", DWORD()),
    ]

LPMCAST_CLIENT_UID = Ptr("<I", MCAST_CLIENT_UID())

###################

###### Functions ######

def dhcpcsvc_DhcpCApiCleanup(jitter):
    """
    VOID DhcpCApiCleanup()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc_DhcpDeRegisterParamChange(jitter):
    """
    [ERROR_CODE] DhcpDeRegisterParamChange(
        DWORD Flags,
        LPVOID Reserved,
        LPVOID Event
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Reserved", "Event"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc_DhcpRegisterParamChange(jitter):
    """
    [ERROR_CODE] DhcpRegisterParamChange(
        DWORD Flags,
        LPVOID Reserved,
        LPWSTR AdapterName,
        LPDHCPCAPI_CLASSID pClassId,
        DHCPCAPI_PARAMS_ARRAY Params,
        LPVOID Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Reserved", "AdapterName", "pClassId", "Params", "Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc_DhcpRequestParams(jitter):
    """
    [ERROR_CODE] DhcpRequestParams(
        DWORD Flags,
        LPVOID Reserved,
        LPWSTR AdapterName,
        LPDHCPCAPI_CLASSID ClassId,
        DHCPCAPI_PARAMS_ARRAY SendParams,
        DHCPCAPI_PARAMS_ARRAY RecdParams,
        LPBYTE Buffer,
        LPDWORD pSize,
        LPWSTR RequestIdStr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Reserved", "AdapterName", "ClassId", "SendParams", "RecdParams", "Buffer", "pSize", "RequestIdStr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc_DhcpRemoveDNSRegistrations(jitter):
    """
    [ERROR_CODE] DhcpRemoveDNSRegistrations()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc_DhcpUndoRequestParams(jitter):
    """
    [ERROR_CODE] DhcpUndoRequestParams(
        DWORD Flags,
        LPVOID Reserved,
        LPWSTR AdapterName,
        LPWSTR RequestIdStr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Reserved", "AdapterName", "RequestIdStr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc_DhcpCApiInitialize(jitter):
    """
    [ERROR_CODE] DhcpCApiInitialize(
        LPDWORD Version
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Version"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc_McastApiCleanup(jitter):
    """
    VOID McastApiCleanup()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc_McastApiStartup(jitter):
    """
    [ERROR_CODE] McastApiStartup(
        PDWORD pVersion
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc_McastEnumerateScopes(jitter):
    """
    [ERROR_CODE] McastEnumerateScopes(
        IP_ADDR_FAMILY AddrFamily,
        BOOL ReQuery,
        PMCAST_SCOPE_ENTRY pScopeList,
        PDWORD pScopeLen,
        PDWORD pScopeCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AddrFamily", "ReQuery", "pScopeList", "pScopeLen", "pScopeCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc_McastGenUID(jitter):
    """
    [ERROR_CODE] McastGenUID(
        LPMCAST_CLIENT_UID pRequestID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRequestID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc_McastReleaseAddress(jitter):
    """
    [ERROR_CODE] McastReleaseAddress(
        IP_ADDR_FAMILY AddrFamily,
        LPMCAST_CLIENT_UID pRequestID,
        PMCAST_LEASE_REQUEST pReleaseRequest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AddrFamily", "pRequestID", "pReleaseRequest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc_McastRenewAddress(jitter):
    """
    [ERROR_CODE] McastRenewAddress(
        IP_ADDR_FAMILY AddrFamily,
        LPMCAST_CLIENT_UID pRequestID,
        PMCAST_LEASE_REQUEST pRenewRequest,
        PMCAST_LEASE_RESPONSE pRenewResponse
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AddrFamily", "pRequestID", "pRenewRequest", "pRenewResponse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc_McastRequestAddress(jitter):
    """
    [ERROR_CODE] McastRequestAddress(
        IP_ADDR_FAMILY AddrFamily,
        LPMCAST_CLIENT_UID pRequestID,
        PMCAST_SCOPE_CTX pScopeCtx,
        PMCAST_LEASE_REQUEST pAddrRequest,
        PMCAST_LEASE_RESPONSE pAddrResponse
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AddrFamily", "pRequestID", "pScopeCtx", "pAddrRequest", "pAddrResponse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
