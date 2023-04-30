WCM_PROPERTY = {
    "wcm_global_property_domain_policy": 0,
    "wcm_global_property_minimize_policy": 1,
    "wcm_global_property_roaming_policy": 2,
    "wcm_global_property_powermanagement_policy": 3,
    "wcm_intf_property_connection_cost": 4,
    "wcm_intf_property_dataplan_status": 5,
    "wcm_intf_property_hotspot_profile": 6,
}
WCM_MEDIA_TYPE = {
    "wcm_media_unknown": 0,
    "wcm_media_ethernet": 1,
    "wcm_media_wlan": 2,
    "wcm_media_mbn": 3,
    "wcm_media_invalid": 4,
}

def wcmapi_WcmFreeMemory(jitter):
    """
    VOID WcmFreeMemory(
        PVOID pMemory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMemory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wcmapi_WcmGetProfileList(jitter):
    """
    [ERROR_CODE] WcmGetProfileList(
        PVOID pReserved,
        PWCM_PROFILE_INFO_LIST* ppProfileList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pReserved", "ppProfileList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wcmapi_WcmQueryProperty(jitter):
    """
    [ERROR_CODE] WcmQueryProperty(
        const GUID* pInterface,
        LPCWSTR strProfileName,
        WCM_PROPERTY Property,
        PVOID pReserved,
        PDWORD pdwDataSize,
        PBYTE* ppData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pInterface", "strProfileName", "Property", "pReserved", "pdwDataSize", "ppData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wcmapi_WcmSetProfileList(jitter):
    """
    [ERROR_CODE] WcmSetProfileList(
        WCM_PROFILE_INFO_LIST* pProfileList,
        DWORD dwPosition,
        BOOL fIgnoreUnknownProfiles,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProfileList", "dwPosition", "fIgnoreUnknownProfiles", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wcmapi_WcmSetProperty(jitter):
    """
    [ERROR_CODE] WcmSetProperty(
        const GUID* pInterface,
        LPCWSTR strProfileName,
        WCM_PROPERTY Property,
        PVOID pReserved,
        DWORD dwDataSize,
        const BYTE* pbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pInterface", "strProfileName", "Property", "pReserved", "dwDataSize", "pbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
