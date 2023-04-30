###### Enums ######
SI_PAGE_TYPE = {
    "SI_PAGE_PERM": 0,
    "SI_PAGE_ADVPERM": 1,
    "SI_PAGE_AUDIT": 2,
    "SI_PAGE_OWNER": 3,
    "SI_PAGE_EFFECTIVE": 4,
    "SI_PAGE_TAKEOWNERSHIP": 5,
}
SI_PAGE_TYPE_INV = {
    0: "SI_PAGE_PERM",
    1: "SI_PAGE_ADVPERM",
    2: "SI_PAGE_AUDIT",
    3: "SI_PAGE_OWNER",
    4: "SI_PAGE_EFFECTIVE",
    5: "SI_PAGE_TAKEOWNERSHIP",
}

###################

###### Types ######
SI_PAGE_TYPE = UINT

###################

###### Functions ######

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
