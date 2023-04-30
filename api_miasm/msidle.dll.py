###### Enums ######

###################

###### Types ######
_IDLECALLBACK = LPVOID

###################

###### Functions ######

def msidle_BeginIdleDetection(jitter):
    """
    [ERROR_CODE] BeginIdleDetection(
        _IDLECALLBACK pfnCallback,
        DWORD dwIdleMin,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfnCallback", "dwIdleMin", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msidle_EndIdleDetection(jitter):
    """
    BOOL EndIdleDetection(
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msidle_GetIdleMinutes(jitter):
    """
    DWORD GetIdleMinutes(
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
