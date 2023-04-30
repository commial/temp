
def psapi_EmptyWorkingSet(jitter):
    """
    BOOL EmptyWorkingSet(
        [ProcessHandle] hProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_EnumDeviceDrivers(jitter):
    """
    BOOL EnumDeviceDrivers(
        LPVOID* lpImageBase,
        DWORD cb,
        LPDWORD lpcbNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpImageBase", "cb", "lpcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_EnumPageFiles(jitter, get_str, set_str):
    """
    BOOL EnumPageFiles(
        PENUM_PAGE_CALLBACK pCallbackRoutine,
        LPVOID lpContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCallbackRoutine", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_EnumPageFilesA(jitter):
    psapi_EnumPageFiles(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def psapi_EnumPageFilesW(jitter):
    psapi_EnumPageFiles(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def psapi_EnumProcesses(jitter):
    """
    BOOL EnumProcesses(
        DWORD* pProcessIds,
        DWORD cb,
        DWORD* pBytesReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProcessIds", "cb", "pBytesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_EnumProcessModules(jitter):
    """
    BOOL EnumProcessModules(
        [ProcessHandle] hProcess,
        HMODULE* lphModule,
        DWORD cb,
        LPDWORD lpcbNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lphModule", "cb", "lpcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_EnumProcessModulesEx(jitter):
    """
    BOOL EnumProcessModulesEx(
        [ProcessHandle] hProcess,
        HMODULE* lphModule,
        DWORD cb,
        LPDWORD lpcbNeeded,
        DWORD dwFilterFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lphModule", "cb", "lpcbNeeded", "dwFilterFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetDeviceDriverBaseName(jitter, get_str, set_str):
    """
    DWORD GetDeviceDriverBaseName(
        LPVOID ImageBase,
        LPTSTR lpBaseName,
        DWORD nSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageBase", "lpBaseName", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetDeviceDriverBaseNameA(jitter):
    psapi_GetDeviceDriverBaseName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def psapi_GetDeviceDriverBaseNameW(jitter):
    psapi_GetDeviceDriverBaseName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def psapi_GetDeviceDriverFileName(jitter, get_str, set_str):
    """
    DWORD GetDeviceDriverFileName(
        LPVOID ImageBase,
        LPTSTR lpFilename,
        DWORD nSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageBase", "lpFilename", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetDeviceDriverFileNameA(jitter):
    psapi_GetDeviceDriverFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def psapi_GetDeviceDriverFileNameW(jitter):
    psapi_GetDeviceDriverFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def psapi_GetMappedFileName(jitter, get_str, set_str):
    """
    DWORD GetMappedFileName(
        [ProcessHandle] hProcess,
        LPVOID lpv,
        LPTSTR lpFilename,
        DWORD nSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpv", "lpFilename", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetMappedFileNameA(jitter):
    psapi_GetMappedFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def psapi_GetMappedFileNameW(jitter):
    psapi_GetMappedFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def psapi_GetModuleBaseName(jitter, get_str, set_str):
    """
    DWORD GetModuleBaseName(
        [ProcessHandle] hProcess,
        HMODULE hModule,
        LPTSTR lpBaseName,
        DWORD nSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hModule", "lpBaseName", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetModuleBaseNameA(jitter):
    psapi_GetModuleBaseName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def psapi_GetModuleBaseNameW(jitter):
    psapi_GetModuleBaseName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def psapi_GetModuleFileNameEx(jitter, get_str, set_str):
    """
    DWORD GetModuleFileNameEx(
        [ProcessHandle] hProcess,
        HMODULE hModule,
        LPTSTR lpFilename,
        DWORD nSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hModule", "lpFilename", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetModuleFileNameExA(jitter):
    psapi_GetModuleFileNameEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def psapi_GetModuleFileNameExW(jitter):
    psapi_GetModuleFileNameEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def psapi_GetModuleInformation(jitter):
    """
    BOOL GetModuleInformation(
        [ProcessHandle] hProcess,
        HMODULE hModule,
        LPMODULEINFO lpmodinfo,
        DWORD cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hModule", "lpmodinfo", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetPerformanceInfo(jitter):
    """
    BOOL GetPerformanceInfo(
        PPERFORMANCE_INFORMATION pPerformanceInformation,
        DWORD cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPerformanceInformation", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetProcessImageFileName(jitter, get_str, set_str):
    """
    DWORD GetProcessImageFileName(
        [ProcessHandle] hProcess,
        LPTSTR lpImageFileName,
        DWORD nSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpImageFileName", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetProcessImageFileNameA(jitter):
    psapi_GetProcessImageFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def psapi_GetProcessImageFileNameW(jitter):
    psapi_GetProcessImageFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def psapi_GetProcessMemoryInfo(jitter):
    """
    BOOL GetProcessMemoryInfo(
        HANDLE Process,
        PPROCESS_MEMORY_COUNTERS ppsmemCounters,
        DWORD cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Process", "ppsmemCounters", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetWsChanges(jitter):
    """
    BOOL GetWsChanges(
        [ProcessHandle] hProcess,
        PPSAPI_WS_WATCH_INFORMATION lpWatchInfo,
        DWORD cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpWatchInfo", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetWsChangesEx(jitter):
    """
    BOOL GetWsChangesEx(
        [ProcessHandle] hProcess,
        PPSAPI_WS_WATCH_INFORMATION_EX lpWatchInfoEx,
        DWORD cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpWatchInfoEx", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_InitializeProcessForWsWatch(jitter):
    """
    BOOL InitializeProcessForWsWatch(
        [ProcessHandle] hProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_QueryWorkingSet(jitter):
    """
    BOOL QueryWorkingSet(
        [ProcessHandle] hProcess,
        PVOID pv,
        DWORD cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "pv", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_QueryWorkingSetEx(jitter):
    """
    BOOL QueryWorkingSetEx(
        [ProcessHandle] hProcess,
        PVOID pv,
        DWORD cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "pv", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
