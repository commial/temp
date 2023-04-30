###### Enums ######
HTTP_DATA_CHUNK_TYPE = {
    "HttpDataChunkFromMemory": 0,
    "HttpDataChunkFromFileHandle": 1,
    "HttpDataChunkFromFragmentCache": 2,
    "HttpDataChunkFromFragmentCacheEx": 3,
}
HTTP_DATA_CHUNK_TYPE_INV = {
    0: "HttpDataChunkFromMemory",
    1: "HttpDataChunkFromFileHandle",
    2: "HttpDataChunkFromFragmentCache",
    3: "HttpDataChunkFromFragmentCacheEx",
}
HTTP_CACHE_POLICY_TYPE = {
    "HttpCachePolicyNocache": 0,
    "HttpCachePolicyUserInvalidates": 1,
    "HttpCachePolicyTimeToLive": 2,
}
HTTP_CACHE_POLICY_TYPE_INV = {
    0: "HttpCachePolicyNocache",
    1: "HttpCachePolicyUserInvalidates",
    2: "HttpCachePolicyTimeToLive",
}
HTTP_LOG_DATA_TYPE = {
    "HttpLogDataTypeFields": 0,
}
HTTP_LOG_DATA_TYPE_INV = {
    0: "HttpLogDataTypeFields",
}
HTTP_SERVICE_CONFIG_ID = {
    "HttpServiceConfigIPListenList": 0,
    "HttpServiceConfigSSLCertInfo": 1,
    "HttpServiceConfigUrlAclInfo": 2,
    "HttpServiceConfigTimeout": 3,
    "HttpServiceConfigMax": 4,
}
HTTP_SERVICE_CONFIG_ID_INV = {
    0: "HttpServiceConfigIPListenList",
    1: "HttpServiceConfigSSLCertInfo",
    2: "HttpServiceConfigUrlAclInfo",
    3: "HttpServiceConfigTimeout",
    4: "HttpServiceConfigMax",
}
HTTP_SERVER_PROPERTY = {
    "HttpServerAuthenticationProperty": 0,
    "HttpServerLoggingProperty": 1,
    "HttpServerQosProperty": 2,
    "HttpServerTimeoutsProperty": 3,
    "HttpServerQueueLengthProperty": 4,
    "HttpServerStateProperty": 5,
    "HttpServer503VerbosityProperty": 6,
    "HttpServerBindingProperty": 7,
    "HttpServerExtendedAuthenticationProperty": 8,
    "HttpServerListenEndpointProperty": 9,
}
HTTP_SERVER_PROPERTY_INV = {
    0: "HttpServerAuthenticationProperty",
    1: "HttpServerLoggingProperty",
    2: "HttpServerQosProperty",
    3: "HttpServerTimeoutsProperty",
    4: "HttpServerQueueLengthProperty",
    5: "HttpServerStateProperty",
    6: "HttpServer503VerbosityProperty",
    7: "HttpServerBindingProperty",
    8: "HttpServerExtendedAuthenticationProperty",
    9: "HttpServerListenEndpointProperty",
}
HTTP_VERB = {
    "HttpVerbUnparsed": 0,
    "HttpVerbUnknown": 1,
    "HttpVerbInvalid": 2,
    "HttpVerbOPTIONS": 3,
    "HttpVerbGET": 4,
    "HttpVerbHEAD": 5,
    "HttpVerbPOST": 6,
    "HttpVerbPUT": 7,
    "HttpVerbDELETE": 8,
    "HttpVerbTRACE": 9,
    "HttpVerbCONNECT": 10,
    "HttpVerbTRACK": 11,
    "HttpVerbMOVE": 12,
    "HttpVerbCOPY": 13,
    "HttpVerbPROPFIND": 14,
    "HttpVerbPROPPATCH": 15,
    "HttpVerbMKCOL": 16,
    "HttpVerbLOCK": 17,
    "HttpVerbUNLOCK": 18,
    "HttpVerbSEARCH": 19,
}
HTTP_VERB_INV = {
    0: "HttpVerbUnparsed",
    1: "HttpVerbUnknown",
    2: "HttpVerbInvalid",
    3: "HttpVerbOPTIONS",
    4: "HttpVerbGET",
    5: "HttpVerbHEAD",
    6: "HttpVerbPOST",
    7: "HttpVerbPUT",
    8: "HttpVerbDELETE",
    9: "HttpVerbTRACE",
    10: "HttpVerbCONNECT",
    11: "HttpVerbTRACK",
    12: "HttpVerbMOVE",
    13: "HttpVerbCOPY",
    14: "HttpVerbPROPFIND",
    15: "HttpVerbPROPPATCH",
    16: "HttpVerbMKCOL",
    17: "HttpVerbLOCK",
    18: "HttpVerbUNLOCK",
    19: "HttpVerbSEARCH",
}
HTTP_REQUEST_INFO_TYPE = {
    "HttpRequestInfoTypeAuth": 0,
    "HttpRequestInfoTypeChannelBind": 1,
}
HTTP_REQUEST_INFO_TYPE_INV = {
    0: "HttpRequestInfoTypeAuth",
    1: "HttpRequestInfoTypeChannelBind",
}
HTTP_RESPONSE_INFO_TYPE = {
    "HttpResponseInfoTypeMultipleKnownHeaders": 0,
    "HttpResponseInfoTypeAuthenticationProperty": 1,
    "HttpResponseInfoTypeQoSProperty": 2,
    "HttpResponseInfoTypeChannelBind": 3,
}
HTTP_RESPONSE_INFO_TYPE_INV = {
    0: "HttpResponseInfoTypeMultipleKnownHeaders",
    1: "HttpResponseInfoTypeAuthenticationProperty",
    2: "HttpResponseInfoTypeQoSProperty",
    3: "HttpResponseInfoTypeChannelBind",
}

