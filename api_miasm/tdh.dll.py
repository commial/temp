
def tdh_TdhCloseDecodingHandle(jitter):
    """
    [ERROR_CODE_ULONG] TdhCloseDecodingHandle(
        TDH_HANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhEnumerateProviderFieldInformation(jitter):
    """
    [ERROR_CODE_ULONG] TdhEnumerateProviderFieldInformation(
        LPGUID pGuid,
        EVENT_FIELD_TYPE EventFieldType,
        PPROVIDER_FIELD_INFOARRAY pBuffer,
        ULONG* pBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pGuid", "EventFieldType", "pBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhEnumerateProviderFilters(jitter):
    """
    [ERROR_CODE_ULONG] TdhEnumerateProviderFilters(
        LPGUID pGuid,
        ULONG TdhContextCount,
        PTDH_CONTEXT pTdhContext,
        ULONG* FilterCount,
        PPROVIDER_FILTER_INFO* pBuffer,
        ULONG* pBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pGuid", "TdhContextCount", "pTdhContext", "FilterCount", "pBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhEnumerateProviders(jitter):
    """
    [ERROR_CODE_ULONG] TdhEnumerateProviders(
        PPROVIDER_ENUMERATION_INFO pBuffer,
        ULONG* pBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhFormatProperty(jitter):
    """
    [ERROR_CODE_ULONG] TdhFormatProperty(
        PTRACE_EVENT_INFO EventInfo,
        PEVENT_MAP_INFO MapInfo,
        ULONG PointerSize,
        USHORT PropertyInType,
        USHORT PropertyOutType,
        USHORT PropertyLength,
        USHORT UserDataLength,
        PBYTE UserData,
        PULONG BufferSize,
        PWCHAR Buffer,
        PUSHORT UserDataConsumed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventInfo", "MapInfo", "PointerSize", "PropertyInType", "PropertyOutType", "PropertyLength", "UserDataLength", "UserData", "BufferSize", "Buffer", "UserDataConsumed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetDecodingParameter(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetDecodingParameter(
        TDH_HANDLE Handle,
        PTDH_CONTEXT TdhContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "TdhContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetEventInformation(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetEventInformation(
        PEVENT_RECORD pEvent,
        ULONG TdhContextCount,
        PTDH_CONTEXT pTdhContext,
        PTRACE_EVENT_INFO pBuffer,
        ULONG* pBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pEvent", "TdhContextCount", "pTdhContext", "pBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetEventMapInformation(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetEventMapInformation(
        PEVENT_RECORD pEvent,
        LPWSTR pMapName,
        PEVENT_MAP_INFO pBuffer,
        ULONG* pBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pEvent", "pMapName", "pBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetPropertySize(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetPropertySize(
        PEVENT_RECORD pEvent,
        ULONG TdhContextCount,
        PTDH_CONTEXT pTdhContext,
        ULONG PropertyDataCount,
        PPROPERTY_DATA_DESCRIPTOR pPropertyData,
        ULONG* pPropertySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pEvent", "TdhContextCount", "pTdhContext", "PropertyDataCount", "pPropertyData", "pPropertySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetProperty(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetProperty(
        PEVENT_RECORD pEvent,
        ULONG TdhContextCount,
        PTDH_CONTEXT pTdhContext,
        ULONG PropertyDataCount,
        PPROPERTY_DATA_DESCRIPTOR pPropertyData,
        ULONG BufferSize,
        PBYTE pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pEvent", "TdhContextCount", "pTdhContext", "PropertyDataCount", "pPropertyData", "BufferSize", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetWppMessage(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetWppMessage(
        TDH_HANDLE Handle,
        PEVENT_RECORD EventRecord,
        PULONG BufferSize,
        PBYTE Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "EventRecord", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetWppProperty(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetWppProperty(
        TDH_HANDLE Handle,
        PEVENT_RECORD EventRecord,
        PWSTR PropertyName,
        PULONG BufferSize,
        PBYTE Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "EventRecord", "PropertyName", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhLoadManifest(jitter):
    """
    [ERROR_CODE_ULONG] TdhLoadManifest(
        PWSTR Manifest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Manifest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhLoadManifestFromBinary(jitter):
    """
    [ERROR_CODE_ULONG] TdhLoadManifestFromBinary(
        PWSTR BinaryPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BinaryPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhOpenDecodingHandle(jitter):
    """
    [ERROR_CODE_ULONG] TdhOpenDecodingHandle(
        PTDH_HANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhQueryProviderFieldInformation(jitter):
    """
    [ERROR_CODE_ULONG] TdhQueryProviderFieldInformation(
        LPGUID pGuid,
        ULONGLONG EventFieldValue,
        EVENT_FIELD_TYPE EventFieldType,
        PPROVIDER_FIELD_INFOARRAY pBuffer,
        ULONG* pBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pGuid", "EventFieldValue", "EventFieldType", "pBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhSetDecodingParameter(jitter):
    """
    [ERROR_CODE_ULONG] TdhSetDecodingParameter(
        TDH_HANDLE Handle,
        PTDH_CONTEXT TdhContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "TdhContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhUnloadManifest(jitter):
    """
    [ERROR_CODE_ULONG] TdhUnloadManifest(
        PWSTR Manifest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Manifest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
