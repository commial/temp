
def peerdist_PeerDistStartup(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistStartup(DWORD dwVersionRequested, PPEERDIST_INSTANCE_HANDLE phPeerDist, PDWORD pdwSupportedVersion)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwVersionRequested", "phPeerDist", "pdwSupportedVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistShutdown(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistShutdown(PEERDIST_INSTANCE_HANDLE hPeerDist)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistGetStatus(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistGetStatus(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_STATUS* pPeerDistStatus)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "pPeerDistStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistGetStatusEx(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistGetStatusEx(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_STATUS_INFO* pPeerDistStatusInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "pPeerDistStatusInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistGetOverlappedResult(jitter):
    """
    [PeerDist.dll] BOOL PeerDistGetOverlappedResult(LPOVERLAPPED lpOverlapped, LPDWORD lpNumberOfBytesTransferred, BOOL bWait)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpOverlapped", "lpNumberOfBytesTransferred", "bWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistRegisterForStatusChangeNotification(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistRegisterForStatusChangeNotification(PEERDIST_INSTANCE_HANDLE hPeerDist, HANDLE hCompletionPort, ULONG_PTR ulCompletionKey, LPOVERLAPPED lpOverlapped, PEERDIST_STATUS* pPeerDistStatus)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hCompletionPort", "ulCompletionKey", "lpOverlapped", "pPeerDistStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistRegisterForStatusChangeNotificationEx(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistRegisterForStatusChangeNotificationEx(PEERDIST_INSTANCE_HANDLE hPeerDist, HANDLE hCompletionPort, ULONG_PTR ulCompletionKey, LPOVERLAPPED lpOverlapped, PEERDIST_STATUS_INFO* pPeerDistStatus)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hCompletionPort", "ulCompletionKey", "lpOverlapped", "pPeerDistStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistUnregisterForStatusChangeNotification(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistUnregisterForStatusChangeNotification(PEERDIST_INSTANCE_HANDLE hPeerDist)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistClientOpenContent(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistClientOpenContent(PEERDIST_INSTANCE_HANDLE hPeerDist, PCPEERDIST_CONTENT_TAG pContentTag, HANDLE hCompletionPort, ULONG_PTR ulCompletionKey, PPEERDIST_CONTENT_HANDLE phContentHandle)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "pContentTag", "hCompletionPort", "ulCompletionKey", "phContentHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistClientCloseContent(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistClientCloseContent(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_CONTENT_HANDLE hContentHandle)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hContentHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistClientGetInformationByHandle(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistClientGetInformationByHandle(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_CONTENT_HANDLE hContentHandle, PEERDIST_CLIENT_INFO_BY_HANDLE_CLASS PeerDistClientInfoClass, DWORD dwBufferSize, LPVOID lpInformation)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hContentHandle", "PeerDistClientInfoClass", "dwBufferSize", "lpInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistClientAddContentInformation(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistClientAddContentInformation(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_CONTENT_HANDLE hContentHandle, DWORD cbNumberOfBytes, PBYTE pBuffer, LPOVERLAPPED lpOverlapped)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hContentHandle", "cbNumberOfBytes", "pBuffer", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistClientCompleteContentInformation(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistClientCompleteContentInformation(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_CONTENT_HANDLE hContentHandle, LPOVERLAPPED lpOverlapped)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hContentHandle", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistClientAddData(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistClientAddData(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_CONTENT_HANDLE hContentHandle, DWORD cbNumberOfBytes, PBYTE pBuffer, LPOVERLAPPED lpOverlapped)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hContentHandle", "cbNumberOfBytes", "pBuffer", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistClientBlockRead(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistClientBlockRead(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_CONTENT_HANDLE hContentHandle, DWORD cbMaxNumberOfBytesToRead, PBYTE pBuffer, DWORD dwTimeoutInMilliseconds, LPOVERLAPPED lpOverlapped)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hContentHandle", "cbMaxNumberOfBytesToRead", "pBuffer", "dwTimeoutInMilliseconds", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistClientStreamRead(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistClientStreamRead(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_CONTENT_HANDLE hContentHandle, DWORD cbMaxNumberOfBytesToRead, PBYTE pBuffer, DWORD dwTimeoutInMilliseconds, LPOVERLAPPED lpOverlapped)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hContentHandle", "cbMaxNumberOfBytesToRead", "pBuffer", "dwTimeoutInMilliseconds", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistClientFlushContent(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistClientFlushContent(PEERDIST_INSTANCE_HANDLE hPeerDist, PCPEERDIST_CONTENT_TAG pContentTag, HANDLE hCompletionPort, ULONG_PTR ulCompletionKey, LPOVERLAPPED lpOverlapped)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "pContentTag", "hCompletionPort", "ulCompletionKey", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistClientCancelAsyncOperation(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistClientCancelAsyncOperation(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_CONTENT_HANDLE hContentHandle, LPOVERLAPPED pOverlapped)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hContentHandle", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistServerPublishStream(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistServerPublishStream(PEERDIST_INSTANCE_HANDLE hPeerDist, DWORD cbContentIdentifier, PBYTE pContentIdentifier, ULONGULONG cbContentLength, PCPEERDIST_PUBLICATION_OPTIONS pPublishOptions, HANDLE hCompletionPort, ULONG_PTR ulCompletionKey, PEERDIST_STREAM_HANDLE phStream)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "cbContentIdentifier", "pContentIdentifier", "cbContentLength", "pPublishOptions", "hCompletionPort", "ulCompletionKey", "phStream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistServerPublishAddToStream(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistServerPublishAddToStream(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_STREAM_HANDLE hStream, DWORD cbNumberOfBytes, PBYTE pBuffer, LPOVERLAPPED lpOverlapped)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hStream", "cbNumberOfBytes", "pBuffer", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistServerPublishCompleteStream(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistServerPublishCompleteStream(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_STREAM_HANDLE hStream, LPOVERLAPPED lpOverlapped)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hStream", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistServerCloseStreamHandle(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistServerCloseStreamHandle(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_STREAM_HANDLE hStream)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hStream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistServerUnpublish(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistServerUnpublish(PEERDIST_INSTANCE_HANDLE hPeerDist, DWORD cbContentIdentifier, PBYTE pContentIdentifier)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "cbContentIdentifier", "pContentIdentifier"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistServerOpenContentInformation(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistServerOpenContentInformation(PEERDIST_INSTANCE_HANDLE hPeerDist, DWORD cbContentIdentifier, PBYTE pContentIdentifier, ULONGULONG ullContentOffset, ULONGULONG cbContentLength, HANDLE hCompletionPort, ULONG_PTR ulCompletionKey, PPEERDIST_CONTENTINFO_HANDLE phContentInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "cbContentIdentifier", "pContentIdentifier", "ullContentOffset", "cbContentLength", "hCompletionPort", "ulCompletionKey", "phContentInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistServerOpenContentInformationEx(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistServerOpenContentInformationEx(PEERDIST_INSTANCE_HANDLE hPeerDist, DWORD cbContentIdentifier, PBYTE pContentIdentifier, ULONGLONG ullContentOffset, ULONGLONG cbContentLength, PEERDIST_RETRIEVAL_OPTIONS* pRetrievalOptions, HANDLE hCompletionPort, ULONG_PTR ulCompletionKey, PPEERDIST_CONTENTINFO_HANDLE phContentInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "cbContentIdentifier", "pContentIdentifier", "ullContentOffset", "cbContentLength", "pRetrievalOptions", "hCompletionPort", "ulCompletionKey", "phContentInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistServerRetrieveContentInformation(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistServerRetrieveContentInformation(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_CONTENTINFO_HANDLE hContentInfo, DWORD cbMaxNumberOfBytes, PBYTE pBuffer, LPOVERLAPPED lpOverlapped)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hContentInfo", "cbMaxNumberOfBytes", "pBuffer", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistServerCloseContentInformation(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistServerCloseContentInformation(PEERDIST_INSTANCE_HANDLE hPeerDist, PEERDIST_CONTENT_HANDLE hContentInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "hContentInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def peerdist_PeerDistServerCancelAsyncOperation(jitter):
    """
    [PeerDist.dll] [ERROR_CODE] PeerDistServerCancelAsyncOperation(PEERDIST_INSTANCE_HANDLE hPeerDist, DWORD cbContentIdentifier, PBYTE pContentIdentifier, LPOVERLAPPED pOverlapped)
    """
    ret_ad, args = jitter.func_args_stdcall(["hPeerDist", "cbContentIdentifier", "pContentIdentifier", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