###################

###### Types ######
HTTPAPI_VERSION = UINT
HTTP_OPAQUE_ID = ULONGLONG
HTTP_REQUEST_ID = HTTP_OPAQUE_ID
HTTP_CONNECTION_ID = HTTP_OPAQUE_ID
HTTP_RAW_CONNECTION_ID = HTTP_OPAQUE_ID
HTTP_SERVER_SESSION_ID = HTTP_OPAQUE_ID
PHTTP_SERVER_SESSION_ID = Ptr("<I", HTTP_SERVER_SESSION_ID())
HTTP_URL_GROUP_ID = HTTP_OPAQUE_ID
PHTTP_URL_GROUP_ID = Ptr("<I", HTTP_URL_GROUP_ID())
HTTP_URL_CONTEXT = ULONGLONG

class HTTP_BYTE_RANGE(MemStruct):
    fields = [
        ("StartingOffset", ULARGE_INTEGER()),
        ("Length", ULARGE_INTEGER()),
    ]

PHTTP_BYTE_RANGE = Ptr("<I", HTTP_BYTE_RANGE())
HTTP_DATA_CHUNK_TYPE = UINT

class _HTTP_DATA_CHUNK_u_s1_(MemStruct):
    fields = [
        # Length is `BufferLength`
        ("pBuffer", PVOID()),
        ("BufferLength", ULONG()),
    ]


class _HTTP_DATA_CHUNK_u_s2_(MemStruct):
    fields = [
        ("ByteRange", HTTP_BYTE_RANGE()),
        ("FileHandle", HANDLE()),
    ]


class _HTTP_DATA_CHUNK_u_s3_(MemStruct):
    fields = [
        ("FragmentNameLength", USHORT()),
        ("pFragmentName", PCWSTR()),
    ]


class _HTTP_DATA_CHUNK_u_s4_(MemStruct):
    fields = [
        ("ByteRange", HTTP_BYTE_RANGE()),
        ("pFragmentName", PCWSTR()),
    ]

_HTTP_DATA_CHUNK_u_ = Union([
    ("FromMemory", _HTTP_DATA_CHUNK_u_s1_),
    ("FromFileHandle", _HTTP_DATA_CHUNK_u_s2_),
    ("FromFragmentCache", _HTTP_DATA_CHUNK_u_s3_),
    ("FromFragmentCacheEx", _HTTP_DATA_CHUNK_u_s4_),
])

