DECODING_SOURCE = {
    "DecodingSourceXMLFile": 0,
    "DecodingSourceWbem": 1,
    "DecodingSourceWPP": 2,
}
TDH_IN_TYPE = {
    "TDH_INTYPE_NULL": 0,
    "TDH_INTYPE_UNICODESTRING": 1,
    "TDH_INTYPE_ANSISTRING": 2,
    "TDH_INTYPE_INT8": 3,
    "TDH_INTYPE_UINT8": 4,
    "TDH_INTYPE_INT16": 5,
    "TDH_INTYPE_UINT16": 6,
    "TDH_INTYPE_INT32": 7,
    "TDH_INTYPE_UINT32": 8,
    "TDH_INTYPE_INT64": 9,
    "TDH_INTYPE_UINT64": 10,
    "TDH_INTYPE_FLOAT": 11,
    "TDH_INTYPE_DOUBLE": 12,
    "TDH_INTYPE_BOOLEAN": 13,
    "TDH_INTYPE_BINARY": 14,
    "TDH_INTYPE_GUID": 15,
    "TDH_INTYPE_POINTER": 16,
    "TDH_INTYPE_FILETIME": 17,
    "TDH_INTYPE_SYSTEMTIME": 18,
    "TDH_INTYPE_SID": 19,
    "TDH_INTYPE_HEXINT32": 20,
    "TDH_INTYPE_HEXINT64": 21,
    "TDH_INTYPE_COUNTEDSTRING": 300,
    "TDH_INTYPE_COUNTEDANSISTRING": 301,
    "TDH_INTYPE_REVERSEDCOUNTEDSTRING": 302,
    "TDH_INTYPE_REVERSEDCOUNTEDANSISTRING": 303,
    "TDH_INTYPE_NONNULLTERMINATEDSTRING": 304,
    "TDH_INTYPE_NONNULLTERMINATEDANSISTRING": 305,
    "TDH_INTYPE_UNICODECHAR": 306,
    "TDH_INTYPE_ANSICHAR": 307,
    "TDH_INTYPE_SIZET": 308,
    "TDH_INTYPE_HEXDUMP": 309,
    "TDH_INTYPE_WBEMSID": 310,
}
TDH_OUT_TYPE = {
    "TDH_OUTTYPE_NULL": 0,
    "TDH_OUTTYPE_STRING": 1,
    "TDH_OUTTYPE_DATETIME": 2,
    "TDH_OUTTYPE_BYTE": 3,
    "TDH_OUTTYPE_UNSIGNEDBYTE": 4,
    "TDH_OUTTYPE_SHORT": 5,
    "TDH_OUTTYPE_UNSIGNEDSHORT": 6,
    "TDH_OUTTYPE_INT": 7,
    "TDH_OUTTYPE_UNSIGNEDINT": 8,
    "TDH_OUTTYPE_LONG": 9,
    "TDH_OUTTYPE_UNSIGNEDLONG": 10,
    "TDH_OUTTYPE_FLOAT": 11,
    "TDH_OUTTYPE_DOUBLE": 12,
    "TDH_OUTTYPE_BOOLEAN": 13,
    "TDH_OUTTYPE_GUID": 14,
    "TDH_OUTTYPE_HEXBINARY": 15,
    "TDH_OUTTYPE_HEXINT8": 16,
    "TDH_OUTTYPE_HEXINT16": 17,
    "TDH_OUTTYPE_HEXINT32": 18,
    "TDH_OUTTYPE_HEXINT64": 19,
    "TDH_OUTTYPE_PID": 20,
    "TDH_OUTTYPE_TID": 21,
    "TDH_OUTTYPE_PORT": 22,
    "TDH_OUTTYPE_IPV4": 23,
    "TDH_OUTTYPE_IPV6": 24,
    "TDH_OUTTYPE_SOCKETADDRESS": 25,
    "TDH_OUTTYPE_CIMDATETIME": 26,
    "TDH_OUTTYPE_ETWTIME": 27,
    "TDH_OUTTYPE_XML": 28,
    "TDH_OUTTYPE_ERRORCODE": 29,
    "TDH_OUTTYPE_WIN32ERROR": 30,
    "TDH_OUTTYPE_NTSTATUS": 31,
    "TDH_OUTTYPE_HRESULT": 32,
    "TDH_OUTTYPE_CULTURE_INSENSITIVE_DATETIME": 33,
    "TDH_OUTTYPE_REDUCEDSTRING": 300,
    "TDH_OUTTYPE_NOPRINT": 301,
}
MAP_VALUETYPE = {
    "EVENTMAP_ENTRY_VALUETYPE_ULONG": 0,
    "EVENTMAP_ENTRY_VALUETYPE_STRING": 1,
}
EVENT_FIELD_TYPE = {
    "EventKeywordInformation": 0,
    "EventLevelInformation": 1,
    "EventChannelInformation": 2,
    "EventTaskInformation": 3,
    "EventOpcodeInformation": 4,
}
TDH_CONTEXT_TYPE = {
    "TDH_CONTEXT_WPP_TMFFILE": 0,
    "TDH_CONTEXT_WPP_TMFSEARCHPATH": 1,
    "TDH_CONTEXT_WPP_GMT": 2,
    "TDH_CONTEXT_POINTERSIZE": 3,
}

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
