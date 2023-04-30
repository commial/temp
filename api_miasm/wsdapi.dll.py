###### Enums ######
_WSDXML_NODE_TYPE_ = {
    "ElementType": 0,
    "TextType": 1,
}
_WSDXML_NODE_TYPE__INV = {
    0: "ElementType",
    1: "TextType",
}
WSD_CONFIG_PARAM_TYPE = {
    "WSD_CONFIG_MAX_INBOUND_MESSAGE_SIZE": 1,
    "WSD_CONFIG_MAX_OUTBOUND_MESSAGE_SIZE": 2,
    "WSD_SECURITY_SSL_CERT_FOR_CLIENT_AUTH": 3,
    "WSD_SECURITY_SSL_SERVER_CERT_VALIDATION": 4,
    "WSD_SECURITY_SSL_CLIENT_CERT_VALIDATION": 5,
    "WSD_SECURITY_SSL_NEGOTIATE_CLIENT_CERT": 6,
    "WSD_SECURITY_COMPACTSIG_SIGNING_CERT": 7,
    "WSD_SECURITY_COMPACTSIG_VALIDATION": 8,
    "WSD_CONFIG_HOSTING_ADDRESSES": 9,
    "WSD_CONFIG_DEVICE_ADDRESSES": 10,
}
WSD_CONFIG_PARAM_TYPE_INV = {
    1: "WSD_CONFIG_MAX_INBOUND_MESSAGE_SIZE",
    2: "WSD_CONFIG_MAX_OUTBOUND_MESSAGE_SIZE",
    3: "WSD_SECURITY_SSL_CERT_FOR_CLIENT_AUTH",
    4: "WSD_SECURITY_SSL_SERVER_CERT_VALIDATION",
    5: "WSD_SECURITY_SSL_CLIENT_CERT_VALIDATION",
    6: "WSD_SECURITY_SSL_NEGOTIATE_CLIENT_CERT",
    7: "WSD_SECURITY_COMPACTSIG_SIGNING_CERT",
    8: "WSD_SECURITY_COMPACTSIG_VALIDATION",
    9: "WSD_CONFIG_HOSTING_ADDRESSES",
    10: "WSD_CONFIG_DEVICE_ADDRESSES",
}

###################

###### Types ######

class WSD_LOCALIZED_STRING(MemStruct):
    fields = [
        ("lang", const_WCHAR_PTR()),
        ("String", const_WCHAR_PTR()),
    ]

WSD_LOCALIZED_STRING_PTR = Ptr("<I", WSD_LOCALIZED_STRING())

class WSD_LOCALIZED_STRING_LIST(MemStruct):
    fields = [
        ("Next", LPVOID()),
        ("Element", WSD_LOCALIZED_STRING_PTR()),
    ]

WSD_LOCALIZED_STRING_LIST_PTR = Ptr("<I", WSD_LOCALIZED_STRING_LIST())

class WSDXML_NAMESPACE(MemStruct):
    fields = [
        ("Uri", const_WCHAR_PTR()),
        ("PreferredPrefix", const_WCHAR_PTR()),
        ("Names", LPVOID()),
        ("NamesCount", WORD()),
        ("Encoding", WORD()),
    ]

WSDXML_NAMESPACE_PTR = Ptr("<I", WSDXML_NAMESPACE())

class WSDXML_NAME(MemStruct):
    fields = [
        ("Space", WSDXML_NAMESPACE_PTR()),
        ("LocalName", WCHAR_PTR()),
    ]

WSDXML_NAME_PTR = Ptr("<I", WSDXML_NAME())
WSDXML_NAME_PTR_PTR = Ptr("<I", WSDXML_NAME_PTR())

class WSD_SOAP_FAULT_SUBCODE(MemStruct):
    fields = [
        ("Value", WSDXML_NAME_PTR()),
        ("Subcode", LPVOID()),
    ]

WSD_SOAP_FAULT_SUBCODE_PTR = Ptr("<I", WSD_SOAP_FAULT_SUBCODE())
_WSDXML_NODE_TYPE_ = UINT

class WSDXML_NODE(MemStruct):
    fields = [
        ("Type", _WSDXML_NODE_TYPE_()),
        ("Parent", LPVOID()),
        ("Next", LPVOID()),
    ]

WSDXML_NODE_PTR = Ptr("<I", WSDXML_NODE())

class WSDXML_ATTRIBUTE(MemStruct):
    fields = [
        ("Element", LPVOID()),
        ("Next", LPVOID()),
        ("Name", WSDXML_NAME_PTR()),
        ("Value", WCHAR_PTR()),
    ]

WSDXML_ATTRIBUTE_PTR = Ptr("<I", WSDXML_ATTRIBUTE())

class WSDXML_PREFIX_MAPPING(MemStruct):
    fields = [
        ("Refs", DWORD()),
        ("Next", LPVOID()),
        ("Space", WSDXML_NAMESPACE_PTR()),
        ("Prefix", WCHAR_PTR()),
    ]

