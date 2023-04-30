###### Enums ######
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

###################

###### Types ######
HCRYPTXML = LPVOID
HCRYPTXML_PTR = Ptr("<I", HCRYPTXML())
PFN_CRYPT_XML_DATA_PROVIDER_READ = LPVOID
PFN_CRYPT_XML_DATA_PROVIDER_CLOSE = LPVOID
PFN_CRYPT_XML_WRITE_CALLBACK = LPVOID
PFN_CRYPT_XML_CREATE_TRANSFORM = LPVOID

class CRYPT_XML_DATA_BLOB(MemStruct):
    fields = [
        ("cbData", ULONG()),
        # Length is `cbData`
        ("pbData", BYTE_PTR()),
    ]

CRYPT_XML_CHARSET = UINT

class CRYPT_XML_BLOB(MemStruct):
    fields = [
        ("dwCharset", CRYPT_XML_CHARSET()),
        ("cbData", ULONG()),
        # Length is `cbData`
        ("pbData", BYTE_PTR()),
    ]

const_PCRYPT_XML_BLOB = Ptr("<I", CRYPT_XML_BLOB())
const_CRYPT_XML_BLOB_PTR = Ptr("<I", CRYPT_XML_BLOB())
CRYPT_XML_BLOB_PTR = Ptr("<I", CRYPT_XML_BLOB())
_CRYPT_XML_KEY_VALUE_TYPE_ = DWORD

class CRYPT_XML_KEY_DSA_KEY_VALUE(MemStruct):
    fields = [
        ("P", CRYPT_XML_DATA_BLOB()),
        ("Q", CRYPT_XML_DATA_BLOB()),
        ("G", CRYPT_XML_DATA_BLOB()),
        ("Y", CRYPT_XML_DATA_BLOB()),
        ("J", CRYPT_XML_DATA_BLOB()),
        ("Seed", CRYPT_XML_DATA_BLOB()),
        ("Counter", CRYPT_XML_DATA_BLOB()),
    ]


class CRYPT_XML_KEY_RSA_KEY_VALUE(MemStruct):
    fields = [
        ("Modulus", CRYPT_XML_DATA_BLOB()),
        ("Exponent", CRYPT_XML_DATA_BLOB()),
    ]


class CRYPT_XML_KEY_ECDSA_KEY_VALUE(MemStruct):
    fields = [
        ("wszNamedCurve", LPCWSTR()),
        ("X", CRYPT_XML_DATA_BLOB()),
        ("Y", CRYPT_XML_DATA_BLOB()),
        ("ExplicitPara", CRYPT_XML_BLOB()),
    ]

_CRYPT_XML_KEY_VALUE_u_ = Union([
    ("DSAKeyValue", CRYPT_XML_KEY_DSA_KEY_VALUE),
    ("RSAKeyValue", CRYPT_XML_KEY_RSA_KEY_VALUE),
    ("ECDSAKeyValue", CRYPT_XML_KEY_ECDSA_KEY_VALUE),
    ("Custom", CRYPT_XML_BLOB),
])

class CRYPT_XML_KEY_VALUE(MemStruct):
    fields = [
        ("dwType", _CRYPT_XML_KEY_VALUE_TYPE_()),
        (None, _CRYPT_XML_KEY_VALUE_u_()),
    ]

CRYPT_XML_KEY_VALUE_PTR = Ptr("<I", CRYPT_XML_KEY_VALUE())
_CRYPT_XML_X509DATA_TYPE_ = DWORD

class CRYPT_XML_ISSUER_SERIAL(MemStruct):
    fields = [
        ("wszIssuer", LPCWSTR()),
        ("wszSerial", LPCWSTR()),
    ]

_CRYPT_XML_X509DATA_ITEM_u_ = Union([
    ("IssuerSerial", CRYPT_XML_ISSUER_SERIAL),
    ("SKI", CRYPT_XML_DATA_BLOB),
    ("wszSubjectName", LPCWSTR),
    ("Certificate", CRYPT_XML_DATA_BLOB),
    ("CRL", CRYPT_XML_DATA_BLOB),
    ("Custom", CRYPT_XML_BLOB),
])

class CRYPT_XML_X509DATA_ITEM(MemStruct):
    fields = [
        ("dwType", _CRYPT_XML_X509DATA_TYPE_()),
        (None, _CRYPT_XML_X509DATA_ITEM_u_()),
    ]

CRYPT_XML_X509DATA_ITEM_PTR = Ptr("<I", CRYPT_XML_X509DATA_ITEM())

class CRYPT_XML_X509DATA(MemStruct):
    fields = [
        ("cX509Data", UINT()),
        ("rgX509Data", CRYPT_XML_X509DATA_ITEM_PTR()),
    ]

