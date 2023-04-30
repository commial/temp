
def idndl_DownlevelGetLocaleScripts(jitter):
    """
    int DownlevelGetLocaleScripts(
        LPCWSTR lpLocaleName,
        LPWSTR lpScripts,
        int cchScripts
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName", "lpScripts", "cchScripts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def idndl_DownlevelGetStringScripts(jitter):
    """
    int DownlevelGetStringScripts(
        DWORD dwFlags,
        LPCWSTR lpString,
        int cchString,
        LPWSTR lpScripts,
        int cchScripts
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpString", "cchString", "lpScripts", "cchScripts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def idndl_DownlevelVerifyScripts(jitter):
    """
    BOOL DownlevelVerifyScripts(
        DWORD dwFlags,
        LPCWSTR lpLocaleScripts,
        int cchLocaleScripts,
        LPCWSTR lpTestScripts,
        int cchTestScripts
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpLocaleScripts", "cchLocaleScripts", "lpTestScripts", "cchTestScripts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
