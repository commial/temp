###### Enums ######
ATTRIBUTE_TYPE = {
    "AT_INVALID": 0,
    "AT_BOOLEAN": 1,
    "AT_INT8": 2,
    "AT_UINT8": 3,
    "AT_INT16": 4,
    "AT_UINT16": 5,
    "AT_INT32": 6,
    "AT_UINT32": 7,
    "AT_INT64": 8,
    "AT_UINT64": 9,
    "AT_STRING": 10,
    "AT_GUID": 11,
    "AT_LIFE_TIME": 12,
    "AT_SOCKADDR": 13,
    "AT_OCTET_STRING": 14,
}
ATTRIBUTE_TYPE_INV = {
    0: "AT_INVALID",
    1: "AT_BOOLEAN",
    2: "AT_INT8",
    3: "AT_UINT8",
    4: "AT_INT16",
    5: "AT_UINT16",
    6: "AT_INT32",
    7: "AT_UINT32",
    8: "AT_INT64",
    9: "AT_UINT64",
    10: "AT_STRING",
    11: "AT_GUID",
    12: "AT_LIFE_TIME",
    13: "AT_SOCKADDR",
    14: "AT_OCTET_STRING",
}

###################

###### Types ######
NDFHANDLE = PVOID
NDFHANDLE_PTR = Ptr("<I", NDFHANDLE())
CHAR__126_ = Array(CHAR, 126)
ATTRIBUTE_TYPE = UINT

class OCTET_STRING(MemStruct):
    fields = [
        ("dwLength", DWORD()),
        ("lpValue", BYTE_PTR()),
    ]


class LIFE_TIME(MemStruct):
    fields = [
        ("startTime", FILETIME()),
        ("endTime", FILETIME()),
    ]


class DIAG_SOCKADDR(MemStruct):
    fields = [
        ("family", USHORT()),
        ("data", CHAR__126_()),
    ]

_HELPER_ATTRIBUTE_u_ = Union([
    ("Boolean", BOOL),
    ("Char", char),
    ("Byte", byte),
    ("Short", short),
    ("Word", WORD),
    ("Int", int),
    ("DWord", DWORD),
    ("Int64", LONGLONG),
    ("UInt64", ULONGLONG),
    ("PWStr", LPWSTR),
    ("Guid", GUID),
    ("LifeTime", LIFE_TIME),
    ("Address", DIAG_SOCKADDR),
    ("OctetString", OCTET_STRING),
])

class HELPER_ATTRIBUTE(MemStruct):
    fields = [
        ("pwszName", LPWSTR()),
        ("type", ATTRIBUTE_TYPE()),
        (None, _HELPER_ATTRIBUTE_u_()),
    ]

HELPER_ATTRIBUTE_PTR = Ptr("<I", HELPER_ATTRIBUTE())

###################

###### Functions ######

def ndfapi_NdfCloseIncident(jitter):
    """
    HRESULT NdfCloseIncident(
        NDFHANDLE handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateConnectivityIncident(jitter):
    """
    HRESULT NdfCreateConnectivityIncident(
        NDFHANDLE* handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateDNSIncident(jitter):
    """
    HRESULT NdfCreateDNSIncident(
        LPCWSTR hostname,
        WORD querytype,
        NDFHANDLE* handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hostname", "querytype", "handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateIncident(jitter):
    """
    HRESULT NdfCreateIncident(
        LPCWSTR helperClassName,
        ULONG celt,
        HELPER_ATTRIBUTE* attributes,
        NDFHANDLE* handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["helperClassName", "celt", "attributes", "handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateSharingIncident(jitter):
    """
    HRESULT NdfCreateSharingIncident(
        LPCWSTR sharename,
        NDFHANDLE* handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sharename", "handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateWebIncident(jitter):
    """
    HRESULT NdfCreateWebIncident(
        LPCWSTR url,
        NDFHANDLE* handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["url", "handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateWebIncidentEx(jitter):
    """
    HRESULT NdfCreateWebIncidentEx(
        LPCWSTR url,
        BOOL useWinHTTP,
        LPWSTR moduleName,
        NDFHANDLE* handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["url", "useWinHTTP", "moduleName", "handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateWinSockIncident(jitter):
    """
    HRESULT NdfCreateWinSockIncident(
        SOCKET sock,
        LPCWSTR host,
        USHORT port,
        LPCWSTR appID,
        SID* userId,
        NDFHANDLE* handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sock", "host", "port", "appID", "userId", "handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfExecuteDiagnosis(jitter):
    """
    HRESULT NdfExecuteDiagnosis(
        NDFHANDLE handle,
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["handle", "hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateNetConnectionIncident(jitter):
    """
    HRESULT NdfCreateNetConnectionIncident(
        NDFHANDLE* handle,
        GUID id
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["handle", "id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
