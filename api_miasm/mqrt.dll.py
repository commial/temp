
def mqrt_MQADsPathToFormatName(jitter):
    """
    HRESULT MQADsPathToFormatName(
        LPCWSTR lpwcsADsPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwcsADsPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQBeginTransaction(jitter):
    """
    HRESULT MQBeginTransaction(
        ITransaction** ppTransaction
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQCloseCursor(jitter):
    """
    HRESULT MQCloseCursor(
        HANDLE hCursor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCursor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQCloseQueue(jitter):
    """
    HRESULT MQCloseQueue(
        QUEUEHANDLE hQueue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hQueue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQCreateCursor(jitter):
    """
    HRESULT MQCreateCursor(
        QUEUEHANDLE hQueue,
        PHANDLE phCursor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hQueue", "phCursor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQCreateQueue(jitter):
    """
    HRESULT MQCreateQueue(
        PSECURITY_DESCRIPTOR pSecurityDescriptor,
        MQQUEUEPROPS* pQueueProps,
        LPWSTR lpwcsFormatName,
        LPDWORD lpdwFormatNameLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "pQueueProps", "lpwcsFormatName", "lpdwFormatNameLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQDeleteQueue(jitter):
    """
    HRESULT MQDeleteQueue(
        LPCWSTR lpwcsFormatName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwcsFormatName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQFreeMemory(jitter):
    """
    VOID MQFreeMemory(
        PVOID pvMemory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMemory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQFreeSecurityContext(jitter):
    """
    VOID MQFreeSecurityContext(
        HANDLE hSecurityContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSecurityContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetMachineProperties(jitter):
    """
    HRESULT MQGetMachineProperties(
        LPCWSTR lpwcsMachineName,
        const GUID* pguidMachineID,
        MQQMPROPS* pQMProps
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwcsMachineName", "pguidMachineID", "pQMProps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetOverlappedResult(jitter):
    """
    HRESULT MQGetOverlappedResult(
        LPOVERLAPPED lpOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetPrivateComputerInformation(jitter):
    """
    HRESULT MQGetPrivateComputerInformation(
        LPCWSTR lpwcsComputerName,
        MQPRIVATEPROPS* pPrivateProps
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwcsComputerName", "pPrivateProps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetQueueProperties(jitter):
    """
    HRESULT MQGetQueueProperties(
        LPCWSTR lpwcsFormatName,
        MQQUEUEPROPS* pQueueProps
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwcsFormatName", "pQueueProps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetQueueSecurity(jitter):
    """
    HRESULT MQGetQueueSecurity(
        LPCWSTR lpwcsFormatName,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR pSecurityDescriptor,
        DWORD nLength,
        LPDWORD lpnLengthNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwcsFormatName", "SecurityInformation", "pSecurityDescriptor", "nLength", "lpnLengthNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetSecurityContext(jitter):
    """
    HRESULT MQGetSecurityContext(
        LPVOID lpCertBuffer,
        DWORD dwCertBufferLength,
        HANDLE* phSecurityContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpCertBuffer", "dwCertBufferLength", "phSecurityContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetSecurityContextEx(jitter):
    """
    HRESULT MQGetSecurityContextEx(
        LPVOID lpCertBuffer,
        DWORD dwCertBufferLength,
        HANDLE* phSecurityContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpCertBuffer", "dwCertBufferLength", "phSecurityContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQHandleToFormatName(jitter):
    """
    HRESULT MQHandleToFormatName(
        QUEUEHANDLE hQueue,
        LPWSTR lpwcsFormatName,
        LPDWORD lpdwCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hQueue", "lpwcsFormatName", "lpdwCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQInstanceToFormatName(jitter):
    """
    HRESULT MQInstanceToFormatName(
        GUID* pGUID,
        LPWSTR lpwcsFormatName,
        LPDWORD lpdwCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pGUID", "lpwcsFormatName", "lpdwCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQLocateBegin(jitter):
    """
    HRESULT MQLocateBegin(
        LPCWSTR lpwcsContext,
        MQRESTRICTION* pRestriction,
        MQCOLUMNSET* pColumns,
        MQSORTSET* pSort,
        PHANDLE phEnum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwcsContext", "pRestriction", "pColumns", "pSort", "phEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQLocateEnd(jitter):
    """
    HRESULT MQLocateEnd(
        HANDLE hEnum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQLocateNext(jitter):
    """
    HRESULT MQLocateNext(
        HANDLE hEnum,
        DWORD* pcProps,
        MQPROPVARIANT[] aPropVar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEnum", "pcProps", "aPropVar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQMarkMessageRejected(jitter):
    """
    HRESULT MQMarkMessageRejected(
        QUEUEHANDLE hQueue,
        ULONGLONG ullLookupId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hQueue", "ullLookupId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQMgmtAction(jitter):
    """
    HRESULT MQMgmtAction(
        LPCWSTR pMachineName,
        LPCWSTR pObjectName,
        LPCWSTR pAction
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "pObjectName", "pAction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQMgmtGetInfo(jitter):
    """
    HRESULT MQMgmtGetInfo(
        LPCWSTR pMachineName,
        LPCWSTR pObjectName,
        MQMGMTPROPS* pMgmtProps
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "pObjectName", "pMgmtProps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQMoveMessage(jitter):
    """
    HRESULT MQMoveMessage(
        QUEUEHANDLE sourceQueue,
        QUEUEHANDLE targetQueue,
        ULONGLONG lookupID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sourceQueue", "targetQueue", "lookupID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQOpenQueue(jitter):
    """
    HRESULT MQOpenQueue(
        LPCWSTR lpwcsFormatName,
        DWORD dwAccess,
        DWORD dwShareMode,
        QUEUEHANDLE* phQueue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwcsFormatName", "dwAccess", "dwShareMode", "phQueue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQPathNameToFormatName(jitter):
    """
    HRESULT MQPathNameToFormatName(
        LPCWSTR lpwcsPathName,
        LPWSTR lpwcsFormatName,
        LPDWORD lpdwCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwcsPathName", "lpwcsFormatName", "lpdwCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQPurgeQueue(jitter):
    """
    HRESULT MQPurgeQueue(
        HANDLE hQueue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hQueue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQReceiveMessage(jitter):
    """
    HRESULT MQReceiveMessage(
        QUEUEHANDLE hSource,
        DWORD dwTimeout,
        DWORD dwAction,
        MQMSGPROPS* pMessageProps,
        LPOVERLAPPED lpOverlapped,
        PMQRECEIVECALLBACK fnReceiveCallback,
        HANDLE hCursor,
        ITransaction* pTransaction
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSource", "dwTimeout", "dwAction", "pMessageProps", "lpOverlapped", "fnReceiveCallback", "hCursor", "pTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQReceiveMessageByLookupId(jitter):
    """
    HRESULT MQReceiveMessageByLookupId(
        QUEUEHANDLE hSource,
        ULONGLONG ullLookupId,
        DWORD dwLookupAction,
        MQMSGPROPS* pMessageProps,
        LPOVERLAPPED lpOverlapped,
        PMQRECEIVECALLBACK fnReceiveCallback,
        ITransaction* pTransaction
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSource", "ullLookupId", "dwLookupAction", "pMessageProps", "lpOverlapped", "fnReceiveCallback", "pTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQRegisterCertificate(jitter):
    """
    HRESULT MQRegisterCertificate(
        DWORD dwFlags,
        PVOID lpCertBuffer,
        DWORD dwCertBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpCertBuffer", "dwCertBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQSendMessage(jitter):
    """
    HRESULT MQSendMessage(
        QUEUEHANDLE hDestinationQueue,
        MQMSGPROPS* pMessageProps,
        ITransaction* pTransaction
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDestinationQueue", "pMessageProps", "pTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQSetQueueProperties(jitter):
    """
    HRESULT MQSetQueueProperties(
        LPCWSTR lpwcsFormatName,
        MQQUEUEPROPS* pQueueProps
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwcsFormatName", "pQueueProps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQSetQueueSecurity(jitter):
    """
    HRESULT MQSetQueueSecurity(
        LPCWSTR lpwcsFormatName,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR pSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwcsFormatName", "SecurityInformation", "pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
