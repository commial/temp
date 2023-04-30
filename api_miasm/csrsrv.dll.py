
def csrsrv_CsrAddStaticServerThread(jitter):
    """
    PCSR_THREAD CsrAddStaticServerThread(
        HANDLE hThread,
        PCLIENT_ID ClientId,
        ULONG ThreadFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hThread", "ClientId", "ThreadFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrCallServerFromServer(jitter):
    """
    NTSTATUS CsrCallServerFromServer(
        PCSR_API_MESSAGE ReceiveMsg,
        PCSR_API_MESSAGE ReplyMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReceiveMsg", "ReplyMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrConnectToUser(jitter):
    """
    PCSR_THREAD CsrConnectToUser()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrCreateProcess(jitter):
    """
    NTSTATUS CsrCreateProcess(
        HANDLE hProcess,
        HANDLE hThread,
        PCLIENT_ID ClientId,
        PCSR_NT_SESSION NtSession,
        ULONG Flags,
        PCLIENT_ID DebugCid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hThread", "ClientId", "NtSession", "Flags", "DebugCid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrCreateRemoteThread(jitter):
    """
    NTSTATUS CsrCreateRemoteThread(
        HANDLE hThread,
        PCLIENT_ID ClientId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hThread", "ClientId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrCreateWait(jitter):
    """
    BOOLEAN CsrCreateWait(
        PLIST_ENTRY WaitList,
        CSR_WAIT_FUNCTION WaitFunction,
        PCSR_THREAD CsrWaitThread,
        PCSR_API_MESSAGE WaitApiMessage,
        PVOID WaitContext,
        PLIST_ENTRY UserWaitList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["WaitList", "WaitFunction", "CsrWaitThread", "WaitApiMessage", "WaitContext", "UserWaitList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDebugProcess(jitter):
    """
    NTSTATUS CsrDebugProcess(
        PCSR_PROCESS CsrProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDebugProcessStop(jitter):
    """
    NTSTATUS CsrDebugProcessStop(
        PCSR_PROCESS CsrProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDereferenceProcess(jitter):
    """
    VOID CsrDereferenceProcess(
        PCSR_PROCESS CsrProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDereferenceThread(jitter):
    """
    VOID CsrDereferenceThread(
        PCSR_THREAD CsrThread
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CsrThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDereferenceWait(jitter):
    """
    VOID CsrDereferenceWait(
        PLIST_ENTRY WaitList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["WaitList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDestroyProcess(jitter):
    """
    NTSTATUS CsrDestroyProcess(
        PCLIENT_ID Cid,
        NTSTATUS ExitStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Cid", "ExitStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrDestroyThread(jitter):
    """
    NTSTATUS CsrDestroyThread(
        PCLIENT_ID Cid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Cid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrExecServerThread(jitter):
    """
    NTSTATUS CsrExecServerThread(
        PVOID ThreadHandler,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandler", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrGetProcessLuid(jitter):
    """
    NTSTATUS CsrGetProcessLuid(
        HANDLE hProcess,
        PLUID Luid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Luid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrImpersonateClient(jitter):
    """
    BOOLEAN CsrImpersonateClient(
        PCSR_THREAD CsrThread
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CsrThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrLockProcessByClientId(jitter):
    """
    NTSTATUS CsrLockProcessByClientId(
        HANDLE Pid,
        PCSR_PROCESS* CsrProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Pid", "CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrLockThreadByClientId(jitter):
    """
    NTSTATUS CsrLockThreadByClientId(
        HANDLE Tid,
        PCSR_THREAD* CsrThread
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Tid", "CsrThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrMoveSatisfiedWait(jitter):
    """
    VOID CsrMoveSatisfiedWait(
        PLIST_ENTRY NewEntry,
        PLIST_ENTRY WaitList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NewEntry", "WaitList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrNotifyWait(jitter):
    """
    BOOLEAN CsrNotifyWait(
        PLIST_ENTRY WaitList,
        ULONG WaitType,
        PVOID WaitArgument1,
        PVOID WaitArgument2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["WaitList", "WaitType", "WaitArgument1", "WaitArgument2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrPopulateDosDevices(jitter):
    """
    VOID CsrPopulateDosDevices()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrLockedReferenceProcess(jitter):
    """
    VOID CsrLockedReferenceProcess(
        PCSR_PROCESS CsrProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrQueryApiPort(jitter):
    """
    HANDLE CsrQueryApiPort()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrReferenceThread(jitter):
    """
    VOID CsrReferenceThread(
        PCSR_THREAD CsrThread
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CsrThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrRevertToSelf(jitter):
    """
    BOOLEAN CsrRevertToSelf()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrServerInitialization(jitter):
    """
    NTSTATUS CsrServerInitialization(
        ULONG ArgumentCount,
        LPVOID Arguments
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ArgumentCount", "Arguments"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrSetBackgroundPriority(jitter):
    """
    VOID CsrSetBackgroundPriority(
        PCSR_PROCESS CsrProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrSetCallingSpooler(jitter):
    """
    VOID CsrSetCallingSpooler(
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrSetForegroundPriority(jitter):
    """
    VOID CsrSetForegroundPriority(
        PCSR_PROCESS CsrProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrShutdownProcesses(jitter):
    """
    NTSTATUS CsrShutdownProcesses(
        PLUID CallerLuid,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CallerLuid", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrUnhandledExceptionFilter(jitter):
    """
    LONG CsrUnhandledExceptionFilter(
        PEXCEPTION_POINTERS ExceptionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExceptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrUnlockProcess(jitter):
    """
    NTSTATUS CsrUnlockProcess(
        PCSR_PROCESS CsrProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CsrProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrUnlockThread(jitter):
    """
    NTSTATUS CsrUnlockThread(
        PCSR_THREAD CsrThread
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CsrThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrValidateMessageBuffer(jitter):
    """
    BOOLEAN CsrValidateMessageBuffer(
        PCSR_API_MESSAGE ApiMessage,
        PVOID* Buffer,
        ULONG ArgumentSize,
        ULONG ArgumentCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ApiMessage", "Buffer", "ArgumentSize", "ArgumentCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def csrsrv_CsrValidateMessageString(jitter):
    """
    BOOLEAN CsrValidateMessageString(
        PCSR_API_MESSAGE ApiMessage,
        LPWSTR* MessageString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ApiMessage", "MessageString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
