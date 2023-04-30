
def wlanapi_WlanAllocateMemory(jitter):
    """
    [Wlanapi.dll] PVOID WlanAllocateMemory(DWORD dwMemorySize)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwMemorySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanCloseHandle(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanCloseHandle(HANDLE hClientHandle, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanConnect(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanConnect(HANDLE hClientHandle, const GUID* pInterfaceGuid, const PWLAN_CONNECTION_PARAMETERS pConnectionParameters, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "pConnectionParameters", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanDeleteProfile(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanDeleteProfile(HANDLE hClientHandle, const GUID* pInterfaceGuid, LPCWSTR strProfileName, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanDisconnect(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanDisconnect(HANDLE hClientHandle, const GUID* pInterfaceGuid, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanEnumInterfaces(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanEnumInterfaces(HANDLE hClientHandle, PVOID pReserved, PWLAN_INTERFACE_INFO_LIST* ppInterfaceList)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pReserved", "ppInterfaceList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanExtractPsdIEDataList(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanExtractPsdIEDataList(HANDLE hClientHandle, DWORD dwIeDataSize, const PBYTE pRawIeData, LPCWSTR strFormat, PVOID pReserved, PWLAN_RAW_DATA_LIST* ppPsdIEDataList)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "dwIeDataSize", "pRawIeData", "strFormat", "pReserved", "ppPsdIEDataList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanFreeMemory(jitter):
    """
    [Wlanapi.dll] VOID WlanFreeMemory(PVOID pMemory)
    """
    ret_ad, args = jitter.func_args_stdcall(["pMemory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetAvailableNetworkList(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanGetAvailableNetworkList(HANDLE hClientHandle, const GUID* pInterfaceGuid, [WlanAvailableFlags] dwFlags, PVOID pReserved, PWLAN_AVAILABLE_NETWORK_LIST* ppAvailableNetworkList)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "dwFlags", "pReserved", "ppAvailableNetworkList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetFilterList(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanGetFilterList(HANDLE hClientHandle, WLAN_FILTER_LIST_TYPE wlanFilterListType, PVOID pReserved, PDOT11_NETWORK_LIST* ppNetworkList)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "wlanFilterListType", "pReserved", "ppNetworkList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetInterfaceCapability(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanGetInterfaceCapability(HANDLE hClientHandle, const GUID* pInterfaceGuid, PVOID pReserved, PWLAN_INTERFACE_CAPABILITY* ppCapability)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "pReserved", "ppCapability"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetNetworkBssList(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanGetNetworkBssList(HANDLE hClientHandle, const GUID* pInterfaceGuid, const PDOT11_SSID pDot11Ssid, DOT11_BSS_TYPE dot11BssType, BOOL bSecurityEnabled, PVOID pReserved, PWLAN_BSS_LIST* ppWlanBssList)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "pDot11Ssid", "dot11BssType", "bSecurityEnabled", "pReserved", "ppWlanBssList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetProfile(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanGetProfile(HANDLE hClientHandle, const GUID* pInterfaceGuid, LPCWSTR strProfileName, PVOID pReserved, LPWSTR* pstrProfileXml, [WlanProfileFlags*] pdwFlags, [WlanAccess*] pdwGrantedAccess)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "pReserved", "pstrProfileXml", "pdwFlags", "pdwGrantedAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetProfileCustomUserData(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanGetProfileCustomUserData(HANDLE hClientHandle, const GUID* pInterfaceGuid, LPCWSTR strProfileName, PVOID pReserved, DWORD* pdwDataSize, PBYTE* ppData)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "pReserved", "pdwDataSize", "ppData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetProfileList(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanGetProfileList(HANDLE hClientHandle, const GUID* pInterfaceGuid, PVOID pReserved, PWLAN_PROFILE_INFO_LIST* ppProfileList)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "pReserved", "ppProfileList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetSecuritySettings(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanGetSecuritySettings(HANDLE hClientHandle, WLAN_SECURABLE_OBJECT SecurableObject, PWLAN_OPCODE_VALUE_TYPE pValueType, LPWSTR* pstrCurrentSDDL, [WlanAccess*] pdwGrantedAccess)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "SecurableObject", "pValueType", "pstrCurrentSDDL", "pdwGrantedAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanIhvControl(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanIhvControl(HANDLE hClientHandle, const GUID* pInterfaceGuid, WLAN_IHV_CONTROL_TYPE Type, DWORD dwInBufferSize, PVOID pInBuffer, DWORD dwOutBufferSize, PVOID pOutBuffer, PDWORD pdwBytesReturned)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "Type", "dwInBufferSize", "pInBuffer", "dwOutBufferSize", "pOutBuffer", "pdwBytesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanOpenHandle(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanOpenHandle(DWORD dwClientVersion, PVOID pReserved, PDWORD pdwNegotiatedVersion, PHANDLE phClientHandle)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwClientVersion", "pReserved", "pdwNegotiatedVersion", "phClientHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanQueryAutoConfigParameter(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanQueryAutoConfigParameter(HANDLE hClientHandle, WLAN_AUTOCONF_OPCODE OpCode, PVOID pReserved, PDWORD pdwDataSize, PVOID ppData, PWLAN_OPCODE_VALUE_TYPE pWlanOpcodeValueType)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "OpCode", "pReserved", "pdwDataSize", "ppData", "pWlanOpcodeValueType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanQueryInterface(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanQueryInterface(HANDLE hClientHandle, const GUID* pInterfaceGuid, WLAN_INTF_OPCODE OpCode, PVOID pReserved, PDWORD pdwDataSize, PVOID* ppData, PWLAN_OPCODE_VALUE_TYPE pWlanOpcodeValueType)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "OpCode", "pReserved", "pdwDataSize", "ppData", "pWlanOpcodeValueType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanReasonCodeToString(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanReasonCodeToString(DWORD dwReasonCode, DWORD dwBufferSize, PWCHAR pStringBuffer, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwReasonCode", "dwBufferSize", "pStringBuffer", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanRegisterNotification(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanRegisterNotification(HANDLE hClientHandle, [WlanNotificationSource] dwNotifSource, BOOL bIgnoreDuplicate, WLAN_NOTIFICATION_CALLBACK funcCallback, PVOID pCallbackContext, PVOID pReserved, [WlanNotificationSource*] pdwPrevNotifSource)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "dwNotifSource", "bIgnoreDuplicate", "funcCallback", "pCallbackContext", "pReserved", "pdwPrevNotifSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanRenameProfile(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanRenameProfile(HANDLE hClientHandle, CONST GUID* pInterfaceGuid, LPCWSTR strOldProfileName, LPCWSTR strNewProfileName, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strOldProfileName", "strNewProfileName", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSaveTemporaryProfile(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanSaveTemporaryProfile(HANDLE hClientHandle, const GUID* pInterfaceGuid, LPCWSTR strProfileName, LPCWSTR strAllUserProfileSecurity, [WlanProfileFlags] dwFlags, BOOL bOverWrite, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "strAllUserProfileSecurity", "dwFlags", "bOverWrite", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanScan(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanScan(HANDLE hClientHandle, const GUID* pInterfaceGuid, const PDOT11_SSID pDot11Ssid, const PWLAN_RAW_DATA pIeData, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "pDot11Ssid", "pIeData", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetAutoConfigParameter(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanSetAutoConfigParameter(HANDLE hClientHandle, WLAN_AUTOCONF_OPCODE OpCode, DWORD dwDataSize, const PVOID pData, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "OpCode", "dwDataSize", "pData", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetFilterList(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanSetFilterList(HANDLE hClientHandle, WLAN_FILTER_LIST_TYPE wlanFilterListType, const PDOT11_NETWORK_LIST pNetworkList, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "wlanFilterListType", "pNetworkList", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetInterface(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanSetInterface(HANDLE hClientHandle, const GUID* pInterfaceGuid, WLAN_INTF_OPCODE OpCode, DWORD dwDataSize, const PVOID pData, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "OpCode", "dwDataSize", "pData", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetProfile(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanSetProfile(HANDLE hClientHandle, const GUID* pInterfaceGuid, DWORD dwFlags, LPCWSTR strProfileXml, LPCWSTR strAllUserProfileSecurity, BOOL bOverwrite, PVOID pReserved, DWORD* pdwReasonCode)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "dwFlags", "strProfileXml", "strAllUserProfileSecurity", "bOverwrite", "pReserved", "pdwReasonCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetProfileCustomUserData(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanSetProfileCustomUserData(HANDLE hClientHandle, const GUID* pInterfaceGuid, LPCWSTR strProfileName, DWORD dwDataSize, const PBYTE pData, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "dwDataSize", "pData", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetProfileEapUserData(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanSetProfileEapUserData(HANDLE hClientHandle, const GUID* pInterfaceGuid, LPCWSTR strProfileName, EAP_METHOD_TYPE eapType, DWORD dwFlags, DWORD dwEapUserDataSize, const LPBYTE pbEapUserData, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "eapType", "dwFlags", "dwEapUserDataSize", "pbEapUserData", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetProfileEapXmlUserData(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanSetProfileEapXmlUserData(HANDLE hClientHandle, const GUID* pInterfaceGuid, LPCWSTR strProfileName, DWORD dwFlags, LPCWSTR strEapXmlUserData, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "dwFlags", "strEapXmlUserData", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetProfileList(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanSetProfileList(HANDLE hClientHandle, const GUID* pInterfaceGuid, DWORD dwItems, LPCWSTR* strProfileNames, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "dwItems", "strProfileNames", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetProfilePosition(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanSetProfilePosition(HANDLE hClientHandle, const GUID* pInterfaceGuid, LPCWSTR strProfileName, DWORD dwPosition, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "dwPosition", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetPsdIEDataList(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanSetPsdIEDataList(HANDLE hClientHandle, LPCWSTR strFormat, const PWLAN_RAW_DATA_LIST pPsdIEDataList, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "strFormat", "pPsdIEDataList", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetSecuritySettings(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanSetSecuritySettings(HANDLE hClientHandle, WLAN_SECURABLE_OBJECT SecurableObject, LPCWSTR strModifiedSDDL)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "SecurableObject", "strModifiedSDDL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDCancelOpenSession(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WFDCancelOpenSession(PHANDLE hSessionHandle)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDCloseHandle(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WFDCloseHandle(HANDLE hClientHandle)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDCloseSession(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WFDCloseSession(PHANDLE hSessionHandle)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDOpenHandle(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WFDOpenHandle(DWORD dwClientVersion, PDWORD pdwNegotiatedVersion, PHANDLE phClientHandle)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwClientVersion", "pdwNegotiatedVersion", "phClientHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDOpenLegacySession(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WFDOpenLegacySession(HANDLE hClientHandle, PDOT11_MAC_ADDRESS pLegacyMacAddress, HANDLE phSessionHandle, GUID pGuidSessionInterface)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pLegacyMacAddress", "phSessionHandle", "pGuidSessionInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDStartOpenSession(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WFDStartOpenSession(HANDLE hClientHandle, PDOT11_MAC_ADDRESS pDeviceAddress, PVOID pvContext, WFD_OPEN_SESSION_COMPLETE_CALLBACK pfnCallback, PHANDLE phSessionHandle)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pDeviceAddress", "pvContext", "pfnCallback", "phSessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDUpdateDeviceVisibility(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WFDUpdateDeviceVisibility(PDOT11_MAC_ADDRESS pDeviceAddress)
    """
    ret_ad, args = jitter.func_args_stdcall(["pDeviceAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkForceStart(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanHostedNetworkForceStart(HANDLE hClientHandle, PWLAN_HOSTED_NETWORK_REASON pFailReason, PVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkForceStop(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanHostedNetworkForceStop(HANDLE hClientHandle, PWLAN_HOSTED_NETWORK_REASON pFailReason, PVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkInitSettings(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanHostedNetworkInitSettings(HANDLE hClientHandle, PWLAN_HOSTED_NETWORK_REASON pFailReason, PVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkQueryProperty(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanHostedNetworkQueryProperty(HANDLE hClientHandle, WLAN_HOSTED_NETWORK_OPCODE OpCode, PDWORD pdwDataSize, PVOID* ppvData, PWLAN_OPCODE_VALUE_TYPE* pWlanOpcodeValueType, PVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "OpCode", "pdwDataSize", "ppvData", "pWlanOpcodeValueType", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkQuerySecondaryKey(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanHostedNetworkQuerySecondaryKey(HANDLE hClientHandle, DWORD pdwKeyLength, PUCHAR* ppucKeyData, PBOOL pbIsPassPhrase, PBOOL pbPersistent, PWLAN_HOSTED_NETWORK_REASON pFailReason, PVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pdwKeyLength", "ppucKeyData", "pbIsPassPhrase", "pbPersistent", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkQueryStatus(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanHostedNetworkQueryStatus(HANDLE hClientHandle, PWLAN_HOSTED_NETWORK_STATUS* ppWlanHostedNetworkStatus, PVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "ppWlanHostedNetworkStatus", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkRefreshSecuritySettings(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanHostedNetworkRefreshSecuritySettings(HANDLE hClientHandle, PWLAN_HOSTED_NETWORK_REASON pFailReason, PVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkSetProperty(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanHostedNetworkSetProperty(HANDLE hClientHandle, WLAN_HOSTED_NETWORK_OPCODE OpCode, DWORD dwDataSize, PVOID pvData, PWLAN_HOSTED_NETWORK_REASON pFailReason, PVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "OpCode", "dwDataSize", "pvData", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkSetSecondaryKey(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanHostedNetworkSetSecondaryKey(HANDLE hClientHandle, DWORD dwKeyLength, PUCHAR pucKeyData, BOOL bIsPassPhrase, BOOL bPersistent, PWLAN_HOSTED_NETWORK_REASON pFailReason, PVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "dwKeyLength", "pucKeyData", "bIsPassPhrase", "bPersistent", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkStartUsing(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanHostedNetworkStartUsing(HANDLE hClientHandle, PWLAN_HOSTED_NETWORK_REASON pFailReason, PVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkStopUsing(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanHostedNetworkStopUsing(HANDLE hClientHandle, PWLAN_HOSTED_NETWORK_REASON pFailReason, PVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanRegisterVirtualStationNotification(jitter):
    """
    [Wlanapi.dll] [ERROR_CODE] WlanRegisterVirtualStationNotification(HANDLE hClientHandle, BOOL bRegister, PVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "bRegister", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
