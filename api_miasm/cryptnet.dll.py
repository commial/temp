
def cryptnet_CryptGetObjectUrl(jitter):
    """"
    [Cryptnet.dll] BOOL CryptGetObjectUrl(LPCSTR pszUrlOid, LPVOID pvPara, [CryptGetObjectUrlFlags] dwFlags, PCRYPT_URL_ARRAY pUrlArray, DWORD* pcbUrlArray, PCRYPT_URL_INFO pUrlInfo, DWORD* pcbUrlInfo, LPVOID pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszUrlOid", "pvPara", "dwFlags", "pUrlArray", "pcbUrlArray", "pUrlInfo", "pcbUrlInfo", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptnet_CryptRetrieveObjectByUrl(jitter):
    """"
    [Cryptnet.dll] BOOL CryptRetrieveObjectByUrl(LPCTSTR pszUrl, LPCSTR pszObjectOid, [CryptRetrievalFlags] dwRetrievalFlags, DWORD dwTimeout, LPVOID* ppvObject, HCRYPTASYNC hAsyncRetrieve, PCRYPT_CREDENTIALS pCredentials, LPVOID pvVerify, PCRYPT_RETRIEVE_AUX_INFO pAuxInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszUrl", "pszObjectOid", "dwRetrievalFlags", "dwTimeout", "ppvObject", "hAsyncRetrieve", "pCredentials", "pvVerify", "pAuxInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
