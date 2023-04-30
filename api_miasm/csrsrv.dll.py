
def csrsrv_CsrAddStaticServerThread(jitter):
    """"
    [CsrSrv.dll] PCSR_THREAD CsrAddStaticServerThread(HANDLE hThread, PCLIENT_ID ClientId, ULONG ThreadFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "ClientId", "ThreadFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrCallServerFromServer(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrCallServerFromServer(PCSR_API_MESSAGE ReceiveMsg, PCSR_API_MESSAGE ReplyMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ReceiveMsg", "ReplyMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrConnectToUser(jitter):
    """"
    [CsrSrv.dll] PCSR_THREAD CsrConnectToUser()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrCreateProcess(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrCreateProcess(HANDLE hProcess, HANDLE hThread, PCLIENT_ID ClientId, PCSR_NT_SESSION NtSession, ULONG Flags, PCLIENT_ID DebugCid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hThread", "ClientId", "NtSession", "Flags", "DebugCid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrCreateRemoteThread(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrCreateRemoteThread(HANDLE hThread, PCLIENT_ID ClientId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "ClientId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrCreateWait(jitter):
    """"
    [CsrSrv.dll] BOOLEAN CsrCreateWait(PLIST_ENTRY WaitList, CSR_WAIT_FUNCTION WaitFunction, PCSR_THREAD CsrWaitThread, PCSR_API_MESSAGE WaitApiMessage, PVOID WaitContext, PLIST_ENTRY UserWaitList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["WaitList", "WaitFunction", "CsrWaitThread", "WaitApiMessage", "WaitContext", "UserWaitList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDebugProcess(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrDebugProcess(PCSR_PROCESS CsrProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDebugProcessStop(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrDebugProcessStop(PCSR_PROCESS CsrProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDereferenceProcess(jitter):
    """"
    [CsrSrv.dll] VOID CsrDereferenceProcess(PCSR_PROCESS CsrProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDereferenceThread(jitter):
    """"
    [CsrSrv.dll] VOID CsrDereferenceThread(PCSR_THREAD CsrThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CsrThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDereferenceWait(jitter):
    """"
    [CsrSrv.dll] VOID CsrDereferenceWait(PLIST_ENTRY WaitList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["WaitList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDestroyProcess(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrDestroyProcess(PCLIENT_ID Cid, NTSTATUS ExitStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Cid", "ExitStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDestroyThread(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrDestroyThread(PCLIENT_ID Cid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Cid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrExecServerThread(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrExecServerThread(PVOID ThreadHandler, ULONG Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandler", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrGetProcessLuid(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrGetProcessLuid(HANDLE hProcess, PLUID Luid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Luid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrImpersonateClient(jitter):
    """"
    [CsrSrv.dll] BOOLEAN CsrImpersonateClient(PCSR_THREAD CsrThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CsrThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrLockProcessByClientId(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrLockProcessByClientId(HANDLE Pid, PCSR_PROCESS* CsrProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Pid", "CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrLockThreadByClientId(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrLockThreadByClientId(HANDLE Tid, PCSR_THREAD* CsrThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Tid", "CsrThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrMoveSatisfiedWait(jitter):
    """"
    [CsrSrv.dll] VOID CsrMoveSatisfiedWait(PLIST_ENTRY NewEntry, PLIST_ENTRY WaitList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["NewEntry", "WaitList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrNotifyWait(jitter):
    """"
    [CsrSrv.dll] BOOLEAN CsrNotifyWait(PLIST_ENTRY WaitList, ULONG WaitType, PVOID WaitArgument1, PVOID WaitArgument2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["WaitList", "WaitType", "WaitArgument1", "WaitArgument2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrPopulateDosDevices(jitter):
    """"
    [CsrSrv.dll] VOID CsrPopulateDosDevices()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrLockedReferenceProcess(jitter):
    """"
    [CsrSrv.dll] VOID CsrLockedReferenceProcess(PCSR_PROCESS CsrProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrQueryApiPort(jitter):
    """"
    [CsrSrv.dll] HANDLE CsrQueryApiPort()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrReferenceThread(jitter):
    """"
    [CsrSrv.dll] VOID CsrReferenceThread(PCSR_THREAD CsrThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CsrThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrRevertToSelf(jitter):
    """"
    [CsrSrv.dll] BOOLEAN CsrRevertToSelf()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrServerInitialization(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrServerInitialization(ULONG ArgumentCount, LPVOID Arguments)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ArgumentCount", "Arguments"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrSetBackgroundPriority(jitter):
    """"
    [CsrSrv.dll] VOID CsrSetBackgroundPriority(PCSR_PROCESS CsrProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrSetCallingSpooler(jitter):
    """"
    [CsrSrv.dll] VOID CsrSetCallingSpooler(ULONG Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrSetForegroundPriority(jitter):
    """"
    [CsrSrv.dll] VOID CsrSetForegroundPriority(PCSR_PROCESS CsrProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrShutdownProcesses(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrShutdownProcesses(PLUID CallerLuid, ULONG Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CallerLuid", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrUnhandledExceptionFilter(jitter):
    """"
    [CsrSrv.dll] LONG CsrUnhandledExceptionFilter(PEXCEPTION_POINTERS ExceptionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExceptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrUnlockProcess(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrUnlockProcess(PCSR_PROCESS CsrProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrUnlockThread(jitter):
    """"
    [CsrSrv.dll] NTSTATUS CsrUnlockThread(PCSR_THREAD CsrThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CsrThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrValidateMessageBuffer(jitter):
    """"
    [CsrSrv.dll] BOOLEAN CsrValidateMessageBuffer(PCSR_API_MESSAGE ApiMessage, PVOID* Buffer, ULONG ArgumentSize, ULONG ArgumentCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ApiMessage", "Buffer", "ArgumentSize", "ArgumentCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrValidateMessageString(jitter):
    """"
    [CsrSrv.dll] BOOLEAN CsrValidateMessageString(PCSR_API_MESSAGE ApiMessage, LPWSTR* MessageString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ApiMessage", "MessageString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
