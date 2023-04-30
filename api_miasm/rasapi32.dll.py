
def rasapi32_RasClearConnectionStatistics(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasClearConnectionStatistics(HRASCONN hRasConn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRasConn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasClearLinkStatistics(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasClearLinkStatistics(HRASCONN hRasConn, DWORD dwSubEntry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "dwSubEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasConnectionNotification(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasConnectionNotification(HRASCONN hrasconn, HANDLE hEvent, [RasConnNotifyFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hrasconn", "hEvent", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasCreatePhonebookEntry(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasCreatePhonebookEntry(HWND hwnd, LPCTSTR lpszPhonebook)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpszPhonebook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasDeleteEntry(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasDeleteEntry(LPCTSTR lpszPhonebook, LPCTSTR lpszEntry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasDeleteSubEntry(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasDeleteSubEntry(LPCTSTR lpszPhonebook, LPCTSTR lpszEntry, DWORD dwSubEntryId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "dwSubEntryId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasDial(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasDial(LPRASDIALEXTENSIONS lpRasDialExtensions, LPCTSTR lpszPhonebook, LPRASDIALPARAMS lpRasDialParams, DWORD dwNotifierType, LPVOID lpvNotifier, LPHRASCONN lphRasConn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpRasDialExtensions", "lpszPhonebook", "lpRasDialParams", "dwNotifierType", "lpvNotifier", "lphRasConn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasEditPhonebookEntry(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasEditPhonebookEntry(HWND hwnd, LPCTSTR lpszPhonebook, LPCTSTR lpszEntryName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpszPhonebook", "lpszEntryName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasEnumAutodialAddresses(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasEnumAutodialAddresses(LPTSTR* lppAddresses, LPDWORD lpdwcbAddresses, LPDWORD lpdwcAddresses)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lppAddresses", "lpdwcbAddresses", "lpdwcAddresses"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasEnumConnections(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasEnumConnections(LPRASCONN lprasconn, LPDWORD lpcb, LPDWORD lpcConnections)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lprasconn", "lpcb", "lpcConnections"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasEnumDevices(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasEnumDevices(LPRASDEVINFO lpRasDevInfo, LPDWORD lpcb, LPDWORD lpcDevices)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpRasDevInfo", "lpcb", "lpcDevices"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasEnumEntries(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasEnumEntries(LPCTSTR reserved, LPCTSTR lpszPhonebook, LPRASENTRYNAME lprasentryname, LPDWORD lpcb, LPDWORD lpcEntries)
    """"
    ret_ad, args = jitter.func_args_stdcall(["reserved", "lpszPhonebook", "lprasentryname", "lpcb", "lpcEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasFreeEapUserIdentity(jitter):
    """"
    [Rasapi32.dll] void RasFreeEapUserIdentity(LPRASEAPUSERIDENTITY pRasEapUserIdentity)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRasEapUserIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetAutodialAddress(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetAutodialAddress(LPCTSTR lpszAddress, LPDWORD lpdwReserved, LPRASAUTODIALENTRY lpAutoDialEntries, LPDWORD lpdwcbAutoDialEntries, LPDWORD lpdwcAutoDialEntries)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszAddress", "lpdwReserved", "lpAutoDialEntries", "lpdwcbAutoDialEntries", "lpdwcAutoDialEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetAutodialEnable(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetAutodialEnable(DWORD dwDialingLocation, LPBOOL lpfEnabled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDialingLocation", "lpfEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetAutodialParam(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetAutodialParam(DWORD dwKey, LPVOID lpvValue, LPDWORD lpdwcbValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwKey", "lpvValue", "lpdwcbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetConnectionStatistics(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetConnectionStatistics(HRASCONN hRasConn, RAS_STATS* lpStatistics)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "lpStatistics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetConnectStatus(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetConnectStatus(HRASCONN hrasconn, LPRASCONNSTATUS lprasconnstatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hrasconn", "lprasconnstatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetCountryInfo(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetCountryInfo(LPRASCTRYINFO lpRasCtryInfo, LPDWORD lpdwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpRasCtryInfo", "lpdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetCredentials(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetCredentials(LPCTSTR lpszPhonebook, LPCTSTR lpszEntry, LPRASCREDENTIALS lpCredentials)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpCredentials"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetCustomAuthData(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetCustomAuthData(LPCWSTR pszPhonebook, LPCWSTR pszEntry, BYTE* pbCustomAuthData, DWORD* pdwSizeofCustomAuthData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPhonebook", "pszEntry", "pbCustomAuthData", "pdwSizeofCustomAuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetEapUserData(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetEapUserData(HANDLE hToken, LPCTSTR pszPhonebook, LPCTSTR pszEntry, BYTE* pbEapData, DWORD* pdwSizeofEapData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hToken", "pszPhonebook", "pszEntry", "pbEapData", "pdwSizeofEapData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetEapUserIdentity(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetEapUserIdentity(LPCSTR pszPhonebook, LPCSTR pszEntry, DWORD dwFlags, HWND hwnd, LPRASEAPUSERIDENTITY* ppRasEapUserIdentity)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPhonebook", "pszEntry", "dwFlags", "hwnd", "ppRasEapUserIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetEntryDialParams(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetEntryDialParams(LPCTSTR lpszPhonebook, LPRASDIALPARAMS lprasdialparams, LPBOOL lpfPassword)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lprasdialparams", "lpfPassword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetEntryProperties(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetEntryProperties(LPCTSTR lpszPhonebook, LPCTSTR lpszEntry, LPRASENTRY lpRasEntry, LPDWORD lpdwEntryInfoSize, LPBYTE lpbDeviceInfo, LPDWORD lpdwDeviceInfoSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpRasEntry", "lpdwEntryInfoSize", "lpbDeviceInfo", "lpdwDeviceInfoSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetErrorString(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetErrorString(UINT uErrorValue, LPTSTR lpszErrorString, DWORD cBufSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uErrorValue", "lpszErrorString", "cBufSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetLinkStatistics(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetLinkStatistics(HRASCONN hRasConn, DWORD dwSubEntry, RAS_STATS* lpStatistics)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "dwSubEntry", "lpStatistics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetNapStatus(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetNapStatus(HRASCONN hRasConn, LPRASNAPSTATE pNapState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "pNapState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetProjectionInfo(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetProjectionInfo(HRASCONN hrasconn, RASPROJECTION rasprojection, LPVOID lpprojection, LPDWORD lpcb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hrasconn", "rasprojection", "lpprojection", "lpcb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetProjectionInfoEx(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetProjectionInfoEx(HRASCONN Hrasconn, PRAS_PROJECTION_INFO pRasProjection, LPDWORD lpdwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Hrasconn", "pRasProjection", "lpdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetQuarantineConnectionId(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetQuarantineConnectionId(HRASCONN hRasConn, ConnectionId* lpConnectionId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "lpConnectionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetSubEntryHandle(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetSubEntryHandle(HRASCONN hRasConn, DWORD dwSubEntry, LPHRASCONN lphRasConn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "dwSubEntry", "lphRasConn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasGetSubEntryProperties(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasGetSubEntryProperties(LPCTSTR lpszPhonebook, LPCTSTR lpszEntry, DWORD dwSubEntry, LPRASSUBENTRY lpRasSubEntry, LPDWORD lpdwcb, LPBYTE lpbDeviceConfig, LPDWORD lpcbDeviceConfig)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "dwSubEntry", "lpRasSubEntry", "lpdwcb", "lpbDeviceConfig", "lpcbDeviceConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasHangUp(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasHangUp(HRASCONN hrasconn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hrasconn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasInvokeEapUI(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasInvokeEapUI(HRASCONN hRasConn, DWORD dwSubEntry, LPRASDIALEXTENSIONS lpExtensions, HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRasConn", "dwSubEntry", "lpExtensions", "hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasRenameEntry(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasRenameEntry(LPCTSTR lpszPhonebook, LPCTSTR lpszOldEntry, LPCTSTR lpszNewEntry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszOldEntry", "lpszNewEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetAutodialAddress(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasSetAutodialAddress(LPCTSTR lpszAddress, DWORD dwReserved, LPRASAUTODIALENTRY lpAutoDialEntries, DWORD dwcbAutoDialEntries, DWORD dwcAutoDialEntries)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszAddress", "dwReserved", "lpAutoDialEntries", "dwcbAutoDialEntries", "dwcAutoDialEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetAutodialEnable(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasSetAutodialEnable(DWORD dwDialingLocation, BOOL fEnabled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDialingLocation", "fEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetAutodialParam(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasSetAutodialParam(DWORD dwKey, LPVOID lpvValue, DWORD dwcbValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwKey", "lpvValue", "dwcbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetCredentials(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasSetCredentials(LPCTSTR lpszPhonebook, LPCTSTR lpszEntry, LPRASCREDENTIALS lpCredentials, BOOL fClearCredentials)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpCredentials", "fClearCredentials"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetCustomAuthData(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasSetCustomAuthData(LPCWSTR pszPhonebook, LPCWSTR pszEntry, BYTE* pbCustomAuthData, DWORD dwSizeofCustomAuthData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPhonebook", "pszEntry", "pbCustomAuthData", "dwSizeofCustomAuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetEapUserData(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasSetEapUserData(HANDLE hToken, LPCTSTR pszPhonebook, LPCTSTR pszEntry, BYTE* pbEapData, DWORD dwSizeofEapData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hToken", "pszPhonebook", "pszEntry", "pbEapData", "dwSizeofEapData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetEntryDialParams(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasSetEntryDialParams(LPCTSTR lpszPhonebook, LPRASDIALPARAMS lprasdialparams, BOOL fRemovePassword)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lprasdialparams", "fRemovePassword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetEntryProperties(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasSetEntryProperties(LPCTSTR lpszPhonebook, LPCTSTR lpszEntry, LPRASENTRY lpRasEntry, DWORD dwEntryInfoSize, LPBYTE lpbDeviceInfo, DWORD dwDeviceInfoSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpRasEntry", "dwEntryInfoSize", "lpbDeviceInfo", "dwDeviceInfoSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasSetSubEntryProperties(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasSetSubEntryProperties(LPCTSTR lpszPhonebook, LPCTSTR lpszEntry, DWORD dwSubEntry, LPRASSUBENTRY lpRasSubEntry, DWORD dwcbRasSubEntry, LPBYTE lpbDeviceConfig, DWORD dwcbDeviceConfig)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "dwSubEntry", "lpRasSubEntry", "dwcbRasSubEntry", "lpbDeviceConfig", "dwcbDeviceConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasUpdateConnection(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasUpdateConnection(HRASCONN hrasconn, LPRASUPDATECONN lprasupdateconn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hrasconn", "lprasupdateconn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasapi32_RasValidateEntryName(jitter):
    """"
    [Rasapi32.dll] [ERROR_CODE] RasValidateEntryName(LPCTSTR lpszPhonebook, LPCTSTR lpszEntry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
