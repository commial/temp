
def dssec_DSCreateSecurityPage(jitter):
    """"
    [DSSec.dll] STDAPI DSCreateSecurityPage(LPCWSTR pwszObjectPath, LPCWSTR pwszObjectClass, [DSSI_FLAGS] dwFlags, HPROPSHEETPAGE* phPage, PFNREADOBJECTSECURITY pfnReadSD, PFNWRITEOBJECTSECURITY pfnWriteSD, LPARAM lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszObjectPath", "pwszObjectClass", "dwFlags", "phPage", "pfnReadSD", "pfnWriteSD", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dssec_DSCreateISecurityInfoObject(jitter):
    """"
    [DSSec.dll] STDAPI DSCreateISecurityInfoObject(LPCWSTR pwszObjectClass, [DSSI_FLAGS] dwFlags, LPSECURITYINFO* ppSI, PFNREADOBJECTSECURITY pfnReadSD, PFNWRITEOBJECTSECURITY pfnWriteSD, LPARAM lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszObjectClass", "dwFlags", "ppSI", "pfnReadSD", "pfnWriteSD", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dssec_DSCreateISecurityInfoObjectEx(jitter):
    """"
    [DSSec.dll] STDAPI DSCreateISecurityInfoObjectEx(LPCWSTR pwszObjectPath, LPCWSTR pwszObjectClass, LPCWSTR pwszServer, LPCWSTR pwszUserName, LPCWSTR pwszPassword, [DSSI_FLAGS] dwFlags, LPSECURITYINFO* ppSI, PFNREADOBJECTSECURITY pfnReadSD, PFNWRITEOBJECTSECURITY pfnWriteSD, LPARAM lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszObjectPath", "pwszObjectClass", "pwszServer", "pwszUserName", "pwszPassword", "dwFlags", "ppSI", "pfnReadSD", "pfnWriteSD", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dssec_DSEditSecurity(jitter):
    """"
    [DSSec.dll] STDAPI DSEditSecurity(HWND hwndOwner, LPCWSTR pwszObjectPath, LPCWSTR pwszObjectClass, [DSSI_FLAGS] dwFlags, LPCWSTR pwszCaption, PFNREADOBJECTSECURITY pfnReadSD, PFNWRITEOBJECTSECURITY pfnWriteSD, LPARAM lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "pwszObjectPath", "pwszObjectClass", "dwFlags", "pwszCaption", "pfnReadSD", "pfnWriteSD", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
