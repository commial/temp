###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def jsproxy_InternetDeInitializeAutoProxyDll(jitter):
    """
    BOOL InternetDeInitializeAutoProxyDll(
        LPSTR lpszMime,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszMime", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def jsproxy_InternetGetProxyInfo(jitter):
    """
    BOOL InternetGetProxyInfo(
        LPCSTR lpszUrl,
        DWORD dwUrlLength,
        LPSTR lpszUrlHostName,
        DWORD dwUrlHostNameLength,
        LPSTR* lplpszProxyHostName,
        LPDWORD lpdwProxyHostNameLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrl", "dwUrlLength", "lpszUrlHostName", "dwUrlHostNameLength", "lplpszProxyHostName", "lpdwProxyHostNameLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def jsproxy_InternetInitializeAutoProxyDll(jitter):
    """
    BOOL InternetInitializeAutoProxyDll(
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
