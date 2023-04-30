
def sensapi_IsDestinationReachable(jitter):
    """"
    [SensAPI.dll] BOOL IsDestinationReachable(LPCSTR lpszDestination, LPQOCINFO lpQOCInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDestination", "lpQOCInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sensapi_IsNetworkAlive(jitter):
    """"
    [SensAPI.dll] BOOL IsNetworkAlive([NetworkAliveFlags*] lpdwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
