###### Enums ######
WEB_SOCKET_ACTION = {
    "WEB_SOCKET_NO_ACTION": 0,
    "WEB_SOCKET_SEND_TO_NETWORK_ACTION": 1,
    "WEB_SOCKET_INDICATE_SEND_COMPLETE_ACTION": 2,
    "WEB_SOCKET_RECEIVE_FROM_NETWORK_ACTION": 3,
    "WEB_SOCKET_INDICATE_RECEIVE_COMPLETE_ACTION": 4,
}
WEB_SOCKET_ACTION_INV = {
    0: "WEB_SOCKET_NO_ACTION",
    1: "WEB_SOCKET_SEND_TO_NETWORK_ACTION",
    2: "WEB_SOCKET_INDICATE_SEND_COMPLETE_ACTION",
    3: "WEB_SOCKET_RECEIVE_FROM_NETWORK_ACTION",
    4: "WEB_SOCKET_INDICATE_RECEIVE_COMPLETE_ACTION",
}
WEB_SOCKET_ACTION_QUEUE = {
    "WEB_SOCKET_SEND_ACTION_QUEUE": 0x1,
    "WEB_SOCKET_RECEIVE_ACTION_QUEUE": 0x2,
    "WEB_SOCKET_ALL_ACTION_QUEUE": 0x3,
}
WEB_SOCKET_ACTION_QUEUE_INV = {
    0x1: "WEB_SOCKET_SEND_ACTION_QUEUE",
    0x2: "WEB_SOCKET_RECEIVE_ACTION_QUEUE",
    0x3: "WEB_SOCKET_ALL_ACTION_QUEUE",
}
WEB_SOCKET_BUFFER_TYPE = {
    "WEB_SOCKET_UTF8_MESSAGE_BUFFER_TYPE": 0x80000000,
    "WEB_SOCKET_UTF8_FRAGMENT_BUFFER_TYPE": 0x80000001,
    "WEB_SOCKET_BINARY_MESSAGE_BUFFER_TYPE": 0x80000002,
    "WEB_SOCKET_BINARY_FRAGMENT_BUFFER_TYPE": 0x80000003,
    "WEB_SOCKET_CLOSE_BUFFER_TYPE": 0x80000004,
    "WEB_SOCKET_PING_PONG_BUFFER_TYPE": 0x80000005,
    "WEB_SOCKET_UNSOLICITED_PONG_BUFFER_TYPE": 0x80000006,
}
WEB_SOCKET_BUFFER_TYPE_INV = {
    0x80000000: "WEB_SOCKET_UTF8_MESSAGE_BUFFER_TYPE",
    0x80000001: "WEB_SOCKET_UTF8_FRAGMENT_BUFFER_TYPE",
    0x80000002: "WEB_SOCKET_BINARY_MESSAGE_BUFFER_TYPE",
    0x80000003: "WEB_SOCKET_BINARY_FRAGMENT_BUFFER_TYPE",
    0x80000004: "WEB_SOCKET_CLOSE_BUFFER_TYPE",
    0x80000005: "WEB_SOCKET_PING_PONG_BUFFER_TYPE",
    0x80000006: "WEB_SOCKET_UNSOLICITED_PONG_BUFFER_TYPE",
}
WEB_SOCKET_CLOSE_STATUS = {
    "WEB_SOCKET_SUCCESS_CLOSE_STATUS": 1000,
    "WEB_SOCKET_ENDPOINT_UNAVAILABLE_CLOSE_STATUS": 1001,
    "WEB_SOCKET_PROTOCOL_ERROR_CLOSE_STATUS": 1002,
    "WEB_SOCKET_INVALID_DATA_TYPE_CLOSE_STATUS": 1003,
    "WEB_SOCKET_EMPTY_CLOSE_STATUS": 1005,
    "WEB_SOCKET_ABORTED_CLOSE_STATUS": 1006,
    "WEB_SOCKET_INVALID_PAYLOAD_CLOSE_STATUS": 1007,
    "WEB_SOCKET_POLICY_VIOLATION_CLOSE_STATUS": 1008,
    "WEB_SOCKET_MESSAGE_TOO_BIG_CLOSE_STATUS": 1009,
    "WEB_SOCKET_UNSUPPORTED_EXTENSIONS_CLOSE_STATUS": 1010,
    "WEB_SOCKET_SERVER_ERROR_CLOSE_STATUS": 1011,
    "WEB_SOCKET_SECURE_HANDSHAKE_ERROR_CLOSE_STATUS": 1015,
}
WEB_SOCKET_CLOSE_STATUS_INV = {
    1000: "WEB_SOCKET_SUCCESS_CLOSE_STATUS",
    1001: "WEB_SOCKET_ENDPOINT_UNAVAILABLE_CLOSE_STATUS",
    1002: "WEB_SOCKET_PROTOCOL_ERROR_CLOSE_STATUS",
    1003: "WEB_SOCKET_INVALID_DATA_TYPE_CLOSE_STATUS",
    1005: "WEB_SOCKET_EMPTY_CLOSE_STATUS",
    1006: "WEB_SOCKET_ABORTED_CLOSE_STATUS",
    1007: "WEB_SOCKET_INVALID_PAYLOAD_CLOSE_STATUS",
    1008: "WEB_SOCKET_POLICY_VIOLATION_CLOSE_STATUS",
    1009: "WEB_SOCKET_MESSAGE_TOO_BIG_CLOSE_STATUS",
    1010: "WEB_SOCKET_UNSUPPORTED_EXTENSIONS_CLOSE_STATUS",
    1011: "WEB_SOCKET_SERVER_ERROR_CLOSE_STATUS",
    1015: "WEB_SOCKET_SECURE_HANDSHAKE_ERROR_CLOSE_STATUS",
}
WEB_SOCKET_PROPERTY_TYPE = {
    "WEB_SOCKET_RECEIVE_BUFFER_SIZE_PROPERTY_TYPE": 0,
    "WEB_SOCKET_SEND_BUFFER_SIZE_PROPERTY_TYPE": 1,
    "WEB_SOCKET_DISABLE_MASKING_PROPERTY_TYPE": 2,
    "WEB_SOCKET_ALLOCATED_BUFFER_PROPERTY_TYPE": 3,
    "WEB_SOCKET_DISABLE_UTF8_VERIFICATION_PROPERTY_TYPE": 4,
    "WEB_SOCKET_KEEPALIVE_INTERVAL_PROPERTY_TYPE": 5,
    "WEB_SOCKET_SUPPORTED_VERSIONS_PROPERTY_TYPE": 6,
}
WEB_SOCKET_PROPERTY_TYPE_INV = {
    0: "WEB_SOCKET_RECEIVE_BUFFER_SIZE_PROPERTY_TYPE",
    1: "WEB_SOCKET_SEND_BUFFER_SIZE_PROPERTY_TYPE",
    2: "WEB_SOCKET_DISABLE_MASKING_PROPERTY_TYPE",
    3: "WEB_SOCKET_ALLOCATED_BUFFER_PROPERTY_TYPE",
    4: "WEB_SOCKET_DISABLE_UTF8_VERIFICATION_PROPERTY_TYPE",
    5: "WEB_SOCKET_KEEPALIVE_INTERVAL_PROPERTY_TYPE",
    6: "WEB_SOCKET_SUPPORTED_VERSIONS_PROPERTY_TYPE",
}

