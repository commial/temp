
def gpedit_BrowseForGPO(jitter):
    """"
    [Gpedit.dll] HRESULT BrowseForGPO(LPGPOBROWSEINFO lpBrowseInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBrowseInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gpedit_CreateGPOLink(jitter):
    """"
    [Gpedit.dll] HRESULT CreateGPOLink(LPOLESTR lpGPO, LPOLESTR lpContainer, BOOL fHighPriority)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpGPO", "lpContainer", "fHighPriority"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gpedit_DeleteAllGPOLinks(jitter):
    """"
    [Gpedit.dll] HRESULT DeleteAllGPOLinks(LPOLESTR lpContainer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpContainer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gpedit_DeleteGPOLink(jitter):
    """"
    [Gpedit.dll] HRESULT DeleteGPOLink(LPOLESTR lpGPO, LPOLESTR lpContainer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpGPO", "lpContainer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gpedit_ExportRSoPData(jitter):
    """"
    [Gpedit.dll] HRESULT ExportRSoPData(LPOLESTR lpNameSpace, LPOLESTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpNameSpace", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gpedit_ImportRSoPData(jitter):
    """"
    [Gpedit.dll] HRESULT ImportRSoPData(LPOLESTR lpNameSpace, LPOLESTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpNameSpace", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
