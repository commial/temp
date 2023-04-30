###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def nlsdl_DownlevelGetParentLocaleLCID(jitter):
    """
    LCID DownlevelGetParentLocaleLCID(
        LCID Locale
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def nlsdl_DownlevelGetParentLocaleName(jitter):
    """
    int DownlevelGetParentLocaleName(
        LCID Locale,
        LPWSTR lpName,
        int cchName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Locale", "lpName", "cchName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def nlsdl_DownlevelLCIDToLocaleName(jitter):
    """
    int DownlevelLCIDToLocaleName(
        LCID Locale,
        LPWSTR lpName,
        int cchName,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Locale", "lpName", "cchName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def nlsdl_DownlevelLocaleNameToLCID(jitter):
    """
    LCID DownlevelLocaleNameToLCID(
        LPWSTR lpName,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