###################

###### Types ######
WEB_SOCKET_HANDLE = HANDLE
WEB_SOCKET_HANDLE_PTR = Ptr("<I", WEB_SOCKET_HANDLE())
WEB_SOCKET_ACTION = UINT
WEB_SOCKET_ACTION_PTR = Ptr("<I", WEB_SOCKET_ACTION())
WEB_SOCKET_ACTION_QUEUE = UINT
WEB_SOCKET_BUFFER_TYPE = UINT
WEB_SOCKET_BUFFER_TYPE_PTR = Ptr("<I", WEB_SOCKET_BUFFER_TYPE())
WEB_SOCKET_CLOSE_STATUS = USHORT
WEB_SOCKET_PROPERTY_TYPE = UINT

class _WEB_SOCKET_BUFFER_s1_(MemStruct):
    fields = [
        # Length is `ulBufferLength`
        ("pbBuffer", PBYTE()),
        ("ulBufferLength", ULONG()),
    ]


class _WEB_SOCKET_BUFFER_s2_(MemStruct):
    fields = [
        # Length is `ulReasonLength`
        ("pbReason", PBYTE()),
        ("ulReasonLength", ULONG()),
        ("usStatus", WEB_SOCKET_CLOSE_STATUS()),
    ]

WEB_SOCKET_BUFFER = Union([
    ("Data", _WEB_SOCKET_BUFFER_s1_),
    ("CloseStatus", _WEB_SOCKET_BUFFER_s2_),
])
WEB_SOCKET_BUFFER_PTR = Ptr("<I", WEB_SOCKET_BUFFER())

class WEB_SOCKET_HTTP_HEADER(MemStruct):
    fields = [
        ("pcName", PCHAR()),
        ("ulNameLength", ULONG()),
        ("pcValue", PCHAR()),
        ("ulValueLength", ULONG()),
    ]

PWEB_SOCKET_HTTP_HEADER = Ptr("<I", WEB_SOCKET_HTTP_HEADER())
PWEB_SOCKET_HTTP_HEADER_PTR = Ptr("<I", PWEB_SOCKET_HTTP_HEADER())
const_PWEB_SOCKET_HTTP_HEADER = Ptr("<I", WEB_SOCKET_HTTP_HEADER())

class WEB_SOCKET_PROPERTY(MemStruct):
    fields = [
        ("Type", WEB_SOCKET_PROPERTY_TYPE()),
        # Length is `ulValueSize`
        ("pvValue", PVOID()),
        ("ulValueSize", ULONG()),
    ]

const_PWEB_SOCKET_PROPERTY = Ptr("<I", WEB_SOCKET_PROPERTY())

###################

