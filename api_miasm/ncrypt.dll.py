###### Enums ######
_SslContentType_ = {
    "CT_CHANGE_CIPHER_SPEC": 20,
    "CT_ALERT": 21,
    "CT_HANDSHAKE": 22,
    "CT_APPLICATIONDATA": 23,
}
_SslContentType__INV = {
    20: "CT_CHANGE_CIPHER_SPEC",
    21: "CT_ALERT",
    22: "CT_HANDSHAKE",
    23: "CT_APPLICATIONDATA",
}

###################

###### Types ######
NCRYPT_HANDLE = ULONG_PTR
NCRYPT_PROV_HANDLE = ULONG_PTR
NCRYPT_PROV_HANDLE_PTR = Ptr("<I", NCRYPT_PROV_HANDLE())
NCRYPT_SECRET_HANDLE = ULONG_PTR
NCRYPT_SECRET_HANDLE_PTR = Ptr("<I", NCRYPT_SECRET_HANDLE())
NCRYPT_HASH_HANDLE = ULONG_PTR
NCRYPT_HASH_HANDLE_PTR = Ptr("<I", NCRYPT_HASH_HANDLE())
NCryptBufferDesc = BCryptBufferDesc
NCryptBufferDesc_PTR = Ptr("<I", NCryptBufferDesc())
PNCryptBufferDesc = Ptr("<I", NCryptBufferDesc())
NCRYPT_DESCRIPTOR_HANDLE = HANDLE
NCRYPT_DESCRIPTOR_HANDLE_PTR = Ptr("<I", NCRYPT_DESCRIPTOR_HANDLE())
PFN_NCRYPT_ALLOC = LPVOID
PFN_NCRYPT_FREE = LPVOID
NCRYPT_STREAM_HANDLE = HANDLE
NCRYPT_STREAM_HANDLE_PTR = Ptr("<I", NCRYPT_STREAM_HANDLE())
PFNCryptStreamOutputCallback = LPVOID
WCHAR_NCRYPT_SSL_MAX_NAME_SIZE_ = WCHAR_PTR
NCRYPT_SSL_CIPHER_SUITE_PTR = LPVOID
NCRYPT_SSL_CIPHER_SUITE_PTR_PTR = Ptr("<I", NCRYPT_SSL_CIPHER_SUITE_PTR())
NCRYPT_SSL_CIPHER_LENGTHS_PTR = LPVOID

class NCryptAlgorithmName(MemStruct):
    fields = [
        ("pszName", LPWSTR()),
        ("dwClass", DWORD()),
        ("dwAlgOperations", DWORD()),
        ("dwFlags", DWORD()),
    ]

NCryptAlgorithmName_PTR = Ptr("<I", NCryptAlgorithmName())
NCryptAlgorithmName_PTR_PTR = Ptr("<I", NCryptAlgorithmName_PTR())

class NCryptKeyName(MemStruct):
    fields = [
        ("pszName", LPWSTR()),
        ("pszAlgid", LPWSTR()),
        ("dwLegacyKeySpec", DWORD()),
        ("dwFlags", DWORD()),
    ]

NCryptKeyName_PTR = Ptr("<I", NCryptKeyName())
NCryptKeyName_PTR_PTR = Ptr("<I", NCryptKeyName_PTR())

class NCryptProviderName(MemStruct):
    fields = [
        ("pszName", LPWSTR()),
        ("pszComment", LPWSTR()),
    ]

NCryptProviderName_PTR = Ptr("<I", NCryptProviderName())
NCryptProviderName_PTR_PTR = Ptr("<I", NCryptProviderName_PTR())
_SslContentType_ = DWORD

class NCRYPT_ALLOC_PARA(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("pfnAlloc", PFN_NCRYPT_ALLOC()),
        ("pfnFree", PFN_NCRYPT_FREE()),
    ]

const_NCRYPT_ALLOC_PARA_PTR = Ptr("<I", NCRYPT_ALLOC_PARA())

class NCRYPT_PROTECT_STREAM_INFO(MemStruct):
    fields = [
        ("pfnStreamOutput", PFNCryptStreamOutputCallback()),
        ("pvCallbackCtxt", void_PTR()),
    ]

NCRYPT_PROTECT_STREAM_INFO_PTR = Ptr("<I", NCRYPT_PROTECT_STREAM_INFO())

###################

###### Functions ######

