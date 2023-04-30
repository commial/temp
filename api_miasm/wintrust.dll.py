
def wintrust_OpenPersonalTrustDBDialog(jitter):
    """
    BOOL OpenPersonalTrustDBDialog(
        HWND hwndParent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_OpenPersonalTrustDBDialogEx(jitter):
    """
    BOOL OpenPersonalTrustDBDialogEx(
        HWND hwndParent,
        DWORD dwFlags,
        PVOID* pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "dwFlags", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATCDFClose(jitter):
    """
    BOOL CryptCATCDFClose(
        CRYPTCATCDF* pCDF
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCDF"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATCDFEnumAttributesWithCDFTag(jitter):
    """
    CRYPTCATATTRIBUTE* CryptCATCDFEnumAttributesWithCDFTag(
        CRYPTCATCDF* pCDF,
        LPWSTR pwszMemberTag,
        CRYPTCATMEMBER* pMember,
        CRYPTCATATTRIBUTE* pPrevAttr,
        PFN_CDF_PARSE_ERROR_CALLBACK pfnParseError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCDF", "pwszMemberTag", "pMember", "pPrevAttr", "pfnParseError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATCDFEnumCatAttributes(jitter):
    """
    CRYPTCATATTRIBUTE* CryptCATCDFEnumCatAttributes(
        CRYPTCATCDF* pCDF,
        CRYPTCATATTRIBUTE* pPrevAttr,
        PFN_CDF_PARSE_ERROR_CALLBACK pfnParseError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCDF", "pPrevAttr", "pfnParseError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATCDFEnumMembersByCDFTagEx(jitter):
    """
    LPWSTR CryptCATCDFEnumMembersByCDFTagEx(
        CRYPTCATCDF* pCDF,
        LPWSTR pwszPrevCDFTag,
        PFN_CDF_PARSE_ERROR_CALLBACK pfnParseError,
        CRYPTCATMEMBER** ppMember,
        BOOL fContinueOnError,
        LPVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCDF", "pwszPrevCDFTag", "pfnParseError", "ppMember", "fContinueOnError", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATCDFOpen(jitter):
    """
    CRYPTCATCDF* CryptCATCDFOpen(
        LPWSTR pwszFilePath,
        PFN_CDF_PARSE_ERROR_CALLBACK pfnParseError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszFilePath", "pfnParseError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATAdminAcquireContext(jitter):
    """
    BOOL CryptCATAdminAcquireContext(
        HCATADMIN* phCatAdmin,
        const GUID* pgSubsystem,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phCatAdmin", "pgSubsystem", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATAdminAddCatalog(jitter):
    """
    HCATINFO CryptCATAdminAddCatalog(
        HCATADMIN hCatAdmin,
        WCHAR* pwszCatalogFile,
        WCHAR* pwszSelectBaseName,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatAdmin", "pwszCatalogFile", "pwszSelectBaseName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATAdminEnumCatalogFromHash(jitter):
    """
    HCATINFO CryptCATAdminEnumCatalogFromHash(
        HCATADMIN hCatAdmin,
        BYTE* pbHash,
        DWORD cbHash,
        DWORD dwFlags,
        HCATINFO* phPrevCatInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatAdmin", "pbHash", "cbHash", "dwFlags", "phPrevCatInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATAdminRemoveCatalog(jitter):
    """
    BOOL CryptCATAdminRemoveCatalog(
        HCATADMIN hCatAdmin,
        LPCWSTR pwszCatalogFile,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatAdmin", "pwszCatalogFile", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATAdminCalcHashFromFileHandle(jitter):
    """
    BOOL CryptCATAdminCalcHashFromFileHandle(
        HANDLE hFile,
        DWORD* pcbHash,
        BYTE* pbHash,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "pcbHash", "pbHash", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATAdminReleaseCatalogContext(jitter):
    """
    BOOL CryptCATAdminReleaseCatalogContext(
        HCATADMIN hCatAdmin,
        HCATINFO hCatInfo,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatAdmin", "hCatInfo", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATAdminReleaseContext(jitter):
    """
    BOOL CryptCATAdminReleaseContext(
        HCATADMIN hCatAdmin,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatAdmin", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATAdminResolveCatalogPath(jitter):
    """
    BOOL CryptCATAdminResolveCatalogPath(
        HCATADMIN hCatAdmin,
        WCHAR* pwszCatalogFile,
        CATALOG_INFO* psCatInfo,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatAdmin", "pwszCatalogFile", "psCatInfo", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATCatalogInfoFromContext(jitter):
    """
    BOOL CryptCATCatalogInfoFromContext(
        HCATINFO hCatInfo,
        CATALOG_INFO* psCatInfo,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatInfo", "psCatInfo", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATClose(jitter):
    """
    BOOL CryptCATClose(
        HANDLE hCatalog
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatalog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATOpen(jitter):
    """
    HANDLE CryptCATOpen(
        LPWSTR pwszFileName,
        DWORD fdwOpenFlags,
        HCRYPTPROV hProv,
        DWORD dwPublicVersion,
        DWORD dwEncodingType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszFileName", "fdwOpenFlags", "hProv", "dwPublicVersion", "dwEncodingType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATEnumerateAttr(jitter):
    """
    CRYPTCATATTRIBUTE* CryptCATEnumerateAttr(
        HANDLE hCatalog,
        CRYPTCATMEMBER* pCatMember,
        CRYPTCATATTRIBUTE* pPrevAttr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatalog", "pCatMember", "pPrevAttr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATEnumerateCatAttr(jitter):
    """
    CRYPTCATATTRIBUTE* CryptCATEnumerateCatAttr(
        HANDLE hCatalog,
        CRYPTCATATTRIBUTE* pPrevAttr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatalog", "pPrevAttr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATEnumerateMember(jitter):
    """
    CRYPTCATMEMBER* CryptCATEnumerateMember(
        HANDLE hCatalog,
        CRYPTCATMEMBER* pPrevMember
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatalog", "pPrevMember"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATGetAttrInfo(jitter):
    """
    CRYPTCATATTRIBUTE* CryptCATGetAttrInfo(
        HANDLE hCatalog,
        CRYPTCATMEMBER* pCatMember,
        LPWSTR pwszReferenceTag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatalog", "pCatMember", "pwszReferenceTag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATGetMemberInfo(jitter):
    """
    CRYPTCATMEMBER* CryptCATGetMemberInfo(
        HANDLE hCatalog,
        LPWSTR pwszReferenceTag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatalog", "pwszReferenceTag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_IsCatalogFile(jitter):
    """
    BOOL IsCatalogFile(
        HANDLE hFile,
        WCHAR* pwszFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "pwszFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATAdminAcquireContext2(jitter):
    """
    BOOL CryptCATAdminAcquireContext2(
        HCATADMIN* phCatAdmin,
        const GUID* pgSubsystem,
        PCWSTR pwszHashAlgorithm,
        PCCERT_STRONG_SIGN_PARA pStrongHashPolicy,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phCatAdmin", "pgSubsystem", "pwszHashAlgorithm", "pStrongHashPolicy", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_CryptCATAdminCalcHashFromFileHandle2(jitter):
    """
    BOOL CryptCATAdminCalcHashFromFileHandle2(
        HCATADMIN hCatAdmin,
        HANDLE hFile,
        DWORD* pcbHash,
        BYTE* pbHash,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCatAdmin", "hFile", "pcbHash", "pbHash", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WintrustAddActionID(jitter):
    """
    BOOL WintrustAddActionID(
        GUID* pgActionID,
        DWORD fdwFlags,
        CRYPT_REGISTER_ACTIONID* psProvInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pgActionID", "fdwFlags", "psProvInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WintrustGetRegPolicyFlags(jitter):
    """
    void WintrustGetRegPolicyFlags(
        [WintrustPolicyFlags*] pdwPolicyFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwPolicyFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WintrustLoadFunctionPointers(jitter):
    """
    BOOL WintrustLoadFunctionPointers(
        GUID* pgActionID,
        CRYPT_PROVIDER_FUNCTIONS* pPfns
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pgActionID", "pPfns"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WintrustRemoveActionID(jitter):
    """
    BOOL WintrustRemoveActionID(
        GUID* pgActionID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pgActionID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WintrustSetDefaultIncludePEPageHashes(jitter):
    """
    void WintrustSetDefaultIncludePEPageHashes(
        BOOL fIncludePEPageHashes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fIncludePEPageHashes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WintrustSetRegPolicyFlags(jitter):
    """
    BOOL WintrustSetRegPolicyFlags(
        [WintrustPolicyFlags] dwPolicyFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwPolicyFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WinVerifyTrust(jitter):
    """
    HRESULT WinVerifyTrust(
        HWND hWnd,
        GUID* pgActionID,
        LPVOID pWVTData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pgActionID", "pWVTData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WinVerifyTrustEx(jitter):
    """
    HRESULT WinVerifyTrustEx(
        HWND hwnd,
        GUID* pgActionID,
        WINTRUST_DATA* pWinTrustData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pgActionID", "pWinTrustData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WTHelperCertCheckValidSignature(jitter):
    """
    HRESULT WTHelperCertCheckValidSignature(
        CRYPT_PROVIDER_DATA* pProvData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProvData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WTHelperCertFindIssuerCertificate(jitter):
    """
    PCCERT_CONTEXT WTHelperCertFindIssuerCertificate(
        PCCERT_CONTEXT pChildContext,
        DWORD chStores,
        HCERTSTORE* pahStores,
        FILETIME* psftVerifyAsOf,
        DWORD dwEncoding,
        DWORD* pdwConfidence,
        DWORD* dwError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pChildContext", "chStores", "pahStores", "psftVerifyAsOf", "dwEncoding", "pdwConfidence", "dwError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WTHelperCertIsSelfSigned(jitter):
    """
    BOOL WTHelperCertIsSelfSigned(
        DWORD dwEncoding,
        CERT_INFO* pCert
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwEncoding", "pCert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WTHelperGetFileHash(jitter):
    """
    LONG WTHelperGetFileHash(
        LPCWSTR pwszFilename,
        DWORD dwFlags,
        PVOID pvReserved,
        BYTE* pbFileHash,
        DWORD* pcbFileHash,
        ALG_ID* pHashAlgid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszFilename", "dwFlags", "pvReserved", "pbFileHash", "pcbFileHash", "pHashAlgid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WTHelperGetProvCertFromChain(jitter):
    """
    CRYPT_PROVIDER_CERT* WTHelperGetProvCertFromChain(
        CRYPT_PROVIDER_SGNR* pSgnr,
        DWORD idxCert
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSgnr", "idxCert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WTHelperGetProvPrivateDataFromChain(jitter):
    """
    CRYPT_PROVIDER_PRIVDATA* WTHelperGetProvPrivateDataFromChain(
        CRYPT_PROVIDER_DATA* pProvData,
        GUID* pgProviderID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProvData", "pgProviderID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WTHelperGetProvSignerFromChain(jitter):
    """
    CRYPT_PROVIDER_SGNR* WTHelperGetProvSignerFromChain(
        CRYPT_PROVIDER_DATA* pProvData,
        DWORD idxSigner,
        BOOL fCounterSigner,
        DWORD idxCounterSigner
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProvData", "idxSigner", "fCounterSigner", "idxCounterSigner"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintrust_WTHelperProvDataFromStateData(jitter):
    """
    CRYPT_PROVIDER_DATA* WTHelperProvDataFromStateData(
        HANDLE hStateData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hStateData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
