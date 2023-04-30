
def mswsock_EnumProtocols(jitter):
    """"
    [Mswsock.dll] [SocketCode-INT] EnumProtocols(LPINT lpiProtocols, LPVOID lpProtocolBuffer, LPDWORD lpdwBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpiProtocols", "lpProtocolBuffer", "lpdwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_GetAcceptExSockaddrs(jitter):
    """"
    [Mswsock.dll] void GetAcceptExSockaddrs(PVOID lpOutputBuffer, DWORD dwReceiveDataLength, DWORD dwLocalAddressLength, DWORD dwRemoteAddressLength, LPSOCKADDR* LocalSockaddr, LPINT LocalSockaddrLength, LPSOCKADDR* RemoteSockaddr, LPINT RemoteSockaddrLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpOutputBuffer", "dwReceiveDataLength", "dwLocalAddressLength", "dwRemoteAddressLength", "LocalSockaddr", "LocalSockaddrLength", "RemoteSockaddr", "RemoteSockaddrLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_AcceptEx(jitter):
    """"
    [Mswsock.dll] BOOL AcceptEx(SOCKET sListenSocket, SOCKET sAcceptSocket, PVOID lpOutputBuffer, DWORD dwReceiveDataLength, DWORD dwLocalAddressLength, DWORD dwRemoteAddressLength, LPDWORD lpdwBytesReceived, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sListenSocket", "sAcceptSocket", "lpOutputBuffer", "dwReceiveDataLength", "dwLocalAddressLength", "dwRemoteAddressLength", "lpdwBytesReceived", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_GetAddressByName(jitter):
    """"
    [Mswsock.dll] INT GetAddressByName([NameSpaceFlags] dwNameSpace, LPGUID lpServiceType, LPTSTR lpServiceName, LPINT lpiProtocols, [ResolutionFlags] dwResolution, LPSERVICE_ASYNC_INFO lpServiceAsyncInfo, LPVOID lpCsaddrBuffer, LPDWORD lpdwBufferLength, LPTSTR lpAliasBuffer, LPDWORD lpdwAliasBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwNameSpace", "lpServiceType", "lpServiceName", "lpiProtocols", "dwResolution", "lpServiceAsyncInfo", "lpCsaddrBuffer", "lpdwBufferLength", "lpAliasBuffer", "lpdwAliasBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_GetNameByType(jitter):
    """"
    [Mswsock.dll] [SocketCode-INT] GetNameByType(LPGUID lpServiceType, LPTSTR lpServiceName, DWORD dwNameLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpServiceType", "lpServiceName", "dwNameLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_GetService(jitter):
    """"
    [Mswsock.dll] [SocketCode-INT] GetService([NameSpaceFlags] dwNameSpace, PGUID lpGuid, LPTSTR lpServiceName, [GetService_Props] dwProperties, LPVOID lpBuffer, LPDWORD lpdwBufferSize, LPSERVICE_ASYNC_INFO lpServiceAsyncInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwNameSpace", "lpGuid", "lpServiceName", "dwProperties", "lpBuffer", "lpdwBufferSize", "lpServiceAsyncInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_GetTypeByName(jitter):
    """"
    [Mswsock.dll] [SocketCode-INT] GetTypeByName(LPTSTR lpServiceName, PGUID lpServiceType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpServiceName", "lpServiceType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_SetService(jitter):
    """"
    [Mswsock.dll] [SocketCode-INT] SetService([NameSpaceFlags] dwNameSpace, [SetService_Operation] dwOperation, [SetService_Flags] dwFlags, LPSERVICE_INFO lpServiceInfo, LPSERVICE_ASYNC_INFO lpServiceAsyncInfo, [SetService_FlagsOut*] lpdwStatusFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwNameSpace", "dwOperation", "dwFlags", "lpServiceInfo", "lpServiceAsyncInfo", "lpdwStatusFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_TransmitFile(jitter):
    """"
    [Mswsock.dll] BOOL TransmitFile(SOCKET hSocket, HANDLE hFile, DWORD nNumberOfBytesToWrite, DWORD nNumberOfBytesPerSend, LPOVERLAPPED lpOverlapped, LPTRANSMIT_FILE_BUFFERS lpTransmitBuffers, [TransmitFile_Flags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSocket", "hFile", "nNumberOfBytesToWrite", "nNumberOfBytesPerSend", "lpOverlapped", "lpTransmitBuffers", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_WSARecvEx(jitter):
    """"
    [Mswsock.dll] [SocketCode-int] WSARecvEx(SOCKET s, char* buf, int len, int* flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["s", "buf", "len", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOCloseCompletionQueue(jitter):
    """"
    [Mswsock.dll] VOID RIOCloseCompletionQueue(RIO_CQ CQ)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CQ"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOCreateCompletionQueue(jitter):
    """"
    [Mswsock.dll] RIO_CQ RIOCreateCompletionQueue(DWORD QueueSize, RIO_NOTIFICATION_COMPLETION* NotificationCompletion)
    """"
    ret_ad, args = jitter.func_args_stdcall(["QueueSize", "NotificationCompletion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOCreateRequestQueue(jitter):
    """"
    [Mswsock.dll] RIO_RQ RIOCreateRequestQueue(SOCKET Socket, ULONG MaxOutstandingReceive, ULONG MaxReceiveDataBuffers, ULONG MaxOutstandingSend, ULONG MaxSendDataBuffers, RIO_CQ ReceiveCQ, RIO_CQ SendCQ, PVOID SocketContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Socket", "MaxOutstandingReceive", "MaxReceiveDataBuffers", "MaxOutstandingSend", "MaxSendDataBuffers", "ReceiveCQ", "SendCQ", "SocketContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIODequeueCompletion(jitter):
    """"
    [Mswsock.dll] ULONG RIODequeueCompletion(RIO_CQ CQ, PRIORESULT Array, ULONG ArraySize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CQ", "Array", "ArraySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIODeregisterBuffer(jitter):
    """"
    [Mswsock.dll] VOID RIODeregisterBuffer(RIO_BUFFERID BufferId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BufferId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIONotify(jitter):
    """"
    [Mswsock.dll] [ERROR_CODE] RIONotify(RIO_CQ CQ)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CQ"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOReceive(jitter):
    """"
    [Mswsock.dll] BOOL RIOReceive(RIO_RQ SocketQueue, PRIO_BUF pData, ULONG DataBufferCount, DWORD Flags, PVOID RequestContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SocketQueue", "pData", "DataBufferCount", "Flags", "RequestContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOReceiveEx(jitter):
    """"
    [Mswsock.dll] BOOL RIOReceiveEx(RIO_RQ SocketQueue, PRIO_BUF pData, ULONG DataBufferCount, PRIO_BUF pLocalAddress, PRIO_BUF pRemoteAddress, PRIO_BUF pControlContext, PRIO_BUF pFlags, DWORD Flags, PVOID RequestContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SocketQueue", "pData", "DataBufferCount", "pLocalAddress", "pRemoteAddress", "pControlContext", "pFlags", "Flags", "RequestContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIORegisterBuffer(jitter):
    """"
    [Mswsock.dll] RIO_BUFFERID RIORegisterBuffer(LPVOID DataBuffer, DWORD DataLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DataBuffer", "DataLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOResizeCompletionQueue(jitter):
    """"
    [Mswsock.dll] BOOL RIOResizeCompletionQueue(RIO_CQ CQ, DWORD QueueSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CQ", "QueueSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOResizeRequestQueue(jitter):
    """"
    [Mswsock.dll] BOOL RIOResizeRequestQueue(RIO_RQ RQ, DWORD MaxOutstandingReceive, DWORD MaxOutstandingSend)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RQ", "MaxOutstandingReceive", "MaxOutstandingSend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOSend(jitter):
    """"
    [Mswsock.dll] BOOL RIOSend(RIO_RQ SocketQueue, PRIO_BUF pData, ULONG DataBufferCount, DWORD Flags, PVOID RequestContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SocketQueue", "pData", "DataBufferCount", "Flags", "RequestContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mswsock_RIOSendEx(jitter):
    """"
    [Mswsock.dll] BOOL RIOSendEx(RIO_RQ SocketQueue, PRIO_BUF pData, ULONG DataBufferCount, PRIO_BUF pLocalAddress, PRIO_BUF pRemoteAddress, PRIO_BUF pControlContext, PRIO_BUF pFlags, DWORD Flags, PVOID RequestContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SocketQueue", "pData", "DataBufferCount", "pLocalAddress", "pRemoteAddress", "pControlContext", "pFlags", "Flags", "RequestContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)