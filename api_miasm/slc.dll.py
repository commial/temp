SLDATATYPE = {
    "SL_DATA_NONE": 0,
    "SL_DATA_SZ": 1,
    "SL_DATA_DWORD": 4,
    "SL_DATA_BINARY": 3,
    "SL_DATA_MULTI_SZ": 7,
    "SL_DATA_SUM": 100,
}
SLDATATYPE_INV = {
    0: "SL_DATA_NONE",
    1: "SL_DATA_SZ",
    4: "SL_DATA_DWORD",
    3: "SL_DATA_BINARY",
    7: "SL_DATA_MULTI_SZ",
    100: "SL_DATA_SUM",
}
SLIDTYPE = {
    "SL_ID_APPLICATION": 0,
    "SL_ID_PRODUCT_SKU": 1,
    "SL_ID_LICENSE_FILE": 2,
    "SL_ID_LICENSE": 3,
    "SL_ID_PKEY": 4,
    "SL_ID_ALL_LICENSES": 5,
    "SL_ID_ALL_LICENSE_FILES": 6,
}
SLIDTYPE_INV = {
    0: "SL_ID_APPLICATION",
    1: "SL_ID_PRODUCT_SKU",
    2: "SL_ID_LICENSE_FILE",
    3: "SL_ID_LICENSE",
    4: "SL_ID_PKEY",
    5: "SL_ID_ALL_LICENSES",
    6: "SL_ID_ALL_LICENSE_FILES",
}
SLREFERRALTYPE = {
    "SL_REFERRALTYPE_SKUID": 0,
    "SL_REFERRALTYPE_APPID": 1,
    "SL_REFERRALTYPE_OVERRIDE_SKUID": 2,
    "SL_REFERRALTYPE_OVERRIDE_APPID": 3,
    "SL_REFERRALTYPE_BEST_MATCH": 4,
}
SLREFERRALTYPE_INV = {
    0: "SL_REFERRALTYPE_SKUID",
    1: "SL_REFERRALTYPE_APPID",
    2: "SL_REFERRALTYPE_OVERRIDE_SKUID",
    3: "SL_REFERRALTYPE_OVERRIDE_APPID",
    4: "SL_REFERRALTYPE_BEST_MATCH",
}
SLLICENSINGSTATUS = {
    "SL_LICENSING_STATUS_UNLICENSED": 0,
    "SL_LICENSING_STATUS_LICENSED": 1,
    "SL_LICENSING_STATUS_IN_GRACE_PERIOD": 2,
    "SL_LICENSING_STATUS_NOTIFICATION": 3,
}
SLLICENSINGSTATUS_INV = {
    0: "SL_LICENSING_STATUS_UNLICENSED",
    1: "SL_LICENSING_STATUS_LICENSED",
    2: "SL_LICENSING_STATUS_IN_GRACE_PERIOD",
    3: "SL_LICENSING_STATUS_NOTIFICATION",
}
SL_ACTIVATION_TYPE = {
    "SL_ACTIVATION_TYPE_DEFAULT": 0,
    "SL_ACTIVATION_TYPE_ACTIVE_DIRECTORY": 1,
}
SL_ACTIVATION_TYPE_INV = {
    0: "SL_ACTIVATION_TYPE_DEFAULT",
    1: "SL_ACTIVATION_TYPE_ACTIVE_DIRECTORY",
}

