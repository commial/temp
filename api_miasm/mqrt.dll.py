
def mqrt_MQADsPathToFormatName(jitter):
    """"
    [Mqrt.dll] HRESULT MQADsPathToFormatName(LPCWSTR lpwcsADsPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwcsADsPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQBeginTransaction(jitter):
    """"
    [Mqrt.dll] HRESULT MQBeginTransaction(ITransaction** ppTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ppTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQCloseCursor(jitter):
    """"
    [Mqrt.dll] HRESULT MQCloseCursor(HANDLE hCursor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCursor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQCloseQueue(jitter):
    """"
    [Mqrt.dll] HRESULT MQCloseQueue(QUEUEHANDLE hQueue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hQueue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQCreateCursor(jitter):
    """"
    [Mqrt.dll] HRESULT MQCreateCursor(QUEUEHANDLE hQueue, PHANDLE phCursor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hQueue", "phCursor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQCreateQueue(jitter):
    """"
    [Mqrt.dll] HRESULT MQCreateQueue(PSECURITY_DESCRIPTOR pSecurityDescriptor, MQQUEUEPROPS* pQueueProps, LPWSTR lpwcsFormatName, LPDWORD lpdwFormatNameLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "pQueueProps", "lpwcsFormatName", "lpdwFormatNameLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQDeleteQueue(jitter):
    """"
    [Mqrt.dll] HRESULT MQDeleteQueue(LPCWSTR lpwcsFormatName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwcsFormatName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQFreeMemory(jitter):
    """"
    [Mqrt.dll] VOID MQFreeMemory(PVOID pvMemory)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMemory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQFreeSecurityContext(jitter):
    """"
    [Mqrt.dll] VOID MQFreeSecurityContext(HANDLE hSecurityContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSecurityContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetMachineProperties(jitter):
    """"
    [Mqrt.dll] HRESULT MQGetMachineProperties(LPCWSTR lpwcsMachineName, const GUID* pguidMachineID, MQQMPROPS* pQMProps)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwcsMachineName", "pguidMachineID", "pQMProps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetOverlappedResult(jitter):
    """"
    [Mqrt.dll] HRESULT MQGetOverlappedResult(LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetPrivateComputerInformation(jitter):
    """"
    [Mqrt.dll] HRESULT MQGetPrivateComputerInformation(LPCWSTR lpwcsComputerName, MQPRIVATEPROPS* pPrivateProps)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwcsComputerName", "pPrivateProps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetQueueProperties(jitter):
    """"
    [Mqrt.dll] HRESULT MQGetQueueProperties(LPCWSTR lpwcsFormatName, MQQUEUEPROPS* pQueueProps)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwcsFormatName", "pQueueProps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetQueueSecurity(jitter):
    """"
    [Mqrt.dll] HRESULT MQGetQueueSecurity(LPCWSTR lpwcsFormatName, SECURITY_INFORMATION SecurityInformation, PSECURITY_DESCRIPTOR pSecurityDescriptor, DWORD nLength, LPDWORD lpnLengthNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwcsFormatName", "SecurityInformation", "pSecurityDescriptor", "nLength", "lpnLengthNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetSecurityContext(jitter):
    """"
    [Mqrt.dll] HRESULT MQGetSecurityContext(LPVOID lpCertBuffer, DWORD dwCertBufferLength, HANDLE* phSecurityContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCertBuffer", "dwCertBufferLength", "phSecurityContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQGetSecurityContextEx(jitter):
    """"
    [Mqrt.dll] HRESULT MQGetSecurityContextEx(LPVOID lpCertBuffer, DWORD dwCertBufferLength, HANDLE* phSecurityContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCertBuffer", "dwCertBufferLength", "phSecurityContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQHandleToFormatName(jitter):
    """"
    [Mqrt.dll] HRESULT MQHandleToFormatName(QUEUEHANDLE hQueue, LPWSTR lpwcsFormatName, LPDWORD lpdwCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hQueue", "lpwcsFormatName", "lpdwCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQInstanceToFormatName(jitter):
    """"
    [Mqrt.dll] HRESULT MQInstanceToFormatName(GUID* pGUID, LPWSTR lpwcsFormatName, LPDWORD lpdwCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pGUID", "lpwcsFormatName", "lpdwCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQLocateBegin(jitter):
    """"
    [Mqrt.dll] HRESULT MQLocateBegin(LPCWSTR lpwcsContext, MQRESTRICTION* pRestriction, MQCOLUMNSET* pColumns, MQSORTSET* pSort, PHANDLE phEnum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwcsContext", "pRestriction", "pColumns", "pSort", "phEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQLocateEnd(jitter):
    """"
    [Mqrt.dll] HRESULT MQLocateEnd(HANDLE hEnum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQLocateNext(jitter):
    """"
    [Mqrt.dll] HRESULT MQLocateNext(HANDLE hEnum, DWORD* pcProps, MQPROPVARIANT[] aPropVar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEnum", "pcProps", "aPropVar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQMarkMessageRejected(jitter):
    """"
    [Mqrt.dll] HRESULT MQMarkMessageRejected(QUEUEHANDLE hQueue, ULONGLONG ullLookupId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hQueue", "ullLookupId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQMgmtAction(jitter):
    """"
    [Mqrt.dll] HRESULT MQMgmtAction(LPCWSTR pMachineName, LPCWSTR pObjectName, LPCWSTR pAction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "pObjectName", "pAction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQMgmtGetInfo(jitter):
    """"
    [Mqrt.dll] HRESULT MQMgmtGetInfo(LPCWSTR pMachineName, LPCWSTR pObjectName, MQMGMTPROPS* pMgmtProps)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "pObjectName", "pMgmtProps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQMoveMessage(jitter):
    """"
    [Mqrt.dll] HRESULT MQMoveMessage(QUEUEHANDLE sourceQueue, QUEUEHANDLE targetQueue, ULONGLONG lookupID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sourceQueue", "targetQueue", "lookupID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQOpenQueue(jitter):
    """"
    [Mqrt.dll] HRESULT MQOpenQueue(LPCWSTR lpwcsFormatName, DWORD dwAccess, DWORD dwShareMode, QUEUEHANDLE* phQueue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwcsFormatName", "dwAccess", "dwShareMode", "phQueue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQPathNameToFormatName(jitter):
    """"
    [Mqrt.dll] HRESULT MQPathNameToFormatName(LPCWSTR lpwcsPathName, LPWSTR lpwcsFormatName, LPDWORD lpdwCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwcsPathName", "lpwcsFormatName", "lpdwCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQPurgeQueue(jitter):
    """"
    [Mqrt.dll] HRESULT MQPurgeQueue(HANDLE hQueue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hQueue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQReceiveMessage(jitter):
    """"
    [Mqrt.dll] HRESULT MQReceiveMessage(QUEUEHANDLE hSource, DWORD dwTimeout, DWORD dwAction, MQMSGPROPS* pMessageProps, LPOVERLAPPED lpOverlapped, PMQRECEIVECALLBACK fnReceiveCallback, HANDLE hCursor, ITransaction* pTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSource", "dwTimeout", "dwAction", "pMessageProps", "lpOverlapped", "fnReceiveCallback", "hCursor", "pTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQReceiveMessageByLookupId(jitter):
    """"
    [Mqrt.dll] HRESULT MQReceiveMessageByLookupId(QUEUEHANDLE hSource, ULONGLONG ullLookupId, DWORD dwLookupAction, MQMSGPROPS* pMessageProps, LPOVERLAPPED lpOverlapped, PMQRECEIVECALLBACK fnReceiveCallback, ITransaction* pTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSource", "ullLookupId", "dwLookupAction", "pMessageProps", "lpOverlapped", "fnReceiveCallback", "pTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQRegisterCertificate(jitter):
    """"
    [Mqrt.dll] HRESULT MQRegisterCertificate(DWORD dwFlags, PVOID lpCertBuffer, DWORD dwCertBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpCertBuffer", "dwCertBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQSendMessage(jitter):
    """"
    [Mqrt.dll] HRESULT MQSendMessage(QUEUEHANDLE hDestinationQueue, MQMSGPROPS* pMessageProps, ITransaction* pTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDestinationQueue", "pMessageProps", "pTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQSetQueueProperties(jitter):
    """"
    [Mqrt.dll] HRESULT MQSetQueueProperties(LPCWSTR lpwcsFormatName, MQQUEUEPROPS* pQueueProps)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwcsFormatName", "pQueueProps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mqrt_MQSetQueueSecurity(jitter):
    """"
    [Mqrt.dll] HRESULT MQSetQueueSecurity(LPCWSTR lpwcsFormatName, SECURITY_INFORMATION SecurityInformation, PSECURITY_DESCRIPTOR pSecurityDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwcsFormatName", "SecurityInformation", "pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
