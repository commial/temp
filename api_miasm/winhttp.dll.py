###### Enums ######
_HttpOpenAccessType_ = {
    "WINHTTP_ACCESS_TYPE_DEFAULT_PROXY": 0,
    "WINHTTP_ACCESS_TYPE_NO_PROXY": 1,
    "WINHTTP_ACCESS_TYPE_NAMED_PROXY": 3,
}
_HttpOpenAccessType__INV = {
    0: "WINHTTP_ACCESS_TYPE_DEFAULT_PROXY",
    1: "WINHTTP_ACCESS_TYPE_NO_PROXY",
    3: "WINHTTP_ACCESS_TYPE_NAMED_PROXY",
}
_WinHttpOpenFlags_ = {
    "WINHTTP_FLAG_ASYNC": 0x10000000,
}
_WinHttpOpenFlags__INV = {
    0x10000000: "WINHTTP_FLAG_ASYNC",
}
_WinHttpOption_ = {
    "WINHTTP_OPTION_CALLBACK": 1,
    "WINHTTP_OPTION_RESOLVE_TIMEOUT": 2,
    "WINHTTP_OPTION_CONNECT_TIMEOUT": 3,
    "WINHTTP_OPTION_CONNECT_RETRIES": 4,
    "WINHTTP_OPTION_SEND_TIMEOUT": 5,
    "WINHTTP_OPTION_RECEIVE_TIMEOUT": 6,
    "WINHTTP_OPTION_RECEIVE_RESPONSE_TIMEOUT": 7,
    "WINHTTP_OPTION_HANDLE_TYPE": 9,
    "WINHTTP_OPTION_READ_BUFFER_SIZE": 12,
    "WINHTTP_OPTION_WRITE_BUFFER_SIZE": 13,
    "WINHTTP_OPTION_PARENT_HANDLE": 21,
    "WINHTTP_OPTION_EXTENDED_ERROR": 24,
    "WINHTTP_OPTION_SECURITY_FLAGS": 31,
    "WINHTTP_OPTION_SECURITY_CERTIFICATE_STRUCT": 32,
    "WINHTTP_OPTION_URL": 34,
    "WINHTTP_OPTION_SECURITY_KEY_BITNESS": 36,
    "WINHTTP_OPTION_PROXY": 38,
    "WINHTTP_OPTION_USER_AGENT": 41,
    "WINHTTP_OPTION_CONTEXT_VALUE": 45,
    "WINHTTP_OPTION_CLIENT_CERT_CONTEXT": 47,
    "WINHTTP_OPTION_REQUEST_PRIORITY": 58,
    "WINHTTP_OPTION_HTTP_VERSION": 59,
    "WINHTTP_OPTION_DISABLE_FEATURE": 63,
    "WINHTTP_OPTION_CODEPAGE": 68,
    "WINHTTP_OPTION_MAX_CONNS_PER_SERVER": 73,
    "WINHTTP_OPTION_MAX_CONNS_PER_1_0_SERVER": 74,
    "WINHTTP_OPTION_AUTOLOGON_POLICY": 77,
    "WINHTTP_OPTION_SERVER_CERT_CONTEXT": 78,
    "WINHTTP_OPTION_ENABLE_FEATURE": 79,
    "WINHTTP_OPTION_WORKER_THREAD_COUNT": 80,
    "WINHTTP_OPTION_PASSPORT_COBRANDING_TEXT": 81,
    "WINHTTP_OPTION_PASSPORT_COBRANDING_URL": 82,
    "WINHTTP_OPTION_CONFIGURE_PASSPORT_AUTH": 83,
    "WINHTTP_OPTION_SECURE_PROTOCOLS": 84,
    "WINHTTP_OPTION_ENABLETRACING": 85,
    "WINHTTP_OPTION_PASSPORT_SIGN_OUT": 86,
    "WINHTTP_OPTION_PASSPORT_RETURN_URL": 87,
    "WINHTTP_OPTION_REDIRECT_POLICY": 88,
    "WINHTTP_OPTION_MAX_HTTP_AUTOMATIC_REDIRECTS": 89,
    "WINHTTP_OPTION_MAX_HTTP_STATUS_CONTINUE": 90,
    "WINHTTP_OPTION_MAX_RESPONSE_HEADER_SIZE": 91,
    "WINHTTP_OPTION_MAX_RESPONSE_DRAIN_SIZE": 92,
    "WINHTTP_OPTION_CONNECTION_INFO": 93,
    "WINHTTP_OPTION_CLIENT_CERT_ISSUER_LIST": 94,
    "WINHTTP_OPTION_SPN": 96,
    "WINHTTP_OPTION_GLOBAL_PROXY_CREDS": 97,
    "WINHTTP_OPTION_GLOBAL_SERVER_CREDS": 98,
    "WINHTTP_OPTION_UNLOAD_NOTIFY_EVENT": 99,
    "WINHTTP_OPTION_REJECT_USERPWD_IN_URL": 100,
    "WINHTTP_OPTION_USE_GLOBAL_SERVER_CREDENTIALS": 101,
    "WINHTTP_OPTION_USERNAME": 0x1000,
    "WINHTTP_OPTION_PASSWORD": 0x1001,
    "WINHTTP_OPTION_PROXY_USERNAME": 0x1002,
    "WINHTTP_OPTION_PROXY_PASSWORD": 0x1003,
}
_WinHttpOption__INV = {
    1: "WINHTTP_OPTION_CALLBACK",
    2: "WINHTTP_OPTION_RESOLVE_TIMEOUT",
    3: "WINHTTP_OPTION_CONNECT_TIMEOUT",
    4: "WINHTTP_OPTION_CONNECT_RETRIES",
    5: "WINHTTP_OPTION_SEND_TIMEOUT",
    6: "WINHTTP_OPTION_RECEIVE_TIMEOUT",
    7: "WINHTTP_OPTION_RECEIVE_RESPONSE_TIMEOUT",
    9: "WINHTTP_OPTION_HANDLE_TYPE",
    12: "WINHTTP_OPTION_READ_BUFFER_SIZE",
    13: "WINHTTP_OPTION_WRITE_BUFFER_SIZE",
    21: "WINHTTP_OPTION_PARENT_HANDLE",
    24: "WINHTTP_OPTION_EXTENDED_ERROR",
    31: "WINHTTP_OPTION_SECURITY_FLAGS",
    32: "WINHTTP_OPTION_SECURITY_CERTIFICATE_STRUCT",
    34: "WINHTTP_OPTION_URL",
    36: "WINHTTP_OPTION_SECURITY_KEY_BITNESS",
    38: "WINHTTP_OPTION_PROXY",
    41: "WINHTTP_OPTION_USER_AGENT",
    45: "WINHTTP_OPTION_CONTEXT_VALUE",
    47: "WINHTTP_OPTION_CLIENT_CERT_CONTEXT",
    58: "WINHTTP_OPTION_REQUEST_PRIORITY",
    59: "WINHTTP_OPTION_HTTP_VERSION",
    63: "WINHTTP_OPTION_DISABLE_FEATURE",
    68: "WINHTTP_OPTION_CODEPAGE",
    73: "WINHTTP_OPTION_MAX_CONNS_PER_SERVER",
    74: "WINHTTP_OPTION_MAX_CONNS_PER_1_0_SERVER",
    77: "WINHTTP_OPTION_AUTOLOGON_POLICY",
    78: "WINHTTP_OPTION_SERVER_CERT_CONTEXT",
    79: "WINHTTP_OPTION_ENABLE_FEATURE",
    80: "WINHTTP_OPTION_WORKER_THREAD_COUNT",
    81: "WINHTTP_OPTION_PASSPORT_COBRANDING_TEXT",
    82: "WINHTTP_OPTION_PASSPORT_COBRANDING_URL",
    83: "WINHTTP_OPTION_CONFIGURE_PASSPORT_AUTH",
    84: "WINHTTP_OPTION_SECURE_PROTOCOLS",
    85: "WINHTTP_OPTION_ENABLETRACING",
    86: "WINHTTP_OPTION_PASSPORT_SIGN_OUT",
    87: "WINHTTP_OPTION_PASSPORT_RETURN_URL",
    88: "WINHTTP_OPTION_REDIRECT_POLICY",
    89: "WINHTTP_OPTION_MAX_HTTP_AUTOMATIC_REDIRECTS",
    90: "WINHTTP_OPTION_MAX_HTTP_STATUS_CONTINUE",
    91: "WINHTTP_OPTION_MAX_RESPONSE_HEADER_SIZE",
    92: "WINHTTP_OPTION_MAX_RESPONSE_DRAIN_SIZE",
    93: "WINHTTP_OPTION_CONNECTION_INFO",
    94: "WINHTTP_OPTION_CLIENT_CERT_ISSUER_LIST",
    96: "WINHTTP_OPTION_SPN",
    97: "WINHTTP_OPTION_GLOBAL_PROXY_CREDS",
    98: "WINHTTP_OPTION_GLOBAL_SERVER_CREDS",
    99: "WINHTTP_OPTION_UNLOAD_NOTIFY_EVENT",
    100: "WINHTTP_OPTION_REJECT_USERPWD_IN_URL",
    101: "WINHTTP_OPTION_USE_GLOBAL_SERVER_CREDENTIALS",
    0x1000: "WINHTTP_OPTION_USERNAME",
    0x1001: "WINHTTP_OPTION_PASSWORD",
    0x1002: "WINHTTP_OPTION_PROXY_USERNAME",
    0x1003: "WINHTTP_OPTION_PROXY_PASSWORD",
}
WINHTTP_WEB_SOCKET_BUFFER_TYPE = {
    "WINHTTP_WEB_SOCKET_BINARY_MESSAGE_BUFFER_TYPE": 0,
    "WINHTTP_WEB_SOCKET_BINARY_FRAGMENT_BUFFER_TYPE": 1,
    "WINHTTP_WEB_SOCKET_UTF8_MESSAGE_BUFFER_TYPE": 2,
    "WINHTTP_WEB_SOCKET_UTF8_FRAGMENT_BUFFER_TYPE": 3,
    "WINHTTP_WEB_SOCKET_CLOSE_BUFFER_TYPE": 4,
}
WINHTTP_WEB_SOCKET_BUFFER_TYPE_INV = {
    0: "WINHTTP_WEB_SOCKET_BINARY_MESSAGE_BUFFER_TYPE",
    1: "WINHTTP_WEB_SOCKET_BINARY_FRAGMENT_BUFFER_TYPE",
    2: "WINHTTP_WEB_SOCKET_UTF8_MESSAGE_BUFFER_TYPE",
    3: "WINHTTP_WEB_SOCKET_UTF8_FRAGMENT_BUFFER_TYPE",
    4: "WINHTTP_WEB_SOCKET_CLOSE_BUFFER_TYPE",
}
WINHTTP_WEB_SOCKET_CLOSE_STATUS = {
    "WINHTTP_WEB_SOCKET_SUCCESS_CLOSE_STATUS": 1000,
    "WINHTTP_WEB_SOCKET_ENDPOINT_TERMINATED_CLOSE_STATUS": 1001,
    "WINHTTP_WEB_SOCKET_PROTOCOL_ERROR_CLOSE_STATUS": 1002,
    "WINHTTP_WEB_SOCKET_INVALID_DATA_TYPE_CLOSE_STATUS": 1003,
    "WINHTTP_WEB_SOCKET_EMPTY_CLOSE_STATUS": 1005,
    "WINHTTP_WEB_SOCKET_ABORTED_CLOSE_STATUS": 1006,
    "WINHTTP_WEB_SOCKET_INVALID_PAYLOAD_CLOSE_STATUS": 1007,
    "WINHTTP_WEB_SOCKET_POLICY_VIOLATION_CLOSE_STATUS": 1008,
    "WINHTTP_WEB_SOCKET_MESSAGE_TOO_BIG_CLOSE_STATUS": 1009,
    "WINHTTP_WEB_SOCKET_UNSUPPORTED_EXTENSIONS_CLOSE_STATUS": 1010,
    "WINHTTP_WEB_SOCKET_SERVER_ERROR_CLOSE_STATUS": 1011,
    "WINHTTP_WEB_SOCKET_SECURE_HANDSHAKE_ERROR_CLOSE_STATUS": 1015,
}
WINHTTP_WEB_SOCKET_CLOSE_STATUS_INV = {
    1000: "WINHTTP_WEB_SOCKET_SUCCESS_CLOSE_STATUS",
    1001: "WINHTTP_WEB_SOCKET_ENDPOINT_TERMINATED_CLOSE_STATUS",
    1002: "WINHTTP_WEB_SOCKET_PROTOCOL_ERROR_CLOSE_STATUS",
    1003: "WINHTTP_WEB_SOCKET_INVALID_DATA_TYPE_CLOSE_STATUS",
    1005: "WINHTTP_WEB_SOCKET_EMPTY_CLOSE_STATUS",
    1006: "WINHTTP_WEB_SOCKET_ABORTED_CLOSE_STATUS",
    1007: "WINHTTP_WEB_SOCKET_INVALID_PAYLOAD_CLOSE_STATUS",
    1008: "WINHTTP_WEB_SOCKET_POLICY_VIOLATION_CLOSE_STATUS",
    1009: "WINHTTP_WEB_SOCKET_MESSAGE_TOO_BIG_CLOSE_STATUS",
    1010: "WINHTTP_WEB_SOCKET_UNSUPPORTED_EXTENSIONS_CLOSE_STATUS",
    1011: "WINHTTP_WEB_SOCKET_SERVER_ERROR_CLOSE_STATUS",
    1015: "WINHTTP_WEB_SOCKET_SECURE_HANDSHAKE_ERROR_CLOSE_STATUS",
}

