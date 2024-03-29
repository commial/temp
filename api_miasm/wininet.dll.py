###### Enums ######
_InternetService_ = {
    "INTERNET_SERVICE_FTP": 1,
    "INTERNET_SERVICE_GOPHER": 2,
    "INTERNET_SERVICE_HTTP": 3,
}
_InternetService__INV = {
    1: "INTERNET_SERVICE_FTP",
    2: "INTERNET_SERVICE_GOPHER",
    3: "INTERNET_SERVICE_HTTP",
}
_InternetOpenType_ = {
    "INTERNET_OPEN_TYPE_PRECONFIG": 0,
    "INTERNET_OPEN_TYPE_DIRECT": 1,
    "INTERNET_OPEN_TYPE_PROXY": 3,
    "INTERNET_OPEN_TYPE_PRECONFIG_WITH_NO_AUTOPROXY": 4,
}
_InternetOpenType__INV = {
    0: "INTERNET_OPEN_TYPE_PRECONFIG",
    1: "INTERNET_OPEN_TYPE_DIRECT",
    3: "INTERNET_OPEN_TYPE_PROXY",
    4: "INTERNET_OPEN_TYPE_PRECONFIG_WITH_NO_AUTOPROXY",
}
InternetCookieState = {
    "COOKIE_STATE_UNKNOWN": 0x0,
    "COOKIE_STATE_ACCEPT": 0x1,
    "COOKIE_STATE_PROMPT": 0x2,
    "COOKIE_STATE_LEASH": 0x3,
    "COOKIE_STATE_DOWNGRADE": 0x4,
    "COOKIE_STATE_REJECT": 0x5,
}
InternetCookieState_INV = {
    0x0: "COOKIE_STATE_UNKNOWN",
    0x1: "COOKIE_STATE_ACCEPT",
    0x2: "COOKIE_STATE_PROMPT",
    0x3: "COOKIE_STATE_LEASH",
    0x4: "COOKIE_STATE_DOWNGRADE",
    0x5: "COOKIE_STATE_REJECT",
}
FORTCMD = {
    "FORTCMD_LOGON": 1,
    "FORTCMD_LOGOFF": 2,
    "FORTCMD_CHG_PERSONALITY": 3,
}
FORTCMD_INV = {
    1: "FORTCMD_LOGON",
    2: "FORTCMD_LOGOFF",
    3: "FORTCMD_CHG_PERSONALITY",
}
APP_CACHE_STATE = {
    "AppCacheStateNoUpdateNeeded": 0,
    "AppCacheStateUpdateNeeded": 1,
    "AppCacheStateUpdateNeededNew": 2,
    "AppCacheStateUpdateNeededMasterOnly": 3,
}
APP_CACHE_STATE_INV = {
    0: "AppCacheStateNoUpdateNeeded",
    1: "AppCacheStateUpdateNeeded",
    2: "AppCacheStateUpdateNeededNew",
    3: "AppCacheStateUpdateNeededMasterOnly",
}
URL_CACHE_LIMIT_TYPE = {
    "UrlCacheLimitTypeIE": 0,
    "UrlCacheLimitTypeIETotal": 1,
    "UrlCacheLimitTypeAppContainer": 2,
    "UrlCacheLimitTypeAppContainerTotal": 3,
    "UrlCacheLimitTypeNum": 4,
}
URL_CACHE_LIMIT_TYPE_INV = {
    0: "UrlCacheLimitTypeIE",
    1: "UrlCacheLimitTypeIETotal",
    2: "UrlCacheLimitTypeAppContainer",
    3: "UrlCacheLimitTypeAppContainerTotal",
    4: "UrlCacheLimitTypeNum",
}
HTTP_PUSH_WAIT_TYPE = {
    "HttpPushWaitEnableComplete": 0,
    "HttpPushWaitReceiveComplete": 1,
    "HttpPushWaitSendComplete": 2,
}
HTTP_PUSH_WAIT_TYPE_INV = {
    0: "HttpPushWaitEnableComplete",
    1: "HttpPushWaitReceiveComplete",
    2: "HttpPushWaitSendComplete",
}
APP_CACHE_FINALIZE_STATE = {
    "AppCacheFinalizeStateIncomplete": 0,
    "AppCacheFinalizeStateManifestChange": 1,
    "AppCacheFinalizeStateComplete": 2,
}
APP_CACHE_FINALIZE_STATE_INV = {
    0: "AppCacheFinalizeStateIncomplete",
    1: "AppCacheFinalizeStateManifestChange",
    2: "AppCacheFinalizeStateComplete",
}
WPAD_CACHE_DELETE = {
    "WPAD_CACHE_DELETE_CURRENT": 0x0,
    "WPAD_CACHE_DELETE_ALL": 0x1,
}
WPAD_CACHE_DELETE_INV = {
    0x0: "WPAD_CACHE_DELETE_CURRENT",
    0x1: "WPAD_CACHE_DELETE_ALL",
}
P3PStatus = {
    "P3P_Success": 0x0,
    "P3P_NoPolicy": 0x2,
    "P3P_InProgress": 0x3,
    "P3P_Failed": 0x4,
    "P3P_NotFound": 0x5,
    "P3P_FormatErr": 0x6,
    "P3P_Cancelled": 0x7,
    "P3P_NotStarted": 0x8,
    "P3P_XMLError": 0x9,
    "P3P_Expired": 0xA,
    "P3P_Error": 0xFF,
}
P3PStatus_INV = {
    0x0: "P3P_Success",
    0x2: "P3P_NoPolicy",
    0x3: "P3P_InProgress",
    0x4: "P3P_Failed",
    0x5: "P3P_NotFound",
    0x6: "P3P_FormatErr",
    0x7: "P3P_Cancelled",
    0x8: "P3P_NotStarted",
    0x9: "P3P_XMLError",
    0xA: "P3P_Expired",
    0xFF: "P3P_Error",
}
HTTP_WEB_SOCKET_BUFFER_TYPE = {
    "HTTP_WEB_SOCKET_BINARY_MESSAGE_TYPE": 0,
    "HTTP_WEB_SOCKET_BINARY_FRAGMENT_TYPE": 1,
    "HTTP_WEB_SOCKET_UTF8_MESSAGE_TYPE": 2,
    "HTTP_WEB_SOCKET_UTF8_FRAGMENT_TYPE": 3,
    "HTTP_WEB_SOCKET_CLOSE_TYPE": 4,
    "HTTP_WEB_SOCKET_PING_TYPE": 5,
}
HTTP_WEB_SOCKET_BUFFER_TYPE_INV = {
    0: "HTTP_WEB_SOCKET_BINARY_MESSAGE_TYPE",
    1: "HTTP_WEB_SOCKET_BINARY_FRAGMENT_TYPE",
    2: "HTTP_WEB_SOCKET_UTF8_MESSAGE_TYPE",
    3: "HTTP_WEB_SOCKET_UTF8_FRAGMENT_TYPE",
    4: "HTTP_WEB_SOCKET_CLOSE_TYPE",
    5: "HTTP_WEB_SOCKET_PING_TYPE",
}
HTTP_WEB_SOCKET_CLOSE_STATUS = {
    "HTTP_WEB_SOCKET_SUCCESS_CLOSE_STATUS": 1000,
    "HTTP_WEB_SOCKET_ENDPOINT_TERMINATED_CLOSE_STATUS": 1001,
    "HTTP_WEB_SOCKET_PROTOCOL_ERROR_CLOSE_STATUS": 1002,
    "HTTP_WEB_SOCKET_INVALID_DATA_TYPE_CLOSE_STATUS": 1003,
    "HTTP_WEB_SOCKET_EMPTY_CLOSE_STATUS": 1005,
    "HTTP_WEB_SOCKET_ABORTED_CLOSE_STATUS": 1006,
    "HTTP_WEB_SOCKET_INVALID_PAYLOAD_CLOSE_STATUS": 1007,
    "HTTP_WEB_SOCKET_POLICY_VIOLATION_CLOSE_STATUS": 1008,
    "HTTP_WEB_SOCKET_MESSAGE_TOO_BIG_CLOSE_STATUS": 1009,
    "HTTP_WEB_SOCKET_UNSUPPORTED_EXTENSIONS_CLOSE_STATUS": 1010,
    "HTTP_WEB_SOCKET_SERVER_ERROR_CLOSE_STATUS": 1011,
    "HTTP_WEB_SOCKET_SECURE_HANDSHAKE_ERROR_CLOSE_STATUS": 1015,
}
HTTP_WEB_SOCKET_CLOSE_STATUS_INV = {
    1000: "HTTP_WEB_SOCKET_SUCCESS_CLOSE_STATUS",
    1001: "HTTP_WEB_SOCKET_ENDPOINT_TERMINATED_CLOSE_STATUS",
    1002: "HTTP_WEB_SOCKET_PROTOCOL_ERROR_CLOSE_STATUS",
    1003: "HTTP_WEB_SOCKET_INVALID_DATA_TYPE_CLOSE_STATUS",
    1005: "HTTP_WEB_SOCKET_EMPTY_CLOSE_STATUS",
    1006: "HTTP_WEB_SOCKET_ABORTED_CLOSE_STATUS",
    1007: "HTTP_WEB_SOCKET_INVALID_PAYLOAD_CLOSE_STATUS",
    1008: "HTTP_WEB_SOCKET_POLICY_VIOLATION_CLOSE_STATUS",
    1009: "HTTP_WEB_SOCKET_MESSAGE_TOO_BIG_CLOSE_STATUS",
    1010: "HTTP_WEB_SOCKET_UNSUPPORTED_EXTENSIONS_CLOSE_STATUS",
    1011: "HTTP_WEB_SOCKET_SERVER_ERROR_CLOSE_STATUS",
    1015: "HTTP_WEB_SOCKET_SECURE_HANDSHAKE_ERROR_CLOSE_STATUS",
}

###################

###### Types ######
HTTP_PUSH_WAIT_HANDLE = HANDLE
HTTP_PUSH_WAIT_HANDLE_PTR = Ptr("<I", HTTP_PUSH_WAIT_HANDLE())
APP_CACHE_HANDLE = PVOID
APP_CACHE_HANDLE_PTR = Ptr("<I", APP_CACHE_HANDLE())
HTTP_DEPENDENCY_HANDLE = PVOID
HTTP_DEPENDENCY_HANDLE_PTR = Ptr("<I", HTTP_DEPENDENCY_HANDLE())
URLCACHE_HANDLE = PVOID
URLCACHE_HANDLE_PTR = Ptr("<I", URLCACHE_HANDLE())
CACHE_OPERATOR = LPVOID
BSTR_PTR_PTR = Ptr("<I", BSTR_PTR())
P3PURL = LPSTR
P3PCURL = LPSTR
P3PVERB = LPSTR
P3PCXSL = BSTR
P3PHANDLE = LPVOID
WCHAR__SZ_ALG_MAX_SIZE_ = Array(WCHAR, 64)
_InternetService_ = DWORD
_CacheEntryType_ = DWORD
_InternetGetConnectedStateFlags_ = DWORD
_InternetGetConnectedStateFlags_PTR_ = Ptr("<I", _InternetGetConnectedStateFlags_())
_InternetOpenType_ = DWORD
_InternetOpenFlags_ = DWORD
_InternetFlags_ = DWORD
_InternetReadFileFlags_ = DWORD
_HttpAddReqFlag_ = DWORD
_InternetCookieFlags_ = DWORD
_InternetErrorDlgFlags_ = DWORD
_CacheEntryFieldControl_ = DWORD
InternetCookieState = DWORD
FORTCMD = UINT
FORTSTAT = DWORD
FORTSTAT_PTR = Ptr("<I", FORTSTAT())
_INTERNET_CACHE_CONTAINER_FLAGS_ = DWORD
_CACHE_FIND_CONTAINER_FLAGS_ = DWORD
_CACHE_CONFIG_FC_ = DWORD
_CACHE_NOTIFY_FILTER_OPTIONS_ = DWORD
_APP_CACHE_LOOKUP_FLAGS_ = DWORD

class SecPkgContext_ConnectionInfo(MemStruct):
    fields = [
        ("dwProtocol", DWORD()),
        ("aiCipher", ALG_ID()),
        ("dwCipherStrength", DWORD()),
        ("aiHash", ALG_ID()),
        ("dwHashStrength", DWORD()),
        ("aiExch", ALG_ID()),
        ("dwExchStrength", DWORD()),
    ]


