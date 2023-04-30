
def bcrypt_BCryptAddContextFunction(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptAddContextFunction([CryptConfigTable] dwTable, LPCWSTR pszContext, [CryptInterface] dwInterface, LPCWSTR pszFunction, [CryptPriority] dwPosition)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction", "dwPosition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptConfigureContext(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptConfigureContext([CryptConfigTable] dwTable, LPCWSTR pszContext, PCRYPT_CONTEXT_CONFIG pConfig)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "pConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptConfigureContextFunction(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptConfigureContextFunction([CryptConfigTable] dwTable, LPCWSTR pszContext, [CryptInterface] dwInterface, LPCWSTR pszFunction, PCRYPT_CONTEXT_FUNCTION_CONFIG pConfig)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction", "pConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptCreateContext(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptCreateContext([CryptConfigTable] dwTable, LPCWSTR pszContext, PCRYPT_CONTEXT_CONFIG pConfig)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "pConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDeleteContext(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptDeleteContext([CryptConfigTable] dwTable, LPCWSTR pszContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEnumAlgorithms(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptEnumAlgorithms([CryptOperation] dwAlgOperations, ULONG* pAlgCount, BCRYPT_ALGORITHM_IDENTIFIER** ppAlgList, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwAlgOperations", "pAlgCount", "ppAlgList", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEnumContextFunctionProviders(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptEnumContextFunctionProviders([CryptConfigTable] dwTable, LPCWSTR pszContext, [CryptInterface] dwInterface, LPCWSTR pszFunction, ULONG* pcbBuffer, PCRYPT_CONTEXT_FUNCTION_PROVIDERS* ppBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEnumContextFunctions(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptEnumContextFunctions([CryptConfigTable] dwTable, LPCWSTR pszContext, [CryptInterface] dwInterface, ULONG* pcbBuffer, PCRYPT_CONTEXT_FUNCTIONS* ppBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEnumContexts(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptEnumContexts([CryptConfigTable] dwTable, ULONG* pcbBuffer, PCRYPT_CONTEXTS* ppBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEnumProviders(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptEnumProviders(LPCWSTR pszAlgId, ULONG* pImplCount, BCRYPT_PROVIDER_NAME** ppImplList, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszAlgId", "pImplCount", "ppImplList", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEnumRegisteredProviders(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptEnumRegisteredProviders(ULONG* pcbBuffer, PCRYPT_PROVIDERS* ppBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptGetFipsAlgorithmMode(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptGetFipsAlgorithmMode(BOOLEAN* pfEnabled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptQueryContextConfiguration(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptQueryContextConfiguration([CryptConfigTable] dwTable, LPCWSTR pszContext, ULONG* pcbBuffer, PCRYPT_CONTEXT_CONFIG* ppBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptQueryContextFunctionConfiguration(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptQueryContextFunctionConfiguration([CryptConfigTable] dwTable, LPCWSTR pszContext, [CryptInterface] dwInterface, LPCWSTR pszFunction, ULONG* pcbBuffer, PCRYPT_CONTEXT_FUNCTION_CONFIG* ppBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptQueryContextFunctionProperty(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptQueryContextFunctionProperty([CryptConfigTable] dwTable, LPCWSTR pszContext, [CryptInterface] dwInterface, LPCWSTR pszFunction, LPCWSTR pszProperty, ULONG* pcbValue, PUCHAR* ppbValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction", "pszProperty", "pcbValue", "ppbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptQueryProviderRegistration(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptQueryProviderRegistration(LPCWSTR pszProvider, [CryptMode] dwMode, [CryptInterface] dwInterface, ULONG* pcbBuffer, PCRYPT_PROVIDER_REG* ppBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszProvider", "dwMode", "dwInterface", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptRegisterConfigChangeNotify(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptRegisterConfigChangeNotify(HANDLE* phEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptRemoveContextFunction(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptRemoveContextFunction([CryptConfigTable] dwTable, LPCWSTR pszContext, [CryptInterface] dwInterface, LPCWSTR pszFunction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptResolveProviders(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptResolveProviders(LPCWSTR pszContext, [CryptInterface] dwInterface, LPCWSTR pszFunction, LPCWSTR pszProvider, [CryptMode] dwMode, [CryptEnumFlags] dwFlags, ULONG* pcbBuffer, PCRYPT_PROVIDER_REFS* ppBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszContext", "dwInterface", "pszFunction", "pszProvider", "dwMode", "dwFlags", "pcbBuffer", "ppBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptSetContextFunctionProperty(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptSetContextFunctionProperty([CryptConfigTable] dwTable, LPCWSTR pszContext, [CryptInterface] dwInterface, LPCWSTR pszFunction, LPCWSTR pszProperty, ULONG cbValue, PUCHAR pbValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTable", "pszContext", "dwInterface", "pszFunction", "pszProperty", "cbValue", "pbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptUnregisterConfigChangeNotify(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptUnregisterConfigChangeNotify(HANDLE hEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptCloseAlgorithmProvider(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptCloseAlgorithmProvider(BCRYPT_ALG_HANDLE hAlgorithm, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptCreateHash(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptCreateHash(BCRYPT_ALG_HANDLE hAlgorithm, BCRYPT_HASH_HANDLE* phHash, PUCHAR pbHashObject, ULONG cbHashObject, PUCHAR pbSecret, ULONG cbSecret, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "phHash", "pbHashObject", "cbHashObject", "pbSecret", "cbSecret", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDecrypt(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptDecrypt(BCRYPT_KEY_HANDLE hKey, PUCHAR pbInput, ULONG cbInput, VOID* pPaddingInfo, PUCHAR pbIV, ULONG cbIV, PUCHAR pbOutput, ULONG cbOutput, ULONG* pcbResult, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pbInput", "cbInput", "pPaddingInfo", "pbIV", "cbIV", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDeriveKey(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptDeriveKey(BCRYPT_SECRET_HANDLE hSharedSecret, LPCWSTR pwszKDF, BCryptBufferDesc* pParameterList, PUCHAR pbDerivedKey, ULONG cbDerivedKey, ULONG* pcbResult, [CryptDeriveKeyFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSharedSecret", "pwszKDF", "pParameterList", "pbDerivedKey", "cbDerivedKey", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDestroyHash(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptDestroyHash(BCRYPT_HASH_HANDLE hHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDestroyKey(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptDestroyKey(BCRYPT_KEY_HANDLE hKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDestroySecret(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptDestroySecret(BCRYPT_SECRET_HANDLE hSecret)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSecret"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDuplicateHash(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptDuplicateHash(BCRYPT_HASH_HANDLE hHash, BCRYPT_HASH_HANDLE* phNewHash, PUCHAR pbHashObject, ULONG cbHashObject, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHash", "phNewHash", "pbHashObject", "cbHashObject", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDuplicateKey(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptDuplicateKey(BCRYPT_KEY_HANDLE hKey, BCRYPT_KEY_HANDLE* phNewKey, PUCHAR pbKeyObject, ULONG cbKeyObject, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "phNewKey", "pbKeyObject", "cbKeyObject", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptEncrypt(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptEncrypt(BCRYPT_KEY_HANDLE hKey, PUCHAR pbInput, ULONG cbInput, VOID* pPaddingInfo, PUCHAR pbIV, ULONG cbIV, PUCHAR pbOutput, ULONG cbOutput, ULONG* pcbResult, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pbInput", "cbInput", "pPaddingInfo", "pbIV", "cbIV", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptExportKey(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptExportKey(BCRYPT_KEY_HANDLE hKey, BCRYPT_KEY_HANDLE hExportKey, LPCWSTR pszBlobType, PUCHAR pbOutput, ULONG cbOutput, ULONG* pcbResult, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "hExportKey", "pszBlobType", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptFinalizeKeyPair(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptFinalizeKeyPair(BCRYPT_KEY_HANDLE hKey, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptFinishHash(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptFinishHash(BCRYPT_HASH_HANDLE hHash, PUCHAR pbOutput, ULONG cbOutput, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHash", "pbOutput", "cbOutput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptFreeBuffer(jitter):
    """"
    [Bcrypt.dll] VOID BCryptFreeBuffer(PVOID pvBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptGenerateKeyPair(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptGenerateKeyPair(BCRYPT_ALG_HANDLE hAlgorithm, BCRYPT_KEY_HANDLE* phKey, ULONG dwLength, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "phKey", "dwLength", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptGenerateSymmetricKey(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptGenerateSymmetricKey(BCRYPT_ALG_HANDLE hAlgorithm, BCRYPT_KEY_HANDLE* phKey, PUCHAR pbKeyObject, ULONG cbKeyObject, PUCHAR pbSecret, ULONG cbSecret, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "phKey", "pbKeyObject", "cbKeyObject", "pbSecret", "cbSecret", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptGenRandom(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptGenRandom(BCRYPT_ALG_HANDLE hAlgorithm, PUCHAR pbBuffer, ULONG cbBuffer, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "pbBuffer", "cbBuffer", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptGetProperty(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptGetProperty(BCRYPT_HANDLE hObject, LPCWSTR pszProperty, PUCHAR pbOutput, ULONG cbOutput, ULONG* pcbResult, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hObject", "pszProperty", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptHashData(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptHashData(BCRYPT_HASH_HANDLE hHash, PUCHAR pbInput, ULONG cbInput, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHash", "pbInput", "cbInput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptImportKey(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptImportKey(BCRYPT_ALG_HANDLE hAlgorithm, BCRYPT_KEY_HANDLE hImportKey, LPCWSTR pszBlobType, BCRYPT_KEY_HANDLE* phKey, PUCHAR pbKeyObject, ULONG cbKeyObject, PUCHAR pbInput, ULONG cbInput, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "hImportKey", "pszBlobType", "phKey", "pbKeyObject", "cbKeyObject", "pbInput", "cbInput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptImportKeyPair(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptImportKeyPair(BCRYPT_ALG_HANDLE hAlgorithm, BCRYPT_KEY_HANDLE hImportKey, LPCWSTR pszBlobType, BCRYPT_KEY_HANDLE* phKey, PUCHAR pbInput, ULONG cbInput, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hAlgorithm", "hImportKey", "pszBlobType", "phKey", "pbInput", "cbInput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptKeyDerivation(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptKeyDerivation(BCRYPT_KEY_HANDLE hKey, BCryptBufferDesc* pParameterList, PUCHAR pbDerivedKey, ULONG cbDerivedKey, ULONG* pcbResult, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pParameterList", "pbDerivedKey", "cbDerivedKey", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptOpenAlgorithmProvider(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptOpenAlgorithmProvider(BCRYPT_ALG_HANDLE* phAlgorithm, LPCWSTR pszAlgId, LPCWSTR pszImplementation, [BCryptOpenAlgorithmProviderFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phAlgorithm", "pszAlgId", "pszImplementation", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptSecretAgreement(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptSecretAgreement(BCRYPT_KEY_HANDLE hPrivKey, BCRYPT_KEY_HANDLE hPubKey, BCRYPT_SECRET_HANDLE* phSecret, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrivKey", "hPubKey", "phSecret", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptSetProperty(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptSetProperty(BCRYPT_HANDLE hObject, LPCWSTR pszProperty, PUCHAR pbInput, ULONG cbInput, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hObject", "pszProperty", "pbInput", "cbInput", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptSignHash(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptSignHash(BCRYPT_KEY_HANDLE hKey, VOID* pPaddingInfo, PBYTE pbInput, DWORD cbInput, PBYTE pbOutput, DWORD cbOutput, DWORD* pcbResult, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pPaddingInfo", "pbInput", "cbInput", "pbOutput", "cbOutput", "pcbResult", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptVerifySignature(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptVerifySignature(BCRYPT_KEY_HANDLE hKey, VOID* pPaddingInfo, PUCHAR pbHash, ULONG cbHash, PUCHAR pbSignature, ULONG cbSignature, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pPaddingInfo", "pbHash", "cbHash", "pbSignature", "cbSignature", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDeriveKeyCapi(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptDeriveKeyCapi(BCRYPT_HASH_HANDLE hHash, BCRYPT_ALG_HANDLE hTargetAlg, PUCHAR pbDerivedKey, ULONG cbDerivedKey, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHash", "hTargetAlg", "pbDerivedKey", "cbDerivedKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bcrypt_BCryptDeriveKeyPBKDF2(jitter):
    """"
    [Bcrypt.dll] NTSTATUS BCryptDeriveKeyPBKDF2(BCRYPT_ALG_HANDLE hPrf, PUCHAR pbPassword, ULONG cbPassword, PUCHAR pbSalt, ULONG cbSalt, ULONGLONG cIterations, PUCHAR pbDerivedKey, ULONG cbDerivedKey, ULONG dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrf", "pbPassword", "cbPassword", "pbSalt", "cbSalt", "cIterations", "pbDerivedKey", "cbDerivedKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
