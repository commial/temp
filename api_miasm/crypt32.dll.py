
def crypt32_CryptInstallDefaultContext(jitter):
    """"
    [Crypt32.dll] BOOL CryptInstallDefaultContext(HCRYPTPROV hCryptProv, DWORD dwDefaultType, const void* pvDefaultPara, DWORD dwFlags, void* pvReserved, HCRYPTDEFAULTCONTEXT* phDefaultContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProv", "dwDefaultType", "pvDefaultPara", "dwFlags", "pvReserved", "phDefaultContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptUninstallDefaultContext(jitter):
    """"
    [Crypt32.dll] BOOL CryptUninstallDefaultContext(HCRYPTDEFAULTCONTEXT hDefaultContext, DWORD dwFlags, void* pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDefaultContext", "dwFlags", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptDecodeObject(jitter):
    """"
    [Crypt32.dll] BOOL CryptDecodeObject([CertEncodingType] dwCertEncodingType, LPCSTR lpszStructType, const BYTE* pbEncoded, DWORD cbEncoded, [CryptDecodeObjectFlags] dwFlags, void* pvStructInfo, DWORD* pcbStructInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "lpszStructType", "pbEncoded", "cbEncoded", "dwFlags", "pvStructInfo", "pcbStructInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptDecodeObjectEx(jitter):
    """"
    [Crypt32.dll] BOOL CryptDecodeObjectEx([CertEncodingType] dwCertEncodingType, LPCSTR lpszStructType, const BYTE* pbEncoded, DWORD cbEncoded, [CryptDecodeObjectFlags] dwFlags, PCRYPT_DECODE_PARA pDecodePara, void* pvStructInfo, DWORD* pcbStructInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "lpszStructType", "pbEncoded", "cbEncoded", "dwFlags", "pDecodePara", "pvStructInfo", "pcbStructInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptEncodeObject(jitter):
    """"
    [Crypt32.dll] BOOL CryptEncodeObject([CertEncodingType] dwCertEncodingType, LPCSTR lpszStructType, const void* pvStructInfo, BYTE* pbEncoded, DWORD* pcbEncoded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "lpszStructType", "pvStructInfo", "pbEncoded", "pcbEncoded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptEncodeObjectEx(jitter):
    """"
    [Crypt32.dll] BOOL CryptEncodeObjectEx([CertEncodingType] dwCertEncodingType, LPCSTR lpszStructType, const void* pvStructInfo, [CryptEncodeObjectFlags] dwFlags, PCRYPT_ENCODE_PARA pEncodePara, void* pvEncoded, DWORD* pcbEncoded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "lpszStructType", "pvStructInfo", "dwFlags", "pEncodePara", "pvEncoded", "pcbEncoded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptProtectData(jitter):
    """"
    [Crypt32.dll] BOOL CryptProtectData(DATA_BLOB* pDataIn, LPCWSTR szDataDescr, DATA_BLOB* pOptionalEntropy, PVOID pvReserved, CRYPTPROTECT_PROMPTSTRUCT* pPromptStruct, [CryptProtectDataFlags] dwFlags, DATA_BLOB* pDataOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pDataIn", "szDataDescr", "pOptionalEntropy", "pvReserved", "pPromptStruct", "dwFlags", "pDataOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptProtectMemory(jitter):
    """"
    [Crypt32.dll] BOOL CryptProtectMemory(LPVOID pData, DWORD cbData, [CryptProtectMemoryFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pData", "cbData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptUnprotectData(jitter):
    """"
    [Crypt32.dll] BOOL CryptUnprotectData(DATA_BLOB* pDataIn, LPWSTR* ppszDataDescr, DATA_BLOB* pOptionalEntropy, PVOID pvReserved, CRYPTPROTECT_PROMPTSTRUCT* pPromptStruct, [CryptProtectDataFlags] dwFlags, DATA_BLOB* pDataOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pDataIn", "ppszDataDescr", "pOptionalEntropy", "pvReserved", "pPromptStruct", "dwFlags", "pDataOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptUnprotectMemory(jitter):
    """"
    [Crypt32.dll] BOOL CryptUnprotectMemory(LPVOID pData, DWORD cbData, [CryptProtectMemoryFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pData", "cbData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAddStoreToCollection(jitter):
    """"
    [Crypt32.dll] BOOL CertAddStoreToCollection(HCERTSTORE hCollectionStore, HCERTSTORE hSiblingStore, [CertPhysicalStoreFlags] dwUpdateFlag, DWORD dwPriority)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCollectionStore", "hSiblingStore", "dwUpdateFlag", "dwPriority"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertCloseStore(jitter):
    """"
    [Crypt32.dll] BOOL CertCloseStore(HCERTSTORE hCertStore, [CertCloseStoreFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertControlStore(jitter):
    """"
    [Crypt32.dll] BOOL CertControlStore(HCERTSTORE hCertStore, DWORD dwFlags, [CertControlType] dwCtrlType, const void* pvCtrlPara)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "dwFlags", "dwCtrlType", "pvCtrlPara"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertDuplicateStore(jitter):
    """"
    [Crypt32.dll] HCERTSTORE CertDuplicateStore(HCERTSTORE hCertStore)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertEnumPhysicalStore(jitter):
    """"
    [Crypt32.dll] BOOL CertEnumPhysicalStore(const void* pvSystemStore, DWORD dwFlags, void* pvArg, PFN_CERT_ENUM_PHYSICAL_STORE pfnEnum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvSystemStore", "dwFlags", "pvArg", "pfnEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertEnumSystemStore(jitter):
    """"
    [Crypt32.dll] BOOL CertEnumSystemStore([CertSystemStoreFlags] dwFlags, void* pvSystemStoreLocationPara, void* pvArg, PFN_CERT_ENUM_SYSTEM_STORE pfnEnum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pvSystemStoreLocationPara", "pvArg", "pfnEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertEnumSystemStoreLocation(jitter):
    """"
    [Crypt32.dll] BOOL CertEnumSystemStoreLocation(DWORD dwFlags, void* pvArg, PFN_CERT_ENUM_SYSTEM_STORE_LOCATION pfnEnum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pvArg", "pfnEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetStoreProperty(jitter):
    """"
    [Crypt32.dll] BOOL CertGetStoreProperty(HCERTSTORE hCertStore, DWORD dwPropId, void* pvData, DWORD* pcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "dwPropId", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertOpenStore(jitter):
    """"
    [Crypt32.dll] HCERTSTORE CertOpenStore([CERT_STORE_PROVIDER] lpszStoreProvider, [CertEncodingType] dwMsgAndCertEncodingType, HCRYPTPROV_LEGACY hCryptProv, [CertOpenStoreFlags] dwFlags, const void* pvPara)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszStoreProvider", "dwMsgAndCertEncodingType", "hCryptProv", "dwFlags", "pvPara"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertOpenSystemStore(jitter, get_str, set_str):
    """"
    [Crypt32.dll] HCERTSTORE CertOpenSystemStore(HCRYPTPROV_LEGACY hprov, LPCTSTR szSubsystemProtocol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hprov", "szSubsystemProtocol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertOpenSystemStoreA(jitter):
    crypt32_CertOpenSystemStore(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def crypt32_CertOpenSystemStoreW(jitter):
    crypt32_CertOpenSystemStore(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def crypt32_CertRegisterPhysicalStore(jitter):
    """"
    [Crypt32.dll] BOOL CertRegisterPhysicalStore(const void* pvSystemStore, DWORD dwFlags, LPCWSTR pwszStoreName, PCERT_PHYSICAL_STORE_INFO pStoreInfo, void* pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvSystemStore", "dwFlags", "pwszStoreName", "pStoreInfo", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertRegisterSystemStore(jitter):
    """"
    [Crypt32.dll] BOOL CertRegisterSystemStore(const void* pvSystemStore, DWORD dwFlags, PCERT_SYSTEM_STORE_INFO pStoreInfo, void* pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvSystemStore", "dwFlags", "pStoreInfo", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertRemoveStoreFromCollection(jitter):
    """"
    [Crypt32.dll] void CertRemoveStoreFromCollection(HCERTSTORE hCollectionStore, HCERTSTORE hSiblingStore)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCollectionStore", "hSiblingStore"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertSaveStore(jitter):
    """"
    [Crypt32.dll] BOOL CertSaveStore(HCERTSTORE hCertStore, DWORD dwMsgAndCertEncodingType, DWORD dwSaveAs, DWORD dwSaveTo, void* pvSaveToPara, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "dwMsgAndCertEncodingType", "dwSaveAs", "dwSaveTo", "pvSaveToPara", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertSetStoreProperty(jitter):
    """"
    [Crypt32.dll] BOOL CertSetStoreProperty(HCERTSTORE hCertStore, DWORD dwPropId, DWORD dwFlags, const void* pvData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "dwPropId", "dwFlags", "pvData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertUnregisterPhysicalStore(jitter):
    """"
    [Crypt32.dll] BOOL CertUnregisterPhysicalStore(const void* pvSystemStore, DWORD dwFlags, LPCWSTR pwszStoreName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvSystemStore", "dwFlags", "pwszStoreName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertUnregisterSystemStore(jitter):
    """"
    [Crypt32.dll] BOOL CertUnregisterSystemStore(const void* pvSystemStore, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvSystemStore", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAddSerializedElementToStore(jitter):
    """"
    [Crypt32.dll] BOOL CertAddSerializedElementToStore(HCERTSTORE hCertStore, const BYTE* pbElement, DWORD cbElement, DWORD dwAddDisposition, DWORD dwFlags, DWORD dwContextTypeFlags, [CertificateStoreContextType*] pdwContextType, const void** ppvContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "pbElement", "cbElement", "dwAddDisposition", "dwFlags", "dwContextTypeFlags", "pdwContextType", "ppvContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertCreateContext(jitter):
    """"
    [Crypt32.dll] const void* CertCreateContext([CertificateStoreContextType] dwContextType, [CertEncodingType] dwEncodingType, const BYTE* pbEncoded, DWORD cbEncoded, [CertCreateContextFlags] dwFlags, PCERT_CREATE_CONTEXT_PARA pCreatePara)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwContextType", "dwEncodingType", "pbEncoded", "cbEncoded", "dwFlags", "pCreatePara"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertEnumSubjectInSortedCTL(jitter):
    """"
    [Crypt32.dll] BOOL CertEnumSubjectInSortedCTL(PCCTL_CONTEXT pCtlContext, void** ppvNextSubject, PCRYPT_DER_BLOB pSubjectIdentifier, PCRYPT_DER_BLOB pEncodedAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCtlContext", "ppvNextSubject", "pSubjectIdentifier", "pEncodedAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFindSubjectInCTL(jitter):
    """"
    [Crypt32.dll] PCTL_ENTRY CertFindSubjectInCTL([CertEncodingType] dwEncodingType, DWORD dwSubjectType, void* pvSubject, PCCTL_CONTEXT pCtlContext, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwEncodingType", "dwSubjectType", "pvSubject", "pCtlContext", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFindSubjectInSortedCTL(jitter):
    """"
    [Crypt32.dll] BOOL CertFindSubjectInSortedCTL(PCRYPT_DATA_BLOB pSubjectIdentifier, PCCTL_CONTEXT pCtlContext, DWORD dwFlags, void* pvReserved, PCRYPT_DER_BLOB pEncodedAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSubjectIdentifier", "pCtlContext", "dwFlags", "pvReserved", "pEncodedAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAddCertificateContextToStore(jitter):
    """"
    [Crypt32.dll] BOOL CertAddCertificateContextToStore(HCERTSTORE hCertStore, PCCERT_CONTEXT pCertContext, DWORD dwAddDisposition, PCCERT_CONTEXT* ppStoreContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "pCertContext", "dwAddDisposition", "ppStoreContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAddCertificateLinkToStore(jitter):
    """"
    [Crypt32.dll] BOOL CertAddCertificateLinkToStore(HCERTSTORE hCertStore, PCCERT_CONTEXT pCertContext, DWORD dwAddDisposition, PCCERT_CONTEXT* ppStoreContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "pCertContext", "dwAddDisposition", "ppStoreContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAddEncodedCertificateToStore(jitter):
    """"
    [Crypt32.dll] BOOL CertAddEncodedCertificateToStore(HCERTSTORE hCertStore, [CertEncodingType] dwCertEncodingType, const BYTE* pbCertEncoded, DWORD cbCertEncoded, [CertStoreAddDisposition] dwAddDisposition, PCCERT_CONTEXT* ppCertContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "dwCertEncodingType", "pbCertEncoded", "cbCertEncoded", "dwAddDisposition", "ppCertContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAddRefServerOcspResponse(jitter):
    """"
    [Crypt32.dll] VOID CertAddRefServerOcspResponse(HCERT_SERVER_OCSP_RESPONSE hServerOcspResponse)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServerOcspResponse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAddRefServerOcspResponseContext(jitter):
    """"
    [Crypt32.dll] VOID CertAddRefServerOcspResponseContext(PCCERT_SERVER_OCSP_RESPONSE_CONTEXT pServerOcspResponseContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pServerOcspResponseContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertCloseServerOcspResponse(jitter):
    """"
    [Crypt32.dll] VOID CertCloseServerOcspResponse(HCERT_SERVER_OCSP_RESPONSE hServerOcspResponse, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServerOcspResponse", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertCreateCertificateContext(jitter):
    """"
    [Crypt32.dll] PCCERT_CONTEXT CertCreateCertificateContext([CertEncodingType] dwCertEncodingType, const BYTE* pbCertEncoded, DWORD cbCertEncoded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "pbCertEncoded", "cbCertEncoded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertCreateSelfSignCertificate(jitter):
    """"
    [Crypt32.dll] PCCERT_CONTEXT CertCreateSelfSignCertificate(HCRYPTPROV_OR_NCRYPT_KEY_HANDLE hCryptProvOrNCryptKey, PCERT_NAME_BLOB pSubjectIssuerBlob, DWORD dwFlags, PCRYPT_KEY_PROV_INFO pKeyProvInfo, PCRYPT_ALGORITHM_IDENTIFIER pSignatureAlgorithm, PSYSTEMTIME pStartTime, PSYSTEMTIME pEndTime, PCERT_EXTENSIONS pExtensions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProvOrNCryptKey", "pSubjectIssuerBlob", "dwFlags", "pKeyProvInfo", "pSignatureAlgorithm", "pStartTime", "pEndTime", "pExtensions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertDeleteCertificateFromStore(jitter):
    """"
    [Crypt32.dll] BOOL CertDeleteCertificateFromStore(PCCERT_CONTEXT pCertContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertDuplicateCertificateContext(jitter):
    """"
    [Crypt32.dll] PCCERT_CONTEXT CertDuplicateCertificateContext(PCCERT_CONTEXT pCertContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertEnumCertificatesInStore(jitter):
    """"
    [Crypt32.dll] PCCERT_CONTEXT CertEnumCertificatesInStore(HCERTSTORE hCertStore, PCCERT_CONTEXT pPrevCertContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "pPrevCertContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFindCertificateInStore(jitter):
    """"
    [Crypt32.dll] PCCERT_CONTEXT CertFindCertificateInStore(HCERTSTORE hCertStore, [CertEncodingType] dwCertEncodingType, DWORD dwFindFlags, [CertFindType] dwFindType, const void* pvFindPara, PCCERT_CONTEXT pPrevCertContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "dwCertEncodingType", "dwFindFlags", "dwFindType", "pvFindPara", "pPrevCertContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFreeCertificateContext(jitter):
    """"
    [Crypt32.dll] BOOL CertFreeCertificateContext(PCCERT_CONTEXT pCertContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetIssuerCertificateFromStore(jitter):
    """"
    [Crypt32.dll] PCCERT_CONTEXT CertGetIssuerCertificateFromStore(HCERTSTORE hCertStore, PCCERT_CONTEXT pSubjectContext, PCCERT_CONTEXT pPrevIssuerContext, DWORD* pdwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "pSubjectContext", "pPrevIssuerContext", "pdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetServerOcspResponseContext(jitter):
    """"
    [Crypt32.dll] PCCERT_SERVER_OCSP_RESPONSE_CONTEXT CertGetServerOcspResponseContext(HCERT_SERVER_OCSP_RESPONSE hServerOcspResponse, DWORD dwFlags, LPVOID pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServerOcspResponse", "dwFlags", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetSubjectCertificateFromStore(jitter):
    """"
    [Crypt32.dll] PCCERT_CONTEXT CertGetSubjectCertificateFromStore(HCERTSTORE hCertStore, [CertEncodingType] dwCertEncodingType, PCERT_INFO pCertId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "dwCertEncodingType", "pCertId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetValidUsages(jitter):
    """"
    [Crypt32.dll] BOOL CertGetValidUsages(DWORD cCerts, PCCERT_CONTEXT* rghCerts, int* cNumOIDs, LPSTR* rghOIDs, DWORD* pcbOIDs)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cCerts", "rghCerts", "cNumOIDs", "rghOIDs", "pcbOIDs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertOpenServerOcspResponse(jitter):
    """"
    [Crypt32.dll] HCERT_SERVER_OCSP_RESPONSE CertOpenServerOcspResponse(PCCERT_CHAIN_CONTEXT pChainContext, DWORD dwFlags, LPVOID pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pChainContext", "dwFlags", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertRetrieveLogoOrBiometricInfo(jitter):
    """"
    [Crypt32.dll] BOOL CertRetrieveLogoOrBiometricInfo(PCCERT_CONTEXT pCertContext, LPCSTR lpszLogoOrBiometricType, DWORD dwRetrievalFlags, DWORD dwTimeout, DWORD dwFlags, void* pvReserved, BYTE** ppbData, DWORD* pcbData, LPWSTR* ppwszMimeType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext", "lpszLogoOrBiometricType", "dwRetrievalFlags", "dwTimeout", "dwFlags", "pvReserved", "ppbData", "pcbData", "ppwszMimeType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertSelectCertificateChains(jitter):
    """"
    [Crypt32.dll] BOOL CertSelectCertificateChains(LPCGUID pSelectionContext, [CertSelectFlags] dwFlags, PCCERT_SELECT_CHAIN_PARA pChainParameters, DWORD cCriteria, PCCERT_SELECT_CRITERIA rgpCriteria, HCERTSTORE hStore, PDWORD pcSelection, PCCERT_CHAIN_CONTEXT** pprgpSelection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSelectionContext", "dwFlags", "pChainParameters", "cCriteria", "rgpCriteria", "hStore", "pcSelection", "pprgpSelection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertSerializeCertificateStoreElement(jitter):
    """"
    [Crypt32.dll] BOOL CertSerializeCertificateStoreElement(PCCERT_CONTEXT pCertContext, DWORD dwFlags, BYTE* pbElement, DWORD* pcbElement)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext", "dwFlags", "pbElement", "pcbElement"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertVerifySubjectCertificateContext(jitter):
    """"
    [Crypt32.dll] BOOL CertVerifySubjectCertificateContext(PCCERT_CONTEXT pSubject, PCCERT_CONTEXT pIssuer, DWORD* pdwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSubject", "pIssuer", "pdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAddCRLContextToStore(jitter):
    """"
    [Crypt32.dll] BOOL CertAddCRLContextToStore(HCERTSTORE hCertStore, PCCRL_CONTEXT pCrlContext, DWORD dwAddDisposition, PCCRL_CONTEXT* ppStoreContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "pCrlContext", "dwAddDisposition", "ppStoreContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAddCRLLinkToStore(jitter):
    """"
    [Crypt32.dll] BOOL CertAddCRLLinkToStore(HCERTSTORE hCertStore, PCCRL_CONTEXT pCrlContext, DWORD dwAddDisposition, PCCRL_CONTEXT* ppStoreContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "pCrlContext", "dwAddDisposition", "ppStoreContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAddEncodedCRLToStore(jitter):
    """"
    [Crypt32.dll] BOOL CertAddEncodedCRLToStore(HCERTSTORE hCertStore, [CertEncodingType] dwCertEncodingType, const BYTE* pbCrlEncoded, DWORD cbCrlEncoded, DWORD dwAddDisposition, PCCRL_CONTEXT* ppCrlContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "dwCertEncodingType", "pbCrlEncoded", "cbCrlEncoded", "dwAddDisposition", "ppCrlContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertCreateCRLContext(jitter):
    """"
    [Crypt32.dll] PCCRL_CONTEXT CertCreateCRLContext([CertEncodingType] dwCertEncodingType, const BYTE* pbCrlEncoded, DWORD cbCrlEncoded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "pbCrlEncoded", "cbCrlEncoded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertDeleteCRLFromStore(jitter):
    """"
    [Crypt32.dll] BOOL CertDeleteCRLFromStore(PCCRL_CONTEXT pCrlContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCrlContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertDuplicateCRLContext(jitter):
    """"
    [Crypt32.dll] PCCRL_CONTEXT CertDuplicateCRLContext(PCCRL_CONTEXT pCrlContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCrlContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertEnumCRLsInStore(jitter):
    """"
    [Crypt32.dll] PCCRL_CONTEXT CertEnumCRLsInStore(HCERTSTORE hCertStore, PCCRL_CONTEXT pPrevCrlContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "pPrevCrlContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFindCertificateInCRL(jitter):
    """"
    [Crypt32.dll] BOOL CertFindCertificateInCRL(PCCERT_CONTEXT pCert, PCCRL_CONTEXT pCrlContext, DWORD dwFlags, void* pvReserved, PCRL_ENTRY* ppCrlEntry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCert", "pCrlContext", "dwFlags", "pvReserved", "ppCrlEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFindCRLInStore(jitter):
    """"
    [Crypt32.dll] PCCRL_CONTEXT CertFindCRLInStore(HCERTSTORE hCertStore, [CertEncodingType] dwEncodingType, [CrlFindIssuedByFlags] dwFindFlags, [CrlFindType] dwFindType, const void* pvFindPara, PCCRL_CONTEXT pPrevCrlContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "dwEncodingType", "dwFindFlags", "dwFindType", "pvFindPara", "pPrevCrlContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFreeCRLContext(jitter):
    """"
    [Crypt32.dll] BOOL CertFreeCRLContext(PCCRL_CONTEXT pCrlContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCrlContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetCRLFromStore(jitter):
    """"
    [Crypt32.dll] PCCRL_CONTEXT CertGetCRLFromStore(HCERTSTORE hCertStore, PCCERT_CONTEXT pIssuerContext, PCCRL_CONTEXT pPrevCrlContext, DWORD* pdwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "pIssuerContext", "pPrevCrlContext", "pdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertSerializeCRLStoreElement(jitter):
    """"
    [Crypt32.dll] BOOL CertSerializeCRLStoreElement(PCCRL_CONTEXT pCrlContext, DWORD dwFlags, BYTE* pbElement, DWORD* pcbElement)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCrlContext", "dwFlags", "pbElement", "pcbElement"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAddCTLContextToStore(jitter):
    """"
    [Crypt32.dll] BOOL CertAddCTLContextToStore(HCERTSTORE hCertStore, PCCTL_CONTEXT pCtlContext, DWORD dwAddDisposition, PCCTL_CONTEXT* ppStoreContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "pCtlContext", "dwAddDisposition", "ppStoreContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAddCTLLinkToStore(jitter):
    """"
    [Crypt32.dll] BOOL CertAddCTLLinkToStore(HCERTSTORE hCertStore, PCCTL_CONTEXT pCtlContext, DWORD dwAddDisposition, PCCTL_CONTEXT* ppStoreContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "pCtlContext", "dwAddDisposition", "ppStoreContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAddEncodedCTLToStore(jitter):
    """"
    [Crypt32.dll] BOOL CertAddEncodedCTLToStore(HCERTSTORE hCertStore, DWORD dwMsgAndCertEncodingType, const BYTE* pbCtlEncoded, DWORD cbCtlEncoded, DWORD dwAddDisposition, PCCTL_CONTEXT* ppCtlContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "dwMsgAndCertEncodingType", "pbCtlEncoded", "cbCtlEncoded", "dwAddDisposition", "ppCtlContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertCreateCTLContext(jitter):
    """"
    [Crypt32.dll] PCCTL_CONTEXT CertCreateCTLContext(DWORD dwMsgAndCertEncodingType, const BYTE* pbCtlEncoded, DWORD cbCtlEncoded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwMsgAndCertEncodingType", "pbCtlEncoded", "cbCtlEncoded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertDeleteCTLFromStore(jitter):
    """"
    [Crypt32.dll] BOOL CertDeleteCTLFromStore(PCCTL_CONTEXT pCtlContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCtlContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertDuplicateCTLContext(jitter):
    """"
    [Crypt32.dll] PCCTL_CONTEXT CertDuplicateCTLContext(PCCTL_CONTEXT pCtlContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCtlContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertEnumCTLsInStore(jitter):
    """"
    [Crypt32.dll] PCCTL_CONTEXT CertEnumCTLsInStore(HCERTSTORE hCertStore, PCCTL_CONTEXT pPrevCtlContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "pPrevCtlContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFindCTLInStore(jitter):
    """"
    [Crypt32.dll] PCCTL_CONTEXT CertFindCTLInStore(HCERTSTORE hCertStore, DWORD dwMsgAndCertEncodingType, DWORD dwFindFlags, DWORD dwFindType, const void* pvFindPara, PCCTL_CONTEXT pPrevCtlContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "dwMsgAndCertEncodingType", "dwFindFlags", "dwFindType", "pvFindPara", "pPrevCtlContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFreeCTLContext(jitter):
    """"
    [Crypt32.dll] BOOL CertFreeCTLContext(PCCTL_CONTEXT pCtlContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCtlContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertSerializeCTLStoreElement(jitter):
    """"
    [Crypt32.dll] BOOL CertSerializeCTLStoreElement(PCCTL_CONTEXT pCtlContext, DWORD dwFlags, BYTE* pbElement, DWORD* pcbElement)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCtlContext", "dwFlags", "pbElement", "pcbElement"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertEnumCertificateContextProperties(jitter):
    """"
    [Crypt32.dll] DWORD CertEnumCertificateContextProperties(PCCERT_CONTEXT pCertContext, DWORD dwPropId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext", "dwPropId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertEnumCRLContextProperties(jitter):
    """"
    [Crypt32.dll] DWORD CertEnumCRLContextProperties(PCCRL_CONTEXT pCrlContext, DWORD dwPropId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCrlContext", "dwPropId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertEnumCTLContextProperties(jitter):
    """"
    [Crypt32.dll] DWORD CertEnumCTLContextProperties(PCCTL_CONTEXT pCtlContext, DWORD dwPropId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCtlContext", "dwPropId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetCertificateContextProperty(jitter):
    """"
    [Crypt32.dll] BOOL CertGetCertificateContextProperty(PCCERT_CONTEXT pCertContext, [CertPropId] dwPropId, void* pvData, DWORD* pcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext", "dwPropId", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetCRLContextProperty(jitter):
    """"
    [Crypt32.dll] BOOL CertGetCRLContextProperty(PCCRL_CONTEXT pCrlContext, [CertPropId] dwPropId, void* pvData, DWORD* pcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCrlContext", "dwPropId", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetCTLContextProperty(jitter):
    """"
    [Crypt32.dll] BOOL CertGetCTLContextProperty(PCCTL_CONTEXT pCtlContext, [CertPropId] dwPropId, void* pvData, DWORD* pcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCtlContext", "dwPropId", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertSetCertificateContextProperty(jitter):
    """"
    [Crypt32.dll] BOOL CertSetCertificateContextProperty(PCCERT_CONTEXT pCertContext, [CertPropId] dwPropId, [CertSetPropertyFlags] dwFlags, const void* pvData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext", "dwPropId", "dwFlags", "pvData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertSetCRLContextProperty(jitter):
    """"
    [Crypt32.dll] BOOL CertSetCRLContextProperty(PCCRL_CONTEXT pCrlContext, [CertPropId] dwPropId, [CertSetPropertyFlags] dwFlags, const void* pvData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCrlContext", "dwPropId", "dwFlags", "pvData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertSetCTLContextProperty(jitter):
    """"
    [Crypt32.dll] BOOL CertSetCTLContextProperty(PCCTL_CONTEXT pCtlContext, [CertPropId] dwPropId, DWORD dwFlags, const void* pvData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCtlContext", "dwPropId", "dwFlags", "pvData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertVerifyCTLUsage(jitter):
    """"
    [Crypt32.dll] BOOL CertVerifyCTLUsage([CertEncodingType] dwEncodingType, DWORD dwSubjectType, void* pvSubject, PCTL_USAGE pSubjectUsage, DWORD dwFlags, PCTL_VERIFY_USAGE_PARA pVerifyUsagePara, PCTL_VERIFY_USAGE_STATUS pVerifyUsageStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwEncodingType", "dwSubjectType", "pvSubject", "pSubjectUsage", "dwFlags", "pVerifyUsagePara", "pVerifyUsageStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgEncodeAndSignCTL(jitter):
    """"
    [Crypt32.dll] BOOL CryptMsgEncodeAndSignCTL([CertEncodingType] dwMsgEncodingType, PCTL_INFO pCtlInfo, PCMSG_SIGNED_ENCODE_INFO pSignInfo, DWORD dwFlags, BYTE* pbEncoded, DWORD* pcbEncoded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwMsgEncodingType", "pCtlInfo", "pSignInfo", "dwFlags", "pbEncoded", "pcbEncoded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgGetAndVerifySigner(jitter):
    """"
    [Crypt32.dll] BOOL CryptMsgGetAndVerifySigner(HCRYPTMSG hCryptMsg, DWORD cSignerStore, HCERTSTORE* rghSignerStore, DWORD dwFlags, PCCERT_CONTEXT* ppSigner, DWORD* pdwSignerIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptMsg", "cSignerStore", "rghSignerStore", "dwFlags", "ppSigner", "pdwSignerIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgSignCTL(jitter):
    """"
    [Crypt32.dll] BOOL CryptMsgSignCTL([CertEncodingType] dwMsgEncodingType, BYTE* pbCtlContent, DWORD cbCtlContent, PCMSG_SIGNED_ENCODE_INFO pSignInfo, DWORD dwFlags, BYTE* pbEncoded, DWORD* pcbEncoded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwMsgEncodingType", "pbCtlContent", "cbCtlContent", "pSignInfo", "dwFlags", "pbEncoded", "pcbEncoded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertCreateCertificateChainEngine(jitter):
    """"
    [Crypt32.dll] BOOL CertCreateCertificateChainEngine(PCERT_CHAIN_ENGINE_CONFIG pConfig, HCERTCHAINENGINE* phChainEngine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pConfig", "phChainEngine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertCreateCTLEntryFromCertificateContextProperties(jitter):
    """"
    [Crypt32.dll] BOOL CertCreateCTLEntryFromCertificateContextProperties(PCCERT_CONTEXT pCertContext, DWORD cOptAttr, PCRYPT_ATTRIBUTE rgOptAttr, DWORD dwFlags, void* pvReserved, PCTL_ENTRY pCtlEntry, DWORD* pcbCtlEntry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext", "cOptAttr", "rgOptAttr", "dwFlags", "pvReserved", "pCtlEntry", "pcbCtlEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertDuplicateCertificateChain(jitter):
    """"
    [Crypt32.dll] PCCERT_CHAIN_CONTEXT CertDuplicateCertificateChain(PCCERT_CHAIN_CONTEXT pChainContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pChainContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFindChainInStore(jitter):
    """"
    [Crypt32.dll] PCCERT_CHAIN_CONTEXT CertFindChainInStore(HCERTSTORE hCertStore, [CertEncodingType] dwCertEncodingType, DWORD dwFindFlags, DWORD dwFindType, const void* pvFindPara, PCCERT_CHAIN_CONTEXT pPrevChainContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "dwCertEncodingType", "dwFindFlags", "dwFindType", "pvFindPara", "pPrevChainContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFreeCertificateChain(jitter):
    """"
    [Crypt32.dll] VOID CertFreeCertificateChain(PCCERT_CHAIN_CONTEXT pChainContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pChainContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFreeCertificateChainEngine(jitter):
    """"
    [Crypt32.dll] void CertFreeCertificateChainEngine(HCERTCHAINENGINE hChainEngine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hChainEngine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFreeCertificateChainList(jitter):
    """"
    [Crypt32.dll] VOID CertFreeCertificateChainList(PCCERT_CHAIN_CONTEXT* prgpSelection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["prgpSelection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetCertificateChain(jitter):
    """"
    [Crypt32.dll] BOOL CertGetCertificateChain(HCERTCHAINENGINE hChainEngine, PCCERT_CONTEXT pCertContext, LPFILETIME pTime, HCERTSTORE hAdditionalStore, PCERT_CHAIN_PARA pChainPara, [CertChainFlags] dwFlags, LPVOID pvReserved, PCCERT_CHAIN_CONTEXT* ppChainContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hChainEngine", "pCertContext", "pTime", "hAdditionalStore", "pChainPara", "dwFlags", "pvReserved", "ppChainContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertIsValidCRLForCertificate(jitter):
    """"
    [Crypt32.dll] BOOL CertIsValidCRLForCertificate(PCCERT_CONTEXT pCert, PCCRL_CONTEXT pCRL, DWORD dwFlags, void* pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCert", "pCRL", "dwFlags", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertSetCertificateContextPropertiesFromCTLEntry(jitter):
    """"
    [Crypt32.dll] BOOL CertSetCertificateContextPropertiesFromCTLEntry(PCCERT_CONTEXT pCertContext, PCTL_ENTRY pCtlEntry, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext", "pCtlEntry", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertVerifyCertificateChainPolicy(jitter):
    """"
    [Crypt32.dll] BOOL CertVerifyCertificateChainPolicy(LPCSTR pszPolicyOID, PCCERT_CHAIN_CONTEXT pChainContext, PCERT_CHAIN_POLICY_PARA pPolicyPara, PCERT_CHAIN_POLICY_STATUS pPolicyStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPolicyOID", "pChainContext", "pPolicyPara", "pPolicyStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgCalculateEncodedLength(jitter):
    """"
    [Crypt32.dll] DWORD CryptMsgCalculateEncodedLength([CertEncodingType] dwMsgEncodingType, DWORD dwFlags, [CryptMsgType] dwMsgType, const void* pvMsgEncodeInfo, LPSTR pszInnerContentObjID, DWORD cbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwMsgEncodingType", "dwFlags", "dwMsgType", "pvMsgEncodeInfo", "pszInnerContentObjID", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgClose(jitter):
    """"
    [Crypt32.dll] BOOL CryptMsgClose(HCRYPTMSG hCryptMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgControl(jitter):
    """"
    [Crypt32.dll] BOOL CryptMsgControl(HCRYPTMSG hCryptMsg, [CryptMsgControlFlags] dwFlags, [CryptMsgControlType] dwCtrlType, const void* pvCtrlPara)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptMsg", "dwFlags", "dwCtrlType", "pvCtrlPara"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgUpdate(jitter):
    """"
    [Crypt32.dll] BOOL CryptMsgUpdate(HCRYPTMSG hCryptMsg, const BYTE* pbData, DWORD cbData, BOOL fFinal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptMsg", "pbData", "cbData", "fFinal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgCountersign(jitter):
    """"
    [Crypt32.dll] BOOL CryptMsgCountersign(HCRYPTMSG hCryptMsg, DWORD dwIndex, DWORD cCountersigners, PCMSG_SIGNER_ENCODE_INFO rgCountersigners)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptMsg", "dwIndex", "cCountersigners", "rgCountersigners"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgCountersignEncoded(jitter):
    """"
    [Crypt32.dll] BOOL CryptMsgCountersignEncoded([CertEncodingType] dwEncodingType, PBYTE pbSignerInfo, DWORD cbSignerInfo, DWORD cCountersigners, PCMSG_SIGNER_ENCODE_INFO rgCountersigners, PBYTE pbCountersignature, PDWORD pcbCountersignature)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwEncodingType", "pbSignerInfo", "cbSignerInfo", "cCountersigners", "rgCountersigners", "pbCountersignature", "pcbCountersignature"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgDuplicate(jitter):
    """"
    [Crypt32.dll] HCRYPTMSG CryptMsgDuplicate(HCRYPTMSG hCryptMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgGetParam(jitter):
    """"
    [Crypt32.dll] BOOL CryptMsgGetParam(HCRYPTMSG hCryptMsg, [CryptMsgParamType] dwParamType, DWORD dwIndex, void* pvData, DWORD* pcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptMsg", "dwParamType", "dwIndex", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgOpenToDecode(jitter):
    """"
    [Crypt32.dll] HCRYPTMSG CryptMsgOpenToDecode([CertEncodingType] dwMsgEncodingType, [CryptMsgOpenFlags] dwFlags, [CryptMsgType] dwMsgType, HCRYPTPROV_LEGACY hCryptProv, PCERT_INFO pRecipientInfo, PCMSG_STREAM_INFO pStreamInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwMsgEncodingType", "dwFlags", "dwMsgType", "hCryptProv", "pRecipientInfo", "pStreamInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgOpenToEncode(jitter):
    """"
    [Crypt32.dll] HCRYPTMSG CryptMsgOpenToEncode([CertEncodingType] dwMsgEncodingType, DWORD dwFlags, [CryptMsgType] dwMsgType, const void* pvMsgEncodeInfo, LPSTR pszInnerContentObjID, PCMSG_STREAM_INFO pStreamInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwMsgEncodingType", "dwFlags", "dwMsgType", "pvMsgEncodeInfo", "pszInnerContentObjID", "pStreamInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgVerifyCountersignatureEncoded(jitter):
    """"
    [Crypt32.dll] BOOL CryptMsgVerifyCountersignatureEncoded(HCRYPTPROV_LEGACY hCryptProv, [CertEncodingType] dwEncodingType, PBYTE pbSignerInfo, DWORD cbSignerInfo, PBYTE pbSignerInfoCountersignature, DWORD cbSignerInfoCountersignature, PCERT_INFO pciCountersigner)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProv", "dwEncodingType", "pbSignerInfo", "cbSignerInfo", "pbSignerInfoCountersignature", "cbSignerInfoCountersignature", "pciCountersigner"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMsgVerifyCountersignatureEncodedEx(jitter):
    """"
    [Crypt32.dll] BOOL CryptMsgVerifyCountersignatureEncodedEx(HCRYPTPROV_LEGACY hCryptProv, [CertEncodingType] dwEncodingType, PBYTE pbSignerInfo, DWORD cbSignerInfo, PBYTE pbSignerInfoCountersignature, DWORD cbSignerInfoCountersignature, [CryptMsgSignerType] dwSignerType, void* pvSigner, DWORD dwFlags, void* pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProv", "dwEncodingType", "pbSignerInfo", "cbSignerInfo", "pbSignerInfoCountersignature", "cbSignerInfoCountersignature", "dwSignerType", "pvSigner", "dwFlags", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptDecodeMessage(jitter):
    """"
    [Crypt32.dll] BOOL CryptDecodeMessage(DWORD dwMsgTypeFlags, PCRYPT_DECRYPT_MESSAGE_PARA pDecryptPara, PCRYPT_VERIFY_MESSAGE_PARA pVerifyPara, DWORD dwSignerIndex, const BYTE* pbEncodedBlob, DWORD cbEncodedBlob, DWORD dwPrevInnerContentType, [CryptMsgType*] pdwMsgType, DWORD* pdwInnerContentType, BYTE* pbDecoded, DWORD* pcbDecoded, PCCERT_CONTEXT* ppXchgCert, PCCERT_CONTEXT* ppSignerCert)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwMsgTypeFlags", "pDecryptPara", "pVerifyPara", "dwSignerIndex", "pbEncodedBlob", "cbEncodedBlob", "dwPrevInnerContentType", "pdwMsgType", "pdwInnerContentType", "pbDecoded", "pcbDecoded", "ppXchgCert", "ppSignerCert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptDecryptAndVerifyMessageSignature(jitter):
    """"
    [Crypt32.dll] BOOL CryptDecryptAndVerifyMessageSignature(PCRYPT_DECRYPT_MESSAGE_PARA pDecryptPara, PCRYPT_VERIFY_MESSAGE_PARA pVerifyPara, DWORD dwSignerIndex, const BYTE* pbEncryptedBlob, DWORD cbEncryptedBlob, BYTE* pbDecrypted, DWORD* pcbDecrypted, PCCERT_CONTEXT* ppXchgCert, PCCERT_CONTEXT* ppSignerCert)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pDecryptPara", "pVerifyPara", "dwSignerIndex", "pbEncryptedBlob", "cbEncryptedBlob", "pbDecrypted", "pcbDecrypted", "ppXchgCert", "ppSignerCert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptDecryptMessage(jitter):
    """"
    [Crypt32.dll] BOOL CryptDecryptMessage(PCRYPT_DECRYPT_MESSAGE_PARA pDecryptPara, const BYTE* pbEncryptedBlob, DWORD cbEncryptedBlob, BYTE* pbDecrypted, DWORD* pcbDecrypted, PCCERT_CONTEXT* ppXchgCert)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pDecryptPara", "pbEncryptedBlob", "cbEncryptedBlob", "pbDecrypted", "pcbDecrypted", "ppXchgCert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptEncryptMessage(jitter):
    """"
    [Crypt32.dll] BOOL CryptEncryptMessage(PCRYPT_ENCRYPT_MESSAGE_PARA pEncryptPara, DWORD cRecipientCert, PCCERT_CONTEXT [] rgpRecipientCert, const BYTE* pbToBeEncrypted, DWORD cbToBeEncrypted, BYTE* pbEncryptedBlob, DWORD* pcbEncryptedBlob)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pEncryptPara", "cRecipientCert", "rgpRecipientCert", "pbToBeEncrypted", "cbToBeEncrypted", "pbEncryptedBlob", "pcbEncryptedBlob"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptGetMessageCertificates(jitter):
    """"
    [Crypt32.dll] HCERTSTORE CryptGetMessageCertificates(DWORD dwMsgAndCertEncodingType, HCRYPTPROV_LEGACY hCryptProv, DWORD dwFlags, const BYTE* pbSignedBlob, DWORD cbSignedBlob)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwMsgAndCertEncodingType", "hCryptProv", "dwFlags", "pbSignedBlob", "cbSignedBlob"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptGetMessageSignerCount(jitter):
    """"
    [Crypt32.dll] LONG CryptGetMessageSignerCount([CertEncodingType] dwMsgEncodingType, const BYTE* pbSignedBlob, DWORD cbSignedBlob)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwMsgEncodingType", "pbSignedBlob", "cbSignedBlob"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptHashMessage(jitter):
    """"
    [Crypt32.dll] BOOL CryptHashMessage(PCRYPT_HASH_MESSAGE_PARA pHashPara, BOOL fDetachedHash, DWORD cToBeHashed, const BYTE* [] rgpbToBeHashed, DWORD [] rgcbToBeHashed, BYTE* pbHashedBlob, DWORD* pcbHashedBlob, BYTE* pbComputedHash, DWORD* pcbComputedHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pHashPara", "fDetachedHash", "cToBeHashed", "rgpbToBeHashed", "rgcbToBeHashed", "pbHashedBlob", "pcbHashedBlob", "pbComputedHash", "pcbComputedHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSignAndEncryptMessage(jitter):
    """"
    [Crypt32.dll] BOOL CryptSignAndEncryptMessage(PCRYPT_SIGN_MESSAGE_PARA pSignPara, PCRYPT_ENCRYPT_MESSAGE_PARA pEncryptPara, DWORD cRecipientCert, PCCERT_CONTEXT [] rgpRecipientCert, const BYTE* pbToBeSignedAndEncrypted, DWORD cbToBeSignedAndEncrypted, BYTE* pbSignedAndEncryptedBlob, DWORD* pcbSignedAndEncryptedBlob)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSignPara", "pEncryptPara", "cRecipientCert", "rgpRecipientCert", "pbToBeSignedAndEncrypted", "cbToBeSignedAndEncrypted", "pbSignedAndEncryptedBlob", "pcbSignedAndEncryptedBlob"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSignMessageWithKey(jitter):
    """"
    [Crypt32.dll] BOOL CryptSignMessageWithKey(PCRYPT_KEY_SIGN_MESSAGE_PARA pSignPara, const BYTE* pbToBeSigned, DWORD cToBeSigned, BYTE* pbSignedBlob, DWORD* pcbSignedBlob)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSignPara", "pbToBeSigned", "cToBeSigned", "pbSignedBlob", "pcbSignedBlob"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSignMessage(jitter):
    """"
    [Crypt32.dll] BOOL CryptSignMessage(PCRYPT_SIGN_MESSAGE_PARA pSignPara, BOOL fDetachedSignature, DWORD cToBeSigned, const BYTE* [] rgpbToBeSigned, DWORD [] rgcbToBeSigned, BYTE* pbSignedBlob, DWORD* pcbSignedBlob)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSignPara", "fDetachedSignature", "cToBeSigned", "rgpbToBeSigned", "rgcbToBeSigned", "pbSignedBlob", "pcbSignedBlob"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptVerifyDetachedMessageHash(jitter):
    """"
    [Crypt32.dll] BOOL CryptVerifyDetachedMessageHash(PCRYPT_HASH_MESSAGE_PARA pHashPara, BYTE* pbDetachedHashBlob, DWORD cbDetachedHashBlob, DWORD cToBeHashed, const BYTE* [] rgpbToBeHashed, DWORD rgcbToBeHashed, BYTE* pbComputedHash, DWORD* pcbComputedHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pHashPara", "pbDetachedHashBlob", "cbDetachedHashBlob", "cToBeHashed", "rgpbToBeHashed", "rgcbToBeHashed", "pbComputedHash", "pcbComputedHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptVerifyDetachedMessageSignature(jitter):
    """"
    [Crypt32.dll] BOOL CryptVerifyDetachedMessageSignature(PCRYPT_VERIFY_MESSAGE_PARA pVerifyPara, DWORD dwSignerIndex, const BYTE* pbDetachedSignBlob, DWORD cbDetachedSignBlob, DWORD cToBeSigned, const BYTE* [] rgpbToBeSigned, DWORD [] rgcbToBeSigned, PCCERT_CONTEXT* ppSignerCert)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pVerifyPara", "dwSignerIndex", "pbDetachedSignBlob", "cbDetachedSignBlob", "cToBeSigned", "rgpbToBeSigned", "rgcbToBeSigned", "ppSignerCert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptVerifyMessageHash(jitter):
    """"
    [Crypt32.dll] BOOL CryptVerifyMessageHash(PCRYPT_HASH_MESSAGE_PARA pHashPara, BYTE* pbHashedBlob, DWORD cbHashedBlob, BYTE* pbToBeHashed, DWORD* pcbToBeHashed, BYTE* pbComputedHash, DWORD* pcbComputedHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pHashPara", "pbHashedBlob", "cbHashedBlob", "pbToBeHashed", "pcbToBeHashed", "pbComputedHash", "pcbComputedHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptVerifyMessageSignature(jitter):
    """"
    [Crypt32.dll] BOOL CryptVerifyMessageSignature(PCRYPT_VERIFY_MESSAGE_PARA pVerifyPara, DWORD dwSignerIndex, const BYTE* pbSignedBlob, DWORD cbSignedBlob, BYTE* pbDecoded, DWORD* pcbDecoded, PCCERT_CONTEXT* ppSignerCert)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pVerifyPara", "dwSignerIndex", "pbSignedBlob", "cbSignedBlob", "pbDecoded", "pcbDecoded", "ppSignerCert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptVerifyMessageSignatureWithKey(jitter):
    """"
    [Crypt32.dll] BOOL CryptVerifyMessageSignatureWithKey(PCRYPT_KEY_VERIFY_MESSAGE_PARA pVerifyPara, PCERT_PUBLIC_KEY_INFO pPublicKeyInfo, const BYTE* pbSignedBlob, DWORD cbSignedBlob, BYTE* pbDecoded, DWORD* pcbDecoded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pVerifyPara", "pPublicKeyInfo", "pbSignedBlob", "cbSignedBlob", "pbDecoded", "pcbDecoded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertCompareCertificate(jitter):
    """"
    [Crypt32.dll] BOOL CertCompareCertificate([CertEncodingType] dwCertEncodingType, PCERT_INFO pCertId1, PCERT_INFO pCertId2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "pCertId1", "pCertId2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertCompareCertificateName(jitter):
    """"
    [Crypt32.dll] BOOL CertCompareCertificateName([CertEncodingType] dwCertEncodingType, PCERT_NAME_BLOB pCertName1, PCERT_NAME_BLOB pCertName2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "pCertName1", "pCertName2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertCompareIntegerBlob(jitter):
    """"
    [Crypt32.dll] BOOL CertCompareIntegerBlob(PCRYPT_INTEGER_BLOB pInt1, PCRYPT_INTEGER_BLOB pInt2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pInt1", "pInt2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertComparePublicKeyInfo(jitter):
    """"
    [Crypt32.dll] BOOL CertComparePublicKeyInfo([CertEncodingType] dwCertEncodingType, PCERT_PUBLIC_KEY_INFO pPublicKey1, PCERT_PUBLIC_KEY_INFO pPublicKey2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "pPublicKey1", "pPublicKey2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFindAttribute(jitter):
    """"
    [Crypt32.dll] PCRYPT_ATTRIBUTE CertFindAttribute(LPCSTR pszObjId, DWORD cAttr, CRYPT_ATTRIBUTE[] rgAttr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszObjId", "cAttr", "rgAttr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFindExtension(jitter):
    """"
    [Crypt32.dll] PCERT_EXTENSION CertFindExtension(LPCSTR pszObjId, DWORD cExtensions, CERT_EXTENSION[] rgExtensions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszObjId", "cExtensions", "rgExtensions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertFindRDNAttr(jitter):
    """"
    [Crypt32.dll] PCERT_RDN_ATTR CertFindRDNAttr(LPCSTR pszObjId, PCERT_NAME_INFO pName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszObjId", "pName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetIntendedKeyUsage(jitter):
    """"
    [Crypt32.dll] BOOL CertGetIntendedKeyUsage([CertEncodingType] dwCertEncodingType, PCERT_INFO pCertInfo, BYTE* pbKeyUsage, DWORD cbKeyUsage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "pCertInfo", "pbKeyUsage", "cbKeyUsage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetPublicKeyLength(jitter):
    """"
    [Crypt32.dll] DWORD CertGetPublicKeyLength([CertEncodingType] dwCertEncodingType, PCERT_PUBLIC_KEY_INFO pPublicKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "pPublicKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertIsRDNAttrsInCertificateName(jitter):
    """"
    [Crypt32.dll] BOOL CertIsRDNAttrsInCertificateName([CertEncodingType] dwCertEncodingType, DWORD dwFlags, PCERT_NAME_BLOB pCertName, PCERT_RDN pRDN)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "dwFlags", "pCertName", "pRDN"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertVerifyCRLRevocation(jitter):
    """"
    [Crypt32.dll] BOOL CertVerifyCRLRevocation([CertEncodingType] dwCertEncodingType, PCERT_INFO pCertId, DWORD cCrlInfo, PCRL_INFO [] rgpCrlInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "pCertId", "cCrlInfo", "rgpCrlInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertVerifyCRLTimeValidity(jitter):
    """"
    [Crypt32.dll] LONG CertVerifyCRLTimeValidity(LPFILETIME pTimeToVerify, PCRL_INFO pCrlInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTimeToVerify", "pCrlInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertVerifyRevocation(jitter):
    """"
    [Crypt32.dll] BOOL CertVerifyRevocation([CertEncodingType] dwEncodingType, DWORD dwRevType, DWORD cContext, PVOID [] rgpvContext, DWORD dwFlags, PCERT_REVOCATION_PARA pRevPara, PCERT_REVOCATION_STATUS pRevStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwEncodingType", "dwRevType", "cContext", "rgpvContext", "dwFlags", "pRevPara", "pRevStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertVerifyTimeValidity(jitter):
    """"
    [Crypt32.dll] LONG CertVerifyTimeValidity(LPFILETIME pTimeToVerify, PCERT_INFO pCertInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTimeToVerify", "pCertInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertVerifyValidityNesting(jitter):
    """"
    [Crypt32.dll] BOOL CertVerifyValidityNesting(PCERT_INFO pSubjectInfo, PCERT_INFO pIssuerInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSubjectInfo", "pIssuerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptExportPKCS8(jitter):
    """"
    [Crypt32.dll] BOOL CryptExportPKCS8(HCRYPTPROV hCryptProv, [CryptKeySpec] dwKeySpec, LPSTR pszPrivateKeyObjId, DWORD dwFlags, void* pvAuxInfo, BYTE* pbPrivateKeyBlob, DWORD* pcbPrivateKeyBlob)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProv", "dwKeySpec", "pszPrivateKeyObjId", "dwFlags", "pvAuxInfo", "pbPrivateKeyBlob", "pcbPrivateKeyBlob"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptExportPKCS8Ex(jitter):
    """"
    [Crypt32.dll] BOOL CryptExportPKCS8Ex(CRYPT_PKCS8_EXPORT_PARAMS* psExportParams, DWORD dwFlags, void* pvAuxInfo, BYTE* pbPrivateKeyBlob, DWORD* pcbPrivateKeyBlob)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psExportParams", "dwFlags", "pvAuxInfo", "pbPrivateKeyBlob", "pcbPrivateKeyBlob"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptExportPublicKeyInfo(jitter):
    """"
    [Crypt32.dll] BOOL CryptExportPublicKeyInfo(HCRYPTPROV_OR_NCRYPT_KEY_HANDLE hCryptProvOrNCryptKey, [CryptKeySpec] dwKeySpec, [CertEncodingType] dwCertEncodingType, PCERT_PUBLIC_KEY_INFO pInfo, DWORD* pcbInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProvOrNCryptKey", "dwKeySpec", "dwCertEncodingType", "pInfo", "pcbInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptExportPublicKeyInfoEx(jitter):
    """"
    [Crypt32.dll] BOOL CryptExportPublicKeyInfoEx(HCRYPTPROV_OR_NCRYPT_KEY_HANDLE hCryptProvOrNCryptKey, [CryptKeySpec] dwKeySpec, [CertEncodingType] dwCertEncodingType, LPSTR pszPublicKeyObjId, DWORD dwFlags, void* pvAuxInfo, PCERT_PUBLIC_KEY_INFO pInfo, DWORD* pcbInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProvOrNCryptKey", "dwKeySpec", "dwCertEncodingType", "pszPublicKeyObjId", "dwFlags", "pvAuxInfo", "pInfo", "pcbInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptExportPublicKeyInfoFromBCryptKeyHandle(jitter):
    """"
    [Crypt32.dll] BOOL CryptExportPublicKeyInfoFromBCryptKeyHandle(BCRYPT_KEY_HANDLE hBCryptKey, [CertEncodingType] dwCertEncodingType, LPSTR pszPublicKeyObjId, DWORD dwFlags, void* pvAuxInfo, PCERT_PUBLIC_KEY_INFO pInfo, DWORD pcbInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hBCryptKey", "dwCertEncodingType", "pszPublicKeyObjId", "dwFlags", "pvAuxInfo", "pInfo", "pcbInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptFindCertificateKeyProvInfo(jitter):
    """"
    [Crypt32.dll] BOOL CryptFindCertificateKeyProvInfo(PCCERT_CONTEXT pCert, DWORD dwFlags, void* pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCert", "dwFlags", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptFindLocalizedName(jitter):
    """"
    [Crypt32.dll] LPCWSTR CryptFindLocalizedName(LPCWSTR pwszCryptName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszCryptName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptHashCertificate(jitter):
    """"
    [Crypt32.dll] BOOL CryptHashCertificate(HCRYPTPROV_LEGACY hCryptProv, ALG_ID Algid, DWORD dwFlags, const BYTE* pbEncoded, DWORD cbEncoded, BYTE* pbComputedHash, DWORD* pcbComputedHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProv", "Algid", "dwFlags", "pbEncoded", "cbEncoded", "pbComputedHash", "pcbComputedHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptHashCertificate2(jitter):
    """"
    [Crypt32.dll] BOOL CryptHashCertificate2(LPCWSTR pwszCNGHashAlgid, DWORD dwFlags, void* pvReserved, BYTE* pbEncoded, DWORD cbEncoded, BYTE* pbComputedHash, DWORD* pcbComputedHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszCNGHashAlgid", "dwFlags", "pvReserved", "pbEncoded", "cbEncoded", "pbComputedHash", "pcbComputedHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptHashPublicKeyInfo(jitter):
    """"
    [Crypt32.dll] BOOL CryptHashPublicKeyInfo(HCRYPTPROV_LEGACY hCryptProv, ALG_ID Algid, DWORD dwFlags, [CertEncodingType] dwCertEncodingType, PCERT_PUBLIC_KEY_INFO pInfo, BYTE* pbComputedHash, DWORD* pcbComputedHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProv", "Algid", "dwFlags", "dwCertEncodingType", "pInfo", "pbComputedHash", "pcbComputedHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptHashToBeSigned(jitter):
    """"
    [Crypt32.dll] BOOL CryptHashToBeSigned(HCRYPTPROV_LEGACY hCryptProv, [CertEncodingType] dwCertEncodingType, const BYTE* pbEncoded, DWORD cbEncoded, BYTE* pbComputedHash, DWORD* pcbComputedHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProv", "dwCertEncodingType", "pbEncoded", "cbEncoded", "pbComputedHash", "pcbComputedHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptImportPKCS8(jitter):
    """"
    [Crypt32.dll] BOOL CryptImportPKCS8(CRYPT_PKCS8_IMPORT_PARAMS sPrivateKeyAndParams, DWORD dwFlags, HCRYPTPROV* phCryptProv, void* pvAuxInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sPrivateKeyAndParams", "dwFlags", "phCryptProv", "pvAuxInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptImportPublicKeyInfo(jitter):
    """"
    [Crypt32.dll] BOOL CryptImportPublicKeyInfo(HCRYPTPROV hCryptProv, [CertEncodingType] dwCertEncodingType, PCERT_PUBLIC_KEY_INFO pInfo, HCRYPTKEY* phKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProv", "dwCertEncodingType", "pInfo", "phKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptImportPublicKeyInfoEx(jitter):
    """"
    [Crypt32.dll] BOOL CryptImportPublicKeyInfoEx(HCRYPTPROV hCryptProv, [CertEncodingType] dwCertEncodingType, PCERT_PUBLIC_KEY_INFO pInfo, ALG_ID aiKeyAlg, DWORD dwFlags, void* pvAuxInfo, HCRYPTKEY* phKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProv", "dwCertEncodingType", "pInfo", "aiKeyAlg", "dwFlags", "pvAuxInfo", "phKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptImportPublicKeyInfoEx2(jitter):
    """"
    [Crypt32.dll] BOOL CryptImportPublicKeyInfoEx2([CertEncodingType] dwCertEncodingType, PCERT_PUBLIC_KEY_INFO pInfo, DWORD dwFlags, void* pvAuxInfo, BCRYPT_KEY_HANDLE* phKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "pInfo", "dwFlags", "pvAuxInfo", "phKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMemAlloc(jitter):
    """"
    [Crypt32.dll] LPVOID CryptMemAlloc(ULONG cbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMemFree(jitter):
    """"
    [Crypt32.dll] void CryptMemFree(LPVOID pv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptMemRealloc(jitter):
    """"
    [Crypt32.dll] LPVOID CryptMemRealloc(LPVOID pv, ULONG cbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pv", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptQueryObject(jitter):
    """"
    [Crypt32.dll] BOOL CryptQueryObject([CryptObjectType] dwObjectType, const void* pvObject, [CryptExpectedContentType] dwExpectedContentTypeFlags, [CryptExpectedFormatType] dwExpectedFormatTypeFlags, DWORD dwFlags, [CertEncodingType*] pdwMsgAndCertEncodingType, [CryptContentType*] pdwContentType, [CryptFormatType*] pdwFormatType, HCERTSTORE* phCertStore, HCRYPTMSG* phMsg, const void** ppvContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwObjectType", "pvObject", "dwExpectedContentTypeFlags", "dwExpectedFormatTypeFlags", "dwFlags", "pdwMsgAndCertEncodingType", "pdwContentType", "pdwFormatType", "phCertStore", "phMsg", "ppvContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSignAndEncodeCertificate(jitter):
    """"
    [Crypt32.dll] BOOL CryptSignAndEncodeCertificate(HCRYPTPROV_OR_NCRYPT_KEY_HANDLE hCryptProvOrNCryptKey, [CryptKeySpec] dwKeySpec, [CertEncodingType] dwCertEncodingType, LPCSTR lpszStructType, const void* pvStructInfo, PCRYPT_ALGORITHM_IDENTIFIER pSignatureAlgorithm, const void* pvHashAuxInfo, PBYTE pbEncoded, DWORD* pcbEncoded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProvOrNCryptKey", "dwKeySpec", "dwCertEncodingType", "lpszStructType", "pvStructInfo", "pSignatureAlgorithm", "pvHashAuxInfo", "pbEncoded", "pcbEncoded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSignCertificate(jitter):
    """"
    [Crypt32.dll] BOOL CryptSignCertificate(HCRYPTPROV_OR_NCRYPT_KEY_HANDLE hCryptProvOrNCryptKey, [CryptKeySpec] dwKeySpec, [CertEncodingType] dwCertEncodingType, const BYTE* pbEncodedToBeSigned, DWORD cbEncodedToBeSigned, PCRYPT_ALGORITHM_IDENTIFIER pSignatureAlgorithm, const void* pvHashAuxInfo, BYTE* pbSignature, DWORD* pcbSignature)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProvOrNCryptKey", "dwKeySpec", "dwCertEncodingType", "pbEncodedToBeSigned", "cbEncodedToBeSigned", "pSignatureAlgorithm", "pvHashAuxInfo", "pbSignature", "pcbSignature"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSIPAddProvider(jitter):
    """"
    [Crypt32.dll] BOOL CryptSIPAddProvider(SIP_ADD_NEWPROVIDER* psNewProv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psNewProv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSIPCreateIndirectData(jitter):
    """"
    [Crypt32.dll] BOOL CryptSIPCreateIndirectData(SIP_SUBJECTINFO* pSubjectInfo, DWORD* pcbIndirectData, SIP_INDIRECT_DATA* pIndirectData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSubjectInfo", "pcbIndirectData", "pIndirectData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSIPGetSignedDataMsg(jitter):
    """"
    [Crypt32.dll] BOOL CryptSIPGetSignedDataMsg(SIP_SUBJECTINFO* pSubjectInfo, [CertEncodingType*] pdwEncodingType, DWORD dwIndex, DWORD* pcbSignedDataMsg, BYTE* pbSignedDataMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSubjectInfo", "pdwEncodingType", "dwIndex", "pcbSignedDataMsg", "pbSignedDataMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSIPLoad(jitter):
    """"
    [Crypt32.dll] BOOL CryptSIPLoad(const GUID* pgSubject, DWORD dwFlags, SIP_DISPATCH_INFO* pSipDispatch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pgSubject", "dwFlags", "pSipDispatch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSIPPutSignedDataMsg(jitter):
    """"
    [Crypt32.dll] BOOL CryptSIPPutSignedDataMsg(SIP_SUBJECTINFO* pSubjectInfo, [CertEncodingType*] pdwEncodingType, DWORD dwIndex, DWORD* pcbSignedDataMsg, BYTE* pbSignedDataMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSubjectInfo", "pdwEncodingType", "dwIndex", "pcbSignedDataMsg", "pbSignedDataMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSIPRemoveProvider(jitter):
    """"
    [Crypt32.dll] BOOL CryptSIPRemoveProvider(GUID* pgProv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pgProv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSIPRemoveSignedDataMsg(jitter):
    """"
    [Crypt32.dll] BOOL CryptSIPRemoveSignedDataMsg(SIP_SUBJECTINFO* pSubjectInfo, DWORD dwIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSubjectInfo", "dwIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSIPRetrieveSubjectGuid(jitter):
    """"
    [Crypt32.dll] BOOL CryptSIPRetrieveSubjectGuid(LPCWSTR FileName, HANDLE hFileIn, GUID* pgSubject)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileName", "hFileIn", "pgSubject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSIPRetrieveSubjectGuidForCatalogFile(jitter):
    """"
    [Crypt32.dll] BOOL CryptSIPRetrieveSubjectGuidForCatalogFile(LPCWSTR FileName, HANDLE hFileIn, GUID* pgSubject)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileName", "hFileIn", "pgSubject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSIPVerifyIndirectData(jitter):
    """"
    [Crypt32.dll] BOOL CryptSIPVerifyIndirectData(SIP_SUBJECTINFO* pSubjectInfo, SIP_INDIRECT_DATA* pIndirectData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSubjectInfo", "pIndirectData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptUpdateProtectedState(jitter):
    """"
    [Crypt32.dll] BOOL CryptUpdateProtectedState(PSID pOldSid, LPCWSTR pwszOldPassword, DWORD dwFlags, DWORD* pdwSuccessCount, DWORD* pdwFailureCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pOldSid", "pwszOldPassword", "dwFlags", "pdwSuccessCount", "pdwFailureCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptVerifyCertificateSignature(jitter):
    """"
    [Crypt32.dll] BOOL CryptVerifyCertificateSignature(HCRYPTPROV_LEGACY hCryptProv, [CertEncodingType] dwCertEncodingType, BYTE* pbEncoded, DWORD cbEncoded, PCERT_PUBLIC_KEY_INFO pPublicKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProv", "dwCertEncodingType", "pbEncoded", "cbEncoded", "pPublicKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptVerifyCertificateSignatureEx(jitter):
    """"
    [Crypt32.dll] BOOL CryptVerifyCertificateSignatureEx(HCRYPTPROV_LEGACY hCryptProv, [CertEncodingType] dwCertEncodingType, [CryptSubjectType] dwSubjectType, void* pvSubject, [CryptIssuerType] dwIssuerType, void* pvIssuer, DWORD dwFlags, void* pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCryptProv", "dwCertEncodingType", "dwSubjectType", "pvSubject", "dwIssuerType", "pvIssuer", "dwFlags", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertIsStrongHashToSign(jitter):
    """"
    [Crypt32.dll] BOOL CertIsStrongHashToSign(PCCERT_STRONG_SIGN_PARA pStrongSignPara, LPCWSTR pwszCNGHashAlgid, PCCERT_CONTEXT pSigningCert)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStrongSignPara", "pwszCNGHashAlgid", "pSigningCert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSIPGetCaps(jitter):
    """"
    [Crypt32.dll] BOOL CryptSIPGetCaps(SIP_SUBJECTINFO* pSubjInfo, SIP_CAP_SET* pCaps)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSubjInfo", "pCaps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertAlgIdToOID(jitter):
    """"
    [Crypt32.dll] LPCSTR CertAlgIdToOID(DWORD dwAlgId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwAlgId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetNameString(jitter, get_str, set_str):
    """"
    [Crypt32.dll] DWORD CertGetNameString(PCCERT_CONTEXT pCertContext, [CertNameType] dwType, [CertNameFlags] dwFlags, void* pvTypePara, LPTSTR pszNameString, DWORD cchNameString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext", "dwType", "dwFlags", "pvTypePara", "pszNameString", "cchNameString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetNameStringA(jitter):
    crypt32_CertGetNameString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def crypt32_CertGetNameStringW(jitter):
    crypt32_CertGetNameString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def crypt32_CertNameToStr(jitter, get_str, set_str):
    """"
    [Crypt32.dll] DWORD CertNameToStr([CertEncodingType] dwCertEncodingType, PCERT_NAME_BLOB pName, [CertStrType] dwStrType, LPTSTR psz, DWORD csz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "pName", "dwStrType", "psz", "csz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertNameToStrA(jitter):
    crypt32_CertNameToStr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def crypt32_CertNameToStrW(jitter):
    crypt32_CertNameToStr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def crypt32_CertOIDToAlgId(jitter):
    """"
    [Crypt32.dll] DWORD CertOIDToAlgId(LPCSTR pszObjId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszObjId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertRDNValueToStr(jitter, get_str, set_str):
    """"
    [Crypt32.dll] DWORD CertRDNValueToStr(DWORD dwValueType, PCERT_RDN_VALUE_BLOB pValue, LPTSTR psz, DWORD csz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwValueType", "pValue", "psz", "csz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertRDNValueToStrA(jitter):
    crypt32_CertRDNValueToStr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def crypt32_CertRDNValueToStrW(jitter):
    crypt32_CertRDNValueToStr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def crypt32_CertStrToName(jitter, get_str, set_str):
    """"
    [Crypt32.dll] BOOL CertStrToName([CertEncodingType] dwCertEncodingType, LPCTSTR pszX500, [CertStrType] dwStrType, void* pvReserved, BYTE* pbEncoded, DWORD* pcbEncoded, LPCTSTR* ppszError)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "pszX500", "dwStrType", "pvReserved", "pbEncoded", "pcbEncoded", "ppszError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertStrToNameA(jitter):
    crypt32_CertStrToName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def crypt32_CertStrToNameW(jitter):
    crypt32_CertStrToName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def crypt32_CryptBinaryToString(jitter, get_str, set_str):
    """"
    [Crypt32.dll] BOOL CryptBinaryToString(const BYTE* pbBinary, DWORD cbBinary, [CryptStringFlags] dwFlags, LPTSTR pszString, DWORD* pcchString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pbBinary", "cbBinary", "dwFlags", "pszString", "pcchString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptBinaryToStringA(jitter):
    crypt32_CryptBinaryToString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def crypt32_CryptBinaryToStringW(jitter):
    crypt32_CryptBinaryToString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def crypt32_CryptFormatObject(jitter):
    """"
    [Crypt32.dll] BOOL CryptFormatObject([CertEncodingType] dwCertEncodingType, DWORD dwFormatType, [CryptFormatStrType] dwFormatStrType, void* pFormatStruct, LPCSTR lpszStructType, const BYTE* pbEncoded, DWORD cbEncoded, void* pbFormat, DWORD* pcbFormat)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "dwFormatType", "dwFormatStrType", "pFormatStruct", "lpszStructType", "pbEncoded", "cbEncoded", "pbFormat", "pcbFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptStringToBinary(jitter, get_str, set_str):
    """"
    [Crypt32.dll] BOOL CryptStringToBinary(LPCTSTR pszString, DWORD cchString, [CryptStringFlags] dwFlags, BYTE* pbBinary, DWORD* pcbBinary, DWORD* pdwSkip, [CryptStringFlags*] pdwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszString", "cchString", "dwFlags", "pbBinary", "pcbBinary", "pdwSkip", "pdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptStringToBinaryA(jitter):
    crypt32_CryptStringToBinary(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def crypt32_CryptStringToBinaryW(jitter):
    crypt32_CryptStringToBinary(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def crypt32_CertAddEnhancedKeyUsageIdentifier(jitter):
    """"
    [Crypt32.dll] BOOL CertAddEnhancedKeyUsageIdentifier(PCCERT_CONTEXT pCertContext, LPCSTR pszUsageIdentifier)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext", "pszUsageIdentifier"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertGetEnhancedKeyUsage(jitter):
    """"
    [Crypt32.dll] BOOL CertGetEnhancedKeyUsage(PCCERT_CONTEXT pCertContext, [CertFindFlags] dwFlags, PCERT_ENHKEY_USAGE pUsage, DWORD* pcbUsage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext", "dwFlags", "pUsage", "pcbUsage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertRemoveEnhancedKeyUsageIdentifier(jitter):
    """"
    [Crypt32.dll] BOOL CertRemoveEnhancedKeyUsageIdentifier(PCCERT_CONTEXT pCertContext, LPCSTR pszUsageIdentifier)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext", "pszUsageIdentifier"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CertSetEnhancedKeyUsage(jitter):
    """"
    [Crypt32.dll] BOOL CertSetEnhancedKeyUsage(PCCERT_CONTEXT pCertContext, PCERT_ENHKEY_USAGE pUsage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertContext", "pUsage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptCreateKeyIdentifierFromCSP(jitter):
    """"
    [Crypt32.dll] BOOL CryptCreateKeyIdentifierFromCSP([CertEncodingType] dwCertEncodingType, LPCSTR pszPubKeyOID, const PUBLICKEYSTRUC* pPubKeyStruc, DWORD cbPubKeyStruc, DWORD dwFlags, void* pvReserved, BYTE* pbHash, DWORD* pcbHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCertEncodingType", "pszPubKeyOID", "pPubKeyStruc", "cbPubKeyStruc", "dwFlags", "pvReserved", "pbHash", "pcbHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptEnumKeyIdentifierProperties(jitter):
    """"
    [Crypt32.dll] BOOL CryptEnumKeyIdentifierProperties(const CRYPT_HASH_BLOB* pKeyIdentifier, DWORD dwPropId, DWORD dwFlags, LPCWSTR pwszComputerName, void* pvReserved, void* pvArg, PFN_CRYPT_ENUM_KEYID_PROP pfnEnum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pKeyIdentifier", "dwPropId", "dwFlags", "pwszComputerName", "pvReserved", "pvArg", "pfnEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptGetKeyIdentifierProperty(jitter):
    """"
    [Crypt32.dll] BOOL CryptGetKeyIdentifierProperty(const CRYPT_HASH_BLOB* pKeyIdentifier, DWORD dwPropId, DWORD dwFlags, LPCWSTR pwszComputerName, void* pvReserved, void* pvData, DWORD* pcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pKeyIdentifier", "dwPropId", "dwFlags", "pwszComputerName", "pvReserved", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSetKeyIdentifierProperty(jitter):
    """"
    [Crypt32.dll] BOOL CryptSetKeyIdentifierProperty(const CRYPT_HASH_BLOB* pKeyIdentifier, DWORD dwPropId, DWORD dwFlags, LPCWSTR pwszComputerName, void* pvReserved, const void* pvData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pKeyIdentifier", "dwPropId", "dwFlags", "pwszComputerName", "pvReserved", "pvData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptEnumOIDFunction(jitter):
    """"
    [Crypt32.dll] BOOL CryptEnumOIDFunction([CertEncodingType] dwEncodingType, LPCSTR pszFuncName, LPCSTR pszOID, DWORD dwFlags, void* pvArg, PFN_CRYPT_ENUM_OID_FUNC pfnEnumOIDFunc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwEncodingType", "pszFuncName", "pszOID", "dwFlags", "pvArg", "pfnEnumOIDFunc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptEnumOIDInfo(jitter):
    """"
    [Crypt32.dll] BOOL CryptEnumOIDInfo([CryptGroupId] dwGroupId, DWORD dwFlags, void* pvArg, PFN_CRYPT_ENUM_OID_INFO pfnEnumOIDInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwGroupId", "dwFlags", "pvArg", "pfnEnumOIDInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptFindOIDInfo(jitter):
    """"
    [Crypt32.dll] PCCRYPT_OID_INFO CryptFindOIDInfo([CryptFindOidInfoKeyType] dwKeyType, void* pvKey, [CryptFindOidInfoGroudId] dwGroupId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwKeyType", "pvKey", "dwGroupId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptFreeOIDFunctionAddress(jitter):
    """"
    [Crypt32.dll] BOOL CryptFreeOIDFunctionAddress(HCRYPTOIDFUNCADDR hFuncAddr, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFuncAddr", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptGetOIDFunctionAddress(jitter):
    """"
    [Crypt32.dll] BOOL CryptGetOIDFunctionAddress(HCRYPTOIDFUNCSET hFuncSet, [CertEncodingType] dwEncodingType, LPCSTR pszOID, DWORD dwFlags, void** ppvFuncAddr, HCRYPTOIDFUNCADDR* phFuncAddr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFuncSet", "dwEncodingType", "pszOID", "dwFlags", "ppvFuncAddr", "phFuncAddr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptGetDefaultOIDFunctionAddress(jitter):
    """"
    [Crypt32.dll] BOOL CryptGetDefaultOIDFunctionAddress(HCRYPTOIDFUNCSET hFuncSet, [CertEncodingType] dwEncodingType, LPCWSTR pwszDll, DWORD dwFlags, void** ppvFuncAddr, HCRYPTOIDFUNCADDR* phFuncAddr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFuncSet", "dwEncodingType", "pwszDll", "dwFlags", "ppvFuncAddr", "phFuncAddr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptGetDefaultOIDDllList(jitter):
    """"
    [Crypt32.dll] BOOL CryptGetDefaultOIDDllList(HCRYPTOIDFUNCSET hFuncSet, [CertEncodingType] dwEncodingType, LPWSTR pwszDllList, DWORD* pcchDllList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFuncSet", "dwEncodingType", "pwszDllList", "pcchDllList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptGetOIDFunctionValue(jitter):
    """"
    [Crypt32.dll] BOOL CryptGetOIDFunctionValue([CertEncodingType] dwEncodingType, LPCSTR pszFuncName, LPCSTR pszOID, LPCWSTR pwszValueName, DWORD* pdwValueType, BYTE* pbValueData, DWORD* pcbValueData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwEncodingType", "pszFuncName", "pszOID", "pwszValueName", "pdwValueType", "pbValueData", "pcbValueData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptInitOIDFunctionSet(jitter):
    """"
    [Crypt32.dll] HCRYPTOIDFUNCSET CryptInitOIDFunctionSet(LPCSTR pszFuncName, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszFuncName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptInstallOIDFunctionAddress(jitter):
    """"
    [Crypt32.dll] BOOL CryptInstallOIDFunctionAddress(HMODULE hModule, [CertEncodingType] dwEncodingType, LPCSTR pszFuncName, DWORD cFuncEntry, CRYPT_OID_FUNC_ENTRY[] rgFuncEntry, [CryptInstallOIDFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "dwEncodingType", "pszFuncName", "cFuncEntry", "rgFuncEntry", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptRegisterDefaultOIDFunction(jitter):
    """"
    [Crypt32.dll] BOOL CryptRegisterDefaultOIDFunction([CertEncodingType] dwEncodingType, LPCSTR pszFuncName, DWORD dwIndex, LPCWSTR pwszDll)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwEncodingType", "pszFuncName", "dwIndex", "pwszDll"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptRegisterOIDFunction(jitter):
    """"
    [Crypt32.dll] BOOL CryptRegisterOIDFunction([CertEncodingType] dwEncodingType, LPCSTR pszFuncName, LPCSTR pszOID, LPCWSTR pwszDll, LPCSTR pszOverrideFuncName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwEncodingType", "pszFuncName", "pszOID", "pwszDll", "pszOverrideFuncName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptRegisterOIDInfo(jitter):
    """"
    [Crypt32.dll] BOOL CryptRegisterOIDInfo(PCCRYPT_OID_INFO pInfo, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pInfo", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptSetOIDFunctionValue(jitter):
    """"
    [Crypt32.dll] BOOL CryptSetOIDFunctionValue([CertEncodingType] dwEncodingType, LPCSTR pszFuncName, LPCSTR pszOID, LPCWSTR pwszValueName, DWORD dwValueType, const BYTE* pbValueData, DWORD cbValueData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwEncodingType", "pszFuncName", "pszOID", "pwszValueName", "dwValueType", "pbValueData", "cbValueData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptUnregisterDefaultOIDFunction(jitter):
    """"
    [Crypt32.dll] BOOL CryptUnregisterDefaultOIDFunction([CertEncodingType] dwEncodingType, LPCSTR pszFuncName, LPCWSTR pwszDll)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwEncodingType", "pszFuncName", "pwszDll"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptUnregisterOIDFunction(jitter):
    """"
    [Crypt32.dll] BOOL CryptUnregisterOIDFunction([CertEncodingType] dwEncodingType, LPCSTR pszFuncName, LPCSTR pszOID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwEncodingType", "pszFuncName", "pszOID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_CryptUnregisterOIDInfo(jitter):
    """"
    [Crypt32.dll] BOOL CryptUnregisterOIDInfo(PCCRYPT_OID_INFO pInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_PFXExportCertStore(jitter):
    """"
    [Crypt32.dll] BOOL PFXExportCertStore(HCERTSTORE hStore, CRYPT_DATA_BLOB* pPFX, LPCWSTR szPassword, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hStore", "pPFX", "szPassword", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_PFXExportCertStoreEx(jitter):
    """"
    [Crypt32.dll] BOOL PFXExportCertStoreEx(HCERTSTORE hStore, CRYPT_DATA_BLOB* pPFX, LPCWSTR szPassword, void* pvReserved, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hStore", "pPFX", "szPassword", "pvReserved", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_PFXImportCertStore(jitter):
    """"
    [Crypt32.dll] HCERTSTORE PFXImportCertStore(CRYPT_DATA_BLOB* pPFX, LPCWSTR szPassword, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPFX", "szPassword", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_PFXIsPFXBlob(jitter):
    """"
    [Crypt32.dll] BOOL PFXIsPFXBlob(CRYPT_DATA_BLOB* pPFX)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPFX"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def crypt32_PFXVerifyPassword(jitter):
    """"
    [Crypt32.dll] BOOL PFXVerifyPassword(CRYPT_DATA_BLOB* pPFX, LPCWSTR szPassword, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPFX", "szPassword", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