class SecPkgContext_CipherInfo(MemStruct):
    fields = [
        ("dwVersion", DWORD()),
        ("dwProtocol", DWORD()),
        ("dwCipherSuite", DWORD()),
        ("dwBaseCipherSuite", DWORD()),
        ("szCipherSuite", WCHAR__SZ_ALG_MAX_SIZE_()),
        ("szCipher", WCHAR__SZ_ALG_MAX_SIZE_()),
        ("dwCipherLen", DWORD()),
        ("dwCipherBlockLen", DWORD()),
        ("szHash", WCHAR__SZ_ALG_MAX_SIZE_()),
        ("dwHashLen", DWORD()),
        ("szExchange", WCHAR__SZ_ALG_MAX_SIZE_()),
        ("dwMinExchangeLen", DWORD()),
        ("dwMaxExchangeLen", DWORD()),
        ("szCertificate", WCHAR__SZ_ALG_MAX_SIZE_()),
        ("dwKeyType", DWORD()),
    ]


class SEC_CHANNEL_BINDINGS(MemStruct):
    fields = [
        ("dwInitiatorAddrType", unsigned_long()),
        ("cbInitiatorLength", unsigned_long()),
        ("dwInitiatorOffset", unsigned_long()),
        ("dwAcceptorAddrType", unsigned_long()),
        ("cbAcceptorLength", unsigned_long()),
        ("dwAcceptorOffset", unsigned_long()),
        ("cbApplicationDataLength", unsigned_long()),
        ("dwApplicationDataOffset", unsigned_long()),
    ]

SEC_CHANNEL_BINDINGS_PTR = Ptr("<I", SEC_CHANNEL_BINDINGS())

class SecPkgContext_Bindings(MemStruct):
    fields = [
        ("BindingsLength", unsigned_long()),
        ("Bindings", SEC_CHANNEL_BINDINGS_PTR()),
    ]


class INTERNET_SECURITY_INFO(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("pCertificate", PCCERT_CONTEXT()),
        ("pcCertChain", PCCERT_CHAIN_CONTEXT()),
        ("connectionInfo", SecPkgContext_ConnectionInfo()),
        ("cipherInfo", SecPkgContext_CipherInfo()),
        ("pcUnverifiedCertChain", PCCERT_CHAIN_CONTEXT()),
        ("channelBindingToken", SecPkgContext_Bindings()),
    ]

LPINTERNET_SECURITY_INFO = Ptr("<I", INTERNET_SECURITY_INFO())
APP_CACHE_STATE = UINT
APP_CACHE_STATE_PTR = Ptr("<I", APP_CACHE_STATE())
URL_CACHE_LIMIT_TYPE = UINT
_APP_CACHE_ENTRY_TYPE_ = DWORD

class APP_CACHE_DOWNLOAD_ENTRY(MemStruct):
    fields = [
        ("pwszUrl", PWSTR()),
        ("dwEntryType", _APP_CACHE_ENTRY_TYPE_()),
    ]

APP_CACHE_DOWNLOAD_ENTRY_PTR = Ptr("<I", APP_CACHE_DOWNLOAD_ENTRY())

class APP_CACHE_DOWNLOAD_LIST(MemStruct):
    fields = [
        ("dwEntryCount", DWORD()),
        ("pEntries", APP_CACHE_DOWNLOAD_ENTRY_PTR()),
    ]

APP_CACHE_DOWNLOAD_LIST_PTR = Ptr("<I", APP_CACHE_DOWNLOAD_LIST())

class HTTP_PUSH_TRANSPORT_SETTING(MemStruct):
    fields = [
        ("TransportSettingId", GUID()),
        ("BrokerEventId", GUID()),
    ]

HTTP_PUSH_TRANSPORT_SETTING_PTR = Ptr("<I", HTTP_PUSH_TRANSPORT_SETTING())
HTTP_PUSH_WAIT_TYPE = UINT

class HTTP_PUSH_NOTIFICATION_STATUS(MemStruct):
    fields = [
        ("ChannelStatusValid", BOOL()),
        ("ChannelStatus", DWORD()),
    ]

HTTP_PUSH_NOTIFICATION_STATUS_PTR = Ptr("<I", HTTP_PUSH_NOTIFICATION_STATUS())
APP_CACHE_FINALIZE_STATE = UINT
APP_CACHE_FINALIZE_STATE_PTR = Ptr("<I", APP_CACHE_FINALIZE_STATE())

class APP_CACHE_GROUP_INFO(MemStruct):
    fields = [
        ("pwszManifestUrl", PWSTR()),
        ("ftLastAccessTime", FILETIME()),
        ("ullSize", ULONGLONG()),
    ]

APP_CACHE_GROUP_INFO_PTR = Ptr("<I", APP_CACHE_GROUP_INFO())

class APP_CACHE_GROUP_LIST(MemStruct):
    fields = [
        ("dwAppCacheGroupCount", DWORD()),
        ("pAppCacheGroups", APP_CACHE_GROUP_INFO_PTR()),
    ]

APP_CACHE_GROUP_LIST_PTR = Ptr("<I", APP_CACHE_GROUP_LIST())

class URLCACHE_ENTRY_INFO(MemStruct):
    fields = [
        ("pwszSourceUrlName", PWSTR()),
        ("pwszLocalFileName", PWSTR()),
        ("dwCacheEntryType", DWORD()),
        ("dwUseCount", DWORD()),
        ("dwHitRate", DWORD()),
        ("dwSizeLow", DWORD()),
        ("dwSizeHigh", DWORD()),
        ("ftLastModifiedTime", FILETIME()),
        ("ftExpireTime", FILETIME()),
        ("ftLastAccessTime", FILETIME()),
        ("ftLastSyncTime", FILETIME()),
        # Length is `cbHeaderInfoSize`
        ("pbHeaderInfo", PBYTE()),
        ("cbHeaderInfoSize", DWORD()),
        # Length is `cbExtraDataSize`
        ("pbExtraData", PBYTE()),
        ("cbExtraDataSize", DWORD()),
    ]

PURLCACHE_ENTRY_INFO = Ptr("<I", URLCACHE_ENTRY_INFO())

class WININET_PROXY_INFO(MemStruct):
    fields = [
        ("fProxy", BOOL()),
        ("fBypass", BOOL()),
        ("ProxyScheme", INTERNET_SCHEME()),
        ("pwszProxy", PWSTR()),
        ("ProxyPort", INTERNET_PORT()),
    ]

WININET_PROXY_INFO_PTR = Ptr("<I", WININET_PROXY_INFO())

class WININET_PROXY_INFO_LIST(MemStruct):
    fields = [
        ("dwProxyInfoCount", DWORD()),
        ("pProxyInfo", WININET_PROXY_INFO_PTR()),
    ]

WININET_PROXY_INFO_LIST_PTR = Ptr("<I", WININET_PROXY_INFO_LIST())

class INTERNET_CACHE_CONTAINER_INFO(MemStruct):
    fields = [
        ("dwCacheVersion", DWORD()),
        ("lpszName", LPTSTR()),
        ("lpszCachePrefix", LPTSTR()),
        ("lpszVolumeLabel", LPTSTR()),
        ("lpszVolumeTitle", LPTSTR()),
    ]

LPINTERNET_CACHE_CONTAINER_INFO = Ptr("<I", INTERNET_CACHE_CONTAINER_INFO())

class INTERNET_CACHE_CONFIG_PATH_ENTRY(MemStruct):
    fields = [
        ("CachePath", TCHAR__MAX_PATH_()),
        ("dwCacheSize", DWORD()),
    ]

INTERNET_CACHE_CONFIG_PATH_ENTRY__ANYSIZE_ARRAY_ = Array(INTERNET_CACHE_CONFIG_PATH_ENTRY, 1)

class INTERNET_CACHE_CONFIG_INFO(MemStruct):
    fields = [
        ("dwStructSize", DWORD()),
        ("dwContainer", DWORD()),
        ("dwQuota", DWORD()),
        ("dwReserved4", DWORD()),
        ("fPerUser", BOOL()),
        ("dwSyncMode", DWORD()),
        ("dwNumCachePaths", DWORD()),
        ("CachePaths", INTERNET_CACHE_CONFIG_PATH_ENTRY__ANYSIZE_ARRAY_()),
        ("dwNormalUsage", DWORD()),
        ("dwExemptUsage", DWORD()),
    ]

LPINTERNET_CACHE_CONFIG_INFO = Ptr("<I", INTERNET_CACHE_CONFIG_INFO())
_INTERNET_DIAL_FLAGS_ = DWORD
_FTP_TRANSFER_FLAGS_ = DWORD
WPAD_CACHE_DELETE = UINT

class P3PResource(MemStruct):
    fields = [
        ("pszLocation", P3PCURL()),
        ("pszVerb", P3PVERB()),
        ("pszP3PHeaderRef", P3PCURL()),
        ("pszLinkTagRef", P3PCURL()),
        ("pContainer", LPVOID()),
    ]

P3PResource_PTR = Ptr("<I", P3PResource())

class P3PSignal(MemStruct):
    fields = [
        ("hwnd", HWND()),
        ("message", unsigned_int()),
        ("hEvent", HANDLE()),
        ("pContext", void_PTR()),
        ("hRequest", P3PHANDLE()),
    ]

P3PSignal_PTR = Ptr("<I", P3PSignal())
P3PStatus = int
HTTP_WEB_SOCKET_BUFFER_TYPE = UINT
HTTP_WEB_SOCKET_BUFFER_TYPE_PTR = Ptr("<I", HTTP_WEB_SOCKET_BUFFER_TYPE())
HTTP_WEB_SOCKET_CLOSE_STATUS = USHORT
HTTP_WEB_SOCKET_CLOSE_STATUS_PTR = Ptr("<I", HTTP_WEB_SOCKET_CLOSE_STATUS())

###################

###### Functions ######