class HTTP_DATA_CHUNK(MemStruct):
    fields = [
        ("DataChunkType", HTTP_DATA_CHUNK_TYPE()),
        (None, _HTTP_DATA_CHUNK_u_()),
    ]

PHTTP_DATA_CHUNK = Ptr("<I", HTTP_DATA_CHUNK())
HTTP_CACHE_POLICY_TYPE = UINT

class HTTP_CACHE_POLICY(MemStruct):
    fields = [
        ("Policy", HTTP_CACHE_POLICY_TYPE()),
        ("SecondsToLive", ULONG()),
    ]

PHTTP_CACHE_POLICY = Ptr("<I", HTTP_CACHE_POLICY())
HTTP_LOG_DATA_TYPE = UINT

class HTTP_LOG_DATA(MemStruct):
    fields = [
        ("Type", HTTP_LOG_DATA_TYPE()),
    ]

PHTTP_LOG_DATA = Ptr("<I", HTTP_LOG_DATA())
HTTP_SERVICE_CONFIG_ID = UINT
HTTP_SERVER_PROPERTY = UINT
_HttpInitializeFlags_ = ULONG
_HTTP_REQUEST_FLAG_ = ULONG

class HTTP_VERSION(MemStruct):
    fields = [
        ("MajorVersion", USHORT()),
        ("MinorVersion", USHORT()),
    ]

HTTP_VERB = UINT

class HTTP_COOKED_URL(MemStruct):
    fields = [
        ("FullUrlLength", USHORT()),
        ("HostLength", USHORT()),
        ("AbsPathLength", USHORT()),
        ("QueryStringLength", USHORT()),
        ("pFullUrl", PCWSTR()),
        ("pHost", PCWSTR()),
        ("pAbsPath", PCWSTR()),
        ("pQueryString", PCWSTR()),
    ]


class HTTP_TRANSPORT_ADDRESS(MemStruct):
    fields = [
        ("pRemoteAddress", PSOCKADDR()),
        ("pLocalAddress", PSOCKADDR()),
    ]


class HTTP_UNKNOWN_HEADER(MemStruct):
    fields = [
        ("NameLength", USHORT()),
        ("RawValueLength", USHORT()),
        ("pName", PCSTR()),
        ("pRawValue", PCSTR()),
    ]

PHTTP_UNKNOWN_HEADER = Ptr("<I", HTTP_UNKNOWN_HEADER())

class HTTP_KNOWN_HEADER(MemStruct):
    fields = [
        ("RawValueLength", USHORT()),
        ("pRawValue", PCSTR()),
    ]

HTTP_KNOWN_HEADER__HttpHeaderRequestMaximum_ = Array(HTTP_KNOWN_HEADER, 41)
HTTP_KNOWN_HEADER__HttpHeaderResponseMaximum_ = Array(HTTP_KNOWN_HEADER, 30)

class HTTP_REQUEST_HEADERS(MemStruct):
    fields = [
        ("UnknownHeaderCount", USHORT()),
        ("pUnknownHeaders", PHTTP_UNKNOWN_HEADER()),
        ("TrailerCount", USHORT()),
        ("pTrailers", PHTTP_UNKNOWN_HEADER()),
        ("KnownHeaders", HTTP_KNOWN_HEADER__HttpHeaderRequestMaximum_()),
    ]


class HTTP_SSL_CLIENT_CERT_INFO(MemStruct):
    fields = [
        ("CertFlags", _CERT_TRUST_Error_()),
        ("CertEncodedSize", ULONG()),
        ("pCertEncoded", PUCHAR()),
        ("Token", HANDLE()),
        ("CertDeniedByMapper", BOOLEAN()),
    ]

PHTTP_SSL_CLIENT_CERT_INFO = Ptr("<I", HTTP_SSL_CLIENT_CERT_INFO())

