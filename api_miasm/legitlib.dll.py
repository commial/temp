###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def legitlib_GetLastErrors(jitter):
    """
    HRESULT GetLastErrors(
        WCHAR** ppwszTrace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppwszTrace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def legitlib_IsAlreadyGenuine(jitter):
    """
    bool IsAlreadyGenuine()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def legitlib_LegitCheck(jitter):
    """
    int LegitCheck()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def legitlib_SetPartnerID(jitter):
    """
    HRESULT SetPartnerID(
        int nPartnerID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nPartnerID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
