
def wdsmc_WdsTransportServerAllocateBuffer(jitter):
    """
    [Wdsmc.dll] PVOID WdsTransportServerAllocateBuffer(HANDLE hProvider, ULONG ulBufferSize)
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "ulBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsmc_WdsTransportServerCompleteRead(jitter):
    """
    [Wdsmc.dll] HRESULT WdsTransportServerCompleteRead(HANDLE hProvider, ULONG ulBytesRead, PVOID pvUserData, HRESULT hReadResult)
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "ulBytesRead", "pvUserData", "hReadResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsmc_WdsTransportServerFreeBuffer(jitter):
    """
    [Wdsmc.dll] HRESULT WdsTransportServerFreeBuffer(HANDLE hProvider, PVOID pvBuffer)
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pvBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsmc_WdsTransportServerRegisterCallback(jitter):
    """
    [Wdsmc.dll] HRESULT WdsTransportServerRegisterCallback(HANDLE hProvider, TRANSPORTPROVIDER_CALLBACK_ID CallbackId, PVOID pfnCallback)
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "CallbackId", "pfnCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsmc_WdsTransportServerTrace(jitter):
    """
    [Wdsmc.dll] HRESULT WdsTransportServerTrace(HANDLE hProvider, WDS_MC_SEVERITY Severity, LPCWSTR pwszFormat)
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "Severity", "pwszFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsmc_WdsTransportServerTraceV(jitter):
    """
    [Wdsmc.dll] HRESULT WdsTransportServerTraceV(HANDLE hProvider, WDS_MC_SEVERITY Severity, LPCWSTR pwszFormat, va_list Params)
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "Severity", "pwszFormat", "Params"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