class HTTP_SSL_INFO(MemStruct):
    fields = [
        ("ServerCertKeySize", USHORT()),
        ("ConnectionKeySize", USHORT()),
        ("ServerCertIssuerSize", ULONG()),
        ("ServerCertSubjectSize", ULONG()),
        ("pServerCertIssuer", PCSTR()),
        ("pServerCertSubject", PCSTR()),
        ("pClientCertInfo", PHTTP_SSL_CLIENT_CERT_INFO()),
        ("SslClientCertNegotiated", ULONG()),
    ]

PHTTP_SSL_INFO = Ptr("<I", HTTP_SSL_INFO())

class HTTP_REQUEST_V1(MemStruct):
    fields = [
        ("Flags", _HTTP_REQUEST_FLAG_()),
        ("ConnectionId", HTTP_CONNECTION_ID()),
        ("RequestId", HTTP_REQUEST_ID()),
        ("UrlContext", HTTP_URL_CONTEXT()),
        ("Version", HTTP_VERSION()),
        ("Verb", HTTP_VERB()),
        ("UnknownVerbLength", USHORT()),
        ("RawUrlLength", USHORT()),
        ("pUnknownVerb", PCSTR()),
        ("pRawUrl", PCSTR()),
        ("CookedUrl", HTTP_COOKED_URL()),
        ("Address", HTTP_TRANSPORT_ADDRESS()),
        ("Headers", HTTP_REQUEST_HEADERS()),
        ("BytesReceived", ULONGLONG()),
        ("EntityChunkCount", USHORT()),
        ("pEntityChunks", PHTTP_DATA_CHUNK()),
        ("RawConnectionId", HTTP_RAW_CONNECTION_ID()),
        ("pSslInfo", PHTTP_SSL_INFO()),
    ]

HTTP_REQUEST_INFO_TYPE = UINT

class HTTP_REQUEST_INFO(MemStruct):
    fields = [
        ("InfoType", HTTP_REQUEST_INFO_TYPE()),
        ("InfoLength", ULONG()),
        # Length is `InfoLength`
        ("pInfo", PVOID()),
    ]

PHTTP_REQUEST_INFO = Ptr("<I", HTTP_REQUEST_INFO())

class HTTP_REQUEST(MemStruct):
    fields = [
        (None, HTTP_REQUEST_V1()),
        ("RequestInfoCount", USHORT()),
        ("pRequestInfo", PHTTP_REQUEST_INFO()),
    ]

PHTTP_REQUEST = Ptr("<I", HTTP_REQUEST())
_HTTP_RESPONSE_FLAG_ = ULONG

class HTTP_RESPONSE_HEADERS(MemStruct):
    fields = [
        ("UnknownHeaderCount", USHORT()),
        ("pUnknownHeaders", PHTTP_UNKNOWN_HEADER()),
        ("TrailerCount", USHORT()),
        ("pTrailers", PHTTP_UNKNOWN_HEADER()),
        ("KnownHeaders", HTTP_KNOWN_HEADER__HttpHeaderResponseMaximum_()),
    ]


class HTTP_RESPONSE_V1(MemStruct):
    fields = [
        ("Flags", _HTTP_RESPONSE_FLAG_()),
        ("Version", HTTP_VERSION()),
        ("StatusCode", USHORT()),
        ("ReasonLength", USHORT()),
        ("pReason", PCSTR()),
        ("Headers", HTTP_RESPONSE_HEADERS()),
        ("EntityChunkCount", USHORT()),
        ("pEntityChunks", PHTTP_DATA_CHUNK()),
    ]

HTTP_RESPONSE_INFO_TYPE = UINT

class HTTP_RESPONSE_INFO(MemStruct):
    fields = [
        ("Type", HTTP_RESPONSE_INFO_TYPE()),
        ("Length", ULONG()),
        # Length is `Length`
        ("pInfo", PVOID()),
    ]

PHTTP_RESPONSE_INFO = Ptr("<I", HTTP_RESPONSE_INFO())

