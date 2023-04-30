GROUP_POLICY_OBJECT_TYPE = {
    "GPOTypeLocal": 0,
    "GPOTypeRemote": 1,
    "GPOTypeDS": 2,
    "GPOTypeLocalUser": 3,
    "GPOTypeLocalGroup": 4,
}
GROUP_POLICY_HINT_TYPE = {
    "GPHintUnknown": 0,
    "GPHintMachine": 1,
    "GPHintSite": 2,
    "GPHintDomain": 3,
    "GPHintOrganizationalUnit": 4,
}

def gpedit_BrowseForGPO(jitter):
    """
    HRESULT BrowseForGPO(
        LPGPOBROWSEINFO lpBrowseInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpBrowseInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gpedit_CreateGPOLink(jitter):
    """
    HRESULT CreateGPOLink(
        LPOLESTR lpGPO,
        LPOLESTR lpContainer,
        BOOL fHighPriority
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpGPO", "lpContainer", "fHighPriority"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gpedit_DeleteAllGPOLinks(jitter):
    """
    HRESULT DeleteAllGPOLinks(
        LPOLESTR lpContainer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpContainer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gpedit_DeleteGPOLink(jitter):
    """
    HRESULT DeleteGPOLink(
        LPOLESTR lpGPO,
        LPOLESTR lpContainer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpGPO", "lpContainer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gpedit_ExportRSoPData(jitter):
    """
    HRESULT ExportRSoPData(
        LPOLESTR lpNameSpace,
        LPOLESTR lpFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpNameSpace", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gpedit_ImportRSoPData(jitter):
    """
    HRESULT ImportRSoPData(
        LPOLESTR lpNameSpace,
        LPOLESTR lpFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpNameSpace", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
