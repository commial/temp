
def dsuiext_DsBrowseForContainer(jitter, get_str, set_str):
    """
    int DsBrowseForContainer(
        PDSBROWSEINFO pInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsuiext_DsBrowseForContainerA(jitter):
    dsuiext_DsBrowseForContainer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dsuiext_DsBrowseForContainerW(jitter):
    dsuiext_DsBrowseForContainer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dsuiext_DsGetFriendlyClassName(jitter):
    """
    HRESULT DsGetFriendlyClassName(
        LPWSTR pszObjectClass,
        LPWSTR pszBuffer,
        INT cchBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszObjectClass", "pszBuffer", "cchBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsuiext_DsGetIcon(jitter):
    """
    HICON DsGetIcon(
        DWORD dwFlags,
        LPWSTR pszObjectClass,
        INT cxImage,
        INT cyImage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pszObjectClass", "cxImage", "cyImage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
