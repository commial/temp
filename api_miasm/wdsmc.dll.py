TRANSPORTPROVIDER_CALLBACK_ID = {
    "WDS_TRANSPORTPROVIDER_CREATE_INSTANCE": 0,
    "WDS_TRANSPORTPROVIDER_COMPARE_CONTENT": 1,
    "WDS_TRANSPORTPROVIDER_OPEN_CONTENT": 2,
    "WDS_TRANSPORTPROVIDER_USER_ACCESS_CHECK": 3,
    "WDS_TRANSPORTPROVIDER_GET_CONTENT_SIZE": 4,
    "WDS_TRANSPORTPROVIDER_READ_CONTENT": 5,
    "WDS_TRANSPORTPROVIDER_CLOSE_CONTENT": 6,
    "WDS_TRANSPORTPROVIDER_CLOSE_INSTANCE": 7,
    "WDS_TRANSPORTPROVIDER_SHUTDOWN": 8,
    "WDS_TRANSPORTPROVIDER_DUMP_STATE": 9,
    "WDS_TRANSPORTPROVIDER_REFRESH_SETTINGS": 10,
    "WDS_TRANSPORTPROVIDER_GET_CONTENT_METADATA": 11,
    "WDS_TRANSPORTPROVIDER_MAX_CALLBACKS": 12,
}
TRANSPORTPROVIDER_CALLBACK_ID_INV = {
    0: "WDS_TRANSPORTPROVIDER_CREATE_INSTANCE",
    1: "WDS_TRANSPORTPROVIDER_COMPARE_CONTENT",
    2: "WDS_TRANSPORTPROVIDER_OPEN_CONTENT",
    3: "WDS_TRANSPORTPROVIDER_USER_ACCESS_CHECK",
    4: "WDS_TRANSPORTPROVIDER_GET_CONTENT_SIZE",
    5: "WDS_TRANSPORTPROVIDER_READ_CONTENT",
    6: "WDS_TRANSPORTPROVIDER_CLOSE_CONTENT",
    7: "WDS_TRANSPORTPROVIDER_CLOSE_INSTANCE",
    8: "WDS_TRANSPORTPROVIDER_SHUTDOWN",
    9: "WDS_TRANSPORTPROVIDER_DUMP_STATE",
    10: "WDS_TRANSPORTPROVIDER_REFRESH_SETTINGS",
    11: "WDS_TRANSPORTPROVIDER_GET_CONTENT_METADATA",
    12: "WDS_TRANSPORTPROVIDER_MAX_CALLBACKS",
}
WDS_MC_SEVERITY = {
    "WDS_MC_TRACE_VERBOSE": 0x00010000,
    "WDS_MC_TRACE_INFO": 0x00020000,
    "WDS_MC_TRACE_WARNING": 0x00040000,
    "WDS_MC_TRACE_ERROR": 0x00080000,
    "WDS_MC_TRACE_FATAL": 0x00100000,
}
WDS_MC_SEVERITY_INV = {
    0x00010000: "WDS_MC_TRACE_VERBOSE",
    0x00020000: "WDS_MC_TRACE_INFO",
    0x00040000: "WDS_MC_TRACE_WARNING",
    0x00080000: "WDS_MC_TRACE_ERROR",
    0x00100000: "WDS_MC_TRACE_FATAL",
}

def wdsmc_WdsTransportServerAllocateBuffer(jitter):
    """
    PVOID WdsTransportServerAllocateBuffer(
        HANDLE hProvider,
        ULONG ulBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "ulBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsmc_WdsTransportServerCompleteRead(jitter):
    """
    HRESULT WdsTransportServerCompleteRead(
        HANDLE hProvider,
        ULONG ulBytesRead,
        PVOID pvUserData,
        HRESULT hReadResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "ulBytesRead", "pvUserData", "hReadResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsmc_WdsTransportServerFreeBuffer(jitter):
    """
    HRESULT WdsTransportServerFreeBuffer(
        HANDLE hProvider,
        PVOID pvBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pvBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsmc_WdsTransportServerRegisterCallback(jitter):
    """
    HRESULT WdsTransportServerRegisterCallback(
        HANDLE hProvider,
        TRANSPORTPROVIDER_CALLBACK_ID CallbackId,
        PVOID pfnCallback
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "CallbackId", "pfnCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsmc_WdsTransportServerTrace(jitter):
    """
    HRESULT WdsTransportServerTrace(
        HANDLE hProvider,
        WDS_MC_SEVERITY Severity,
        LPCWSTR pwszFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "Severity", "pwszFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsmc_WdsTransportServerTraceV(jitter):
    """
    HRESULT WdsTransportServerTraceV(
        HANDLE hProvider,
        WDS_MC_SEVERITY Severity,
        LPCWSTR pwszFormat,
        va_list Params
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "Severity", "pwszFormat", "Params"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