_CRYPT_XML_KEYINFO_TYPE_ = DWORD
_CRYPT_XML_KEY_INFO_ITEM_u_ = Union([
    ("wszKeyName", LPCWSTR),
    ("KeyValue", CRYPT_XML_KEY_VALUE),
    ("RetrievalMethod", CRYPT_XML_BLOB),
    ("X509Data", CRYPT_XML_X509DATA),
    ("Custom", CRYPT_XML_BLOB),
])

class CRYPT_XML_KEY_INFO_ITEM(MemStruct):
    fields = [
        ("dwType", _CRYPT_XML_KEYINFO_TYPE_()),
        (None, _CRYPT_XML_KEY_INFO_ITEM_u_()),
    ]

CRYPT_XML_KEY_INFO_ITEM_PTR = Ptr("<I", CRYPT_XML_KEY_INFO_ITEM())

class CRYPT_XML_ALGORITHM(MemStruct):
    fields = [
        ("cbSize", ULONG()),
        ("wszAlgorithm", LPCWSTR()),
        ("Encoded", CRYPT_XML_BLOB()),
    ]

CRYPT_XML_ALGORITHM_PTR = Ptr("<I", CRYPT_XML_ALGORITHM())
const_CRYPT_XML_ALGORITHM_PTR = Ptr("<I", CRYPT_XML_ALGORITHM())
CRYPT_XML_PROPERTY_ID = UINT

class CRYPT_XML_PROPERTY(MemStruct):
    fields = [
        ("dwPropId", CRYPT_XML_PROPERTY_ID()),
        # Length is `cbValue`
        ("pvValue", const_void_PTR()),
        ("cbValue", ULONG()),
    ]

CRYPT_XML_PROPERTY_PTR = Ptr("<I", CRYPT_XML_PROPERTY())
const_CRYPT_XML_PROPERTY_PTR = CRYPT_XML_PROPERTY_PTR

class CRYPT_XML_REFERENCE(MemStruct):
    fields = [
        ("cbSize", ULONG()),
        ("hReference", HCRYPTXML()),
        ("wszId", LPCWSTR()),
        ("wszUri", LPCWSTR()),
        ("wszType", LPCWSTR()),
        ("DigestMethod", CRYPT_XML_ALGORITHM()),
        ("DigestValue", CRYPT_DATA_BLOB()),
        ("cTransform", ULONG()),
        ("rgTransform", CRYPT_XML_ALGORITHM_PTR()),
    ]

PCRYPT_XML_REFERENCE = Ptr("<I", CRYPT_XML_REFERENCE())
PCRYPT_XML_REFERENCE_PTR = Ptr("<I", PCRYPT_XML_REFERENCE())
CRYPT_XML_REFERENCE_PTR = Ptr("<I", CRYPT_XML_REFERENCE())
const_CRYPT_XML_REFERENCE_PTR_PTR = Ptr("<I", CRYPT_XML_REFERENCE_PTR())

class CRYPT_XML_REFERENCES(MemStruct):
    fields = [
        ("cReference", ULONG()),
        ("rgpReference", PCRYPT_XML_REFERENCE_PTR()),
    ]


class CRYPT_XML_OBJECT(MemStruct):
    fields = [
        ("cbSize", ULONG()),
        ("hObject", HCRYPTXML()),
        ("wszId", LPCWSTR()),
        ("wszMimeType", LPCWSTR()),
        ("wszEncoding", LPCWSTR()),
        ("Manifest", CRYPT_XML_REFERENCES()),
        ("Encoded", CRYPT_XML_BLOB()),
    ]

CRYPT_XML_OBJECT_PTR = Ptr("<I", CRYPT_XML_OBJECT())
PCRYPT_XML_OBJECT = Ptr("<I", CRYPT_XML_OBJECT())
PCRYPT_XML_OBJECT_PTR = Ptr("<I", PCRYPT_XML_OBJECT())
const_CRYPT_XML_OBJECT_PTR_PTR = Ptr("<I", CRYPT_XML_OBJECT_PTR())

class CRYPT_XML_DATA_PROVIDER(MemStruct):
    fields = [
        ("pvCallbackState", void_PTR()),
        ("cbBufferSize", ULONG()),
        ("pfnRead", PFN_CRYPT_XML_DATA_PROVIDER_READ()),
        ("pfnClose", PFN_CRYPT_XML_DATA_PROVIDER_CLOSE()),
    ]

CRYPT_XML_DATA_PROVIDER_PTR = Ptr("<I", CRYPT_XML_DATA_PROVIDER())

class CRYPT_XML_ALGORITHM_INFO(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("wszAlgorithmURI", WCHAR_PTR()),
        ("wszName", WCHAR_PTR()),
        ("dwGroupId", DWORD()),
        ("wszCNGAlgid", WCHAR_PTR()),
        ("wszCNGExtraAlgid", WCHAR_PTR()),
        ("dwSignFlags", DWORD()),
        ("dwVerifyFlags", DWORD()),
        ("pvPaddingInfo", void_PTR()),
        ("pvExtraInfo", void_PTR()),
    ]

