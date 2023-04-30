
def mssign32_SignerFreeSignerContext(jitter):
    """
    [Mssign32.dll] HRESULT SignerFreeSignerContext(SIGNER_CONTEXT* pSignerContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["pSignerContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_SignerSignEx(jitter):
    """
    [Mssign32.dll] HRESULT SignerSignEx([SignerSignEx_FLAGS] dwFlags, SIGNER_SUBJECT_INFO* pSubjectInfo, SIGNER_CERT* pSignerCert, SIGNER_SIGNATURE_INFO* pSignatureInfo, SIGNER_PROVIDER_INFO* pProviderInfo, LPCWSTR pwszHttpTimeStamp, PCRYPT_ATTRIBUTES psRequest, LPVOID pSipData, SIGNER_CONTEXT** ppSignerContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pSubjectInfo", "pSignerCert", "pSignatureInfo", "pProviderInfo", "pwszHttpTimeStamp", "psRequest", "pSipData", "ppSignerContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_SignerSignEx2(jitter):
    """
    [Mssign32.dll] HRESULT SignerSignEx2([SignerSignEx2_FLAGS] dwFlags, SIGNER_SUBJECT_INFO* pSubjectInfo, SIGNER_CERT* pSignerCert, SIGNER_SIGNATURE_INFO* pSignatureInfo, SIGNER_PROVIDER_INFO* pProviderInfo, DWORD dwTimestampFlags, PCSTR pszTimestampAlgorithmOid, PCWSTR pwszHttpTimeStamp, PCRYPT_ATTRIBUTES psRequest, PVOID pSipData, SIGNER_CONTEXT** ppSignerContext, PCERT_STRONG_SIGN_PARA pCryptoPolicy, PVOID pReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pSubjectInfo", "pSignerCert", "pSignatureInfo", "pProviderInfo", "dwTimestampFlags", "pszTimestampAlgorithmOid", "pwszHttpTimeStamp", "psRequest", "pSipData", "ppSignerContext", "pCryptoPolicy", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_SignError(jitter):
    """
    [Mssign32.dll] HRESULT SignError()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_SignerSign(jitter):
    """
    [Mssign32.dll] HRESULT SignerSign(SIGNER_SUBJECT_INFO* pSubjectInfo, SIGNER_CERT* pSignerCert, SIGNER_SIGNATURE_INFO* pSignatureInfo, SIGNER_PROVIDER_INFO* pProviderInfo, LPCWSTR pwszHttpTimeStamp, PCRYPT_ATTRIBUTES psRequest, LPVOID pSipData)
    """
    ret_ad, args = jitter.func_args_stdcall(["pSubjectInfo", "pSignerCert", "pSignatureInfo", "pProviderInfo", "pwszHttpTimeStamp", "psRequest", "pSipData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_SignerTimeStamp(jitter):
    """
    [Mssign32.dll] HRESULT SignerTimeStamp(SIGNER_SUBJECT_INFO* pSubjectInfo, LPCWSTR pwszHttpTimeStamp, PCRYPT_ATTRIBUTES psRequest, LPVOID pSipData)
    """
    ret_ad, args = jitter.func_args_stdcall(["pSubjectInfo", "pwszHttpTimeStamp", "psRequest", "pSipData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_SignerTimeStampEx2(jitter):
    """
    [Mssign32.dll] HRESULT SignerTimeStampEx2(DWORD dwFlags, SIGNER_SUBJECT_INFO* pSubjectInfo, LPCWSTR pwszHttpTimeStamp, ALG_ID dwAlgId, PCRYPT_ATTRIBUTES psRequest, LPVOID pSipData, SIGNER_CONTEXT** ppSignerContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pSubjectInfo", "pwszHttpTimeStamp", "dwAlgId", "psRequest", "pSipData", "ppSignerContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_SignerTimeStampEx(jitter):
    """
    [Mssign32.dll] HRESULT SignerTimeStampEx(DWORD dwFlags, SIGNER_SUBJECT_INFO* pSubjectInfo, LPCWSTR pwszHttpTimeStamp, PCRYPT_ATTRIBUTES psRequest, LPVOID pSipData, SIGNER_CONTEXT** ppSignerContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pSubjectInfo", "pwszHttpTimeStamp", "psRequest", "pSipData", "ppSignerContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_FreeCryptProvFromCertEx(jitter):
    """
    [Mssign32.dll] void FreeCryptProvFromCertEx(BOOL fAcquired, HCRYPTPROV_OR_NCRYPT_KEY_HANDLE hProv, DWORD dwKeySpec, LPWSTR pwszCapiProvider, DWORD dwProviderType, LPWSTR pwszTmpContainer)
    """
    ret_ad, args = jitter.func_args_stdcall(["fAcquired", "hProv", "dwKeySpec", "pwszCapiProvider", "dwProviderType", "pwszTmpContainer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_FreeCryptProvFromCert(jitter):
    """
    [Mssign32.dll] void FreeCryptProvFromCert(BOOL fAcquired, HCRYPTPROV hProv, LPWSTR pwszCapiProvider, DWORD dwProviderType, LPWSTR pwszTmpContainer)
    """
    ret_ad, args = jitter.func_args_stdcall(["fAcquired", "hProv", "pwszCapiProvider", "dwProviderType", "pwszTmpContainer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_GetCryptProvFromCert(jitter):
    """
    [Mssign32.dll] BOOL GetCryptProvFromCert(HWND hwnd, PCCERT_CONTEXT pCert, HCRYPTPROV* phCryptProv, DWORD* pdwKeySpec, BOOL* pfDidCryptAcquire, LPWSTR* ppwszTmpContainer, LPWSTR* ppwszProviderName, DWORD* pdwProviderType)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pCert", "phCryptProv", "pdwKeySpec", "pfDidCryptAcquire", "ppwszTmpContainer", "ppwszProviderName", "pdwProviderType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_PvkFreeCryptProv(jitter):
    """
    [Mssign32.dll] void PvkFreeCryptProv(HCRYPTPROV hProv, LPCWSTR pwszCapiProvider, DWORD dwProviderType, LPWSTR pwszTmpContainer)
    """
    ret_ad, args = jitter.func_args_stdcall(["hProv", "pwszCapiProvider", "dwProviderType", "pwszTmpContainer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_PvkGetCryptProv(jitter):
    """
    [Mssign32.dll] HRESULT PvkGetCryptProv(HWND hwnd, LPCWSTR pwszCaption, LPCWSTR pwszCapiProvider, DWORD dwProviderType, LPCWSTR pwszPvkFile, LPCWSTR pwszKeyContainerName, DWORD* pdwKeySpec, LPWSTR* ppwszTmpContainer, HCRYPTPROV* phCryptProv)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pwszCaption", "pwszCapiProvider", "dwProviderType", "pwszPvkFile", "pwszKeyContainerName", "pdwKeySpec", "ppwszTmpContainer", "phCryptProv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_PvkPrivateKeyAcquireContextFromMemory(jitter):
    """
    [Mssign32.dll] BOOL PvkPrivateKeyAcquireContextFromMemory(LPCWSTR pwszProvName, [CryptProv] dwProvType, BYTE* pbData, DWORD cbData, HWND hwndOwner, LPCWSTR pwszKeyName, DWORD* pdwKeySpec, HCRYPTPROV* phCryptProv, LPTSTR* ppwszTmpContainer)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszProvName", "dwProvType", "pbData", "cbData", "hwndOwner", "pwszKeyName", "pdwKeySpec", "phCryptProv", "ppwszTmpContainer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mssign32_PvkPrivateKeySave(jitter):
    """
    [Mssign32.dll] BOOL PvkPrivateKeySave(HCRYPTPROV hCryptProv, HANDLE hFile, DWORD dwKeySpec, HWND hwndOwner, LPCWSTR pwszKeyName, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hCryptProv", "hFile", "dwKeySpec", "hwndOwner", "pwszKeyName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
