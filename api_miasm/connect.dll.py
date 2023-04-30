
def connect_CreateVPNConnection(jitter):
    """
    HRESULT CreateVPNConnection(
        HWND hwndParent,
        DWORD dwWizardType,
        DWORD dwContextFlags,
        DWORD dwUserFlags,
        HANDLE hUserContext,
        LPWSTR pszCommandLine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "dwWizardType", "dwContextFlags", "dwUserFlags", "hUserContext", "pszCommandLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def connect_GetInternetConnected(jitter):
    """
    HRESULT GetInternetConnected(
        HWND hwndParent,
        DWORD dwWizardType,
        DWORD dwContextFlags,
        DWORD dwUserFlags,
        HANDLE hUserContext,
        LPWSTR pszCommandLine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "dwWizardType", "dwContextFlags", "dwUserFlags", "hUserContext", "pszCommandLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def connect_GetNetworkConnected(jitter):
    """
    HRESULT GetNetworkConnected(
        HWND hwndParent,
        DWORD dwWizardType,
        DWORD dwContextFlags,
        DWORD dwUserFlags,
        HANDLE hUserContext,
        LPWSTR pszCommandLine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "dwWizardType", "dwContextFlags", "dwUserFlags", "hUserContext", "pszCommandLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def connect_GetVPNConnected(jitter):
    """
    HRESULT GetVPNConnected(
        HWND hwndParent,
        DWORD dwWizardType,
        DWORD dwContextFlags,
        DWORD dwUserFlags,
        HANDLE hUserContext,
        LPWSTR pszCommandLine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "dwWizardType", "dwContextFlags", "dwUserFlags", "hUserContext", "pszCommandLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def connect_IsInternetConnected(jitter):
    """
    HRESULT IsInternetConnected()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def connect_RegisterPageWithPage(jitter):
    """
    HRESULT RegisterPageWithPage(
        GUID* pguidParentPage,
        GUID* pguidChildPage,
        LPWSTR pszChildModuleFileName,
        LPWSTR pszFriendlyName,
        DWORD dwBehaviorFlags,
        DWORD dwUserFlags,
        LPWSTR pszCommandLine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pguidParentPage", "pguidChildPage", "pszChildModuleFileName", "pszFriendlyName", "dwBehaviorFlags", "dwUserFlags", "pszCommandLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def connect_UnregisterPage(jitter):
    """
    HRESULT UnregisterPage(
        GUID* pguidPage,
        BOOL fUnregisterFromCOM
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pguidPage", "fUnregisterFromCOM"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def connect_UnregisterPagesLink(jitter):
    """
    HRESULT UnregisterPagesLink(
        GUID* pguidParentPage,
        GUID* pguidChildPage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pguidParentPage", "pguidChildPage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