###################

###### Types ######
_CallbackNotificationFlags_ = DWORD
_HttpOpenAccessType_ = DWORD
_WinHttpOpenFlags_ = DWORD
_WinHttpOpenRequestFlags_ = DWORD
_WinHttpOption_ = DWORD
_WinHttpAddReqFlag_ = DWORD
_WinHttpQueryLevelFlags_ = DWORD

class WINHTTP_PROXY_RESULT_ENTRY(MemStruct):
    fields = [
        ("fProxy", BOOL()),
        ("fBypass", BOOL()),
        ("ProxyScheme", INTERNET_SCHEME()),
        ("pwszProxy", PWSTR()),
        ("ProxyPort", INTERNET_PORT()),
    ]

WINHTTP_PROXY_RESULT_ENTRY_PTR = Ptr("<I", WINHTTP_PROXY_RESULT_ENTRY())

class WINHTTP_PROXY_RESULT(MemStruct):
    fields = [
        ("cEntries", DWORD()),
        ("pEntries", WINHTTP_PROXY_RESULT_ENTRY_PTR()),
    ]

WINHTTP_PROXY_RESULT_PTR = Ptr("<I", WINHTTP_PROXY_RESULT())
WINHTTP_WEB_SOCKET_BUFFER_TYPE = UINT
WINHTTP_WEB_SOCKET_BUFFER_TYPE_PTR = Ptr("<I", WINHTTP_WEB_SOCKET_BUFFER_TYPE())
WINHTTP_WEB_SOCKET_CLOSE_STATUS = USHORT
WINHTTP_WEB_SOCKET_CLOSE_STATUS_PTR = Ptr("<I", WINHTTP_WEB_SOCKET_CLOSE_STATUS())