def slc_SLActivateProduct(jitter):
    """
    HRESULT SLActivateProduct(
        HSLC hSLC,
        const SLID* pProductSkuId,
        UINT cbAppSpecificData,
        const PVOID pvAppSpecificData,
        const SL_ACTIVATION_INFO_HEADER* pActivationInfo,
        PCWSTR pwszProxyServer,
        WORD wProxyPort
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "cbAppSpecificData", "pvAppSpecificData", "pActivationInfo", "pwszProxyServer", "wProxyPort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLClose(jitter):
    """
    HRESULT SLClose(
        HSLC hSLC
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLConsumeRight(jitter):
    """
    HRESULT SLConsumeRight(
        HSLC hSLC,
        const SLID* pAppId,
        const SLID* pProductSkuId,
        PCWSTR pwszRightName,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pAppId", "pProductSkuId", "pwszRightName", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLDepositMigrationBlob(jitter):
    """
    HRESULT SLDepositMigrationBlob(
        HANDLE hFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLDepositOfflineConfirmationId(jitter):
    """
    HRESULT SLDepositOfflineConfirmationId(
        HSLC hSLC,
        const SLID* pProductSkuId,
        PCWSTR pwszInstallationId,
        PCWSTR pwszConfirmationId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "pwszInstallationId", "pwszConfirmationId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLDepositOfflineConfirmationIdEx(jitter):
    """
    HRESULT SLDepositOfflineConfirmationIdEx(
        HSLC hSLC,
        const SLID* pProductSkuId,
        const SL_ACTIVATION_INFO_HEADER* pActivationInfo,
        PCWSTR pwszInstallationId,
        PCWSTR pwszConfirmationId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "pActivationInfo", "pwszInstallationId", "pwszConfirmationId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLFireEvent(jitter):
    """
    HRESULT SLFireEvent(
        HSLC hSLC,
        PCWSTR pwszEventId,
        const SLID* pApplicationId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszEventId", "pApplicationId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGatherMigrationBlob(jitter):
    """
    HRESULT SLGatherMigrationBlob(
        BOOL bMigratableOnly,
        LPCWSTR pwszEncryptorUri,
        HANDLE hFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bMigratableOnly", "pwszEncryptorUri", "hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGenerateOfflineInstallationId(jitter):
    """
    HRESULT SLGenerateOfflineInstallationId(
        HSLC hSLC,
        const SLID* pProductSkuId,
        PWSTR* ppwszInstallationId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "ppwszInstallationId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGenerateOfflineInstallationIdEx(jitter):
    """
    HRESULT SLGenerateOfflineInstallationIdEx(
        HSLC hSLC,
        const SLID* pProductSkuId,
        const SL_ACTIVATION_INFO_HEADER* pActivationInfo,
        PWSTR* ppwszInstallationId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "pActivationInfo", "ppwszInstallationId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetApplicationInformation(jitter):
    """
    HRESULT SLGetApplicationInformation(
        HSLC hSLC,
        const SLID* pApplicationId,
        PCWSTR pwszValueName,
        SLDATATYPE* peDataType,
        UINT* pcbValue,
        PBYTE* ppbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pApplicationId", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetApplicationPolicy(jitter):
    """
    HRESULT SLGetApplicationPolicy(
        HSLP hPolicyContext,
        PCWSTR pwszValueName,
        SLDATATYPE* peDataType,
        UINT* pcbValue,
        PBYTE* ppbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPolicyContext", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetAuthenticationResult(jitter):
    """
    HRESULT SLGetAuthenticationResult(
        HSLC hSLC,
        UINT* pcbValue,
        PBYTE* ppbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetGenuineInformation(jitter):
    """
    HRESULT SLGetGenuineInformation(
        const SLID* pAppId,
        PCWSTR pwszValueName,
        SLDATATYPE* peDataType,
        UINT* pcbValue,
        BYTE** ppbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppId", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLSetGenuineInformation(jitter):
    """
    HRESULT SLSetGenuineInformation(
        const SLID* pAppId,
        PCWSTR pwszValueName,
        SLDATATYPE eDataType,
        UINT cbValue,
        const BYTE* pbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppId", "pwszValueName", "eDataType", "cbValue", "pbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetGenuineInformationEx(jitter):
    """
    HRESULT SLGetGenuineInformationEx(
        const SLID* pAppId,
        PCWSTR pwszValueName,
        SLDATATYPE* peDataType,
        UINT* pcbValue,
        BYTE** ppbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppId", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetInstalledProductKeyIds(jitter):
    """
    HRESULT SLGetInstalledProductKeyIds(
        HSLC hSLC,
        const SLID* pProductSkuId,
        UINT* pnProductKeyIds,
        SLID** ppProductKeyIds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "pnProductKeyIds", "ppProductKeyIds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetInstalledSAMLicenseApplications(jitter):
    """
    HRESULT SLGetInstalledSAMLicenseApplications(
        UINT* pnReturnedAppIds,
        SLID** ppReturnedAppIds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pnReturnedAppIds", "ppReturnedAppIds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetLicense(jitter):
    """
    HRESULT SLGetLicense(
        HSLC hSLC,
        const SLID* pLicenseFileId,
        UINT* pcbLicenseFile,
        PBYTE* ppbLicenseFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pLicenseFileId", "pcbLicenseFile", "ppbLicenseFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetLicenseFileId(jitter):
    """
    HRESULT SLGetLicenseFileId(
        HSLC hSLC,
        UINT cbLicenseBlob,
        const BYTE* pbLicenseBlob,
        SLID* pLicenseFileId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "cbLicenseBlob", "pbLicenseBlob", "pLicenseFileId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetLicenseInformation(jitter):
    """
    HRESULT SLGetLicenseInformation(
        HSLC hSLC,
        const SLID* pSLLicenseId,
        PCWSTR pwszValueName,
        SLDATATYPE* peDataType,
        UINT* pcbValue,
        PBYTE* ppbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pSLLicenseId", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetLicensingStatusInformation(jitter):
    """
    HRESULT SLGetLicensingStatusInformation(
        HSLC hSLC,
        const SLID* pAppID,
        const SLID* pProductSkuId,
        PCWSTR pwszRightName,
        UINT* pnStatusCount,
        SL_LICENSING_STATUS** ppLicensingStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pAppID", "pProductSkuId", "pwszRightName", "pnStatusCount", "ppLicensingStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetPKeyId(jitter):
    """
    HRESULT SLGetPKeyId(
        HSLC hSLC,
        PCWSTR pwszPKeyAlgorithm,
        PCWSTR pwszPKeyString,
        UINT cbPKeySpecificData,
        const BYTE* pbPKeySpecificData,
        SLID* pPKeyId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszPKeyAlgorithm", "pwszPKeyString", "cbPKeySpecificData", "pbPKeySpecificData", "pPKeyId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetPKeyInformation(jitter):
    """
    HRESULT SLGetPKeyInformation(
        HSLC hSLC,
        const SLID* pPKeyId,
        PCWSTR pwszValueName,
        SLDATATYPE* peDataType,
        UINT* pcbValue,
        PBYTE* ppbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pPKeyId", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetPolicyInformation(jitter):
    """
    HRESULT SLGetPolicyInformation(
        HSLC hSLC,
        PCWSTR pwszValueName,
        SLDATATYPE* peDataType,
        UINT* pcbValue,
        PBYTE* ppbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetPolicyInformationDWORD(jitter):
    """
    HRESULT SLGetPolicyInformationDWORD(
        HSLC hSLC,
        PCWSTR pwszValueName,
        DWORD* pdwValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszValueName", "pdwValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetProductSkuInformation(jitter):
    """
    HRESULT SLGetProductSkuInformation(
        HSLC hSLC,
        const SLID* pProductSkuId,
        PCWSTR pwszValueName,
        SLDATATYPE* peDataType,
        UINT* pcbValue,
        PBYTE* ppbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetReferralInformation(jitter):
    """
    HRESULT SLGetReferralInformation(
        HSLC hSLC,
        SLREFERRALTYPE eReferralType,
        const SLID* pSkuOrAppId,
        PCWSTR pwszValueName,
        PWSTR* ppwszValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "eReferralType", "pSkuOrAppId", "pwszValueName", "ppwszValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetSAMLicense(jitter):
    """
    HRESULT SLGetSAMLicense(
        const SLID* pApplicationId,
        UINT* pcbXmlLicenseData,
        PBYTE* ppbXmlLicenseData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pApplicationId", "pcbXmlLicenseData", "ppbXmlLicenseData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetServerStatus(jitter):
    """
    HRESULT SLGetServerStatus(
        PCWSTR pwszServerURL,
        PCWSTR pwszAcquisitionType,
        PCWSTR pwszProxyServer,
        WORD wProxyPort,
        HRESULT* phrStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszServerURL", "pwszAcquisitionType", "pwszProxyServer", "wProxyPort", "phrStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetServiceInformation(jitter):
    """
    HRESULT SLGetServiceInformation(
        HSLC hSLC,
        PCWSTR pwszValueName,
        SLDATATYPE* peDataType,
        UINT* pcbValue,
        PBYTE* ppbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetSLIDList(jitter):
    """
    HRESULT SLGetSLIDList(
        HSLC hSLC,
        SLIDTYPE eQueryIdType,
        const SLID* pQueryId,
        SLIDTYPE eReturnIdType,
        UINT* pnReturnIds,
        SLID** ppReturnIds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "eQueryIdType", "pQueryId", "eReturnIdType", "pnReturnIds", "ppReturnIds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetWindowsInformation(jitter):
    """
    HRESULT SLGetWindowsInformation(
        PCWSTR pwszValueName,
        SLDATATYPE* peDataType,
        UINT* pcbValue,
        PBYTE* ppbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszValueName", "peDataType", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLGetWindowsInformationDWORD(jitter):
    """
    HRESULT SLGetWindowsInformationDWORD(
        PCWSTR pwszValueName,
        DWORD* pdwValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszValueName", "pdwValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLInstallLicense(jitter):
    """
    HRESULT SLInstallLicense(
        HSLC hSLC,
        UINT cbLicenseBlob,
        const BYTE* pbLicenseBlob,
        SLID* pLicenseFileId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "cbLicenseBlob", "pbLicenseBlob", "pLicenseFileId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLInstallProofOfPurchase(jitter):
    """
    HRESULT SLInstallProofOfPurchase(
        HSLC hSLC,
        PCWSTR pwszPKeyAlgorithm,
        PCWSTR pwszPKeyString,
        UINT cbPKeySpecificData,
        PBYTE pbPKeySpecificData,
        SLID* pPKeyId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszPKeyAlgorithm", "pwszPKeyString", "cbPKeySpecificData", "pbPKeySpecificData", "pPKeyId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLInstallProofOfPurchaseEx(jitter):
    """
    HRESULT SLInstallProofOfPurchaseEx(
        HSLC hSLC,
        const SLID* pApplicationId,
        const SLID* pProductSkuId,
        PCWSTR pwszPKeyAlgorithm,
        PCWSTR pwszPKeyString,
        UINT cbPKeySpecificData,
        PBYTE pbPKeySpecificData,
        SLID* pPKeyId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pApplicationId", "pProductSkuId", "pwszPKeyAlgorithm", "pwszPKeyString", "cbPKeySpecificData", "pbPKeySpecificData", "pPKeyId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLInstallSAMLicense(jitter):
    """
    HRESULT SLInstallSAMLicense(
        const SLID* pApplicationId,
        UINT cbXmlLicenseData,
        const BYTE* pbXmlLicenseData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pApplicationId", "cbXmlLicenseData", "pbXmlLicenseData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLLoadApplicationPolicies(jitter):
    """
    HRESULT SLLoadApplicationPolicies(
        const SLID* pApplicationId,
        const SLID* pProductSkuId,
        DWORD dwFlags,
        HSLP* phPolicyContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pApplicationId", "pProductSkuId", "dwFlags", "phPolicyContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLOpen(jitter):
    """
    HRESULT SLOpen(
        HSLC* phSLC
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phSLC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLPersistApplicationPolicies(jitter):
    """
    HRESULT SLPersistApplicationPolicies(
        const SLID* pApplicationId,
        const SLID* pProductSkuId,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pApplicationId", "pProductSkuId", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLPersistRTSPayloadOverride(jitter):
    """
    HRESULT SLPersistRTSPayloadOverride(
        HSLC hSLC,
        const SLID* pApplicationId,
        const SLID* pProductSkuId,
        BYTE* pbData,
        DWORD cbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pApplicationId", "pProductSkuId", "pbData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLReArm(jitter):
    """
    HRESULT SLReArm(
        HSLC hSLC,
        const SLID* pApplicationId,
        const SLID* pProductSkuId,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pApplicationId", "pProductSkuId", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLRegisterEvent(jitter):
    """
    HRESULT SLRegisterEvent(
        HSLC hSLC,
        PCWSTR pwszEventId,
        const SLID* pApplicationId,
        HANDLE hEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszEventId", "pApplicationId", "hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLSetAuthenticationData(jitter):
    """
    HRESULT SLSetAuthenticationData(
        HSLC hSLC,
        UINT cbValue,
        const BYTE* pbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "cbValue", "pbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLSetCurrentProductKey(jitter):
    """
    HRESULT SLSetCurrentProductKey(
        HSLC hSLC,
        const SLID* pProductSkuId,
        const SLID* pProductKeyId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pProductSkuId", "pProductKeyId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLUninstallLicense(jitter):
    """
    HRESULT SLUninstallLicense(
        HSLC hSLC,
        const SLID* pLicenseFileId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pLicenseFileId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLUninstallProofOfPurchase(jitter):
    """
    HRESULT SLUninstallProofOfPurchase(
        HSLC hSLC,
        const SLID* pPKeyId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pPKeyId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLUninstallSAMLicense(jitter):
    """
    HRESULT SLUninstallSAMLicense(
        const SLID* pApplicationId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pApplicationId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLUnloadApplicationPolicies(jitter):
    """
    HRESULT SLUnloadApplicationPolicies(
        HSLP hPolicyContext,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPolicyContext", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slc_SLUnregisterEvent(jitter):
    """
    HRESULT SLUnregisterEvent(
        HSLC hSLC,
        PCWSTR pwszEventId,
        const SLID* pApplicationId,
        HANDLE hEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSLC", "pwszEventId", "pApplicationId", "hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
