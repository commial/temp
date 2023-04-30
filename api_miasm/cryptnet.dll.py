###### Enums ######

###################

###### Types ######
HCRYPTASYNC = HANDLE

class CRYPT_URL_ARRAY(MemStruct):
    fields = [
        ("cUrl", DWORD()),
        ("rgwszUrl", LPWSTR_PTR()),
    ]

PCRYPT_URL_ARRAY = Ptr("<I", CRYPT_URL_ARRAY())

class CRYPT_URL_INFO(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("dwSyncDeltaTime", DWORD()),
        ("cGroup", DWORD()),
        ("rgcGroupEntry", DWORD_PTR()),
    ]

PCRYPT_URL_INFO = Ptr("<I", CRYPT_URL_INFO())

class CRYPT_CREDENTIALS(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("pszCredentialsOid", LPCSTR()),
        ("pvCredentials", LPVOID()),
    ]

PCRYPT_CREDENTIALS = Ptr("<I", CRYPT_CREDENTIALS())

class CRYPTNET_URL_CACHE_PRE_FETCH_INFO(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("dwObjectType", DWORD()),
        ("dwError", DWORD()),
        ("dwReserved", DWORD()),
        ("ThisUpdateTime", FILETIME()),
        ("NextUpdateTime", FILETIME()),
        ("PublishTime", FILETIME()),
    ]

PCRYPTNET_URL_CACHE_PRE_FETCH_INFO = Ptr("<I", CRYPTNET_URL_CACHE_PRE_FETCH_INFO())

class CRYPTNET_URL_CACHE_FLUSH_INFO(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("dwExemptSeconds", DWORD()),
        ("ExpireTime", FILETIME()),
    ]

PCRYPTNET_URL_CACHE_FLUSH_INFO = Ptr("<I", CRYPTNET_URL_CACHE_FLUSH_INFO())

class CRYPTNET_URL_CACHE_RESPONSE_INFO(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("wResponseType", WORD()),
        ("wResponseFlags", WORD()),
        ("LastModifiedTime", FILETIME()),
        ("dwMaxAge", DWORD()),
        ("pwszETag", LPCWSTR()),
        ("dwProxyId", DWORD()),
    ]

PCRYPTNET_URL_CACHE_RESPONSE_INFO = Ptr("<I", CRYPTNET_URL_CACHE_RESPONSE_INFO())
PCRYPTNET_URL_CACHE_RESPONSE_INFO_PTR = Ptr("<I", PCRYPTNET_URL_CACHE_RESPONSE_INFO())

class CRYPT_RETRIEVE_AUX_INFO(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("pLastSyncTime", FILETIME_PTR()),
        ("dwMaxUrlRetrievalByteCount", DWORD()),
        ("pPreFetchInfo", PCRYPTNET_URL_CACHE_PRE_FETCH_INFO()),
        ("pFlushInfo", PCRYPTNET_URL_CACHE_FLUSH_INFO()),
        ("ppResponseInfo", PCRYPTNET_URL_CACHE_RESPONSE_INFO_PTR()),
        ("pwszCacheFileNamePrefix", LPWSTR()),
        ("pftCacheResync", LPFILETIME()),
        ("fProxyCacheRetrieval", BOOL()),
        ("dwHttpStatusCode", DWORD()),
    ]

PCRYPT_RETRIEVE_AUX_INFO = Ptr("<I", CRYPT_RETRIEVE_AUX_INFO())
_CryptRetrievalFlags_ = DWORD
_CryptGetObjectUrlFlags_ = DWORD

###################

###### Functions ######

def cryptnet_CryptGetObjectUrl(jitter):
    """
    BOOL CryptGetObjectUrl(
        LPCSTR pszUrlOid,
        LPVOID pvPara,
        [CryptGetObjectUrlFlags] dwFlags,
        PCRYPT_URL_ARRAY pUrlArray,
        DWORD* pcbUrlArray,
        PCRYPT_URL_INFO pUrlInfo,
        DWORD* pcbUrlInfo,
        LPVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUrlOid", "pvPara", "dwFlags", "pUrlArray", "pcbUrlArray", "pUrlInfo", "pcbUrlInfo", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptnet_CryptRetrieveObjectByUrl(jitter, get_str, set_str):
    """
    BOOL CryptRetrieveObjectByUrl(
        LPCTSTR pszUrl,
        LPCSTR pszObjectOid,
        [CryptRetrievalFlags] dwRetrievalFlags,
        DWORD dwTimeout,
        LPVOID* ppvObject,
        HCRYPTASYNC hAsyncRetrieve,
        PCRYPT_CREDENTIALS pCredentials,
        LPVOID pvVerify,
        PCRYPT_RETRIEVE_AUX_INFO pAuxInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUrl", "pszObjectOid", "dwRetrievalFlags", "dwTimeout", "ppvObject", "hAsyncRetrieve", "pCredentials", "pvVerify", "pAuxInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptnet_CryptRetrieveObjectByUrlA(jitter):
    cryptnet_CryptRetrieveObjectByUrl(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cryptnet_CryptRetrieveObjectByUrlW(jitter):
    cryptnet_CryptRetrieveObjectByUrl(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
