CRYPT_XML_CHARSET = {
    "CRYPT_XML_CHARSET_AUTO": 0,
    "CRYPT_XML_CHARSET_UTF8": 1,
    "CRYPT_XML_CHARSET_UTF16LE": 2,
    "CRYPT_XML_CHARSET_UTF16BE": 3,
}
CRYPT_XML_CHARSET_INV = {
    0: "CRYPT_XML_CHARSET_AUTO",
    1: "CRYPT_XML_CHARSET_UTF8",
    2: "CRYPT_XML_CHARSET_UTF16LE",
    3: "CRYPT_XML_CHARSET_UTF16BE",
}
_CRYPT_XML_KEY_VALUE_TYPE_ = {
    "CRYPT_XML_KEY_VALUE_TYPE_DSA": 0x00000001,
    "CRYPT_XML_KEY_VALUE_TYPE_RSA": 0x00000002,
    "CRYPT_XML_KEY_VALUE_TYPE_ECDSA": 0x00000003,
    "CRYPT_XML_KEY_VALUE_TYPE_CUSTOM": 0x00000004,
}
_CRYPT_XML_KEY_VALUE_TYPE__INV = {
    0x00000001: "CRYPT_XML_KEY_VALUE_TYPE_DSA",
    0x00000002: "CRYPT_XML_KEY_VALUE_TYPE_RSA",
    0x00000003: "CRYPT_XML_KEY_VALUE_TYPE_ECDSA",
    0x00000004: "CRYPT_XML_KEY_VALUE_TYPE_CUSTOM",
}
_CRYPT_XML_X509DATA_TYPE_ = {
    "CRYPT_XML_X509DATA_TYPE_ISSUER_SERIAL": 0x00000001,
    "CRYPT_XML_X509DATA_TYPE_SKI": 0x00000002,
    "CRYPT_XML_X509DATA_TYPE_SUBJECT_NAME": 0x00000003,
    "CRYPT_XML_X509DATA_TYPE_CERTIFICATE": 0x00000004,
    "CRYPT_XML_X509DATA_TYPE_CRL": 0x00000005,
    "CRYPT_XML_X509DATA_TYPE_CUSTOM": 0x00000006,
}
_CRYPT_XML_X509DATA_TYPE__INV = {
    0x00000001: "CRYPT_XML_X509DATA_TYPE_ISSUER_SERIAL",
    0x00000002: "CRYPT_XML_X509DATA_TYPE_SKI",
    0x00000003: "CRYPT_XML_X509DATA_TYPE_SUBJECT_NAME",
    0x00000004: "CRYPT_XML_X509DATA_TYPE_CERTIFICATE",
    0x00000005: "CRYPT_XML_X509DATA_TYPE_CRL",
    0x00000006: "CRYPT_XML_X509DATA_TYPE_CUSTOM",
}
_CRYPT_XML_KEYINFO_TYPE_ = {
    "CRYPT_XML_KEYINFO_TYPE_KEYNAME": 0x00000001,
    "CRYPT_XML_KEYINFO_TYPE_KEYVALUE": 0x00000002,
    "CRYPT_XML_KEYINFO_TYPE_RETRIEVAL": 0x00000003,
    "CRYPT_XML_KEYINFO_TYPE_X509DATA": 0x00000004,
    "CRYPT_XML_KEYINFO_TYPE_CUSTOM": 0x00000005,
}
_CRYPT_XML_KEYINFO_TYPE__INV = {
    0x00000001: "CRYPT_XML_KEYINFO_TYPE_KEYNAME",
    0x00000002: "CRYPT_XML_KEYINFO_TYPE_KEYVALUE",
    0x00000003: "CRYPT_XML_KEYINFO_TYPE_RETRIEVAL",
    0x00000004: "CRYPT_XML_KEYINFO_TYPE_X509DATA",
    0x00000005: "CRYPT_XML_KEYINFO_TYPE_CUSTOM",
}
CRYPT_XML_PROPERTY_ID = {
    "CRYPT_XML_PROPERTY_MAX_HEAP_SIZE": 1,
    "CRYPT_XML_PROPERTY_SIGNATURE_LOCATION": 2,
    "CRYPT_XML_PROPERTY_MAX_SIGNATURES": 3,
    "CRYPT_XML_PROPERTY_DOC_DECLARATION": 4,
    "CRYPT_XML_PROPERTY_XML_OUTPUT_CHARSET": 5,
}
CRYPT_XML_PROPERTY_ID_INV = {
    1: "CRYPT_XML_PROPERTY_MAX_HEAP_SIZE",
    2: "CRYPT_XML_PROPERTY_SIGNATURE_LOCATION",
    3: "CRYPT_XML_PROPERTY_MAX_SIGNATURES",
    4: "CRYPT_XML_PROPERTY_DOC_DECLARATION",
    5: "CRYPT_XML_PROPERTY_XML_OUTPUT_CHARSET",
}
CRYPT_XML_KEYINFO_SPEC = {
    "CRYPT_XML_KEYINFO_SPEC_NONE": 0,
    "CRYPT_XML_KEYINFO_SPEC_ENCODED": 1,
    "CRYPT_XML_KEYINFO_SPEC_PARAM": 2,
}
CRYPT_XML_KEYINFO_SPEC_INV = {
    0: "CRYPT_XML_KEYINFO_SPEC_NONE",
    1: "CRYPT_XML_KEYINFO_SPEC_ENCODED",
    2: "CRYPT_XML_KEYINFO_SPEC_PARAM",
}

