###### Enums ######
_CryptConfigTable_ = {
    "CRYPT_LOCAL": 0x00000001,
    "CRYPT_DOMAIN": 0x00000002,
}
_CryptConfigTable__INV = {
    0x00000001: "CRYPT_LOCAL",
    0x00000002: "CRYPT_DOMAIN",
}
_CryptInterface_ = {
    "BCRYPT_CIPHER_INTERFACE": 0x00000001,
    "BCRYPT_HASH_INTERFACE": 0x00000002,
    "BCRYPT_ASYMMETRIC_ENCRYPTION_INTERFACE": 0x00000003,
    "BCRYPT_SECRET_AGREEMENT_INTERFACE": 0x00000004,
    "BCRYPT_SIGNATURE_INTERFACE": 0x00000005,
    "BCRYPT_RNG_INTERFACE": 0x00000006,
    "NCRYPT_KEY_STORAGE_INTERFACE": 0x00010001,
    "NCRYPT_SCHANNEL_INTERFACE": 0x00010002,
    "NCRYPT_SCHANNEL_SIGNATURE_INTERFACE": 0x00010003,
}
_CryptInterface__INV = {
    0x00000001: "BCRYPT_CIPHER_INTERFACE",
    0x00000002: "BCRYPT_HASH_INTERFACE",
    0x00000003: "BCRYPT_ASYMMETRIC_ENCRYPTION_INTERFACE",
    0x00000004: "BCRYPT_SECRET_AGREEMENT_INTERFACE",
    0x00000005: "BCRYPT_SIGNATURE_INTERFACE",
    0x00000006: "BCRYPT_RNG_INTERFACE",
    0x00010001: "NCRYPT_KEY_STORAGE_INTERFACE",
    0x00010002: "NCRYPT_SCHANNEL_INTERFACE",
    0x00010003: "NCRYPT_SCHANNEL_SIGNATURE_INTERFACE",
}
_CryptPriority_ = {
    "CRYPT_PRIORITY_TOP": 0x00000000,
    "CRYPT_PRIORITY_BOTTOM": 0xFFFFFFFF,
}
_CryptPriority__INV = {
    0x00000000: "CRYPT_PRIORITY_TOP",
    0xFFFFFFFF: "CRYPT_PRIORITY_BOTTOM",
}
_CryptMode_ = {
    "CRYPT_UM": 0x00000001,
    "CRYPT_KM": 0x00000002,
    "CRYPT_MM": 0x00000003,
    "CRYPT_ANY": 0x00000004,
}
_CryptMode__INV = {
    0x00000001: "CRYPT_UM",
    0x00000002: "CRYPT_KM",
    0x00000003: "CRYPT_MM",
    0x00000004: "CRYPT_ANY",
}

###################

###### Types ######
BCRYPT_HANDLE = LPVOID
BCRYPT_ALG_HANDLE = LPVOID
BCRYPT_ALG_HANDLE_PTR = Ptr("<I", BCRYPT_ALG_HANDLE())
BCRYPT_HASH_HANDLE = LPVOID
BCRYPT_HASH_HANDLE_PTR = Ptr("<I", BCRYPT_HASH_HANDLE())
BCRYPT_SECRET_HANDLE = LPVOID
BCRYPT_SECRET_HANDLE_PTR = Ptr("<I", BCRYPT_SECRET_HANDLE())

class CRYPT_CONTEXT_CONFIG(MemStruct):
    fields = [
        ("dwFlags", ULONG()),
        ("dwReserved", ULONG()),
    ]

PCRYPT_CONTEXT_CONFIG = Ptr("<I", CRYPT_CONTEXT_CONFIG())
PCRYPT_CONTEXT_CONFIG_PTR = Ptr("<I", PCRYPT_CONTEXT_CONFIG())
PCRYPT_CONTEXT_FUNCTION_CONFIG = Ptr("<I", CRYPT_CONTEXT_CONFIG())
PCRYPT_CONTEXT_FUNCTION_CONFIG_PTR = Ptr("<I", PCRYPT_CONTEXT_FUNCTION_CONFIG())

class BCRYPT_ALGORITHM_IDENTIFIER(MemStruct):
    fields = [
        ("pszName", LPWSTR()),
        ("dwClass", ULONG()),
        ("dwFlags", ULONG()),
    ]

