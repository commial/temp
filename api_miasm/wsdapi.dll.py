
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