WSDXML_PREFIX_MAPPING_PTR = Ptr("<I", WSDXML_PREFIX_MAPPING())

class WSDXML_ELEMENT(MemStruct):
    fields = [
        ("Node", WSDXML_NODE()),
        ("Name", WSDXML_NAME_PTR()),
        ("FirstAttribute", WSDXML_ATTRIBUTE_PTR()),
        ("FirstChild", WSDXML_NODE_PTR()),
        ("PrefixMappings", WSDXML_PREFIX_MAPPING_PTR()),
    ]

WSDXML_ELEMENT_PTR = Ptr("<I", WSDXML_ELEMENT())
WSDXML_ELEMENT_PTR_PTR = Ptr("<I", WSDXML_ELEMENT_PTR())
WSD_CONFIG_PARAM_TYPE = UINT

class WSD_CONFIG_PARAM(MemStruct):
    fields = [
        ("configParamType", WSD_CONFIG_PARAM_TYPE()),
        ("pConfigData", PVOID()),
        ("dwConfigDataSize", DWORD()),
    ]

WSD_CONFIG_PARAM_PTR = Ptr("<I", WSD_CONFIG_PARAM())

class WSD_SOAP_FAULT_CODE(MemStruct):
    fields = [
        ("Value", WSDXML_NAME_PTR()),
        ("Subcode", WSD_SOAP_FAULT_SUBCODE_PTR()),
    ]

WSD_SOAP_FAULT_CODE_PTR = Ptr("<I", WSD_SOAP_FAULT_CODE())

class WSD_SOAP_FAULT_REASON(MemStruct):
    fields = [
        ("Text", WSD_LOCALIZED_STRING_LIST_PTR()),
    ]

WSD_SOAP_FAULT_REASON_PTR = Ptr("<I", WSD_SOAP_FAULT_REASON())

class WSD_SOAP_FAULT(MemStruct):
    fields = [
        ("Code", WSD_SOAP_FAULT_CODE_PTR()),
        ("Reason", WSD_SOAP_FAULT_REASON_PTR()),
        ("Node", const_WCHAR_PTR()),
        ("Role", const_WCHAR_PTR()),
        ("Detail", WSDXML_ELEMENT_PTR()),
    ]

WSD_SOAP_FAULT_PTR = Ptr("<I", WSD_SOAP_FAULT())
WSD_SOAP_FAULT_PTR_PTR = Ptr("<I", WSD_SOAP_FAULT_PTR())

###################

###### Functions ######