def ncrypt_NCryptCreatePersistedKey(jitter):
    """
    SECURITY_STATUS NCryptCreatePersistedKey(
        NCRYPT_PROV_HANDLE hProvider,
        NCRYPT_KEY_HANDLE* phKey,
        LPCWSTR pszAlgId,
        LPCWSTR pszKeyName,
        DWORD dwLegacyKeySpec,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "phKey", "pszAlgId", "pszKeyName", "dwLegacyKeySpec", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptDecrypt(jitter):
    """
    SECURITY_STATUS NCryptDecrypt(
        NCRYPT_KEY_HANDLE hKey,
        PBYTE pbInput,
        DWORD cbInput,
        VOID* pPaddingInfo,
        PBYTE pbOutput,
        DWORD cbOutput,
        DWORD* pcbResult,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pbInput", "cbInput", "pPaddingInfo", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptDeleteKey(jitter):
    """
    SECURITY_STATUS NCryptDeleteKey(
        NCRYPT_KEY_HANDLE hKey,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptDeriveKey(jitter):
    """
    SECURITY_STATUS NCryptDeriveKey(
        NCRYPT_SECRET_HANDLE hSharedSecret,
        LPCWSTR pwszKDF,
        NCryptBufferDesc* pParameterList,
        PBYTE pbDerivedKey,
        DWORD cbDerivedKey,
        DWORD* pcbResult,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSharedSecret", "pwszKDF", "pParameterList", "pbDerivedKey", "cbDerivedKey", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptEncrypt(jitter):
    """
    SECURITY_STATUS NCryptEncrypt(
        NCRYPT_KEY_HANDLE hKey,
        PBYTE pbInput,
        DWORD cbInput,
        VOID* pPaddingInfo,
        PBYTE pbOutput,
        DWORD cbOutput,
        DWORD* pcbResult,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pbInput", "cbInput", "pPaddingInfo", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptEnumAlgorithms(jitter):
    """
    SECURITY_STATUS NCryptEnumAlgorithms(
        NCRYPT_PROV_HANDLE hProvider,
        DWORD dwAlgOperations,
        DWORD* pdwAlgCount,
        NCryptAlgorithmName** ppAlgList,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "dwAlgOperations", "pdwAlgCount", "ppAlgList", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptEnumKeys(jitter):
    """
    SECURITY_STATUS NCryptEnumKeys(
        NCRYPT_PROV_HANDLE hProvider,
        LPCWSTR pszScope,
        NCryptKeyName** ppKeyName,
        PVOID* ppEnumState,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pszScope", "ppKeyName", "ppEnumState", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptEnumStorageProviders(jitter):
    """
    SECURITY_STATUS NCryptEnumStorageProviders(
        DWORD* pdwProviderCount,
        NCryptProviderName** ppProviderList,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwProviderCount", "ppProviderList", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptExportKey(jitter):
    """
    SECURITY_STATUS NCryptExportKey(
        NCRYPT_KEY_HANDLE hKey,
        NCRYPT_KEY_HANDLE hExportKey,
        LPCWSTR pszBlobType,
        NCryptBufferDesc* pParameterList,
        PBYTE pbOutput,
        DWORD cbOutput,
        DWORD* pcbResult,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "hExportKey", "pszBlobType", "pParameterList", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptFinalizeKey(jitter):
    """
    SECURITY_STATUS NCryptFinalizeKey(
        NCRYPT_KEY_HANDLE hKey,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptFreeBuffer(jitter):
    """
    SECURITY_STATUS NCryptFreeBuffer(
        PVOID pvInput
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvInput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptFreeObject(jitter):
    """
    SECURITY_STATUS NCryptFreeObject(
        NCRYPT_HANDLE hObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptGetProperty(jitter):
    """
    SECURITY_STATUS NCryptGetProperty(
        NCRYPT_HANDLE hObject,
        LPCWSTR pszProperty,
        PBYTE pbOutput,
        DWORD cbOutput,
        DWORD* pcbResult,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hObject", "pszProperty", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptImportKey(jitter):
    """
    SECURITY_STATUS NCryptImportKey(
        NCRYPT_PROV_HANDLE hProvider,
        NCRYPT_KEY_HANDLE hImportKey,
        LPCWSTR pszBlobType,
        NCryptBufferDesc* pParameterList,
        NCRYPT_KEY_HANDLE* phKey,
        PBYTE pbData,
        DWORD cbData,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "hImportKey", "pszBlobType", "pParameterList", "phKey", "pbData", "cbData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptIsAlgSupported(jitter):
    """
    SECURITY_STATUS NCryptIsAlgSupported(
        NCRYPT_PROV_HANDLE hProvider,
        LPCWSTR pszAlgId,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pszAlgId", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptIsKeyHandle(jitter):
    """
    BOOL NCryptIsKeyHandle(
        NCRYPT_KEY_HANDLE hKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptKeyDerivation(jitter):
    """
    SECURITY_STATUS NCryptKeyDerivation(
        NCRYPT_KEY_HANDLE hKey,
        NCryptBufferDesc* pParameterList,
        PUCHAR pbDerivedKey,
        DWORD cbDerivedKey,
        DWORD* pcbResult,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pParameterList", "pbDerivedKey", "cbDerivedKey", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptNotifyChangeKey(jitter):
    """
    SECURITY_STATUS NCryptNotifyChangeKey(
        NCRYPT_PROV_HANDLE hProvider,
        HANDLE* phEvent,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "phEvent", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptOpenKey(jitter):
    """
    SECURITY_STATUS NCryptOpenKey(
        NCRYPT_PROV_HANDLE hProvider,
        NCRYPT_KEY_HANDLE* phKey,
        LPCWSTR pszKeyName,
        DWORD dwLegacyKeySpec,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "phKey", "pszKeyName", "dwLegacyKeySpec", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptOpenStorageProvider(jitter):
    """
    SECURITY_STATUS NCryptOpenStorageProvider(
        NCRYPT_PROV_HANDLE* phProvider,
        LPCWSTR pszProviderName,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phProvider", "pszProviderName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptSecretAgreement(jitter):
    """
    SECURITY_STATUS NCryptSecretAgreement(
        NCRYPT_KEY_HANDLE hPrivKey,
        NCRYPT_KEY_HANDLE hPubKey,
        NCRYPT_SECRET_HANDLE* phSecret,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrivKey", "hPubKey", "phSecret", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptSetProperty(jitter):
    """
    SECURITY_STATUS NCryptSetProperty(
        NCRYPT_HANDLE hObject,
        LPCWSTR pszProperty,
        PBYTE pbInput,
        DWORD cbInput,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hObject", "pszProperty", "pbInput", "cbInput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptSignHash(jitter):
    """
    SECURITY_STATUS NCryptSignHash(
        NCRYPT_KEY_HANDLE hKey,
        VOID* pPaddingInfo,
        PBYTE pbHashValue,
        DWORD cbHashValue,
        PBYTE pbSignature,
        DWORD cbSignature,
        DWORD* pcbResult,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pPaddingInfo", "pbHashValue", "cbHashValue", "pbSignature", "cbSignature", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptTranslateHandle(jitter):
    """
    SECURITY_STATUS NCryptTranslateHandle(
        NCRYPT_PROV_HANDLE* phProvider,
        NCRYPT_KEY_HANDLE* phKey,
        HCRYPTPROV hLegacyProv,
        HCRYPTKEY hLegacyKey,
        DWORD dwLegacyKeySpec,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phProvider", "phKey", "hLegacyProv", "hLegacyKey", "dwLegacyKeySpec", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptVerifySignature(jitter):
    """
    SECURITY_STATUS NCryptVerifySignature(
        NCRYPT_KEY_HANDLE hKey,
        VOID* pPaddingInfo,
        PBYTE pbHashValue,
        DWORD cbHashValue,
        PBYTE pbSignature,
        DWORD cbSignature,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pPaddingInfo", "pbHashValue", "cbHashValue", "pbSignature", "cbSignature", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslChangeNotify(jitter):
    """
    SECURITY_STATUS SslChangeNotify(
        HANDLE hEvent,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEvent", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslComputeClientAuthHash(jitter):
    """
    SECURITY_STATUS SslComputeClientAuthHash(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE hMasterKey,
        NCRYPT_HASH_HANDLE hHandshakeHash,
        LPCWSTR pszAlgId,
        PBYTE pbOutput,
        DWORD cbOutput,
        DWORD* pcbResult,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "hMasterKey", "hHandshakeHash", "pszAlgId", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslComputeEapKeyBlock(jitter):
    """
    SECURITY_STATUS SslComputeEapKeyBlock(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE hMasterKey,
        PBYTE pbRandoms,
        DWORD cbRandoms,
        PBYTE pbOutput,
        DWORD cbOutput,
        DWORD* pcbResult,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "hMasterKey", "pbRandoms", "cbRandoms", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslComputeFinishedHash(jitter):
    """
    SECURITY_STATUS SslComputeFinishedHash(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE hMasterKey,
        NCRYPT_HASH_HANDLE hHandshakeHash,
        PBYTE pbOutput,
        DWORD cbOutput,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "hMasterKey", "hHandshakeHash", "pbOutput", "cbOutput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslCreateClientAuthHash(jitter):
    """
    SECURITY_STATUS SslCreateClientAuthHash(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_HASH_HANDLE* phHandshakeHash,
        DWORD dwProtocol,
        DWORD dwCipherSuite,
        LPCWSTR pszHashAlgId,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "phHandshakeHash", "dwProtocol", "dwCipherSuite", "pszHashAlgId", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslCreateEphemeralKey(jitter):
    """
    SECURITY_STATUS SslCreateEphemeralKey(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE* phEphemeralKey,
        DWORD dwProtocol,
        DWORD dwCipherSuite,
        DWORD dwKeyType,
        DWORD dwKeyBitLen,
        PBYTE pbParams,
        DWORD cbParams,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "phEphemeralKey", "dwProtocol", "dwCipherSuite", "dwKeyType", "dwKeyBitLen", "pbParams", "cbParams", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslCreateHandshakeHash(jitter):
    """
    SECURITY_STATUS SslCreateHandshakeHash(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_HASH_HANDLE* phHandshakeHash,
        DWORD dwProtocol,
        DWORD dwCipherSuite,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "phHandshakeHash", "dwProtocol", "dwCipherSuite", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslDecrementProviderReferenceCount(jitter):
    """
    SECURITY_STATUS SslDecrementProviderReferenceCount(
        NCRYPT_PROV_HANDLE hSslProvider
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslDecryptPacket(jitter):
    """
    SECURITY_STATUS SslDecryptPacket(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE hKey,
        PBYTE pbInput,
        DWORD cbInput,
        PBYTE pbOutput,
        DWORD cbOutput,
        DWORD* pcbResult,
        ULONGLONG SequenceNumber,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "hKey", "pbInput", "cbInput", "pbOutput", "cbOutput", "pcbResult", "SequenceNumber", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslEncryptPacket(jitter):
    """
    SECURITY_STATUS SslEncryptPacket(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE hKey,
        PBYTE pbInput,
        DWORD cbInput,
        PBYTE pbOutput,
        DWORD cbOutput,
        DWORD* pcbResult,
        ULONGLONG SequenceNumber,
        [SslContentType] dwContentType,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "hKey", "pbInput", "cbInput", "pbOutput", "cbOutput", "pcbResult", "SequenceNumber", "dwContentType", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslEnumCipherSuites(jitter):
    """
    SECURITY_STATUS SslEnumCipherSuites(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE hPrivateKey,
        NCRYPT_SSL_CIPHER_SUITE** ppCipherSuite,
        PVOID* ppEnumState,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "hPrivateKey", "ppCipherSuite", "ppEnumState", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslEnumProtocolProviders(jitter):
    """
    SECURITY_STATUS SslEnumProtocolProviders(
        DWORD* pdwProviderCount,
        NCryptProviderName** ppProviderList,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwProviderCount", "ppProviderList", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslExportKey(jitter):
    """
    SECURITY_STATUS SslExportKey(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE hKey,
        LPCWSTR pszBlobType,
        PBYTE pbOutput,
        DWORD cbOutput,
        DWORD* pcbResult,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "hKey", "pszBlobType", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslFreeBuffer(jitter):
    """
    SECURITY_STATUS SslFreeBuffer(
        PVOID pvInput
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvInput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslFreeObject(jitter):
    """
    SECURITY_STATUS SslFreeObject(
        NCRYPT_HANDLE hObject,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hObject", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslGenerateMasterKey(jitter):
    """
    SECURITY_STATUS SslGenerateMasterKey(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE hPrivateKey,
        NCRYPT_KEY_HANDLE hPublicKey,
        NCRYPT_KEY_HANDLE* phMasterKey,
        DWORD dwProtocol,
        DWORD dwCipherSuite,
        PNCryptBufferDesc pParameterList,
        PBYTE pbOutput,
        DWORD cbOutput,
        DWORD* pcbResult,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "hPrivateKey", "hPublicKey", "phMasterKey", "dwProtocol", "dwCipherSuite", "pParameterList", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslGenerateSessionKeys(jitter):
    """
    SECURITY_STATUS SslGenerateSessionKeys(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE hMasterKey,
        NCRYPT_KEY_HANDLE* phReadKey,
        NCRYPT_KEY_HANDLE* phWriteKey,
        PNCryptBufferDesc pParameterList,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "hMasterKey", "phReadKey", "phWriteKey", "pParameterList", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslGetCipherSuitePRFHashAlgorithm(jitter):
    """
    SECURITY_STATUS SslGetCipherSuitePRFHashAlgorithm(
        NCRYPT_PROV_HANDLE hSslProvider,
        DWORD dwProtocol,
        DWORD dwCipherSuite,
        DWORD dwKeyType,
        WCHAR[NCRYPT_SSL_MAX_NAME_SIZE] szPRFHash,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "dwProtocol", "dwCipherSuite", "dwKeyType", "szPRFHash", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslGetKeyProperty(jitter):
    """
    SECURITY_STATUS SslGetKeyProperty(
        NCRYPT_KEY_HANDLE hKey,
        LPCWSTR pszProperty,
        PBYTE ppbOutput,
        DWORD* pcbOutput,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pszProperty", "ppbOutput", "pcbOutput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslGetProviderProperty(jitter):
    """
    SECURITY_STATUS SslGetProviderProperty(
        NCRYPT_PROV_HANDLE hSslProvider,
        LPCWSTR pszProperty,
        PBYTE ppbOutput,
        DWORD* pcbOutput,
        PVOID* ppEnumState,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "pszProperty", "ppbOutput", "pcbOutput", "ppEnumState", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslHashHandshake(jitter):
    """
    SECURITY_STATUS SslHashHandshake(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_HASH_HANDLE hHandshakeHash,
        PBYTE pbInput,
        DWORD cbInput,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "hHandshakeHash", "pbInput", "cbInput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslImportKey(jitter):
    """
    SECURITY_STATUS SslImportKey(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE* phKey,
        LPCWSTR pszBlobType,
        PBYTE pbKeyBlob,
        DWORD cbKeyBlob,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "phKey", "pszBlobType", "pbKeyBlob", "cbKeyBlob", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslImportMasterKey(jitter):
    """
    SECURITY_STATUS SslImportMasterKey(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE hPrivateKey,
        NCRYPT_KEY_HANDLE* phMasterKey,
        DWORD dwProtocol,
        DWORD dwCipherSuite,
        PNCryptBufferDesc pParameterList,
        PBYTE pbEncryptedKey,
        DWORD cbEncryptedKey,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "hPrivateKey", "phMasterKey", "dwProtocol", "dwCipherSuite", "pParameterList", "pbEncryptedKey", "cbEncryptedKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslIncrementProviderReferenceCount(jitter):
    """
    SECURITY_STATUS SslIncrementProviderReferenceCount(
        NCRYPT_PROV_HANDLE hSslProvider
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslLookupCipherLengths(jitter):
    """
    SECURITY_STATUS SslLookupCipherLengths(
        NCRYPT_PROV_HANDLE hSslProvider,
        DWORD dwProtocol,
        DWORD dwCipherSuite,
        DWORD dwKeyType,
        NCRYPT_SSL_CIPHER_LENGTHS* pCipherLengths,
        DWORD cbCipherLengths,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "dwProtocol", "dwCipherSuite", "dwKeyType", "pCipherLengths", "cbCipherLengths", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslLookupCipherSuiteInfo(jitter):
    """
    SECURITY_STATUS SslLookupCipherSuiteInfo(
        NCRYPT_PROV_HANDLE hSslProvider,
        DWORD dwProtocol,
        DWORD dwCipherSuite,
        DWORD dwKeyType,
        NCRYPT_SSL_CIPHER_SUITE* pCipherSuite,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "dwProtocol", "dwCipherSuite", "dwKeyType", "pCipherSuite", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslOpenPrivateKey(jitter):
    """
    SECURITY_STATUS SslOpenPrivateKey(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE* phPrivateKey,
        PCCERT_CONTEXT pCertContext,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "phPrivateKey", "pCertContext", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslOpenProvider(jitter):
    """
    SECURITY_STATUS SslOpenProvider(
        NCRYPT_PROV_HANDLE* phSslProvider,
        LPCWSTR pszProviderName,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phSslProvider", "pszProviderName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslSignHash(jitter):
    """
    SECURITY_STATUS SslSignHash(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE hPrivateKey,
        PBYTE pbHashValue,
        DWORD cbHashValue,
        PBYTE pbSignature,
        DWORD cbSignature,
        DWORD* pcbResult,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "hPrivateKey", "pbHashValue", "cbHashValue", "pbSignature", "cbSignature", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_SslVerifySignature(jitter):
    """
    SECURITY_STATUS SslVerifySignature(
        NCRYPT_PROV_HANDLE hSslProvider,
        NCRYPT_KEY_HANDLE hPublicKey,
        PBYTE pbHashValue,
        DWORD cbHashValue,
        PBYTE pbSignature,
        DWORD cbSignature,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSslProvider", "hPublicKey", "pbHashValue", "cbHashValue", "pbSignature", "cbSignature", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptCreateProtectionDescriptor(jitter):
    """
    NTSTATUS NCryptCreateProtectionDescriptor(
        LPCWSTR pwszDescriptorString,
        DWORD dwFlags,
        NCRYPT_DESCRIPTOR_HANDLE* phDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszDescriptorString", "dwFlags", "phDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptCloseProtectionDescriptor(jitter):
    """
    NTSTATUS NCryptCloseProtectionDescriptor(
        NCRYPT_DESCRIPTOR_HANDLE hDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptGetProtectionDescriptorInfo(jitter):
    """
    NTSTATUS NCryptGetProtectionDescriptorInfo(
        NCRYPT_DESCRIPTOR_HANDLE hDescriptor,
        const NCRYPT_ALLOC_PARA* pMemPara,
        DWORD dwInfoType,
        void* ppvInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDescriptor", "pMemPara", "dwInfoType", "ppvInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptProtectSecret(jitter):
    """
    NTSTATUS NCryptProtectSecret(
        NCRYPT_DESCRIPTOR_HANDLE hDescriptor,
        DWORD dwFlags,
        const BYTE* pbData,
        ULONG cbData,
        const NCRYPT_ALLOC_PARA* pMemPara,
        HWND hWnd,
        BYTE** ppbProtectedBlob,
        ULONG* pcbProtectedBlob
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDescriptor", "dwFlags", "pbData", "cbData", "pMemPara", "hWnd", "ppbProtectedBlob", "pcbProtectedBlob"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptQueryProtectionDescriptorName(jitter):
    """
    NTSTATUS NCryptQueryProtectionDescriptorName(
        LPCWSTR pwszName,
        LPWSTR pwszDescriptorString,
        SIZE_T* pcDescriptorString,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszName", "pwszDescriptorString", "pcDescriptorString", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptRegisterProtectionDescriptorName(jitter):
    """
    NTSTATUS NCryptRegisterProtectionDescriptorName(
        LPCWSTR pwszName,
        LPCWSTR pwszDescriptorString,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszName", "pwszDescriptorString", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptStreamClose(jitter):
    """
    NTSTATUS NCryptStreamClose(
        NCRYPT_STREAM_HANDLE hStream
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hStream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptStreamOpenToProtect(jitter):
    """
    NTSTATUS NCryptStreamOpenToProtect(
        NCRYPT_DESCRIPTOR_HANDLE hDescriptor,
        DWORD dwFlags,
        HWND hWnd,
        NCRYPT_PROTECT_STREAM_INFO* pStreamInfo,
        NCRYPT_STREAM_HANDLE* phStream
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDescriptor", "dwFlags", "hWnd", "pStreamInfo", "phStream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptStreamOpenToUnprotect(jitter):
    """
    NTSTATUS NCryptStreamOpenToUnprotect(
        NCRYPT_PROTECT_STREAM_INFO* pStreamInfo,
        DWORD dwFlags,
        HWND hWnd,
        NCRYPT_STREAM_HANDLE* phStream
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStreamInfo", "dwFlags", "hWnd", "phStream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptStreamUpdate(jitter):
    """
    NTSTATUS NCryptStreamUpdate(
        NCRYPT_STREAM_HANDLE hStream,
        const BYTE* pbData,
        SIZE_T cbData,
        BOOL fFinal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hStream", "pbData", "cbData", "fFinal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ncrypt_NCryptUnprotectSecret(jitter):
    """
    NTSTATUS NCryptUnprotectSecret(
        NCRYPT_DESCRIPTOR_HANDLE* phDescriptor,
        DWORD dwFlags,
        const BYTE* pbProtectedBlob,
        ULONG cbProtectedBlob,
        const NCRYPT_ALLOC_PARA* pMemPara,
        HWND hWnd,
        BYTE** ppbData,
        ULONG* pcbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phDescriptor", "dwFlags", "pbProtectedBlob", "cbProtectedBlob", "pMemPara", "hWnd", "ppbData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
