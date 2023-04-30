
def ntshrui_CanShareFolderW(jitter):
    """
    STDAPI CanShareFolderW(
        LPCWSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntshrui_ShowShareFolderUI(jitter):
    """
    HRESULT ShowShareFolderUI(
        HWND hwndParent,
        LPCWSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
