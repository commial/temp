
def psapi_EmptyWorkingSet(jitter):
    """"
    [Psapi.dll] BOOL EmptyWorkingSet([ProcessHandle] hProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_EnumDeviceDrivers(jitter):
    """"
    [Psapi.dll] BOOL EnumDeviceDrivers(LPVOID* lpImageBase, DWORD cb, LPDWORD lpcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpImageBase", "cb", "lpcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_EnumPageFiles(jitter):
    """"
    [Psapi.dll] BOOL EnumPageFiles(PENUM_PAGE_CALLBACK pCallbackRoutine, LPVOID lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCallbackRoutine", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_EnumProcesses(jitter):
    """"
    [Psapi.dll] BOOL EnumProcesses(DWORD* pProcessIds, DWORD cb, DWORD* pBytesReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pProcessIds", "cb", "pBytesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_EnumProcessModules(jitter):
    """"
    [Psapi.dll] BOOL EnumProcessModules([ProcessHandle] hProcess, HMODULE* lphModule, DWORD cb, LPDWORD lpcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lphModule", "cb", "lpcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_EnumProcessModulesEx(jitter):
    """"
    [Psapi.dll] BOOL EnumProcessModulesEx([ProcessHandle] hProcess, HMODULE* lphModule, DWORD cb, LPDWORD lpcbNeeded, DWORD dwFilterFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lphModule", "cb", "lpcbNeeded", "dwFilterFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetDeviceDriverBaseName(jitter):
    """"
    [Psapi.dll] DWORD GetDeviceDriverBaseName(LPVOID ImageBase, LPTSTR lpBaseName, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ImageBase", "lpBaseName", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetDeviceDriverFileName(jitter):
    """"
    [Psapi.dll] DWORD GetDeviceDriverFileName(LPVOID ImageBase, LPTSTR lpFilename, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ImageBase", "lpFilename", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetMappedFileName(jitter):
    """"
    [Psapi.dll] DWORD GetMappedFileName([ProcessHandle] hProcess, LPVOID lpv, LPTSTR lpFilename, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpv", "lpFilename", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetModuleBaseName(jitter):
    """"
    [Psapi.dll] DWORD GetModuleBaseName([ProcessHandle] hProcess, HMODULE hModule, LPTSTR lpBaseName, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hModule", "lpBaseName", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetModuleFileNameEx(jitter):
    """"
    [Psapi.dll] DWORD GetModuleFileNameEx([ProcessHandle] hProcess, HMODULE hModule, LPTSTR lpFilename, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hModule", "lpFilename", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetModuleInformation(jitter):
    """"
    [Psapi.dll] BOOL GetModuleInformation([ProcessHandle] hProcess, HMODULE hModule, LPMODULEINFO lpmodinfo, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hModule", "lpmodinfo", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetPerformanceInfo(jitter):
    """"
    [Psapi.dll] BOOL GetPerformanceInfo(PPERFORMANCE_INFORMATION pPerformanceInformation, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPerformanceInformation", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetProcessImageFileName(jitter):
    """"
    [Psapi.dll] DWORD GetProcessImageFileName([ProcessHandle] hProcess, LPTSTR lpImageFileName, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpImageFileName", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetProcessMemoryInfo(jitter):
    """"
    [Psapi.dll] BOOL GetProcessMemoryInfo(HANDLE Process, PPROCESS_MEMORY_COUNTERS ppsmemCounters, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Process", "ppsmemCounters", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetWsChanges(jitter):
    """"
    [Psapi.dll] BOOL GetWsChanges([ProcessHandle] hProcess, PPSAPI_WS_WATCH_INFORMATION lpWatchInfo, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpWatchInfo", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_GetWsChangesEx(jitter):
    """"
    [Psapi.dll] BOOL GetWsChangesEx([ProcessHandle] hProcess, PPSAPI_WS_WATCH_INFORMATION_EX lpWatchInfoEx, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpWatchInfoEx", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_InitializeProcessForWsWatch(jitter):
    """"
    [Psapi.dll] BOOL InitializeProcessForWsWatch([ProcessHandle] hProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_QueryWorkingSet(jitter):
    """"
    [Psapi.dll] BOOL QueryWorkingSet([ProcessHandle] hProcess, PVOID pv, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "pv", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def psapi_QueryWorkingSetEx(jitter):
    """"
    [Psapi.dll] BOOL QueryWorkingSetEx([ProcessHandle] hProcess, PVOID pv, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "pv", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
