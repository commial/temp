EVT_CHANNEL_CONFIG_PROPERTY_ID = {
    "EvtChannelConfigEnabled": 0,
    "EvtChannelConfigIsolation": 1,
    "EvtChannelConfigType": 2,
    "EvtChannelConfigOwningPublisher": 3,
    "EvtChannelConfigClassicEventlog": 4,
    "EvtChannelConfigAccess": 5,
    "EvtChannelLoggingConfigRetention": 6,
    "EvtChannelLoggingConfigAutoBackup": 7,
    "EvtChannelLoggingConfigMaxSize": 8,
    "EvtChannelLoggingConfigLogFilePath": 9,
    "EvtChannelPublishingConfigLevel": 10,
    "EvtChannelPublishingConfigKeywords": 11,
    "EvtChannelPublishingConfigControlGuid": 12,
    "EvtChannelPublishingConfigBufferSize": 13,
    "EvtChannelPublishingConfigMinBuffers": 14,
    "EvtChannelPublishingConfigMaxBuffers": 15,
    "EvtChannelPublishingConfigLatency": 16,
    "EvtChannelPublishingConfigClockType": 17,
    "EvtChannelPublishingConfigSidType": 18,
    "EvtChannelPublisherList": 19,
    "EvtChannelPublishingConfigFileMax": 20,
}
EVT_CHANNEL_CONFIG_PROPERTY_ID_INV = {
    0: "EvtChannelConfigEnabled",
    1: "EvtChannelConfigIsolation",
    2: "EvtChannelConfigType",
    3: "EvtChannelConfigOwningPublisher",
    4: "EvtChannelConfigClassicEventlog",
    5: "EvtChannelConfigAccess",
    6: "EvtChannelLoggingConfigRetention",
    7: "EvtChannelLoggingConfigAutoBackup",
    8: "EvtChannelLoggingConfigMaxSize",
    9: "EvtChannelLoggingConfigLogFilePath",
    10: "EvtChannelPublishingConfigLevel",
    11: "EvtChannelPublishingConfigKeywords",
    12: "EvtChannelPublishingConfigControlGuid",
    13: "EvtChannelPublishingConfigBufferSize",
    14: "EvtChannelPublishingConfigMinBuffers",
    15: "EvtChannelPublishingConfigMaxBuffers",
    16: "EvtChannelPublishingConfigLatency",
    17: "EvtChannelPublishingConfigClockType",
    18: "EvtChannelPublishingConfigSidType",
    19: "EvtChannelPublisherList",
    20: "EvtChannelPublishingConfigFileMax",
}
EVT_PUBLISHER_METADATA_PROPERTY_ID = {
    "EvtPublisherMetadataPublisherGuid": 0,
    "EvtPublisherMetadataResourceFilePath": 1,
    "EvtPublisherMetadataParameterFilePath": 2,
    "EvtPublisherMetadataMessageFilePath": 3,
    "EvtPublisherMetadataHelpLink": 4,
    "EvtPublisherMetadataPublisherMessageID": 5,
    "EvtPublisherMetadataChannelReferences": 6,
    "EvtPublisherMetadataChannelReferencePath": 7,
    "EvtPublisherMetadataChannelReferenceIndex": 8,
    "EvtPublisherMetadataChannelReferenceID": 9,
    "EvtPublisherMetadataChannelReferenceFlags": 10,
    "EvtPublisherMetadataChannelReferenceMessageID": 11,
    "EvtPublisherMetadataLevels": 12,
    "EvtPublisherMetadataLevelName": 13,
    "EvtPublisherMetadataLevelValue": 14,
    "EvtPublisherMetadataLevelMessageID": 15,
    "EvtPublisherMetadataTasks": 16,
    "EvtPublisherMetadataTaskName": 17,
    "EvtPublisherMetadataTaskEventGuid": 18,
    "EvtPublisherMetadataTaskValue": 19,
    "EvtPublisherMetadataTaskMessageID": 20,
    "EvtPublisherMetadataOpcodes": 21,
    "EvtPublisherMetadataOpcodeName": 22,
    "EvtPublisherMetadataOpcodeValue": 23,
    "EvtPublisherMetadataOpcodeMessageID": 24,
    "EvtPublisherMetadataKeywords": 25,
    "EvtPublisherMetadataKeywordName": 26,
    "EvtPublisherMetadataKeywordValue": 27,
    "EvtPublisherMetadataKeywordMessageID": 28,
}
EVT_PUBLISHER_METADATA_PROPERTY_ID_INV = {
    0: "EvtPublisherMetadataPublisherGuid",
    1: "EvtPublisherMetadataResourceFilePath",
    2: "EvtPublisherMetadataParameterFilePath",
    3: "EvtPublisherMetadataMessageFilePath",
    4: "EvtPublisherMetadataHelpLink",
    5: "EvtPublisherMetadataPublisherMessageID",
    6: "EvtPublisherMetadataChannelReferences",
    7: "EvtPublisherMetadataChannelReferencePath",
    8: "EvtPublisherMetadataChannelReferenceIndex",
    9: "EvtPublisherMetadataChannelReferenceID",
    10: "EvtPublisherMetadataChannelReferenceFlags",
    11: "EvtPublisherMetadataChannelReferenceMessageID",
    12: "EvtPublisherMetadataLevels",
    13: "EvtPublisherMetadataLevelName",
    14: "EvtPublisherMetadataLevelValue",
    15: "EvtPublisherMetadataLevelMessageID",
    16: "EvtPublisherMetadataTasks",
    17: "EvtPublisherMetadataTaskName",
    18: "EvtPublisherMetadataTaskEventGuid",
    19: "EvtPublisherMetadataTaskValue",
    20: "EvtPublisherMetadataTaskMessageID",
    21: "EvtPublisherMetadataOpcodes",
    22: "EvtPublisherMetadataOpcodeName",
    23: "EvtPublisherMetadataOpcodeValue",
    24: "EvtPublisherMetadataOpcodeMessageID",
    25: "EvtPublisherMetadataKeywords",
    26: "EvtPublisherMetadataKeywordName",
    27: "EvtPublisherMetadataKeywordValue",
    28: "EvtPublisherMetadataKeywordMessageID",
}
_EvtFormatMessageFlags_ = {
    "EvtFormatMessageEvent": 1,
    "EvtFormatMessageLevel": 2,
    "EvtFormatMessageTask": 3,
    "EvtFormatMessageOpcode": 4,
    "EvtFormatMessageKeyword": 5,
    "EvtFormatMessageChannel": 6,
    "EvtFormatMessageProvider": 7,
    "EvtFormatMessageId": 8,
    "EvtFormatMessageXml": 9,
}
_EvtFormatMessageFlags__INV = {
    1: "EvtFormatMessageEvent",
    2: "EvtFormatMessageLevel",
    3: "EvtFormatMessageTask",
    4: "EvtFormatMessageOpcode",
    5: "EvtFormatMessageKeyword",
    6: "EvtFormatMessageChannel",
    7: "EvtFormatMessageProvider",
    8: "EvtFormatMessageId",
    9: "EvtFormatMessageXml",
}
EVT_LOG_PROPERTY_ID = {
    "EvtLogCreationTime": 0,
    "EvtLogLastAccessTime": 1,
    "EvtLogLastWriteTime": 2,
    "EvtLogFileSize": 3,
    "EvtLogAttributes": 4,
    "EvtLogNumberOfLogRecords": 5,
    "EvtLogOldestRecordNumber": 6,
    "EvtLogFull": 7,
}
EVT_LOG_PROPERTY_ID_INV = {
    0: "EvtLogCreationTime",
    1: "EvtLogLastAccessTime",
    2: "EvtLogLastWriteTime",
    3: "EvtLogFileSize",
    4: "EvtLogAttributes",
    5: "EvtLogNumberOfLogRecords",
    6: "EvtLogOldestRecordNumber",
    7: "EvtLogFull",
}
_EvtRenderFlags_ = {
    "EvtRenderEventValues": 0,
    "EvtRenderEventXml": 1,
    "EvtRenderBookmark": 2,
}
_EvtRenderFlags__INV = {
    0: "EvtRenderEventValues",
    1: "EvtRenderEventXml",
    2: "EvtRenderBookmark",
}
_EvtRenderContextFlags_ = {
    "EvtRenderContextValues": 0,
    "EvtRenderContextSystem": 1,
    "EvtRenderContextUser": 2,
}
_EvtRenderContextFlags__INV = {
    0: "EvtRenderContextValues",
    1: "EvtRenderContextSystem",
    2: "EvtRenderContextUser",
}
EVT_QUERY_PROPERTY_ID = {
    "EvtQueryNames": 0,
    "EvtQueryStatuses": 1,
}
EVT_QUERY_PROPERTY_ID_INV = {
    0: "EvtQueryNames",
    1: "EvtQueryStatuses",
}
EVT_EVENT_PROPERTY_ID = {
    "EvtEventQueryIDs": 0,
    "EvtEventPath": 1,
}
EVT_EVENT_PROPERTY_ID_INV = {
    0: "EvtEventQueryIDs",
    1: "EvtEventPath",
}
EVT_LOGIN_CLASS = {
    "EvtRpcLogin": 1,
}
EVT_LOGIN_CLASS_INV = {
    1: "EvtRpcLogin",
}
EVT_EVENT_METADATA_PROPERTY_ID = {
    "EventMetadataEventID": 0,
    "EventMetadataEventVersion": 1,
    "EventMetadataEventChannel": 2,
    "EventMetadataEventLevel": 3,
    "EventMetadataEventOpcode": 4,
    "EventMetadataEventTask": 5,
    "EventMetadataEventKeyword": 6,
    "EventMetadataEventMessageID": 7,
    "EventMetadataEventTemplate": 8,
}
EVT_EVENT_METADATA_PROPERTY_ID_INV = {
    0: "EventMetadataEventID",
    1: "EventMetadataEventVersion",
    2: "EventMetadataEventChannel",
    3: "EventMetadataEventLevel",
    4: "EventMetadataEventOpcode",
    5: "EventMetadataEventTask",
    6: "EventMetadataEventKeyword",
    7: "EventMetadataEventMessageID",
    8: "EventMetadataEventTemplate",
}