def cryptxml_CryptXmlCreateReference(jitter):
    """
    HRESULT CryptXmlCreateReference(
        HCRYPTXML hCryptXml,
        DWORD dwFlags,
        LPCWSTR wszId,
        LPCWSTR wszURI,
        LPCWSTR wszType,
        const CRYPT_XML_ALGORITHM* pDigestMethod,
        ULONG cTransform,
        const CRYPT_XML_ALGORITHM* rgTransform,
        HCRYPTXML* phReference
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCryptXml", "dwFlags", "wszId", "wszURI", "wszType", "pDigestMethod", "cTransform", "rgTransform", "phReference"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlAddObject(jitter):
    """
    HRESULT CryptXmlAddObject(
        HCRYPTXML hSignatureOrObject,
        DWORD dwFlags,
        const CRYPT_XML_PROPERTY* rgProperty,
        ULONG cProperty,
        const PCRYPT_XML_BLOB pEncoded,
        const CRYPT_XML_OBJECT** ppObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSignatureOrObject", "dwFlags", "rgProperty", "cProperty", "pEncoded", "ppObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlClose(jitter):
    """
    HRESULT CryptXmlClose(
        HCRYPTXML hCryptXml
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCryptXml"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlDigestReference(jitter):
    """
    HRESULT CryptXmlDigestReference(
        HCRYPTXML hReference,
        DWORD dwFlags,
        CRYPT_XML_DATA_PROVIDER* pDataProviderIn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hReference", "dwFlags", "pDataProviderIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlEncode(jitter):
    """
    HRESULT CryptXmlEncode(
        HCRYPTXML hCryptXml,
        CRYPT_XML_CHARSET dwCharset,
        const CRYPT_XML_PROPERTY* rgProperty,
        ULONG cProperty,
        void* pvCallbackState,
        PFN_CRYPT_XML_WRITE_CALLBACK pfnWrite
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCryptXml", "dwCharset", "rgProperty", "cProperty", "pvCallbackState", "pfnWrite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlGetAlgorithmInfo(jitter):
    """
    HRESULT CryptXmlGetAlgorithmInfo(
        const CRYPT_XML_ALGORITHM* pXmlAlgorithm,
        DWORD dwFlags,
        CRYPT_XML_ALGORITHM_INFO** ppAlgInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pXmlAlgorithm", "dwFlags", "ppAlgInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlGetDocContext(jitter):
    """
    HRESULT CryptXmlGetDocContext(
        HCRYPTXML hCryptXml,
        const CRYPT_XML_DOC_CTXT** ppStruct
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCryptXml", "ppStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlGetReference(jitter):
    """
    HRESULT CryptXmlGetReference(
        HCRYPTXML HCRYPTXML,
        const CRYPT_XML_REFERENCE** ppStruct
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HCRYPTXML", "ppStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlGetSignature(jitter):
    """
    HRESULT CryptXmlGetSignature(
        HCRYPTXML hCryptXml,
        const CRYPT_XML_SIGNATURE** ppStruct
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCryptXml", "ppStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlGetStatus(jitter):
    """
    HRESULT CryptXmlGetStatus(
        HCRYPTXML hCryptXml,
        CRYPT_XML_STATUS* pStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCryptXml", "pStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlGetTransforms(jitter):
    """
    HRESULT CryptXmlGetTransforms(
        CRYPT_XML_TRANSFORM_CHAIN_CONFIG** ppConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlImportPublicKey(jitter):
    """
    HRESULT CryptXmlImportPublicKey(
        DWORD dwFlags,
        CRYPT_XML_KEY_VALUE* pKeyValue,
        BCRYPT_KEY_HANDLE* phKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pKeyValue", "phKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlOpenToEncode(jitter):
    """
    HRESULT CryptXmlOpenToEncode(
        CRYPT_XML_TRANSFORM_CHAIN_CONFIG* pConfig,
        DWORD dwFlags,
        LPCWSTR wszId,
        CRYPT_XML_PROPERTY* rgProperty,
        ULONG cProperty,
        CRYPT_XML_BLOB* pEncoded,
        HCRYPTXML* phSignature
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pConfig", "dwFlags", "wszId", "rgProperty", "cProperty", "pEncoded", "phSignature"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlOpenToDecode(jitter):
    """
    HRESULT CryptXmlOpenToDecode(
        CRYPT_XML_TRANSFORM_CHAIN_CONFIG* pConfig,
        DWORD dwFlags,
        const CRYPT_XML_PROPERTY* rgProperty,
        ULONG cProperty,
        const CRYPT_XML_BLOB* pEncoded,
        HCRYPTXML phCryptXml
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pConfig", "dwFlags", "rgProperty", "cProperty", "pEncoded", "phCryptXml"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlSetHMACSecret(jitter):
    """
    HRESULT CryptXmlSetHMACSecret(
        HCRYPTXML hSignature,
        const BYTE* pbSecret,
        ULONG cbSecret
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSignature", "pbSecret", "cbSecret"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlVerifySignature(jitter):
    """
    HRESULT CryptXmlVerifySignature(
        HCRYPTXML hSignature,
        BCRYPT_KEY_HANDLE hKey,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSignature", "hKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptxml_CryptXmlSign(jitter):
    """
    HRESULT CryptXmlSign(
        HCRYPTXML hSignature,
        HCRYPTPROV_OR_NCRYPT_KEY_HANDLE hKey,
        DWORD dwKeySpec,
        DWORD dwFlags,
        CRYPT_XML_KEYINFO_SPEC dwKeyInfoSpec,
        const void* pvKeyInfoSpec,
        const CRYPT_XML_ALGORITHM* pSignatureMethod,
        const CRYPT_XML_ALGORITHM* pCanonicalization
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSignature", "hKey", "dwKeySpec", "dwFlags", "dwKeyInfoSpec", "pvKeyInfoSpec", "pSignatureMethod", "pCanonicalization"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