def wininet_CommitUrlCacheEntry(jitter, get_str, set_str):
    """
    BOOLAPI CommitUrlCacheEntry(
        LPCTSTR lpszUrlName,
        LPCTSTR lpszLocalFileName,
        FILETIME ExpireTime,
        FILETIME LastModifiedTime,
        [CacheEntryType] CacheEntryType,
        LPVOID lpHeaderInfo,
        DWORD dwHeaderSize,
        LPCTSTR lpszFileExtension,
        LPCTSTR lpszOriginalUrl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName", "lpszLocalFileName", "ExpireTime", "LastModifiedTime", "CacheEntryType", "lpHeaderInfo", "dwHeaderSize", "lpszFileExtension", "lpszOriginalUrl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_CommitUrlCacheEntryA(jitter):
    wininet_CommitUrlCacheEntry(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_CommitUrlCacheEntryW(jitter):
    wininet_CommitUrlCacheEntry(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_CreateMD5SSOHash(jitter):
    """
    BOOL CreateMD5SSOHash(
        PWSTR pszChallengeInfo,
        PWSTR pwszRealm,
        PWSTR pwszTarget,
        PBYTE pbHexHash
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszChallengeInfo", "pwszRealm", "pwszTarget", "pbHexHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_CreateUrlCacheEntry(jitter, get_str, set_str):
    """
    BOOLAPI CreateUrlCacheEntry(
        LPCTSTR lpszUrlName,
        DWORD dwExpectedFileSize,
        LPCTSTR lpszFileExtension,
        LPTSTR lpszFileName,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName", "dwExpectedFileSize", "lpszFileExtension", "lpszFileName", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_CreateUrlCacheEntryA(jitter):
    wininet_CreateUrlCacheEntry(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_CreateUrlCacheEntryW(jitter):
    wininet_CreateUrlCacheEntry(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_CreateUrlCacheGroup(jitter):
    """
    GROUPID CreateUrlCacheGroup(
        DWORD dwFlags,
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_DeleteUrlCacheEntry(jitter, get_str, set_str):
    """
    BOOLAPI DeleteUrlCacheEntry(
        LPCTSTR lpszUrlName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_DeleteUrlCacheEntryA(jitter):
    wininet_DeleteUrlCacheEntry(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_DeleteUrlCacheEntryW(jitter):
    wininet_DeleteUrlCacheEntry(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_DeleteUrlCacheEntry(jitter):
    """
    BOOLAPI DeleteUrlCacheEntry(
        LPCSTR lpszUrlName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_DeleteUrlCacheGroup(jitter):
    """
    BOOL DeleteUrlCacheGroup(
        GROUPID GroupId,
        DWORD dwFlags,
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["GroupId", "dwFlags", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_DetectAutoProxyUrl(jitter):
    """
    BOOL DetectAutoProxyUrl(
        LPSTR lpszAutoProxyUrl,
        DWORD dwAutoProxyUrlLength,
        DWORD dwDetectFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszAutoProxyUrl", "dwAutoProxyUrlLength", "dwDetectFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FindCloseUrlCache(jitter):
    """
    BOOLAPI FindCloseUrlCache(
        HANDLE hEnumHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEnumHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FindFirstUrlCacheEntry(jitter, get_str, set_str):
    """
    HANDLE FindFirstUrlCacheEntry(
        LPCTSTR lpszUrlSearchPattern,
        LPINTERNET_CACHE_ENTRY_INFO lpFirstCacheEntryInfo,
        LPDWORD lpcbCacheEntryInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlSearchPattern", "lpFirstCacheEntryInfo", "lpcbCacheEntryInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FindFirstUrlCacheEntryA(jitter):
    wininet_FindFirstUrlCacheEntry(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FindFirstUrlCacheEntryW(jitter):
    wininet_FindFirstUrlCacheEntry(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FindFirstUrlCacheEntryEx(jitter, get_str, set_str):
    """
    HANDLE FindFirstUrlCacheEntryEx(
        LPCTSTR lpszUrlSearchPattern,
        DWORD dwFlags,
        DWORD dwFilter,
        GROUPID GroupId,
        LPINTERNET_CACHE_ENTRY_INFO lpFirstCacheEntryInfo,
        LPDWORD lpdwEntryInfo,
        LPVOID lpGroupAttributes,
        LPDWORD lpcbGroupAttributes,
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlSearchPattern", "dwFlags", "dwFilter", "GroupId", "lpFirstCacheEntryInfo", "lpdwEntryInfo", "lpGroupAttributes", "lpcbGroupAttributes", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FindFirstUrlCacheEntryExA(jitter):
    wininet_FindFirstUrlCacheEntryEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FindFirstUrlCacheEntryExW(jitter):
    wininet_FindFirstUrlCacheEntryEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FindFirstUrlCacheGroup(jitter):
    """
    HANDLE FindFirstUrlCacheGroup(
        DWORD dwFlags,
        DWORD dwFilter,
        LPVOID lpSearchCondition,
        DWORD dwSearchCondition,
        GROUPID* lpGroupId,
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "dwFilter", "lpSearchCondition", "dwSearchCondition", "lpGroupId", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FindNextUrlCacheEntry(jitter, get_str, set_str):
    """
    BOOLAPI FindNextUrlCacheEntry(
        HANDLE hEnumHandle,
        LPINTERNET_CACHE_ENTRY_INFO lpNextCacheEntryInfo,
        LPDWORD lpcbCacheEntryInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEnumHandle", "lpNextCacheEntryInfo", "lpcbCacheEntryInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FindNextUrlCacheEntryA(jitter):
    wininet_FindNextUrlCacheEntry(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FindNextUrlCacheEntryW(jitter):
    wininet_FindNextUrlCacheEntry(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FindNextUrlCacheEntryEx(jitter, get_str, set_str):
    """
    BOOL FindNextUrlCacheEntryEx(
        HANDLE hEnumHandle,
        LPINTERNET_CACHE_ENTRY_INFO lpNextCacheEntryInfo,
        LPDWORD lpcbEntryInfo,
        LPVOID lpGroupAttributes,
        LPDWORD lpcbGroupAttributes,
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEnumHandle", "lpNextCacheEntryInfo", "lpcbEntryInfo", "lpGroupAttributes", "lpcbGroupAttributes", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FindNextUrlCacheEntryExA(jitter):
    wininet_FindNextUrlCacheEntryEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FindNextUrlCacheEntryExW(jitter):
    wininet_FindNextUrlCacheEntryEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FindNextUrlCacheGroup(jitter):
    """
    BOOL FindNextUrlCacheGroup(
        HANDLE hFind,
        GROUPID* lpGroupId,
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFind", "lpGroupId", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpCommand(jitter, get_str, set_str):
    """
    BOOL FtpCommand(
        HINTERNET hConnect,
        BOOL fExpectResponse,
        DWORD dwFlags,
        LPCTSTR lpszCommand,
        DWORD_PTR dwContext,
        HINTERNET* phFtpCommand
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "fExpectResponse", "dwFlags", "lpszCommand", "dwContext", "phFtpCommand"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpCommandA(jitter):
    wininet_FtpCommand(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FtpCommandW(jitter):
    wininet_FtpCommand(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FtpCreateDirectory(jitter, get_str, set_str):
    """
    BOOL FtpCreateDirectory(
        HINTERNET hConnect,
        LPCTSTR lpszDirectory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszDirectory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpCreateDirectoryA(jitter):
    wininet_FtpCreateDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FtpCreateDirectoryW(jitter):
    wininet_FtpCreateDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FtpDeleteFile(jitter, get_str, set_str):
    """
    BOOL FtpDeleteFile(
        HINTERNET hConnect,
        LPCTSTR lpszFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpDeleteFileA(jitter):
    wininet_FtpDeleteFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FtpDeleteFileW(jitter):
    wininet_FtpDeleteFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FtpFindFirstFile(jitter, get_str, set_str):
    """
    HINTERNET FtpFindFirstFile(
        HINTERNET hConnect,
        LPCTSTR lpszSearchFile,
        LPWIN32_FIND_DATA lpFindFileData,
        DWORD dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszSearchFile", "lpFindFileData", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpFindFirstFileA(jitter):
    wininet_FtpFindFirstFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FtpFindFirstFileW(jitter):
    wininet_FtpFindFirstFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FtpGetCurrentDirectory(jitter, get_str, set_str):
    """
    BOOL FtpGetCurrentDirectory(
        HINTERNET hConnect,
        LPTSTR lpszCurrentDirectory,
        LPDWORD lpdwCurrentDirectory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszCurrentDirectory", "lpdwCurrentDirectory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpGetCurrentDirectoryA(jitter):
    wininet_FtpGetCurrentDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FtpGetCurrentDirectoryW(jitter):
    wininet_FtpGetCurrentDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FtpGetFile(jitter, get_str, set_str):
    """
    BOOL FtpGetFile(
        HINTERNET hConnect,
        LPCTSTR lpszRemoteFile,
        LPCTSTR lpszNewFile,
        BOOL fFailIfExists,
        [FileAttributes] dwFlagsAndAttributes,
        [FTP_TRANSFER_FLAGS] dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszRemoteFile", "lpszNewFile", "fFailIfExists", "dwFlagsAndAttributes", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpGetFileA(jitter):
    wininet_FtpGetFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FtpGetFileW(jitter):
    wininet_FtpGetFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FtpGetFileSize(jitter):
    """
    DWORD FtpGetFileSize(
        HINTERNET hFile,
        LPDWORD lpdwFileSizeHigh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpdwFileSizeHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpOpenFile(jitter, get_str, set_str):
    """
    HINTERNET FtpOpenFile(
        HINTERNET hConnect,
        LPCTSTR lpszFileName,
        DWORD dwAccess,
        DWORD dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszFileName", "dwAccess", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpOpenFileA(jitter):
    wininet_FtpOpenFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FtpOpenFileW(jitter):
    wininet_FtpOpenFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FtpPutFile(jitter, get_str, set_str):
    """
    BOOL FtpPutFile(
        HINTERNET hConnect,
        LPCTSTR lpszLocalFile,
        LPCTSTR lpszNewRemoteFile,
        [FTP_TRANSFER_FLAGS] dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszLocalFile", "lpszNewRemoteFile", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpPutFileA(jitter):
    wininet_FtpPutFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FtpPutFileW(jitter):
    wininet_FtpPutFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FtpRemoveDirectory(jitter, get_str, set_str):
    """
    BOOL FtpRemoveDirectory(
        HINTERNET hConnect,
        LPCTSTR lpszDirectory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszDirectory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpRemoveDirectoryA(jitter):
    wininet_FtpRemoveDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FtpRemoveDirectoryW(jitter):
    wininet_FtpRemoveDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FtpRenameFile(jitter, get_str, set_str):
    """
    BOOL FtpRenameFile(
        HINTERNET hConnect,
        LPCTSTR lpszExisting,
        LPCTSTR lpszNew
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszExisting", "lpszNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpRenameFileA(jitter):
    wininet_FtpRenameFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FtpRenameFileW(jitter):
    wininet_FtpRenameFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FtpSetCurrentDirectory(jitter, get_str, set_str):
    """
    BOOL FtpSetCurrentDirectory(
        HINTERNET hConnect,
        LPCTSTR lpszDirectory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszDirectory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpSetCurrentDirectoryA(jitter):
    wininet_FtpSetCurrentDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FtpSetCurrentDirectoryW(jitter):
    wininet_FtpSetCurrentDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_GetUrlCacheEntryInfo(jitter, get_str, set_str):
    """
    BOOL GetUrlCacheEntryInfo(
        LPCTSTR lpszUrlName,
        LPINTERNET_CACHE_ENTRY_INFO lpCacheEntryInfo,
        LPDWORD lpcbCacheEntryInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName", "lpCacheEntryInfo", "lpcbCacheEntryInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GetUrlCacheEntryInfoA(jitter):
    wininet_GetUrlCacheEntryInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_GetUrlCacheEntryInfoW(jitter):
    wininet_GetUrlCacheEntryInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_GetUrlCacheEntryInfoEx(jitter, get_str, set_str):
    """
    BOOLAPI GetUrlCacheEntryInfoEx(
        LPCTSTR lpszUrl,
        LPINTERNET_CACHE_ENTRY_INFO lpCacheEntryInfo,
        LPDWORD lpcbCacheEntryInfo,
        LPTSTR lpszRedirectUrl,
        LPDWORD lpcbRedirectUrl,
        LPVOID lpReserved,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrl", "lpCacheEntryInfo", "lpcbCacheEntryInfo", "lpszRedirectUrl", "lpcbRedirectUrl", "lpReserved", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GetUrlCacheEntryInfoExA(jitter):
    wininet_GetUrlCacheEntryInfoEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_GetUrlCacheEntryInfoExW(jitter):
    wininet_GetUrlCacheEntryInfoEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_GetUrlCacheGroupAttribute(jitter, get_str, set_str):
    """
    BOOL GetUrlCacheGroupAttribute(
        GROUPID gid,
        DWORD dwFlags,
        DWORD dwAttributes,
        LPINTERNET_CACHE_GROUP_INFO lpGroupInfo,
        LPDWORD lpdwGroupInfo,
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["gid", "dwFlags", "dwAttributes", "lpGroupInfo", "lpdwGroupInfo", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GetUrlCacheGroupAttributeA(jitter):
    wininet_GetUrlCacheGroupAttribute(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_GetUrlCacheGroupAttributeW(jitter):
    wininet_GetUrlCacheGroupAttribute(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_GopherCreateLocator(jitter, get_str, set_str):
    """
    BOOL GopherCreateLocator(
        LPCTSTR lpszHost,
        INTERNET_PORT nServerPort,
        LPCTSTR lpszDisplayString,
        LPCTSTR lpszSelectorString,
        DWORD dwGopherType,
        LPTSTR lpszLocator,
        LPDWORD lpdwBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszHost", "nServerPort", "lpszDisplayString", "lpszSelectorString", "dwGopherType", "lpszLocator", "lpdwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GopherCreateLocatorA(jitter):
    wininet_GopherCreateLocator(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_GopherCreateLocatorW(jitter):
    wininet_GopherCreateLocator(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_GopherFindFirstFile(jitter, get_str, set_str):
    """
    HINTERNET GopherFindFirstFile(
        HINTERNET hConnect,
        LPCTSTR lpszLocator,
        LPCTSTR lpszSearchString,
        LPGOPHER_FIND_DATA lpFindData,
        DWORD dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszLocator", "lpszSearchString", "lpFindData", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GopherFindFirstFileA(jitter):
    wininet_GopherFindFirstFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_GopherFindFirstFileW(jitter):
    wininet_GopherFindFirstFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_GopherGetAttribute(jitter, get_str, set_str):
    """
    BOOL GopherGetAttribute(
        HINTERNET hConnect,
        LPCTSTR lpszLocator,
        LPCTSTR lpszAttributeName,
        LPBYTE lpBuffer,
        DWORD dwBufferLength,
        LPDWORD lpdwCharactersReturned,
        GOPHER_ATTRIBUTE_ENUMERATOR lpfnEnumerator,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszLocator", "lpszAttributeName", "lpBuffer", "dwBufferLength", "lpdwCharactersReturned", "lpfnEnumerator", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GopherGetAttributeA(jitter):
    wininet_GopherGetAttribute(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_GopherGetAttributeW(jitter):
    wininet_GopherGetAttribute(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_GopherGetLocatorType(jitter, get_str, set_str):
    """
    BOOL GopherGetLocatorType(
        LPCTSTR lpszLocator,
        LPDWORD lpdwGopherType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszLocator", "lpdwGopherType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GopherGetLocatorTypeA(jitter):
    wininet_GopherGetLocatorType(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_GopherGetLocatorTypeW(jitter):
    wininet_GopherGetLocatorType(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_GopherOpenFile(jitter, get_str, set_str):
    """
    HINTERNET GopherOpenFile(
        HINTERNET hConnect,
        LPCTSTR lpszLocator,
        LPCTSTR lpszView,
        DWORD dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszLocator", "lpszView", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GopherOpenFileA(jitter):
    wininet_GopherOpenFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_GopherOpenFileW(jitter):
    wininet_GopherOpenFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_HttpAddRequestHeaders(jitter, get_str, set_str):
    """
    BOOL HttpAddRequestHeaders(
        HINTERNET hConnect,
        LPCTSTR lpszHeaders,
        DWORD dwHeadersLength,
        [HttpAddReqFlag] dwModifiers
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszHeaders", "dwHeadersLength", "dwModifiers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpAddRequestHeadersA(jitter):
    wininet_HttpAddRequestHeaders(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_HttpAddRequestHeadersW(jitter):
    wininet_HttpAddRequestHeaders(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_HttpEndRequest(jitter, get_str, set_str):
    """
    BOOL HttpEndRequest(
        HINTERNET hRequest,
        LPINTERNET_BUFFERS lpBuffersOut,
        DWORD dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "lpBuffersOut", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpEndRequestA(jitter):
    wininet_HttpEndRequest(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_HttpEndRequestW(jitter):
    wininet_HttpEndRequest(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_HttpOpenRequest(jitter, get_str, set_str):
    """
    HINTERNET HttpOpenRequest(
        HINTERNET hConnect,
        LPCTSTR lpszVerb,
        LPCTSTR lpszObjectName,
        LPCTSTR lpszVersion,
        LPCTSTR lpszReferer,
        LPCTSTR* lplpszAcceptTypes,
        [InternetFlags] dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConnect", "lpszVerb", "lpszObjectName", "lpszVersion", "lpszReferer", "lplpszAcceptTypes", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpOpenRequestA(jitter):
    wininet_HttpOpenRequest(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_HttpOpenRequestW(jitter):
    wininet_HttpOpenRequest(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_HttpQueryInfo(jitter, get_str, set_str):
    """
    BOOL HttpQueryInfo(
        HINTERNET hRequest,
        [HTTP_QUERY_FLAGS] dwInfoLevel,
        LPVOID lpvBuffer,
        LPDWORD lpdwBufferLength,
        LPDWORD lpdwIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "dwInfoLevel", "lpvBuffer", "lpdwBufferLength", "lpdwIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpQueryInfoA(jitter):
    wininet_HttpQueryInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_HttpQueryInfoW(jitter):
    wininet_HttpQueryInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_HttpSendRequest(jitter, get_str, set_str):
    """
    BOOL HttpSendRequest(
        HINTERNET hRequest,
        LPCTSTR lpszHeaders,
        DWORD dwHeadersLength,
        LPVOID lpOptional,
        DWORD dwOptionalLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "lpszHeaders", "dwHeadersLength", "lpOptional", "dwOptionalLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpSendRequestA(jitter):
    wininet_HttpSendRequest(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_HttpSendRequestW(jitter):
    wininet_HttpSendRequest(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_HttpSendRequestEx(jitter, get_str, set_str):
    """
    BOOL HttpSendRequestEx(
        HINTERNET hRequest,
        LPINTERNET_BUFFERS lpBuffersIn,
        LPINTERNET_BUFFERS lpBuffersOut,
        DWORD dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "lpBuffersIn", "lpBuffersOut", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpSendRequestExA(jitter):
    wininet_HttpSendRequestEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_HttpSendRequestExW(jitter):
    wininet_HttpSendRequestEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetAttemptConnect(jitter):
    """
    [ERROR_CODE] InternetAttemptConnect(
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetAutodial(jitter):
    """
    BOOL InternetAutodial(
        DWORD dwFlags,
        HWND hwndParent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "hwndParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetAutodialHangup(jitter):
    """
    BOOL InternetAutodialHangup(
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetCanonicalizeUrl(jitter, get_str, set_str):
    """
    BOOL InternetCanonicalizeUrl(
        LPCTSTR lpszUrl,
        LPTSTR lpszBuffer,
        LPDWORD lpdwBufferLength,
        [InternetCanonicalizeUrlFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrl", "lpszBuffer", "lpdwBufferLength", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetCanonicalizeUrlA(jitter):
    wininet_InternetCanonicalizeUrl(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetCanonicalizeUrlW(jitter):
    wininet_InternetCanonicalizeUrl(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetCheckConnection(jitter, get_str, set_str):
    """
    BOOL InternetCheckConnection(
        LPCTSTR lpszUrl,
        DWORD dwFlags,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrl", "dwFlags", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetCheckConnectionA(jitter):
    wininet_InternetCheckConnection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetCheckConnectionW(jitter):
    wininet_InternetCheckConnection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetCloseHandle(jitter):
    """
    BOOL InternetCloseHandle(
        HINTERNET hInternet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetCombineUrl(jitter, get_str, set_str):
    """
    BOOL InternetCombineUrl(
        LPCTSTR lpszBaseUrl,
        LPCTSTR lpszRelativeUrl,
        LPTSTR lpszBuffer,
        LPDWORD lpdwBufferLength,
        [InternetCanonicalizeUrlFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszBaseUrl", "lpszRelativeUrl", "lpszBuffer", "lpdwBufferLength", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetCombineUrlA(jitter):
    wininet_InternetCombineUrl(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetCombineUrlW(jitter):
    wininet_InternetCombineUrl(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetConfirmZoneCrossing(jitter, get_str, set_str):
    """
    [ERROR_CODE] InternetConfirmZoneCrossing(
        HWND hWnd,
        LPTSTR szUrlPrev,
        LPTSTR szUrlNew,
        BOOL bPost
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "szUrlPrev", "szUrlNew", "bPost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetConfirmZoneCrossingA(jitter):
    wininet_InternetConfirmZoneCrossing(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetConfirmZoneCrossingW(jitter):
    wininet_InternetConfirmZoneCrossing(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetConfirmZoneCrossing(jitter):
    """
    [ERROR_CODE] InternetConfirmZoneCrossing(
        HWND hWnd,
        LPSTR szUrlPrev,
        LPSTR szUrlNew,
        BOOL bPost
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "szUrlPrev", "szUrlNew", "bPost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetConnect(jitter, get_str, set_str):
    """
    HINTERNET InternetConnect(
        HINTERNET hInternet,
        LPCTSTR lpszServerName,
        INTERNET_PORT nServerPort,
        LPCTSTR lpszUsername,
        LPCTSTR lpszPassword,
        [InternetService] dwService,
        [InternetFlags] dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "lpszServerName", "nServerPort", "lpszUsername", "lpszPassword", "dwService", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetConnectA(jitter):
    wininet_InternetConnect(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetConnectW(jitter):
    wininet_InternetConnect(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetCrackUrl(jitter, get_str, set_str):
    """
    BOOL InternetCrackUrl(
        LPCTSTR lpszUrl,
        DWORD dwUrlLength,
        [InternetCrackUrlFlags] dwFlags,
        LPURL_COMPONENTS lpUrlComponents
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrl", "dwUrlLength", "dwFlags", "lpUrlComponents"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetCrackUrlA(jitter):
    wininet_InternetCrackUrl(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetCrackUrlW(jitter):
    wininet_InternetCrackUrl(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetCreateUrl(jitter, get_str, set_str):
    """
    BOOL InternetCreateUrl(
        LPURL_COMPONENTS lpUrlComponents,
        [InternetCrackUrlFlags] dwFlags,
        LPTSTR lpszUrl,
        LPDWORD lpdwUrlLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpUrlComponents", "dwFlags", "lpszUrl", "lpdwUrlLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetCreateUrlA(jitter):
    wininet_InternetCreateUrl(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetCreateUrlW(jitter):
    wininet_InternetCreateUrl(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetDial(jitter, get_str, set_str):
    """
    [ERROR_CODE] InternetDial(
        HWND hwndParent,
        LPTSTR pszEntryName,
        [INTERNET_DIAL_FLAGS] dwFlags,
        DWORD_PTR* lpdwConnection,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "pszEntryName", "dwFlags", "lpdwConnection", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetDialA(jitter):
    wininet_InternetDial(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetDialW(jitter):
    wininet_InternetDial(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetDial(jitter):
    """
    [ERROR_CODE] InternetDial(
        HWND hwndParent,
        LPSTR pszEntryName,
        [INTERNET_DIAL_FLAGS] dwFlags,
        LPDWORD* lpdwConnection,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "pszEntryName", "dwFlags", "lpdwConnection", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetErrorDlg(jitter):
    """
    [ERROR_CODE] InternetErrorDlg(
        HWND hWnd,
        HINTERNET hRequest,
        [ERROR_INTERNET] dwError,
        [InternetErrorDlgFlags] dwFlags,
        LPVOID* lppvData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hRequest", "dwError", "dwFlags", "lppvData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetFindNextFile(jitter, get_str, set_str):
    """
    BOOL InternetFindNextFile(
        HINTERNET hFind,
        LPVOID lpvFindData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFind", "lpvFindData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetFindNextFileA(jitter):
    wininet_InternetFindNextFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetFindNextFileW(jitter):
    wininet_InternetFindNextFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetGetConnectedState(jitter):
    """
    BOOL InternetGetConnectedState(
        [InternetGetConnectedStateFlags*] lpdwFlags,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpdwFlags", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGetConnectedStateEx(jitter, get_str, set_str):
    """
    BOOL InternetGetConnectedStateEx(
        [InternetGetConnectedStateFlags*] lpdwFlags,
        LPTSTR lpszConnectionName,
        DWORD dwNameLen,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpdwFlags", "lpszConnectionName", "dwNameLen", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGetConnectedStateExA(jitter):
    wininet_InternetGetConnectedStateEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetGetConnectedStateExW(jitter):
    wininet_InternetGetConnectedStateEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetGetConnectedStateEx(jitter):
    """
    BOOL InternetGetConnectedStateEx(
        [InternetGetConnectedStateFlags*] lpdwFlags,
        LPSTR lpszConnectionName,
        DWORD dwNameLen,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpdwFlags", "lpszConnectionName", "dwNameLen", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGetCookie(jitter, get_str, set_str):
    """
    BOOL InternetGetCookie(
        LPCTSTR lpszUrl,
        LPCTSTR lpszCookieName,
        LPTSTR lpszCookieData,
        LPDWORD lpdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrl", "lpszCookieName", "lpszCookieData", "lpdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGetCookieA(jitter):
    wininet_InternetGetCookie(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetGetCookieW(jitter):
    wininet_InternetGetCookie(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetGetCookieEx(jitter, get_str, set_str):
    """
    BOOL InternetGetCookieEx(
        LPCTSTR pchURL,
        LPCTSTR pchCookieName,
        LPTSTR pchCookieData,
        LPDWORD pcchCookieData,
        [InternetCookieFlags] dwFlags,
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pchURL", "pchCookieName", "pchCookieData", "pcchCookieData", "dwFlags", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGetCookieExA(jitter):
    wininet_InternetGetCookieEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetGetCookieExW(jitter):
    wininet_InternetGetCookieEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetGetLastResponseInfo(jitter, get_str, set_str):
    """
    BOOL InternetGetLastResponseInfo(
        LPDWORD lpdwError,
        LPTSTR lpszBuffer,
        LPDWORD lpdwBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpdwError", "lpszBuffer", "lpdwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGetLastResponseInfoA(jitter):
    wininet_InternetGetLastResponseInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetGetLastResponseInfoW(jitter):
    wininet_InternetGetLastResponseInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetGoOnline(jitter, get_str, set_str):
    """
    BOOL InternetGoOnline(
        LPTSTR lpszURL,
        HWND hwndParent,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszURL", "hwndParent", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGoOnlineA(jitter):
    wininet_InternetGoOnline(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetGoOnlineW(jitter):
    wininet_InternetGoOnline(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetGoOnline(jitter):
    """
    BOOL InternetGoOnline(
        LPSTR lpszURL,
        HWND hwndParent,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszURL", "hwndParent", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetHangUp(jitter):
    """
    [ERROR_CODE] InternetHangUp(
        DWORD_PTR dwConnection,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwConnection", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetLockRequestFile(jitter):
    """
    BOOL InternetLockRequestFile(
        HINTERNET hInternet,
        HANDLE* lphLockReqHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "lphLockReqHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetOpen(jitter, get_str, set_str):
    """
    HINTERNET InternetOpen(
        LPCTSTR lpszAgent,
        [InternetOpenType] dwAccessType,
        LPCTSTR lpszProxyName,
        LPCTSTR lpszProxyBypass,
        [InternetOpenFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszAgent", "dwAccessType", "lpszProxyName", "lpszProxyBypass", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetOpenA(jitter):
    wininet_InternetOpen(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetOpenW(jitter):
    wininet_InternetOpen(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetOpenUrl(jitter, get_str, set_str):
    """
    HINTERNET InternetOpenUrl(
        HINTERNET hInternet,
        LPCTSTR lpszUrl,
        LPCTSTR lpszHeaders,
        DWORD dwHeadersLength,
        [InternetFlags] dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "lpszUrl", "lpszHeaders", "dwHeadersLength", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetOpenUrlA(jitter):
    wininet_InternetOpenUrl(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetOpenUrlW(jitter):
    wininet_InternetOpenUrl(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetQueryDataAvailable(jitter):
    """
    BOOL InternetQueryDataAvailable(
        HINTERNET hFile,
        LPDWORD lpdwNumberOfBytesAvailable,
        DWORD dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpdwNumberOfBytesAvailable", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetQueryOption(jitter, get_str, set_str):
    """
    BOOL InternetQueryOption(
        HINTERNET hInternet,
        [INTERNET_OPTION] dwOption,
        LPVOID lpBuffer,
        LPDWORD lpdwBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "dwOption", "lpBuffer", "lpdwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetQueryOptionA(jitter):
    wininet_InternetQueryOption(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetQueryOptionW(jitter):
    wininet_InternetQueryOption(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetReadFile(jitter):
    """
    BOOL InternetReadFile(
        HINTERNET hFile,
        LPVOID lpBuffer,
        DWORD dwNumberOfBytesToRead,
        LPDWORD lpdwNumberOfBytesRead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffer", "dwNumberOfBytesToRead", "lpdwNumberOfBytesRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetReadFileEx(jitter, get_str, set_str):
    """
    BOOL InternetReadFileEx(
        HINTERNET hFile,
        LPINTERNET_BUFFERS lpBuffersOut,
        [InternetReadFileFlags] dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffersOut", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetReadFileExA(jitter):
    wininet_InternetReadFileEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetReadFileExW(jitter):
    wininet_InternetReadFileEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetSetCookie(jitter, get_str, set_str):
    """
    BOOL InternetSetCookie(
        LPCTSTR lpszUrl,
        LPCTSTR lpszCookieName,
        LPCTSTR lpszCookieData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrl", "lpszCookieName", "lpszCookieData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetSetCookieA(jitter):
    wininet_InternetSetCookie(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetSetCookieW(jitter):
    wininet_InternetSetCookie(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetSetCookieEx(jitter, get_str, set_str):
    """
    InternetCookieState InternetSetCookieEx(
        LPCTSTR lpszURL,
        LPCTSTR lpszCookieName,
        LPCTSTR lpszCookieData,
        [InternetCookieFlags] dwFlags,
        DWORD_PTR dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszURL", "lpszCookieName", "lpszCookieData", "dwFlags", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetSetCookieExA(jitter):
    wininet_InternetSetCookieEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetSetCookieExW(jitter):
    wininet_InternetSetCookieEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetSetFilePointer(jitter):
    """
    DWORD InternetSetFilePointer(
        HINTERNET hFile,
        LONG lDistanceToMove,
        PVOID pReserved,
        DWORD dwMoveMethod,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lDistanceToMove", "pReserved", "dwMoveMethod", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetSetOption(jitter, get_str, set_str):
    """
    BOOL InternetSetOption(
        HINTERNET hInternet,
        [INTERNET_OPTION] dwOption,
        LPVOID lpBuffer,
        DWORD dwBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "dwOption", "lpBuffer", "dwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetSetOptionA(jitter):
    wininet_InternetSetOption(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetSetOptionW(jitter):
    wininet_InternetSetOption(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetSetStatusCallback(jitter, get_str, set_str):
    """
    INTERNET_STATUS_CALLBACK InternetSetStatusCallback(
        HINTERNET hInternet,
        INTERNET_STATUS_CALLBACK lpfnInternetCallback
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "lpfnInternetCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetSetStatusCallbackA(jitter):
    wininet_InternetSetStatusCallback(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetSetStatusCallbackW(jitter):
    wininet_InternetSetStatusCallback(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetSetStatusCallback(jitter):
    """
    INTERNET_STATUS_CALLBACK InternetSetStatusCallback(
        HINTERNET hInternet,
        INTERNET_STATUS_CALLBACK lpfnInternetCallback
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "lpfnInternetCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetTimeFromSystemTime(jitter, get_str, set_str):
    """
    BOOL InternetTimeFromSystemTime(
        const SYSTEMTIME* pst,
        DWORD dwRFC,
        LPTSTR lpszTime,
        DWORD cbTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pst", "dwRFC", "lpszTime", "cbTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetTimeFromSystemTimeA(jitter):
    wininet_InternetTimeFromSystemTime(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetTimeFromSystemTimeW(jitter):
    wininet_InternetTimeFromSystemTime(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetTimeFromSystemTime(jitter):
    """
    BOOL InternetTimeFromSystemTime(
        const SYSTEMTIME* pst,
        DWORD dwRFC,
        LPSTR lpszTime,
        DWORD cbTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pst", "dwRFC", "lpszTime", "cbTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetTimeToSystemTime(jitter, get_str, set_str):
    """
    BOOL InternetTimeToSystemTime(
        LPCTSTR lpszTime,
        SYSTEMTIME* pst,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszTime", "pst", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetTimeToSystemTimeA(jitter):
    wininet_InternetTimeToSystemTime(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetTimeToSystemTimeW(jitter):
    wininet_InternetTimeToSystemTime(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetTimeToSystemTime(jitter):
    """
    BOOL InternetTimeToSystemTime(
        LPCSTR lpszTime,
        SYSTEMTIME* pst,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszTime", "pst", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetUnlockRequestFile(jitter):
    """
    BOOLAPI InternetUnlockRequestFile(
        HANDLE hLockRequestInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLockRequestInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetWriteFile(jitter):
    """
    BOOL InternetWriteFile(
        HINTERNET hFile,
        LPCVOID lpBuffer,
        DWORD dwNumberOfBytesToWrite,
        LPDWORD lpdwNumberOfBytesWritten
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffer", "dwNumberOfBytesToWrite", "lpdwNumberOfBytesWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_ReadUrlCacheEntryStream(jitter):
    """
    BOOLAPI ReadUrlCacheEntryStream(
        HANDLE hUrlCacheStream,
        DWORD dwLocation,
        LPVOID lpBuffer,
        LPDWORD lpdwLen,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUrlCacheStream", "dwLocation", "lpBuffer", "lpdwLen", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_ResumeSuspendedDownload(jitter):
    """
    BOOL ResumeSuspendedDownload(
        HINTERNET hRequest,
        DWORD dwResultCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "dwResultCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_RetrieveUrlCacheEntryFile(jitter, get_str, set_str):
    """
    BOOLAPI RetrieveUrlCacheEntryFile(
        LPCTSTR lpszUrlName,
        LPINTERNET_CACHE_ENTRY_INFO lpCacheEntryInfo,
        LPDWORD lpcbCacheEntryInfo,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName", "lpCacheEntryInfo", "lpcbCacheEntryInfo", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_RetrieveUrlCacheEntryFileA(jitter):
    wininet_RetrieveUrlCacheEntryFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_RetrieveUrlCacheEntryFileW(jitter):
    wininet_RetrieveUrlCacheEntryFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_RetrieveUrlCacheEntryStream(jitter, get_str, set_str):
    """
    HANDLE RetrieveUrlCacheEntryStream(
        LPCTSTR lpszUrlName,
        LPINTERNET_CACHE_ENTRY_INFO lpCacheEntryInfo,
        LPDWORD lpcbCacheEntryInfo,
        BOOL fRandomRead,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName", "lpCacheEntryInfo", "lpcbCacheEntryInfo", "fRandomRead", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_RetrieveUrlCacheEntryStreamA(jitter):
    wininet_RetrieveUrlCacheEntryStream(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_RetrieveUrlCacheEntryStreamW(jitter):
    wininet_RetrieveUrlCacheEntryStream(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_SetUrlCacheEntryGroup(jitter, get_str, set_str):
    """
    BOOLAPI SetUrlCacheEntryGroup(
        LPCTSTR lpszUrlName,
        DWORD dwFlags,
        GROUPID GroupId,
        LPBYTE pbGroupAttributes,
        DWORD cbGroupAttributes,
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName", "dwFlags", "GroupId", "pbGroupAttributes", "cbGroupAttributes", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_SetUrlCacheEntryGroupA(jitter):
    wininet_SetUrlCacheEntryGroup(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_SetUrlCacheEntryGroupW(jitter):
    wininet_SetUrlCacheEntryGroup(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_SetUrlCacheEntryGroup(jitter):
    """
    BOOLAPI SetUrlCacheEntryGroup(
        LPCSTR lpszUrlName,
        DWORD dwFlags,
        GROUPID GroupId,
        LPBYTE pbGroupAttributes,
        DWORD cbGroupAttributes,
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName", "dwFlags", "GroupId", "pbGroupAttributes", "cbGroupAttributes", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_SetUrlCacheEntryInfo(jitter, get_str, set_str):
    """
    BOOLAPI SetUrlCacheEntryInfo(
        LPCTSTR lpszUrlName,
        LPINTERNET_CACHE_ENTRY_INFO lpCacheEntryInfo,
        [CacheEntryFieldControl] dwFieldControl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName", "lpCacheEntryInfo", "dwFieldControl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_SetUrlCacheEntryInfoA(jitter):
    wininet_SetUrlCacheEntryInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_SetUrlCacheEntryInfoW(jitter):
    wininet_SetUrlCacheEntryInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_SetUrlCacheGroupAttribute(jitter, get_str, set_str):
    """
    BOOL SetUrlCacheGroupAttribute(
        GROUPID gid,
        DWORD dwFlags,
        DWORD dwAttributes,
        LPINTERNET_CACHE_GROUP_INFO lpGroupInfo,
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["gid", "dwFlags", "dwAttributes", "lpGroupInfo", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_SetUrlCacheGroupAttributeA(jitter):
    wininet_SetUrlCacheGroupAttribute(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_SetUrlCacheGroupAttributeW(jitter):
    wininet_SetUrlCacheGroupAttribute(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_UnlockUrlCacheEntryFile(jitter, get_str, set_str):
    """
    BOOLAPI UnlockUrlCacheEntryFile(
        LPCTSTR lpszUrlName,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UnlockUrlCacheEntryFileA(jitter):
    wininet_UnlockUrlCacheEntryFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_UnlockUrlCacheEntryFileW(jitter):
    wininet_UnlockUrlCacheEntryFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_UnlockUrlCacheEntryFile(jitter):
    """
    BOOLAPI UnlockUrlCacheEntryFile(
        LPCSTR lpszUrlName,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UnlockUrlCacheEntryStream(jitter):
    """
    BOOLAPI UnlockUrlCacheEntryStream(
        HANDLE hUrlCacheStream,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUrlCacheStream", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetClearAllPerSiteCookieDecisions(jitter):
    """
    BOOL InternetClearAllPerSiteCookieDecisions()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetEnumPerSiteCookieDecision(jitter, get_str, set_str):
    """
    BOOL InternetEnumPerSiteCookieDecision(
        LPTSTR pszSiteName,
        unsigned long* pcSiteNameSize,
        unsigned long* pdwDecision,
        unsigned long dwIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSiteName", "pcSiteNameSize", "pdwDecision", "dwIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetEnumPerSiteCookieDecisionA(jitter):
    wininet_InternetEnumPerSiteCookieDecision(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetEnumPerSiteCookieDecisionW(jitter):
    wininet_InternetEnumPerSiteCookieDecision(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetGetPerSiteCookieDecision(jitter, get_str, set_str):
    """
    BOOL InternetGetPerSiteCookieDecision(
        LPCTSTR pchHostName,
        unsigned long* pResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pchHostName", "pResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGetPerSiteCookieDecisionA(jitter):
    wininet_InternetGetPerSiteCookieDecision(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetGetPerSiteCookieDecisionW(jitter):
    wininet_InternetGetPerSiteCookieDecision(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetSetPerSiteCookieDecision(jitter, get_str, set_str):
    """
    BOOL InternetSetPerSiteCookieDecision(
        LPCTSTR pchHostName,
        DWORD dwDecision
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pchHostName", "dwDecision"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetSetPerSiteCookieDecisionA(jitter):
    wininet_InternetSetPerSiteCookieDecision(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetSetPerSiteCookieDecisionW(jitter):
    wininet_InternetSetPerSiteCookieDecision(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_PrivacyGetZonePreferenceW(jitter):
    """
    [ERROR_CODE] PrivacyGetZonePreferenceW(
        [URLZONE|DWORD] dwZone,
        DWORD dwType,
        LPDWORD pdwTemplate,
        LPWSTR pszBuffer,
        LPDWORD pdwBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwZone", "dwType", "pdwTemplate", "pszBuffer", "pdwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_PrivacySetZonePreferenceW(jitter):
    """
    [ERROR_CODE] PrivacySetZonePreferenceW(
        [URLZONE|DWORD] dwZone,
        DWORD dwType,
        DWORD dwTemplate,
        LPCWSTR pszPreference
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwZone", "dwType", "dwTemplate", "pszPreference"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetInitializeAutoProxyDll(jitter):
    """
    BOOL InternetInitializeAutoProxyDll(
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetAlgIdToString(jitter, get_str, set_str):
    """
    BOOLAPI InternetAlgIdToString(
        ALG_ID ai,
        LPTSTR lpstr,
        LPDWORD lpdwstrLength,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ai", "lpstr", "lpdwstrLength", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetAlgIdToStringA(jitter):
    wininet_InternetAlgIdToString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetAlgIdToStringW(jitter):
    wininet_InternetAlgIdToString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetSecurityProtocolToString(jitter, get_str, set_str):
    """
    BOOLAPI InternetSecurityProtocolToString(
        DWORD dwProtocol,
        LPTSTR lpstr,
        LPDWORD lpdwstrLength,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwProtocol", "lpstr", "lpdwstrLength", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetSecurityProtocolToStringA(jitter):
    wininet_InternetSecurityProtocolToString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetSecurityProtocolToStringW(jitter):
    wininet_InternetSecurityProtocolToString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetGetSecurityInfoByURL(jitter, get_str, set_str):
    """
    BOOLAPI InternetGetSecurityInfoByURL(
        LPTSTR lpszURL,
        PCCERT_CHAIN_CONTEXT* ppCertChain,
        DWORD* pdwSecureFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszURL", "ppCertChain", "pdwSecureFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGetSecurityInfoByURLA(jitter):
    wininet_InternetGetSecurityInfoByURL(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetGetSecurityInfoByURLW(jitter):
    wininet_InternetGetSecurityInfoByURL(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetGetSecurityInfoByURL(jitter):
    """
    BOOLAPI InternetGetSecurityInfoByURL(
        LPSTR lpszURL,
        PCCERT_CHAIN_CONTEXT* ppCertChain,
        DWORD* pdwSecureFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszURL", "ppCertChain", "pdwSecureFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_ShowSecurityInfo(jitter):
    """
    [ERROR_CODE] ShowSecurityInfo(
        HWND hWndParent,
        LPINTERNET_SECURITY_INFO pSecurityInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndParent", "pSecurityInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_ShowX509EncodedCertificate(jitter):
    """
    [ERROR_CODE] ShowX509EncodedCertificate(
        HWND hWndParent,
        LPBYTE lpCert,
        DWORD cbCert
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndParent", "lpCert", "cbCert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_ShowClientAuthCerts(jitter):
    """
    [ERROR_CODE] ShowClientAuthCerts(
        HWND hWndParent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_ParseX509EncodedCertificateForListBoxEntry(jitter):
    """
    [ERROR_CODE] ParseX509EncodedCertificateForListBoxEntry(
        LPBYTE lpCert,
        DWORD cbCert,
        LPSTR lpszListBoxEntry,
        LPDWORD lpdwListBoxEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpCert", "cbCert", "lpszListBoxEntry", "lpdwListBoxEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetShowSecurityInfoByURL(jitter, get_str, set_str):
    """
    BOOLAPI InternetShowSecurityInfoByURL(
        LPTSTR lpszURL,
        HWND hwndParent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszURL", "hwndParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetShowSecurityInfoByURLA(jitter):
    wininet_InternetShowSecurityInfoByURL(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetShowSecurityInfoByURLW(jitter):
    wininet_InternetShowSecurityInfoByURL(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetShowSecurityInfoByURL(jitter):
    """
    BOOLAPI InternetShowSecurityInfoByURL(
        LPSTR lpszURL,
        HWND hwndParent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszURL", "hwndParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGetCertByURL(jitter):
    """
    BOOLAPI InternetGetCertByURL(
        LPSTR lpszURL,
        LPSTR lpszCertText,
        DWORD dwcbCertText
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszURL", "lpszCertText", "dwcbCertText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGetCertByURLA(jitter):
    """
    BOOLAPI InternetGetCertByURLA(
        LPSTR lpszURL,
        LPSTR lpszCertText,
        DWORD dwcbCertText
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszURL", "lpszCertText", "dwcbCertText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetFortezzaCommand(jitter):
    """
    BOOLAPI InternetFortezzaCommand(
        FORTCMD dwCommand,
        HWND hwnd,
        DWORD_PTR dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwCommand", "hwnd", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetQueryFortezzaStatus(jitter):
    """
    BOOLAPI InternetQueryFortezzaStatus(
        FORTSTAT* pdwStatus,
        DWORD_PTR dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwStatus", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetDebugGetLocalTime(jitter):
    """
    BOOLAPI InternetDebugGetLocalTime(
        SYSTEMTIME* pstLocalTime,
        DWORD* pdwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstLocalTime", "pdwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetWriteFileEx(jitter, get_str, set_str):
    """
    BOOLAPI InternetWriteFileEx(
        HINTERNET hFile,
        LPINTERNET_BUFFERS lpBuffersIn,
        DWORD dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffersIn", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetWriteFileExA(jitter):
    wininet_InternetWriteFileEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetWriteFileExW(jitter):
    wininet_InternetWriteFileEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FindP3PPolicySymbol(jitter):
    """
    P3PStatus FindP3PPolicySymbol(
        const char* pszSymbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSymbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpPushEnable(jitter):
    """
    [ERROR_CODE] HttpPushEnable(
        HINTERNET hRequest,
        HTTP_PUSH_TRANSPORT_SETTING* pTransportSetting,
        HTTP_PUSH_WAIT_HANDLE* phWait
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "pTransportSetting", "phWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpPushWait(jitter):
    """
    [ERROR_CODE] HttpPushWait(
        HTTP_PUSH_WAIT_HANDLE hWait,
        HTTP_PUSH_WAIT_TYPE eType,
        HTTP_PUSH_NOTIFICATION_STATUS* pNotificationStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWait", "eType", "pNotificationStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpPushClose(jitter):
    """
    VOID HttpPushClose(
        HTTP_PUSH_WAIT_HANDLE hWait
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpCheckDavCompliance(jitter, get_str, set_str):
    """
    BOOLAPI HttpCheckDavCompliance(
        LPCTSTR lpszUrl,
        LPCTSTR lpszComplianceToken,
        LPBOOL lpfFound,
        HWND hWnd,
        LPVOID lpvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrl", "lpszComplianceToken", "lpfFound", "hWnd", "lpvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpCheckDavComplianceA(jitter):
    wininet_HttpCheckDavCompliance(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_HttpCheckDavComplianceW(jitter):
    wininet_HttpCheckDavCompliance(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_HttpCheckDavCompliance(jitter):
    """
    BOOLAPI HttpCheckDavCompliance(
        LPCSTR lpszUrl,
        LPCSTR lpszComplianceToken,
        LPBOOL lpfFound,
        HWND hWnd,
        LPVOID lpvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrl", "lpszComplianceToken", "lpfFound", "hWnd", "lpvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_IsUrlCacheEntryExpired(jitter, get_str, set_str):
    """
    BOOLAPI IsUrlCacheEntryExpired(
        LPCTSTR lpszUrlName,
        DWORD dwFlags,
        FILETIME* pftLastModified
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName", "dwFlags", "pftLastModified"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_IsUrlCacheEntryExpiredA(jitter):
    wininet_IsUrlCacheEntryExpired(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_IsUrlCacheEntryExpiredW(jitter):
    wininet_IsUrlCacheEntryExpired(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_CreateUrlCacheEntryExW(jitter):
    """
    BOOLAPI CreateUrlCacheEntryExW(
        LPCWSTR lpszUrlName,
        DWORD dwExpectedFileSize,
        LPCWSTR lpszFileExtension,
        LPWSTR lpszFileName,
        DWORD dwReserved,
        BOOL fPreserveIncomingFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName", "dwExpectedFileSize", "lpszFileExtension", "lpszFileName", "dwReserved", "fPreserveIncomingFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GetUrlCacheEntryBinaryBlob(jitter):
    """
    [ERROR_CODE] GetUrlCacheEntryBinaryBlob(
        PCWSTR pwszUrlName,
        DWORD* dwType,
        FILETIME* pftExpireTime,
        FILETIME* pftAccessTime,
        FILETIME* pftModifiedTime,
        BYTE** ppbBlob,
        DWORD* pcbBlob
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszUrlName", "dwType", "pftExpireTime", "pftAccessTime", "pftModifiedTime", "ppbBlob", "pcbBlob"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_CommitUrlCacheEntryBinaryBlob(jitter):
    """
    [ERROR_CODE] CommitUrlCacheEntryBinaryBlob(
        PCWSTR pwszUrlName,
        DWORD dwType,
        FILETIME ftExpireTime,
        FILETIME ftModifiedTime,
        const BYTE* pbBlob,
        DWORD cbBlob
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszUrlName", "dwType", "ftExpireTime", "ftModifiedTime", "pbBlob", "cbBlob"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_CreateUrlCacheContainer(jitter, get_str, set_str):
    """
    BOOLAPI CreateUrlCacheContainer(
        LPCTSTR Name,
        LPCTSTR lpCachePrefix,
        LPCTSTR lpszCachePath,
        DWORD KBCacheLimit,
        DWORD dwContainerType,
        [INTERNET_CACHE_CONTAINER_FLAGS] dwOptions,
        LPVOID pvBuffer,
        LPDWORD cbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Name", "lpCachePrefix", "lpszCachePath", "KBCacheLimit", "dwContainerType", "dwOptions", "pvBuffer", "cbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_CreateUrlCacheContainerA(jitter):
    wininet_CreateUrlCacheContainer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_CreateUrlCacheContainerW(jitter):
    wininet_CreateUrlCacheContainer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_DeleteUrlCacheContainer(jitter, get_str, set_str):
    """
    BOOLAPI DeleteUrlCacheContainer(
        LPCTSTR Name,
        DWORD dwOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Name", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_DeleteUrlCacheContainerA(jitter):
    wininet_DeleteUrlCacheContainer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_DeleteUrlCacheContainerW(jitter):
    wininet_DeleteUrlCacheContainer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FindFirstUrlCacheContainer(jitter, get_str, set_str):
    """
    HANDLE FindFirstUrlCacheContainer(
        LPDWORD pdwModified,
        LPINTERNET_CACHE_CONTAINER_INFO lpContainerInfo,
        LPDWORD lpcbContainerInfo,
        [CACHE_FIND_CONTAINER_FLAGS] dwOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwModified", "lpContainerInfo", "lpcbContainerInfo", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FindFirstUrlCacheContainerA(jitter):
    wininet_FindFirstUrlCacheContainer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FindFirstUrlCacheContainerW(jitter):
    wininet_FindFirstUrlCacheContainer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FindNextUrlCacheContainer(jitter, get_str, set_str):
    """
    BOOLAPI FindNextUrlCacheContainer(
        HANDLE hEnumHandle,
        LPINTERNET_CACHE_CONTAINER_INFO lpContainerInfo,
        LPDWORD lpcbContainerInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEnumHandle", "lpContainerInfo", "lpcbContainerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FindNextUrlCacheContainerA(jitter):
    wininet_FindNextUrlCacheContainer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FindNextUrlCacheContainerW(jitter):
    wininet_FindNextUrlCacheContainer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FreeUrlCacheSpace(jitter, get_str, set_str):
    """
    BOOLAPI FreeUrlCacheSpace(
        LPCTSTR lpszCachePath,
        DWORD dwSize,
        DWORD dwFilter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszCachePath", "dwSize", "dwFilter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FreeUrlCacheSpaceA(jitter):
    wininet_FreeUrlCacheSpace(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_FreeUrlCacheSpaceW(jitter):
    wininet_FreeUrlCacheSpace(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_GetUrlCacheConfigInfo(jitter, get_str, set_str):
    """
    BOOLAPI GetUrlCacheConfigInfo(
        LPINTERNET_CACHE_CONFIG_INFO lpCacheConfigInfo,
        LPDWORD lpcbCacheConfigInfo,
        [CACHE_CONFIG_FC] dwFieldControl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpCacheConfigInfo", "lpcbCacheConfigInfo", "dwFieldControl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GetUrlCacheConfigInfoA(jitter):
    wininet_GetUrlCacheConfigInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_GetUrlCacheConfigInfoW(jitter):
    wininet_GetUrlCacheConfigInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_SetUrlCacheConfigInfo(jitter, get_str, set_str):
    """
    BOOLAPI SetUrlCacheConfigInfo(
        LPINTERNET_CACHE_CONFIG_INFO lpCacheConfigInfo,
        [CACHE_CONFIG_FC] dwFieldControl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpCacheConfigInfo", "dwFieldControl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_SetUrlCacheConfigInfoA(jitter):
    wininet_SetUrlCacheConfigInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_SetUrlCacheConfigInfoW(jitter):
    wininet_SetUrlCacheConfigInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_RunOnceUrlCache(jitter):
    """
    [ERROR_CODE] RunOnceUrlCache(
        HWND hwnd,
        HINSTANCE hinst,
        LPSTR lpszCmd,
        int nCmdShow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hinst", "lpszCmd", "nCmdShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_DeleteIE3Cache(jitter):
    """
    [ERROR_CODE] DeleteIE3Cache(
        HWND hwnd,
        HINSTANCE hinst,
        LPSTR lpszCmd,
        int nCmdShow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hinst", "lpszCmd", "nCmdShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UpdateUrlCacheContentPath(jitter):
    """
    BOOLAPI UpdateUrlCacheContentPath(
        LPCSTR szNewPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szNewPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_RegisterUrlCacheNotification(jitter):
    """
    BOOLAPI RegisterUrlCacheNotification(
        HWND hWnd,
        UINT uMsg,
        GROUPID gid,
        [CACHE_NOTIFY_FILTER_OPTIONS] dwOpsFilter,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "uMsg", "gid", "dwOpsFilter", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GetUrlCacheHeaderData(jitter):
    """
    BOOLAPI GetUrlCacheHeaderData(
        DWORD nIdx,
        LPDWORD lpdwData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nIdx", "lpdwData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_SetUrlCacheHeaderData(jitter):
    """
    BOOLAPI SetUrlCacheHeaderData(
        DWORD nIdx,
        DWORD dwData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nIdx", "dwData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_IncrementUrlCacheHeaderData(jitter):
    """
    BOOLAPI IncrementUrlCacheHeaderData(
        DWORD nIdx,
        LPDWORD lpdwData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nIdx", "lpdwData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_LoadUrlCacheContent(jitter):
    """
    BOOLAPI LoadUrlCacheContent()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GetUrlCacheContainerInfo(jitter, get_str, set_str):
    """
    BOOLAPI GetUrlCacheContainerInfo(
        LPTSTR lpszUrlName,
        LPINTERNET_CACHE_CONTAINER_INFO lpContainerInfo,
        LPDWORD lpcbContainerInfo,
        DWORD dwOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrlName", "lpContainerInfo", "lpcbContainerInfo", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GetUrlCacheContainerInfoA(jitter):
    wininet_GetUrlCacheContainerInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_GetUrlCacheContainerInfoW(jitter):
    wininet_GetUrlCacheContainerInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_AppCacheLookup(jitter):
    """
    [ERROR_CODE] AppCacheLookup(
        PCWSTR pwszUrl,
        [APP_CACHE_LOOKUP_FLAGS] dwFlags,
        APP_CACHE_HANDLE* phAppCache
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszUrl", "dwFlags", "phAppCache"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheCheckManifest(jitter):
    """
    [ERROR_CODE] AppCacheCheckManifest(
        PCWSTR pwszMasterUrl,
        PCWSTR pwszManifestUrl,
        const BYTE* pbManifestData,
        DWORD dwManifestDataSize,
        const BYTE* pbManifestResponseHeaders,
        DWORD dwManifestResponseHeadersSize,
        APP_CACHE_STATE* peState,
        APP_CACHE_HANDLE* phNewAppCache
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszMasterUrl", "pwszManifestUrl", "pbManifestData", "dwManifestDataSize", "pbManifestResponseHeaders", "dwManifestResponseHeadersSize", "peState", "phNewAppCache"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheGetDownloadList(jitter):
    """
    [ERROR_CODE] AppCacheGetDownloadList(
        APP_CACHE_HANDLE hAppCache,
        APP_CACHE_DOWNLOAD_LIST* pDownloadList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAppCache", "pDownloadList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheFreeDownloadList(jitter):
    """
    VOID AppCacheFreeDownloadList(
        APP_CACHE_DOWNLOAD_LIST* pDownloadList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDownloadList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheFinalize(jitter):
    """
    [ERROR_CODE] AppCacheFinalize(
        APP_CACHE_HANDLE hAppCache,
        const BYTE* pbManifestData,
        DWORD dwManifestDataSize,
        APP_CACHE_FINALIZE_STATE* peState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAppCache", "pbManifestData", "dwManifestDataSize", "peState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheGetFallbackUrl(jitter):
    """
    [ERROR_CODE] AppCacheGetFallbackUrl(
        APP_CACHE_HANDLE hAppCache,
        PCWSTR pwszUrl,
        PWSTR* ppwszFallbackUrl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAppCache", "pwszUrl", "ppwszFallbackUrl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheGetManifestUrl(jitter):
    """
    [ERROR_CODE] AppCacheGetManifestUrl(
        APP_CACHE_HANDLE hAppCache,
        PWSTR* ppwszManifestUrl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAppCache", "ppwszManifestUrl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheDuplicateHandle(jitter):
    """
    [ERROR_CODE] AppCacheDuplicateHandle(
        APP_CACHE_HANDLE hAppCache,
        APP_CACHE_HANDLE* phDuplicatedAppCache
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAppCache", "phDuplicatedAppCache"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheCloseHandle(jitter):
    """
    VOID AppCacheCloseHandle(
        APP_CACHE_HANDLE hAppCache
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAppCache"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheFreeGroupList(jitter):
    """
    VOID AppCacheFreeGroupList(
        APP_CACHE_GROUP_LIST* pAppCacheGroupList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppCacheGroupList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheGetGroupList(jitter):
    """
    [ERROR_CODE] AppCacheGetGroupList(
        APP_CACHE_GROUP_LIST* pAppCacheGroupList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppCacheGroupList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheGetInfo(jitter):
    """
    [ERROR_CODE] AppCacheGetInfo(
        APP_CACHE_HANDLE hAppCache,
        APP_CACHE_GROUP_INFO* pAppCacheInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAppCache", "pAppCacheInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheDeleteGroup(jitter):
    """
    [ERROR_CODE] AppCacheDeleteGroup(
        PCWSTR pwszManifestUrl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszManifestUrl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheGetIEGroupList(jitter):
    """
    [ERROR_CODE] AppCacheGetIEGroupList(
        APP_CACHE_GROUP_LIST* pAppCacheGroupList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppCacheGroupList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheDeleteIEGroup(jitter):
    """
    [ERROR_CODE] AppCacheDeleteIEGroup(
        PCWSTR pwszManifestUrl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszManifestUrl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_AppCacheFreeIESpace(jitter):
    """
    [ERROR_CODE] AppCacheFreeIESpace(
        FILETIME ftCutOff
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ftCutOff"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpOpenDependencyHandle(jitter):
    """
    [ERROR_CODE] HttpOpenDependencyHandle(
        HINTERNET hRequestHandle,
        BOOL fBackground,
        HTTP_DEPENDENCY_HANDLE* phDependencyHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequestHandle", "fBackground", "phDependencyHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpCloseDependencyHandle(jitter):
    """
    VOID HttpCloseDependencyHandle(
        HTTP_DEPENDENCY_HANDLE hDependencyHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDependencyHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpDuplicateDependencyHandle(jitter):
    """
    [ERROR_CODE] HttpDuplicateDependencyHandle(
        HTTP_DEPENDENCY_HANDLE hDependencyHandle,
        HTTP_DEPENDENCY_HANDLE* phDuplicatedDependencyHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDependencyHandle", "phDuplicatedDependencyHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheFreeEntryInfo(jitter):
    """
    VOID UrlCacheFreeEntryInfo(
        PURLCACHE_ENTRY_INFO pCacheEntryInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCacheEntryInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheGetEntryInfo(jitter):
    """
    [ERROR_CODE] UrlCacheGetEntryInfo(
        APP_CACHE_HANDLE hAppCache,
        PCWSTR pcwszUrl,
        PURLCACHE_ENTRY_INFO pCacheEntryInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAppCache", "pcwszUrl", "pCacheEntryInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheCloseEntryHandle(jitter):
    """
    VOID UrlCacheCloseEntryHandle(
        URLCACHE_HANDLE hEntryFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEntryFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheRetrieveEntryFile(jitter):
    """
    [ERROR_CODE] UrlCacheRetrieveEntryFile(
        APP_CACHE_HANDLE hAppCache,
        PCWSTR pcwszUrl,
        PURLCACHE_ENTRY_INFO pCacheEntryInfo,
        URLCACHE_HANDLE* phEntryFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAppCache", "pcwszUrl", "pCacheEntryInfo", "phEntryFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheReadEntryStream(jitter):
    """
    [ERROR_CODE] UrlCacheReadEntryStream(
        URLCACHE_HANDLE hUrlCacheStream,
        ULONGLONG ullLocation,
        PVOID pBuffer,
        DWORD dwBufferLen,
        PDWORD pdwBufferLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUrlCacheStream", "ullLocation", "pBuffer", "dwBufferLen", "pdwBufferLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheRetrieveEntryStream(jitter):
    """
    [ERROR_CODE] UrlCacheRetrieveEntryStream(
        APP_CACHE_HANDLE hAppCache,
        PCWSTR pcwszUrl,
        BOOL fRandomRead,
        PURLCACHE_ENTRY_INFO pCacheEntryInfo,
        URLCACHE_HANDLE* phEntryStream
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAppCache", "pcwszUrl", "fRandomRead", "pCacheEntryInfo", "phEntryStream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheUpdateEntryExtraData(jitter):
    """
    [ERROR_CODE] UrlCacheUpdateEntryExtraData(
        APP_CACHE_HANDLE hAppCache,
        PCWSTR pcwszUrl,
        const BYTE* pbExtraData,
        DWORD cbExtraData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAppCache", "pcwszUrl", "pbExtraData", "cbExtraData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheCreateContainer(jitter):
    """
    [ERROR_CODE] UrlCacheCreateContainer(
        const WCHAR* pwszName,
        const WCHAR* pwszPrefix,
        const WCHAR* pwszDirectory,
        ULONGLONG ullLimit,
        [INTERNET_CACHE_CONTAINER_FLAGS] dwOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszName", "pwszPrefix", "pwszDirectory", "ullLimit", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheCheckEntriesExist(jitter):
    """
    [ERROR_CODE] UrlCacheCheckEntriesExist(
        PCWSTR* rgpwszUrls,
        DWORD cEntries,
        BOOL* rgfExist
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rgpwszUrls", "cEntries", "rgfExist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheGetContentPaths(jitter):
    """
    [ERROR_CODE] UrlCacheGetContentPaths(
        PWSTR** pppwszDirectories,
        DWORD* pcDirectories
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pppwszDirectories", "pcDirectories"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheGetGlobalLimit(jitter):
    """
    [ERROR_CODE] UrlCacheGetGlobalLimit(
        URL_CACHE_LIMIT_TYPE limitType,
        ULONGLONG* pullLimit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["limitType", "pullLimit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheSetGlobalLimit(jitter):
    """
    [ERROR_CODE] UrlCacheSetGlobalLimit(
        URL_CACHE_LIMIT_TYPE limitType,
        ULONGLONG ullLimit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["limitType", "ullLimit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheReloadSettings(jitter):
    """
    [ERROR_CODE] UrlCacheReloadSettings()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_UrlCacheContainerSetEntryMaximumAge(jitter):
    """
    [ERROR_CODE] UrlCacheContainerSetEntryMaximumAge(
        const WCHAR* pwszPrefix,
        DWORD dwEntryMaxAge
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszPrefix", "dwEntryMaxAge"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGetDialEngineW(jitter):
    """
    HRESULT InternetGetDialEngineW(
        LPWSTR pwzConnectoid,
        IDialEventSink* pdes,
        IDialEngine** ppde
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzConnectoid", "pdes", "ppde"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGetDialBrandingW(jitter):
    """
    HRESULT InternetGetDialBrandingW(
        LPWSTR pwzConnectoid,
        IDialBranding** ppdb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzConnectoid", "ppdb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_ReadGuidsForConnectedNetworks(jitter):
    """
    BOOLAPI ReadGuidsForConnectedNetworks(
        DWORD* pcNetworks,
        PWSTR** pppwszNetworkGuids,
        BSTR** pppbstrNetworkNames,
        PWSTR** pppwszGWMacs,
        DWORD* pcGatewayMacs,
        DWORD* pdwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcNetworks", "pppwszNetworkGuids", "pppbstrNetworkNames", "pppwszGWMacs", "pcGatewayMacs", "pdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetSetDialState(jitter, get_str, set_str):
    """
    BOOLAPI InternetSetDialState(
        LPCTSTR lpszConnectoid,
        DWORD dwState,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszConnectoid", "dwState", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetSetDialStateA(jitter):
    wininet_InternetSetDialState(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetSetDialStateW(jitter):
    wininet_InternetSetDialState(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_InternetSetDialState(jitter):
    """
    BOOLAPI InternetSetDialState(
        LPCSTR lpszConnectoid,
        DWORD dwState,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszConnectoid", "dwState", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_IsHostInProxyBypassList(jitter):
    """
    BOOLAPI IsHostInProxyBypassList(
        INTERNET_SCHEME tScheme,
        LPCSTR lpszHost,
        DWORD cchHost
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["tScheme", "lpszHost", "cchHost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetFreeProxyInfoList(jitter):
    """
    VOID InternetFreeProxyInfoList(
        WININET_PROXY_INFO_LIST* pProxyInfoList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxyInfoList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetGetProxyForUrl(jitter):
    """
    [ERROR_CODE] InternetGetProxyForUrl(
        HINTERNET hInternet,
        PCWSTR pcwszUrl,
        WININET_PROXY_INFO_LIST* pProxyInfoList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "pcwszUrl", "pProxyInfoList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_DoConnectoidsExist(jitter):
    """
    BOOL DoConnectoidsExist()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GetDiskInfoA(jitter):
    """
    BOOLAPI GetDiskInfoA(
        PCSTR pszPath,
        PDWORD pdwClusterSize,
        PDWORDLONG pdlAvail,
        PDWORDLONG pdlTotal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pdwClusterSize", "pdlAvail", "pdlTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_PerformOperationOverUrlCacheA(jitter):
    """
    BOOL PerformOperationOverUrlCacheA(
        PCSTR pszUrlSearchPattern,
        DWORD dwFlags,
        DWORD dwFilter,
        GROUPID GroupId,
        PVOID pReserved1,
        PDWORD pdwReserved2,
        PVOID pReserved3,
        CACHE_OPERATOR op,
        PVOID pOperatorData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUrlSearchPattern", "dwFlags", "dwFilter", "GroupId", "pReserved1", "pdwReserved2", "pReserved3", "op", "pOperatorData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_IsProfilesEnabled(jitter):
    """
    BOOL IsProfilesEnabled()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet__GetFileExtensionFromUrl(jitter):
    """
    [ERROR_CODE] _GetFileExtensionFromUrl(
        LPSTR lpszUrl,
        DWORD dwFlags,
        LPSTR lpszExt,
        DWORD* pcchExt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrl", "dwFlags", "lpszExt", "pcchExt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternalInternetGetCookie(jitter):
    """
    [ERROR_CODE] InternalInternetGetCookie(
        LPCSTR lpszUrl,
        LPSTR lpszCookieData,
        DWORD* lpdwDataSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrl", "lpszCookieData", "lpdwDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_ImportCookieFile(jitter, get_str, set_str):
    """
    BOOLAPI ImportCookieFile(
        LPCTSTR szFilename
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szFilename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_ImportCookieFileA(jitter):
    wininet_ImportCookieFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_ImportCookieFileW(jitter):
    wininet_ImportCookieFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_ExportCookieFile(jitter, get_str, set_str):
    """
    BOOLAPI ExportCookieFile(
        LPCTSTR szFilename,
        BOOL fAppend
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szFilename", "fAppend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_ExportCookieFileA(jitter):
    wininet_ExportCookieFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_ExportCookieFileW(jitter):
    wininet_ExportCookieFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_IsDomainLegalCookieDomain(jitter, get_str, set_str):
    """
    BOOLAPI IsDomainLegalCookieDomain(
        LPCTSTR pchDomain,
        LPCTSTR pchFullDomain
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pchDomain", "pchFullDomain"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_IsDomainLegalCookieDomainA(jitter):
    wininet_IsDomainLegalCookieDomain(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_IsDomainLegalCookieDomainW(jitter):
    wininet_IsDomainLegalCookieDomain(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_UrlZonesDetach(jitter):
    """
    VOID UrlZonesDetach()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_ReadUrlCacheEntryStreamEx(jitter):
    """
    BOOLAPI ReadUrlCacheEntryStreamEx(
        HANDLE hUrlCacheStream,
        DWORDLONG qwLocation,
        LPVOID lpBuffer,
        LPDWORD lpdwLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUrlCacheStream", "qwLocation", "lpBuffer", "lpdwLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_MapResourceToPolicy(jitter):
    """
    P3PStatus MapResourceToPolicy(
        P3PResource* pResource,
        P3PURL pszPolicy,
        unsigned long dwSize,
        P3PSignal* pSignal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pResource", "pszPolicy", "dwSize", "pSignal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GetP3PPolicy(jitter):
    """
    P3PStatus GetP3PPolicy(
        P3PCURL pszPolicyURL,
        HANDLE hDestination,
        P3PCXSL pszXSLtransform,
        P3PSignal* pSignal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPolicyURL", "hDestination", "pszXSLtransform", "pSignal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FreeP3PObject(jitter):
    """
    P3PStatus FreeP3PObject(
        P3PHANDLE hObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_GetP3PRequestStatus(jitter):
    """
    P3PStatus GetP3PRequestStatus(
        P3PHANDLE hObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetSetOptionEx(jitter, get_str, set_str):
    """
    BOOLAPI InternetSetOptionEx(
        HINTERNET hInternet,
        [INTERNET_OPTION] dwOption,
        LPVOID lpBuffer,
        DWORD dwBufferLength,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInternet", "dwOption", "lpBuffer", "dwBufferLength", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_InternetSetOptionExA(jitter):
    wininet_InternetSetOptionEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wininet_InternetSetOptionExW(jitter):
    wininet_InternetSetOptionEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wininet_FtpPutFileEx(jitter):
    """
    BOOLAPI FtpPutFileEx(
        HINTERNET hFtpSession,
        LPCWSTR lpszLocalFile,
        LPCSTR lpszNewRemoteFile,
        DWORD dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFtpSession", "lpszLocalFile", "lpszNewRemoteFile", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_FtpGetFileEx(jitter):
    """
    BOOLAPI FtpGetFileEx(
        HINTERNET hFtpSession,
        LPCSTR lpszRemoteFile,
        LPCWSTR lpszNewFile,
        BOOL fFailIfExists,
        [FileAttributes] dwFlagsAndAttributes,
        [FTP_TRANSFER_FLAGS] dwFlags,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFtpSession", "lpszRemoteFile", "lpszNewFile", "fFailIfExists", "dwFlagsAndAttributes", "dwFlags", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_DeleteWpadCacheForNetworks(jitter):
    """
    BOOLAPI DeleteWpadCacheForNetworks(
        WPAD_CACHE_DELETE enType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["enType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpWebSocketCompleteUpgrade(jitter):
    """
    HINTERNET HttpWebSocketCompleteUpgrade(
        HINTERNET hRequest,
        DWORD_PTR dwContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRequest", "dwContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpWebSocketSend(jitter):
    """
    BOOLAPI HttpWebSocketSend(
        HINTERNET hWebSocket,
        HTTP_WEB_SOCKET_BUFFER_TYPE BufferType,
        PVOID pvBuffer,
        DWORD dwBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "BufferType", "pvBuffer", "dwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpWebSocketReceive(jitter):
    """
    BOOLAPI HttpWebSocketReceive(
        HINTERNET hWebSocket,
        PVOID pvBuffer,
        DWORD dwBufferLength,
        DWORD* pdwBytesRead,
        HTTP_WEB_SOCKET_BUFFER_TYPE* pBufferType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pvBuffer", "dwBufferLength", "pdwBytesRead", "pBufferType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpWebSocketClose(jitter):
    """
    BOOLAPI HttpWebSocketClose(
        HINTERNET hWebSocket,
        HTTP_WEB_SOCKET_CLOSE_STATUS usStatus,
        PVOID pvReason,
        DWORD dwReasonLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "usStatus", "pvReason", "dwReasonLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpWebSocketShutdown(jitter):
    """
    BOOLAPI HttpWebSocketShutdown(
        HINTERNET hWebSocket,
        HTTP_WEB_SOCKET_CLOSE_STATUS usStatus,
        PVOID pvReason,
        DWORD dwReasonLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "usStatus", "pvReason", "dwReasonLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wininet_HttpWebSocketQueryCloseStatus(jitter):
    """
    BOOLAPI HttpWebSocketQueryCloseStatus(
        HINTERNET hWebSocket,
        HTTP_WEB_SOCKET_CLOSE_STATUS* pusStatus,
        PVOID pvReason,
        DWORD dwReasonLength,
        DWORD* pdwReasonLengthConsumed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pusStatus", "pvReason", "dwReasonLength", "pdwReasonLengthConsumed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
