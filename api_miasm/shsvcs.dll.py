###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def shsvcs_CreateHardwareEventMoniker(jitter):
    """
    HRESULT CreateHardwareEventMoniker(
        REFCLSID clsid,
        LPCTSTR pszEventHandler,
        IMoniker** ppmoniker
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsid", "pszEventHandler", "ppmoniker"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
