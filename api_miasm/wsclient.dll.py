
def wsclient_CheckDeveloperLicense(jitter):
    """"
    [WSClient.dll] STDAPI CheckDeveloperLicense(FILETIME* pExpiration)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pExpiration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsclient_AcquireDeveloperLicense(jitter):
    """"
    [WSClient.dll] STDAPI AcquireDeveloperLicense(HWND hwndParent, FILETIME* pExpiration)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "pExpiration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsclient_RemoveDeveloperLicense(jitter):
    """"
    [WSClient.dll] STDAPI RemoveDeveloperLicense(HWND hwndParent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
