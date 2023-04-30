###### Enums ######
_WdsAuthLevel_ = {
    "WDS_TRANSPORTCLIENT_AUTH": 0x1,
    "WDS_TRANSPORTCLIENT_NO_AUTH": 0x2,
}
_WdsAuthLevel__INV = {
    0x1: "WDS_TRANSPORTCLIENT_AUTH",
    0x2: "WDS_TRANSPORTCLIENT_NO_AUTH",
}
TRANSPORTCLIENT_CALLBACK_ID = {
    "WDS_TRANSPORTCLIENT_SESSION_START": 0,
    "WDS_TRANSPORTCLIENT_RECEIVE_CONTENTS": 1,
    "WDS_TRANSPORTCLIENT_SESSION_COMPLETE": 2,
    "WDS_TRANSPORTCLIENT_RECEIVE_METADATA": 3,
    "WDS_TRANSPORTCLIENT_SESSION_STARTEX": 4,
}
TRANSPORTCLIENT_CALLBACK_ID_INV = {
    0: "WDS_TRANSPORTCLIENT_SESSION_START",
    1: "WDS_TRANSPORTCLIENT_RECEIVE_CONTENTS",
    2: "WDS_TRANSPORTCLIENT_SESSION_COMPLETE",
    3: "WDS_TRANSPORTCLIENT_RECEIVE_METADATA",
    4: "WDS_TRANSPORTCLIENT_SESSION_STARTEX",
}

###################

###### Types ######
_WdsAuthLevel_ = ULONG

class WDS_TRANSPORTCLIENT_REQUEST(MemStruct):
    fields = [
        ("ulLength", ULONG()),
        ("ulApiVersion", ULONG()),
        ("ulAuthLevel", _WdsAuthLevel_()),
        ("pwszServer", LPCWSTR()),
        ("pwszNamespace", LPCWSTR()),
        ("pwszObjectName", LPCWSTR()),
        ("ulCacheSize", ULONG()),
        ("ulProtocol", ULONG()),
        # Length is `ulProtocolDataLength`
        ("pvProtocolData", PVOID()),
        ("ulProtocolDataLength", ULONG()),
    ]

PWDS_TRANSPORTCLIENT_REQUEST = Ptr("<I", WDS_TRANSPORTCLIENT_REQUEST())
TRANSPORTCLIENT_CALLBACK_ID = UINT

###################

###### Functions ######

def wdstptc_WdsTransportClientAddRefBuffer(jitter):
    """
    [ERROR_CODE] WdsTransportClientAddRefBuffer(
        PVOID pvBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientCancelSession(jitter):
    """
    [ERROR_CODE] WdsTransportClientCancelSession(
        HANDLE hSessionKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientCloseSession(jitter):
    """
    [ERROR_CODE] WdsTransportClientCloseSession(
        HANDLE hSessionKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientCompleteReceive(jitter):
    """
    [ERROR_CODE] WdsTransportClientCompleteReceive(
        HANDLE hSessionKey,
        HANDLE ulSize,
        PULARGE_INTEGER pullOffset
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey", "ulSize", "pullOffset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientInitialize(jitter):
    """
    [ERROR_CODE] WdsTransportClientInitialize()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientInitializeSession(jitter):
    """
    [ERROR_CODE] WdsTransportClientInitializeSession(
        PWDS_TRANSPORTCLIENT_REQUEST pSessionRequest,
        PVOID pCallerData,
        PHANDLE hSessionKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSessionRequest", "pCallerData", "hSessionKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientQueryStatus(jitter):
    """
    [ERROR_CODE] WdsTransportClientQueryStatus(
        HANDLE hSessionKey,
        PULONG puStatus,
        PULONG puErrorCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey", "puStatus", "puErrorCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientRegisterCallback(jitter):
    """
    [ERROR_CODE] WdsTransportClientRegisterCallback(
        HANDLE hSessionKey,
        TRANSPORTCLIENT_CALLBACK_ID CallbackId,
        PVOID pfnCallback
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey", "CallbackId", "pfnCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientReleaseBuffer(jitter):
    """
    [ERROR_CODE] WdsTransportClientReleaseBuffer(
        PVOID pvBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientShutdown(jitter):
    """
    [ERROR_CODE] WdsTransportClientShutdown()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientStartSession(jitter):
    """
    [ERROR_CODE] WdsTransportClientStartSession(
        HANDLE hSessionKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientWaitForCompletion(jitter):
    """
    [ERROR_CODE] WdsTransportClientWaitForCompletion(
        HANDLE hSessionKey,
        ULONG uTimeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey", "uTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
