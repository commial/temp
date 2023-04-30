
def wevtapi_EvtOpenSession(jitter):
    """"
    [Wevtapi.dll] EVT_HANDLE EvtOpenSession(EVT_LOGIN_CLASS LoginClass, PVOID Login, DWORD Timeout, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LoginClass", "Login", "Timeout", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtClose(jitter):
    """"
    [Wevtapi.dll] BOOL EvtClose(EVT_HANDLE Object)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetExtendedStatus(jitter):
    """"
    [Wevtapi.dll] BOOL EvtGetExtendedStatus(DWORD BufferSize, LPWSTR Buffer, PDWORD BufferUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BufferSize", "Buffer", "BufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetQueryInfo(jitter):
    """"
    [Wevtapi.dll] BOOL EvtGetQueryInfo(EVT_HANDLE QueryOrSubscription, EVT_QUERY_PROPERTY_ID PropertyId, DWORD PropertyValueBufferSize, PEVT_VARIANT PropertyValueBuffer, PDWORD PropertyValueBufferUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["QueryOrSubscription", "PropertyId", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtQuery(jitter):
    """"
    [Wevtapi.dll] EVT_HANDLE EvtQuery(EVT_HANDLE Session, LPCWSTR Path, LPCWSTR Query, [EvtQueryFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Session", "Path", "Query", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtNext(jitter):
    """"
    [Wevtapi.dll] BOOL EvtNext(EVT_HANDLE ResultSet, DWORD EventArraySize, EVT_HANDLE* EventArray, [WaitTimeout] Timeout, DWORD Flags, PDWORD Returned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ResultSet", "EventArraySize", "EventArray", "Timeout", "Flags", "Returned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtSeek(jitter):
    """"
    [Wevtapi.dll] BOOL EvtSeek(EVT_HANDLE ResultSet, LONGLONG Position, EVT_HANDLE Bookmark, DWORD Timeout, [EvtSeekFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ResultSet", "Position", "Bookmark", "Timeout", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtSubscribe(jitter):
    """"
    [Wevtapi.dll] EVT_HANDLE EvtSubscribe(EVT_HANDLE Session, HANDLE SignalEvent, LPCWSTR ChannelPath, LPCWSTR Query, EVT_HANDLE Bookmark, PVOID context, EVT_SUBSCRIBE_CALLBACK Callback, [EvtSubscribeFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Session", "SignalEvent", "ChannelPath", "Query", "Bookmark", "context", "Callback", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtCreateBookmark(jitter):
    """"
    [Wevtapi.dll] EVT_HANDLE EvtCreateBookmark(LPCWSTR BookmarkXml)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BookmarkXml"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtUpdateBookmark(jitter):
    """"
    [Wevtapi.dll] BOOL EvtUpdateBookmark(EVT_HANDLE Bookmark, EVT_HANDLE Event)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Bookmark", "Event"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetEventInfo(jitter):
    """"
    [Wevtapi.dll] BOOL EvtGetEventInfo(EVT_HANDLE Event, EVT_EVENT_PROPERTY_ID PropertyId, DWORD PropertyValueBufferSize, PEVT_VARIANT PropertyValueBuffer, PDWORD PropertyValueBufferUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Event", "PropertyId", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtCreateRenderContext(jitter):
    """"
    [Wevtapi.dll] EVT_HANDLE EvtCreateRenderContext(DWORD ValuePathsCount, LPCWSTR* ValuePaths, [EvtRenderContextFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ValuePathsCount", "ValuePaths", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtRender(jitter):
    """"
    [Wevtapi.dll] BOOL EvtRender(EVT_HANDLE Context, EVT_HANDLE Fragment, [EvtRenderFlags] Flags, DWORD BufferSize, PVOID Buffer, PDWORD BufferUsed, PDWORD PropertyCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "Fragment", "Flags", "BufferSize", "Buffer", "BufferUsed", "PropertyCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtFormatMessage(jitter):
    """"
    [Wevtapi.dll] BOOL EvtFormatMessage(EVT_HANDLE PublisherMetadata, EVT_HANDLE Event, DWORD MessageId, DWORD ValueCount, PEVT_VARIANT Values, [EvtFormatMessageFlags] Flags, DWORD BufferSize, LPWSTR Buffer, PDWORD BufferUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PublisherMetadata", "Event", "MessageId", "ValueCount", "Values", "Flags", "BufferSize", "Buffer", "BufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtOpenLog(jitter):
    """"
    [Wevtapi.dll] EVT_HANDLE EvtOpenLog(EVT_HANDLE Session, LPCWSTR Path, [EvtOpenFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Session", "Path", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetLogInfo(jitter):
    """"
    [Wevtapi.dll] BOOL EvtGetLogInfo(EVT_HANDLE Log, EVT_LOG_PROPERTY_ID PropertyId, DWORD PropertyValueBufferSize, PEVT_VARIANT PropertyValueBuffer, PDWORD PropertyValueBufferUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Log", "PropertyId", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtClearLog(jitter):
    """"
    [Wevtapi.dll] BOOL EvtClearLog(EVT_HANDLE Session, LPCWSTR ChannelPath, LPCWSTR TargetFilePath, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Session", "ChannelPath", "TargetFilePath", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtExportLog(jitter):
    """"
    [Wevtapi.dll] BOOL EvtExportLog(EVT_HANDLE Session, LPCWSTR Path, LPCWSTR Query, LPCWSTR TargetFilePath, [EvtExportLogFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Session", "Path", "Query", "TargetFilePath", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtArchiveExportedLog(jitter):
    """"
    [Wevtapi.dll] BOOL EvtArchiveExportedLog(EVT_HANDLE Session, LPCWSTR LogFilePath, LCID Locale, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Session", "LogFilePath", "Locale", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtOpenChannelEnum(jitter):
    """"
    [Wevtapi.dll] EVT_HANDLE EvtOpenChannelEnum(EVT_HANDLE Session, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Session", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtNextChannelPath(jitter):
    """"
    [Wevtapi.dll] BOOL EvtNextChannelPath(EVT_HANDLE ChannelEnum, DWORD ChannelPathBufferSize, LPWSTR ChannelPathBuffer, PDWORD ChannelPathBufferUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ChannelEnum", "ChannelPathBufferSize", "ChannelPathBuffer", "ChannelPathBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtOpenChannelConfig(jitter):
    """"
    [Wevtapi.dll] EVT_HANDLE EvtOpenChannelConfig(EVT_HANDLE Session, LPCWSTR ChannelPath, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Session", "ChannelPath", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtSaveChannelConfig(jitter):
    """"
    [Wevtapi.dll] BOOL EvtSaveChannelConfig(EVT_HANDLE ChannelConfig, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ChannelConfig", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtSetChannelConfigProperty(jitter):
    """"
    [Wevtapi.dll] BOOL EvtSetChannelConfigProperty(EVT_HANDLE ChannelConfig, EVT_CHANNEL_CONFIG_PROPERTY_ID PropertyId, DWORD Flags, PEVT_VARIANT PropertyValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ChannelConfig", "PropertyId", "Flags", "PropertyValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetChannelConfigProperty(jitter):
    """"
    [Wevtapi.dll] BOOL EvtGetChannelConfigProperty(EVT_HANDLE ChannelConfig, EVT_CHANNEL_CONFIG_PROPERTY_ID PropertyId, DWORD Flags, DWORD PropertyValueBufferSize, PEVT_VARIANT PropertyValueBuffer, PDWORD PropertyValueBufferUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ChannelConfig", "PropertyId", "Flags", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtNextPublisherId(jitter):
    """"
    [Wevtapi.dll] BOOL EvtNextPublisherId(EVT_HANDLE PublisherEnum, DWORD PublisherIdBufferSize, LPWSTR PublisherIdBuffer, PDWORD PublisherIdBufferUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PublisherEnum", "PublisherIdBufferSize", "PublisherIdBuffer", "PublisherIdBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtOpenPublisherEnum(jitter):
    """"
    [Wevtapi.dll] EVT_HANDLE EvtOpenPublisherEnum(EVT_HANDLE Session, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Session", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtOpenPublisherMetadata(jitter):
    """"
    [Wevtapi.dll] EVT_HANDLE EvtOpenPublisherMetadata(EVT_HANDLE Session, LPCWSTR PublisherIdentity, LPCWSTR LogFilePath, LCID Locale, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Session", "PublisherIdentity", "LogFilePath", "Locale", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetPublisherMetadataProperty(jitter):
    """"
    [Wevtapi.dll] BOOL EvtGetPublisherMetadataProperty(EVT_HANDLE PublisherMetadata, EVT_PUBLISHER_METADATA_PROPERTY_ID PropertyId, DWORD Flags, DWORD PublisherMetadataPropertyBufferSize, PEVT_VARIANT PublisherMetadataPropertyBuffer, PDWORD PublisherMetadataPropertyBufferUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PublisherMetadata", "PropertyId", "Flags", "PublisherMetadataPropertyBufferSize", "PublisherMetadataPropertyBuffer", "PublisherMetadataPropertyBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtOpenEventMetadataEnum(jitter):
    """"
    [Wevtapi.dll] EVT_HANDLE EvtOpenEventMetadataEnum(EVT_HANDLE PublisherMetadata, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PublisherMetadata", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtNextEventMetadata(jitter):
    """"
    [Wevtapi.dll] EVT_HANDLE EvtNextEventMetadata(EVT_HANDLE EventMetadataEnum, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EventMetadataEnum", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetEventMetadataProperty(jitter):
    """"
    [Wevtapi.dll] BOOL EvtGetEventMetadataProperty(EVT_HANDLE EventMetadata, EVT_EVENT_METADATA_PROPERTY_ID PropertyId, DWORD Flags, DWORD EventMetadataPropertyBufferSize, PEVT_VARIANT EventMetadataPropertyBuffer, PDWORD EventMetadataPropertyBufferUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EventMetadata", "PropertyId", "Flags", "EventMetadataPropertyBufferSize", "EventMetadataPropertyBuffer", "EventMetadataPropertyBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetObjectArraySize(jitter):
    """"
    [Wevtapi.dll] BOOL EvtGetObjectArraySize(EVT_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray, PDWORD ObjectArraySize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "ObjectArraySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetObjectArrayProperty(jitter):
    """"
    [Wevtapi.dll] BOOL EvtGetObjectArrayProperty(EVT_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray, DWORD PropertyId, DWORD ArrayIndex, DWORD Flags, DWORD PropertyValueBufferSize, PEVT_VARIANT PropertyValueBuffer, PDWORD PropertyValueBufferUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "PropertyId", "ArrayIndex", "Flags", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