BCRYPT_ALGORITHM_IDENTIFIER_PTR = Ptr("<I", BCRYPT_ALGORITHM_IDENTIFIER())
BCRYPT_ALGORITHM_IDENTIFIER_PTR_PTR = Ptr("<I", BCRYPT_ALGORITHM_IDENTIFIER_PTR())

class CRYPT_CONTEXT_FUNCTION_PROVIDERS(MemStruct):
    fields = [
        ("cProviders", ULONG()),
        ("rgpszProviders", PWSTR_PTR()),
    ]

PCRYPT_CONTEXT_FUNCTION_PROVIDERS = Ptr("<I", CRYPT_CONTEXT_FUNCTION_PROVIDERS())
PCRYPT_CONTEXT_FUNCTION_PROVIDERS_PTR = Ptr("<I", PCRYPT_CONTEXT_FUNCTION_PROVIDERS())

class CRYPT_CONTEXT_FUNCTIONS(MemStruct):
    fields = [
        ("cFunctions", ULONG()),
        ("rgpszFunctions", PWSTR_PTR()),
    ]

PCRYPT_CONTEXT_FUNCTIONS = Ptr("<I", CRYPT_CONTEXT_FUNCTIONS())
PCRYPT_CONTEXT_FUNCTIONS_PTR = Ptr("<I", PCRYPT_CONTEXT_FUNCTIONS())

class CRYPT_CONTEXTS(MemStruct):
    fields = [
        ("cContexts", ULONG()),
        ("rgpszContexts", PWSTR_PTR()),
    ]

PCRYPT_CONTEXTS = Ptr("<I", CRYPT_CONTEXTS())
PCRYPT_CONTEXTS_PTR = Ptr("<I", PCRYPT_CONTEXTS())

class BCRYPT_PROVIDER_NAME(MemStruct):
    fields = [
        ("pszProviderName", LPWSTR()),
    ]

BCRYPT_PROVIDER_NAME_PTR = Ptr("<I", BCRYPT_PROVIDER_NAME())
BCRYPT_PROVIDER_NAME_PTR_PTR = Ptr("<I", BCRYPT_PROVIDER_NAME_PTR())
CRYPT_PROVIDERS = CRYPT_CONTEXT_FUNCTION_PROVIDERS
PCRYPT_PROVIDERS = Ptr("<I", CRYPT_PROVIDERS())
PCRYPT_PROVIDERS_PTR = Ptr("<I", PCRYPT_PROVIDERS())

class CRYPT_INTERFACE_REG(MemStruct):
    fields = [
        ("dwInterface", ULONG()),
        ("dwFlags", ULONG()),
        ("cFunctions", ULONG()),
        ("rgpszFunctions", PWSTR_PTR()),
    ]

PCRYPT_INTERFACE_REG = Ptr("<I", CRYPT_INTERFACE_REG())
PCRYPT_INTERFACE_REG_PTR = Ptr("<I", PCRYPT_INTERFACE_REG())

class CRYPT_IMAGE_REG(MemStruct):
    fields = [
        ("pszImage", PWSTR()),
        ("cInterfaces", ULONG()),
        ("rgpInterfaces", PCRYPT_INTERFACE_REG_PTR()),
    ]

PCRYPT_IMAGE_REG = Ptr("<I", CRYPT_IMAGE_REG())

class CRYPT_PROVIDER_REG(MemStruct):
    fields = [
        ("cAliases", ULONG()),
        ("rgpszAliases", PWSTR_PTR()),
        ("pUM", PCRYPT_IMAGE_REG()),
        ("pKM", PCRYPT_IMAGE_REG()),
    ]

PCRYPT_PROVIDER_REG = Ptr("<I", CRYPT_PROVIDER_REG())
PCRYPT_PROVIDER_REG_PTR = Ptr("<I", PCRYPT_PROVIDER_REG())

class CRYPT_PROPERTY_REF(MemStruct):
    fields = [
        ("pszProperty", PWSTR()),
        ("cbValue", ULONG()),
        ("pbValue", PUCHAR()),
    ]

PCRYPT_PROPERTY_REF = Ptr("<I", CRYPT_PROPERTY_REF())
PCRYPT_PROPERTY_REF_PTR = Ptr("<I", PCRYPT_PROPERTY_REF())

class CRYPT_IMAGE_REF(MemStruct):
    fields = [
        ("pszImage", PWSTR()),
        ("dwFlags", ULONG()),
    ]

PCRYPT_IMAGE_REF = Ptr("<I", CRYPT_IMAGE_REF())