###################

###### Functions ######

def winhttp_WinHttpAddRequestHeaders(jitter):
    """
    BOOL WinHttpAddRequestHeaders(
        HINTERNET hRequest,
        LPCWSTR pwszHeaders,
        DWORD dwHeadersLength,
        [WinHttpAddReqFlag] dwModifiers
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "pwszHeaders", "dwHeadersLength", "dwModifiers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpCheckPlatform(jitter):
    """
    BOOL WinHttpCheckPlatform()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpCloseHandle(jitter):
    """
    BOOL WinHttpCloseHandle(
        HINTERNET hInternet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpConnect(jitter):
    """
    HINTERNET WinHttpConnect(
        HINTERNET hSession,
        LPCWSTR pswzServerName,
        INTERNET_PORT nServerPort,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSession", "pswzServerName", "nServerPort", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpCrackUrl(jitter):
    """
    BOOL WinHttpCrackUrl(
        LPCWSTR pwszUrl,
        DWORD dwUrlLength,
        [InternetCrackUrlFlags] dwFlags,
        LPURL_COMPONENTSW lpUrlComponents
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszUrl", "dwUrlLength", "dwFlags", "lpUrlComponents"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpCreateProxyResolver(jitter):
    """
    [ERROR_CODE] WinHttpCreateProxyResolver(
        HINTERNET hSession,
        HINTERNET* phResolver
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSession", "phResolver"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpCreateUrl(jitter):
    """
    BOOL WinHttpCreateUrl(
        LPURL_COMPONENTSW lpUrlComponents,
        [InternetCrackUrlFlags] dwFlags,
        LPWSTR pwszUrl,
        LPDWORD lpdwUrlLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpUrlComponents", "dwFlags", "pwszUrl", "lpdwUrlLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpDetectAutoProxyConfigUrl(jitter):
    """
    BOOL WinHttpDetectAutoProxyConfigUrl(
        DWORD dwAutoDetectFlags,
        LPWSTR* ppwszAutoConfigUrl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwAutoDetectFlags", "ppwszAutoConfigUrl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpFreeProxyResult(jitter):
    """
    VOID WinHttpFreeProxyResult(
        WINHTTP_PROXY_RESULT* pProxyResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpGetDefaultProxyConfiguration(jitter):
    """
    BOOL WinHttpGetDefaultProxyConfiguration(
        WINHTTP_PROXY_INFO* pProxyInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxyInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpGetIEProxyConfigForCurrentUser(jitter):
    """
    BOOL WinHttpGetIEProxyConfigForCurrentUser(
        WINHTTP_CURRENT_USER_IE_PROXY_CONFIG* pProxyConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxyConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpGetProxyForUrl(jitter):
    """
    BOOL WinHttpGetProxyForUrl(
        HINTERNET hSession,
        LPCWSTR lpcwszUrl,
        WINHTTP_AUTOPROXY_OPTIONS* pAutoProxyOptions,
        WINHTTP_PROXY_INFO* pProxyInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSession", "lpcwszUrl", "pAutoProxyOptions", "pProxyInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpGetProxyForUrlEx(jitter):
    """
    [ERROR_CODE] WinHttpGetProxyForUrlEx(
        HINTERNET hResolver,
        PCWSTR pcwszUrl,
        WINHTTP_AUTOPROXY_OPTIONS* pAutoProxyOptions,
        DWORD_PTR pContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hResolver", "pcwszUrl", "pAutoProxyOptions", "pContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpGetProxyResult(jitter):
    """
    [ERROR_CODE] WinHttpGetProxyResult(
        HINTERNET hResolver,
        WINHTTP_PROXY_RESULT* pProxyResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hResolver", "pProxyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpOpen(jitter):
    """
    HINTERNET WinHttpOpen(
        LPCWSTR pwszUserAgent,
        [HttpOpenAccessType] dwAccessType,
        LPCWSTR pwszProxyName,
        LPCWSTR pwszProxyBypass,
        [WinHttpOpenFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszUserAgent", "dwAccessType", "pwszProxyName", "pwszProxyBypass", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpOpenRequest(jitter):
    """
    HINTERNET WinHttpOpenRequest(
        HINTERNET hConnect,
        LPCWSTR pwszVerb,
        LPCWSTR pwszObjectName,
        LPCWSTR pwszVersion,
        LPCWSTR pwszReferrer,
        LPCWSTR* ppwszAcceptTypes,
        [WinHttpOpenRequestFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "pwszVerb", "pwszObjectName", "pwszVersion", "pwszReferrer", "ppwszAcceptTypes", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpQueryAuthSchemes(jitter):
    """
    BOOL WinHttpQueryAuthSchemes(
        HINTERNET hRequest,
        LPDWORD lpdwSupportedSchemes,
        LPDWORD lpdwFirstScheme,
        LPDWORD pdwAuthTarget
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "lpdwSupportedSchemes", "lpdwFirstScheme", "pdwAuthTarget"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpQueryDataAvailable(jitter):
    """
    BOOL WinHttpQueryDataAvailable(
        HINTERNET hRequest,
        LPDWORD lpdwNumberOfBytesAvailable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "lpdwNumberOfBytesAvailable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpQueryHeaders(jitter):
    """
    BOOL WinHttpQueryHeaders(
        HINTERNET hRequest,
        [WinHttpQueryLevelFlags] dwInfoLevel,
        LPCWSTR pwszName,
        LPVOID lpBuffer,
        LPDWORD lpdwBufferLength,
        LPDWORD lpdwIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "dwInfoLevel", "pwszName", "lpBuffer", "lpdwBufferLength", "lpdwIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpQueryOption(jitter):
    """
    BOOL WinHttpQueryOption(
        HINTERNET hInternet,
        [WinHttpOption] dwOption,
        LPVOID lpBuffer,
        LPDWORD lpdwBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "dwOption", "lpBuffer", "lpdwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpReadData(jitter):
    """
    BOOL WinHttpReadData(
        HINTERNET hRequest,
        LPVOID lpBuffer,
        DWORD dwNumberOfBytesToRead,
        LPDWORD lpdwNumberOfBytesRead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "lpBuffer", "dwNumberOfBytesToRead", "lpdwNumberOfBytesRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpReceiveResponse(jitter):
    """
    BOOL WinHttpReceiveResponse(
        HINTERNET hRequest,
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpResetAutoProxy(jitter):
    """
    [ERROR_CODE] WinHttpResetAutoProxy(
        HINTERNET hSession,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSession", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpSendRequest(jitter):
    """
    BOOL WinHttpSendRequest(
        HINTERNET hRequest,
        LPCWSTR pwszHeaders,
        DWORD dwHeadersLength,
        LPVOID lpOptional,
        DWORD dwOptionalLength,
        DWORD dwTotalLength,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "pwszHeaders", "dwHeadersLength", "lpOptional", "dwOptionalLength", "dwTotalLength", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpSetCredentials(jitter):
    """
    BOOL WinHttpSetCredentials(
        HINTERNET hRequest,
        DWORD AuthTargets,
        DWORD AuthScheme,
        LPCWSTR pwszUserName,
        LPCWSTR pwszPassword,
        LPVOID pAuthParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "AuthTargets", "AuthScheme", "pwszUserName", "pwszPassword", "pAuthParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpSetDefaultProxyConfiguration(jitter):
    """
    BOOL WinHttpSetDefaultProxyConfiguration(
        WINHTTP_PROXY_INFO* pProxyInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxyInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpSetOption(jitter):
    """
    BOOL WinHttpSetOption(
        HINTERNET hInternet,
        [WinHttpOption] dwOption,
        LPVOID lpBuffer,
        DWORD dwBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "dwOption", "lpBuffer", "dwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpSetStatusCallback(jitter):
    """
    WINHTTP_STATUS_CALLBACK WinHttpSetStatusCallback(
        HINTERNET hInternet,
        WINHTTP_STATUS_CALLBACK lpfnInternetCallback,
        [CallbackNotificationFlags] dwNotificationFlags,
        DWORD_PTR dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "lpfnInternetCallback", "dwNotificationFlags", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpSetTimeouts(jitter):
    """
    BOOL WinHttpSetTimeouts(
        HINTERNET hInternet,
        int dwResolveTimeout,
        int dwConnectTimeout,
        int dwSendTimeout,
        int dwReceiveTimeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "dwResolveTimeout", "dwConnectTimeout", "dwSendTimeout", "dwReceiveTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpTimeFromSystemTime(jitter):
    """
    BOOL WinHttpTimeFromSystemTime(
        SYSTEMTIME* pst,
        LPWSTR pwszTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pst", "pwszTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpTimeToSystemTime(jitter):
    """
    BOOL WinHttpTimeToSystemTime(
        LPCWSTR pwszTime,
        SYSTEMTIME* pst
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszTime", "pst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWriteData(jitter):
    """
    BOOL WinHttpWriteData(
        HINTERNET hRequest,
        LPCVOID lpBuffer,
        DWORD dwNumberOfBytesToWrite,
        LPDWORD lpdwNumberOfBytesWritten
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "lpBuffer", "dwNumberOfBytesToWrite", "lpdwNumberOfBytesWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWebSocketClose(jitter):
    """
    [ERROR_CODE] WinHttpWebSocketClose(
        HINTERNET hWebSocket,
        WINHTTP_WEB_SOCKET_CLOSE_STATUS usStatus,
        PVOID pvReason,
        DWORD dwReasonLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "usStatus", "pvReason", "dwReasonLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWebSocketCompleteUpgrade(jitter):
    """
    HINTERNET WinHttpWebSocketCompleteUpgrade(
        HINTERNET hRequest,
        DWORD_PTR pContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "pContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWebSocketQueryCloseStatus(jitter):
    """
    [ERROR_CODE] WinHttpWebSocketQueryCloseStatus(
        HINTERNET hWebSocket,
        WINHTTP_WEB_SOCKET_CLOSE_STATUS* pusStatus,
        PVOID pvReason,
        DWORD dwReasonLength,
        DWORD* pdwReasonLengthConsumed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pusStatus", "pvReason", "dwReasonLength", "pdwReasonLengthConsumed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWebSocketReceive(jitter):
    """
    [ERROR_CODE] WinHttpWebSocketReceive(
        HINTERNET hWebSocket,
        PVOID pvBuffer,
        DWORD dwBufferLength,
        DWORD* pdwBytesRead,
        WINHTTP_WEB_SOCKET_BUFFER_TYPE* peBufferType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pvBuffer", "dwBufferLength", "pdwBytesRead", "peBufferType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWebSocketSend(jitter):
    """
    [ERROR_CODE] WinHttpWebSocketSend(
        HINTERNET hWebSocket,
        WINHTTP_WEB_SOCKET_BUFFER_TYPE eBufferType,
        PVOID pvBuffer,
        DWORD dwBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "eBufferType", "pvBuffer", "dwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWebSocketShutdown(jitter):
    """
    [ERROR_CODE] WinHttpWebSocketShutdown(
        HINTERNET hWebSocket,
        WINHTTP_WEB_SOCKET_CLOSE_STATUS usStatus,
        PVOID pvReason,
        DWORD dwReasonLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "usStatus", "pvReason", "dwReasonLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
