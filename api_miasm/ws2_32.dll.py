###### Enums ######
_WsaIoctl_ = {
    "SIO_ASSOCIATE_HANDLE": 0x88000001,
    "SIO_ENABLE_CIRCULAR_QUEUEING": 0x28000002,
    "SIO_FIND_ROUTE": 0x48000003,
    "SIO_FLUSH": 0x28000004,
    "SIO_GET_BROADCAST_ADDRESS": 0x48000005,
    "SIO_GET_EXTENSION_FUNCTION_POINTER": 0xc8000006,
    "SIO_GET_QOS": 0xc8000007,
    "SIO_GET_GROUP_QOS": 0xc8000008,
    "SIO_MULTIPOINT_LOOPBACK": 0x88000009,
    "SIO_MULTICAST_SCOPE": 0x8800000a,
    "SIO_SET_QOS": 0x8800000b,
    "SIO_SET_GROUP_QOS": 0x8800000c,
    "SIO_TRANSLATE_HANDLE": 0xc800000d,
    "SIO_ROUTING_INTERFACE_QUERY": 0xc8000014,
    "SIO_ROUTING_INTERFACE_CHANGE": 0x88000015,
    "SIO_ADDRESS_LIST_QUERY": 0x48000016,
    "SIO_ADDRESS_LIST_CHANGE": 0x28000017,
    "SIO_QUERY_TARGET_PNP_HANDLE": 0x48000018,
    "SIO_ADDRESS_LIST_SORT": 0xc8000019,
    "SIO_RESERVED_1": 0x8800001a,
    "SIO_RESERVED_2": 0x88000021,
}
_WsaIoctl__INV = {
    0x88000001: "SIO_ASSOCIATE_HANDLE",
    0x28000002: "SIO_ENABLE_CIRCULAR_QUEUEING",
    0x48000003: "SIO_FIND_ROUTE",
    0x28000004: "SIO_FLUSH",
    0x48000005: "SIO_GET_BROADCAST_ADDRESS",
    0xc8000006: "SIO_GET_EXTENSION_FUNCTION_POINTER",
    0xc8000007: "SIO_GET_QOS",
    0xc8000008: "SIO_GET_GROUP_QOS",
    0x88000009: "SIO_MULTIPOINT_LOOPBACK",
    0x8800000a: "SIO_MULTICAST_SCOPE",
    0x8800000b: "SIO_SET_QOS",
    0x8800000c: "SIO_SET_GROUP_QOS",
    0xc800000d: "SIO_TRANSLATE_HANDLE",
    0xc8000014: "SIO_ROUTING_INTERFACE_QUERY",
    0x88000015: "SIO_ROUTING_INTERFACE_CHANGE",
    0x48000016: "SIO_ADDRESS_LIST_QUERY",
    0x28000017: "SIO_ADDRESS_LIST_CHANGE",
    0x48000018: "SIO_QUERY_TARGET_PNP_HANDLE",
    0xc8000019: "SIO_ADDRESS_LIST_SORT",
    0x8800001a: "SIO_RESERVED_1",
    0x88000021: "SIO_RESERVED_2",
}

###################

###### Types ######
_WSA_ERROR_ = _ERROR_CODE_
_LookupServiceFlags_ = DWORD
_WsaFlags_ = DWORD
_WsaIoctl_ = DWORD

###################

###### Functions ######

