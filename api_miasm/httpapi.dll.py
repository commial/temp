
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
