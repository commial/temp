
def ntshrui_CanShareFolderW(jitter):
    """"
    [Ntshrui.dll] STDAPI CanShareFolderW(LPCWSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntshrui_ShowShareFolderUI(jitter):
    """"
    [Ntshrui.dll] HRESULT ShowShareFolderUI(HWND hwndParent, LPCWSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
