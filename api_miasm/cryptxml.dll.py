
def cryptxml_CryptXmlCreateReference(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlCreateReference(HCRYPTXML hCryptXml, DWORD dwFlags, LPCWSTR wszId, LPCWSTR wszURI, LPCWSTR wszType, const CRYPT_XML_ALGORITHM* pDigestMethod, ULONG cTransform, const CRYPT_XML_ALGORITHM* rgTransform, HCRYPTXML* phReference)
    """
    ret_ad, args = jitter.func_args_stdcall(["hCryptXml", "dwFlags", "wszId", "wszURI", "wszType", "pDigestMethod", "cTransform", "rgTransform", "phReference"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlAddObject(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlAddObject(HCRYPTXML hSignatureOrObject, DWORD dwFlags, const CRYPT_XML_PROPERTY* rgProperty, ULONG cProperty, const PCRYPT_XML_BLOB pEncoded, const CRYPT_XML_OBJECT** ppObject)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSignatureOrObject", "dwFlags", "rgProperty", "cProperty", "pEncoded", "ppObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlClose(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlClose(HCRYPTXML hCryptXml)
    """
    ret_ad, args = jitter.func_args_stdcall(["hCryptXml"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlDigestReference(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlDigestReference(HCRYPTXML hReference, DWORD dwFlags, CRYPT_XML_DATA_PROVIDER* pDataProviderIn)
    """
    ret_ad, args = jitter.func_args_stdcall(["hReference", "dwFlags", "pDataProviderIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlEncode(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlEncode(HCRYPTXML hCryptXml, CRYPT_XML_CHARSET dwCharset, const CRYPT_XML_PROPERTY* rgProperty, ULONG cProperty, void* pvCallbackState, PFN_CRYPT_XML_WRITE_CALLBACK pfnWrite)
    """
    ret_ad, args = jitter.func_args_stdcall(["hCryptXml", "dwCharset", "rgProperty", "cProperty", "pvCallbackState", "pfnWrite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlGetAlgorithmInfo(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlGetAlgorithmInfo(const CRYPT_XML_ALGORITHM* pXmlAlgorithm, DWORD dwFlags, CRYPT_XML_ALGORITHM_INFO** ppAlgInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["pXmlAlgorithm", "dwFlags", "ppAlgInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlGetDocContext(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlGetDocContext(HCRYPTXML hCryptXml, const CRYPT_XML_DOC_CTXT** ppStruct)
    """
    ret_ad, args = jitter.func_args_stdcall(["hCryptXml", "ppStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlGetReference(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlGetReference(HCRYPTXML HCRYPTXML, const CRYPT_XML_REFERENCE** ppStruct)
    """
    ret_ad, args = jitter.func_args_stdcall(["HCRYPTXML", "ppStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlGetSignature(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlGetSignature(HCRYPTXML hCryptXml, const CRYPT_XML_SIGNATURE** ppStruct)
    """
    ret_ad, args = jitter.func_args_stdcall(["hCryptXml", "ppStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlGetStatus(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlGetStatus(HCRYPTXML hCryptXml, CRYPT_XML_STATUS* pStatus)
    """
    ret_ad, args = jitter.func_args_stdcall(["hCryptXml", "pStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlGetTransforms(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlGetTransforms(CRYPT_XML_TRANSFORM_CHAIN_CONFIG** ppConfig)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlImportPublicKey(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlImportPublicKey(DWORD dwFlags, CRYPT_XML_KEY_VALUE* pKeyValue, BCRYPT_KEY_HANDLE* phKey)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pKeyValue", "phKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlOpenToEncode(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlOpenToEncode(CRYPT_XML_TRANSFORM_CHAIN_CONFIG* pConfig, DWORD dwFlags, LPCWSTR wszId, CRYPT_XML_PROPERTY* rgProperty, ULONG cProperty, CRYPT_XML_BLOB* pEncoded, HCRYPTXML* phSignature)
    """
    ret_ad, args = jitter.func_args_stdcall(["pConfig", "dwFlags", "wszId", "rgProperty", "cProperty", "pEncoded", "phSignature"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlOpenToDecode(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlOpenToDecode(CRYPT_XML_TRANSFORM_CHAIN_CONFIG* pConfig, DWORD dwFlags, const CRYPT_XML_PROPERTY* rgProperty, ULONG cProperty, const CRYPT_XML_BLOB* pEncoded, HCRYPTXML phCryptXml)
    """
    ret_ad, args = jitter.func_args_stdcall(["pConfig", "dwFlags", "rgProperty", "cProperty", "pEncoded", "phCryptXml"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlSetHMACSecret(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlSetHMACSecret(HCRYPTXML hSignature, const BYTE* pbSecret, ULONG cbSecret)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSignature", "pbSecret", "cbSecret"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlVerifySignature(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlVerifySignature(HCRYPTXML hSignature, BCRYPT_KEY_HANDLE hKey, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSignature", "hKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlSign(jitter):
    """
    [Cryptxml.dll] HRESULT CryptXmlSign(HCRYPTXML hSignature, HCRYPTPROV_OR_NCRYPT_KEY_HANDLE hKey, DWORD dwKeySpec, DWORD dwFlags, CRYPT_XML_KEYINFO_SPEC dwKeyInfoSpec, const void* pvKeyInfoSpec, const CRYPT_XML_ALGORITHM* pSignatureMethod, const CRYPT_XML_ALGORITHM* pCanonicalization)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSignature", "hKey", "dwKeySpec", "dwFlags", "dwKeyInfoSpec", "pvKeyInfoSpec", "pSignatureMethod", "pCanonicalization"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
