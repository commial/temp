
def aclui_CreateSecurityPage(jitter):
    """
    HPROPSHEETPAGE CreateSecurityPage(
        LPSECURITYINFO psi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def aclui_EditSecurity(jitter):
    """
    BOOL EditSecurity(
        HWND hwndOwner,
        LPSECURITYINFO psi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "psi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def aclui_EditSecurityAdvanced(jitter):
    """
    HRESULT EditSecurityAdvanced(
        HWND hwndOwner,
        LPSECURITYINFO psi,
        SI_PAGE_TYPE uSIPage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "psi", "uSIPage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