CRYPT_XML_ALGORITHM_INFO_PTR = Ptr("<I", CRYPT_XML_ALGORITHM_INFO())
CRYPT_XML_ALGORITHM_INFO_PTR_PTR = Ptr("<I", CRYPT_XML_ALGORITHM_INFO_PTR())

class CRYPT_XML_TRANSFORM_INFO(MemStruct):
    fields = [
        ("cbSize", ULONG()),
        ("wszAlgorithm", LPCWSTR()),
        ("cbBufferSize", ULONG()),
        ("dwFlags", DWORD()),
        ("pfnCreateTransform", PFN_CRYPT_XML_CREATE_TRANSFORM()),
    ]

PCRYPT_XML_TRANSFORM_INFO = Ptr("<I", CRYPT_XML_TRANSFORM_INFO())
PCRYPT_XML_TRANSFORM_INFO_PTR = Ptr("<I", PCRYPT_XML_TRANSFORM_INFO())

class CRYPT_XML_TRANSFORM_CHAIN_CONFIG(MemStruct):
    fields = [
        ("cbSize", ULONG()),
        ("cTransformInfo", ULONG()),
        ("rgpTransformInfo", PCRYPT_XML_TRANSFORM_INFO_PTR()),
    ]

CRYPT_XML_TRANSFORM_CHAIN_CONFIG_PTR = Ptr("<I", CRYPT_XML_TRANSFORM_CHAIN_CONFIG())
CRYPT_XML_TRANSFORM_CHAIN_CONFIG_PTR_PTR = Ptr("<I", CRYPT_XML_TRANSFORM_CHAIN_CONFIG_PTR())

class CRYPT_XML_SIGNED_INFO(MemStruct):
    fields = [
        ("cbSize", ULONG()),
        ("wszId", LPCWSTR()),
        ("Canonicalization", CRYPT_XML_ALGORITHM()),
        ("SignatureMethod", CRYPT_XML_ALGORITHM()),
        ("cReference", ULONG()),
        ("rgpReference", PCRYPT_XML_REFERENCE_PTR()),
        ("Encoded", CRYPT_XML_BLOB()),
    ]


class CRYPT_XML_KEY_INFO(MemStruct):
    fields = [
        ("cbSize", ULONG()),
        ("wszId", LPCWSTR()),
        ("cKeyInfo", UINT()),
        ("rgKeyInfo", CRYPT_XML_KEY_INFO_ITEM_PTR()),
        ("hVerifyKey", BCRYPT_KEY_HANDLE()),
    ]

CRYPT_XML_KEY_INFO_PTR = Ptr("<I", CRYPT_XML_KEY_INFO())

class CRYPT_XML_SIGNATURE(MemStruct):
    fields = [
        ("cbSize", ULONG()),
        ("hSignature", HCRYPTXML()),
        ("wszId", LPCWSTR()),
        ("SignedInfo", CRYPT_XML_SIGNED_INFO()),
        ("SignatureValue", CRYPT_DATA_BLOB()),
        ("pKeyInfo", CRYPT_XML_KEY_INFO_PTR()),
        ("cObject", ULONG()),
        ("rgpObject", PCRYPT_XML_OBJECT_PTR()),
    ]

PCRYPT_XML_SIGNATURE = Ptr("<I", CRYPT_XML_SIGNATURE())
PCRYPT_XML_SIGNATURE_PTR = Ptr("<I", PCRYPT_XML_SIGNATURE())
const_CRYPT_XML_SIGNATURE_PTR_PTR = Ptr("<I", PCRYPT_XML_SIGNATURE())

class CRYPT_XML_DOC_CTXT(MemStruct):
    fields = [
        ("cbSize", ULONG()),
        ("hDocCtxt", HCRYPTXML()),
        ("pTransformsConfig", CRYPT_XML_TRANSFORM_CHAIN_CONFIG_PTR()),
        ("cSignature", ULONG()),
        ("rgpSignature", PCRYPT_XML_SIGNATURE_PTR()),
    ]

CRYPT_XML_DOC_CTXT_PTR = Ptr("<I", CRYPT_XML_DOC_CTXT())
const_CRYPT_XML_DOC_CTXT_PTR_PTR = Ptr("<I", CRYPT_XML_DOC_CTXT_PTR())

class CRYPT_XML_STATUS(MemStruct):
    fields = [
        ("cbSize", ULONG()),
        ("dwErrorStatus", DWORD()),
        ("dwInfoStatus", DWORD()),
    ]

CRYPT_XML_STATUS_PTR = Ptr("<I", CRYPT_XML_STATUS())
CRYPT_XML_KEYINFO_SPEC = UINT

###################

###### Functions ######

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
