
def dsuiext_DsBrowseForContainer(jitter):
    """"
    [Dsuiext.dll] int DsBrowseForContainer(PDSBROWSEINFO pInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsuiext_DsGetFriendlyClassName(jitter):
    """"
    [Dsuiext.dll] HRESULT DsGetFriendlyClassName(LPWSTR pszObjectClass, LPWSTR pszBuffer, INT cchBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszObjectClass", "pszBuffer", "cchBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsuiext_DsGetIcon(jitter):
    """"
    [Dsuiext.dll] HICON DsGetIcon(DWORD dwFlags, LPWSTR pszObjectClass, INT cxImage, INT cyImage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pszObjectClass", "cxImage", "cyImage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
