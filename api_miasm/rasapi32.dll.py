RASAPIVERSION = {
    "RASAPIVERSION_500": 1,
    "RASAPIVERSION_501": 2,
    "RASAPIVERSION_600": 3,
    "RASAPIVERSION_601": 4,
}
RASAPIVERSION_INV = {
    1: "RASAPIVERSION_500",
    2: "RASAPIVERSION_501",
    3: "RASAPIVERSION_600",
    4: "RASAPIVERSION_601",
}
_RASTUNNELENDPOINT_TYPE_ = {
    "RASTUNNELENDPOINT_UNKNOWN": 0,
    "RASTUNNELENDPOINT_IPv4": 1,
    "RASTUNNELENDPOINT_IPv6": 2,
}
_RASTUNNELENDPOINT_TYPE__INV = {
    0: "RASTUNNELENDPOINT_UNKNOWN",
    1: "RASTUNNELENDPOINT_IPv4",
    2: "RASTUNNELENDPOINT_IPv6",
}
RASCONNSTATE = {
    "RASCS_OpenPort": 0,
    "RASCS_PortOpened": 1,
    "RASCS_ConnectDevice": 2,
    "RASCS_DeviceConnected": 3,
    "RASCS_AllDevicesConnected": 4,
    "RASCS_Authenticate": 5,
    "RASCS_AuthNotify": 6,
    "RASCS_AuthRetry": 7,
    "RASCS_AuthCallback": 8,
    "RASCS_AuthChangePassword": 9,
    "RASCS_AuthProject": 10,
    "RASCS_AuthLinkSpeed": 11,
    "RASCS_AuthAck": 12,
    "RASCS_ReAuthenticate": 13,
    "RASCS_Authenticated": 14,
    "RASCS_PrepareForCallback": 15,
    "RASCS_WaitForModemReset": 16,
    "RASCS_WaitForCallback": 17,
    "RASCS_Projected": 18,
    "RASCS_StartAuthentication": 19,
    "RASCS_CallbackComplete": 20,
    "RASCS_LogonNetwork": 21,
    "RASCS_SubEntryConnected": 22,
    "RASCS_SubEntryDisconnected": 23,
    "RASCS_ApplySettings": 24,
    "RASCS_Interactive": 0x1000,
    "RASCS_RetryAuthentication": 0x1001,
    "RASCS_CallbackSetByCaller": 0x1002,
    "RASCS_PasswordExpired": 0x1003,
    "RASCS_InvokeEapUI": 0x1004,
    "RASCS_Connected": 0x2000,
    "RASCS_Disconnected": 0x2001,
}
RASCONNSTATE_INV = {
    0: "RASCS_OpenPort",
    1: "RASCS_PortOpened",
    2: "RASCS_ConnectDevice",
    3: "RASCS_DeviceConnected",
    4: "RASCS_AllDevicesConnected",
    5: "RASCS_Authenticate",
    6: "RASCS_AuthNotify",
    7: "RASCS_AuthRetry",
    8: "RASCS_AuthCallback",
    9: "RASCS_AuthChangePassword",
    10: "RASCS_AuthProject",
    11: "RASCS_AuthLinkSpeed",
    12: "RASCS_AuthAck",
    13: "RASCS_ReAuthenticate",
    14: "RASCS_Authenticated",
    15: "RASCS_PrepareForCallback",
    16: "RASCS_WaitForModemReset",
    17: "RASCS_WaitForCallback",
    18: "RASCS_Projected",
    19: "RASCS_StartAuthentication",
    20: "RASCS_CallbackComplete",
    21: "RASCS_LogonNetwork",
    22: "RASCS_SubEntryConnected",
    23: "RASCS_SubEntryDisconnected",
    24: "RASCS_ApplySettings",
    0x1000: "RASCS_Interactive",
    0x1001: "RASCS_RetryAuthentication",
    0x1002: "RASCS_CallbackSetByCaller",
    0x1003: "RASCS_PasswordExpired",
    0x1004: "RASCS_InvokeEapUI",
    0x2000: "RASCS_Connected",
    0x2001: "RASCS_Disconnected",
}
RASCONNSUBSTATE = {
    "RASCSS_None": 0,
    "RASCSS_Dormant": 1,
    "RASCSS_Reconnecting": 2,
    "RASCSS_Reconnected": 0x2000,
}
RASCONNSUBSTATE_INV = {
    0: "RASCSS_None",
    1: "RASCSS_Dormant",
    2: "RASCSS_Reconnecting",
    0x2000: "RASCSS_Reconnected",
}
_RASEDM_ENUM_ = {
    "RASEDM_DialAll": 1,
    "RASEDM_DialAsNeeded": 2,
}
_RASEDM_ENUM__INV = {
    1: "RASEDM_DialAll",
    2: "RASEDM_DialAsNeeded",
}
_RASET_ENUM_ = {
    "RASET_Phone": 1,
    "RASET_Vpn": 2,
    "RASET_Direct": 3,
    "RASET_Internet": 4,
    "RASET_Broadband": 5,
}
_RASET_ENUM__INV = {
    1: "RASET_Phone",
    2: "RASET_Vpn",
    3: "RASET_Direct",
    4: "RASET_Internet",
    5: "RASET_Broadband",
}
_RAS_ENCRYPTION_TYPE_ = {
    "ET_None": 0,
    "ET_Require": 1,
    "ET_RequireMax": 2,
    "ET_Optional": 3,
}
_RAS_ENCRYPTION_TYPE__INV = {
    0: "ET_None",
    1: "ET_Require",
    2: "ET_RequireMax",
    3: "ET_Optional",
}
_RAS_VPN_STRATEGY_ = {
    "VS_Default": 0,
    "VS_PptpOnly": 1,
    "VS_PptpFirst": 2,
    "VS_L2tpOnly": 3,
    "VS_L2tpFirst": 4,
    "VS_SstpOnly": 5,
    "VS_SstpFirst": 6,
    "VS_Ikev2Only": 7,
    "VS_Ikev2First": 8,
    "VS_PptpSstp": 12,
    "VS_L2tpSstp": 13,
    "VS_Ikev2Sstp": 14,
}
_RAS_VPN_STRATEGY__INV = {
    0: "VS_Default",
    1: "VS_PptpOnly",
    2: "VS_PptpFirst",
    3: "VS_L2tpOnly",
    4: "VS_L2tpFirst",
    5: "VS_SstpOnly",
    6: "VS_SstpFirst",
    7: "VS_Ikev2Only",
    8: "VS_Ikev2First",
    12: "VS_PptpSstp",
    13: "VS_L2tpSstp",
    14: "VS_Ikev2Sstp",
}
_RASLCPAP_ = {
    "RASLCPAP_PAP": 0xC023,
    "RASLCPAP_SPAP": 0xC027,
    "RASLCPAP_CHAP": 0xC223,
    "RASLCPAP_EAP": 0xC227,
}
_RASLCPAP__INV = {
    0xC023: "RASLCPAP_PAP",
    0xC027: "RASLCPAP_SPAP",
    0xC223: "RASLCPAP_CHAP",
    0xC227: "RASLCPAP_EAP",
}
_RASLCPAD_ = {
    "RASLCPAD_CHAP_MD5": 0x05,
    "RASLCPAD_CHAP_MS": 0x80,
    "RASLCPAD_CHAP_MSV2": 0x81,
}
_RASLCPAD__INV = {
    0x05: "RASLCPAD_CHAP_MD5",
    0x80: "RASLCPAD_CHAP_MS",
    0x81: "RASLCPAD_CHAP_MSV2",
}
_RASCCPCA_ = {
    "RASCCPCA_MPPC": 0x00000006,
    "RASCCPCA_STAC": 0x00000005,
}
_RASCCPCA__INV = {
    0x00000006: "RASCCPCA_MPPC",
    0x00000005: "RASCCPCA_STAC",
}
IPSEC_CIPHER_TYPE = {
    "IPSEC_CIPHER_TYPE_DES": 1,
    "IPSEC_CIPHER_TYPE_3DES": 2,
    "IPSEC_CIPHER_TYPE_AES_128": 3,
    "IPSEC_CIPHER_TYPE_AES_192": 4,
    "IPSEC_CIPHER_TYPE_AES_256": 5,
}
IPSEC_CIPHER_TYPE_INV = {
    1: "IPSEC_CIPHER_TYPE_DES",
    2: "IPSEC_CIPHER_TYPE_3DES",
    3: "IPSEC_CIPHER_TYPE_AES_128",
    4: "IPSEC_CIPHER_TYPE_AES_192",
    5: "IPSEC_CIPHER_TYPE_AES_256",
}
_RASIKEv2_AUTH_ = {
    "RASIKEv2_AUTH_MACHINECERTIFICATES": 1,
    "RASIKEv2_AUTH_EAP": 2,
}
_RASIKEv2_AUTH__INV = {
    1: "RASIKEv2_AUTH_MACHINECERTIFICATES",
    2: "RASIKEv2_AUTH_EAP",
}
RASPROJECTION_INFO_TYPE = {
    "PROJECTION_INFO_TYPE_PPP": 1,
    "PROJECTION_INFO_TYPE_IKEv2": 2,
}
RASPROJECTION_INFO_TYPE_INV = {
    1: "PROJECTION_INFO_TYPE_PPP",
    2: "PROJECTION_INFO_TYPE_IKEv2",
}
IsolationState = {
    "isolationStateNotRestricted": 1,
    "isolationStateInProbation": 2,
    "isolationStateRestrictedAccess": 3,
}
IsolationState_INV = {
    1: "isolationStateNotRestricted",
    2: "isolationStateInProbation",
    3: "isolationStateRestrictedAccess",
}