def wsdapi_WSDAllocateLinkedMemory(jitter):
    """
    void* WSDAllocateLinkedMemory(
        void* pParent,
        size_t cbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pParent", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDAttachLinkedMemory(jitter):
    """
    void WSDAttachLinkedMemory(
        void* pParent,
        void* pChild
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pParent", "pChild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDCreateDeviceHost(jitter):
    """
    HRESULT WSDCreateDeviceHost(
        const WCHAR* pszLocalId,
        IWSDXMLContext* pContext,
        IWSDDeviceHost** ppDeviceHost
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszLocalId", "pContext", "ppDeviceHost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDCreateDeviceHostAdvanced(jitter):
    """
    HRESULT WSDCreateDeviceHostAdvanced(
        const WCHAR* pszLocalId,
        IWSDXMLContext* pContext,
        IWSDAddress** ppHostAddresses,
        DWORD dwHostAddressCount,
        IWSDDeviceHost** ppDeviceHost
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszLocalId", "pContext", "ppHostAddresses", "dwHostAddressCount", "ppDeviceHost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDCreateDeviceProxy(jitter):
    """
    HRESULT WSDCreateDeviceProxy(
        const WCHAR* pszDeviceId,
        const WCHAR* pszLocalId,
        IWSDXMLContext* pContext,
        IWSDDeviceProxy** ppDeviceProxy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceId", "pszLocalId", "pContext", "ppDeviceProxy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDCreateDeviceProxyAdvanced(jitter):
    """
    HRESULT WSDCreateDeviceProxyAdvanced(
        const WCHAR* pszDeviceId,
        IWSDAddress* pDeviceAddress,
        const WCHAR* pszLocalId,
        IWSDXMLContext* pContext,
        IWSDDeviceProxy** ppDeviceProxy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceId", "pDeviceAddress", "pszLocalId", "pContext", "ppDeviceProxy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDCreateDiscoveryProvider(jitter):
    """
    HRESULT WSDCreateDiscoveryProvider(
        IWSDXMLContext* pContext,
        IWSDiscoveryProvider** ppProvider
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pContext", "ppProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDCreateDiscoveryProvider2(jitter):
    """
    HRESULT WSDCreateDiscoveryProvider2(
        IWSDXMLContext* pContext,
        WSD_CONFIG_PARAM* pConfigParams,
        DWORD dwConfigParamCount,
        IWSDiscoveryProvider** ppProvider
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pContext", "pConfigParams", "dwConfigParamCount", "ppProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDCreateDiscoveryPublisher(jitter):
    """
    HRESULT WSDCreateDiscoveryPublisher(
        IWSDXMLContext* pContext,
        IWSDiscoveryPublisher** ppPublisher
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pContext", "ppPublisher"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDCreateDiscoveryPublisher2(jitter):
    """
    HRESULT WSDCreateDiscoveryPublisher2(
        IWSDXMLContext* pContext,
        WSD_CONFIG_PARAM* pConfigParams,
        DWORD dwConfigParamCount,
        IWSDiscoveryPublisher** ppPublisher
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pContext", "pConfigParams", "dwConfigParamCount", "ppPublisher"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDCreateHttpAddress(jitter):
    """
    HRESULT WSDCreateHttpAddress(
        IWSDHttpAddress** ppAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDCreateHttpMessageParameters(jitter):
    """
    HRESULT WSDCreateHttpMessageParameters(
        IWSDHttpMessageParameters** ppTxParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppTxParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDCreateOutboundAttachment(jitter):
    """
    HRESULT WSDCreateOutboundAttachment(
        IWSDOutboundAttachment** attachmentOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["attachmentOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDCreateUdpAddress(jitter):
    """
    HRESULT WSDCreateUdpAddress(
        IWSDUdpAddress** ppAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDCreateUdpMessageParameters(jitter):
    """
    HRESULT WSDCreateUdpMessageParameters(
        IWSDUdpMessageParameters** ppTxParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppTxParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDDetachLinkedMemory(jitter):
    """
    void WSDDetachLinkedMemory(
        void* pVoid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pVoid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDFreeLinkedMemory(jitter):
    """
    void WSDFreeLinkedMemory(
        void* pVoid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pVoid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDGenerateFault(jitter):
    """
    HRESULT WSDGenerateFault(
        LPCWSTR pszCode,
        LPCWSTR pszSubCode,
        LPCWSTR pszReason,
        LPCWSTR pszDetail,
        IWSDXMLContext* pContext,
        WSD_SOAP_FAULT** ppFault
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszCode", "pszSubCode", "pszReason", "pszDetail", "pContext", "ppFault"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDGenerateFaultEx(jitter):
    """
    HRESULT WSDGenerateFaultEx(
        WSDXML_NAME* pCode,
        WSDXML_NAME* pSubCode,
        WSD_LOCALIZED_STRING_LIST* pReasons,
        LPCWSTR pszDetail,
        WSD_SOAP_FAULT** ppFault
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCode", "pSubCode", "pReasons", "pszDetail", "ppFault"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDGetConfigurationOption(jitter):
    """
    HRESULT WSDGetConfigurationOption(
        DWORD dwOption,
        LPVOID pVoid,
        DWORD cbOutBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwOption", "pVoid", "cbOutBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDSetConfigurationOption(jitter):
    """
    HRESULT WSDSetConfigurationOption(
        DWORD dwOption,
        LPVOID pVoid,
        DWORD cbInBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwOption", "pVoid", "cbInBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDUriDecode(jitter):
    """
    HRESULT WSDUriDecode(
        LPCWSTR source,
        DWORD cchSource,
        LPWSTR* destOut,
        DWORD* cchDestOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["source", "cchSource", "destOut", "cchDestOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDUriEncode(jitter):
    """
    HRESULT WSDUriEncode(
        LPCWSTR source,
        DWORD cchSource,
        LPWSTR* destOut,
        DWORD* cchDestOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["source", "cchSource", "destOut", "cchDestOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDXMLAddChild(jitter):
    """
    HRESULT WSDXMLAddChild(
        WSDXML_ELEMENT* pParent,
        WSDXML_ELEMENT* pChild
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pParent", "pChild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDXMLAddSibling(jitter):
    """
    HRESULT WSDXMLAddSibling(
        WSDXML_ELEMENT* pFirst,
        WSDXML_ELEMENT* pSecond
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFirst", "pSecond"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDXMLBuildAnyForSingleElement(jitter):
    """
    HRESULT WSDXMLBuildAnyForSingleElement(
        WSDXML_NAME* pElementName,
        LPCWSTR pszText,
        WSDXML_ELEMENT** ppAny
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pElementName", "pszText", "ppAny"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDXMLCleanupElement(jitter):
    """
    HRESULT WSDXMLCleanupElement(
        WSDXML_ELEMENT* pAny
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAny"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDXMLCreateContext(jitter):
    """
    HRESULT WSDXMLCreateContext(
        IWSDXMLContext** ppContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDXMLGetNameFromBuiltinNamespace(jitter):
    """
    HRESULT WSDXMLGetNameFromBuiltinNamespace(
        LPCWSTR pszNamespace,
        LPCWSTR pszName,
        WSDXML_NAME** ppName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszNamespace", "pszName", "ppName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsdapi_WSDXMLGetValueFromAny(jitter):
    """
    HRESULT WSDXMLGetValueFromAny(
        const WCHAR* pszNamespace,
        const WCHAR* pszName,
        WSDXML_ELEMENT* pAny,
        LPCWSTR* ppszValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszNamespace", "pszName", "pAny", "ppszValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
