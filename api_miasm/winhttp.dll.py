
def winhttp_WinHttpAddRequestHeaders(jitter):
    """
    [Winhttp.dll] BOOL WinHttpAddRequestHeaders(HINTERNET hRequest, LPCWSTR pwszHeaders, DWORD dwHeadersLength, [WinHttpAddReqFlag] dwModifiers)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "pwszHeaders", "dwHeadersLength", "dwModifiers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpCheckPlatform(jitter):
    """
    [Winhttp.dll] BOOL WinHttpCheckPlatform()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpCloseHandle(jitter):
    """
    [Winhttp.dll] BOOL WinHttpCloseHandle(HINTERNET hInternet)
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpConnect(jitter):
    """
    [Winhttp.dll] HINTERNET WinHttpConnect(HINTERNET hSession, LPCWSTR pswzServerName, INTERNET_PORT nServerPort, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSession", "pswzServerName", "nServerPort", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpCrackUrl(jitter):
    """
    [Winhttp.dll] BOOL WinHttpCrackUrl(LPCWSTR pwszUrl, DWORD dwUrlLength, [InternetCrackUrlFlags] dwFlags, LPURL_COMPONENTSW lpUrlComponents)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszUrl", "dwUrlLength", "dwFlags", "lpUrlComponents"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpCreateProxyResolver(jitter):
    """
    [Winhttp.dll] [ERROR_CODE] WinHttpCreateProxyResolver(HINTERNET hSession, HINTERNET* phResolver)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSession", "phResolver"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpCreateUrl(jitter):
    """
    [Winhttp.dll] BOOL WinHttpCreateUrl(LPURL_COMPONENTSW lpUrlComponents, [InternetCrackUrlFlags] dwFlags, LPWSTR pwszUrl, LPDWORD lpdwUrlLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpUrlComponents", "dwFlags", "pwszUrl", "lpdwUrlLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpDetectAutoProxyConfigUrl(jitter):
    """
    [Winhttp.dll] BOOL WinHttpDetectAutoProxyConfigUrl(DWORD dwAutoDetectFlags, LPWSTR* ppwszAutoConfigUrl)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwAutoDetectFlags", "ppwszAutoConfigUrl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpFreeProxyResult(jitter):
    """
    [Winhttp.dll] VOID WinHttpFreeProxyResult(WINHTTP_PROXY_RESULT* pProxyResult)
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpGetDefaultProxyConfiguration(jitter):
    """
    [Winhttp.dll] BOOL WinHttpGetDefaultProxyConfiguration(WINHTTP_PROXY_INFO* pProxyInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxyInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpGetIEProxyConfigForCurrentUser(jitter):
    """
    [Winhttp.dll] BOOL WinHttpGetIEProxyConfigForCurrentUser(WINHTTP_CURRENT_USER_IE_PROXY_CONFIG* pProxyConfig)
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxyConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpGetProxyForUrl(jitter):
    """
    [Winhttp.dll] BOOL WinHttpGetProxyForUrl(HINTERNET hSession, LPCWSTR lpcwszUrl, WINHTTP_AUTOPROXY_OPTIONS* pAutoProxyOptions, WINHTTP_PROXY_INFO* pProxyInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSession", "lpcwszUrl", "pAutoProxyOptions", "pProxyInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpGetProxyForUrlEx(jitter):
    """
    [Winhttp.dll] [ERROR_CODE] WinHttpGetProxyForUrlEx(HINTERNET hResolver, PCWSTR pcwszUrl, WINHTTP_AUTOPROXY_OPTIONS* pAutoProxyOptions, DWORD_PTR pContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["hResolver", "pcwszUrl", "pAutoProxyOptions", "pContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpGetProxyResult(jitter):
    """
    [Winhttp.dll] [ERROR_CODE] WinHttpGetProxyResult(HINTERNET hResolver, WINHTTP_PROXY_RESULT* pProxyResult)
    """
    ret_ad, args = jitter.func_args_stdcall(["hResolver", "pProxyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpOpen(jitter):
    """
    [Winhttp.dll] HINTERNET WinHttpOpen(LPCWSTR pwszUserAgent, [HttpOpenAccessType] dwAccessType, LPCWSTR pwszProxyName, LPCWSTR pwszProxyBypass, [WinHttpOpenFlags] dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszUserAgent", "dwAccessType", "pwszProxyName", "pwszProxyBypass", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpOpenRequest(jitter):
    """
    [Winhttp.dll] HINTERNET WinHttpOpenRequest(HINTERNET hConnect, LPCWSTR pwszVerb, LPCWSTR pwszObjectName, LPCWSTR pwszVersion, LPCWSTR pwszReferrer, LPCWSTR* ppwszAcceptTypes, [WinHttpOpenRequestFlags] dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "pwszVerb", "pwszObjectName", "pwszVersion", "pwszReferrer", "ppwszAcceptTypes", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpQueryAuthSchemes(jitter):
    """
    [Winhttp.dll] BOOL WinHttpQueryAuthSchemes(HINTERNET hRequest, LPDWORD lpdwSupportedSchemes, LPDWORD lpdwFirstScheme, LPDWORD pdwAuthTarget)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "lpdwSupportedSchemes", "lpdwFirstScheme", "pdwAuthTarget"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpQueryDataAvailable(jitter):
    """
    [Winhttp.dll] BOOL WinHttpQueryDataAvailable(HINTERNET hRequest, LPDWORD lpdwNumberOfBytesAvailable)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "lpdwNumberOfBytesAvailable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpQueryHeaders(jitter):
    """
    [Winhttp.dll] BOOL WinHttpQueryHeaders(HINTERNET hRequest, [WinHttpQueryLevelFlags] dwInfoLevel, LPCWSTR pwszName, LPVOID lpBuffer, LPDWORD lpdwBufferLength, LPDWORD lpdwIndex)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "dwInfoLevel", "pwszName", "lpBuffer", "lpdwBufferLength", "lpdwIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpQueryOption(jitter):
    """
    [Winhttp.dll] BOOL WinHttpQueryOption(HINTERNET hInternet, [WinHttpOption] dwOption, LPVOID lpBuffer, LPDWORD lpdwBufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "dwOption", "lpBuffer", "lpdwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpReadData(jitter):
    """
    [Winhttp.dll] BOOL WinHttpReadData(HINTERNET hRequest, LPVOID lpBuffer, DWORD dwNumberOfBytesToRead, LPDWORD lpdwNumberOfBytesRead)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "lpBuffer", "dwNumberOfBytesToRead", "lpdwNumberOfBytesRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpReceiveResponse(jitter):
    """
    [Winhttp.dll] BOOL WinHttpReceiveResponse(HINTERNET hRequest, LPVOID lpReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpResetAutoProxy(jitter):
    """
    [Winhttp.dll] [ERROR_CODE] WinHttpResetAutoProxy(HINTERNET hSession, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hSession", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpSendRequest(jitter):
    """
    [Winhttp.dll] BOOL WinHttpSendRequest(HINTERNET hRequest, LPCWSTR pwszHeaders, DWORD dwHeadersLength, LPVOID lpOptional, DWORD dwOptionalLength, DWORD dwTotalLength, DWORD_PTR dwContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "pwszHeaders", "dwHeadersLength", "lpOptional", "dwOptionalLength", "dwTotalLength", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpSetCredentials(jitter):
    """
    [Winhttp.dll] BOOL WinHttpSetCredentials(HINTERNET hRequest, DWORD AuthTargets, DWORD AuthScheme, LPCWSTR pwszUserName, LPCWSTR pwszPassword, LPVOID pAuthParams)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "AuthTargets", "AuthScheme", "pwszUserName", "pwszPassword", "pAuthParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpSetDefaultProxyConfiguration(jitter):
    """
    [Winhttp.dll] BOOL WinHttpSetDefaultProxyConfiguration(WINHTTP_PROXY_INFO* pProxyInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxyInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpSetOption(jitter):
    """
    [Winhttp.dll] BOOL WinHttpSetOption(HINTERNET hInternet, [WinHttpOption] dwOption, LPVOID lpBuffer, DWORD dwBufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "dwOption", "lpBuffer", "dwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpSetStatusCallback(jitter):
    """
    [Winhttp.dll] WINHTTP_STATUS_CALLBACK WinHttpSetStatusCallback(HINTERNET hInternet, WINHTTP_STATUS_CALLBACK lpfnInternetCallback, [CallbackNotificationFlags] dwNotificationFlags, DWORD_PTR dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "lpfnInternetCallback", "dwNotificationFlags", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpSetTimeouts(jitter):
    """
    [Winhttp.dll] BOOL WinHttpSetTimeouts(HINTERNET hInternet, int dwResolveTimeout, int dwConnectTimeout, int dwSendTimeout, int dwReceiveTimeout)
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "dwResolveTimeout", "dwConnectTimeout", "dwSendTimeout", "dwReceiveTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpTimeFromSystemTime(jitter):
    """
    [Winhttp.dll] BOOL WinHttpTimeFromSystemTime(SYSTEMTIME* pst, LPWSTR pwszTime)
    """
    ret_ad, args = jitter.func_args_stdcall(["pst", "pwszTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpTimeToSystemTime(jitter):
    """
    [Winhttp.dll] BOOL WinHttpTimeToSystemTime(LPCWSTR pwszTime, SYSTEMTIME* pst)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszTime", "pst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWriteData(jitter):
    """
    [Winhttp.dll] BOOL WinHttpWriteData(HINTERNET hRequest, LPCVOID lpBuffer, DWORD dwNumberOfBytesToWrite, LPDWORD lpdwNumberOfBytesWritten)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "lpBuffer", "dwNumberOfBytesToWrite", "lpdwNumberOfBytesWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWebSocketClose(jitter):
    """
    [Winhttp.dll] [ERROR_CODE] WinHttpWebSocketClose(HINTERNET hWebSocket, WINHTTP_WEB_SOCKET_CLOSE_STATUS usStatus, PVOID pvReason, DWORD dwReasonLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "usStatus", "pvReason", "dwReasonLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWebSocketCompleteUpgrade(jitter):
    """
    [Winhttp.dll] HINTERNET WinHttpWebSocketCompleteUpgrade(HINTERNET hRequest, DWORD_PTR pContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "pContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWebSocketQueryCloseStatus(jitter):
    """
    [Winhttp.dll] [ERROR_CODE] WinHttpWebSocketQueryCloseStatus(HINTERNET hWebSocket, WINHTTP_WEB_SOCKET_CLOSE_STATUS* pusStatus, PVOID pvReason, DWORD dwReasonLength, DWORD* pdwReasonLengthConsumed)
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pusStatus", "pvReason", "dwReasonLength", "pdwReasonLengthConsumed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWebSocketReceive(jitter):
    """
    [Winhttp.dll] [ERROR_CODE] WinHttpWebSocketReceive(HINTERNET hWebSocket, PVOID pvBuffer, DWORD dwBufferLength, DWORD* pdwBytesRead, WINHTTP_WEB_SOCKET_BUFFER_TYPE* peBufferType)
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pvBuffer", "dwBufferLength", "pdwBytesRead", "peBufferType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWebSocketSend(jitter):
    """
    [Winhttp.dll] [ERROR_CODE] WinHttpWebSocketSend(HINTERNET hWebSocket, WINHTTP_WEB_SOCKET_BUFFER_TYPE eBufferType, PVOID pvBuffer, DWORD dwBufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "eBufferType", "pvBuffer", "dwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winhttp_WinHttpWebSocketShutdown(jitter):
    """
    [Winhttp.dll] [ERROR_CODE] WinHttpWebSocketShutdown(HINTERNET hWebSocket, WINHTTP_WEB_SOCKET_CLOSE_STATUS usStatus, PVOID pvReason, DWORD dwReasonLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "usStatus", "pvReason", "dwReasonLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
