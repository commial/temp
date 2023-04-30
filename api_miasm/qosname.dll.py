###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def qosname_WPUGetQOSTemplate(jitter):
    """
    INT WPUGetQOSTemplate(
        const LPGUID lpProviderId,
        LPWSABUF lpQOSName,
        LPQOS lpQOS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpProviderId", "lpQOSName", "lpQOS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def qosname_WSCInstallQOSTemplate(jitter):
    """
    BOOL WSCInstallQOSTemplate(
        const LPGUID lpProviderId,
        LPWSABUF lpQOSName,
        LPQOS lpQOS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpProviderId", "lpQOSName", "lpQOS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def qosname_WSCRemoveQOSTemplate(jitter):
    """
    BOOL WSCRemoveQOSTemplate(
        const LPGUID lpProviderId,
        LPWSABUF lpQOSName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpProviderId", "lpQOSName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