def wevtapi_EvtOpenSession(jitter):
    """
    EVT_HANDLE EvtOpenSession(
        EVT_LOGIN_CLASS LoginClass,
        PVOID Login,
        DWORD Timeout,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LoginClass", "Login", "Timeout", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtClose(jitter):
    """
    BOOL EvtClose(
        EVT_HANDLE Object
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetExtendedStatus(jitter):
    """
    BOOL EvtGetExtendedStatus(
        DWORD BufferSize,
        LPWSTR Buffer,
        PDWORD BufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferSize", "Buffer", "BufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetQueryInfo(jitter):
    """
    BOOL EvtGetQueryInfo(
        EVT_HANDLE QueryOrSubscription,
        EVT_QUERY_PROPERTY_ID PropertyId,
        DWORD PropertyValueBufferSize,
        PEVT_VARIANT PropertyValueBuffer,
        PDWORD PropertyValueBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["QueryOrSubscription", "PropertyId", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtQuery(jitter):
    """
    EVT_HANDLE EvtQuery(
        EVT_HANDLE Session,
        LPCWSTR Path,
        LPCWSTR Query,
        [EvtQueryFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Session", "Path", "Query", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtNext(jitter):
    """
    BOOL EvtNext(
        EVT_HANDLE ResultSet,
        DWORD EventArraySize,
        EVT_HANDLE* EventArray,
        [WaitTimeout] Timeout,
        DWORD Flags,
        PDWORD Returned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ResultSet", "EventArraySize", "EventArray", "Timeout", "Flags", "Returned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtSeek(jitter):
    """
    BOOL EvtSeek(
        EVT_HANDLE ResultSet,
        LONGLONG Position,
        EVT_HANDLE Bookmark,
        DWORD Timeout,
        [EvtSeekFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ResultSet", "Position", "Bookmark", "Timeout", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtSubscribe(jitter):
    """
    EVT_HANDLE EvtSubscribe(
        EVT_HANDLE Session,
        HANDLE SignalEvent,
        LPCWSTR ChannelPath,
        LPCWSTR Query,
        EVT_HANDLE Bookmark,
        PVOID context,
        EVT_SUBSCRIBE_CALLBACK Callback,
        [EvtSubscribeFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Session", "SignalEvent", "ChannelPath", "Query", "Bookmark", "context", "Callback", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtCreateBookmark(jitter):
    """
    EVT_HANDLE EvtCreateBookmark(
        LPCWSTR BookmarkXml
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BookmarkXml"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtUpdateBookmark(jitter):
    """
    BOOL EvtUpdateBookmark(
        EVT_HANDLE Bookmark,
        EVT_HANDLE Event
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Bookmark", "Event"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetEventInfo(jitter):
    """
    BOOL EvtGetEventInfo(
        EVT_HANDLE Event,
        EVT_EVENT_PROPERTY_ID PropertyId,
        DWORD PropertyValueBufferSize,
        PEVT_VARIANT PropertyValueBuffer,
        PDWORD PropertyValueBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Event", "PropertyId", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtCreateRenderContext(jitter):
    """
    EVT_HANDLE EvtCreateRenderContext(
        DWORD ValuePathsCount,
        LPCWSTR* ValuePaths,
        [EvtRenderContextFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ValuePathsCount", "ValuePaths", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtRender(jitter):
    """
    BOOL EvtRender(
        EVT_HANDLE Context,
        EVT_HANDLE Fragment,
        [EvtRenderFlags] Flags,
        DWORD BufferSize,
        PVOID Buffer,
        PDWORD BufferUsed,
        PDWORD PropertyCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context", "Fragment", "Flags", "BufferSize", "Buffer", "BufferUsed", "PropertyCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtFormatMessage(jitter):
    """
    BOOL EvtFormatMessage(
        EVT_HANDLE PublisherMetadata,
        EVT_HANDLE Event,
        DWORD MessageId,
        DWORD ValueCount,
        PEVT_VARIANT Values,
        [EvtFormatMessageFlags] Flags,
        DWORD BufferSize,
        LPWSTR Buffer,
        PDWORD BufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PublisherMetadata", "Event", "MessageId", "ValueCount", "Values", "Flags", "BufferSize", "Buffer", "BufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtOpenLog(jitter):
    """
    EVT_HANDLE EvtOpenLog(
        EVT_HANDLE Session,
        LPCWSTR Path,
        [EvtOpenFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Session", "Path", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetLogInfo(jitter):
    """
    BOOL EvtGetLogInfo(
        EVT_HANDLE Log,
        EVT_LOG_PROPERTY_ID PropertyId,
        DWORD PropertyValueBufferSize,
        PEVT_VARIANT PropertyValueBuffer,
        PDWORD PropertyValueBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Log", "PropertyId", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtClearLog(jitter):
    """
    BOOL EvtClearLog(
        EVT_HANDLE Session,
        LPCWSTR ChannelPath,
        LPCWSTR TargetFilePath,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Session", "ChannelPath", "TargetFilePath", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtExportLog(jitter):
    """
    BOOL EvtExportLog(
        EVT_HANDLE Session,
        LPCWSTR Path,
        LPCWSTR Query,
        LPCWSTR TargetFilePath,
        [EvtExportLogFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Session", "Path", "Query", "TargetFilePath", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtArchiveExportedLog(jitter):
    """
    BOOL EvtArchiveExportedLog(
        EVT_HANDLE Session,
        LPCWSTR LogFilePath,
        LCID Locale,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Session", "LogFilePath", "Locale", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtOpenChannelEnum(jitter):
    """
    EVT_HANDLE EvtOpenChannelEnum(
        EVT_HANDLE Session,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Session", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtNextChannelPath(jitter):
    """
    BOOL EvtNextChannelPath(
        EVT_HANDLE ChannelEnum,
        DWORD ChannelPathBufferSize,
        LPWSTR ChannelPathBuffer,
        PDWORD ChannelPathBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ChannelEnum", "ChannelPathBufferSize", "ChannelPathBuffer", "ChannelPathBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtOpenChannelConfig(jitter):
    """
    EVT_HANDLE EvtOpenChannelConfig(
        EVT_HANDLE Session,
        LPCWSTR ChannelPath,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Session", "ChannelPath", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtSaveChannelConfig(jitter):
    """
    BOOL EvtSaveChannelConfig(
        EVT_HANDLE ChannelConfig,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ChannelConfig", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtSetChannelConfigProperty(jitter):
    """
    BOOL EvtSetChannelConfigProperty(
        EVT_HANDLE ChannelConfig,
        EVT_CHANNEL_CONFIG_PROPERTY_ID PropertyId,
        DWORD Flags,
        PEVT_VARIANT PropertyValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ChannelConfig", "PropertyId", "Flags", "PropertyValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetChannelConfigProperty(jitter):
    """
    BOOL EvtGetChannelConfigProperty(
        EVT_HANDLE ChannelConfig,
        EVT_CHANNEL_CONFIG_PROPERTY_ID PropertyId,
        DWORD Flags,
        DWORD PropertyValueBufferSize,
        PEVT_VARIANT PropertyValueBuffer,
        PDWORD PropertyValueBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ChannelConfig", "PropertyId", "Flags", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtNextPublisherId(jitter):
    """
    BOOL EvtNextPublisherId(
        EVT_HANDLE PublisherEnum,
        DWORD PublisherIdBufferSize,
        LPWSTR PublisherIdBuffer,
        PDWORD PublisherIdBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PublisherEnum", "PublisherIdBufferSize", "PublisherIdBuffer", "PublisherIdBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtOpenPublisherEnum(jitter):
    """
    EVT_HANDLE EvtOpenPublisherEnum(
        EVT_HANDLE Session,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Session", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtOpenPublisherMetadata(jitter):
    """
    EVT_HANDLE EvtOpenPublisherMetadata(
        EVT_HANDLE Session,
        LPCWSTR PublisherIdentity,
        LPCWSTR LogFilePath,
        LCID Locale,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Session", "PublisherIdentity", "LogFilePath", "Locale", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetPublisherMetadataProperty(jitter):
    """
    BOOL EvtGetPublisherMetadataProperty(
        EVT_HANDLE PublisherMetadata,
        EVT_PUBLISHER_METADATA_PROPERTY_ID PropertyId,
        DWORD Flags,
        DWORD PublisherMetadataPropertyBufferSize,
        PEVT_VARIANT PublisherMetadataPropertyBuffer,
        PDWORD PublisherMetadataPropertyBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PublisherMetadata", "PropertyId", "Flags", "PublisherMetadataPropertyBufferSize", "PublisherMetadataPropertyBuffer", "PublisherMetadataPropertyBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtOpenEventMetadataEnum(jitter):
    """
    EVT_HANDLE EvtOpenEventMetadataEnum(
        EVT_HANDLE PublisherMetadata,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PublisherMetadata", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtNextEventMetadata(jitter):
    """
    EVT_HANDLE EvtNextEventMetadata(
        EVT_HANDLE EventMetadataEnum,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventMetadataEnum", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetEventMetadataProperty(jitter):
    """
    BOOL EvtGetEventMetadataProperty(
        EVT_HANDLE EventMetadata,
        EVT_EVENT_METADATA_PROPERTY_ID PropertyId,
        DWORD Flags,
        DWORD EventMetadataPropertyBufferSize,
        PEVT_VARIANT EventMetadataPropertyBuffer,
        PDWORD EventMetadataPropertyBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventMetadata", "PropertyId", "Flags", "EventMetadataPropertyBufferSize", "EventMetadataPropertyBuffer", "EventMetadataPropertyBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetObjectArraySize(jitter):
    """
    BOOL EvtGetObjectArraySize(
        EVT_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray,
        PDWORD ObjectArraySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "ObjectArraySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wevtapi_EvtGetObjectArrayProperty(jitter):
    """
    BOOL EvtGetObjectArrayProperty(
        EVT_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray,
        DWORD PropertyId,
        DWORD ArrayIndex,
        DWORD Flags,
        DWORD PropertyValueBufferSize,
        PEVT_VARIANT PropertyValueBuffer,
        PDWORD PropertyValueBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "PropertyId", "ArrayIndex", "Flags", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