class HTTP_RESPONSE(MemStruct):
    fields = [
        (None, HTTP_RESPONSE_V1()),
        ("ResponseInfoCount", USHORT()),
        ("pResponseInfo", PHTTP_RESPONSE_INFO()),
    ]

PHTTP_RESPONSE = Ptr("<I", HTTP_RESPONSE())

###################

###### Functions ######

def httpapi_HttpCreateHttpHandle(jitter):
    """
    [ERROR_CODE_ULONG] HttpCreateHttpHandle(
        PHANDLE pReqQueueHandle,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pReqQueueHandle", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpInitialize(jitter):
    """
    [ERROR_CODE_ULONG] HttpInitialize(
        HTTPAPI_VERSION Version,
        [HttpInitializeFlags] Flags,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Version", "Flags", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpPrepareUrl(jitter):
    """
    [ERROR_CODE_ULONG] HttpPrepareUrl(
        PVOID Reserved,
        ULONG Flags,
        PCWSTR Url,
        PWSTR* PreparedUrl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Reserved", "Flags", "Url", "PreparedUrl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpTerminate(jitter):
    """
    [ERROR_CODE_ULONG] HttpTerminate(
        [HttpInitializeFlags] Flags,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpAddFragmentToCache(jitter):
    """
    [ERROR_CODE_ULONG] HttpAddFragmentToCache(
        HANDLE ReqQueueHandle,
        PCWSTR pUrlPrefix,
        PHTTP_DATA_CHUNK pDataChunk,
        PHTTP_CACHE_POLICY pCachePolicy,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReqQueueHandle", "pUrlPrefix", "pDataChunk", "pCachePolicy", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpFlushResponseCache(jitter):
    """
    [ERROR_CODE_ULONG] HttpFlushResponseCache(
        HANDLE ReqQueueHandle,
        PCWSTR pUrlPrefix,
        ULONG Flags,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReqQueueHandle", "pUrlPrefix", "Flags", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpReadFragmentFromCache(jitter):
    """
    [ERROR_CODE_ULONG] HttpReadFragmentFromCache(
        HANDLE ReqQueueHandle,
        PCWSTR pUrlPrefix,
        PHTTP_BYTE_RANGE pByteRange,
        PVOID pBuffer,
        ULONG BufferLength,
        PULONG pBytesRead,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReqQueueHandle", "pUrlPrefix", "pByteRange", "pBuffer", "BufferLength", "pBytesRead", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpDeleteServiceConfiguration(jitter):
    """
    [ERROR_CODE_ULONG] HttpDeleteServiceConfiguration(
        HANDLE ServiceHandle,
        HTTP_SERVICE_CONFIG_ID ConfigId,
        PVOID pConfigInformation,
        ULONG ConfigInformationLength,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServiceHandle", "ConfigId", "pConfigInformation", "ConfigInformationLength", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpQueryServiceConfiguration(jitter):
    """
    [ERROR_CODE_ULONG] HttpQueryServiceConfiguration(
        HANDLE ServiceHandle,
        HTTP_SERVICE_CONFIG_ID ConfigId,
        PVOID pInputConfigInfo,
        ULONG InputConfigInfoLength,
        PVOID pOutputConfigInfo,
        ULONG OutputConfigInfoLength,
        PULONG pReturnLength,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServiceHandle", "ConfigId", "pInputConfigInfo", "InputConfigInfoLength", "pOutputConfigInfo", "OutputConfigInfoLength", "pReturnLength", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpSetServiceConfiguration(jitter):
    """
    [ERROR_CODE_ULONG] HttpSetServiceConfiguration(
        HANDLE ServiceHandle,
        HTTP_SERVICE_CONFIG_ID ConfigId,
        PVOID pConfigInformation,
        ULONG ConfigInformationLength,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServiceHandle", "ConfigId", "pConfigInformation", "ConfigInformationLength", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpReceiveHttpRequest(jitter):
    """
    [ERROR_CODE_ULONG] HttpReceiveHttpRequest(
        HANDLE ReqQueueHandle,
        HTTP_REQUEST_ID RequestId,
        ULONG Flags,
        PHTTP_REQUEST pRequestBuffer,
        ULONG RequestBufferLength,
        PULONG pBytesReceived,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReqQueueHandle", "RequestId", "Flags", "pRequestBuffer", "RequestBufferLength", "pBytesReceived", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpReceiveRequestEntityBody(jitter):
    """
    [ERROR_CODE_ULONG] HttpReceiveRequestEntityBody(
        HANDLE ReqQueueHandle,
        HTTP_REQUEST_ID RequestId,
        ULONG Flags,
        PVOID pBuffer,
        ULONG BufferLength,
        PULONG pBytesReceived,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReqQueueHandle", "RequestId", "Flags", "pBuffer", "BufferLength", "pBytesReceived", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpSendHttpResponse(jitter):
    """
    [ERROR_CODE_ULONG] HttpSendHttpResponse(
        HANDLE ReqQueueHandle,
        HTTP_REQUEST_ID RequestId,
        ULONG Flags,
        PHTTP_RESPONSE pHttpResponse,
        PHTTP_CACHE_POLICY pCachePolicy,
        PULONG pBytesSent,
        PVOID pReserved2,
        ULONG Reserved3,
        LPOVERLAPPED pOverlapped,
        PHTTP_LOG_DATA pLogData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReqQueueHandle", "RequestId", "Flags", "pHttpResponse", "pCachePolicy", "pBytesSent", "pReserved2", "Reserved3", "pOverlapped", "pLogData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpSendResponseEntityBody(jitter):
    """
    [ERROR_CODE_ULONG] HttpSendResponseEntityBody(
        HANDLE ReqQueueHandle,
        HTTP_REQUEST_ID RequestId,
        ULONG Flags,
        USHORT EntityChunkCount,
        PHTTP_DATA_CHUNK pEntityChunks,
        PULONG pBytesSent,
        PVOID pReserved1,
        ULONG Reserved2,
        LPOVERLAPPED pOverlapped,
        PHTTP_LOG_DATA pLogData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReqQueueHandle", "RequestId", "Flags", "EntityChunkCount", "pEntityChunks", "pBytesSent", "pReserved1", "Reserved2", "pOverlapped", "pLogData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpWaitForDisconnect(jitter):
    """
    [ERROR_CODE_ULONG] HttpWaitForDisconnect(
        HANDLE ReqQueueHandle,
        HTTP_CONNECTION_ID ConnectionId,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReqQueueHandle", "ConnectionId", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpReceiveClientCertificate(jitter):
    """
    [ERROR_CODE_ULONG] HttpReceiveClientCertificate(
        HANDLE ReqQueueHandle,
        HTTP_CONNECTION_ID ConnectionId,
        ULONG Flags,
        PHTTP_SSL_CLIENT_CERT_INFO pSslClientCertInfo,
        ULONG SslClientCertInfoSize,
        PULONG pBytesReceived,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReqQueueHandle", "ConnectionId", "Flags", "pSslClientCertInfo", "SslClientCertInfoSize", "pBytesReceived", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpAddUrl(jitter):
    """
    [ERROR_CODE_ULONG] HttpAddUrl(
        HANDLE ReqQueueHandle,
        PCWSTR pFullyQualifiedUrl,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReqQueueHandle", "pFullyQualifiedUrl", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpRemoveUrl(jitter):
    """
    [ERROR_CODE_ULONG] HttpRemoveUrl(
        HANDLE ReqQueueHandle,
        PCWSTR pFullyQualifiedUrl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReqQueueHandle", "pFullyQualifiedUrl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpCloseServerSession(jitter):
    """
    [ERROR_CODE_ULONG] HttpCloseServerSession(
        HTTP_SERVER_SESSION_ID ServerSessionId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerSessionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpCreateServerSession(jitter):
    """
    [ERROR_CODE_ULONG] HttpCreateServerSession(
        HTTPAPI_VERSION Version,
        PHTTP_SERVER_SESSION_ID pServerSessionId,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Version", "pServerSessionId", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpQueryServerSessionProperty(jitter):
    """
    [ERROR_CODE_ULONG] HttpQueryServerSessionProperty(
        HTTP_SERVER_SESSION_ID ServerSessionId,
        HTTP_SERVER_PROPERTY Property,
        PVOID pPropertyInformation,
        ULONG PropertyInformationLength,
        PULONG pReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerSessionId", "Property", "pPropertyInformation", "PropertyInformationLength", "pReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpSetServerSessionProperty(jitter):
    """
    [ERROR_CODE_ULONG] HttpSetServerSessionProperty(
        HTTP_SERVER_SESSION_ID ServerSessionId,
        HTTP_SERVER_PROPERTY Property,
        PVOID pPropertyInformation,
        ULONG PropertyInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerSessionId", "Property", "pPropertyInformation", "PropertyInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpAddUrlToUrlGroup(jitter):
    """
    [ERROR_CODE_ULONG] HttpAddUrlToUrlGroup(
        HTTP_URL_GROUP_ID UrlGroupId,
        PCWSTR pFullyQualifiedUrl,
        HTTP_URL_CONTEXT UrlContext,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UrlGroupId", "pFullyQualifiedUrl", "UrlContext", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpCreateUrlGroup(jitter):
    """
    [ERROR_CODE_ULONG] HttpCreateUrlGroup(
        HTTP_SERVER_SESSION_ID ServerSessionId,
        PHTTP_URL_GROUP_ID pUrlGroupId,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerSessionId", "pUrlGroupId", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpCloseUrlGroup(jitter):
    """
    [ERROR_CODE_ULONG] HttpCloseUrlGroup(
        HTTP_URL_GROUP_ID UrlGroupId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UrlGroupId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpQueryUrlGroupProperty(jitter):
    """
    [ERROR_CODE_ULONG] HttpQueryUrlGroupProperty(
        HTTP_URL_GROUP_ID UrlGroupId,
        HTTP_SERVER_PROPERTY Property,
        PVOID pPropertyInformation,
        ULONG PropertyInformationLength,
        PULONG pReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UrlGroupId", "Property", "pPropertyInformation", "PropertyInformationLength", "pReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpRemoveUrlFromUrlGroup(jitter):
    """
    [ERROR_CODE_ULONG] HttpRemoveUrlFromUrlGroup(
        HTTP_URL_GROUP_ID UrlGroupId,
        PCWSTR pFullyQualifiedUrl,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UrlGroupId", "pFullyQualifiedUrl", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpSetUrlGroupProperty(jitter):
    """
    [ERROR_CODE_ULONG] HttpSetUrlGroupProperty(
        HTTP_URL_GROUP_ID UrlGroupId,
        HTTP_SERVER_PROPERTY Property,
        PVOID pPropertyInformation,
        ULONG PropertyInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UrlGroupId", "Property", "pPropertyInformation", "PropertyInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpCloseRequestQueue(jitter):
    """
    [ERROR_CODE_ULONG] HttpCloseRequestQueue(
        HANDLE ReqQueueHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReqQueueHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpCreateRequestQueue(jitter):
    """
    [ERROR_CODE_ULONG] HttpCreateRequestQueue(
        HTTPAPI_VERSION Version,
        PCWSTR pName,
        PSECURITY_ATTRIBUTES pSecurityAttributes,
        ULONG Flags,
        PHANDLE pReqQueueHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Version", "pName", "pSecurityAttributes", "Flags", "pReqQueueHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpSetRequestQueueProperty(jitter):
    """
    [ERROR_CODE_ULONG] HttpSetRequestQueueProperty(
        HANDLE Handle,
        HTTP_SERVER_PROPERTY Property,
        PVOID pPropertyInformation,
        ULONG PropertyInformationLength,
        ULONG Reserved,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "Property", "pPropertyInformation", "PropertyInformationLength", "Reserved", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def httpapi_HttpWaitForDemandStart(jitter):
    """
    [ERROR_CODE_ULONG] HttpWaitForDemandStart(
        HANDLE ReqQueueHandle,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReqQueueHandle", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