def rasapi32_RasClearConnectionStatistics(jitter):
    """
    [ERROR_CODE] RasClearConnectionStatistics(
        HRASCONN hRasConn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasConn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasClearLinkStatistics(jitter):
    """
    [ERROR_CODE] RasClearLinkStatistics(
        HRASCONN hRasConn,
        DWORD dwSubEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "dwSubEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasConnectionNotification(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasConnectionNotification(
        HRASCONN hrasconn,
        HANDLE hEvent,
        [RasConnNotifyFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrasconn", "hEvent", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasConnectionNotificationA(jitter):
    rasapi32_RasConnectionNotification(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasConnectionNotificationW(jitter):
    rasapi32_RasConnectionNotification(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasCreatePhonebookEntry(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasCreatePhonebookEntry(
        HWND hwnd,
        LPCTSTR lpszPhonebook
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpszPhonebook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasCreatePhonebookEntryA(jitter):
    rasapi32_RasCreatePhonebookEntry(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasCreatePhonebookEntryW(jitter):
    rasapi32_RasCreatePhonebookEntry(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasDeleteEntry(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasDeleteEntry(
        LPCTSTR lpszPhonebook,
        LPCTSTR lpszEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasDeleteEntryA(jitter):
    rasapi32_RasDeleteEntry(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasDeleteEntryW(jitter):
    rasapi32_RasDeleteEntry(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasDeleteSubEntry(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasDeleteSubEntry(
        LPCTSTR lpszPhonebook,
        LPCTSTR lpszEntry,
        DWORD dwSubEntryId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "dwSubEntryId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasDeleteSubEntryA(jitter):
    rasapi32_RasDeleteSubEntry(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasDeleteSubEntryW(jitter):
    rasapi32_RasDeleteSubEntry(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasDial(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasDial(
        LPRASDIALEXTENSIONS lpRasDialExtensions,
        LPCTSTR lpszPhonebook,
        LPRASDIALPARAMS lpRasDialParams,
        DWORD dwNotifierType,
        LPVOID lpvNotifier,
        LPHRASCONN lphRasConn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpRasDialExtensions", "lpszPhonebook", "lpRasDialParams", "dwNotifierType", "lpvNotifier", "lphRasConn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasDialA(jitter):
    rasapi32_RasDial(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasDialW(jitter):
    rasapi32_RasDial(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasEditPhonebookEntry(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasEditPhonebookEntry(
        HWND hwnd,
        LPCTSTR lpszPhonebook,
        LPCTSTR lpszEntryName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpszPhonebook", "lpszEntryName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasEditPhonebookEntryA(jitter):
    rasapi32_RasEditPhonebookEntry(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasEditPhonebookEntryW(jitter):
    rasapi32_RasEditPhonebookEntry(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasEnumAutodialAddresses(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasEnumAutodialAddresses(
        LPTSTR* lppAddresses,
        LPDWORD lpdwcbAddresses,
        LPDWORD lpdwcAddresses
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lppAddresses", "lpdwcbAddresses", "lpdwcAddresses"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasEnumAutodialAddressesA(jitter):
    rasapi32_RasEnumAutodialAddresses(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasEnumAutodialAddressesW(jitter):
    rasapi32_RasEnumAutodialAddresses(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasEnumConnections(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasEnumConnections(
        LPRASCONN lprasconn,
        LPDWORD lpcb,
        LPDWORD lpcConnections
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprasconn", "lpcb", "lpcConnections"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasEnumConnectionsA(jitter):
    rasapi32_RasEnumConnections(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasEnumConnectionsW(jitter):
    rasapi32_RasEnumConnections(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasEnumDevices(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasEnumDevices(
        LPRASDEVINFO lpRasDevInfo,
        LPDWORD lpcb,
        LPDWORD lpcDevices
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpRasDevInfo", "lpcb", "lpcDevices"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasEnumDevicesA(jitter):
    rasapi32_RasEnumDevices(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasEnumDevicesW(jitter):
    rasapi32_RasEnumDevices(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasEnumEntries(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasEnumEntries(
        LPCTSTR reserved,
        LPCTSTR lpszPhonebook,
        LPRASENTRYNAME lprasentryname,
        LPDWORD lpcb,
        LPDWORD lpcEntries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["reserved", "lpszPhonebook", "lprasentryname", "lpcb", "lpcEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasEnumEntriesA(jitter):
    rasapi32_RasEnumEntries(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasEnumEntriesW(jitter):
    rasapi32_RasEnumEntries(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasFreeEapUserIdentity(jitter, get_str, set_str):
    """
    void RasFreeEapUserIdentity(
        LPRASEAPUSERIDENTITY pRasEapUserIdentity
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRasEapUserIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasFreeEapUserIdentityA(jitter):
    rasapi32_RasFreeEapUserIdentity(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasFreeEapUserIdentityW(jitter):
    rasapi32_RasFreeEapUserIdentity(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetAutodialAddress(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetAutodialAddress(
        LPCTSTR lpszAddress,
        LPDWORD lpdwReserved,
        LPRASAUTODIALENTRY lpAutoDialEntries,
        LPDWORD lpdwcbAutoDialEntries,
        LPDWORD lpdwcAutoDialEntries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszAddress", "lpdwReserved", "lpAutoDialEntries", "lpdwcbAutoDialEntries", "lpdwcAutoDialEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetAutodialAddressA(jitter):
    rasapi32_RasGetAutodialAddress(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetAutodialAddressW(jitter):
    rasapi32_RasGetAutodialAddress(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetAutodialEnable(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetAutodialEnable(
        DWORD dwDialingLocation,
        LPBOOL lpfEnabled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwDialingLocation", "lpfEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetAutodialEnableA(jitter):
    rasapi32_RasGetAutodialEnable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetAutodialEnableW(jitter):
    rasapi32_RasGetAutodialEnable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetAutodialParam(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetAutodialParam(
        DWORD dwKey,
        LPVOID lpvValue,
        LPDWORD lpdwcbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwKey", "lpvValue", "lpdwcbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetAutodialParamA(jitter):
    rasapi32_RasGetAutodialParam(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetAutodialParamW(jitter):
    rasapi32_RasGetAutodialParam(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetConnectionStatistics(jitter):
    """
    [ERROR_CODE] RasGetConnectionStatistics(
        HRASCONN hRasConn,
        RAS_STATS* lpStatistics
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "lpStatistics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetConnectStatus(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetConnectStatus(
        HRASCONN hrasconn,
        LPRASCONNSTATUS lprasconnstatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrasconn", "lprasconnstatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetConnectStatusA(jitter):
    rasapi32_RasGetConnectStatus(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetConnectStatusW(jitter):
    rasapi32_RasGetConnectStatus(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetCountryInfo(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetCountryInfo(
        LPRASCTRYINFO lpRasCtryInfo,
        LPDWORD lpdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpRasCtryInfo", "lpdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetCountryInfoA(jitter):
    rasapi32_RasGetCountryInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetCountryInfoW(jitter):
    rasapi32_RasGetCountryInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetCredentials(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetCredentials(
        LPCTSTR lpszPhonebook,
        LPCTSTR lpszEntry,
        LPRASCREDENTIALS lpCredentials
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpCredentials"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetCredentialsA(jitter):
    rasapi32_RasGetCredentials(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetCredentialsW(jitter):
    rasapi32_RasGetCredentials(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetCustomAuthData(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetCustomAuthData(
        LPCWSTR pszPhonebook,
        LPCWSTR pszEntry,
        BYTE* pbCustomAuthData,
        DWORD* pdwSizeofCustomAuthData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPhonebook", "pszEntry", "pbCustomAuthData", "pdwSizeofCustomAuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetCustomAuthDataA(jitter):
    rasapi32_RasGetCustomAuthData(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetCustomAuthDataW(jitter):
    rasapi32_RasGetCustomAuthData(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetEapUserData(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetEapUserData(
        HANDLE hToken,
        LPCTSTR pszPhonebook,
        LPCTSTR pszEntry,
        BYTE* pbEapData,
        DWORD* pdwSizeofEapData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hToken", "pszPhonebook", "pszEntry", "pbEapData", "pdwSizeofEapData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetEapUserDataA(jitter):
    rasapi32_RasGetEapUserData(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetEapUserDataW(jitter):
    rasapi32_RasGetEapUserData(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetEapUserIdentity(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetEapUserIdentity(
        LPCSTR pszPhonebook,
        LPCSTR pszEntry,
        DWORD dwFlags,
        HWND hwnd,
        LPRASEAPUSERIDENTITY* ppRasEapUserIdentity
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPhonebook", "pszEntry", "dwFlags", "hwnd", "ppRasEapUserIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetEapUserIdentityA(jitter):
    rasapi32_RasGetEapUserIdentity(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetEapUserIdentityW(jitter):
    rasapi32_RasGetEapUserIdentity(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetEntryDialParams(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetEntryDialParams(
        LPCTSTR lpszPhonebook,
        LPRASDIALPARAMS lprasdialparams,
        LPBOOL lpfPassword
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lprasdialparams", "lpfPassword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetEntryDialParamsA(jitter):
    rasapi32_RasGetEntryDialParams(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetEntryDialParamsW(jitter):
    rasapi32_RasGetEntryDialParams(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetEntryProperties(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetEntryProperties(
        LPCTSTR lpszPhonebook,
        LPCTSTR lpszEntry,
        LPRASENTRY lpRasEntry,
        LPDWORD lpdwEntryInfoSize,
        LPBYTE lpbDeviceInfo,
        LPDWORD lpdwDeviceInfoSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpRasEntry", "lpdwEntryInfoSize", "lpbDeviceInfo", "lpdwDeviceInfoSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetEntryPropertiesA(jitter):
    rasapi32_RasGetEntryProperties(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetEntryPropertiesW(jitter):
    rasapi32_RasGetEntryProperties(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetErrorString(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetErrorString(
        UINT uErrorValue,
        LPTSTR lpszErrorString,
        DWORD cBufSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uErrorValue", "lpszErrorString", "cBufSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetErrorStringA(jitter):
    rasapi32_RasGetErrorString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetErrorStringW(jitter):
    rasapi32_RasGetErrorString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetLinkStatistics(jitter):
    """
    [ERROR_CODE] RasGetLinkStatistics(
        HRASCONN hRasConn,
        DWORD dwSubEntry,
        RAS_STATS* lpStatistics
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "dwSubEntry", "lpStatistics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetNapStatus(jitter):
    """
    [ERROR_CODE] RasGetNapStatus(
        HRASCONN hRasConn,
        LPRASNAPSTATE pNapState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "pNapState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetProjectionInfo(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetProjectionInfo(
        HRASCONN hrasconn,
        RASPROJECTION rasprojection,
        LPVOID lpprojection,
        LPDWORD lpcb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrasconn", "rasprojection", "lpprojection", "lpcb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetProjectionInfoA(jitter):
    rasapi32_RasGetProjectionInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetProjectionInfoW(jitter):
    rasapi32_RasGetProjectionInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetProjectionInfoEx(jitter):
    """
    [ERROR_CODE] RasGetProjectionInfoEx(
        HRASCONN Hrasconn,
        PRAS_PROJECTION_INFO pRasProjection,
        LPDWORD lpdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Hrasconn", "pRasProjection", "lpdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetQuarantineConnectionId(jitter):
    """
    [ERROR_CODE] RasGetQuarantineConnectionId(
        HRASCONN hRasConn,
        ConnectionId* lpConnectionId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "lpConnectionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetSubEntryHandle(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetSubEntryHandle(
        HRASCONN hRasConn,
        DWORD dwSubEntry,
        LPHRASCONN lphRasConn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "dwSubEntry", "lphRasConn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetSubEntryHandleA(jitter):
    rasapi32_RasGetSubEntryHandle(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetSubEntryHandleW(jitter):
    rasapi32_RasGetSubEntryHandle(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasGetSubEntryProperties(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasGetSubEntryProperties(
        LPCTSTR lpszPhonebook,
        LPCTSTR lpszEntry,
        DWORD dwSubEntry,
        LPRASSUBENTRY lpRasSubEntry,
        LPDWORD lpdwcb,
        LPBYTE lpbDeviceConfig,
        LPDWORD lpcbDeviceConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "dwSubEntry", "lpRasSubEntry", "lpdwcb", "lpbDeviceConfig", "lpcbDeviceConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetSubEntryPropertiesA(jitter):
    rasapi32_RasGetSubEntryProperties(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasGetSubEntryPropertiesW(jitter):
    rasapi32_RasGetSubEntryProperties(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasHangUp(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasHangUp(
        HRASCONN hrasconn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrasconn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasHangUpA(jitter):
    rasapi32_RasHangUp(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasHangUpW(jitter):
    rasapi32_RasHangUp(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasInvokeEapUI(jitter):
    """
    [ERROR_CODE] RasInvokeEapUI(
        HRASCONN hRasConn,
        DWORD dwSubEntry,
        LPRASDIALEXTENSIONS lpExtensions,
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "dwSubEntry", "lpExtensions", "hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasRenameEntry(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasRenameEntry(
        LPCTSTR lpszPhonebook,
        LPCTSTR lpszOldEntry,
        LPCTSTR lpszNewEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszOldEntry", "lpszNewEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasRenameEntryA(jitter):
    rasapi32_RasRenameEntry(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasRenameEntryW(jitter):
    rasapi32_RasRenameEntry(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasSetAutodialAddress(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasSetAutodialAddress(
        LPCTSTR lpszAddress,
        DWORD dwReserved,
        LPRASAUTODIALENTRY lpAutoDialEntries,
        DWORD dwcbAutoDialEntries,
        DWORD dwcAutoDialEntries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszAddress", "dwReserved", "lpAutoDialEntries", "dwcbAutoDialEntries", "dwcAutoDialEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetAutodialAddressA(jitter):
    rasapi32_RasSetAutodialAddress(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasSetAutodialAddressW(jitter):
    rasapi32_RasSetAutodialAddress(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasSetAutodialEnable(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasSetAutodialEnable(
        DWORD dwDialingLocation,
        BOOL fEnabled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwDialingLocation", "fEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetAutodialEnableA(jitter):
    rasapi32_RasSetAutodialEnable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasSetAutodialEnableW(jitter):
    rasapi32_RasSetAutodialEnable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasSetAutodialParam(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasSetAutodialParam(
        DWORD dwKey,
        LPVOID lpvValue,
        DWORD dwcbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwKey", "lpvValue", "dwcbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetAutodialParamA(jitter):
    rasapi32_RasSetAutodialParam(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasSetAutodialParamW(jitter):
    rasapi32_RasSetAutodialParam(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasSetCredentials(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasSetCredentials(
        LPCTSTR lpszPhonebook,
        LPCTSTR lpszEntry,
        LPRASCREDENTIALS lpCredentials,
        BOOL fClearCredentials
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpCredentials", "fClearCredentials"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetCredentialsA(jitter):
    rasapi32_RasSetCredentials(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasSetCredentialsW(jitter):
    rasapi32_RasSetCredentials(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasSetCustomAuthData(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasSetCustomAuthData(
        LPCWSTR pszPhonebook,
        LPCWSTR pszEntry,
        BYTE* pbCustomAuthData,
        DWORD dwSizeofCustomAuthData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPhonebook", "pszEntry", "pbCustomAuthData", "dwSizeofCustomAuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetCustomAuthDataA(jitter):
    rasapi32_RasSetCustomAuthData(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasSetCustomAuthDataW(jitter):
    rasapi32_RasSetCustomAuthData(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasSetEapUserData(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasSetEapUserData(
        HANDLE hToken,
        LPCTSTR pszPhonebook,
        LPCTSTR pszEntry,
        BYTE* pbEapData,
        DWORD dwSizeofEapData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hToken", "pszPhonebook", "pszEntry", "pbEapData", "dwSizeofEapData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetEapUserDataA(jitter):
    rasapi32_RasSetEapUserData(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasSetEapUserDataW(jitter):
    rasapi32_RasSetEapUserData(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasSetEntryDialParams(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasSetEntryDialParams(
        LPCTSTR lpszPhonebook,
        LPRASDIALPARAMS lprasdialparams,
        BOOL fRemovePassword
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lprasdialparams", "fRemovePassword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetEntryDialParamsA(jitter):
    rasapi32_RasSetEntryDialParams(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasSetEntryDialParamsW(jitter):
    rasapi32_RasSetEntryDialParams(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasSetEntryProperties(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasSetEntryProperties(
        LPCTSTR lpszPhonebook,
        LPCTSTR lpszEntry,
        LPRASENTRY lpRasEntry,
        DWORD dwEntryInfoSize,
        LPBYTE lpbDeviceInfo,
        DWORD dwDeviceInfoSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpRasEntry", "dwEntryInfoSize", "lpbDeviceInfo", "dwDeviceInfoSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetEntryPropertiesA(jitter):
    rasapi32_RasSetEntryProperties(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasSetEntryPropertiesW(jitter):
    rasapi32_RasSetEntryProperties(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasSetSubEntryProperties(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasSetSubEntryProperties(
        LPCTSTR lpszPhonebook,
        LPCTSTR lpszEntry,
        DWORD dwSubEntry,
        LPRASSUBENTRY lpRasSubEntry,
        DWORD dwcbRasSubEntry,
        LPBYTE lpbDeviceConfig,
        DWORD dwcbDeviceConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "dwSubEntry", "lpRasSubEntry", "dwcbRasSubEntry", "lpbDeviceConfig", "dwcbDeviceConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetSubEntryPropertiesA(jitter):
    rasapi32_RasSetSubEntryProperties(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasSetSubEntryPropertiesW(jitter):
    rasapi32_RasSetSubEntryProperties(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasapi32_RasUpdateConnection(jitter):
    """
    [ERROR_CODE] RasUpdateConnection(
        HRASCONN hrasconn,
        LPRASUPDATECONN lprasupdateconn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrasconn", "lprasupdateconn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasValidateEntryName(jitter, get_str, set_str):
    """
    [ERROR_CODE] RasValidateEntryName(
        LPCTSTR lpszPhonebook,
        LPCTSTR lpszEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasValidateEntryNameA(jitter):
    rasapi32_RasValidateEntryName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasapi32_RasValidateEntryNameW(jitter):
    rasapi32_RasValidateEntryName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
