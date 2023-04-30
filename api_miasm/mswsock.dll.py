
def mswsock_EnumProtocols(jitter, get_str, set_str):
    """
    [SocketCode-INT] EnumProtocols(
        LPINT lpiProtocols,
        LPVOID lpProtocolBuffer,
        LPDWORD lpdwBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpiProtocols", "lpProtocolBuffer", "lpdwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_EnumProtocolsA(jitter):
    mswsock_EnumProtocols(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mswsock_EnumProtocolsW(jitter):
    mswsock_EnumProtocols(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mswsock_GetAcceptExSockaddrs(jitter):
    """
    void GetAcceptExSockaddrs(
        PVOID lpOutputBuffer,
        DWORD dwReceiveDataLength,
        DWORD dwLocalAddressLength,
        DWORD dwRemoteAddressLength,
        LPSOCKADDR* LocalSockaddr,
        LPINT LocalSockaddrLength,
        LPSOCKADDR* RemoteSockaddr,
        LPINT RemoteSockaddrLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpOutputBuffer", "dwReceiveDataLength", "dwLocalAddressLength", "dwRemoteAddressLength", "LocalSockaddr", "LocalSockaddrLength", "RemoteSockaddr", "RemoteSockaddrLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_AcceptEx(jitter):
    """
    BOOL AcceptEx(
        SOCKET sListenSocket,
        SOCKET sAcceptSocket,
        PVOID lpOutputBuffer,
        DWORD dwReceiveDataLength,
        DWORD dwLocalAddressLength,
        DWORD dwRemoteAddressLength,
        LPDWORD lpdwBytesReceived,
        LPOVERLAPPED lpOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sListenSocket", "sAcceptSocket", "lpOutputBuffer", "dwReceiveDataLength", "dwLocalAddressLength", "dwRemoteAddressLength", "lpdwBytesReceived", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_GetAddressByName(jitter, get_str, set_str):
    """
    INT GetAddressByName(
        [NameSpaceFlags] dwNameSpace,
        LPGUID lpServiceType,
        LPTSTR lpServiceName,
        LPINT lpiProtocols,
        [ResolutionFlags] dwResolution,
        LPSERVICE_ASYNC_INFO lpServiceAsyncInfo,
        LPVOID lpCsaddrBuffer,
        LPDWORD lpdwBufferLength,
        LPTSTR lpAliasBuffer,
        LPDWORD lpdwAliasBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwNameSpace", "lpServiceType", "lpServiceName", "lpiProtocols", "dwResolution", "lpServiceAsyncInfo", "lpCsaddrBuffer", "lpdwBufferLength", "lpAliasBuffer", "lpdwAliasBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_GetAddressByNameA(jitter):
    mswsock_GetAddressByName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mswsock_GetAddressByNameW(jitter):
    mswsock_GetAddressByName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mswsock_GetNameByType(jitter, get_str, set_str):
    """
    [SocketCode-INT] GetNameByType(
        LPGUID lpServiceType,
        LPTSTR lpServiceName,
        DWORD dwNameLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServiceType", "lpServiceName", "dwNameLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_GetNameByTypeA(jitter):
    mswsock_GetNameByType(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mswsock_GetNameByTypeW(jitter):
    mswsock_GetNameByType(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mswsock_GetService(jitter, get_str, set_str):
    """
    [SocketCode-INT] GetService(
        [NameSpaceFlags] dwNameSpace,
        PGUID lpGuid,
        LPTSTR lpServiceName,
        [GetService_Props] dwProperties,
        LPVOID lpBuffer,
        LPDWORD lpdwBufferSize,
        LPSERVICE_ASYNC_INFO lpServiceAsyncInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwNameSpace", "lpGuid", "lpServiceName", "dwProperties", "lpBuffer", "lpdwBufferSize", "lpServiceAsyncInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_GetServiceA(jitter):
    mswsock_GetService(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mswsock_GetServiceW(jitter):
    mswsock_GetService(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mswsock_GetTypeByName(jitter, get_str, set_str):
    """
    [SocketCode-INT] GetTypeByName(
        LPTSTR lpServiceName,
        PGUID lpServiceType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServiceName", "lpServiceType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_GetTypeByNameA(jitter):
    mswsock_GetTypeByName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mswsock_GetTypeByNameW(jitter):
    mswsock_GetTypeByName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mswsock_SetService(jitter, get_str, set_str):
    """
    [SocketCode-INT] SetService(
        [NameSpaceFlags] dwNameSpace,
        [SetService_Operation] dwOperation,
        [SetService_Flags] dwFlags,
        LPSERVICE_INFO lpServiceInfo,
        LPSERVICE_ASYNC_INFO lpServiceAsyncInfo,
        [SetService_FlagsOut*] lpdwStatusFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwNameSpace", "dwOperation", "dwFlags", "lpServiceInfo", "lpServiceAsyncInfo", "lpdwStatusFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_SetServiceA(jitter):
    mswsock_SetService(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mswsock_SetServiceW(jitter):
    mswsock_SetService(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mswsock_TransmitFile(jitter):
    """
    BOOL TransmitFile(
        SOCKET hSocket,
        HANDLE hFile,
        DWORD nNumberOfBytesToWrite,
        DWORD nNumberOfBytesPerSend,
        LPOVERLAPPED lpOverlapped,
        LPTRANSMIT_FILE_BUFFERS lpTransmitBuffers,
        [TransmitFile_Flags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSocket", "hFile", "nNumberOfBytesToWrite", "nNumberOfBytesPerSend", "lpOverlapped", "lpTransmitBuffers", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_WSARecvEx(jitter):
    """
    [SocketCode-int] WSARecvEx(
        SOCKET s,
        char* buf,
        int len,
        int* flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "buf", "len", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOCloseCompletionQueue(jitter):
    """
    VOID RIOCloseCompletionQueue(
        RIO_CQ CQ
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CQ"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOCreateCompletionQueue(jitter):
    """
    RIO_CQ RIOCreateCompletionQueue(
        DWORD QueueSize,
        RIO_NOTIFICATION_COMPLETION* NotificationCompletion
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["QueueSize", "NotificationCompletion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOCreateRequestQueue(jitter):
    """
    RIO_RQ RIOCreateRequestQueue(
        SOCKET Socket,
        ULONG MaxOutstandingReceive,
        ULONG MaxReceiveDataBuffers,
        ULONG MaxOutstandingSend,
        ULONG MaxSendDataBuffers,
        RIO_CQ ReceiveCQ,
        RIO_CQ SendCQ,
        PVOID SocketContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Socket", "MaxOutstandingReceive", "MaxReceiveDataBuffers", "MaxOutstandingSend", "MaxSendDataBuffers", "ReceiveCQ", "SendCQ", "SocketContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIODequeueCompletion(jitter):
    """
    ULONG RIODequeueCompletion(
        RIO_CQ CQ,
        PRIORESULT Array,
        ULONG ArraySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CQ", "Array", "ArraySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIODeregisterBuffer(jitter):
    """
    VOID RIODeregisterBuffer(
        RIO_BUFFERID BufferId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIONotify(jitter):
    """
    [ERROR_CODE] RIONotify(
        RIO_CQ CQ
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CQ"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOReceive(jitter):
    """
    BOOL RIOReceive(
        RIO_RQ SocketQueue,
        PRIO_BUF pData,
        ULONG DataBufferCount,
        DWORD Flags,
        PVOID RequestContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SocketQueue", "pData", "DataBufferCount", "Flags", "RequestContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOReceiveEx(jitter):
    """
    BOOL RIOReceiveEx(
        RIO_RQ SocketQueue,
        PRIO_BUF pData,
        ULONG DataBufferCount,
        PRIO_BUF pLocalAddress,
        PRIO_BUF pRemoteAddress,
        PRIO_BUF pControlContext,
        PRIO_BUF pFlags,
        DWORD Flags,
        PVOID RequestContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SocketQueue", "pData", "DataBufferCount", "pLocalAddress", "pRemoteAddress", "pControlContext", "pFlags", "Flags", "RequestContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIORegisterBuffer(jitter):
    """
    RIO_BUFFERID RIORegisterBuffer(
        LPVOID DataBuffer,
        DWORD DataLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DataBuffer", "DataLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOResizeCompletionQueue(jitter):
    """
    BOOL RIOResizeCompletionQueue(
        RIO_CQ CQ,
        DWORD QueueSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CQ", "QueueSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOResizeRequestQueue(jitter):
    """
    BOOL RIOResizeRequestQueue(
        RIO_RQ RQ,
        DWORD MaxOutstandingReceive,
        DWORD MaxOutstandingSend
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RQ", "MaxOutstandingReceive", "MaxOutstandingSend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOSend(jitter):
    """
    BOOL RIOSend(
        RIO_RQ SocketQueue,
        PRIO_BUF pData,
        ULONG DataBufferCount,
        DWORD Flags,
        PVOID RequestContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SocketQueue", "pData", "DataBufferCount", "Flags", "RequestContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOSendEx(jitter):
    """
    BOOL RIOSendEx(
        RIO_RQ SocketQueue,
        PRIO_BUF pData,
        ULONG DataBufferCount,
        PRIO_BUF pLocalAddress,
        PRIO_BUF pRemoteAddress,
        PRIO_BUF pControlContext,
        PRIO_BUF pFlags,
        DWORD Flags,
        PVOID RequestContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SocketQueue", "pData", "DataBufferCount", "pLocalAddress", "pRemoteAddress", "pControlContext", "pFlags", "Flags", "RequestContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
