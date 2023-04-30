
def slc_SLActivateProduct(jitter):
    """
    [Slc.dll] HRESULT SLActivateProduct(HSLC hSLC, const SLID* pProductSkuId, UINT cbAppSpecificData, const PVOID pvAppSpecificData, const SL_ACTIVATION_INFO_HEADER* pActivationInfo, PCWSTR pwszProxyServer, WORD wProxyPort)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "cbAppSpecificData", "pvAppSpecificData", "pActivationInfo", "pwszProxyServer", "wProxyPort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLClose(jitter):
    """
    [Slc.dll] HRESULT SLClose(HSLC hSLC)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLConsumeRight(jitter):
    """
    [Slc.dll] HRESULT SLConsumeRight(HSLC hSLC, const SLID* pAppId, const SLID* pProductSkuId, PCWSTR pwszRightName, PVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pAppId", "pProductSkuId", "pwszRightName", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLDepositMigrationBlob(jitter):
    """
    [Slc.dll] HRESULT SLDepositMigrationBlob(HANDLE hFile)
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLDepositOfflineConfirmationId(jitter):
    """
    [Slc.dll] HRESULT SLDepositOfflineConfirmationId(HSLC hSLC, const SLID* pProductSkuId, PCWSTR pwszInstallationId, PCWSTR pwszConfirmationId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "pwszInstallationId", "pwszConfirmationId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLDepositOfflineConfirmationIdEx(jitter):
    """
    [Slc.dll] HRESULT SLDepositOfflineConfirmationIdEx(HSLC hSLC, const SLID* pProductSkuId, const SL_ACTIVATION_INFO_HEADER* pActivationInfo, PCWSTR pwszInstallationId, PCWSTR pwszConfirmationId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "pActivationInfo", "pwszInstallationId", "pwszConfirmationId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLFireEvent(jitter):
    """
    [Slc.dll] HRESULT SLFireEvent(HSLC hSLC, PCWSTR pwszEventId, const SLID* pApplicationId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszEventId", "pApplicationId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGatherMigrationBlob(jitter):
    """
    [Slc.dll] HRESULT SLGatherMigrationBlob(BOOL bMigratableOnly, LPCWSTR pwszEncryptorUri, HANDLE hFile)
    """
    ret_ad, args = jitter.func_args_stdcall(["bMigratableOnly", "pwszEncryptorUri", "hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGenerateOfflineInstallationId(jitter):
    """
    [Slc.dll] HRESULT SLGenerateOfflineInstallationId(HSLC hSLC, const SLID* pProductSkuId, PWSTR* ppwszInstallationId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "ppwszInstallationId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGenerateOfflineInstallationIdEx(jitter):
    """
    [Slc.dll] HRESULT SLGenerateOfflineInstallationIdEx(HSLC hSLC, const SLID* pProductSkuId, const SL_ACTIVATION_INFO_HEADER* pActivationInfo, PWSTR* ppwszInstallationId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "pActivationInfo", "ppwszInstallationId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetApplicationInformation(jitter):
    """
    [Slc.dll] HRESULT SLGetApplicationInformation(HSLC hSLC, const SLID* pApplicationId, PCWSTR pwszValueName, SLDATATYPE* peDataType, UINT* pcbValue, PBYTE* ppbValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pApplicationId", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetApplicationPolicy(jitter):
    """
    [Slc.dll] HRESULT SLGetApplicationPolicy(HSLP hPolicyContext, PCWSTR pwszValueName, SLDATATYPE* peDataType, UINT* pcbValue, PBYTE* ppbValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPolicyContext", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetAuthenticationResult(jitter):
    """
    [Slc.dll] HRESULT SLGetAuthenticationResult(HSLC hSLC, UINT* pcbValue, PBYTE* ppbValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetGenuineInformation(jitter):
    """
    [Slc.dll] HRESULT SLGetGenuineInformation(const SLID* pAppId, PCWSTR pwszValueName, SLDATATYPE* peDataType, UINT* pcbValue, BYTE** ppbValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppId", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLSetGenuineInformation(jitter):
    """
    [Slc.dll] HRESULT SLSetGenuineInformation(const SLID* pAppId, PCWSTR pwszValueName, SLDATATYPE eDataType, UINT cbValue, const BYTE* pbValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppId", "pwszValueName", "eDataType", "cbValue", "pbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetGenuineInformationEx(jitter):
    """
    [Slc.dll] HRESULT SLGetGenuineInformationEx(const SLID* pAppId, PCWSTR pwszValueName, SLDATATYPE* peDataType, UINT* pcbValue, BYTE** ppbValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppId", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetInstalledProductKeyIds(jitter):
    """
    [Slc.dll] HRESULT SLGetInstalledProductKeyIds(HSLC hSLC, const SLID* pProductSkuId, UINT* pnProductKeyIds, SLID** ppProductKeyIds)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "pnProductKeyIds", "ppProductKeyIds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetInstalledSAMLicenseApplications(jitter):
    """
    [Slc.dll] HRESULT SLGetInstalledSAMLicenseApplications(UINT* pnReturnedAppIds, SLID** ppReturnedAppIds)
    """
    ret_ad, args = jitter.func_args_stdcall(["pnReturnedAppIds", "ppReturnedAppIds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetLicense(jitter):
    """
    [Slc.dll] HRESULT SLGetLicense(HSLC hSLC, const SLID* pLicenseFileId, UINT* pcbLicenseFile, PBYTE* ppbLicenseFile)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pLicenseFileId", "pcbLicenseFile", "ppbLicenseFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetLicenseFileId(jitter):
    """
    [Slc.dll] HRESULT SLGetLicenseFileId(HSLC hSLC, UINT cbLicenseBlob, const BYTE* pbLicenseBlob, SLID* pLicenseFileId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "cbLicenseBlob", "pbLicenseBlob", "pLicenseFileId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetLicenseInformation(jitter):
    """
    [Slc.dll] HRESULT SLGetLicenseInformation(HSLC hSLC, const SLID* pSLLicenseId, PCWSTR pwszValueName, SLDATATYPE* peDataType, UINT* pcbValue, PBYTE* ppbValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pSLLicenseId", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetLicensingStatusInformation(jitter):
    """
    [Slc.dll] HRESULT SLGetLicensingStatusInformation(HSLC hSLC, const SLID* pAppID, const SLID* pProductSkuId, PCWSTR pwszRightName, UINT* pnStatusCount, SL_LICENSING_STATUS** ppLicensingStatus)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pAppID", "pProductSkuId", "pwszRightName", "pnStatusCount", "ppLicensingStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetPKeyId(jitter):
    """
    [Slc.dll] HRESULT SLGetPKeyId(HSLC hSLC, PCWSTR pwszPKeyAlgorithm, PCWSTR pwszPKeyString, UINT cbPKeySpecificData, const BYTE* pbPKeySpecificData, SLID* pPKeyId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszPKeyAlgorithm", "pwszPKeyString", "cbPKeySpecificData", "pbPKeySpecificData", "pPKeyId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetPKeyInformation(jitter):
    """
    [Slc.dll] HRESULT SLGetPKeyInformation(HSLC hSLC, const SLID* pPKeyId, PCWSTR pwszValueName, SLDATATYPE* peDataType, UINT* pcbValue, PBYTE* ppbValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pPKeyId", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetPolicyInformation(jitter):
    """
    [Slc.dll] HRESULT SLGetPolicyInformation(HSLC hSLC, PCWSTR pwszValueName, SLDATATYPE* peDataType, UINT* pcbValue, PBYTE* ppbValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetPolicyInformationDWORD(jitter):
    """
    [Slc.dll] HRESULT SLGetPolicyInformationDWORD(HSLC hSLC, PCWSTR pwszValueName, DWORD* pdwValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszValueName", "pdwValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetProductSkuInformation(jitter):
    """
    [Slc.dll] HRESULT SLGetProductSkuInformation(HSLC hSLC, const SLID* pProductSkuId, PCWSTR pwszValueName, SLDATATYPE* peDataType, UINT* pcbValue, PBYTE* ppbValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetReferralInformation(jitter):
    """
    [Slc.dll] HRESULT SLGetReferralInformation(HSLC hSLC, SLREFERRALTYPE eReferralType, const SLID* pSkuOrAppId, PCWSTR pwszValueName, PWSTR* ppwszValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "eReferralType", "pSkuOrAppId", "pwszValueName", "ppwszValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetSAMLicense(jitter):
    """
    [Slc.dll] HRESULT SLGetSAMLicense(const SLID* pApplicationId, UINT* pcbXmlLicenseData, PBYTE* ppbXmlLicenseData)
    """
    ret_ad, args = jitter.func_args_stdcall(["pApplicationId", "pcbXmlLicenseData", "ppbXmlLicenseData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetServerStatus(jitter):
    """
    [Slc.dll] HRESULT SLGetServerStatus(PCWSTR pwszServerURL, PCWSTR pwszAcquisitionType, PCWSTR pwszProxyServer, WORD wProxyPort, HRESULT* phrStatus)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszServerURL", "pwszAcquisitionType", "pwszProxyServer", "wProxyPort", "phrStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetServiceInformation(jitter):
    """
    [Slc.dll] HRESULT SLGetServiceInformation(HSLC hSLC, PCWSTR pwszValueName, SLDATATYPE* peDataType, UINT* pcbValue, PBYTE* ppbValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetSLIDList(jitter):
    """
    [Slc.dll] HRESULT SLGetSLIDList(HSLC hSLC, SLIDTYPE eQueryIdType, const SLID* pQueryId, SLIDTYPE eReturnIdType, UINT* pnReturnIds, SLID** ppReturnIds)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "eQueryIdType", "pQueryId", "eReturnIdType", "pnReturnIds", "ppReturnIds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetWindowsInformation(jitter):
    """
    [Slc.dll] HRESULT SLGetWindowsInformation(PCWSTR pwszValueName, SLDATATYPE* peDataType, UINT* pcbValue, PBYTE* ppbValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetWindowsInformationDWORD(jitter):
    """
    [Slc.dll] HRESULT SLGetWindowsInformationDWORD(PCWSTR pwszValueName, DWORD* pdwValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszValueName", "pdwValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLInstallLicense(jitter):
    """
    [Slc.dll] HRESULT SLInstallLicense(HSLC hSLC, UINT cbLicenseBlob, const BYTE* pbLicenseBlob, SLID* pLicenseFileId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "cbLicenseBlob", "pbLicenseBlob", "pLicenseFileId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLInstallProofOfPurchase(jitter):
    """
    [Slc.dll] HRESULT SLInstallProofOfPurchase(HSLC hSLC, PCWSTR pwszPKeyAlgorithm, PCWSTR pwszPKeyString, UINT cbPKeySpecificData, PBYTE pbPKeySpecificData, SLID* pPKeyId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszPKeyAlgorithm", "pwszPKeyString", "cbPKeySpecificData", "pbPKeySpecificData", "pPKeyId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLInstallProofOfPurchaseEx(jitter):
    """
    [Slc.dll] HRESULT SLInstallProofOfPurchaseEx(HSLC hSLC, const SLID* pApplicationId, const SLID* pProductSkuId, PCWSTR pwszPKeyAlgorithm, PCWSTR pwszPKeyString, UINT cbPKeySpecificData, PBYTE pbPKeySpecificData, SLID* pPKeyId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pApplicationId", "pProductSkuId", "pwszPKeyAlgorithm", "pwszPKeyString", "cbPKeySpecificData", "pbPKeySpecificData", "pPKeyId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLInstallSAMLicense(jitter):
    """
    [Slc.dll] HRESULT SLInstallSAMLicense(const SLID* pApplicationId, UINT cbXmlLicenseData, const BYTE* pbXmlLicenseData)
    """
    ret_ad, args = jitter.func_args_stdcall(["pApplicationId", "cbXmlLicenseData", "pbXmlLicenseData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLLoadApplicationPolicies(jitter):
    """
    [Slc.dll] HRESULT SLLoadApplicationPolicies(const SLID* pApplicationId, const SLID* pProductSkuId, DWORD dwFlags, HSLP* phPolicyContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["pApplicationId", "pProductSkuId", "dwFlags", "phPolicyContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLOpen(jitter):
    """
    [Slc.dll] HRESULT SLOpen(HSLC* phSLC)
    """
    ret_ad, args = jitter.func_args_stdcall(["phSLC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLPersistApplicationPolicies(jitter):
    """
    [Slc.dll] HRESULT SLPersistApplicationPolicies(const SLID* pApplicationId, const SLID* pProductSkuId, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pApplicationId", "pProductSkuId", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLPersistRTSPayloadOverride(jitter):
    """
    [Slc.dll] HRESULT SLPersistRTSPayloadOverride(HSLC hSLC, const SLID* pApplicationId, const SLID* pProductSkuId, BYTE* pbData, DWORD cbData)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pApplicationId", "pProductSkuId", "pbData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLReArm(jitter):
    """
    [Slc.dll] HRESULT SLReArm(HSLC hSLC, const SLID* pApplicationId, const SLID* pProductSkuId, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pApplicationId", "pProductSkuId", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLRegisterEvent(jitter):
    """
    [Slc.dll] HRESULT SLRegisterEvent(HSLC hSLC, PCWSTR pwszEventId, const SLID* pApplicationId, HANDLE hEvent)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszEventId", "pApplicationId", "hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLSetAuthenticationData(jitter):
    """
    [Slc.dll] HRESULT SLSetAuthenticationData(HSLC hSLC, UINT cbValue, const BYTE* pbValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "cbValue", "pbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLSetCurrentProductKey(jitter):
    """
    [Slc.dll] HRESULT SLSetCurrentProductKey(HSLC hSLC, const SLID* pProductSkuId, const SLID* pProductKeyId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "pProductKeyId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLUninstallLicense(jitter):
    """
    [Slc.dll] HRESULT SLUninstallLicense(HSLC hSLC, const SLID* pLicenseFileId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pLicenseFileId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLUninstallProofOfPurchase(jitter):
    """
    [Slc.dll] HRESULT SLUninstallProofOfPurchase(HSLC hSLC, const SLID* pPKeyId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pPKeyId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLUninstallSAMLicense(jitter):
    """
    [Slc.dll] HRESULT SLUninstallSAMLicense(const SLID* pApplicationId)
    """
    ret_ad, args = jitter.func_args_stdcall(["pApplicationId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLUnloadApplicationPolicies(jitter):
    """
    [Slc.dll] HRESULT SLUnloadApplicationPolicies(HSLP hPolicyContext, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPolicyContext", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLUnregisterEvent(jitter):
    """
    [Slc.dll] HRESULT SLUnregisterEvent(HSLC hSLC, PCWSTR pwszEventId, const SLID* pApplicationId, HANDLE hEvent)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszEventId", "pApplicationId", "hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
