
def wlanui_WlanUIEditProfile(jitter):
    """
    [Wlanui.dll] [ERROR_CODE] WlanUIEditProfile(DWORD dwClientVersion, LPCWSTR wstrProfileName, GUID* pInterfaceGuid, HWND hWnd, WL_DISPLAY_PAGES wlStartPage, PVOID pReserved, PWLAN_REASON_CODE pWlanReasonCode)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwClientVersion", "wstrProfileName", "pInterfaceGuid", "hWnd", "wlStartPage", "pReserved", "pWlanReasonCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
