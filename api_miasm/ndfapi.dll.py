
def ndfapi_NdfCloseIncident(jitter):
    """"
    [Ndfapi.dll] HRESULT NdfCloseIncident(NDFHANDLE handle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateConnectivityIncident(jitter):
    """"
    [Ndfapi.dll] HRESULT NdfCreateConnectivityIncident(NDFHANDLE* handle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateDNSIncident(jitter):
    """"
    [Ndfapi.dll] HRESULT NdfCreateDNSIncident(LPCWSTR hostname, WORD querytype, NDFHANDLE* handle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hostname", "querytype", "handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateIncident(jitter):
    """"
    [Ndfapi.dll] HRESULT NdfCreateIncident(LPCWSTR helperClassName, ULONG celt, HELPER_ATTRIBUTE* attributes, NDFHANDLE* handle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["helperClassName", "celt", "attributes", "handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateSharingIncident(jitter):
    """"
    [Ndfapi.dll] HRESULT NdfCreateSharingIncident(LPCWSTR sharename, NDFHANDLE* handle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sharename", "handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateWebIncident(jitter):
    """"
    [Ndfapi.dll] HRESULT NdfCreateWebIncident(LPCWSTR url, NDFHANDLE* handle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["url", "handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateWebIncidentEx(jitter):
    """"
    [Ndfapi.dll] HRESULT NdfCreateWebIncidentEx(LPCWSTR url, BOOL useWinHTTP, LPWSTR moduleName, NDFHANDLE* handle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["url", "useWinHTTP", "moduleName", "handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateWinSockIncident(jitter):
    """"
    [Ndfapi.dll] HRESULT NdfCreateWinSockIncident(SOCKET sock, LPCWSTR host, USHORT port, LPCWSTR appID, SID* userId, NDFHANDLE* handle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sock", "host", "port", "appID", "userId", "handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfExecuteDiagnosis(jitter):
    """"
    [Ndfapi.dll] HRESULT NdfExecuteDiagnosis(NDFHANDLE handle, HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["handle", "hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ndfapi_NdfCreateNetConnectionIncident(jitter):
    """"
    [Ndfapi.dll] HRESULT NdfCreateNetConnectionIncident(NDFHANDLE* handle, GUID id)
    """"
    ret_ad, args = jitter.func_args_stdcall(["handle", "id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
