
def avrt_AvQuerySystemResponsiveness(jitter):
    """"
    [Avrt.dll] BOOL AvQuerySystemResponsiveness(HANDLE AvrtHandle, PULONG SystemResponsivenessValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["AvrtHandle", "SystemResponsivenessValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRtCreateThreadOrderingGroup(jitter):
    """"
    [Avrt.dll] BOOL AvRtCreateThreadOrderingGroup(PHANDLE Context, PLARGE_INTEGER Period, GUID* ThreadOrderingGuid, PLARGE_INTEGER Timeout)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "Period", "ThreadOrderingGuid", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRtCreateThreadOrderingGroupEx(jitter):
    """"
    [Avrt.dll] BOOL AvRtCreateThreadOrderingGroupEx(PHANDLE Context, PLARGE_INTEGER Period, GUID* ThreadOrderingGuid, PLARGE_INTEGER Timeout, LPCTSTR TaskName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "Period", "ThreadOrderingGuid", "Timeout", "TaskName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRtDeleteThreadOrderingGroup(jitter):
    """"
    [Avrt.dll] BOOL AvRtDeleteThreadOrderingGroup(HANDLE Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRtJoinThreadOrderingGroup(jitter):
    """"
    [Avrt.dll] BOOL AvRtJoinThreadOrderingGroup(PHANDLE Context, GUID* ThreadOrderingGuid, BOOL Before)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "ThreadOrderingGuid", "Before"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRtLeaveThreadOrderingGroup(jitter):
    """"
    [Avrt.dll] BOOL AvRtLeaveThreadOrderingGroup(HANDLE Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRtWaitOnThreadOrderingGroup(jitter):
    """"
    [Avrt.dll] BOOL AvRtWaitOnThreadOrderingGroup(HANDLE Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvRevertMmThreadCharacteristics(jitter):
    """"
    [Avrt.dll] BOOL AvRevertMmThreadCharacteristics(HANDLE AvrtHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["AvrtHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvSetMmMaxThreadCharacteristics(jitter):
    """"
    [Avrt.dll] HANDLE AvSetMmMaxThreadCharacteristics(LPCTSTR FirstTask, LPCTSTR SecondTask, LPDWORD TaskIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FirstTask", "SecondTask", "TaskIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvSetMmThreadCharacteristics(jitter):
    """"
    [Avrt.dll] HANDLE AvSetMmThreadCharacteristics(LPCTSTR TaskName, LPDWORD TaskIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TaskName", "TaskIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avrt_AvSetMmThreadPriority(jitter):
    """"
    [Avrt.dll] BOOL AvSetMmThreadPriority(HANDLE AvrtHandle, AVRT_PRIORITY Priority)
    """"
    ret_ad, args = jitter.func_args_stdcall(["AvrtHandle", "Priority"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