def ws2_32_accept(jitter):
    """
    SOCKET accept(
        SOCKET s,
        struct sockaddr* addr,
        int* addrlen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "addr", "addrlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_bind(jitter):
    """
    [SocketCode-int] bind(
        SOCKET s,
        const struct sockaddr* name,
        int namelen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "name", "namelen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_closesocket(jitter):
    """
    [SocketCode-int] closesocket(
        SOCKET s
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_connect(jitter):
    """
    [SocketCode-int] connect(
        SOCKET s,
        const struct sockaddr* name,
        int namelen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "name", "namelen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_freeaddrinfo(jitter):
    """
    void freeaddrinfo(
        struct addrinfo* ai
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ai"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_getaddrinfo(jitter):
    """
    [WSA_ERROR] getaddrinfo(
        const char* nodename,
        const char* servname,
        const struct addrinfo* hints,
        struct addrinfo** res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nodename", "servname", "hints", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_FreeAddrInfoEx(jitter, get_str, set_str):
    """
    void FreeAddrInfoEx(
        PADDRINFOEX pAddrInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAddrInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_FreeAddrInfoExA(jitter):
    ws2_32_FreeAddrInfoEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_FreeAddrInfoExW(jitter):
    ws2_32_FreeAddrInfoEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_GetAddrInfoEx(jitter, get_str, set_str):
    """
    [WSA_ERROR] GetAddrInfoEx(
        PCTSTR pName,
        PCTSTR pServiceName,
        [NameSpaceFlags] dwNameSpace,
        LPGUID lpNspId,
        const ADDRINFOEX* pHints,
        PADDRINFOEX* ppResult,
        struct timeval* timeout,
        LPOVERLAPPED lpOverlapped,
        LPLOOKUPSERVICE_COMPLETION_ROUTINE lpCompletionRoutine,
        LPHANDLE lpNameHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pServiceName", "dwNameSpace", "lpNspId", "pHints", "ppResult", "timeout", "lpOverlapped", "lpCompletionRoutine", "lpNameHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_GetAddrInfoExA(jitter):
    ws2_32_GetAddrInfoEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_GetAddrInfoExW(jitter):
    ws2_32_GetAddrInfoEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_FreeAddrInfoW(jitter):
    """
    void FreeAddrInfoW(
        PADDRINFOW pAddrInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAddrInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_GetAddrInfoW(jitter):
    """
    [WSA_ERROR] GetAddrInfoW(
        PCWSTR pNodeName,
        PCWSTR pServiceName,
        const ADDRINFOW* pHints,
        PADDRINFOW* ppResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pNodeName", "pServiceName", "pHints", "ppResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_gethostbyaddr(jitter):
    """
    struct hostent* gethostbyaddr(
        const char* addr,
        int len,
        [AddressFamily] type
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["addr", "len", "type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_gethostbyname(jitter):
    """
    struct hostent* gethostbyname(
        const char* name
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["name"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_gethostname(jitter):
    """
    [SocketCode-int] gethostname(
        char* name,
        int namelen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["name", "namelen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_getnameinfo(jitter):
    """
    [WSA_ERROR] getnameinfo(
        const struct sockaddr* sa,
        socklen_t salen,
        char* host,
        DWORD hostlen,
        char* serv,
        DWORD servlen,
        [NI_Flags] flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sa", "salen", "host", "hostlen", "serv", "servlen", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_GetNameInfoW(jitter):
    """
    [WSA_ERROR] GetNameInfoW(
        const SOCKADDR* pSockaddr,
        socklen_t SockaddrLength,
        PWCHAR pNodeBuffer,
        DWORD NodeBufferSize,
        PWCHAR pServiceBuffer,
        DWORD ServiceBufferSize,
        [NI_Flags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSockaddr", "SockaddrLength", "pNodeBuffer", "NodeBufferSize", "pServiceBuffer", "ServiceBufferSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_getpeername(jitter):
    """
    [SocketCode-int] getpeername(
        SOCKET s,
        struct sockaddr* name,
        int* namelen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "name", "namelen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_getprotobyname(jitter):
    """
    struct PROTOENT* getprotobyname(
        const char* name
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["name"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_getprotobynumber(jitter):
    """
    struct PROTOENT* getprotobynumber(
        int number
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["number"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_getservbyname(jitter):
    """
    struct servent* getservbyname(
        const char* name,
        const char* proto
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["name", "proto"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_getservbyport(jitter):
    """
    struct servent* getservbyport(
        int port,
        const char* proto
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["port", "proto"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_getsockname(jitter):
    """
    [SocketCode-int] getsockname(
        SOCKET s,
        struct sockaddr* name,
        int* namelen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "name", "namelen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_getsockopt(jitter):
    """
    [SocketCode-int] getsockopt(
        SOCKET s,
        [SocketLevel] level,
        [SocketOption] optname,
        [LPVOID|char*] optval,
        int* optlen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "level", "optname", "optval", "optlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_htonl(jitter):
    """
    u_long htonl(
        u_long hostlong
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hostlong"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_htons(jitter):
    """
    u_short htons(
        u_short hostshort
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hostshort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_inet_addr(jitter):
    """
    [INET_ADDR_OUTPUT] inet_addr(
        const char* cp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_inet_ntoa(jitter):
    """
    char* inet_ntoa(
        struct in_addr in
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["in"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_InetNtopW(jitter):
    """
    PCWSTR InetNtopW(
        INT Family,
        PVOID pAddr,
        PWSTR pStringBuf,
        size_t StringBufSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "pAddr", "pStringBuf", "StringBufSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_inet_ntop(jitter):
    """
    PCSTR inet_ntop(
        INT Family,
        PVOID pAddr,
        PSTR pStringBuf,
        size_t StringBufSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "pAddr", "pStringBuf", "StringBufSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_inet_pton(jitter):
    """
    PCSTR inet_pton(
        INT Family,
        PCSTR pszAddrString,
        PVOID pAddrBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "pszAddrString", "pAddrBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_InetPtonW(jitter):
    """
    PCWSTR InetPtonW(
        INT Family,
        PCWSTR pszAddrString,
        PVOID pAddrBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "pszAddrString", "pAddrBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_ioctlsocket(jitter):
    """
    [SocketCode-int] ioctlsocket(
        SOCKET s,
        [Socket_IOCTL] cmd,
        u_long* argp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "cmd", "argp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_listen(jitter):
    """
    [SocketCode-int] listen(
        SOCKET s,
        int backlog
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "backlog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_ntohl(jitter):
    """
    u_long ntohl(
        u_long netlong
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["netlong"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_ntohs(jitter):
    """
    u_short ntohs(
        u_short netshort
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["netshort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_recv(jitter):
    """
    [SocketCode-int] recv(
        SOCKET s,
        [LPVOID|char*] buf,
        int len,
        [SendRecvFlags] flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "buf", "len", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_recvfrom(jitter):
    """
    [SocketCode-int] recvfrom(
        SOCKET s,
        [LPVOID|char*] buf,
        int len,
        int flags,
        struct sockaddr* from,
        int* fromlen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "buf", "len", "flags", "from", "fromlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_select(jitter):
    """
    [SocketCode-int] select(
        int nfds,
        fd_set* readfds,
        fd_set* writefds,
        fd_set* exceptfds,
        const struct timeval* timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nfds", "readfds", "writefds", "exceptfds", "timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_send(jitter):
    """
    [SocketCode-int] send(
        SOCKET s,
        LPVOID buf,
        int len,
        [SendRecvFlags] flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "buf", "len", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_sendto(jitter):
    """
    [SocketCode-int] sendto(
        SOCKET s,
        LPVOID buf,
        int len,
        [SendRecvFlags] flags,
        const struct sockaddr* to,
        int tolen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "buf", "len", "flags", "to", "tolen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_SetAddrInfoEx(jitter, get_str, set_str):
    """
    [WSA_ERROR] SetAddrInfoEx(
        PCTSTR pName,
        PCTSTR pServiceName,
        SOCKET_ADDRESS* pAddresses,
        DWORD dwAddressCount,
        LPBLOB lpBlob,
        DWORD dwFlags,
        [NameSpaceFlags] dwNameSpace,
        LPGUID lpNspId,
        struct timeval* timeout,
        LPOVERLAPPED lpOverlapped,
        LPLOOKUPSERVICE_COMPLETION_ROUTINE lpCompletionRoutine,
        LPHANDLE lpNameHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pServiceName", "pAddresses", "dwAddressCount", "lpBlob", "dwFlags", "dwNameSpace", "lpNspId", "timeout", "lpOverlapped", "lpCompletionRoutine", "lpNameHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_SetAddrInfoExA(jitter):
    ws2_32_SetAddrInfoEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_SetAddrInfoExW(jitter):
    ws2_32_SetAddrInfoEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_setsockopt(jitter):
    """
    [SocketCode-int] setsockopt(
        SOCKET s,
        [SocketLevel] level,
        [SocketOption] optname,
        LPVOID optval,
        int optlen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "level", "optname", "optval", "optlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_shutdown(jitter):
    """
    [SocketCode-int] shutdown(
        SOCKET s,
        [SocketShutdownFlags] how
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "how"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_socket(jitter):
    """
    SOCKET socket(
        [AddressFamily] af,
        [SocketType] type,
        [SocketProtocol] protocol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["af", "type", "protocol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAAccept(jitter):
    """
    SOCKET WSAAccept(
        SOCKET s,
        struct sockaddr* addr,
        LPINT addrlen,
        LPCONDITIONPROC lpfnCondition,
        DWORD dwCallbackData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "addr", "addrlen", "lpfnCondition", "dwCallbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAAddressToString(jitter, get_str, set_str):
    """
    [SocketCode-INT] WSAAddressToString(
        LPSOCKADDR lpsaAddress,
        DWORD dwAddressLength,
        LPWSAPROTOCOL_INFO lpProtocolInfo,
        LPTSTR lpszAddressString,
        LPDWORD lpdwAddressStringLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpsaAddress", "dwAddressLength", "lpProtocolInfo", "lpszAddressString", "lpdwAddressStringLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAAddressToStringA(jitter):
    ws2_32_WSAAddressToString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSAAddressToStringW(jitter):
    ws2_32_WSAAddressToString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSAAsyncGetHostByAddr(jitter):
    """
    HANDLE WSAAsyncGetHostByAddr(
        HWND hWnd,
        unsigned int wMsg,
        const char* addr,
        int len,
        int type,
        char* buf,
        int buflen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "wMsg", "addr", "len", "type", "buf", "buflen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAAsyncGetHostByName(jitter):
    """
    HANDLE WSAAsyncGetHostByName(
        HWND hWnd,
        unsigned int wMsg,
        const char* name,
        char* buf,
        int buflen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "wMsg", "name", "buf", "buflen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAAsyncGetProtoByName(jitter):
    """
    HANDLE WSAAsyncGetProtoByName(
        HWND hWnd,
        unsigned int wMsg,
        const char* name,
        char* buf,
        int buflen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "wMsg", "name", "buf", "buflen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAAsyncGetProtoByNumber(jitter):
    """
    HANDLE WSAAsyncGetProtoByNumber(
        HWND hWnd,
        unsigned int wMsg,
        int number,
        char* buf,
        int buflen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "wMsg", "number", "buf", "buflen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAAsyncGetServByName(jitter):
    """
    HANDLE WSAAsyncGetServByName(
        HWND hWnd,
        unsigned int wMsg,
        const char* name,
        const char* proto,
        char* buf,
        int buflen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "wMsg", "name", "proto", "buf", "buflen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAAsyncGetServByPort(jitter):
    """
    HANDLE WSAAsyncGetServByPort(
        HWND hWnd,
        unsigned int wMsg,
        int port,
        const char* proto,
        char* buf,
        int buflen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "wMsg", "port", "proto", "buf", "buflen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAAsyncSelect(jitter):
    """
    [SocketCode-int] WSAAsyncSelect(
        SOCKET s,
        HWND hWnd,
        unsigned int wMsg,
        [FDEvents] lEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "hWnd", "wMsg", "lEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSACancelAsyncRequest(jitter):
    """
    [SocketCode-int] WSACancelAsyncRequest(
        HANDLE hAsyncTaskHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAsyncTaskHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSACleanup(jitter):
    """
    [SocketCode-int] WSACleanup()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSACloseEvent(jitter):
    """
    BOOL WSACloseEvent(
        WSAEVENT hEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAConnect(jitter):
    """
    [SocketCode-int] WSAConnect(
        SOCKET s,
        const struct sockaddr* name,
        int namelen,
        LPWSABUF lpCallerData,
        LPWSABUF lpCalleeData,
        LPQOS lpSQOS,
        LPQOS lpGQOS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "name", "namelen", "lpCallerData", "lpCalleeData", "lpSQOS", "lpGQOS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAConnectByList(jitter):
    """
    BOOL WSAConnectByList(
        SOCKET s,
        PSOCKET_ADDRESS_LIST SocketAddressList,
        LPDWORD LocalAddressLength,
        LPSOCKADDR LocalAddress,
        LPDWORD RemoteAddressLength,
        LPSOCKADDR RemoteAddress,
        const struct timeval* timeout,
        LPWSAOVERLAPPED Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "SocketAddressList", "LocalAddressLength", "LocalAddress", "RemoteAddressLength", "RemoteAddress", "timeout", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAConnectByName(jitter, get_str, set_str):
    """
    BOOL WSAConnectByName(
        SOCKET s,
        LPSTR nodename,
        LPSTR servicename,
        LPDWORD LocalAddressLength,
        LPSOCKADDR LocalAddress,
        LPDWORD RemoteAddressLength,
        LPSOCKADDR RemoteAddress,
        const struct timeval* timeout,
        LPWSAOVERLAPPED Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "nodename", "servicename", "LocalAddressLength", "LocalAddress", "RemoteAddressLength", "RemoteAddress", "timeout", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAConnectByNameA(jitter):
    ws2_32_WSAConnectByName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSAConnectByNameW(jitter):
    ws2_32_WSAConnectByName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSACreateEvent(jitter):
    """
    WSAEVENT WSACreateEvent()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSADuplicateSocket(jitter, get_str, set_str):
    """
    [SocketCode-int] WSADuplicateSocket(
        SOCKET s,
        DWORD dwProcessId,
        LPWSAPROTOCOL_INFO lpProtocolInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "dwProcessId", "lpProtocolInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSADuplicateSocketA(jitter):
    ws2_32_WSADuplicateSocket(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSADuplicateSocketW(jitter):
    ws2_32_WSADuplicateSocket(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSAEnumNameSpaceProviders(jitter, get_str, set_str):
    """
    [SocketCode-INT] WSAEnumNameSpaceProviders(
        LPDWORD lpdwBufferLength,
        LPWSANAMESPACE_INFO lpnspBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpdwBufferLength", "lpnspBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAEnumNameSpaceProvidersA(jitter):
    ws2_32_WSAEnumNameSpaceProviders(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSAEnumNameSpaceProvidersW(jitter):
    ws2_32_WSAEnumNameSpaceProviders(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSAEnumNameSpaceProvidersEx(jitter, get_str, set_str):
    """
    [SocketCode-INT] WSAEnumNameSpaceProvidersEx(
        LPDWORD lpdwBufferLength,
        LPWSANAMESPACE_INFOEX lpnspBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpdwBufferLength", "lpnspBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAEnumNameSpaceProvidersExA(jitter):
    ws2_32_WSAEnumNameSpaceProvidersEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSAEnumNameSpaceProvidersExW(jitter):
    ws2_32_WSAEnumNameSpaceProvidersEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSAEnumNetworkEvents(jitter):
    """
    [SocketCode-int] WSAEnumNetworkEvents(
        SOCKET s,
        WSAEVENT hEventObject,
        LPWSANETWORKEVENTS lpNetworkEvents
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "hEventObject", "lpNetworkEvents"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAEnumProtocols(jitter, get_str, set_str):
    """
    [SocketCode-int] WSAEnumProtocols(
        LPINT lpiProtocols,
        LPWSAPROTOCOL_INFO lpProtocolBuffer,
        LPDWORD lpdwBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpiProtocols", "lpProtocolBuffer", "lpdwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAEnumProtocolsA(jitter):
    ws2_32_WSAEnumProtocols(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSAEnumProtocolsW(jitter):
    ws2_32_WSAEnumProtocols(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSAEventSelect(jitter):
    """
    [SocketCode-int] WSAEventSelect(
        SOCKET s,
        WSAEVENT hEventObject,
        [FDEvents] lNetworkEvents
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "hEventObject", "lNetworkEvents"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAGetLastError(jitter):
    """
    [WSA_ERROR] WSAGetLastError()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAGetOverlappedResult(jitter):
    """
    BOOL WSAGetOverlappedResult(
        SOCKET s,
        LPWSAOVERLAPPED lpOverlapped,
        LPDWORD lpcbTransfer,
        BOOL fWait,
        LPDWORD lpdwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "lpOverlapped", "lpcbTransfer", "fWait", "lpdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAGetServiceClassInfo(jitter, get_str, set_str):
    """
    [SocketCode-INT] WSAGetServiceClassInfo(
        LPGUID lpProviderId,
        LPGUID lpServiceClassId,
        LPDWORD lpdwBufferLength,
        LPWSASERVICECLASSINFO lpServiceClassInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpProviderId", "lpServiceClassId", "lpdwBufferLength", "lpServiceClassInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAGetServiceClassInfoA(jitter):
    ws2_32_WSAGetServiceClassInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSAGetServiceClassInfoW(jitter):
    ws2_32_WSAGetServiceClassInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSAGetServiceClassNameByClassId(jitter, get_str, set_str):
    """
    [SocketCode-INT] WSAGetServiceClassNameByClassId(
        LPGUID lpServiceClassId,
        LPTSTR lpszServiceClassName,
        LPDWORD lpdwBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServiceClassId", "lpszServiceClassName", "lpdwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAGetServiceClassNameByClassIdA(jitter):
    ws2_32_WSAGetServiceClassNameByClassId(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSAGetServiceClassNameByClassIdW(jitter):
    ws2_32_WSAGetServiceClassNameByClassId(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSAHtonl(jitter):
    """
    [SocketCode-int] WSAHtonl(
        SOCKET s,
        u_long hostlong,
        u_long* lpnetlong
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "hostlong", "lpnetlong"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAHtons(jitter):
    """
    [SocketCode-int] WSAHtons(
        SOCKET s,
        u_short hostshort,
        u_short* lpnetshort
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "hostshort", "lpnetshort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAInstallServiceClass(jitter, get_str, set_str):
    """
    [SocketCode-INT] WSAInstallServiceClass(
        LPWSASERVICECLASSINFO lpServiceClassInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServiceClassInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAInstallServiceClassA(jitter):
    ws2_32_WSAInstallServiceClass(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSAInstallServiceClassW(jitter):
    ws2_32_WSAInstallServiceClass(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSAIoctl(jitter):
    """
    [SocketCode-int] WSAIoctl(
        SOCKET s,
        [WsaIoctl] dwIoControlCode,
        LPVOID lpvInBuffer,
        DWORD cbInBuffer,
        LPVOID lpvOutBuffer,
        DWORD cbOutBuffer,
        LPDWORD lpcbBytesReturned,
        LPWSAOVERLAPPED lpOverlapped,
        LPWSAOVERLAPPED_COMPLETION_ROUTINE lpCompletionRoutine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "dwIoControlCode", "lpvInBuffer", "cbInBuffer", "lpvOutBuffer", "cbOutBuffer", "lpcbBytesReturned", "lpOverlapped", "lpCompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAJoinLeaf(jitter):
    """
    SOCKET WSAJoinLeaf(
        SOCKET s,
        const struct sockaddr* name,
        int namelen,
        LPWSABUF lpCallerData,
        LPWSABUF lpCalleeData,
        LPQOS lpSQOS,
        LPQOS lpGQOS,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "name", "namelen", "lpCallerData", "lpCalleeData", "lpSQOS", "lpGQOS", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSALookupServiceBegin(jitter, get_str, set_str):
    """
    [SocketCode-INT] WSALookupServiceBegin(
        LPWSAQUERYSET lpqsRestrictions,
        [LookupServiceFlags] dwControlFlags,
        LPHANDLE lphLookup
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpqsRestrictions", "dwControlFlags", "lphLookup"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSALookupServiceBeginA(jitter):
    ws2_32_WSALookupServiceBegin(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSALookupServiceBeginW(jitter):
    ws2_32_WSALookupServiceBegin(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSALookupServiceEnd(jitter):
    """
    [SocketCode-INT] WSALookupServiceEnd(
        HANDLE hLookup
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLookup"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSALookupServiceNext(jitter, get_str, set_str):
    """
    [SocketCode-INT] WSALookupServiceNext(
        HANDLE hLookup,
        [LookupServiceFlags] dwControlFlags,
        LPDWORD lpdwBufferLength,
        LPWSAQUERYSET lpqsResults
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLookup", "dwControlFlags", "lpdwBufferLength", "lpqsResults"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSALookupServiceNextA(jitter):
    ws2_32_WSALookupServiceNext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSALookupServiceNextW(jitter):
    ws2_32_WSALookupServiceNext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSANtohl(jitter):
    """
    [SocketCode-int] WSANtohl(
        SOCKET s,
        u_long netlong,
        u_long* lphostlong
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "netlong", "lphostlong"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSANtohs(jitter):
    """
    [SocketCode-int] WSANtohs(
        SOCKET s,
        u_short netshort,
        u_short* lphostshort
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "netshort", "lphostshort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAPoll(jitter):
    """
    [SocketCode-int] WSAPoll(
        ULONG nfds,
        INT timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nfds", "timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAProviderConfigChange(jitter):
    """
    [SocketCode-int] WSAProviderConfigChange(
        LPHANDLE lpNotificationHandle,
        LPWSAOVERLAPPED lpOverlapped,
        LPWSAOVERLAPPED_COMPLETION_ROUTINE lpCompletionRoutine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpNotificationHandle", "lpOverlapped", "lpCompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSARecv(jitter):
    """
    [SocketCode-int] WSARecv(
        SOCKET s,
        [LPWSABUF_IN] lpBuffers,
        DWORD dwBufferCount,
        LPDWORD lpNumberOfBytesRecvd,
        [SendRecvFlags*] lpFlags,
        LPWSAOVERLAPPED lpOverlapped,
        LPWSAOVERLAPPED_COMPLETION_ROUTINE lpCompletionRoutine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "lpBuffers", "dwBufferCount", "lpNumberOfBytesRecvd", "lpFlags", "lpOverlapped", "lpCompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSARecvDisconnect(jitter):
    """
    [SocketCode-int] WSARecvDisconnect(
        SOCKET s,
        LPWSABUF lpInboundDisconnectData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "lpInboundDisconnectData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSARecvFrom(jitter):
    """
    [SocketCode-int] WSARecvFrom(
        SOCKET s,
        LPWSABUF lpBuffers,
        DWORD dwBufferCount,
        LPDWORD lpNumberOfBytesRecvd,
        LPDWORD lpFlags,
        struct sockaddr* lpFrom,
        LPINT lpFromlen,
        LPWSAOVERLAPPED lpOverlapped,
        LPWSAOVERLAPPED_COMPLETION_ROUTINE lpCompletionRoutine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "lpBuffers", "dwBufferCount", "lpNumberOfBytesRecvd", "lpFlags", "lpFrom", "lpFromlen", "lpOverlapped", "lpCompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSARemoveServiceClass(jitter):
    """
    [SocketCode-INT] WSARemoveServiceClass(
        LPGUID lpServiceClassId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServiceClassId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAResetEvent(jitter):
    """
    BOOL WSAResetEvent(
        WSAEVENT hEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSASend(jitter):
    """
    [SocketCode-int] WSASend(
        SOCKET s,
        LPWSABUF lpBuffers,
        DWORD dwBufferCount,
        LPDWORD lpNumberOfBytesSent,
        [SendRecvFlags] dwFlags,
        LPWSAOVERLAPPED lpOverlapped,
        LPWSAOVERLAPPED_COMPLETION_ROUTINE lpCompletionRoutine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "lpBuffers", "dwBufferCount", "lpNumberOfBytesSent", "dwFlags", "lpOverlapped", "lpCompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSASendDisconnect(jitter):
    """
    [SocketCode-int] WSASendDisconnect(
        SOCKET s,
        LPWSABUF lpOutboundDisconnectData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "lpOutboundDisconnectData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSASendMsg(jitter):
    """
    [SocketCode-int] WSASendMsg(
        SOCKET s,
        LPWSAMSG lpMsg,
        DWORD dwFlags,
        LPDWORD lpNumberOfBytesSent,
        LPWSAOVERLAPPED lpOverlapped,
        LPWSAOVERLAPPED_COMPLETION_ROUTINE lpCompletionRoutine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "lpMsg", "dwFlags", "lpNumberOfBytesSent", "lpOverlapped", "lpCompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSASendTo(jitter):
    """
    [SocketCode-int] WSASendTo(
        SOCKET s,
        LPWSABUF lpBuffers,
        DWORD dwBufferCount,
        LPDWORD lpNumberOfBytesSent,
        [SendRecvFlags] dwFlags,
        const struct sockaddr* lpTo,
        int iToLen,
        LPWSAOVERLAPPED lpOverlapped,
        LPWSAOVERLAPPED_COMPLETION_ROUTINE lpCompletionRoutine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "lpBuffers", "dwBufferCount", "lpNumberOfBytesSent", "dwFlags", "lpTo", "iToLen", "lpOverlapped", "lpCompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSASetEvent(jitter):
    """
    BOOL WSASetEvent(
        WSAEVENT hEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSASetLastError(jitter):
    """
    void WSASetLastError(
        [WSA_ERROR] iError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["iError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSASetService(jitter, get_str, set_str):
    """
    [SocketCode-INT] WSASetService(
        LPWSAQUERYSET lpqsRegInfo,
        WSAESETSERVICEOP essOperation,
        DWORD dwControlFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpqsRegInfo", "essOperation", "dwControlFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSASetServiceA(jitter):
    ws2_32_WSASetService(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSASetServiceW(jitter):
    ws2_32_WSASetService(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSASocket(jitter, get_str, set_str):
    """
    SOCKET WSASocket(
        [AddressFamily] af,
        [SocketType] type,
        [SocketProtocol] protocol,
        LPWSAPROTOCOL_INFO lpProtocolInfo,
        GROUP g,
        [WsaFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["af", "type", "protocol", "lpProtocolInfo", "g", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSASocketA(jitter):
    ws2_32_WSASocket(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSASocketW(jitter):
    ws2_32_WSASocket(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSAStartup(jitter):
    """
    [WSA_ERROR] WSAStartup(
        WORD wVersionRequested,
        LPWSADATA lpWSAData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wVersionRequested", "lpWSAData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAStringToAddress(jitter, get_str, set_str):
    """
    [SocketCode-INT] WSAStringToAddress(
        LPTSTR AddressString,
        [AddressFamily] AddressFamily,
        LPWSAPROTOCOL_INFO lpProtocolInfo,
        LPSOCKADDR lpAddress,
        LPINT lpAddressLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AddressString", "AddressFamily", "lpProtocolInfo", "lpAddress", "lpAddressLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAStringToAddressA(jitter):
    ws2_32_WSAStringToAddress(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ws2_32_WSAStringToAddressW(jitter):
    ws2_32_WSAStringToAddress(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ws2_32_WSAWaitForMultipleEvents(jitter):
    """
    DWORD WSAWaitForMultipleEvents(
        DWORD cEvents,
        const WSAEVENT* lphEvents,
        BOOL fWaitAll,
        DWORD dwTimeout,
        BOOL fAlertable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cEvents", "lphEvents", "fWaitAll", "dwTimeout", "fAlertable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAIsBlocking(jitter):
    """
    BOOL WSAIsBlocking()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_GetAddrInfoExCancel(jitter):
    """
    [WSA_ERROR] GetAddrInfoExCancel(
        LPHANDLE lpHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_GetAddrInfoExOverlappedResult(jitter):
    """
    [WSA_ERROR] GetAddrInfoExOverlappedResult(
        LPOVERLAPPED lpOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ws2_32_WSAGetQOSByName(jitter):
    """
    BOOL WSAGetQOSByName(
        SOCKET s,
        LPWSABUF lpQOSName,
        LPQOS lpQOS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "lpQOSName", "lpQOS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
