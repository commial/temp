
def websocket_WebSocketAbortHandle(jitter):
    """"
    [Websocket] VOID WebSocketAbortHandle(WEB_SOCKET_HANDLE hWebSocket)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketBeginClientHandshake(jitter):
    """"
    [Websocket] HRESULT WebSocketBeginClientHandshake(WEB_SOCKET_HANDLE hWebSocket, PCSTR* pszSubprotocols, ULONG ulSubprotocolCount, PCSTR* pszExtensions, ULONG ulExtensionCount, const PWEB_SOCKET_HTTP_HEADER pInitialHeaders, ULONG ulInitialHeaderCount, PWEB_SOCKET_HTTP_HEADER* pAdditionalHeaders, ULONG* pulAdditionalHeaderCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pszSubprotocols", "ulSubprotocolCount", "pszExtensions", "ulExtensionCount", "pInitialHeaders", "ulInitialHeaderCount", "pAdditionalHeaders", "pulAdditionalHeaderCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketBeginServerHandshake(jitter):
    """"
    [Websocket] HRESULT WebSocketBeginServerHandshake(WEB_SOCKET_HANDLE hWebSocket, PCSTR pszSubprotocolSelected, PCSTR* pszExtensionSelected, ULONG ulExtensionSelectedCount, const PWEB_SOCKET_HTTP_HEADER pRequestHeaders, ULONG ulRequestHeaderCount, PWEB_SOCKET_HTTP_HEADER* pResponseHeaders, ULONG* pulResponseHeaderCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pszSubprotocolSelected", "pszExtensionSelected", "ulExtensionSelectedCount", "pRequestHeaders", "ulRequestHeaderCount", "pResponseHeaders", "pulResponseHeaderCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketCompleteAction(jitter):
    """"
    [Websocket] VOID WebSocketCompleteAction(WEB_SOCKET_HANDLE hWebSocket, PVOID pvActionContext, ULONG ulBytesTransferred)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pvActionContext", "ulBytesTransferred"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketCreateClientHandle(jitter):
    """"
    [Websocket] HRESULT WebSocketCreateClientHandle(const PWEB_SOCKET_PROPERTY pProperties, ULONG ulPropertyCount, WEB_SOCKET_HANDLE* phWebSocket)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pProperties", "ulPropertyCount", "phWebSocket"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketCreateServerHandle(jitter):
    """"
    [Websocket] HRESULT WebSocketCreateServerHandle(const PWEB_SOCKET_PROPERTY pProperties, ULONG ulPropertyCount, WEB_SOCKET_HANDLE* phWebSocket)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pProperties", "ulPropertyCount", "phWebSocket"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketDeleteHandle(jitter):
    """"
    [Websocket] VOID WebSocketDeleteHandle(WEB_SOCKET_HANDLE hWebSocket)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketEndClientHandshake(jitter):
    """"
    [Websocket] HRESULT WebSocketEndClientHandshake(WEB_SOCKET_HANDLE hWebSocket, const PWEB_SOCKET_HTTP_HEADER pResponseHeaders, ULONG ulReponseHeaderCount, ULONG* pulSelectedExtensions, ULONG* pulSelectedExtensionCount, ULONG* pulSelectedSubprotocol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pResponseHeaders", "ulReponseHeaderCount", "pulSelectedExtensions", "pulSelectedExtensionCount", "pulSelectedSubprotocol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketEndServerHandshake(jitter):
    """"
    [Websocket] HRESULT WebSocketEndServerHandshake(WEB_SOCKET_HANDLE hWebSocket)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketGetAction(jitter):
    """"
    [Websocket] HRESULT WebSocketGetAction(WEB_SOCKET_HANDLE hWebSocket, WEB_SOCKET_ACTION_QUEUE eActionQueue, WEB_SOCKET_BUFFER* pDataBuffers, ULONG* pulDataBufferCount, WEB_SOCKET_ACTION* pAction, WEB_SOCKET_BUFFER_TYPE* pBufferType, PVOID* pvApplicationContext, PVOID* pvActionContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "eActionQueue", "pDataBuffers", "pulDataBufferCount", "pAction", "pBufferType", "pvApplicationContext", "pvActionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketGetGlobalProperty(jitter):
    """"
    [Websocket] HRESULT WebSocketGetGlobalProperty(WEB_SOCKET_PROPERTY eType, PVOID pvValue, ULONG* ulSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["eType", "pvValue", "ulSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketReceive(jitter):
    """"
    [Websocket] HRESULT WebSocketReceive(WEB_SOCKET_HANDLE hWebSocket, WEB_SOCKET_BUFFER* pBuffer, PVOID pvContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "pBuffer", "pvContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def websocket_WebSocketSend(jitter):
    """"
    [Websocket] HRESULT WebSocketSend(WEB_SOCKET_HANDLE hWebSocket, WEB_SOCKET_BUFFER_TYPE BufferType, WEB_SOCKET_BUFFER* pBuffer, PVOID Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWebSocket", "BufferType", "pBuffer", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