class CRYPT_PROVIDER_REF(MemStruct):
    fields = [
        ("dwInterface", ULONG()),
        ("pszFunction", PWSTR()),
        ("pszProvider", PWSTR()),
        ("cProperties", ULONG()),
        ("rgpProperties", PCRYPT_PROPERTY_REF_PTR()),
        ("pUM", PCRYPT_IMAGE_REF()),
        ("pKM", PCRYPT_IMAGE_REF()),
    ]

PCRYPT_PROVIDER_REF = Ptr("<I", CRYPT_PROVIDER_REF())
PCRYPT_PROVIDER_REF_PTR = Ptr("<I", PCRYPT_PROVIDER_REF())

class CRYPT_PROVIDER_REFS(MemStruct):
    fields = [
        ("cProviders", ULONG()),
        ("rgpProviders", PCRYPT_PROVIDER_REF_PTR()),
    ]

PCRYPT_PROVIDER_REFS = Ptr("<I", CRYPT_PROVIDER_REFS())
PCRYPT_PROVIDER_REFS_PTR = Ptr("<I", PCRYPT_PROVIDER_REFS())
_CryptConfigTable_ = ULONG
_CryptInterface_ = ULONG
_CryptPriority_ = ULONG
_CryptOperation_ = ULONG
_CryptMode_ = ULONG
_CryptEnumFlags_ = ULONG
_CryptDeriveKeyFlags_ = ULONG
_BCryptOpenAlgorithmProviderFlags_ = ULONG

###################

###### Functions ######

