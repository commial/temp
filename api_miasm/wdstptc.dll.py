
def wdstptc_WdsTransportClientAddRefBuffer(jitter):
    """"
    [Wdstptc.dll] [ERROR_CODE] WdsTransportClientAddRefBuffer(PVOID pvBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientCancelSession(jitter):
    """"
    [Wdstptc.dll] [ERROR_CODE] WdsTransportClientCancelSession(HANDLE hSessionKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientCloseSession(jitter):
    """"
    [Wdstptc.dll] [ERROR_CODE] WdsTransportClientCloseSession(HANDLE hSessionKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientCompleteReceive(jitter):
    """"
    [Wdstptc.dll] [ERROR_CODE] WdsTransportClientCompleteReceive(HANDLE hSessionKey, HANDLE ulSize, PULARGE_INTEGER pullOffset)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey", "ulSize", "pullOffset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientInitialize(jitter):
    """"
    [Wdstptc.dll] [ERROR_CODE] WdsTransportClientInitialize()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientInitializeSession(jitter):
    """"
    [Wdstptc.dll] [ERROR_CODE] WdsTransportClientInitializeSession(PWDS_TRANSPORTCLIENT_REQUEST pSessionRequest, PVOID pCallerData, PHANDLE hSessionKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSessionRequest", "pCallerData", "hSessionKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientQueryStatus(jitter):
    """"
    [Wdstptc.dll] [ERROR_CODE] WdsTransportClientQueryStatus(HANDLE hSessionKey, PULONG puStatus, PULONG puErrorCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey", "puStatus", "puErrorCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientRegisterCallback(jitter):
    """"
    [Wdstptc.dll] [ERROR_CODE] WdsTransportClientRegisterCallback(HANDLE hSessionKey, TRANSPORTCLIENT_CALLBACK_ID CallbackId, PVOID pfnCallback)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey", "CallbackId", "pfnCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientReleaseBuffer(jitter):
    """"
    [Wdstptc.dll] [ERROR_CODE] WdsTransportClientReleaseBuffer(PVOID pvBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientShutdown(jitter):
    """"
    [Wdstptc.dll] [ERROR_CODE] WdsTransportClientShutdown()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientStartSession(jitter):
    """"
    [Wdstptc.dll] [ERROR_CODE] WdsTransportClientStartSession(HANDLE hSessionKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdstptc_WdsTransportClientWaitForCompletion(jitter):
    """"
    [Wdstptc.dll] [ERROR_CODE] WdsTransportClientWaitForCompletion(HANDLE hSessionKey, ULONG uTimeout)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSessionKey", "uTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
