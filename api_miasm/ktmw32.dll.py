
def ktmw32_CommitTransaction(jitter):
    """"
    [Ktmw32.dll] BOOL CommitTransaction(HANDLE TransactionHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_CommitTransactionAsync(jitter):
    """"
    [Ktmw32.dll] BOOL CommitTransactionAsync(HANDLE TransactionHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_CreateTransaction(jitter):
    """"
    [Ktmw32.dll] HANDLE CreateTransaction(LPSECURITY_ATTRIBUTES lpTransactionAttributes, LPGUID UOW, DWORD CreateOptions, DWORD IsolationLevel, DWORD IsolationFlags, DWORD Timeout, LPWSTR Description)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTransactionAttributes", "UOW", "CreateOptions", "IsolationLevel", "IsolationFlags", "Timeout", "Description"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_GetTransactionId(jitter):
    """"
    [Ktmw32.dll] BOOL GetTransactionId(HANDLE TransactionHandle, LPGUID TransactionId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle", "TransactionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_GetTransactionInformation(jitter):
    """"
    [Ktmw32.dll] BOOL GetTransactionInformation(HANDLE TransactionHandle, PDWORD Outcome, PDWORD IsolationLevel, PDWORD IsolationFlags, PDWORD Timeout, DWORD BufferLength, LPWSTR Description)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle", "Outcome", "IsolationLevel", "IsolationFlags", "Timeout", "BufferLength", "Description"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_OpenTransaction(jitter):
    """"
    [Ktmw32.dll] HANDLE OpenTransaction(DWORD dwDesiredAccess, LPGUID TransactionId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDesiredAccess", "TransactionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_RollbackComplete(jitter):
    """"
    [Ktmw32.dll] BOOL RollbackComplete(HANDLE EnlistmentHandle, PLARGE_INTEGER TmVirtualClock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_RollbackTransaction(jitter):
    """"
    [Ktmw32.dll] BOOL RollbackTransaction(HANDLE TransactionHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_RollbackTransactionAsync(jitter):
    """"
    [Ktmw32.dll] BOOL RollbackTransactionAsync(HANDLE TransactionHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_SetTransactionInformation(jitter):
    """"
    [Ktmw32.dll] BOOL SetTransactionInformation(HANDLE TransactionHandle, DWORD IsolationLevel, DWORD IsolationFlags, DWORD Timeout, LPWSTR Description)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle", "IsolationLevel", "IsolationFlags", "Timeout", "Description"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_CommitComplete(jitter):
    """"
    [Ktmw32.dll] BOOL CommitComplete(HANDLE EnlistmentHandle, PLARGE_INTEGER TmVirtualClock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_CommitEnlistment(jitter):
    """"
    [Ktmw32.dll] BOOL CommitEnlistment(HANDLE EnlistmentHandle, PLARGE_INTEGER TmVirtualClock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_GetEnlistmentId(jitter):
    """"
    [Ktmw32.dll] BOOL GetEnlistmentId(HANDLE EnlistmentHandle, LPGUID EnlistmentId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "EnlistmentId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_CreateEnlistment(jitter):
    """"
    [Ktmw32.dll] HANDLE CreateEnlistment(LPSECURITY_ATTRIBUTES lpEnlistmentrAttributes, HANDLE ResourceManagerHandle, HANDLE TransactionHandle, NOTIFICATION_MASK NotificationMask, DWORD CreateOptions, PVOID EnlistmentKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpEnlistmentrAttributes", "ResourceManagerHandle", "TransactionHandle", "NotificationMask", "CreateOptions", "EnlistmentKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_GetEnlistmentRecoveryInformation(jitter):
    """"
    [Ktmw32.dll] BOOL GetEnlistmentRecoveryInformation(HANDLE EnlistmentHandle, ULONG BufferSize, PVOID Buffer, PULONG BufferUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "BufferSize", "Buffer", "BufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_OpenEnlistment(jitter):
    """"
    [Ktmw32.dll] HANDLE OpenEnlistment(DWORD dwDesiredAccess, HANDLE ResourceManagerHandle, LPGUID EnlistmentId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDesiredAccess", "ResourceManagerHandle", "EnlistmentId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_PrepareEnlistment(jitter):
    """"
    [Ktmw32.dll] BOOL PrepareEnlistment(HANDLE EnlistmentHandle, PLARGE_INTEGER TmVirtualClock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_PrePrepareEnlistment(jitter):
    """"
    [Ktmw32.dll] BOOL PrePrepareEnlistment(HANDLE EnlistmentHandle, PLARGE_INTEGER TmVirtualClock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_RecoverEnlistment(jitter):
    """"
    [Ktmw32.dll] BOOL RecoverEnlistment(HANDLE EnlistmentHandle, PVOID EnlistmentKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "EnlistmentKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_ReadOnlyEnlistment(jitter):
    """"
    [Ktmw32.dll] BOOL ReadOnlyEnlistment(HANDLE EnlistmentHandle, PLARGE_INTEGER TmVirtualClock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_RollbackEnlistment(jitter):
    """"
    [Ktmw32.dll] BOOL RollbackEnlistment(HANDLE EnlistmentHandle, PLARGE_INTEGER TmVirtualClock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_SetEnlistmentRecoveryInformation(jitter):
    """"
    [Ktmw32.dll] BOOL SetEnlistmentRecoveryInformation(HANDLE EnlistmentHandle, ULONG BufferSize, PVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_SinglePhaseReject(jitter):
    """"
    [Ktmw32.dll] BOOL SinglePhaseReject(HANDLE EnlistmentHandle, PLARGE_INTEGER TmVirtualClock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_CreateResourceManager(jitter):
    """"
    [Ktmw32.dll] HANDLE CreateResourceManager(LPSECURITY_ATTRIBUTES lpResourceManagerAttributes, LPGUID ResourceManagerID, DWORD CreateOptions, HANDLE TmHandle, LPWSTR Description)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpResourceManagerAttributes", "ResourceManagerID", "CreateOptions", "TmHandle", "Description"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_GetNotificationResourceManager(jitter):
    """"
    [Ktmw32.dll] BOOL GetNotificationResourceManager(HANDLE ResourceManagerHandle, PTRANSACTION_NOTIFICATION TransactionNotification, ULONG NotificationLength, DWORD dwMilliseconds, PULONG ReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ResourceManagerHandle", "TransactionNotification", "NotificationLength", "dwMilliseconds", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_GetNotificationResourceManagerAsync(jitter):
    """"
    [Ktmw32.dll] BOOL GetNotificationResourceManagerAsync(HANDLE ResourceManagerHandle, PTRANSACTION_NOTIFICATION TransactionNotification, ULONG TransactionNotificationLength, PULONG ReturnLength, LPOVERLAPPED pOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ResourceManagerHandle", "TransactionNotification", "TransactionNotificationLength", "ReturnLength", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_OpenResourceManager(jitter):
    """"
    [Ktmw32.dll] HANDLE OpenResourceManager(DWORD dwDesiredAccess, HANDLE TmHandle, LPGUID RmGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDesiredAccess", "TmHandle", "RmGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_PrepareComplete(jitter):
    """"
    [Ktmw32.dll] BOOL PrepareComplete(HANDLE EnlistmentHandle, PLARGE_INTEGER TmVirtualClock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_PrePrepareComplete(jitter):
    """"
    [Ktmw32.dll] BOOL PrePrepareComplete(HANDLE EnlistmentHandle, PLARGE_INTEGER TmVirtualClock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_RecoverResourceManager(jitter):
    """"
    [Ktmw32.dll] BOOL RecoverResourceManager(HANDLE ResourceManagerHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ResourceManagerHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_SetResourceManagerCompletionPort(jitter):
    """"
    [Ktmw32.dll] BOOL SetResourceManagerCompletionPort(HANDLE ResourceManagerHandle, HANDLE IoCompletionPortHandle, ULONG_PTR CompletionKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ResourceManagerHandle", "IoCompletionPortHandle", "CompletionKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_CreateTransactionManager(jitter):
    """"
    [Ktmw32.dll] HANDLE CreateTransactionManager(LPSECURITY_ATTRIBUTES lpTransactionAttributes, LPWSTR LogFileName, ULONG CreateOptions, ULONG CommitStrength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTransactionAttributes", "LogFileName", "CreateOptions", "CommitStrength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_GetCurrentClockTransactionManager(jitter):
    """"
    [Ktmw32.dll] BOOL GetCurrentClockTransactionManager(HANDLE TransactionManagerHandle, PLARGE_INTEGER TmVirtualClock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TransactionManagerHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_GetTransactionManagerId(jitter):
    """"
    [Ktmw32.dll] BOOL GetTransactionManagerId(HANDLE TransactionManagerHandle, LPGUID TransactionManagerId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TransactionManagerHandle", "TransactionManagerId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_OpenTransactionManager(jitter):
    """"
    [Ktmw32.dll] HANDLE OpenTransactionManager(LPWSTR LogFileName, ACCESS_MASK DesiredAccess, ULONG OpenOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LogFileName", "DesiredAccess", "OpenOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_OpenTransactionManagerById(jitter):
    """"
    [Ktmw32.dll] HANDLE OpenTransactionManagerById(LPGUID TransactionManagerId, ACCESS_MASK DesiredAccess, ULONG OpenOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TransactionManagerId", "DesiredAccess", "OpenOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_RecoverTransactionManager(jitter):
    """"
    [Ktmw32.dll] BOOL RecoverTransactionManager(HANDLE TransactionManagerHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TransactionManagerHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_RenameTransactionManager(jitter):
    """"
    [Ktmw32.dll] BOOL RenameTransactionManager(LPWSTR LogFileName, LPGUID ExistingTransactionManagerGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LogFileName", "ExistingTransactionManagerGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ktmw32_RollforwardTransactionManager(jitter):
    """"
    [Ktmw32.dll] BOOL RollforwardTransactionManager(HANDLE TransactionManagerHandle, PLARGE_INTEGER TmVirtualClock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TransactionManagerHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