def bcrypt_BCryptAddContextFunction(jitter):
    """
    NTSTATUS BCryptAddContextFunction(
        [CryptConfigTable] dwTable,
        LPCWSTR pszContext,
        [CryptInterface] dwInterface,
        LPCWSTR pszFunction,
        [CryptPriority] dwPosition
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction", "dwPosition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptConfigureContext(jitter):
    """
    NTSTATUS BCryptConfigureContext(
        [CryptConfigTable] dwTable,
        LPCWSTR pszContext,
        PCRYPT_CONTEXT_CONFIG pConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "pConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptConfigureContextFunction(jitter):
    """
    NTSTATUS BCryptConfigureContextFunction(
        [CryptConfigTable] dwTable,
        LPCWSTR pszContext,
        [CryptInterface] dwInterface,
        LPCWSTR pszFunction,
        PCRYPT_CONTEXT_FUNCTION_CONFIG pConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction", "pConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptCreateContext(jitter):
    """
    NTSTATUS BCryptCreateContext(
        [CryptConfigTable] dwTable,
        LPCWSTR pszContext,
        PCRYPT_CONTEXT_CONFIG pConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "pConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDeleteContext(jitter):
    """
    NTSTATUS BCryptDeleteContext(
        [CryptConfigTable] dwTable,
        LPCWSTR pszContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEnumAlgorithms(jitter):
    """
    NTSTATUS BCryptEnumAlgorithms(
        [CryptOperation] dwAlgOperations,
        ULONG* pAlgCount,
        BCRYPT_ALGORITHM_IDENTIFIER** ppAlgList,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwAlgOperations", "pAlgCount", "ppAlgList", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEnumContextFunctionProviders(jitter):
    """
    NTSTATUS BCryptEnumContextFunctionProviders(
        [CryptConfigTable] dwTable,
        LPCWSTR pszContext,
        [CryptInterface] dwInterface,
        LPCWSTR pszFunction,
        ULONG* pcbBuffer,
        PCRYPT_CONTEXT_FUNCTION_PROVIDERS* ppBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEnumContextFunctions(jitter):
    """
    NTSTATUS BCryptEnumContextFunctions(
        [CryptConfigTable] dwTable,
        LPCWSTR pszContext,
        [CryptInterface] dwInterface,
        ULONG* pcbBuffer,
        PCRYPT_CONTEXT_FUNCTIONS* ppBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEnumContexts(jitter):
    """
    NTSTATUS BCryptEnumContexts(
        [CryptConfigTable] dwTable,
        ULONG* pcbBuffer,
        PCRYPT_CONTEXTS* ppBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEnumProviders(jitter):
    """
    NTSTATUS BCryptEnumProviders(
        LPCWSTR pszAlgId,
        ULONG* pImplCount,
        BCRYPT_PROVIDER_NAME** ppImplList,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszAlgId", "pImplCount", "ppImplList", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEnumRegisteredProviders(jitter):
    """
    NTSTATUS BCryptEnumRegisteredProviders(
        ULONG* pcbBuffer,
        PCRYPT_PROVIDERS* ppBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptGetFipsAlgorithmMode(jitter):
    """
    NTSTATUS BCryptGetFipsAlgorithmMode(
        BOOLEAN* pfEnabled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptQueryContextConfiguration(jitter):
    """
    NTSTATUS BCryptQueryContextConfiguration(
        [CryptConfigTable] dwTable,
        LPCWSTR pszContext,
        ULONG* pcbBuffer,
        PCRYPT_CONTEXT_CONFIG* ppBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptQueryContextFunctionConfiguration(jitter):
    """
    NTSTATUS BCryptQueryContextFunctionConfiguration(
        [CryptConfigTable] dwTable,
        LPCWSTR pszContext,
        [CryptInterface] dwInterface,
        LPCWSTR pszFunction,
        ULONG* pcbBuffer,
        PCRYPT_CONTEXT_FUNCTION_CONFIG* ppBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptQueryContextFunctionProperty(jitter):
    """
    NTSTATUS BCryptQueryContextFunctionProperty(
        [CryptConfigTable] dwTable,
        LPCWSTR pszContext,
        [CryptInterface] dwInterface,
        LPCWSTR pszFunction,
        LPCWSTR pszProperty,
        ULONG* pcbValue,
        PUCHAR* ppbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction", "pszProperty", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptQueryProviderRegistration(jitter):
    """
    NTSTATUS BCryptQueryProviderRegistration(
        LPCWSTR pszProvider,
        [CryptMode] dwMode,
        [CryptInterface] dwInterface,
        ULONG* pcbBuffer,
        PCRYPT_PROVIDER_REG* ppBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszProvider", "dwMode", "dwInterface", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptRegisterConfigChangeNotify(jitter):
    """
    NTSTATUS BCryptRegisterConfigChangeNotify(
        HANDLE* phEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptRemoveContextFunction(jitter):
    """
    NTSTATUS BCryptRemoveContextFunction(
        [CryptConfigTable] dwTable,
        LPCWSTR pszContext,
        [CryptInterface] dwInterface,
        LPCWSTR pszFunction
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptResolveProviders(jitter):
    """
    NTSTATUS BCryptResolveProviders(
        LPCWSTR pszContext,
        [CryptInterface] dwInterface,
        LPCWSTR pszFunction,
        LPCWSTR pszProvider,
        [CryptMode] dwMode,
        [CryptEnumFlags] dwFlags,
        ULONG* pcbBuffer,
        PCRYPT_PROVIDER_REFS* ppBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszContext", "dwInterface", "pszFunction", "pszProvider", "dwMode", "dwFlags", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptSetContextFunctionProperty(jitter):
    """
    NTSTATUS BCryptSetContextFunctionProperty(
        [CryptConfigTable] dwTable,
        LPCWSTR pszContext,
        [CryptInterface] dwInterface,
        LPCWSTR pszFunction,
        LPCWSTR pszProperty,
        ULONG cbValue,
        PUCHAR pbValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction", "pszProperty", "cbValue", "pbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptUnregisterConfigChangeNotify(jitter):
    """
    NTSTATUS BCryptUnregisterConfigChangeNotify(
        HANDLE hEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptCloseAlgorithmProvider(jitter):
    """
    NTSTATUS BCryptCloseAlgorithmProvider(
        BCRYPT_ALG_HANDLE hAlgorithm,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptCreateHash(jitter):
    """
    NTSTATUS BCryptCreateHash(
        BCRYPT_ALG_HANDLE hAlgorithm,
        BCRYPT_HASH_HANDLE* phHash,
        PUCHAR pbHashObject,
        ULONG cbHashObject,
        PUCHAR pbSecret,
        ULONG cbSecret,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "phHash", "pbHashObject", "cbHashObject", "pbSecret", "cbSecret", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDecrypt(jitter):
    """
    NTSTATUS BCryptDecrypt(
        BCRYPT_KEY_HANDLE hKey,
        PUCHAR pbInput,
        ULONG cbInput,
        VOID* pPaddingInfo,
        PUCHAR pbIV,
        ULONG cbIV,
        PUCHAR pbOutput,
        ULONG cbOutput,
        ULONG* pcbResult,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pbInput", "cbInput", "pPaddingInfo", "pbIV", "cbIV", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDeriveKey(jitter):
    """
    NTSTATUS BCryptDeriveKey(
        BCRYPT_SECRET_HANDLE hSharedSecret,
        LPCWSTR pwszKDF,
        BCryptBufferDesc* pParameterList,
        PUCHAR pbDerivedKey,
        ULONG cbDerivedKey,
        ULONG* pcbResult,
        [CryptDeriveKeyFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSharedSecret", "pwszKDF", "pParameterList", "pbDerivedKey", "cbDerivedKey", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDestroyHash(jitter):
    """
    NTSTATUS BCryptDestroyHash(
        BCRYPT_HASH_HANDLE hHash
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDestroyKey(jitter):
    """
    NTSTATUS BCryptDestroyKey(
        BCRYPT_KEY_HANDLE hKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDestroySecret(jitter):
    """
    NTSTATUS BCryptDestroySecret(
        BCRYPT_SECRET_HANDLE hSecret
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSecret"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDuplicateHash(jitter):
    """
    NTSTATUS BCryptDuplicateHash(
        BCRYPT_HASH_HANDLE hHash,
        BCRYPT_HASH_HANDLE* phNewHash,
        PUCHAR pbHashObject,
        ULONG cbHashObject,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hHash", "phNewHash", "pbHashObject", "cbHashObject", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDuplicateKey(jitter):
    """
    NTSTATUS BCryptDuplicateKey(
        BCRYPT_KEY_HANDLE hKey,
        BCRYPT_KEY_HANDLE* phNewKey,
        PUCHAR pbKeyObject,
        ULONG cbKeyObject,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "phNewKey", "pbKeyObject", "cbKeyObject", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEncrypt(jitter):
    """
    NTSTATUS BCryptEncrypt(
        BCRYPT_KEY_HANDLE hKey,
        PUCHAR pbInput,
        ULONG cbInput,
        VOID* pPaddingInfo,
        PUCHAR pbIV,
        ULONG cbIV,
        PUCHAR pbOutput,
        ULONG cbOutput,
        ULONG* pcbResult,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pbInput", "cbInput", "pPaddingInfo", "pbIV", "cbIV", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptExportKey(jitter):
    """
    NTSTATUS BCryptExportKey(
        BCRYPT_KEY_HANDLE hKey,
        BCRYPT_KEY_HANDLE hExportKey,
        LPCWSTR pszBlobType,
        PUCHAR pbOutput,
        ULONG cbOutput,
        ULONG* pcbResult,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "hExportKey", "pszBlobType", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptFinalizeKeyPair(jitter):
    """
    NTSTATUS BCryptFinalizeKeyPair(
        BCRYPT_KEY_HANDLE hKey,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptFinishHash(jitter):
    """
    NTSTATUS BCryptFinishHash(
        BCRYPT_HASH_HANDLE hHash,
        PUCHAR pbOutput,
        ULONG cbOutput,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hHash", "pbOutput", "cbOutput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptFreeBuffer(jitter):
    """
    VOID BCryptFreeBuffer(
        PVOID pvBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptGenerateKeyPair(jitter):
    """
    NTSTATUS BCryptGenerateKeyPair(
        BCRYPT_ALG_HANDLE hAlgorithm,
        BCRYPT_KEY_HANDLE* phKey,
        ULONG dwLength,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "phKey", "dwLength", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptGenerateSymmetricKey(jitter):
    """
    NTSTATUS BCryptGenerateSymmetricKey(
        BCRYPT_ALG_HANDLE hAlgorithm,
        BCRYPT_KEY_HANDLE* phKey,
        PUCHAR pbKeyObject,
        ULONG cbKeyObject,
        PUCHAR pbSecret,
        ULONG cbSecret,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "phKey", "pbKeyObject", "cbKeyObject", "pbSecret", "cbSecret", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptGenRandom(jitter):
    """
    NTSTATUS BCryptGenRandom(
        BCRYPT_ALG_HANDLE hAlgorithm,
        PUCHAR pbBuffer,
        ULONG cbBuffer,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "pbBuffer", "cbBuffer", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptGetProperty(jitter):
    """
    NTSTATUS BCryptGetProperty(
        BCRYPT_HANDLE hObject,
        LPCWSTR pszProperty,
        PUCHAR pbOutput,
        ULONG cbOutput,
        ULONG* pcbResult,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hObject", "pszProperty", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptHashData(jitter):
    """
    NTSTATUS BCryptHashData(
        BCRYPT_HASH_HANDLE hHash,
        PUCHAR pbInput,
        ULONG cbInput,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hHash", "pbInput", "cbInput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptImportKey(jitter):
    """
    NTSTATUS BCryptImportKey(
        BCRYPT_ALG_HANDLE hAlgorithm,
        BCRYPT_KEY_HANDLE hImportKey,
        LPCWSTR pszBlobType,
        BCRYPT_KEY_HANDLE* phKey,
        PUCHAR pbKeyObject,
        ULONG cbKeyObject,
        PUCHAR pbInput,
        ULONG cbInput,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "hImportKey", "pszBlobType", "phKey", "pbKeyObject", "cbKeyObject", "pbInput", "cbInput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptImportKeyPair(jitter):
    """
    NTSTATUS BCryptImportKeyPair(
        BCRYPT_ALG_HANDLE hAlgorithm,
        BCRYPT_KEY_HANDLE hImportKey,
        LPCWSTR pszBlobType,
        BCRYPT_KEY_HANDLE* phKey,
        PUCHAR pbInput,
        ULONG cbInput,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "hImportKey", "pszBlobType", "phKey", "pbInput", "cbInput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptKeyDerivation(jitter):
    """
    NTSTATUS BCryptKeyDerivation(
        BCRYPT_KEY_HANDLE hKey,
        BCryptBufferDesc* pParameterList,
        PUCHAR pbDerivedKey,
        ULONG cbDerivedKey,
        ULONG* pcbResult,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pParameterList", "pbDerivedKey", "cbDerivedKey", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptOpenAlgorithmProvider(jitter):
    """
    NTSTATUS BCryptOpenAlgorithmProvider(
        BCRYPT_ALG_HANDLE* phAlgorithm,
        LPCWSTR pszAlgId,
        LPCWSTR pszImplementation,
        [BCryptOpenAlgorithmProviderFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phAlgorithm", "pszAlgId", "pszImplementation", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptSecretAgreement(jitter):
    """
    NTSTATUS BCryptSecretAgreement(
        BCRYPT_KEY_HANDLE hPrivKey,
        BCRYPT_KEY_HANDLE hPubKey,
        BCRYPT_SECRET_HANDLE* phSecret,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrivKey", "hPubKey", "phSecret", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptSetProperty(jitter):
    """
    NTSTATUS BCryptSetProperty(
        BCRYPT_HANDLE hObject,
        LPCWSTR pszProperty,
        PUCHAR pbInput,
        ULONG cbInput,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hObject", "pszProperty", "pbInput", "cbInput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptSignHash(jitter):
    """
    NTSTATUS BCryptSignHash(
        BCRYPT_KEY_HANDLE hKey,
        VOID* pPaddingInfo,
        PBYTE pbInput,
        DWORD cbInput,
        PBYTE pbOutput,
        DWORD cbOutput,
        DWORD* pcbResult,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pPaddingInfo", "pbInput", "cbInput", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptVerifySignature(jitter):
    """
    NTSTATUS BCryptVerifySignature(
        BCRYPT_KEY_HANDLE hKey,
        VOID* pPaddingInfo,
        PUCHAR pbHash,
        ULONG cbHash,
        PUCHAR pbSignature,
        ULONG cbSignature,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pPaddingInfo", "pbHash", "cbHash", "pbSignature", "cbSignature", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDeriveKeyCapi(jitter):
    """
    NTSTATUS BCryptDeriveKeyCapi(
        BCRYPT_HASH_HANDLE hHash,
        BCRYPT_ALG_HANDLE hTargetAlg,
        PUCHAR pbDerivedKey,
        ULONG cbDerivedKey,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hHash", "hTargetAlg", "pbDerivedKey", "cbDerivedKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDeriveKeyPBKDF2(jitter):
    """
    NTSTATUS BCryptDeriveKeyPBKDF2(
        BCRYPT_ALG_HANDLE hPrf,
        PUCHAR pbPassword,
        ULONG cbPassword,
        PUCHAR pbSalt,
        ULONG cbSalt,
        ULONGLONG cIterations,
        PUCHAR pbDerivedKey,
        ULONG cbDerivedKey,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrf", "pbPassword", "cbPassword", "pbSalt", "cbSalt", "cIterations", "pbDerivedKey", "cbDerivedKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
