
def avrt_AvQuerySystemResponsiveness(jitter):
    """
    BOOL AvQuerySystemResponsiveness(
        HANDLE AvrtHandle,
        PULONG SystemResponsivenessValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AvrtHandle", "SystemResponsivenessValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRtCreateThreadOrderingGroup(jitter):
    """
    BOOL AvRtCreateThreadOrderingGroup(
        PHANDLE Context,
        PLARGE_INTEGER Period,
        GUID* ThreadOrderingGuid,
        PLARGE_INTEGER Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context", "Period", "ThreadOrderingGuid", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRtCreateThreadOrderingGroupEx(jitter, get_str, set_str):
    """
    BOOL AvRtCreateThreadOrderingGroupEx(
        PHANDLE Context,
        PLARGE_INTEGER Period,
        GUID* ThreadOrderingGuid,
        PLARGE_INTEGER Timeout,
        LPCTSTR TaskName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context", "Period", "ThreadOrderingGuid", "Timeout", "TaskName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRtCreateThreadOrderingGroupExA(jitter):
    avrt_AvRtCreateThreadOrderingGroupEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avrt_AvRtCreateThreadOrderingGroupExW(jitter):
    avrt_AvRtCreateThreadOrderingGroupEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def avrt_AvRtDeleteThreadOrderingGroup(jitter):
    """
    BOOL AvRtDeleteThreadOrderingGroup(
        HANDLE Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRtJoinThreadOrderingGroup(jitter):
    """
    BOOL AvRtJoinThreadOrderingGroup(
        PHANDLE Context,
        GUID* ThreadOrderingGuid,
        BOOL Before
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context", "ThreadOrderingGuid", "Before"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRtLeaveThreadOrderingGroup(jitter):
    """
    BOOL AvRtLeaveThreadOrderingGroup(
        HANDLE Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRtWaitOnThreadOrderingGroup(jitter):
    """
    BOOL AvRtWaitOnThreadOrderingGroup(
        HANDLE Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRevertMmThreadCharacteristics(jitter):
    """
    BOOL AvRevertMmThreadCharacteristics(
        HANDLE AvrtHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AvrtHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvSetMmMaxThreadCharacteristics(jitter, get_str, set_str):
    """
    HANDLE AvSetMmMaxThreadCharacteristics(
        LPCTSTR FirstTask,
        LPCTSTR SecondTask,
        LPDWORD TaskIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FirstTask", "SecondTask", "TaskIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvSetMmMaxThreadCharacteristicsA(jitter):
    avrt_AvSetMmMaxThreadCharacteristics(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avrt_AvSetMmMaxThreadCharacteristicsW(jitter):
    avrt_AvSetMmMaxThreadCharacteristics(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def avrt_AvSetMmThreadCharacteristics(jitter, get_str, set_str):
    """
    HANDLE AvSetMmThreadCharacteristics(
        LPCTSTR TaskName,
        LPDWORD TaskIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TaskName", "TaskIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvSetMmThreadCharacteristicsA(jitter):
    avrt_AvSetMmThreadCharacteristics(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avrt_AvSetMmThreadCharacteristicsW(jitter):
    avrt_AvSetMmThreadCharacteristics(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def avrt_AvSetMmThreadPriority(jitter):
    """
    BOOL AvSetMmThreadPriority(
        HANDLE AvrtHandle,
        AVRT_PRIORITY Priority
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AvrtHandle", "Priority"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
