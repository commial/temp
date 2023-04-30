###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def cscapi_CscSearchApiGetInterface(jitter):
    """
    NTSTATUS CscSearchApiGetInterface(
        ULONG Version,
        ULONG Cookie,
        CCscSearchApiInterface** Interface
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Version", "Cookie", "Interface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cscapi_OfflineFilesEnable(jitter):
    """
    [ERROR_CODE] OfflineFilesEnable(
        BOOL bEnable,
        BOOL* pbRebootRequired
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bEnable", "pbRebootRequired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cscapi_OfflineFilesQueryStatus(jitter):
    """
    [ERROR_CODE] OfflineFilesQueryStatus(
        BOOL* pbActive,
        BOOL* pbEnabled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbActive", "pbEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cscapi_OfflineFilesQueryStatusEx(jitter):
    """
    [ERROR_CODE] OfflineFilesQueryStatusEx(
        BOOL* pbActive,
        BOOL* pbEnabled,
        BOOL* pbAvailable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbActive", "pbEnabled", "pbAvailable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cscapi_OfflineFilesStart(jitter):
    """
    [ERROR_CODE] OfflineFilesStart()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
