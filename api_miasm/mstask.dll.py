
def mstask_GetNetScheduleAccountInformation(jitter):
    """
    [Mstask.dll] HRESULT GetNetScheduleAccountInformation(LPCWSTR pwszServerName, DWORD ccAccount, WCHAR [] wszAccount)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszServerName", "ccAccount", "wszAccount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mstask_SetNetScheduleAccountInformation(jitter):
    """
    [Mstask.dll] HRESULT SetNetScheduleAccountInformation(LPCWSTR pwszServerName, LPCWSTR pwszAccount, LPCWSTR pwszPassword)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszServerName", "pwszAccount", "pwszPassword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