###### Functions ######

def websocket_WebSocketAbortHandle(jitter):
    """
    VOID WebSocketAbortHandle(
        WEB_SOCKET_HANDLE hWebSocket
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketBeginClientHandshake(jitter):
    """
    HRESULT WebSocketBeginClientHandshake(
        WEB_SOCKET_HANDLE hWebSocket,
        PCSTR* pszSubprotocols,
        ULONG ulSubprotocolCount,
        PCSTR* pszExtensions,
        ULONG ulExtensionCount,
        const PWEB_SOCKET_HTTP_HEADER pInitialHeaders,
        ULONG ulInitialHeaderCount,
        PWEB_SOCKET_HTTP_HEADER* pAdditionalHeaders,
        ULONG* pulAdditionalHeaderCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pszSubprotocols", "ulSubprotocolCount", "pszExtensions", "ulExtensionCount", "pInitialHeaders", "ulInitialHeaderCount", "pAdditionalHeaders", "pulAdditionalHeaderCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketBeginServerHandshake(jitter):
    """
    HRESULT WebSocketBeginServerHandshake(
        WEB_SOCKET_HANDLE hWebSocket,
        PCSTR pszSubprotocolSelected,
        PCSTR* pszExtensionSelected,
        ULONG ulExtensionSelectedCount,
        const PWEB_SOCKET_HTTP_HEADER pRequestHeaders,
        ULONG ulRequestHeaderCount,
        PWEB_SOCKET_HTTP_HEADER* pResponseHeaders,
        ULONG* pulResponseHeaderCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pszSubprotocolSelected", "pszExtensionSelected", "ulExtensionSelectedCount", "pRequestHeaders", "ulRequestHeaderCount", "pResponseHeaders", "pulResponseHeaderCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketCompleteAction(jitter):
    """
    VOID WebSocketCompleteAction(
        WEB_SOCKET_HANDLE hWebSocket,
        PVOID pvActionContext,
        ULONG ulBytesTransferred
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pvActionContext", "ulBytesTransferred"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketCreateClientHandle(jitter):
    """
    HRESULT WebSocketCreateClientHandle(
        const PWEB_SOCKET_PROPERTY pProperties,
        ULONG ulPropertyCount,
        WEB_SOCKET_HANDLE* phWebSocket
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProperties", "ulPropertyCount", "phWebSocket"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketCreateServerHandle(jitter):
    """
    HRESULT WebSocketCreateServerHandle(
        const PWEB_SOCKET_PROPERTY pProperties,
        ULONG ulPropertyCount,
        WEB_SOCKET_HANDLE* phWebSocket
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProperties", "ulPropertyCount", "phWebSocket"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketDeleteHandle(jitter):
    """
    VOID WebSocketDeleteHandle(
        WEB_SOCKET_HANDLE hWebSocket
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketEndClientHandshake(jitter):
    """
    HRESULT WebSocketEndClientHandshake(
        WEB_SOCKET_HANDLE hWebSocket,
        const PWEB_SOCKET_HTTP_HEADER pResponseHeaders,
        ULONG ulReponseHeaderCount,
        ULONG* pulSelectedExtensions,
        ULONG* pulSelectedExtensionCount,
        ULONG* pulSelectedSubprotocol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pResponseHeaders", "ulReponseHeaderCount", "pulSelectedExtensions", "pulSelectedExtensionCount", "pulSelectedSubprotocol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketEndServerHandshake(jitter):
    """
    HRESULT WebSocketEndServerHandshake(
        WEB_SOCKET_HANDLE hWebSocket
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketGetAction(jitter):
    """
    HRESULT WebSocketGetAction(
        WEB_SOCKET_HANDLE hWebSocket,
        WEB_SOCKET_ACTION_QUEUE eActionQueue,
        WEB_SOCKET_BUFFER* pDataBuffers,
        ULONG* pulDataBufferCount,
        WEB_SOCKET_ACTION* pAction,
        WEB_SOCKET_BUFFER_TYPE* pBufferType,
        PVOID* pvApplicationContext,
        PVOID* pvActionContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "eActionQueue", "pDataBuffers", "pulDataBufferCount", "pAction", "pBufferType", "pvApplicationContext", "pvActionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketGetGlobalProperty(jitter):
    """
    HRESULT WebSocketGetGlobalProperty(
        WEB_SOCKET_PROPERTY eType,
        PVOID pvValue,
        ULONG* ulSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["eType", "pvValue", "ulSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketReceive(jitter):
    """
    HRESULT WebSocketReceive(
        WEB_SOCKET_HANDLE hWebSocket,
        WEB_SOCKET_BUFFER* pBuffer,
        PVOID pvContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pBuffer", "pvContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketSend(jitter):
    """
    HRESULT WebSocketSend(
        WEB_SOCKET_HANDLE hWebSocket,
        WEB_SOCKET_BUFFER_TYPE BufferType,
        WEB_SOCKET_BUFFER* pBuffer,
        PVOID Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "BufferType", "pBuffer", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
