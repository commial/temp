
def kernel32_CheckRemoteDebuggerPresent(jitter):
    """"
    [Kernel32.dll] BOOL CheckRemoteDebuggerPresent([ProcessHandle] hProcess, PBOOL pbDebuggerPresent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "pbDebuggerPresent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ContinueDebugEvent(jitter):
    """"
    [Kernel32.dll] BOOL ContinueDebugEvent(DWORD dwProcessId, DWORD dwThreadId, [ContinueStatusFlag] dwContinueStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwProcessId", "dwThreadId", "dwContinueStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CopyExtendedContext(jitter):
    """"
    [Kernel32.dll] BOOL CopyExtendedContext(PCONTEXT_EX Destination, DWORD ContextFlags, PCONTEXT_EX Source)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Destination", "ContextFlags", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DebugActiveProcess(jitter):
    """"
    [Kernel32.dll] BOOL DebugActiveProcess(DWORD dwProcessId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DebugActiveProcessStop(jitter):
    """"
    [Kernel32.dll] BOOL DebugActiveProcessStop(DWORD dwProcessId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DebugBreak(jitter):
    """"
    [Kernel32.dll] VOID DebugBreak()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DebugBreakProcess(jitter):
    """"
    [Kernel32.dll] BOOL DebugBreakProcess(HANDLE Process)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Process"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DebugSetProcessKillOnExit(jitter):
    """"
    [Kernel32.dll] BOOL DebugSetProcessKillOnExit(BOOL KillOnExit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["KillOnExit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FatalExit(jitter):
    """"
    [Kernel32.dll] VOID FatalExit(int ExitCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExitCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FlushInstructionCache(jitter):
    """"
    [Kernel32.dll] BOOL FlushInstructionCache([ProcessHandle] hProcess, LPCVOID lpBaseAddress, SIZE_T dwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpBaseAddress", "dwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetEnabledExtendedFeatures(jitter):
    """"
    [Kernel32.dll] DWORD64 GetEnabledExtendedFeatures(DWORD64 FeatureMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FeatureMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetExtendedContextLength(jitter):
    """"
    [Kernel32.dll] BOOL GetExtendedContextLength(DWORD ContextFlags, PDWORD ContextLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextFlags", "ContextLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetExtendedFeaturesMask(jitter):
    """"
    [Kernel32.dll] DWORD64 GetExtendedFeaturesMask(PCONTEXT_EX ContextEx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextEx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadContext(jitter):
    """"
    [Kernel32.dll] BOOL GetThreadContext([ThreadHandle] hThread, LPCONTEXT lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadSelectorEntry(jitter):
    """"
    [Kernel32.dll] BOOL GetThreadSelectorEntry([ThreadHandle] hThread, DWORD dwSelector, LPLDT_ENTRY lpSelectorEntry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "dwSelector", "lpSelectorEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitializeExtendedContext(jitter):
    """"
    [Kernel32.dll] BOOL InitializeExtendedContext(PVOID Context, DWORD ContextFlags, PCONTEXT_EX* ContextEx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "ContextFlags", "ContextEx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsDebuggerPresent(jitter):
    """"
    [Kernel32.dll] BOOL IsDebuggerPresent()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LocateExtendedFeature(jitter):
    """"
    [Kernel32.dll] PVOID LocateExtendedFeature(PCONTEXT_EX ContextEx, DWORD FeatureId, PDWORD Length)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextEx", "FeatureId", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LocateLegacyContext(jitter):
    """"
    [Kernel32.dll] PCONTEXT LocateLegacyContext(PCONTEXT_EX ContextEx, PDWORD Length)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextEx", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OutputDebugString(jitter, get_str, set_str):
    """"
    [Kernel32.dll] void OutputDebugString(LPCTSTR lpOutputString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpOutputString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OutputDebugStringA(jitter):
    kernel32_OutputDebugString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_OutputDebugStringW(jitter):
    kernel32_OutputDebugString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_ReadProcessMemory(jitter):
    """"
    [Kernel32.dll] BOOL ReadProcessMemory([ProcessHandle] hProcess, LPCVOID lpBaseAddress, LPVOID lpBuffer, SIZE_T nSize, SIZE_T* lpNumberOfBytesRead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpBaseAddress", "lpBuffer", "nSize", "lpNumberOfBytesRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetExtendedFeaturesMask(jitter):
    """"
    [Kernel32.dll] VOID SetExtendedFeaturesMask(PCONTEXT_EX ContextEx, DWORD64 FeatureMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextEx", "FeatureMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadContext(jitter):
    """"
    [Kernel32.dll] BOOL SetThreadContext([ThreadHandle] hThread, const CONTEXT* lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WaitForDebugEvent(jitter):
    """"
    [Kernel32.dll] BOOL WaitForDebugEvent(LPDEBUG_EVENT lpDebugEvent, [WaitTimeout] dwMilliseconds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpDebugEvent", "dwMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Wow64GetThreadContext(jitter):
    """"
    [Kernel32.dll] BOOL Wow64GetThreadContext([ThreadHandle] hThread, PWOW64_CONTEXT lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Wow64GetThreadSelectorEntry(jitter):
    """"
    [Kernel32.dll] BOOL Wow64GetThreadSelectorEntry([ThreadHandle] hThread, DWORD dwSelector, PWOW64_LDT_ENTRY lpSelectorEntry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "dwSelector", "lpSelectorEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Wow64SetThreadContext(jitter):
    """"
    [Kernel32.dll] BOOL Wow64SetThreadContext([ThreadHandle] hThread, CONST WOW64_CONTEXT* lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WriteProcessMemory(jitter):
    """"
    [Kernel32.dll] BOOL WriteProcessMemory([ProcessHandle] hProcess, LPVOID lpBaseAddress, LPCVOID lpBuffer, SIZE_T nSize, SIZE_T* lpNumberOfBytesWritten)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpBaseAddress", "lpBuffer", "nSize", "lpNumberOfBytesWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AddDllDirectory(jitter):
    """"
    [Kernel32.dll] DLL_DIRECTORY_COOKIE AddDllDirectory(PCWSTR NewDirectory)
    """"
    ret_ad, args = jitter.func_args_stdcall(["NewDirectory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DisableThreadLibraryCalls(jitter):
    """"
    [Kernel32.dll] BOOL DisableThreadLibraryCalls(HMODULE hModule)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FreeLibrary(jitter):
    """"
    [Kernel32.dll] BOOL FreeLibrary(HMODULE hModule)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FreeLibraryAndExitThread(jitter):
    """"
    [Kernel32.dll] VOID FreeLibraryAndExitThread(HMODULE hModule, DWORD dwExitCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "dwExitCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDllDirectory(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetDllDirectory(DWORD nBufferLength, LPTSTR lpBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nBufferLength", "lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDllDirectoryA(jitter):
    kernel32_GetDllDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetDllDirectoryW(jitter):
    kernel32_GetDllDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetModuleFileName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetModuleFileName(HMODULE hModule, LPTSTR lpFilename, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "lpFilename", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetModuleFileNameA(jitter):
    kernel32_GetModuleFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetModuleFileNameW(jitter):
    kernel32_GetModuleFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetModuleHandle(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HMODULE GetModuleHandle(LPCTSTR lpModuleName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpModuleName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetModuleHandleA(jitter):
    kernel32_GetModuleHandle(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetModuleHandleW(jitter):
    kernel32_GetModuleHandle(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetModuleHandleEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetModuleHandleEx([GetModuleHandleExFlags] dwFlags, LPCTSTR lpModuleName, HMODULE* phModule)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpModuleName", "phModule"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetModuleHandleExA(jitter):
    kernel32_GetModuleHandleEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetModuleHandleExW(jitter):
    kernel32_GetModuleHandleEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetProcAddress(jitter):
    """"
    [Kernel32.dll] FARPROC GetProcAddress(HMODULE hModule, LPCSTR lpProcName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "lpProcName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LoadLibrary(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HMODULE LoadLibrary(LPCTSTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LoadLibraryA(jitter):
    kernel32_LoadLibrary(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_LoadLibraryW(jitter):
    kernel32_LoadLibrary(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_LoadLibraryEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HMODULE LoadLibraryEx(LPCTSTR lpFileName, HANDLE hFile, [LoadLibraryExFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "hFile", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LoadLibraryExA(jitter):
    kernel32_LoadLibraryEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_LoadLibraryExW(jitter):
    kernel32_LoadLibraryEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_LoadModule(jitter):
    """"
    [Kernel32.dll] DWORD LoadModule(LPCSTR lpModuleName, LPVOID lpParameterBlock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpModuleName", "lpParameterBlock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LoadPackagedLibrary(jitter):
    """"
    [Kernel32.dll] HMODULE LoadPackagedLibrary(LPCWSTR lpwLibFileName, DWORD Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwLibFileName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RemoveDllDirectory(jitter):
    """"
    [Kernel32.dll] BOOL RemoveDllDirectory(DLL_DIRECTORY_COOKIE Cookie)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetDefaultDllDirectories(jitter):
    """"
    [Kernel32.dll] BOOL SetDefaultDllDirectories([LOAD_LIBRARY_SEARCH_FLAGS] DirectoryFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DirectoryFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetDllDirectory(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetDllDirectory(LPCTSTR lpPathName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPathName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetDllDirectoryA(jitter):
    kernel32_SetDllDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetDllDirectoryW(jitter):
    kernel32_SetDllDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateToolhelp32Snapshot(jitter):
    """"
    [Kernel32.dll] [FILE_HANDLE] CreateToolhelp32Snapshot([CreateToolhelp32SnapshotFlags] dwFlags, DWORD th32ProcessID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "th32ProcessID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Heap32First(jitter):
    """"
    [Kernel32.dll] BOOL Heap32First(LPHEAPENTRY32 lphe, DWORD th32ProcessID, ULONG_PTR th32HeapID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lphe", "th32ProcessID", "th32HeapID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Heap32ListFirst(jitter):
    """"
    [Kernel32.dll] BOOL Heap32ListFirst(HANDLE hSnapshot, LPHEAPLIST32 lphl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSnapshot", "lphl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Heap32ListNext(jitter):
    """"
    [Kernel32.dll] BOOL Heap32ListNext(HANDLE hSnapshot, LPHEAPLIST32 lphl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSnapshot", "lphl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Heap32Next(jitter):
    """"
    [Kernel32.dll] BOOL Heap32Next(LPHEAPENTRY32 lphe)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lphe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Module32First(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL Module32First(HANDLE hSnapshot, LPMODULEENTRY32 lpme)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSnapshot", "lpme"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Module32FirstA(jitter):
    kernel32_Module32First(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_Module32FirstW(jitter):
    kernel32_Module32First(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_Module32Next(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL Module32Next(HANDLE hSnapshot, LPMODULEENTRY32 lpme)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSnapshot", "lpme"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Module32NextA(jitter):
    kernel32_Module32Next(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_Module32NextW(jitter):
    kernel32_Module32Next(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_Process32First(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL Process32First(HANDLE hSnapshot, LPPROCESSENTRY32 lppe)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSnapshot", "lppe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Process32FirstA(jitter):
    kernel32_Process32First(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_Process32FirstW(jitter):
    kernel32_Process32First(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_Process32Next(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL Process32Next(HANDLE hSnapshot, LPPROCESSENTRY32 lppe)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSnapshot", "lppe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Process32NextA(jitter):
    kernel32_Process32Next(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_Process32NextW(jitter):
    kernel32_Process32Next(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_Thread32First(jitter):
    """"
    [Kernel32.dll] BOOL Thread32First(HANDLE hSnapshot, LPTHREADENTRY32 lpte)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSnapshot", "lpte"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Thread32Next(jitter):
    """"
    [Kernel32.dll] BOOL Thread32Next(HANDLE hSnapshot, LPTHREADENTRY32 lpte)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSnapshot", "lpte"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Toolhelp32ReadProcessMemory(jitter):
    """"
    [Kernel32.dll] BOOL Toolhelp32ReadProcessMemory(DWORD th32ProcessID, LPCVOID lpBaseAddress, LPVOID lpBuffer, SIZE_T cbRead, SIZE_T lpNumberOfBytesRead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["th32ProcessID", "lpBaseAddress", "lpBuffer", "cbRead", "lpNumberOfBytesRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ApplicationRecoveryFinished(jitter):
    """"
    [Kernel32.dll] VOID ApplicationRecoveryFinished(BOOL bSuccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bSuccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ApplicationRecoveryInProgress(jitter):
    """"
    [Kernel32.dll] HRESULT ApplicationRecoveryInProgress(PBOOL pbCanceled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pbCanceled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetApplicationRecoveryCallback(jitter):
    """"
    [Kernel32.dll] HRESULT GetApplicationRecoveryCallback([ProcessHandle] hProcess, APPLICATION_RECOVERY_CALLBACK* pRecoveryCallback, PVOID* ppvParameter, DWORD dwPingInterval, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "pRecoveryCallback", "ppvParameter", "dwPingInterval", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetApplicationRestartSettings(jitter):
    """"
    [Kernel32.dll] HRESULT GetApplicationRestartSettings([ProcessHandle] hProcess, PWSTR pwzCommandline, PDWORD pcchSize, PDWORD pdwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "pwzCommandline", "pcchSize", "pdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RegisterApplicationRecoveryCallback(jitter):
    """"
    [Kernel32.dll] HRESULT RegisterApplicationRecoveryCallback(APPLICATION_RECOVERY_CALLBACK pRecoveryCallback, PVOID pvParameter, DWORD dwPingInterval, [ApplicationRestartFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRecoveryCallback", "pvParameter", "dwPingInterval", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RegisterApplicationRestart(jitter):
    """"
    [Kernel32.dll] HRESULT RegisterApplicationRestart(PCWSTR pwzCommandline, [ApplicationRestartFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwzCommandline", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_UnregisterApplicationRecoveryCallback(jitter):
    """"
    [Kernel32.dll] HRESULT UnregisterApplicationRecoveryCallback()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_UnregisterApplicationRestart(jitter):
    """"
    [Kernel32.dll] HRESULT UnregisterApplicationRestart()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPrivateProfileInt(jitter, get_str, set_str):
    """"
    [Kernel32.dll] UINT GetPrivateProfileInt(LPCTSTR lpAppName, LPCTSTR lpKeyName, INT nDefault, LPCTSTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAppName", "lpKeyName", "nDefault", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPrivateProfileIntA(jitter):
    kernel32_GetPrivateProfileInt(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetPrivateProfileIntW(jitter):
    kernel32_GetPrivateProfileInt(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetPrivateProfileSection(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetPrivateProfileSection(LPCTSTR lpAppName, LPTSTR lpReturnedString, DWORD nSize, LPCTSTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAppName", "lpReturnedString", "nSize", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPrivateProfileSectionA(jitter):
    kernel32_GetPrivateProfileSection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetPrivateProfileSectionW(jitter):
    kernel32_GetPrivateProfileSection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetPrivateProfileSectionNames(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetPrivateProfileSectionNames(LPTSTR lpszReturnBuffer, DWORD nSize, LPCTSTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszReturnBuffer", "nSize", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPrivateProfileSectionNamesA(jitter):
    kernel32_GetPrivateProfileSectionNames(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetPrivateProfileSectionNamesW(jitter):
    kernel32_GetPrivateProfileSectionNames(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetPrivateProfileString(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetPrivateProfileString(LPCTSTR lpAppName, LPCTSTR lpKeyName, LPCTSTR lpDefault, LPTSTR lpReturnedString, DWORD nSize, LPCTSTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAppName", "lpKeyName", "lpDefault", "lpReturnedString", "nSize", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPrivateProfileStringA(jitter):
    kernel32_GetPrivateProfileString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetPrivateProfileStringW(jitter):
    kernel32_GetPrivateProfileString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetPrivateProfileStruct(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetPrivateProfileStruct(LPCTSTR lpszSection, LPCTSTR lpszKey, LPVOID lpStruct, UINT uSizeStruct, LPCTSTR szFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszSection", "lpszKey", "lpStruct", "uSizeStruct", "szFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPrivateProfileStructA(jitter):
    kernel32_GetPrivateProfileStruct(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetPrivateProfileStructW(jitter):
    kernel32_GetPrivateProfileStruct(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetProfileInt(jitter, get_str, set_str):
    """"
    [Kernel32.dll] UINT GetProfileInt(LPCTSTR lpAppName, LPCTSTR lpKeyName, INT nDefault)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAppName", "lpKeyName", "nDefault"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProfileIntA(jitter):
    kernel32_GetProfileInt(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetProfileIntW(jitter):
    kernel32_GetProfileInt(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetProfileSection(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetProfileSection(LPCTSTR lpAppName, LPTSTR lpReturnedString, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAppName", "lpReturnedString", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProfileSectionA(jitter):
    kernel32_GetProfileSection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetProfileSectionW(jitter):
    kernel32_GetProfileSection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetProfileString(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetProfileString(LPCTSTR lpAppName, LPCTSTR lpKeyName, LPCTSTR lpDefault, LPTSTR lpReturnedString, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAppName", "lpKeyName", "lpDefault", "lpReturnedString", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProfileStringA(jitter):
    kernel32_GetProfileString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetProfileStringW(jitter):
    kernel32_GetProfileString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_WritePrivateProfileSection(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL WritePrivateProfileSection(LPCTSTR lpAppName, LPCTSTR lpString, LPCTSTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAppName", "lpString", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WritePrivateProfileSectionA(jitter):
    kernel32_WritePrivateProfileSection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_WritePrivateProfileSectionW(jitter):
    kernel32_WritePrivateProfileSection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_WritePrivateProfileString(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL WritePrivateProfileString(LPCTSTR lpAppName, LPCTSTR lpKeyName, LPCTSTR lpString, LPCTSTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAppName", "lpKeyName", "lpString", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WritePrivateProfileStringA(jitter):
    kernel32_WritePrivateProfileString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_WritePrivateProfileStringW(jitter):
    kernel32_WritePrivateProfileString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_WritePrivateProfileStruct(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL WritePrivateProfileStruct(LPCTSTR lpszSection, LPCTSTR lpszKey, LPVOID lpStruct, UINT uSizeStruct, LPCTSTR szFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszSection", "lpszKey", "lpStruct", "uSizeStruct", "szFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WritePrivateProfileStructA(jitter):
    kernel32_WritePrivateProfileStruct(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_WritePrivateProfileStructW(jitter):
    kernel32_WritePrivateProfileStruct(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_WriteProfileSection(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL WriteProfileSection(LPCTSTR lpAppName, LPCTSTR lpString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAppName", "lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WriteProfileSectionA(jitter):
    kernel32_WriteProfileSection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_WriteProfileSectionW(jitter):
    kernel32_WriteProfileSection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_WriteProfileString(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL WriteProfileString(LPCTSTR lpAppName, LPCTSTR lpKeyName, LPCTSTR lpString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAppName", "lpKeyName", "lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WriteProfileStringA(jitter):
    kernel32_WriteProfileString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_WriteProfileStringW(jitter):
    kernel32_WriteProfileString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32__lopen(jitter):
    """"
    [Kernel32.dll] HFILE _lopen(LPCSTR lpPathName, int iReadWrite)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPathName", "iReadWrite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32__lcreat(jitter):
    """"
    [Kernel32.dll] HFILE _lcreat(LPCSTR lpPathName, [lcreatAttribute] iAttribute)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPathName", "iAttribute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32__lread(jitter):
    """"
    [Kernel32.dll] UINT _lread(HFILE hFile, LPVOID lpBuffer, UINT uBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffer", "uBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32__lwrite(jitter):
    """"
    [Kernel32.dll] UINT _lwrite(HFILE hFile, LPVOID lpBuffer, UINT uBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffer", "uBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32__hread(jitter):
    """"
    [Kernel32.dll] long _hread(HFILE hFile, LPVOID lpBuffer, LONG lBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffer", "lBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32__hwrite(jitter):
    """"
    [Kernel32.dll] long _hwrite(HFILE hFile, LPVOID lpBuffer, LONG lBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffer", "lBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32__lclose(jitter):
    """"
    [Kernel32.dll] HFILE _lclose(HFILE hFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32__llseek(jitter):
    """"
    [Kernel32.dll] LONG _llseek(HFILE hFile, LONG lOffset, [SEEK_TYPE] iOrigin)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lOffset", "iOrigin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AreFileApisANSI(jitter):
    """"
    [Kernel32.dll] BOOL AreFileApisANSI()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CheckNameLegalDOS8Dot3(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL CheckNameLegalDOS8Dot3(LPCTSTR lpName, LPSTR lpOemName, DWORD OemNameSize, PBOOL pbNameContainsSpaces, PBOOL pbNameLegal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpName", "lpOemName", "OemNameSize", "pbNameContainsSpaces", "pbNameLegal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CheckNameLegalDOS8Dot3A(jitter):
    kernel32_CheckNameLegalDOS8Dot3(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CheckNameLegalDOS8Dot3W(jitter):
    kernel32_CheckNameLegalDOS8Dot3(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CopyFile(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL CopyFile(LPCTSTR lpExistingFileName, LPCTSTR lpNewFileName, BOOL bFailIfExists)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpExistingFileName", "lpNewFileName", "bFailIfExists"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CopyFileA(jitter):
    kernel32_CopyFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CopyFileW(jitter):
    kernel32_CopyFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CopyFile2(jitter):
    """"
    [Kernel32.dll] HRESULT CopyFile2(PCWSTR pwszExistingFileName, PCWSTR pwszNewFileName, COPYFILE2_EXTENDED_PARAMETERS* pExtendedParameters)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszExistingFileName", "pwszNewFileName", "pExtendedParameters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CopyFileEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL CopyFileEx(LPCTSTR lpExistingFileName, LPCTSTR lpNewFileName, LPPROGRESS_ROUTINE lpProgressRoutine, LPVOID lpData, LPBOOL pbCancel, [COPY_FILE_FLAGS] dwCopyFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpExistingFileName", "lpNewFileName", "lpProgressRoutine", "lpData", "pbCancel", "dwCopyFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CopyFileExA(jitter):
    kernel32_CopyFileEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CopyFileExW(jitter):
    kernel32_CopyFileEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CopyFileTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL CopyFileTransacted(LPCTSTR lpExistingFileName, LPCTSTR lpNewFileName, LPPROGRESS_ROUTINE lpProgressRoutine, LPVOID lpData, LPBOOL pbCancel, [COPY_FILE_FLAGS] dwCopyFlags, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpExistingFileName", "lpNewFileName", "lpProgressRoutine", "lpData", "pbCancel", "dwCopyFlags", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CopyFileTransactedA(jitter):
    kernel32_CopyFileTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CopyFileTransactedW(jitter):
    kernel32_CopyFileTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateFile(jitter, get_str, set_str):
    """"
    [Kernel32.dll] [FILE_HANDLE] CreateFile(LPCTSTR lpFileName, [FILE_ACCESS_MASK] dwDesiredAccess, [FILE_SHARE_MODE] dwShareMode, LPSECURITY_ATTRIBUTES lpSecurityAttributes, [CreationDisposition] dwCreationDisposition, [FlagsAndAttributes] dwFlagsAndAttributes, HANDLE hTemplateFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "dwDesiredAccess", "dwShareMode", "lpSecurityAttributes", "dwCreationDisposition", "dwFlagsAndAttributes", "hTemplateFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateFileA(jitter):
    kernel32_CreateFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateFileW(jitter):
    kernel32_CreateFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateFile2(jitter):
    """"
    [Kernel32.dll] HANDLE CreateFile2(LPCWSTR lpFileName, [FILE_ACCESS_MASK] dwDesiredAccess, [FILE_SHARE_MODE] dwShareMode, [CreationDisposition] dwCreationDisposition, LPCREATEFILE2_EXTENDED_PARAMETERS pCreateExParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "dwDesiredAccess", "dwShareMode", "dwCreationDisposition", "pCreateExParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateFileTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] [FILE_HANDLE] CreateFileTransacted(LPCTSTR lpFileName, [FILE_ACCESS_MASK] dwDesiredAccess, [FILE_SHARE_MODE] dwShareMode, LPSECURITY_ATTRIBUTES lpSecurityAttributes, [CreationDisposition] dwCreationDisposition, [FlagsAndAttributes] dwFlagsAndAttributes, HANDLE hTemplateFile, HANDLE hTransaction, PUSHORT pusMiniVersion, PVOID pExtendedParameter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "dwDesiredAccess", "dwShareMode", "lpSecurityAttributes", "dwCreationDisposition", "dwFlagsAndAttributes", "hTemplateFile", "hTransaction", "pusMiniVersion", "pExtendedParameter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateFileTransactedA(jitter):
    kernel32_CreateFileTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateFileTransactedW(jitter):
    kernel32_CreateFileTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateHardLink(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL CreateHardLink(LPCTSTR lpFileName, LPCTSTR lpExistingFileName, LPSECURITY_ATTRIBUTES lpSecurityAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "lpExistingFileName", "lpSecurityAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateHardLinkA(jitter):
    kernel32_CreateHardLink(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateHardLinkW(jitter):
    kernel32_CreateHardLink(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateHardLinkTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL CreateHardLinkTransacted(LPCTSTR lpFileName, LPCTSTR lpExistingFileName, LPSECURITY_ATTRIBUTES lpSecurityAttributes, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "lpExistingFileName", "lpSecurityAttributes", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateHardLinkTransactedA(jitter):
    kernel32_CreateHardLinkTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateHardLinkTransactedW(jitter):
    kernel32_CreateHardLinkTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateSymbolicLink(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOLEAN CreateSymbolicLink(LPTSTR lpSymlinkFileName, LPTSTR lpTargetFileName, [CreateSymbolicLinkFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSymlinkFileName", "lpTargetFileName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateSymbolicLinkA(jitter):
    kernel32_CreateSymbolicLink(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateSymbolicLinkW(jitter):
    kernel32_CreateSymbolicLink(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateSymbolicLinkTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOLEAN CreateSymbolicLinkTransacted(LPTSTR lpSymlinkFileName, LPTSTR lpTargetFileName, [CreateSymbolicLinkFlags] dwFlags, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSymlinkFileName", "lpTargetFileName", "dwFlags", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateSymbolicLinkTransactedA(jitter):
    kernel32_CreateSymbolicLinkTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateSymbolicLinkTransactedW(jitter):
    kernel32_CreateSymbolicLinkTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_DeleteFile(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL DeleteFile(LPCTSTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DeleteFileA(jitter):
    kernel32_DeleteFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_DeleteFileW(jitter):
    kernel32_DeleteFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_DeleteFileTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL DeleteFileTransacted(LPCTSTR lpFileName, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DeleteFileTransactedA(jitter):
    kernel32_DeleteFileTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_DeleteFileTransactedW(jitter):
    kernel32_DeleteFileTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindClose(jitter):
    """"
    [Kernel32.dll] BOOL FindClose(HANDLE hFindFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFindFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindFirstFile(jitter, get_str, set_str):
    """"
    [Kernel32.dll] [FILE_HANDLE] FindFirstFile(LPCTSTR lpFileName, LPWIN32_FIND_DATA lpFindFileData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "lpFindFileData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindFirstFileA(jitter):
    kernel32_FindFirstFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FindFirstFileW(jitter):
    kernel32_FindFirstFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindFirstFileEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] [FILE_HANDLE] FindFirstFileEx(LPCTSTR lpFileName, FINDEX_INFO_LEVELS fInfoLevelId, LPVOID lpFindFileData, FINDEX_SEARCH_OPS fSearchOp, LPVOID lpSearchFilter, [FindFirstFileExFlags] dwAdditionalFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "fInfoLevelId", "lpFindFileData", "fSearchOp", "lpSearchFilter", "dwAdditionalFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindFirstFileExA(jitter):
    kernel32_FindFirstFileEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FindFirstFileExW(jitter):
    kernel32_FindFirstFileEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindFirstFileNameTransactedW(jitter):
    """"
    [Kernel32.dll] [FILE_HANDLE] FindFirstFileNameTransactedW(LPCWSTR lpFileName, DWORD dwFlags, LPDWORD StringLength, PWCHAR LinkName, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "dwFlags", "StringLength", "LinkName", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindFirstFileNameW(jitter):
    """"
    [Kernel32.dll] [FILE_HANDLE] FindFirstFileNameW(LPCWSTR lpFileName, DWORD dwFlags, LPDWORD StringLength, PWCHAR LinkName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "dwFlags", "StringLength", "LinkName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindFirstFileTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] [FILE_HANDLE] FindFirstFileTransacted(LPCTSTR lpFileName, FINDEX_INFO_LEVELS fInfoLevelId, LPVOID lpFindFileData, FINDEX_SEARCH_OPS fSearchOp, LPVOID lpSearchFilter, [FindFirstFileExFlags] dwAdditionalFlags, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "fInfoLevelId", "lpFindFileData", "fSearchOp", "lpSearchFilter", "dwAdditionalFlags", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindFirstFileTransactedA(jitter):
    kernel32_FindFirstFileTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FindFirstFileTransactedW(jitter):
    kernel32_FindFirstFileTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindFirstStreamTransactedW(jitter):
    """"
    [Kernel32.dll] [FILE_HANDLE] FindFirstStreamTransactedW(LPCWSTR lpFileName, STREAM_INFO_LEVELS InfoLevel, LPVOID lpFindStreamData, DWORD dwFlags, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "InfoLevel", "lpFindStreamData", "dwFlags", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindFirstStreamW(jitter):
    """"
    [Kernel32.dll] [FILE_HANDLE] FindFirstStreamW(LPCWSTR lpFileName, STREAM_INFO_LEVELS InfoLevel, LPVOID lpFindStreamData, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "InfoLevel", "lpFindStreamData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindNextFile(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL FindNextFile(HANDLE hFindFile, LPWIN32_FIND_DATA lpFindFileData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFindFile", "lpFindFileData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindNextFileA(jitter):
    kernel32_FindNextFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FindNextFileW(jitter):
    kernel32_FindNextFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindNextFileNameW(jitter):
    """"
    [Kernel32.dll] BOOL FindNextFileNameW(HANDLE hFindStream, LPDWORD StringLength, PWCHAR LinkName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFindStream", "StringLength", "LinkName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindNextStreamW(jitter):
    """"
    [Kernel32.dll] BOOL FindNextStreamW(HANDLE hFindStream, LPVOID lpFindStreamData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFindStream", "lpFindStreamData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetBinaryType(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetBinaryType(LPCTSTR lpApplicationName, [GetBinaryTypeResult*] lpBinaryType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpApplicationName", "lpBinaryType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetBinaryTypeA(jitter):
    kernel32_GetBinaryType(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetBinaryTypeW(jitter):
    kernel32_GetBinaryType(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetCompressedFileSize(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetCompressedFileSize(LPCTSTR lpFileName, LPDWORD lpFileSizeHigh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "lpFileSizeHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCompressedFileSizeA(jitter):
    kernel32_GetCompressedFileSize(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetCompressedFileSizeW(jitter):
    kernel32_GetCompressedFileSize(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetCompressedFileSizeTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetCompressedFileSizeTransacted(LPCTSTR lpFileName, LPDWORD lpFileSizeHigh, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "lpFileSizeHigh", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCompressedFileSizeTransactedA(jitter):
    kernel32_GetCompressedFileSizeTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetCompressedFileSizeTransactedW(jitter):
    kernel32_GetCompressedFileSizeTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetFileAttributes(jitter, get_str, set_str):
    """"
    [Kernel32.dll] [FileAttributes] GetFileAttributes(LPCTSTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFileAttributesA(jitter):
    kernel32_GetFileAttributes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetFileAttributesW(jitter):
    kernel32_GetFileAttributes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetFileAttributesEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetFileAttributesEx(LPCTSTR lpFileName, GET_FILEEX_INFO_LEVELS fInfoLevelId, LPVOID lpFileInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "fInfoLevelId", "lpFileInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFileAttributesExA(jitter):
    kernel32_GetFileAttributesEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetFileAttributesExW(jitter):
    kernel32_GetFileAttributesEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetFileAttributesTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetFileAttributesTransacted(LPCTSTR lpFileName, GET_FILEEX_INFO_LEVELS fInfoLevelId, LPVOID lpFileInformation, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "fInfoLevelId", "lpFileInformation", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFileAttributesTransactedA(jitter):
    kernel32_GetFileAttributesTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetFileAttributesTransactedW(jitter):
    kernel32_GetFileAttributesTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetFileBandwidthReservation(jitter):
    """"
    [Kernel32.dll] BOOL GetFileBandwidthReservation(HANDLE hFile, LPDWORD lpPeriodMilliseconds, LPDWORD lpBytesPerPeriod, LPBOOL pDiscardable, LPDWORD lpTransferSize, LPDWORD lpNumOutstandingRequests)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpPeriodMilliseconds", "lpBytesPerPeriod", "pDiscardable", "lpTransferSize", "lpNumOutstandingRequests"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFileInformationByHandle(jitter):
    """"
    [Kernel32.dll] BOOL GetFileInformationByHandle(HANDLE hFile, LPBY_HANDLE_FILE_INFORMATION lpFileInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpFileInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFileInformationByHandleEx(jitter):
    """"
    [Kernel32.dll] BOOL GetFileInformationByHandleEx(HANDLE hFile, FILE_INFO_BY_HANDLE_CLASS FileInformationClass, LPVOID lpFileInformation, DWORD dwBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "FileInformationClass", "lpFileInformation", "dwBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFileSize(jitter):
    """"
    [Kernel32.dll] DWORD GetFileSize(HANDLE hFile, LPDWORD lpFileSizeHigh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpFileSizeHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFileSizeEx(jitter):
    """"
    [Kernel32.dll] BOOL GetFileSizeEx(HANDLE hFile, PLARGE_INTEGER lpFileSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpFileSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFileType(jitter):
    """"
    [Kernel32.dll] [FileType] GetFileType(HANDLE hFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFinalPathNameByHandle(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetFinalPathNameByHandle(HANDLE hFile, LPTSTR lpszFilePath, DWORD cchFilePath, [GetFinalPathNameByHandleFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpszFilePath", "cchFilePath", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFinalPathNameByHandleA(jitter):
    kernel32_GetFinalPathNameByHandle(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetFinalPathNameByHandleW(jitter):
    kernel32_GetFinalPathNameByHandle(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetFullPathName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetFullPathName(LPCTSTR lpFileName, DWORD nBufferLength, LPTSTR lpBuffer, LPTSTR* lpFilePart)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "nBufferLength", "lpBuffer", "lpFilePart"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFullPathNameA(jitter):
    kernel32_GetFullPathName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetFullPathNameW(jitter):
    kernel32_GetFullPathName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetFullPathNameTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetFullPathNameTransacted(LPCTSTR lpFileName, DWORD nBufferLength, LPTSTR lpBuffer, LPTSTR* lpFilePart, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "nBufferLength", "lpBuffer", "lpFilePart", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFullPathNameTransactedA(jitter):
    kernel32_GetFullPathNameTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetFullPathNameTransactedW(jitter):
    kernel32_GetFullPathNameTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetLongPathName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetLongPathName(LPCTSTR lpszShortPath, LPTSTR lpszLongPath, DWORD cchBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszShortPath", "lpszLongPath", "cchBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetLongPathNameA(jitter):
    kernel32_GetLongPathName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetLongPathNameW(jitter):
    kernel32_GetLongPathName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetLongPathNameTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetLongPathNameTransacted(LPCTSTR lpszShortPath, LPTSTR lpszLongPath, DWORD cchBuffer, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszShortPath", "lpszLongPath", "cchBuffer", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetLongPathNameTransactedA(jitter):
    kernel32_GetLongPathNameTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetLongPathNameTransactedW(jitter):
    kernel32_GetLongPathNameTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetShortPathName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetShortPathName(LPCTSTR lpszLongPath, LPTSTR lpszShortPath, DWORD cchBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszLongPath", "lpszShortPath", "cchBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetShortPathNameA(jitter):
    kernel32_GetShortPathName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetShortPathNameW(jitter):
    kernel32_GetShortPathName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetTempFileName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] UINT GetTempFileName(LPCTSTR lpPathName, LPCTSTR lpPrefixString, UINT uUnique, LPTSTR lpTempFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPathName", "lpPrefixString", "uUnique", "lpTempFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetTempFileNameA(jitter):
    kernel32_GetTempFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetTempFileNameW(jitter):
    kernel32_GetTempFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetTempPath(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetTempPath(DWORD nBufferLength, LPTSTR lpBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nBufferLength", "lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetTempPathA(jitter):
    kernel32_GetTempPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetTempPathW(jitter):
    kernel32_GetTempPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_MoveFile(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL MoveFile(LPCTSTR lpExistingFileName, LPCTSTR lpNewFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpExistingFileName", "lpNewFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_MoveFileA(jitter):
    kernel32_MoveFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_MoveFileW(jitter):
    kernel32_MoveFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_MoveFileEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL MoveFileEx(LPCTSTR lpExistingFileName, LPCTSTR lpNewFileName, [MoveFileFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpExistingFileName", "lpNewFileName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_MoveFileExA(jitter):
    kernel32_MoveFileEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_MoveFileExW(jitter):
    kernel32_MoveFileEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_MoveFileTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL MoveFileTransacted(LPCTSTR lpExistingFileName, LPCTSTR lpNewFileName, LPPROGRESS_ROUTINE lpProgressRoutine, LPVOID lpData, DWORD dwFlags, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpExistingFileName", "lpNewFileName", "lpProgressRoutine", "lpData", "dwFlags", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_MoveFileTransactedA(jitter):
    kernel32_MoveFileTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_MoveFileTransactedW(jitter):
    kernel32_MoveFileTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_MoveFileWithProgress(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL MoveFileWithProgress(LPCTSTR lpExistingFileName, LPCTSTR lpNewFileName, LPPROGRESS_ROUTINE lpProgressRoutine, LPVOID lpData, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpExistingFileName", "lpNewFileName", "lpProgressRoutine", "lpData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_MoveFileWithProgressA(jitter):
    kernel32_MoveFileWithProgress(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_MoveFileWithProgressW(jitter):
    kernel32_MoveFileWithProgress(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_OpenFile(jitter):
    """"
    [Kernel32.dll] HFILE OpenFile(LPCSTR lpFileName, LPOFSTRUCT lpReOpenBuff, [OpenFileFlags] uStyle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "lpReOpenBuff", "uStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OpenFileById(jitter):
    """"
    [Kernel32.dll] [FILE_HANDLE] OpenFileById(HANDLE hFile, LPFILE_ID_DESCRIPTOR lpFileID, [FILE_ACCESS_MASK] dwDesiredAccess, [FILE_SHARE_MODE] dwShareMode, LPSECURITY_ATTRIBUTES lpSecurityAttributes, [FlagsAndAttributes] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpFileID", "dwDesiredAccess", "dwShareMode", "lpSecurityAttributes", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReOpenFile(jitter):
    """"
    [Kernel32.dll] [FILE_HANDLE] ReOpenFile(HANDLE hOriginalFile, [FILE_ACCESS_MASK] dwDesiredAccess, [FILE_SHARE_MODE] dwShareMode, [FlagsAndAttributes] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hOriginalFile", "dwDesiredAccess", "dwShareMode", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReplaceFile(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL ReplaceFile(LPCTSTR lpReplacedFileName, LPCTSTR lpReplacementFileName, LPCTSTR lpBackupFileName, DWORD dwReplaceFlags, LPVOID lpExclude, LPVOID lpReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpReplacedFileName", "lpReplacementFileName", "lpBackupFileName", "dwReplaceFlags", "lpExclude", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReplaceFileA(jitter):
    kernel32_ReplaceFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_ReplaceFileW(jitter):
    kernel32_ReplaceFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SearchPath(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD SearchPath(LPCTSTR lpPath, LPCTSTR lpFileName, LPCTSTR lpExtension, DWORD nBufferLength, LPTSTR lpBuffer, LPTSTR* lpFilePart)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPath", "lpFileName", "lpExtension", "nBufferLength", "lpBuffer", "lpFilePart"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SearchPathA(jitter):
    kernel32_SearchPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SearchPathW(jitter):
    kernel32_SearchPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetFileApisToANSI(jitter):
    """"
    [Kernel32.dll] void SetFileApisToANSI()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetFileApisToOEM(jitter):
    """"
    [Kernel32.dll] void SetFileApisToOEM()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetFileAttributes(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetFileAttributes(LPCTSTR lpFileName, [FileAttributes] dwFileAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "dwFileAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetFileAttributesA(jitter):
    kernel32_SetFileAttributes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetFileAttributesW(jitter):
    kernel32_SetFileAttributes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetFileAttributesTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetFileAttributesTransacted(LPCTSTR lpFileName, [FileAttributes] dwFileAttributes, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "dwFileAttributes", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetFileAttributesTransactedA(jitter):
    kernel32_SetFileAttributesTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetFileAttributesTransactedW(jitter):
    kernel32_SetFileAttributesTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetFileBandwidthReservation(jitter):
    """"
    [Kernel32.dll] BOOL SetFileBandwidthReservation(HANDLE hFile, DWORD nPeriodMilliseconds, DWORD nBytesPerPeriod, BOOL bDiscardable, LPDWORD lpTransferSize, LPDWORD lpNumOutstandingRequests)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "nPeriodMilliseconds", "nBytesPerPeriod", "bDiscardable", "lpTransferSize", "lpNumOutstandingRequests"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetFileInformationByHandle(jitter):
    """"
    [Kernel32.dll] BOOL SetFileInformationByHandle(HANDLE hFile, FILE_INFO_BY_HANDLE_CLASS FileInformationClass, LPVOID lpFileInformation, DWORD dwBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "FileInformationClass", "lpFileInformation", "dwBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetFileShortName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetFileShortName(HANDLE hFile, LPCTSTR lpShortName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpShortName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetFileShortNameA(jitter):
    kernel32_SetFileShortName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetFileShortNameW(jitter):
    kernel32_SetFileShortName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetFileValidData(jitter):
    """"
    [Kernel32.dll] BOOL SetFileValidData(HANDLE hFile, LONGLONG ValidDataLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "ValidDataLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetSearchPathMode(jitter):
    """"
    [Kernel32.dll] BOOL SetSearchPathMode(DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CancelIo(jitter):
    """"
    [Kernel32.dll] BOOL CancelIo(HANDLE hFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CancelIoEx(jitter):
    """"
    [Kernel32.dll] BOOL CancelIoEx(HANDLE hFile, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CancelSynchronousIo(jitter):
    """"
    [Kernel32.dll] BOOL CancelSynchronousIo([ThreadHandle] hThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateIoCompletionPort(jitter):
    """"
    [Kernel32.dll] HANDLE CreateIoCompletionPort(HANDLE FileHandle, HANDLE ExistingCompletionPort, ULONG_PTR CompletionKey, DWORD NumberOfConcurrentThreads)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "ExistingCompletionPort", "CompletionKey", "NumberOfConcurrentThreads"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FlushFileBuffers(jitter):
    """"
    [Kernel32.dll] BOOL FlushFileBuffers(HANDLE hFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetQueuedCompletionStatus(jitter):
    """"
    [Kernel32.dll] BOOL GetQueuedCompletionStatus(HANDLE CompletionPort, LPDWORD lpNumberOfBytes, PULONG_PTR lpCompletionKey, LPOVERLAPPED* lpOverlapped, [WaitTimeout] dwMilliseconds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CompletionPort", "lpNumberOfBytes", "lpCompletionKey", "lpOverlapped", "dwMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetQueuedCompletionStatusEx(jitter):
    """"
    [Kernel32.dll] BOOL GetQueuedCompletionStatusEx(HANDLE CompletionPort, LPOVERLAPPED_ENTRY lpCompletionPortEntries, ULONG ulCount, PULONG ulNumEntriesRemoved, [WaitTimeout] dwMilliseconds, BOOL fAlertable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CompletionPort", "lpCompletionPortEntries", "ulCount", "ulNumEntriesRemoved", "dwMilliseconds", "fAlertable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LockFile(jitter):
    """"
    [Kernel32.dll] BOOL LockFile(HANDLE hFile, DWORD dwFileOffsetLow, DWORD dwFileOffsetHigh, DWORD nNumberOfBytesToLockLow, DWORD nNumberOfBytesToLockHigh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "dwFileOffsetLow", "dwFileOffsetHigh", "nNumberOfBytesToLockLow", "nNumberOfBytesToLockHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LockFileEx(jitter):
    """"
    [Kernel32.dll] BOOL LockFileEx(HANDLE hFile, [LockFileFlags] dwFlags, DWORD dwReserved, DWORD nNumberOfBytesToLockLow, DWORD nNumberOfBytesToLockHigh, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "dwFlags", "dwReserved", "nNumberOfBytesToLockLow", "nNumberOfBytesToLockHigh", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PostQueuedCompletionStatus(jitter):
    """"
    [Kernel32.dll] BOOL PostQueuedCompletionStatus(HANDLE CompletionPort, DWORD dwNumberOfBytesTransferred, ULONG_PTR dwCompletionKey, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CompletionPort", "dwNumberOfBytesTransferred", "dwCompletionKey", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReadFile(jitter):
    """"
    [Kernel32.dll] BOOL ReadFile(HANDLE hFile, LPVOID lpBuffer, DWORD nNumberOfBytesToRead, LPDWORD lpNumberOfBytesRead, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffer", "nNumberOfBytesToRead", "lpNumberOfBytesRead", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReadFileEx(jitter):
    """"
    [Kernel32.dll] BOOL ReadFileEx(HANDLE hFile, LPVOID lpBuffer, DWORD nNumberOfBytesToRead, LPOVERLAPPED lpOverlapped, LPOVERLAPPED_COMPLETION_ROUTINE lpCompletionRoutine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffer", "nNumberOfBytesToRead", "lpOverlapped", "lpCompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReadFileScatter(jitter):
    """"
    [Kernel32.dll] BOOL ReadFileScatter(HANDLE hFile, FILE_SEGMENT_ELEMENT[] aSegmentArray, DWORD nNumberOfBytesToRead, LPDWORD lpReserved, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "aSegmentArray", "nNumberOfBytesToRead", "lpReserved", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetEndOfFile(jitter):
    """"
    [Kernel32.dll] BOOL SetEndOfFile(HANDLE hFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetFileCompletionNotificationModes(jitter):
    """"
    [Kernel32.dll] BOOL SetFileCompletionNotificationModes(HANDLE FileHandle, UCHAR Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetFileIoOverlappedRange(jitter):
    """"
    [Kernel32.dll] BOOL SetFileIoOverlappedRange(HANDLE FileHandle, PUCHAR OverlappedRangeStart, ULONG Length)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "OverlappedRangeStart", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetFilePointer(jitter):
    """"
    [Kernel32.dll] DWORD SetFilePointer(HANDLE hFile, LONG lDistanceToMove, PLONG lpDistanceToMoveHigh, [MoveMethodEnum] dwMoveMethod)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lDistanceToMove", "lpDistanceToMoveHigh", "dwMoveMethod"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetFilePointerEx(jitter):
    """"
    [Kernel32.dll] BOOL SetFilePointerEx(HANDLE hFile, LARGE_INTEGER liDistanceToMove, PLARGE_INTEGER lpNewFilePointer, [MoveMethodEnum] dwMoveMethod)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "liDistanceToMove", "lpNewFilePointer", "dwMoveMethod"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_UnlockFile(jitter):
    """"
    [Kernel32.dll] BOOL UnlockFile(HANDLE hFile, DWORD dwFileOffsetLow, DWORD dwFileOffsetHigh, DWORD nNumberOfBytesToUnlockLow, DWORD nNumberOfBytesToUnlockHigh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "dwFileOffsetLow", "dwFileOffsetHigh", "nNumberOfBytesToUnlockLow", "nNumberOfBytesToUnlockHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_UnlockFileEx(jitter):
    """"
    [Kernel32.dll] BOOL UnlockFileEx(HANDLE hFile, DWORD dwReserved, DWORD nNumberOfBytesToUnlockLow, DWORD nNumberOfBytesToUnlockHigh, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "dwReserved", "nNumberOfBytesToUnlockLow", "nNumberOfBytesToUnlockHigh", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WriteFile(jitter):
    """"
    [Kernel32.dll] BOOL WriteFile(HANDLE hFile, LPCVOID lpBuffer, DWORD nNumberOfBytesToWrite, LPDWORD lpNumberOfBytesWritten, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffer", "nNumberOfBytesToWrite", "lpNumberOfBytesWritten", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WriteFileEx(jitter):
    """"
    [Kernel32.dll] BOOL WriteFileEx(HANDLE hFile, LPCVOID lpBuffer, DWORD nNumberOfBytesToWrite, LPOVERLAPPED lpOverlapped, LPOVERLAPPED_COMPLETION_ROUTINE lpCompletionRoutine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffer", "nNumberOfBytesToWrite", "lpOverlapped", "lpCompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WriteFileGather(jitter):
    """"
    [Kernel32.dll] BOOL WriteFileGather(HANDLE hFile, FILE_SEGMENT_ELEMENT[] aSegmentArray, DWORD nNumberOfBytesToWrite, LPDWORD lpReserved, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "aSegmentArray", "nNumberOfBytesToWrite", "lpReserved", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Wow64DisableWow64FsRedirection(jitter):
    """"
    [Kernel32.dll] BOOL Wow64DisableWow64FsRedirection(PVOID* OldValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["OldValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Wow64EnableWow64FsRedirection(jitter):
    """"
    [Kernel32.dll] BOOLEAN Wow64EnableWow64FsRedirection(BOOLEAN Wow64FsEnableRedirection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Wow64FsEnableRedirection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Wow64RevertWow64FsRedirection(jitter):
    """"
    [Kernel32.dll] BOOL Wow64RevertWow64FsRedirection(PVOID OldValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["OldValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AddSecureMemoryCacheCallback(jitter):
    """"
    [Kernel32.dll] BOOL AddSecureMemoryCacheCallback(PSECURE_MEMORY_CACHE_CALLBACK pfnCallBack)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfnCallBack"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateMemoryResourceNotification(jitter):
    """"
    [Kernel32.dll] HANDLE CreateMemoryResourceNotification(MEMORY_RESOURCE_NOTIFICATION_TYPE NotificationType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["NotificationType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetLargePageMinimum(jitter):
    """"
    [Kernel32.dll] SIZE_T GetLargePageMinimum()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPhysicallyInstalledSystemMemory(jitter):
    """"
    [Kernel32.dll] BOOL GetPhysicallyInstalledSystemMemory(PULONGLONG TotalMemoryInKilobytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TotalMemoryInKilobytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemFileCacheSize(jitter):
    """"
    [Kernel32.dll] BOOL GetSystemFileCacheSize(PSIZE_T lpMinimumFileCacheSize, PSIZE_T lpMaximumFileCacheSize, PDWORD lpFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMinimumFileCacheSize", "lpMaximumFileCacheSize", "lpFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetWriteWatch(jitter):
    """"
    [Kernel32.dll] UINT GetWriteWatch(DWORD dwFlags, PVOID lpBaseAddress, SIZE_T dwRegionSize, PVOID* lpAddresses, PULONG_PTR lpdwCount, PULONG lpdwGranularity)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpBaseAddress", "dwRegionSize", "lpAddresses", "lpdwCount", "lpdwGranularity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalMemoryStatusEx(jitter):
    """"
    [Kernel32.dll] BOOL GlobalMemoryStatusEx(LPMEMORYSTATUSEX lpBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryMemoryResourceNotification(jitter):
    """"
    [Kernel32.dll] BOOL QueryMemoryResourceNotification(HANDLE ResourceNotificationHandle, PBOOL ResourceState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ResourceNotificationHandle", "ResourceState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RemoveSecureMemoryCacheCallback(jitter):
    """"
    [Kernel32.dll] BOOL RemoveSecureMemoryCacheCallback(PSECURE_MEMORY_CACHE_CALLBACK pfnCallBack)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfnCallBack"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ResetWriteWatch(jitter):
    """"
    [Kernel32.dll] UINT ResetWriteWatch(LPVOID lpBaseAddress, SIZE_T dwRegionSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBaseAddress", "dwRegionSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetSystemFileCacheSize(jitter):
    """"
    [Kernel32.dll] BOOL SetSystemFileCacheSize(SIZE_T MinimumFileCacheSize, SIZE_T MaximumFileCacheSize, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["MinimumFileCacheSize", "MaximumFileCacheSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessDEPPolicy(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessDEPPolicy([ProcessHandle] hProcess, LPDWORD lpFlags, PBOOL lpPermanent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpFlags", "lpPermanent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemDEPPolicy(jitter):
    """"
    [Kernel32.dll] DEP_SYSTEM_POLICY_TYPE GetSystemDEPPolicy()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetProcessDEPPolicy(jitter):
    """"
    [Kernel32.dll] BOOL SetProcessDEPPolicy(DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateFileMapping(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateFileMapping([FILE_HANDLE] hFile, LPSECURITY_ATTRIBUTES lpAttributes, [MemoryProtection] flProtect, DWORD dwMaximumSizeHigh, DWORD dwMaximumSizeLow, LPCTSTR lpName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpAttributes", "flProtect", "dwMaximumSizeHigh", "dwMaximumSizeLow", "lpName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateFileMappingA(jitter):
    kernel32_CreateFileMapping(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateFileMappingW(jitter):
    kernel32_CreateFileMapping(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateFileMappingFromApp(jitter):
    """"
    [Kernel32.dll] HANDLE CreateFileMappingFromApp(HANDLE hFile, PSECURITY_ATTRIBUTES SecurityAttributes, ULONG PageProtection, ULONG64 MaximumSize, PCWSTR Name)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "SecurityAttributes", "PageProtection", "MaximumSize", "Name"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateFileMappingNuma(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateFileMappingNuma([FILE_HANDLE] hFile, LPSECURITY_ATTRIBUTES lpFileMappingAttributes, [MemoryProtection] flProtect, DWORD dwMaximumSizeHigh, DWORD dwMaximumSizeLow, LPCTSTR lpName, DWORD nndPreferred)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpFileMappingAttributes", "flProtect", "dwMaximumSizeHigh", "dwMaximumSizeLow", "lpName", "nndPreferred"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateFileMappingNumaA(jitter):
    kernel32_CreateFileMappingNuma(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateFileMappingNumaW(jitter):
    kernel32_CreateFileMappingNuma(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FlushViewOfFile(jitter):
    """"
    [Kernel32.dll] BOOL FlushViewOfFile(LPCVOID lpBaseAddress, SIZE_T dwNumberOfBytesToFlush)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBaseAddress", "dwNumberOfBytesToFlush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_MapViewOfFile(jitter):
    """"
    [Kernel32.dll] LPVOID MapViewOfFile(HANDLE hFileMappingObject, [MapAccessFlags] dwDesiredAccess, DWORD dwFileOffsetHigh, DWORD dwFileOffsetLow, SIZE_T dwNumberOfBytesToMap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFileMappingObject", "dwDesiredAccess", "dwFileOffsetHigh", "dwFileOffsetLow", "dwNumberOfBytesToMap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_MapViewOfFileEx(jitter):
    """"
    [Kernel32.dll] LPVOID MapViewOfFileEx(HANDLE hFileMappingObject, [MapAccessFlags] dwDesiredAccess, DWORD dwFileOffsetHigh, DWORD dwFileOffsetLow, SIZE_T dwNumberOfBytesToMap, LPVOID lpBaseAddress)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFileMappingObject", "dwDesiredAccess", "dwFileOffsetHigh", "dwFileOffsetLow", "dwNumberOfBytesToMap", "lpBaseAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_MapViewOfFileExNuma(jitter):
    """"
    [Kernel32.dll] LPVOID MapViewOfFileExNuma(HANDLE hFileMappingObject, DWORD dwDesiredAccess, DWORD dwFileOffsetHigh, DWORD dwFileOffsetLow, SIZE_T dwNumberOfBytesToMap, LPVOID lpBaseAddress, DWORD nndPreferred)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFileMappingObject", "dwDesiredAccess", "dwFileOffsetHigh", "dwFileOffsetLow", "dwNumberOfBytesToMap", "lpBaseAddress", "nndPreferred"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_MapViewOfFileFromApp(jitter):
    """"
    [Kernel32.dll] PVOID MapViewOfFileFromApp(HANDLE hFileMappingObject, ULONG DesiredAccess, ULONG64 FileOffset, SIZE_T NumberOfBytesToMap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFileMappingObject", "DesiredAccess", "FileOffset", "NumberOfBytesToMap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OpenFileMapping(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE OpenFileMapping([MapAccessFlags] dwDesiredAccess, BOOL bInheritHandle, LPCTSTR lpName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDesiredAccess", "bInheritHandle", "lpName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OpenFileMappingA(jitter):
    kernel32_OpenFileMapping(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_OpenFileMappingW(jitter):
    kernel32_OpenFileMapping(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_UnmapViewOfFile(jitter):
    """"
    [Kernel32.dll] BOOL UnmapViewOfFile(LPCVOID lpBaseAddress)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBaseAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AllocateUserPhysicalPages(jitter):
    """"
    [Kernel32.dll] BOOL AllocateUserPhysicalPages([ProcessHandle] hProcess, PULONG_PTR NumberOfPages, PULONG_PTR UserPfnArray)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "NumberOfPages", "UserPfnArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FreeUserPhysicalPages(jitter):
    """"
    [Kernel32.dll] BOOL FreeUserPhysicalPages([ProcessHandle] hProcess, PULONG_PTR NumberOfPages, PULONG_PTR UserPfnArray)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "NumberOfPages", "UserPfnArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_MapUserPhysicalPages(jitter):
    """"
    [Kernel32.dll] BOOL MapUserPhysicalPages(PVOID lpAddress, ULONG_PTR NumberOfPages, PULONG_PTR UserPfnArray)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAddress", "NumberOfPages", "UserPfnArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_MapUserPhysicalPagesScatter(jitter):
    """"
    [Kernel32.dll] BOOL MapUserPhysicalPagesScatter(PVOID* VirtualAddresses, ULONG_PTR NumberOfPages, PULONG_PTR PageArray)
    """"
    ret_ad, args = jitter.func_args_stdcall(["VirtualAddresses", "NumberOfPages", "PageArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessHeap(jitter):
    """"
    [Kernel32.dll] HANDLE GetProcessHeap()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessHeaps(jitter):
    """"
    [Kernel32.dll] DWORD GetProcessHeaps(DWORD NumberOfHeaps, PHANDLE ProcessHeaps)
    """"
    ret_ad, args = jitter.func_args_stdcall(["NumberOfHeaps", "ProcessHeaps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapAlloc(jitter):
    """"
    [Kernel32.dll] LPVOID HeapAlloc(HANDLE hHeap, [HEAP_FLAGS] dwFlags, SIZE_T dwBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHeap", "dwFlags", "dwBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapCompact(jitter):
    """"
    [Kernel32.dll] SIZE_T HeapCompact(HANDLE hHeap, [HEAP_FLAGS] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHeap", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapCreate(jitter):
    """"
    [Kernel32.dll] HANDLE HeapCreate([HEAP_FLAGS] flOptions, SIZE_T dwInitialSize, SIZE_T dwMaximumSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["flOptions", "dwInitialSize", "dwMaximumSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapDestroy(jitter):
    """"
    [Kernel32.dll] BOOL HeapDestroy(HANDLE hHeap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHeap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapFree(jitter):
    """"
    [Kernel32.dll] BOOL HeapFree(HANDLE hHeap, [HEAP_FLAGS] dwFlags, LPVOID lpMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHeap", "dwFlags", "lpMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapLock(jitter):
    """"
    [Kernel32.dll] BOOL HeapLock(HANDLE hHeap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHeap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapQueryInformation(jitter):
    """"
    [Kernel32.dll] BOOL HeapQueryInformation(HANDLE HeapHandle, HEAP_INFORMATION_CLASS HeapInformationClass, PVOID HeapInformation, SIZE_T HeapInformationLength, PSIZE_T ReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "HeapInformationClass", "HeapInformation", "HeapInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapReAlloc(jitter):
    """"
    [Kernel32.dll] LPVOID HeapReAlloc(HANDLE hHeap, [HEAP_FLAGS] dwFlags, LPVOID lpMem, SIZE_T dwBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHeap", "dwFlags", "lpMem", "dwBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapSetInformation(jitter):
    """"
    [Kernel32.dll] BOOL HeapSetInformation(HANDLE HeapHandle, HEAP_INFORMATION_CLASS HeapInformationClass, PVOID HeapInformation, SIZE_T HeapInformationLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "HeapInformationClass", "HeapInformation", "HeapInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapSize(jitter):
    """"
    [Kernel32.dll] SIZE_T HeapSize(HANDLE hHeap, [HEAP_FLAGS] dwFlags, LPCVOID lpMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHeap", "dwFlags", "lpMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapUnlock(jitter):
    """"
    [Kernel32.dll] BOOL HeapUnlock(HANDLE hHeap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHeap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapValidate(jitter):
    """"
    [Kernel32.dll] BOOL HeapValidate(HANDLE hHeap, [HEAP_FLAGS] dwFlags, LPCVOID lpMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHeap", "dwFlags", "lpMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapWalk(jitter):
    """"
    [Kernel32.dll] BOOL HeapWalk(HANDLE hHeap, LPPROCESS_HEAP_ENTRY lpEntry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHeap", "lpEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_HeapSummary(jitter):
    """"
    [Kernel32.dll] BOOL HeapSummary(HANDLE hHeap, DWORD dwFlags, LPHEAP_SUMMARY lpSummary)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHeap", "dwFlags", "lpSummary"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PrefetchVirtualMemory(jitter):
    """"
    [Kernel32.dll] BOOL PrefetchVirtualMemory(HANDLE hProcess, ULONG_PTR NumberOfEntries, PWIN32_MEMORY_RANGE_ENTRY VirtualAddresses, ULONG Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "NumberOfEntries", "VirtualAddresses", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VirtualAlloc(jitter):
    """"
    [Kernel32.dll] LPVOID VirtualAlloc(LPVOID lpAddress, SIZE_T dwSize, [MemoryAllocationFlags] flAllocationType, [MemoryProtection] flProtect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAddress", "dwSize", "flAllocationType", "flProtect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VirtualAllocEx(jitter):
    """"
    [Kernel32.dll] LPVOID VirtualAllocEx([ProcessHandle] hProcess, LPVOID lpAddress, SIZE_T dwSize, [MemoryAllocationFlags] flAllocationType, [MemoryProtection] flProtect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpAddress", "dwSize", "flAllocationType", "flProtect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VirtualAllocExNuma(jitter):
    """"
    [Kernel32.dll] LPVOID VirtualAllocExNuma([ProcessHandle] hProcess, LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, [MemoryProtection] flProtect, DWORD nndPreferred)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpAddress", "dwSize", "flAllocationType", "flProtect", "nndPreferred"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VirtualFree(jitter):
    """"
    [Kernel32.dll] BOOL VirtualFree(LPVOID lpAddress, SIZE_T dwSize, [MemoryAllocationFlags] dwFreeType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAddress", "dwSize", "dwFreeType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VirtualFreeEx(jitter):
    """"
    [Kernel32.dll] BOOL VirtualFreeEx([ProcessHandle] hProcess, LPVOID lpAddress, SIZE_T dwSize, [MemoryAllocationFlags] dwFreeType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpAddress", "dwSize", "dwFreeType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VirtualLock(jitter):
    """"
    [Kernel32.dll] BOOL VirtualLock(LPVOID lpAddress, SIZE_T dwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAddress", "dwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VirtualProtect(jitter):
    """"
    [Kernel32.dll] BOOL VirtualProtect(LPVOID lpAddress, SIZE_T dwSize, [MemoryProtection] flNewProtect, [MemoryProtection*] lpflOldProtect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAddress", "dwSize", "flNewProtect", "lpflOldProtect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VirtualProtectEx(jitter):
    """"
    [Kernel32.dll] BOOL VirtualProtectEx([ProcessHandle] hProcess, LPVOID lpAddress, SIZE_T dwSize, [MemoryProtection] flNewProtect, [MemoryProtection*] lpflOldProtect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpAddress", "dwSize", "flNewProtect", "lpflOldProtect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VirtualQuery(jitter):
    """"
    [Kernel32.dll] SIZE_T VirtualQuery(LPCVOID lpAddress, PMEMORY_BASIC_INFORMATION lpBuffer, SIZE_T dwLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAddress", "lpBuffer", "dwLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VirtualQueryEx(jitter):
    """"
    [Kernel32.dll] SIZE_T VirtualQueryEx([ProcessHandle] hProcess, LPCVOID lpAddress, PMEMORY_BASIC_INFORMATION lpBuffer, SIZE_T dwLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpAddress", "lpBuffer", "dwLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VirtualUnlock(jitter):
    """"
    [Kernel32.dll] BOOL VirtualUnlock(LPVOID lpAddress, SIZE_T dwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAddress", "dwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalAlloc(jitter):
    """"
    [Kernel32.dll] HGLOBAL GlobalAlloc([GlobalMemoryFlag] uFlags, SIZE_T dwBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uFlags", "dwBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LocalAlloc(jitter):
    """"
    [Kernel32.dll] HLOCAL LocalAlloc([LocalMemoryFlag] uFlags, SIZE_T uBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uFlags", "uBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalFlags(jitter):
    """"
    [Kernel32.dll] UINT GlobalFlags(HGLOBAL hMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LocalFlags(jitter):
    """"
    [Kernel32.dll] UINT LocalFlags(HLOCAL hMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalFree(jitter):
    """"
    [Kernel32.dll] HGLOBAL GlobalFree(HGLOBAL hMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LocalFree(jitter):
    """"
    [Kernel32.dll] HLOCAL LocalFree(HLOCAL hMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalHandle(jitter):
    """"
    [Kernel32.dll] HGLOBAL GlobalHandle(LPCVOID pMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LocalHandle(jitter):
    """"
    [Kernel32.dll] HLOCAL LocalHandle(LPCVOID pMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalLock(jitter):
    """"
    [Kernel32.dll] LPVOID GlobalLock(HGLOBAL hMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LocalLock(jitter):
    """"
    [Kernel32.dll] LPVOID LocalLock(HLOCAL hMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalReAlloc(jitter):
    """"
    [Kernel32.dll] HGLOBAL GlobalReAlloc(HGLOBAL hMem, SIZE_T dwBytes, [GlobalMemoryFlag] uFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMem", "dwBytes", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LocalReAlloc(jitter):
    """"
    [Kernel32.dll] HLOCAL LocalReAlloc(HLOCAL hMem, SIZE_T uBytes, [LocalMemoryFlag] uFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMem", "uBytes", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalSize(jitter):
    """"
    [Kernel32.dll] SIZE_T GlobalSize(HGLOBAL hMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LocalSize(jitter):
    """"
    [Kernel32.dll] UINT LocalSize(HLOCAL hMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalUnlock(jitter):
    """"
    [Kernel32.dll] BOOL GlobalUnlock(HGLOBAL hMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LocalUnlock(jitter):
    """"
    [Kernel32.dll] BOOL LocalUnlock(HLOCAL hMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetMemoryErrorHandlingCapabilities(jitter):
    """"
    [Kernel32.dll] BOOL GetMemoryErrorHandlingCapabilities(PULONG Capabilities)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Capabilities"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RegisterBadMemoryNotification(jitter):
    """"
    [Kernel32.dll] PVOID RegisterBadMemoryNotification(PBAD_MEMORY_CALLBACK_ROUTINE Callback)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Callback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_UnregisterBadMemoryNotification(jitter):
    """"
    [Kernel32.dll] BOOL UnregisterBadMemoryNotification(PVOID RegistrationHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegistrationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsBadCodePtr(jitter):
    """"
    [Kernel32.dll] BOOL IsBadCodePtr(FARPROC lpfn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpfn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsBadReadPtr(jitter):
    """"
    [Kernel32.dll] BOOL IsBadReadPtr(const VOID* lp, UINT_PTR ucb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lp", "ucb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsBadStringPtr(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL IsBadStringPtr(LPCTSTR lpsz, UINT_PTR ucchMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpsz", "ucchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsBadStringPtrA(jitter):
    kernel32_IsBadStringPtr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_IsBadStringPtrW(jitter):
    kernel32_IsBadStringPtr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_IsBadWritePtr(jitter):
    """"
    [Kernel32.dll] BOOL IsBadWritePtr(LPVOID lp, UINT_PTR ucb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lp", "ucb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalMemoryStatus(jitter):
    """"
    [Kernel32.dll] void GlobalMemoryStatus(LPMEMORYSTATUS lpBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateProcess(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL CreateProcess(LPCTSTR lpApplicationName, LPTSTR lpCommandLine, LPSECURITY_ATTRIBUTES lpProcessAttributes, LPSECURITY_ATTRIBUTES lpThreadAttributes, BOOL bInheritHandles, [CreateProcessFlags] dwCreationFlags, LPVOID lpEnvironment, LPCTSTR lpCurrentDirectory, LPSTARTUPINFO lpStartupInfo, LPPROCESS_INFORMATION lpProcessInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpApplicationName", "lpCommandLine", "lpProcessAttributes", "lpThreadAttributes", "bInheritHandles", "dwCreationFlags", "lpEnvironment", "lpCurrentDirectory", "lpStartupInfo", "lpProcessInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateProcessA(jitter):
    kernel32_CreateProcess(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateProcessW(jitter):
    kernel32_CreateProcess(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_ExitProcess(jitter):
    """"
    [Kernel32.dll] VOID ExitProcess(UINT uExitCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uExitCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FlushProcessWriteBuffers(jitter):
    """"
    [Kernel32.dll] VOID FlushProcessWriteBuffers()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FreeEnvironmentStrings(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL FreeEnvironmentStrings(LPTCH lpszEnvironmentBlock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszEnvironmentBlock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FreeEnvironmentStringsA(jitter):
    kernel32_FreeEnvironmentStrings(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FreeEnvironmentStringsW(jitter):
    kernel32_FreeEnvironmentStrings(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetCommandLine(jitter, get_str, set_str):
    """"
    [Kernel32.dll] LPTSTR GetCommandLine()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCommandLineA(jitter):
    kernel32_GetCommandLine(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetCommandLineW(jitter):
    kernel32_GetCommandLine(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetCurrentProcess(jitter):
    """"
    [Kernel32.dll] [ProcessHandle] GetCurrentProcess()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentProcessId(jitter):
    """"
    [Kernel32.dll] DWORD GetCurrentProcessId()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetEnvironmentStrings(jitter):
    """"
    [Kernel32.dll] LPCH GetEnvironmentStrings()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetEnvironmentStrings(jitter, get_str, set_str):
    """"
    [Kernel32.dll] LPTCH GetEnvironmentStrings()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetEnvironmentStringsA(jitter):
    kernel32_GetEnvironmentStrings(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetEnvironmentStringsW(jitter):
    kernel32_GetEnvironmentStrings(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetEnvironmentVariable(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetEnvironmentVariable(LPCTSTR lpName, LPTSTR lpBuffer, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpName", "lpBuffer", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetEnvironmentVariableA(jitter):
    kernel32_GetEnvironmentVariable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetEnvironmentVariableW(jitter):
    kernel32_GetEnvironmentVariable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetExitCodeProcess(jitter):
    """"
    [Kernel32.dll] BOOL GetExitCodeProcess([ProcessHandle] hProcess, LPDWORD lpExitCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpExitCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPriorityClass(jitter):
    """"
    [Kernel32.dll] DWORD GetPriorityClass([ProcessHandle] hProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessAffinityMask(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessAffinityMask([ProcessHandle] hProcess, PDWORD_PTR lpProcessAffinityMask, PDWORD_PTR lpSystemAffinityMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpProcessAffinityMask", "lpSystemAffinityMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessGroupAffinity(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessGroupAffinity([ProcessHandle] hProcess, PUSHORT GroupCount, PUSHORT GroupArray)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "GroupCount", "GroupArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessHandleCount(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessHandleCount([ProcessHandle] hProcess, PDWORD pdwHandleCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "pdwHandleCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessId(jitter):
    """"
    [Kernel32.dll] DWORD GetProcessId(HANDLE Process)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Process"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessIdOfThread(jitter):
    """"
    [Kernel32.dll] DWORD GetProcessIdOfThread(HANDLE Thread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Thread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessInformation(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessInformation(HANDLE hProcess, PROCESS_INFORMATION_CLASS ProcessInformationClass, LPVOID ProcessInformation, DWORD ProcessInformationSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ProcessInformationClass", "ProcessInformation", "ProcessInformationSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessIoCounters(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessIoCounters([ProcessHandle] hProcess, PIO_COUNTERS lpIoCounters)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpIoCounters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessMitigationPolicy(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessMitigationPolicy(HANDLE hProcess, PROCESS_MITIGATION_POLICY MitigationPolicy, PVOID lpBuffer, SIZE_T dwLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "MitigationPolicy", "lpBuffer", "dwLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessPriorityBoost(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessPriorityBoost([ProcessHandle] hProcess, PBOOL pDisablePriorityBoost)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "pDisablePriorityBoost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessShutdownParameters(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessShutdownParameters(LPDWORD lpdwLevel, LPDWORD lpdwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpdwLevel", "lpdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessTimes(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessTimes([ProcessHandle] hProcess, LPFILETIME lpCreationTime, LPFILETIME lpExitTime, LPFILETIME lpKernelTime, LPFILETIME lpUserTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpCreationTime", "lpExitTime", "lpKernelTime", "lpUserTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessVersion(jitter):
    """"
    [Kernel32.dll] DWORD GetProcessVersion(DWORD ProcessId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessWorkingSetSize(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessWorkingSetSize([ProcessHandle] hProcess, PSIZE_T lpMinimumWorkingSetSize, PSIZE_T lpMaximumWorkingSetSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpMinimumWorkingSetSize", "lpMaximumWorkingSetSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessWorkingSetSizeEx(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessWorkingSetSizeEx([ProcessHandle] hProcess, PSIZE_T lpMinimumWorkingSetSize, PSIZE_T lpMaximumWorkingSetSize, PDWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpMinimumWorkingSetSize", "lpMaximumWorkingSetSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessorSystemCycleTime(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessorSystemCycleTime(USHORT Group, PSYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION Buffer, PDWORD ReturnedLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Group", "Buffer", "ReturnedLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetStartupInfo(jitter, get_str, set_str):
    """"
    [Kernel32.dll] VOID GetStartupInfo(LPSTARTUPINFO lpStartupInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpStartupInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetStartupInfoA(jitter):
    kernel32_GetStartupInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetStartupInfoW(jitter):
    kernel32_GetStartupInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_NeedCurrentDirectoryForExePath(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL NeedCurrentDirectoryForExePath(LPCTSTR ExeName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_NeedCurrentDirectoryForExePathA(jitter):
    kernel32_NeedCurrentDirectoryForExePath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_NeedCurrentDirectoryForExePathW(jitter):
    kernel32_NeedCurrentDirectoryForExePath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_OpenProcess(jitter):
    """"
    [Kernel32.dll] HANDLE OpenProcess([PROCESS_ACCESS_MASK] dwDesiredAccess, BOOL bInheritHandle, DWORD dwProcessId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDesiredAccess", "bInheritHandle", "dwProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryFullProcessImageName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL QueryFullProcessImageName([ProcessHandle] hProcess, [QueryFullProcessImageNameFlags] dwFlags, LPTSTR lpExeName, PDWORD lpdwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwFlags", "lpExeName", "lpdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryFullProcessImageNameA(jitter):
    kernel32_QueryFullProcessImageName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_QueryFullProcessImageNameW(jitter):
    kernel32_QueryFullProcessImageName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_QueryProcessAffinityUpdateMode(jitter):
    """"
    [Kernel32.dll] BOOL QueryProcessAffinityUpdateMode(HANDLE ProcessHandle, DWORD lpdwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "lpdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryProcessCycleTime(jitter):
    """"
    [Kernel32.dll] BOOL QueryProcessCycleTime(HANDLE ProcessHandle, PULONG64 CycleTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "CycleTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetEnvironmentVariable(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetEnvironmentVariable(LPCTSTR lpName, LPCTSTR lpValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpName", "lpValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetEnvironmentVariableA(jitter):
    kernel32_SetEnvironmentVariable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetEnvironmentVariableW(jitter):
    kernel32_SetEnvironmentVariable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetPriorityClass(jitter):
    """"
    [Kernel32.dll] BOOL SetPriorityClass([ProcessHandle] hProcess, [PriorityClass] dwPriorityClass)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwPriorityClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetProcessAffinityMask(jitter):
    """"
    [Kernel32.dll] BOOL SetProcessAffinityMask([ProcessHandle] hProcess, DWORD_PTR dwProcessAffinityMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwProcessAffinityMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetProcessAffinityUpdateMode(jitter):
    """"
    [Kernel32.dll] BOOL SetProcessAffinityUpdateMode(HANDLE ProcessHandle, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetProcessInformation(jitter):
    """"
    [Kernel32.dll] BOOL SetProcessInformation(HANDLE hProcess, PROCESS_INFORMATION_CLASS ProcessInformationClass, LPVOID ProcessInformation, DWORD ProcessInformationSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ProcessInformationClass", "ProcessInformation", "ProcessInformationSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetProcessMitigationPolicy(jitter):
    """"
    [Kernel32.dll] BOOL SetProcessMitigationPolicy(PROCESS_MITIGATION_POLICY MitigationPolicy, PVOID lpBuffer, SIZE_T dwLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["MitigationPolicy", "lpBuffer", "dwLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetProcessPriorityBoost(jitter):
    """"
    [Kernel32.dll] BOOL SetProcessPriorityBoost([ProcessHandle] hProcess, BOOL DisablePriorityBoost)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "DisablePriorityBoost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetProcessShutdownParameters(jitter):
    """"
    [Kernel32.dll] BOOL SetProcessShutdownParameters(DWORD dwLevel, [ProcessShutdownFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwLevel", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetProcessWorkingSetSize(jitter):
    """"
    [Kernel32.dll] BOOL SetProcessWorkingSetSize([ProcessHandle] hProcess, SIZE_T dwMinimumWorkingSetSize, SIZE_T dwMaximumWorkingSetSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwMinimumWorkingSetSize", "dwMaximumWorkingSetSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetProcessWorkingSetSizeEx(jitter):
    """"
    [Kernel32.dll] BOOL SetProcessWorkingSetSizeEx([ProcessHandle] hProcess, SIZE_T dwMinimumWorkingSetSize, SIZE_T dwMaximumWorkingSetSize, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwMinimumWorkingSetSize", "dwMaximumWorkingSetSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TerminateProcess(jitter):
    """"
    [Kernel32.dll] BOOL TerminateProcess([ProcessHandle] hProcess, UINT uExitCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "uExitCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateRemoteThread(jitter):
    """"
    [Kernel32.dll] HANDLE CreateRemoteThread([ProcessHandle] hProcess, LPSECURITY_ATTRIBUTES lpThreadAttributes, SIZE_T dwStackSize, LPTHREAD_START_ROUTINE lpStartAddress, LPVOID lpParameter, DWORD dwCreationFlags, LPDWORD lpThreadId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpThreadAttributes", "dwStackSize", "lpStartAddress", "lpParameter", "dwCreationFlags", "lpThreadId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateRemoteThreadEx(jitter):
    """"
    [Kernel32.dll] HANDLE CreateRemoteThreadEx([ProcessHandle] hProcess, LPSECURITY_ATTRIBUTES lpThreadAttributes, SIZE_T dwStackSize, LPTHREAD_START_ROUTINE lpStartAddress, LPVOID lpParameter, DWORD dwCreationFlags, LPPROC_THREAD_ATTRIBUTE_LIST lpAttributeList, LPDWORD lpThreadId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpThreadAttributes", "dwStackSize", "lpStartAddress", "lpParameter", "dwCreationFlags", "lpAttributeList", "lpThreadId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateThread(jitter):
    """"
    [Kernel32.dll] HANDLE CreateThread(LPSECURITY_ATTRIBUTES lpThreadAttributes, SIZE_T dwStackSize, LPTHREAD_START_ROUTINE lpStartAddress, LPVOID lpParameter, [ThreadCreationFlags] dwCreationFlags, LPDWORD lpThreadId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpThreadAttributes", "dwStackSize", "lpStartAddress", "lpParameter", "dwCreationFlags", "lpThreadId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ExitThread(jitter):
    """"
    [Kernel32.dll] VOID ExitThread(DWORD dwExitCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwExitCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentThread(jitter):
    """"
    [Kernel32.dll] [ThreadHandle] GetCurrentThread()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentThreadId(jitter):
    """"
    [Kernel32.dll] DWORD GetCurrentThreadId()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetExitCodeThread(jitter):
    """"
    [Kernel32.dll] BOOL GetExitCodeThread([ThreadHandle] hThread, LPDWORD lpExitCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "lpExitCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadGroupAffinity(jitter):
    """"
    [Kernel32.dll] BOOL GetThreadGroupAffinity([ThreadHandle] hThread, PGROUP_AFFINITY GroupAffinity)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "GroupAffinity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadId(jitter):
    """"
    [Kernel32.dll] DWORD GetThreadId(HANDLE Thread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Thread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadIdealProcessorEx(jitter):
    """"
    [Kernel32.dll] BOOL GetThreadIdealProcessorEx([ThreadHandle] hThread, PPROCESSOR_NUMBER lpIdealProcessor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "lpIdealProcessor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadInformation(jitter):
    """"
    [Kernel32.dll] BOOL GetThreadInformation([ThreadHandle] hThread, THREAD_INFORMATION_CLASS ThreadInformationClass, LPVOID ThreadInformation, DWORD ThreadInformationSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "ThreadInformationClass", "ThreadInformation", "ThreadInformationSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadIOPendingFlag(jitter):
    """"
    [Kernel32.dll] BOOL GetThreadIOPendingFlag([ThreadHandle] hThread, PBOOL lpIOIsPending)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "lpIOIsPending"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadPriority(jitter):
    """"
    [Kernel32.dll] [THREAD_PRIORITY] GetThreadPriority([ThreadHandle] hThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadPriorityBoost(jitter):
    """"
    [Kernel32.dll] BOOL GetThreadPriorityBoost([ThreadHandle] hThread, PBOOL pDisablePriorityBoost)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "pDisablePriorityBoost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadTimes(jitter):
    """"
    [Kernel32.dll] BOOL GetThreadTimes([ThreadHandle] hThread, LPFILETIME lpCreationTime, LPFILETIME lpExitTime, LPFILETIME lpKernelTime, LPFILETIME lpUserTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "lpCreationTime", "lpExitTime", "lpKernelTime", "lpUserTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OpenThread(jitter):
    """"
    [Kernel32.dll] HANDLE OpenThread([THREAD_ACCESS_MASK] dwDesiredAccess, BOOL bInheritHandle, DWORD dwThreadId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDesiredAccess", "bInheritHandle", "dwThreadId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryThreadCycleTime(jitter):
    """"
    [Kernel32.dll] BOOL QueryThreadCycleTime([ThreadHandle] ThreadHandle, PULONG64 CycleTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "CycleTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ResumeThread(jitter):
    """"
    [Kernel32.dll] DWORD ResumeThread([ThreadHandle] hThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadAffinityMask(jitter):
    """"
    [Kernel32.dll] DWORD_PTR SetThreadAffinityMask([ThreadHandle] hThread, DWORD_PTR dwThreadAffinityMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "dwThreadAffinityMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadGroupAffinity(jitter):
    """"
    [Kernel32.dll] BOOL SetThreadGroupAffinity([ThreadHandle] hThread, const GROUP_AFFINITY* GroupAffinity)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "GroupAffinity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadIdealProcessor(jitter):
    """"
    [Kernel32.dll] DWORD SetThreadIdealProcessor([ThreadHandle] hThread, DWORD dwIdealProcessor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "dwIdealProcessor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadIdealProcessorEx(jitter):
    """"
    [Kernel32.dll] BOOL SetThreadIdealProcessorEx([ThreadHandle] hThread, PPROCESSOR_NUMBER lpIdealProcessor, PPROCESSOR_NUMBER lpPreviousIdealProcessor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "lpIdealProcessor", "lpPreviousIdealProcessor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadInformation(jitter):
    """"
    [Kernel32.dll] BOOL SetThreadInformation([ThreadHandle] hThread, THREAD_INFORMATION_CLASS ThreadInformationClass, LPVOID ThreadInformation, DWORD ThreadInformationSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "ThreadInformationClass", "ThreadInformation", "ThreadInformationSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadPriority(jitter):
    """"
    [Kernel32.dll] BOOL SetThreadPriority([ThreadHandle] hThread, [THREAD_PRIORITY] nPriority)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "nPriority"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadPriorityBoost(jitter):
    """"
    [Kernel32.dll] BOOL SetThreadPriorityBoost([ThreadHandle] hThread, BOOL DisablePriorityBoost)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "DisablePriorityBoost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadStackGuarantee(jitter):
    """"
    [Kernel32.dll] BOOL SetThreadStackGuarantee(PULONG StackSizeInBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["StackSizeInBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Sleep(jitter):
    """"
    [Kernel32.dll] VOID Sleep([WaitTimeout] dwMilliseconds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SleepEx(jitter):
    """"
    [Kernel32.dll] DWORD SleepEx([WaitTimeout] dwMilliseconds, BOOL bAlertable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwMilliseconds", "bAlertable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SuspendThread(jitter):
    """"
    [Kernel32.dll] DWORD SuspendThread([ThreadHandle] hThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SwitchToThread(jitter):
    """"
    [Kernel32.dll] BOOL SwitchToThread()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TerminateThread(jitter):
    """"
    [Kernel32.dll] BOOL TerminateThread([ThreadHandle] hThread, DWORD dwExitCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread", "dwExitCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TlsAlloc(jitter):
    """"
    [Kernel32.dll] DWORD TlsAlloc()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TlsFree(jitter):
    """"
    [Kernel32.dll] BOOL TlsFree(DWORD dwTlsIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTlsIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TlsGetValue(jitter):
    """"
    [Kernel32.dll] LPVOID TlsGetValue(DWORD dwTlsIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTlsIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TlsSetValue(jitter):
    """"
    [Kernel32.dll] BOOL TlsSetValue(DWORD dwTlsIndex, LPVOID lpTlsValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTlsIndex", "lpTlsValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DeleteProcThreadAttributeList(jitter):
    """"
    [Kernel32.dll] VOID DeleteProcThreadAttributeList(LPPROC_THREAD_ATTRIBUTE_LIST lpAttributeList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAttributeList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitializeProcThreadAttributeList(jitter):
    """"
    [Kernel32.dll] BOOL InitializeProcThreadAttributeList(LPPROC_THREAD_ATTRIBUTE_LIST lpAttributeList, DWORD dwAttributeCount, DWORD dwFlags, PSIZE_T lpSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAttributeList", "dwAttributeCount", "dwFlags", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_UpdateProcThreadAttribute(jitter):
    """"
    [Kernel32.dll] BOOL UpdateProcThreadAttribute(LPPROC_THREAD_ATTRIBUTE_LIST lpAttributeList, DWORD dwFlags, [ProcThreadAttribute] Attribute, PVOID lpValue, SIZE_T cbSize, PVOID lpPreviousValue, PSIZE_T lpReturnSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAttributeList", "dwFlags", "Attribute", "lpValue", "cbSize", "lpPreviousValue", "lpReturnSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsWow64Process(jitter):
    """"
    [Kernel32.dll] BOOL IsWow64Process([ProcessHandle] hProcess, PBOOL Wow64Process)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Wow64Process"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Wow64SuspendThread(jitter):
    """"
    [Kernel32.dll] DWORD Wow64SuspendThread([ThreadHandle] hThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AssignProcessToJobObject(jitter):
    """"
    [Kernel32.dll] BOOL AssignProcessToJobObject(HANDLE hJob, [ProcessHandle] hProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hJob", "hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateJobObject(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateJobObject(LPSECURITY_ATTRIBUTES lpJobAttributes, LPCTSTR lpName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpJobAttributes", "lpName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateJobObjectA(jitter):
    kernel32_CreateJobObject(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateJobObjectW(jitter):
    kernel32_CreateJobObject(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_IsProcessInJob(jitter):
    """"
    [Kernel32.dll] BOOL IsProcessInJob(HANDLE ProcessHandle, HANDLE JobHandle, PBOOL Result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "JobHandle", "Result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OpenJobObject(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE OpenJobObject(DWORD dwDesiredAccess, BOOL bInheritHandles, LPCTSTR lpName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDesiredAccess", "bInheritHandles", "lpName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OpenJobObjectA(jitter):
    kernel32_OpenJobObject(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_OpenJobObjectW(jitter):
    kernel32_OpenJobObject(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_QueryInformationJobObject(jitter):
    """"
    [Kernel32.dll] BOOL QueryInformationJobObject(HANDLE hJob, JOBOBJECTINFOCLASS JobObjectInfoClass, LPVOID lpJobObjectInfo, DWORD cbJobObjectInfoLength, LPDWORD lpReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hJob", "JobObjectInfoClass", "lpJobObjectInfo", "cbJobObjectInfoLength", "lpReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetInformationJobObject(jitter):
    """"
    [Kernel32.dll] BOOL SetInformationJobObject(HANDLE hJob, JOBOBJECTINFOCLASS JobObjectInfoClass, LPVOID lpJobObjectInfo, DWORD cbJobObjectInfoLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hJob", "JobObjectInfoClass", "lpJobObjectInfo", "cbJobObjectInfoLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TerminateJobObject(jitter):
    """"
    [Kernel32.dll] BOOL TerminateJobObject(HANDLE hJob, UINT uExitCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hJob", "uExitCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CallbackMayRunLong(jitter):
    """"
    [Kernel32.dll] BOOL CallbackMayRunLong(PTP_CALLBACK_INSTANCE pci)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pci"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CancelThreadpoolIo(jitter):
    """"
    [Kernel32.dll] VOID CancelThreadpoolIo(PTP_IO pio)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pio"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CloseThreadpool(jitter):
    """"
    [Kernel32.dll] VOID CloseThreadpool(PTP_POOL ptpp)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ptpp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CloseThreadpoolCleanupGroup(jitter):
    """"
    [Kernel32.dll] VOID CloseThreadpoolCleanupGroup(PTP_CLEANUP_GROUP ptpcg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ptpcg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CloseThreadpoolCleanupGroupMembers(jitter):
    """"
    [Kernel32.dll] VOID CloseThreadpoolCleanupGroupMembers(PTP_CLEANUP_GROUP ptpcg, BOOL fCancelPendingCallbacks, PVOID pvCleanupContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ptpcg", "fCancelPendingCallbacks", "pvCleanupContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CloseThreadpoolIo(jitter):
    """"
    [Kernel32.dll] VOID CloseThreadpoolIo(PTP_IO pio)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pio"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CloseThreadpoolTimer(jitter):
    """"
    [Kernel32.dll] VOID CloseThreadpoolTimer(PTP_TIMER pti)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pti"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CloseThreadpoolWait(jitter):
    """"
    [Kernel32.dll] VOID CloseThreadpoolWait(PTP_WAIT pwa)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CloseThreadpoolWork(jitter):
    """"
    [Kernel32.dll] VOID CloseThreadpoolWork(PTP_WORK pwk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateThreadpool(jitter):
    """"
    [Kernel32.dll] PTP_POOL CreateThreadpool(PVOID reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateThreadpoolCleanupGroup(jitter):
    """"
    [Kernel32.dll] PTP_CLEANUP_GROUP CreateThreadpoolCleanupGroup()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateThreadpoolIo(jitter):
    """"
    [Kernel32.dll] PTP_IO CreateThreadpoolIo(HANDLE fl, PTP_WIN32_IO_CALLBACK pfnio, PVOID pv, PTP_CALLBACK_ENVIRON pcbe)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fl", "pfnio", "pv", "pcbe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateThreadpoolTimer(jitter):
    """"
    [Kernel32.dll] PTP_TIMER CreateThreadpoolTimer(PTP_TIMER_CALLBACK pfnti, PVOID pv, PTP_CALLBACK_ENVIRON pcbe)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfnti", "pv", "pcbe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateThreadpoolWait(jitter):
    """"
    [Kernel32.dll] PTP_WAIT CreateThreadpoolWait(PTP_WAIT_CALLBACK pfnwa, PVOID pv, PTP_CALLBACK_ENVIRON pcbe)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfnwa", "pv", "pcbe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateThreadpoolWork(jitter):
    """"
    [Kernel32.dll] PTP_WORK CreateThreadpoolWork(PTP_WORK_CALLBACK pfnwk, PVOID pv, PTP_CALLBACK_ENVIRON pcbe)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfnwk", "pv", "pcbe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DisassociateCurrentThreadFromCallback(jitter):
    """"
    [Kernel32.dll] VOID DisassociateCurrentThreadFromCallback(PTP_CALLBACK_INSTANCE pci)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pci"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FreeLibraryWhenCallbackReturns(jitter):
    """"
    [Kernel32.dll] VOID FreeLibraryWhenCallbackReturns(PTP_CALLBACK_INSTANCE pci, HMODULE mod)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pci", "mod"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsThreadpoolTimerSet(jitter):
    """"
    [Kernel32.dll] BOOL IsThreadpoolTimerSet(PTP_TIMER pti)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pti"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LeaveCriticalSectionWhenCallbackReturns(jitter):
    """"
    [Kernel32.dll] VOID LeaveCriticalSectionWhenCallbackReturns(PTP_CALLBACK_INSTANCE pci, PCRITICAL_SECTION pcs)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pci", "pcs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryThreadpoolStackInformation(jitter):
    """"
    [Kernel32.dll] BOOL QueryThreadpoolStackInformation(PTP_POOL ptpp, PTP_POOL_STACK_INFORMATION ptpsi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ptpp", "ptpsi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReleaseMutexWhenCallbackReturns(jitter):
    """"
    [Kernel32.dll] VOID ReleaseMutexWhenCallbackReturns(PTP_CALLBACK_INSTANCE pci, HANDLE mut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pci", "mut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReleaseSemaphoreWhenCallbackReturns(jitter):
    """"
    [Kernel32.dll] VOID ReleaseSemaphoreWhenCallbackReturns(PTP_CALLBACK_INSTANCE pci, HANDLE sem, DWORD crel)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pci", "sem", "crel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetEventWhenCallbackReturns(jitter):
    """"
    [Kernel32.dll] VOID SetEventWhenCallbackReturns(PTP_CALLBACK_INSTANCE pci, HANDLE evt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pci", "evt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadpoolStackInformation(jitter):
    """"
    [Kernel32.dll] BOOL SetThreadpoolStackInformation(PTP_POOL ptpp, PTP_POOL_STACK_INFORMATION ptpsi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ptpp", "ptpsi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadpoolThreadMaximum(jitter):
    """"
    [Kernel32.dll] VOID SetThreadpoolThreadMaximum(PTP_POOL ptpp, DWORD cthrdMost)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ptpp", "cthrdMost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadpoolThreadMinimum(jitter):
    """"
    [Kernel32.dll] BOOL SetThreadpoolThreadMinimum(PTP_POOL ptpp, DWORD cthrdMic)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ptpp", "cthrdMic"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadpoolTimer(jitter):
    """"
    [Kernel32.dll] VOID SetThreadpoolTimer(PTP_TIMER pti, PFILETIME pftDueTime, DWORD msPeriod, DWORD msWindowLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pti", "pftDueTime", "msPeriod", "msWindowLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadpoolWait(jitter):
    """"
    [Kernel32.dll] VOID SetThreadpoolWait(PTP_WAIT pwa, HANDLE h, PFILETIME pftTimeout)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwa", "h", "pftTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_StartThreadpoolIo(jitter):
    """"
    [Kernel32.dll] VOID StartThreadpoolIo(PTP_IO pio)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pio"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SubmitThreadpoolWork(jitter):
    """"
    [Kernel32.dll] VOID SubmitThreadpoolWork(PTP_WORK pwk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TrySubmitThreadpoolCallback(jitter):
    """"
    [Kernel32.dll] BOOL TrySubmitThreadpoolCallback(PTP_SIMPLE_CALLBACK pfns, PVOID pv, PTP_CALLBACK_ENVIRON pcbe)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfns", "pv", "pcbe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WaitForThreadpoolIoCallbacks(jitter):
    """"
    [Kernel32.dll] VOID WaitForThreadpoolIoCallbacks(PTP_IO pio, BOOL fCancelPendingCallbacks)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pio", "fCancelPendingCallbacks"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WaitForThreadpoolTimerCallbacks(jitter):
    """"
    [Kernel32.dll] VOID WaitForThreadpoolTimerCallbacks(PTP_TIMER pti, BOOL fCancelPendingCallbacks)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pti", "fCancelPendingCallbacks"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WaitForThreadpoolWaitCallbacks(jitter):
    """"
    [Kernel32.dll] VOID WaitForThreadpoolWaitCallbacks(PTP_WAIT pwa, BOOL fCancelPendingCallbacks)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwa", "fCancelPendingCallbacks"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WaitForThreadpoolWorkCallbacks(jitter):
    """"
    [Kernel32.dll] VOID WaitForThreadpoolWorkCallbacks(PTP_WORK pwk, BOOL fCancelPendingCallbacks)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwk", "fCancelPendingCallbacks"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_BindIoCompletionCallback(jitter):
    """"
    [Kernel32.dll] BOOL BindIoCompletionCallback(HANDLE FileHandle, LPOVERLAPPED_COMPLETION_ROUTINE Function, ULONG Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Function", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueueUserWorkItem(jitter):
    """"
    [Kernel32.dll] BOOL QueueUserWorkItem(LPTHREAD_START_ROUTINE Function, PVOID Context, [WorkItemFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Function", "Context", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ConvertFiberToThread(jitter):
    """"
    [Kernel32.dll] BOOL ConvertFiberToThread()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ConvertThreadToFiber(jitter):
    """"
    [Kernel32.dll] LPVOID ConvertThreadToFiber(LPVOID lpParameter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpParameter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ConvertThreadToFiberEx(jitter):
    """"
    [Kernel32.dll] LPVOID ConvertThreadToFiberEx(LPVOID lpParameter, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpParameter", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateFiber(jitter):
    """"
    [Kernel32.dll] LPVOID CreateFiber(SIZE_T dwStackSize, LPFIBER_START_ROUTINE lpStartAddress, LPVOID lpParameter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwStackSize", "lpStartAddress", "lpParameter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateFiberEx(jitter):
    """"
    [Kernel32.dll] LPVOID CreateFiberEx(SIZE_T dwStackCommitSize, SIZE_T dwStackReserveSize, DWORD dwFlags, LPFIBER_START_ROUTINE lpStartAddress, LPVOID lpParameter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwStackCommitSize", "dwStackReserveSize", "dwFlags", "lpStartAddress", "lpParameter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DeleteFiber(jitter):
    """"
    [Kernel32.dll] VOID DeleteFiber(LPVOID lpFiber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFiber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FlsAlloc(jitter):
    """"
    [Kernel32.dll] DWORD FlsAlloc(PFLS_CALLBACK_FUNCTION lpCallback)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FlsFree(jitter):
    """"
    [Kernel32.dll] BOOL FlsFree(DWORD dwFlsIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlsIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FlsGetValue(jitter):
    """"
    [Kernel32.dll] PVOID FlsGetValue(DWORD dwFlsIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlsIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FlsSetValue(jitter):
    """"
    [Kernel32.dll] BOOL FlsSetValue(DWORD dwFlsIndex, PVOID lpFlsData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlsIndex", "lpFlsData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsThreadAFiber(jitter):
    """"
    [Kernel32.dll] BOOL IsThreadAFiber()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SwitchToFiber(jitter):
    """"
    [Kernel32.dll] VOID SwitchToFiber(LPVOID lpFiber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFiber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AllocateUserPhysicalPagesNuma(jitter):
    """"
    [Kernel32.dll] BOOL AllocateUserPhysicalPagesNuma([ProcessHandle] hProcess, PULONG_PTR NumberOfPages, PULONG_PTR PageArray, DWORD nndPreferred)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "NumberOfPages", "PageArray", "nndPreferred"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumaAvailableMemoryNode(jitter):
    """"
    [Kernel32.dll] BOOL GetNumaAvailableMemoryNode(UCHAR Node, PULONGLONG AvailableBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Node", "AvailableBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumaAvailableMemoryNodeEx(jitter):
    """"
    [Kernel32.dll] BOOL GetNumaAvailableMemoryNodeEx(USHORT Node, PULONGLONG AvailableBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Node", "AvailableBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumaHighestNodeNumber(jitter):
    """"
    [Kernel32.dll] BOOL GetNumaHighestNodeNumber(PULONG HighestNodeNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HighestNodeNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumaNodeNumberFromHandle(jitter):
    """"
    [Kernel32.dll] BOOL GetNumaNodeNumberFromHandle(HANDLE hFile, PUSHORT NodeNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "NodeNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumaNodeProcessorMask(jitter):
    """"
    [Kernel32.dll] BOOL GetNumaNodeProcessorMask(UCHAR Node, PULONGLONG ProcessorMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Node", "ProcessorMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumaNodeProcessorMaskEx(jitter):
    """"
    [Kernel32.dll] BOOL GetNumaNodeProcessorMaskEx(USHORT Node, PGROUP_AFFINITY ProcessorMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Node", "ProcessorMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumaProcessorNode(jitter):
    """"
    [Kernel32.dll] BOOL GetNumaProcessorNode(UCHAR Processor, PUCHAR NodeNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Processor", "NodeNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumaProcessorNodeEx(jitter):
    """"
    [Kernel32.dll] BOOL GetNumaProcessorNodeEx(PPROCESSOR_NUMBER Processor, PUSHORT NodeNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Processor", "NodeNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumaProximityNode(jitter):
    """"
    [Kernel32.dll] BOOL GetNumaProximityNode(ULONG ProximityId, PUCHAR NodeNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProximityId", "NodeNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumaProximityNodeEx(jitter):
    """"
    [Kernel32.dll] BOOL GetNumaProximityNodeEx(ULONG ProximityId, PUSHORT NodeNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProximityId", "NodeNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetActiveProcessorCount(jitter):
    """"
    [Kernel32.dll] DWORD GetActiveProcessorCount(WORD GroupNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["GroupNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetActiveProcessorGroupCount(jitter):
    """"
    [Kernel32.dll] WORD GetActiveProcessorGroupCount()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentProcessorNumber(jitter):
    """"
    [Kernel32.dll] DWORD GetCurrentProcessorNumber()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentProcessorNumberEx(jitter):
    """"
    [Kernel32.dll] VOID GetCurrentProcessorNumberEx(PPROCESSOR_NUMBER ProcNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProcNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetLogicalProcessorInformation(jitter):
    """"
    [Kernel32.dll] BOOL GetLogicalProcessorInformation(PSYSTEM_LOGICAL_PROCESSOR_INFORMATION Buffer, PDWORD ReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Buffer", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetLogicalProcessorInformationEx(jitter):
    """"
    [Kernel32.dll] BOOL GetLogicalProcessorInformationEx(LOGICAL_PROCESSOR_RELATIONSHIP RelationshipType, PSYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX Buffer, PDWORD ReturnedLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RelationshipType", "Buffer", "ReturnedLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetMaximumProcessorCount(jitter):
    """"
    [Kernel32.dll] DWORD GetMaximumProcessorCount(WORD GroupNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["GroupNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetMaximumProcessorGroupCount(jitter):
    """"
    [Kernel32.dll] WORD GetMaximumProcessorGroupCount()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryIdleProcessorCycleTime(jitter):
    """"
    [Kernel32.dll] BOOL QueryIdleProcessorCycleTime(PULONG BufferLength, PULONG64 ProcessorIdleCycleTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BufferLength", "ProcessorIdleCycleTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryIdleProcessorCycleTimeEx(jitter):
    """"
    [Kernel32.dll] BOOL QueryIdleProcessorCycleTimeEx(USHORT Group, PULONG BufferLength, PULONG64 ProcessorIdleCycleTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Group", "BufferLength", "ProcessorIdleCycleTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateUmsCompletionList(jitter):
    """"
    [Kernel32.dll] BOOL CreateUmsCompletionList(PUMS_COMPLETION_LIST* UmsCompletionList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UmsCompletionList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateUmsThreadContext(jitter):
    """"
    [Kernel32.dll] BOOL CreateUmsThreadContext(PUMS_CONTEXT* lpUmsThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpUmsThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DeleteUmsCompletionList(jitter):
    """"
    [Kernel32.dll] BOOL DeleteUmsCompletionList(PUMS_COMPLETION_LIST UmsCompletionList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UmsCompletionList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DeleteUmsThreadContext(jitter):
    """"
    [Kernel32.dll] BOOL DeleteUmsThreadContext(PUMS_CONTEXT UmsThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UmsThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DequeueUmsCompletionListItems(jitter):
    """"
    [Kernel32.dll] BOOL DequeueUmsCompletionListItems(PUMS_COMPLETION_LIST UmsCompletionList, DWORD WaitTimeOut, PUMS_CONTEXT* UmsThreadList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UmsCompletionList", "WaitTimeOut", "UmsThreadList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnterUmsSchedulingMode(jitter):
    """"
    [Kernel32.dll] BOOL EnterUmsSchedulingMode(PUMS_SCHEDULER_STARTUP_INFO SchedulerStartupInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SchedulerStartupInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ExecuteUmsThread(jitter):
    """"
    [Kernel32.dll] BOOL ExecuteUmsThread(PUMS_CONTEXT UmsThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UmsThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentUmsThread(jitter):
    """"
    [Kernel32.dll] PUMS_CONTEXT GetCurrentUmsThread()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNextUmsListItem(jitter):
    """"
    [Kernel32.dll] PUMS_CONTEXT GetNextUmsListItem(PUMS_CONTEXT UmsContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UmsContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetUmsCompletionListEvent(jitter):
    """"
    [Kernel32.dll] BOOL GetUmsCompletionListEvent(PUMS_COMPLETION_LIST UmsCompletionList, PHANDLE UmsCompletionEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UmsCompletionList", "UmsCompletionEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetUmsSystemThreadInformation(jitter):
    """"
    [Kernel32.dll] BOOL GetUmsSystemThreadInformation([ThreadHandle] ThreadHandle, PUMS_SYSTEM_THREAD_INFORMATION SystemThreadInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "SystemThreadInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryUmsThreadInformation(jitter):
    """"
    [Kernel32.dll] BOOL QueryUmsThreadInformation(PUMS_CONTEXT UmsThread, UMS_THREAD_INFO_CLASS UmsThreadInfoClass, PVOID UmsThreadInformation, ULONG UmsThreadInformationLength, PULONG ReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UmsThread", "UmsThreadInfoClass", "UmsThreadInformation", "UmsThreadInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetUmsThreadInformation(jitter):
    """"
    [Kernel32.dll] BOOL SetUmsThreadInformation(PUMS_CONTEXT UmsThread, UMS_THREAD_INFO_CLASS UmsThreadInfoClass, PVOID UmsThreadInformation, ULONG UmsThreadInformationLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UmsThread", "UmsThreadInfoClass", "UmsThreadInformation", "UmsThreadInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_UmsThreadYield(jitter):
    """"
    [Kernel32.dll] BOOL UmsThreadYield(PVOID SchedulerParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SchedulerParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WinExec(jitter):
    """"
    [Kernel32.dll] UINT WinExec(LPCSTR lpCmdLine, UINT uCmdShow)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCmdLine", "uCmdShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ActivateActCtx(jitter):
    """"
    [Kernel32.dll] BOOL ActivateActCtx(HANDLE hActCtx, ULONG_PTR* lpCookie)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hActCtx", "lpCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AddRefActCtx(jitter):
    """"
    [Kernel32.dll] void AddRefActCtx(HANDLE hActCtx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hActCtx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateActCtx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateActCtx(PACTCTX pActCtx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pActCtx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateActCtxA(jitter):
    kernel32_CreateActCtx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateActCtxW(jitter):
    kernel32_CreateActCtx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_DeactivateActCtx(jitter):
    """"
    [Kernel32.dll] BOOL DeactivateActCtx([DeactivateActCtxFlags] dwFlags, ULONG_PTR ulCookie)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "ulCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindActCtxSectionGuid(jitter):
    """"
    [Kernel32.dll] BOOL FindActCtxSectionGuid([FIND_ACTCTX_SECTION_FLAGS] dwFlags, const GUID* lpExtensionGuid, [ACTIVATION_CONTEXT_SECTION] ulSectionId, const GUID* lpGuidToFind, PACTCTX_SECTION_KEYED_DATA ReturnedData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpExtensionGuid", "ulSectionId", "lpGuidToFind", "ReturnedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindActCtxSectionString(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL FindActCtxSectionString([FIND_ACTCTX_SECTION_FLAGS] dwFlags, const GUID* lpExtensionGuid, [ACTIVATION_CONTEXT_SECTION] ulSectionId, LPCTSTR lpStringToFind, PACTCTX_SECTION_KEYED_DATA ReturnedData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpExtensionGuid", "ulSectionId", "lpStringToFind", "ReturnedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindActCtxSectionStringA(jitter):
    kernel32_FindActCtxSectionString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FindActCtxSectionStringW(jitter):
    kernel32_FindActCtxSectionString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetCurrentActCtx(jitter):
    """"
    [Kernel32.dll] BOOL GetCurrentActCtx(HANDLE* lphActCtx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lphActCtx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryActCtxW(jitter):
    """"
    [Kernel32.dll] BOOL QueryActCtxW([QueryActCtxFlags] dwFlags, HANDLE hActCtx, PVOID pvSubInstance, [ActivationContextInfoClass] ulInfoClass, PVOID pvBuffer, SIZE_T cbBuffer, SIZE_T* pcbWrittenOrRequired)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "hActCtx", "pvSubInstance", "ulInfoClass", "pvBuffer", "cbBuffer", "pcbWrittenOrRequired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryActCtxSettingsW(jitter):
    """"
    [Kernel32.dll] BOOL QueryActCtxSettingsW(DWORD dwFlags, HANDLE hActCtx, PCWSTR settingsNameSpace, PCWSTR settingName, PWSTR pvBuffer, SIZE_T dwBuffer, SIZE_T* pdwWrittenOrRequired)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "hActCtx", "settingsNameSpace", "settingName", "pvBuffer", "dwBuffer", "pdwWrittenOrRequired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReleaseActCtx(jitter):
    """"
    [Kernel32.dll] void ReleaseActCtx(HANDLE hActCtx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hActCtx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ZombifyActCtx(jitter):
    """"
    [Kernel32.dll] BOOL ZombifyActCtx(HANDLE hActCtx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hActCtx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AddAtom(jitter, get_str, set_str):
    """"
    [Kernel32.dll] ATOM AddAtom(LPCTSTR lpString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AddAtomA(jitter):
    kernel32_AddAtom(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_AddAtomW(jitter):
    kernel32_AddAtom(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_DeleteAtom(jitter):
    """"
    [Kernel32.dll] ATOM DeleteAtom(ATOM nAtom)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nAtom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindAtom(jitter, get_str, set_str):
    """"
    [Kernel32.dll] ATOM FindAtom(LPCTSTR lpString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindAtomA(jitter):
    kernel32_FindAtom(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FindAtomW(jitter):
    kernel32_FindAtom(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetAtomName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] UINT GetAtomName(ATOM nAtom, LPTSTR lpBuffer, int nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nAtom", "lpBuffer", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetAtomNameA(jitter):
    kernel32_GetAtomName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetAtomNameW(jitter):
    kernel32_GetAtomName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GlobalAddAtom(jitter, get_str, set_str):
    """"
    [Kernel32.dll] ATOM GlobalAddAtom(LPCTSTR lpString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalAddAtomA(jitter):
    kernel32_GlobalAddAtom(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GlobalAddAtomW(jitter):
    kernel32_GlobalAddAtom(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GlobalDeleteAtom(jitter):
    """"
    [Kernel32.dll] ATOM GlobalDeleteAtom(ATOM nAtom)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nAtom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalFindAtom(jitter, get_str, set_str):
    """"
    [Kernel32.dll] ATOM GlobalFindAtom(LPCTSTR lpString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalFindAtomA(jitter):
    kernel32_GlobalFindAtom(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GlobalFindAtomW(jitter):
    kernel32_GlobalFindAtom(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GlobalGetAtomName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] UINT GlobalGetAtomName(ATOM nAtom, LPTSTR lpBuffer, int nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nAtom", "lpBuffer", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GlobalGetAtomNameA(jitter):
    kernel32_GlobalGetAtomName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GlobalGetAtomNameW(jitter):
    kernel32_GlobalGetAtomName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_InitAtomTable(jitter):
    """"
    [Kernel32.dll] BOOL InitAtomTable(DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_BuildCommDCB(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL BuildCommDCB(LPCTSTR lpDef, LPDCB lpDCB)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpDef", "lpDCB"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_BuildCommDCBA(jitter):
    kernel32_BuildCommDCB(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_BuildCommDCBW(jitter):
    kernel32_BuildCommDCB(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_BuildCommDCBAndTimeouts(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL BuildCommDCBAndTimeouts(LPCTSTR lpDef, LPDCB lpDCB, LPCOMMTIMEOUTS lpCommTimeouts)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpDef", "lpDCB", "lpCommTimeouts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_BuildCommDCBAndTimeoutsA(jitter):
    kernel32_BuildCommDCBAndTimeouts(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_BuildCommDCBAndTimeoutsW(jitter):
    kernel32_BuildCommDCBAndTimeouts(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_ClearCommBreak(jitter):
    """"
    [Kernel32.dll] BOOL ClearCommBreak(HANDLE hFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ClearCommError(jitter):
    """"
    [Kernel32.dll] BOOL ClearCommError(HANDLE hFile, LPDWORD lpErrors, LPCOMSTAT lpStat)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpErrors", "lpStat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CommConfigDialog(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL CommConfigDialog(LPCTSTR lpszName, HWND hWnd, LPCOMMCONFIG lpCC)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszName", "hWnd", "lpCC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CommConfigDialogA(jitter):
    kernel32_CommConfigDialog(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CommConfigDialogW(jitter):
    kernel32_CommConfigDialog(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EscapeCommFunction(jitter):
    """"
    [Kernel32.dll] BOOL EscapeCommFunction(HANDLE hFile, [COMM_FUNCTION] dwFunc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "dwFunc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCommConfig(jitter):
    """"
    [Kernel32.dll] BOOL GetCommConfig(HANDLE hCommDev, LPCOMMCONFIG lpCC, LPDWORD lpdwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCommDev", "lpCC", "lpdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCommMask(jitter):
    """"
    [Kernel32.dll] BOOL GetCommMask(HANDLE hFile, [COMM_EVENT*] lpEvtMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpEvtMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCommModemStatus(jitter):
    """"
    [Kernel32.dll] BOOL GetCommModemStatus(HANDLE hFile, [MODEM_STATUS_FLAGS*] lpModemStat)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpModemStat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCommProperties(jitter):
    """"
    [Kernel32.dll] BOOL GetCommProperties(HANDLE hFile, LPCOMMPROP lpCommProp)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpCommProp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCommState(jitter):
    """"
    [Kernel32.dll] BOOL GetCommState(HANDLE hFile, LPDCB lpDCB)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpDCB"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCommTimeouts(jitter):
    """"
    [Kernel32.dll] BOOL GetCommTimeouts(HANDLE hFile, LPCOMMTIMEOUTS lpCommTimeouts)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpCommTimeouts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDefaultCommConfig(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetDefaultCommConfig(LPCTSTR lpszName, LPCOMMCONFIG lpCC, LPDWORD lpdwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszName", "lpCC", "lpdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDefaultCommConfigA(jitter):
    kernel32_GetDefaultCommConfig(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetDefaultCommConfigW(jitter):
    kernel32_GetDefaultCommConfig(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_PurgeComm(jitter):
    """"
    [Kernel32.dll] BOOL PurgeComm(HANDLE hFile, [PURGE_FLAGS] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetCommBreak(jitter):
    """"
    [Kernel32.dll] BOOL SetCommBreak(HANDLE hFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetCommConfig(jitter):
    """"
    [Kernel32.dll] BOOL SetCommConfig(HANDLE hCommDev, LPCOMMCONFIG lpCC, DWORD dwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCommDev", "lpCC", "dwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetCommMask(jitter):
    """"
    [Kernel32.dll] BOOL SetCommMask(HANDLE hFile, [COMM_EVENT] dwEvtMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "dwEvtMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetCommState(jitter):
    """"
    [Kernel32.dll] BOOL SetCommState(HANDLE hFile, LPDCB lpDCB)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpDCB"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetCommTimeouts(jitter):
    """"
    [Kernel32.dll] BOOL SetCommTimeouts(HANDLE hFile, LPCOMMTIMEOUTS lpCommTimeouts)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpCommTimeouts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetDefaultCommConfig(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetDefaultCommConfig(LPCTSTR lpszName, LPCOMMCONFIG lpCC, DWORD dwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszName", "lpCC", "dwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetDefaultCommConfigA(jitter):
    kernel32_SetDefaultCommConfig(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetDefaultCommConfigW(jitter):
    kernel32_SetDefaultCommConfig(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetupComm(jitter):
    """"
    [Kernel32.dll] BOOL SetupComm(HANDLE hFile, DWORD dwInQueue, DWORD dwOutQueue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "dwInQueue", "dwOutQueue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TransmitCommChar(jitter):
    """"
    [Kernel32.dll] BOOL TransmitCommChar(HANDLE hFile, char cChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "cChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WaitCommEvent(jitter):
    """"
    [Kernel32.dll] BOOL WaitCommEvent(HANDLE hFile, [COMM_EVENT*] lpEvtMask, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpEvtMask", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AddConsoleAlias(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL AddConsoleAlias(LPCTSTR Source, LPCTSTR Target, LPCTSTR ExeName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Source", "Target", "ExeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AddConsoleAliasA(jitter):
    kernel32_AddConsoleAlias(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_AddConsoleAliasW(jitter):
    kernel32_AddConsoleAlias(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_AllocConsole(jitter):
    """"
    [Kernel32.dll] BOOL AllocConsole()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AttachConsole(jitter):
    """"
    [Kernel32.dll] BOOL AttachConsole(DWORD dwProcessId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateConsoleScreenBuffer(jitter):
    """"
    [Kernel32.dll] HANDLE CreateConsoleScreenBuffer(DWORD dwDesiredAccess, [FILE_SHARE_MODE] dwShareMode, const SECURITY_ATTRIBUTES* lpSecurityAttributes, [CONSOLE_TEXTMODE_FLAGS] dwFlags, LPVOID lpScreenBufferData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDesiredAccess", "dwShareMode", "lpSecurityAttributes", "dwFlags", "lpScreenBufferData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FillConsoleOutputAttribute(jitter):
    """"
    [Kernel32.dll] BOOL FillConsoleOutputAttribute(HANDLE hConsoleOutput, [ConsoleAttribute] wAttribute, DWORD nLength, COORD dwWriteCoord, LPDWORD lpNumberOfAttrsWritten)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "wAttribute", "nLength", "dwWriteCoord", "lpNumberOfAttrsWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FillConsoleOutputCharacter(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL FillConsoleOutputCharacter(HANDLE hConsoleOutput, TCHAR cCharacter, DWORD nLength, COORD dwWriteCoord, LPDWORD lpNumberOfCharsWritten)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "cCharacter", "nLength", "dwWriteCoord", "lpNumberOfCharsWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FillConsoleOutputCharacterA(jitter):
    kernel32_FillConsoleOutputCharacter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FillConsoleOutputCharacterW(jitter):
    kernel32_FillConsoleOutputCharacter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FlushConsoleInputBuffer(jitter):
    """"
    [Kernel32.dll] BOOL FlushConsoleInputBuffer(HANDLE hConsoleInput)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleInput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FreeConsole(jitter):
    """"
    [Kernel32.dll] BOOL FreeConsole()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GenerateConsoleCtrlEvent(jitter):
    """"
    [Kernel32.dll] BOOL GenerateConsoleCtrlEvent(DWORD dwCtrlEvent, DWORD dwProcessGroupId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCtrlEvent", "dwProcessGroupId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleAlias(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetConsoleAlias(LPTSTR lpSource, LPTSTR lpTargetBuffer, DWORD TargetBufferLength, LPTSTR lpExeName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSource", "lpTargetBuffer", "TargetBufferLength", "lpExeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleAliasA(jitter):
    kernel32_GetConsoleAlias(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetConsoleAliasW(jitter):
    kernel32_GetConsoleAlias(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetConsoleAliases(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetConsoleAliases(LPTSTR lpAliasBuffer, DWORD AliasBufferLength, LPTSTR lpExeName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAliasBuffer", "AliasBufferLength", "lpExeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleAliasesA(jitter):
    kernel32_GetConsoleAliases(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetConsoleAliasesW(jitter):
    kernel32_GetConsoleAliases(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetConsoleAliasesLength(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetConsoleAliasesLength(LPTSTR lpExeName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpExeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleAliasesLengthA(jitter):
    kernel32_GetConsoleAliasesLength(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetConsoleAliasesLengthW(jitter):
    kernel32_GetConsoleAliasesLength(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetConsoleAliasExes(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetConsoleAliasExes(LPTSTR lpExeNameBuffer, DWORD ExeNameBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpExeNameBuffer", "ExeNameBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleAliasExesA(jitter):
    kernel32_GetConsoleAliasExes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetConsoleAliasExesW(jitter):
    kernel32_GetConsoleAliasExes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetConsoleAliasExesLength(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetConsoleAliasExesLength()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleAliasExesLengthA(jitter):
    kernel32_GetConsoleAliasExesLength(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetConsoleAliasExesLengthW(jitter):
    kernel32_GetConsoleAliasExesLength(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetConsoleCP(jitter):
    """"
    [Kernel32.dll] [CodePageEnum] GetConsoleCP()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleCursorInfo(jitter):
    """"
    [Kernel32.dll] BOOL GetConsoleCursorInfo(HANDLE hConsoleOutput, PCONSOLE_CURSOR_INFO lpConsoleCursorInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "lpConsoleCursorInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleDisplayMode(jitter):
    """"
    [Kernel32.dll] BOOL GetConsoleDisplayMode([CONSOLE_FULLSCREEN_MODE*] lpModeFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpModeFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleFontSize(jitter):
    """"
    [Kernel32.dll] COORD GetConsoleFontSize(HANDLE hConsoleOutput, DWORD nFont)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "nFont"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleHistoryInfo(jitter):
    """"
    [Kernel32.dll] BOOL GetConsoleHistoryInfo(PCONSOLE_HISTORY_INFO lpConsoleHistoryInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpConsoleHistoryInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleMode(jitter):
    """"
    [Kernel32.dll] BOOL GetConsoleMode(HANDLE hConsoleHandle, [ConsoleModeFlags*] lpMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleHandle", "lpMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleOriginalTitle(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetConsoleOriginalTitle(LPTSTR lpConsoleTitle, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpConsoleTitle", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleOriginalTitleA(jitter):
    kernel32_GetConsoleOriginalTitle(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetConsoleOriginalTitleW(jitter):
    kernel32_GetConsoleOriginalTitle(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetConsoleOutputCP(jitter):
    """"
    [Kernel32.dll] UINT GetConsoleOutputCP()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleProcessList(jitter):
    """"
    [Kernel32.dll] DWORD GetConsoleProcessList(LPDWORD lpdwProcessList, DWORD dwProcessCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpdwProcessList", "dwProcessCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleScreenBufferInfo(jitter):
    """"
    [Kernel32.dll] BOOL GetConsoleScreenBufferInfo(HANDLE hConsoleOutput, PCONSOLE_SCREEN_BUFFER_INFO lpConsoleScreenBufferInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "lpConsoleScreenBufferInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleScreenBufferInfoEx(jitter):
    """"
    [Kernel32.dll] BOOL GetConsoleScreenBufferInfoEx(HANDLE hConsoleOutput, PCONSOLE_SCREEN_BUFFER_INFOEX lpConsoleScreenBufferInfoEx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "lpConsoleScreenBufferInfoEx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleSelectionInfo(jitter):
    """"
    [Kernel32.dll] BOOL GetConsoleSelectionInfo(PCONSOLE_SELECTION_INFO lpConsoleSelectionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpConsoleSelectionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleTitle(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetConsoleTitle(LPTSTR lpConsoleTitle, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpConsoleTitle", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetConsoleTitleA(jitter):
    kernel32_GetConsoleTitle(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetConsoleTitleW(jitter):
    kernel32_GetConsoleTitle(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetConsoleWindow(jitter):
    """"
    [Kernel32.dll] HWND GetConsoleWindow()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentConsoleFont(jitter):
    """"
    [Kernel32.dll] BOOL GetCurrentConsoleFont(HANDLE hConsoleOutput, BOOL bMaximumWindow, PCONSOLE_FONT_INFO lpConsoleCurrentFont)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "bMaximumWindow", "lpConsoleCurrentFont"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentConsoleFontEx(jitter):
    """"
    [Kernel32.dll] BOOL GetCurrentConsoleFontEx(HANDLE hConsoleOutput, BOOL bMaximumWindow, PCONSOLE_FONT_INFOEX lpConsoleCurrentFontEx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "bMaximumWindow", "lpConsoleCurrentFontEx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetLargestConsoleWindowSize(jitter):
    """"
    [Kernel32.dll] COORD GetLargestConsoleWindowSize(HANDLE hConsoleOutput)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumberOfConsoleInputEvents(jitter):
    """"
    [Kernel32.dll] BOOL GetNumberOfConsoleInputEvents(HANDLE hConsoleInput, LPDWORD lpcNumberOfEvents)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleInput", "lpcNumberOfEvents"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumberOfConsoleMouseButtons(jitter):
    """"
    [Kernel32.dll] BOOL GetNumberOfConsoleMouseButtons(LPDWORD lpNumberOfMouseButtons)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpNumberOfMouseButtons"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetStdHandle(jitter):
    """"
    [Kernel32.dll] [FILE_HANDLE] GetStdHandle([StdHandle] nStdHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nStdHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PeekConsoleInput(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL PeekConsoleInput(HANDLE hConsoleInput, PINPUT_RECORD lpBuffer, DWORD nLength, LPDWORD lpNumberOfEventsRead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleInput", "lpBuffer", "nLength", "lpNumberOfEventsRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PeekConsoleInputA(jitter):
    kernel32_PeekConsoleInput(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_PeekConsoleInputW(jitter):
    kernel32_PeekConsoleInput(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_ReadConsole(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL ReadConsole(HANDLE hConsoleInput, LPVOID lpBuffer, DWORD nNumberOfCharsToRead, LPDWORD lpNumberOfCharsRead, LPVOID pInputControl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleInput", "lpBuffer", "nNumberOfCharsToRead", "lpNumberOfCharsRead", "pInputControl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReadConsoleA(jitter):
    kernel32_ReadConsole(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_ReadConsoleW(jitter):
    kernel32_ReadConsole(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_ReadConsoleInput(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL ReadConsoleInput(HANDLE hConsoleInput, PINPUT_RECORD lpBuffer, DWORD nLength, LPDWORD lpNumberOfEventsRead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleInput", "lpBuffer", "nLength", "lpNumberOfEventsRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReadConsoleInputA(jitter):
    kernel32_ReadConsoleInput(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_ReadConsoleInputW(jitter):
    kernel32_ReadConsoleInput(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_ReadConsoleOutput(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL ReadConsoleOutput(HANDLE hConsoleOutput, PCHAR_INFO lpBuffer, COORD dwBufferSize, COORD dwBufferCoord, PSMALL_RECT lpReadRegion)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "lpBuffer", "dwBufferSize", "dwBufferCoord", "lpReadRegion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReadConsoleOutputA(jitter):
    kernel32_ReadConsoleOutput(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_ReadConsoleOutputW(jitter):
    kernel32_ReadConsoleOutput(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_ReadConsoleOutputAttribute(jitter):
    """"
    [Kernel32.dll] BOOL ReadConsoleOutputAttribute(HANDLE hConsoleOutput, [ConsoleAttribute*] lpAttribute, DWORD nLength, COORD dwReadCoord, LPDWORD lpNumberOfAttrsRead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "lpAttribute", "nLength", "dwReadCoord", "lpNumberOfAttrsRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReadConsoleOutputCharacter(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL ReadConsoleOutputCharacter(HANDLE hConsoleOutput, LPTSTR lpCharacter, DWORD nLength, COORD dwReadCoord, LPDWORD lpNumberOfCharsRead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "lpCharacter", "nLength", "dwReadCoord", "lpNumberOfCharsRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReadConsoleOutputCharacterA(jitter):
    kernel32_ReadConsoleOutputCharacter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_ReadConsoleOutputCharacterW(jitter):
    kernel32_ReadConsoleOutputCharacter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_ScrollConsoleScreenBuffer(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL ScrollConsoleScreenBuffer(HANDLE hConsoleOutput, const SMALL_RECT* lpScrollRectangle, const SMALL_RECT* lpClipRectangle, COORD dwDestinationOrigin, const CHAR_INFO* lpFill)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "lpScrollRectangle", "lpClipRectangle", "dwDestinationOrigin", "lpFill"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ScrollConsoleScreenBufferA(jitter):
    kernel32_ScrollConsoleScreenBuffer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_ScrollConsoleScreenBufferW(jitter):
    kernel32_ScrollConsoleScreenBuffer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetConsoleActiveScreenBuffer(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleActiveScreenBuffer(HANDLE hConsoleOutput)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleCP(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleCP([CodePageEnum] wCodePageID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["wCodePageID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleCtrlHandler(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleCtrlHandler(PHANDLER_ROUTINE HandlerRoutine, BOOL Add)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HandlerRoutine", "Add"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleCursorInfo(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleCursorInfo(HANDLE hConsoleOutput, const CONSOLE_CURSOR_INFO* lpConsoleCursorInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "lpConsoleCursorInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleCursorPosition(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleCursorPosition(HANDLE hConsoleOutput, COORD dwCursorPosition)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "dwCursorPosition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleDisplayMode(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleDisplayMode(HANDLE hConsoleOutput, [CONSOLE_DISPLAY_MODE] dwFlags, PCOORD lpNewScreenBufferDimensions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "dwFlags", "lpNewScreenBufferDimensions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleHistoryInfo(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleHistoryInfo(PCONSOLE_HISTORY_INFO lpConsoleHistoryInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpConsoleHistoryInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleMode(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleMode(HANDLE hConsoleHandle, [ConsoleModeFlags] dwMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleHandle", "dwMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleOutputCP(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleOutputCP([CodePageEnum] wCodePageID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["wCodePageID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleScreenBufferInfoEx(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleScreenBufferInfoEx(HANDLE hConsoleOutput, PCONSOLE_SCREEN_BUFFER_INFOEX lpConsoleScreenBufferInfoEx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "lpConsoleScreenBufferInfoEx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleScreenBufferSize(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleScreenBufferSize(HANDLE hConsoleOutput, COORD dwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "dwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleTextAttribute(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleTextAttribute(HANDLE hConsoleOutput, [ConsoleAttribute] wAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "wAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleTitle(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetConsoleTitle(LPCTSTR lpConsoleTitle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpConsoleTitle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleTitleA(jitter):
    kernel32_SetConsoleTitle(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetConsoleTitleW(jitter):
    kernel32_SetConsoleTitle(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetConsoleWindowInfo(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleWindowInfo(HANDLE hConsoleOutput, BOOL bAbsolute, const SMALL_RECT* lpConsoleWindow)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "bAbsolute", "lpConsoleWindow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetCurrentConsoleFontEx(jitter):
    """"
    [Kernel32.dll] BOOL SetCurrentConsoleFontEx(HANDLE hConsoleOutput, BOOL bMaximumWindow, PCONSOLE_FONT_INFOEX lpConsoleCurrentFontEx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "bMaximumWindow", "lpConsoleCurrentFontEx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetStdHandle(jitter):
    """"
    [Kernel32.dll] BOOL SetStdHandle([StdHandle] nStdHandle, HANDLE hHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nStdHandle", "hHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WriteConsole(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL WriteConsole(HANDLE hConsoleOutput, LPCTSTR lpBuffer, DWORD nNumberOfCharsToWrite, LPDWORD lpNumberOfCharsWritten, LPVOID lpReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "lpBuffer", "nNumberOfCharsToWrite", "lpNumberOfCharsWritten", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WriteConsoleA(jitter):
    kernel32_WriteConsole(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_WriteConsoleW(jitter):
    kernel32_WriteConsole(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_WriteConsoleInput(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL WriteConsoleInput(HANDLE hConsoleInput, const INPUT_RECORD* lpBuffer, DWORD nLength, LPDWORD lpNumberOfEventsWritten)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleInput", "lpBuffer", "nLength", "lpNumberOfEventsWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WriteConsoleInputA(jitter):
    kernel32_WriteConsoleInput(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_WriteConsoleInputW(jitter):
    kernel32_WriteConsoleInput(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_WriteConsoleOutput(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL WriteConsoleOutput(HANDLE hConsoleOutput, const CHAR_INFO* lpBuffer, COORD dwBufferSize, COORD dwBufferCoord, PSMALL_RECT lpWriteRegion)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "lpBuffer", "dwBufferSize", "dwBufferCoord", "lpWriteRegion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WriteConsoleOutputA(jitter):
    kernel32_WriteConsoleOutput(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_WriteConsoleOutputW(jitter):
    kernel32_WriteConsoleOutput(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_WriteConsoleOutputAttribute(jitter):
    """"
    [Kernel32.dll] BOOL WriteConsoleOutputAttribute(HANDLE hConsoleOutput, [ConsoleAttribute*] lpAttribute, DWORD nLength, COORD dwWriteCoord, LPDWORD lpNumberOfAttrsWritten)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "lpAttribute", "nLength", "dwWriteCoord", "lpNumberOfAttrsWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WriteConsoleOutputCharacter(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL WriteConsoleOutputCharacter(HANDLE hConsoleOutput, LPCTSTR lpCharacter, DWORD nLength, COORD dwWriteCoord, LPDWORD lpNumberOfCharsWritten)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "lpCharacter", "nLength", "dwWriteCoord", "lpNumberOfCharsWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WriteConsoleOutputCharacterA(jitter):
    kernel32_WriteConsoleOutputCharacter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_WriteConsoleOutputCharacterW(jitter):
    kernel32_WriteConsoleOutputCharacter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetConsoleInputExeName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetConsoleInputExeName(LPCTSTR lpName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleInputExeNameA(jitter):
    kernel32_SetConsoleInputExeName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetConsoleInputExeNameW(jitter):
    kernel32_SetConsoleInputExeName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_DeviceIoControl(jitter):
    """"
    [Kernel32.dll] BOOL DeviceIoControl(HANDLE hDevice, [IOCTL] dwIoControlCode, LPVOID lpInBuffer, DWORD nInBufferSize, LPVOID lpOutBuffer, DWORD nOutBufferSize, LPDWORD lpBytesReturned, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDevice", "dwIoControlCode", "lpInBuffer", "nInBufferSize", "lpOutBuffer", "nOutBufferSize", "lpBytesReturned", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Beep(jitter):
    """"
    [Kernel32.dll] BOOL Beep(DWORD dwFreq, DWORD dwDuration)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFreq", "dwDuration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RtlCaptureStackBackTrace(jitter):
    """"
    [Kernel32.dll] USHORT RtlCaptureStackBackTrace(ULONG FramesToSkip, ULONG FramesToCapture, PVOID* BackTrace, PULONG BackTraceHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FramesToSkip", "FramesToCapture", "BackTrace", "BackTraceHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FatalAppExit(jitter, get_str, set_str):
    """"
    [Kernel32.dll] void FatalAppExit(UINT uAction, LPCTSTR lpMessageText)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uAction", "lpMessageText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FatalAppExitA(jitter):
    kernel32_FatalAppExit(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FatalAppExitW(jitter):
    kernel32_FatalAppExit(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FormatMessage(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD FormatMessage([FormatMessageFlags] dwFlags, LPCVOID lpSource, DWORD dwMessageId, DWORD dwLanguageId, LPTSTR lpBuffer, DWORD nSize, va_list* Arguments)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpSource", "dwMessageId", "dwLanguageId", "lpBuffer", "nSize", "Arguments"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FormatMessageA(jitter):
    kernel32_FormatMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FormatMessageW(jitter):
    kernel32_FormatMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetErrorMode(jitter):
    """"
    [Kernel32.dll] [SEM_FLAGS] GetErrorMode()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetLastError(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] GetLastError()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadErrorMode(jitter):
    """"
    [Kernel32.dll] [SEM_FLAGS_DWORD] GetThreadErrorMode()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RtlLookupFunctionEntry(jitter):
    """"
    [Kernel32.dll] PVOID RtlLookupFunctionEntry(ULONGLONG ControlPC, PULONGLONG ImageBase, PULONGLONG TargetGp)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ControlPC", "ImageBase", "TargetGp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RtlPcToFileHeader(jitter):
    """"
    [Kernel32.dll] PVOID RtlPcToFileHeader(PVOID PcValue, PVOID* BaseOfImage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PcValue", "BaseOfImage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetErrorMode(jitter):
    """"
    [Kernel32.dll] [SEM_FLAGS] SetErrorMode([SEM_FLAGS] uMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetLastError(jitter):
    """"
    [Kernel32.dll] void SetLastError([ERROR_CODE] dwErrCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwErrCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadErrorMode(jitter):
    """"
    [Kernel32.dll] BOOL SetThreadErrorMode([SEM_FLAGS_DWORD] dwNewMode, [SEM_FLAGS_DWORD*] lpOldMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwNewMode", "lpOldMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CloseHandle(jitter):
    """"
    [Kernel32.dll] BOOL CloseHandle(HANDLE hObject)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DuplicateHandle(jitter):
    """"
    [Kernel32.dll] BOOL DuplicateHandle([ProcessHandle] hSourceProcessHandle, [PROCESS_THREAD_HANDLE] hSourceHandle, [ProcessHandle] hTargetProcessHandle, LPHANDLE lpTargetHandle, [StandardAccessRights] dwDesiredAccess, BOOL bInheritHandle, [DUPLICATE_HANDLE_FLAGS] dwOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSourceProcessHandle", "hSourceHandle", "hTargetProcessHandle", "lpTargetHandle", "dwDesiredAccess", "bInheritHandle", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetHandleInformation(jitter):
    """"
    [Kernel32.dll] BOOL GetHandleInformation(HANDLE hObject, [HANDLE_FLAGS*] lpdwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hObject", "lpdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetHandleInformation(jitter):
    """"
    [Kernel32.dll] BOOL SetHandleInformation(HANDLE hObject, [HANDLE_FLAGS] dwMask, [HANDLE_FLAGS] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hObject", "dwMask", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetHandleCount(jitter):
    """"
    [Kernel32.dll] UINT SetHandleCount(UINT uNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateMailslot(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateMailslot(LPCTSTR lpName, DWORD nMaxMessageSize, DWORD lReadTimeout, LPSECURITY_ATTRIBUTES lpSecurityAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpName", "nMaxMessageSize", "lReadTimeout", "lpSecurityAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateMailslotA(jitter):
    kernel32_CreateMailslot(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateMailslotW(jitter):
    kernel32_CreateMailslot(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetMailslotInfo(jitter):
    """"
    [Kernel32.dll] BOOL GetMailslotInfo(HANDLE hMailslot, LPDWORD lpMaxMessageSize, LPDWORD lpNextSize, LPDWORD lpMessageCount, LPDWORD lpReadTimeout)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMailslot", "lpMaxMessageSize", "lpNextSize", "lpMessageCount", "lpReadTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetMailslotInfo(jitter):
    """"
    [Kernel32.dll] BOOL SetMailslotInfo(HANDLE hMailslot, DWORD lReadTimeout)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMailslot", "lReadTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AdjustCalendarDate(jitter):
    """"
    [Kernel32.dll] BOOL AdjustCalendarDate(LPCALDATETIME lpCalDateTime, CALDATETIME_DATEUNIT calUnit, INT amount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCalDateTime", "calUnit", "amount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CompareString(jitter, get_str, set_str):
    """"
    [Kernel32.dll] int CompareString(LCID Locale, [NLS_STRING_COMPARE_FLAGS] dwCmpFlags, LPCTSTR lpString1, int cchCount1, LPCTSTR lpString2, int cchCount2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwCmpFlags", "lpString1", "cchCount1", "lpString2", "cchCount2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CompareStringA(jitter):
    kernel32_CompareString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CompareStringW(jitter):
    kernel32_CompareString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CompareStringEx(jitter):
    """"
    [Kernel32.dll] int CompareStringEx(LPCWSTR lpLocaleName, [NLS_STRING_COMPARE_FLAGS] dwCmpFlags, LPCWSTR lpString1, int cchCount1, LPCWSTR lpString2, int cchCount2, LPNLSVERSIONINFO lpVersionInformation, LPVOID lpReserved, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName", "dwCmpFlags", "lpString1", "cchCount1", "lpString2", "cchCount2", "lpVersionInformation", "lpReserved", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CompareStringOrdinal(jitter):
    """"
    [Kernel32.dll] int CompareStringOrdinal(LPCWSTR lpString1, int cchCount1, LPCWSTR lpString2, int cchCount2, BOOL bIgnoreCase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString1", "cchCount1", "lpString2", "cchCount2", "bIgnoreCase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ConvertCalDateTimeToSystemTime(jitter):
    """"
    [Kernel32.dll] BOOL ConvertCalDateTimeToSystemTime(const LPCALDATETIME lpCalDateTime, SYSTEMTIME* lpSysTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCalDateTime", "lpSysTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ConvertDefaultLocale(jitter):
    """"
    [Kernel32.dll] LCID ConvertDefaultLocale(LCID Locale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ConvertSystemTimeToCalDateTime(jitter):
    """"
    [Kernel32.dll] BOOL ConvertSystemTimeToCalDateTime(const SYSTEMTIME lpSysTime, CALID calId, LPCALDATETIME lpCalDateTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSysTime", "calId", "lpCalDateTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumCalendarInfo(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumCalendarInfo(CALINFO_ENUMPROC pCalInfoEnumProc, LCID Locale, CALID Calendar, CALTYPE CalType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCalInfoEnumProc", "Locale", "Calendar", "CalType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumCalendarInfoA(jitter):
    kernel32_EnumCalendarInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumCalendarInfoW(jitter):
    kernel32_EnumCalendarInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumCalendarInfoEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumCalendarInfoEx(CALINFO_ENUMPROCEX pCalInfoEnumProcEx, LCID Locale, CALID Calendar, CALTYPE CalType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCalInfoEnumProcEx", "Locale", "Calendar", "CalType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumCalendarInfoExA(jitter):
    kernel32_EnumCalendarInfoEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumCalendarInfoExW(jitter):
    kernel32_EnumCalendarInfoEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumCalendarInfoExEx(jitter):
    """"
    [Kernel32.dll] BOOL EnumCalendarInfoExEx(CALINFO_ENUMPROCEXEX pCalInfoEnumProcExEx, LPCWSTR lpLocaleName, CALID Calendar, LPCWSTR lpReserved, CALTYPE CalType, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCalInfoEnumProcExEx", "lpLocaleName", "Calendar", "lpReserved", "CalType", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumDateFormats(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumDateFormats(DATEFMT_ENUMPROC lpDateFmtEnumProc, LCID Locale, [NLS_DATE_FLAGS] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpDateFmtEnumProc", "Locale", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumDateFormatsA(jitter):
    kernel32_EnumDateFormats(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumDateFormatsW(jitter):
    kernel32_EnumDateFormats(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumDateFormatsEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumDateFormatsEx(DATEFMT_ENUMPROCEX lpDateFmtEnumProcEx, LCID Locale, [NLS_DATE_FLAGS] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpDateFmtEnumProcEx", "Locale", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumDateFormatsExA(jitter):
    kernel32_EnumDateFormatsEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumDateFormatsExW(jitter):
    kernel32_EnumDateFormatsEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumDateFormatsExEx(jitter):
    """"
    [Kernel32.dll] BOOL EnumDateFormatsExEx(DATEFMT_ENUMPROCEXEX lpDateFmtEnumProcExEx, LPCWSTR lpLocaleName, [NLS_DATE_FLAGS] dwFlags, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpDateFmtEnumProcExEx", "lpLocaleName", "dwFlags", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumLanguageGroupLocales(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumLanguageGroupLocales(LANGGROUPLOCALE_ENUMPROC lpLangGroupLocaleEnumProc, LGRPID LanguageGroup, DWORD dwFlags, LONG_PTR lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLangGroupLocaleEnumProc", "LanguageGroup", "dwFlags", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumLanguageGroupLocalesA(jitter):
    kernel32_EnumLanguageGroupLocales(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumLanguageGroupLocalesW(jitter):
    kernel32_EnumLanguageGroupLocales(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumSystemCodePages(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumSystemCodePages(CODEPAGE_ENUMPROC lpCodePageEnumProc, [CodePageEnumerationFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCodePageEnumProc", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumSystemCodePagesA(jitter):
    kernel32_EnumSystemCodePages(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumSystemCodePagesW(jitter):
    kernel32_EnumSystemCodePages(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumSystemGeoID(jitter):
    """"
    [Kernel32.dll] BOOL EnumSystemGeoID(GEOCLASS GeoClass, GEOID ParentGeoId, GEO_ENUMPROC lpGeoEnumProc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["GeoClass", "ParentGeoId", "lpGeoEnumProc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumSystemLanguageGroups(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumSystemLanguageGroups(LANGUAGEGROUP_ENUMPROC lpLanguageGroupEnumProc, [LANGUAGE_GROUP_FLAGS] dwFlags, LONG_PTR lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLanguageGroupEnumProc", "dwFlags", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumSystemLanguageGroupsA(jitter):
    kernel32_EnumSystemLanguageGroups(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumSystemLanguageGroupsW(jitter):
    kernel32_EnumSystemLanguageGroups(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumSystemLocales(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumSystemLocales(LOCALE_ENUMPROC lpLocaleEnumProc, [LocaleEnumerationFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleEnumProc", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumSystemLocalesA(jitter):
    kernel32_EnumSystemLocales(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumSystemLocalesW(jitter):
    kernel32_EnumSystemLocales(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumSystemLocalesEx(jitter):
    """"
    [Kernel32.dll] BOOL EnumSystemLocalesEx(LOCALE_ENUMPROCEX lpLocaleEnumProcEx, [EnumSystemLocalesExFlags] dwFlags, LPARAM lParam, LPVOID lpReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleEnumProcEx", "dwFlags", "lParam", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumTimeFormats(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumTimeFormats(TIMEFMT_ENUMPROC lpTimeFmtEnumProc, LCID Locale, [NLS_TIME_FLAGS] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTimeFmtEnumProc", "Locale", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumTimeFormatsA(jitter):
    kernel32_EnumTimeFormats(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumTimeFormatsW(jitter):
    kernel32_EnumTimeFormats(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumTimeFormatsEx(jitter):
    """"
    [Kernel32.dll] BOOL EnumTimeFormatsEx(TIMEFMT_ENUMPROCEX lpTimeFmtEnumProcEx, LPCWSTR lpLocaleName, [NLS_TIME_FLAGS] dwFlags, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTimeFmtEnumProcEx", "lpLocaleName", "dwFlags", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindNLSString(jitter):
    """"
    [Kernel32.dll] int FindNLSString(LCID Locale, [NLS_STRING_FIND_FLAGS] dwFindNLSStringFlags, LPCWSTR lpStringSource, int cchSource, LPCWSTR lpStringValue, int cchValue, LPINT pcchFound)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwFindNLSStringFlags", "lpStringSource", "cchSource", "lpStringValue", "cchValue", "pcchFound"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindNLSStringEx(jitter):
    """"
    [Kernel32.dll] int FindNLSStringEx(LPCWSTR lpLocaleName, [NLS_STRING_FIND_FLAGS] dwFindNLSStringFlags, LPCWSTR lpStringSource, int cchSource, LPCWSTR lpStringValue, int cchValue, LPINT pcchFound, LPNLSVERSIONINFO lpVersionInformation, LPVOID lpReserved, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName", "dwFindNLSStringFlags", "lpStringSource", "cchSource", "lpStringValue", "cchValue", "pcchFound", "lpVersionInformation", "lpReserved", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindStringOrdinal(jitter):
    """"
    [Kernel32.dll] int FindStringOrdinal([NLS_FIND_FLAGS] dwFindStringOrdinalFlags, LPCWSTR lpStringSource, int cchSource, LPCWSTR lpStringValue, int cchValue, BOOL bIgnoreCase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFindStringOrdinalFlags", "lpStringSource", "cchSource", "lpStringValue", "cchValue", "bIgnoreCase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FoldString(jitter, get_str, set_str):
    """"
    [Kernel32.dll] int FoldString([MappingFlags] dwMapFlags, LPCTSTR lpSrcStr, int cchSrc, LPTSTR lpDestStr, int cchDest)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwMapFlags", "lpSrcStr", "cchSrc", "lpDestStr", "cchDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FoldStringA(jitter):
    kernel32_FoldString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FoldStringW(jitter):
    kernel32_FoldString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetACP(jitter):
    """"
    [Kernel32.dll] UINT GetACP()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCalendarDateFormatEx(jitter):
    """"
    [Kernel32.dll] BOOL GetCalendarDateFormatEx(LPCWSTR lpszLocale, [NLS_DATE_FLAGS] dwFlags, const LPCALDATETIME lpCalDateTime, LPCWSTR lpFormat, LPWSTR lpDateStr, int cchDate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszLocale", "dwFlags", "lpCalDateTime", "lpFormat", "lpDateStr", "cchDate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCalendarInfo(jitter, get_str, set_str):
    """"
    [Kernel32.dll] int GetCalendarInfo(LCID Locale, CALID Calendar, CALTYPE CalType, LPTSTR lpCalData, int cchData, LPDWORD lpValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "Calendar", "CalType", "lpCalData", "cchData", "lpValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCalendarInfoA(jitter):
    kernel32_GetCalendarInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetCalendarInfoW(jitter):
    kernel32_GetCalendarInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetCalendarInfoEx(jitter):
    """"
    [Kernel32.dll] int GetCalendarInfoEx(LPCWSTR lpLocaleName, CALID Calendar, LPCWSTR lpReserved, CALTYPE CalType, LPWSTR lpCalData, int cchData, LPDWORD lpValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName", "Calendar", "lpReserved", "CalType", "lpCalData", "cchData", "lpValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCalendarSupportedDateRange(jitter):
    """"
    [Kernel32.dll] BOOL GetCalendarSupportedDateRange(CALID Calendar, LPCALDATETIME lpCalMinDateTime, LPCALDATETIME lpCalMaxDateTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Calendar", "lpCalMinDateTime", "lpCalMaxDateTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCPInfo(jitter):
    """"
    [Kernel32.dll] BOOL GetCPInfo([CodePageEnum] CodePage, LPCPINFO lpCPInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CodePage", "lpCPInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCPInfoEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetCPInfoEx([CodePageEnum] CodePage, DWORD dwFlags, LPCPINFOEX lpCPInfoEx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CodePage", "dwFlags", "lpCPInfoEx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCPInfoExA(jitter):
    kernel32_GetCPInfoEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetCPInfoExW(jitter):
    kernel32_GetCPInfoEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetCurrencyFormat(jitter, get_str, set_str):
    """"
    [Kernel32.dll] int GetCurrencyFormat(LCID Locale, [LOCALE_NOUSEROVERRIDE_FLAG] dwFlags, LPCTSTR lpValue, const CURRENCYFMT* lpFormat, LPTSTR lpCurrencyStr, int cchCurrency)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwFlags", "lpValue", "lpFormat", "lpCurrencyStr", "cchCurrency"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrencyFormatA(jitter):
    kernel32_GetCurrencyFormat(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetCurrencyFormatW(jitter):
    kernel32_GetCurrencyFormat(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetCurrencyFormatEx(jitter):
    """"
    [Kernel32.dll] int GetCurrencyFormatEx(LPCWSTR lpLocaleName, [LOCALE_NOUSEROVERRIDE_FLAG] dwFlags, LPCWSTR lpValue, const CURRENCYFMT* lpFormat, LPWSTR lpCurrencyStr, int cchCurrency)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName", "dwFlags", "lpValue", "lpFormat", "lpCurrencyStr", "cchCurrency"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDateFormat(jitter, get_str, set_str):
    """"
    [Kernel32.dll] int GetDateFormat(LCID Locale, [NLS_DATE_FLAGS] dwFlags, const SYSTEMTIME* lpDate, LPCTSTR lpFormat, LPTSTR lpDateStr, int cchDate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwFlags", "lpDate", "lpFormat", "lpDateStr", "cchDate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDateFormatA(jitter):
    kernel32_GetDateFormat(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetDateFormatW(jitter):
    kernel32_GetDateFormat(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetDateFormatEx(jitter):
    """"
    [Kernel32.dll] int GetDateFormatEx(LPCWSTR lpLocaleName, [NLS_DATE_FLAGS] dwFlags, const SYSTEMTIME* lpDate, LPCWSTR lpFormat, LPWSTR lpDateStr, int cchDate, LPCWSTR lpCalendar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName", "dwFlags", "lpDate", "lpFormat", "lpDateStr", "cchDate", "lpCalendar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDurationFormat(jitter):
    """"
    [Kernel32.dll] int GetDurationFormat(LCID Locale, [LOCALE_NOUSEROVERRIDE_FLAG] dwFlags, const SYSTEMTIME* lpDuration, ULONGLONG ullDuration, LPCWSTR lpFormat, LPWSTR lpDurationStr, int cchDuration)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwFlags", "lpDuration", "ullDuration", "lpFormat", "lpDurationStr", "cchDuration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDurationFormatEx(jitter):
    """"
    [Kernel32.dll] int GetDurationFormatEx(LPCWSTR lpLocaleName, [LOCALE_NOUSEROVERRIDE_FLAG] dwFlags, const SYSTEMTIME* lpDuration, ULONGLONG ullDuration, LPCWSTR lpFormat, LPWSTR lpDurationStr, int cchDuration)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName", "dwFlags", "lpDuration", "ullDuration", "lpFormat", "lpDurationStr", "cchDuration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetGeoInfo(jitter, get_str, set_str):
    """"
    [Kernel32.dll] int GetGeoInfo(GEOID Location, GEOTYPE GeoType, LPTSTR lpGeoData, int cchData, LANGID LangId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Location", "GeoType", "lpGeoData", "cchData", "LangId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetGeoInfoA(jitter):
    kernel32_GetGeoInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetGeoInfoW(jitter):
    kernel32_GetGeoInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetLocaleInfo(jitter, get_str, set_str):
    """"
    [Kernel32.dll] int GetLocaleInfo(LCID Locale, LCTYPE LCType, LPTSTR lpLCData, int cchData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "LCType", "lpLCData", "cchData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetLocaleInfoA(jitter):
    kernel32_GetLocaleInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetLocaleInfoW(jitter):
    kernel32_GetLocaleInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetLocaleInfoEx(jitter):
    """"
    [Kernel32.dll] int GetLocaleInfoEx(LPCWSTR lpLocaleName, LCTYPE LCType, LPWSTR lpLCData, int cchData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName", "LCType", "lpLCData", "cchData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNLSVersion(jitter):
    """"
    [Kernel32.dll] BOOL GetNLSVersion(NLS_FUNCTION Function, LCID Locale, LPNLSVERSIONINFO lpVersionInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Function", "Locale", "lpVersionInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNLSVersionEx(jitter):
    """"
    [Kernel32.dll] BOOL GetNLSVersionEx(NLS_FUNCTION function, LPCWSTR lpLocaleName, LPNLSVERSIONINFOEX lpVersionInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["function", "lpLocaleName", "lpVersionInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumberFormat(jitter, get_str, set_str):
    """"
    [Kernel32.dll] int GetNumberFormat(LCID Locale, [LOCALE_NOUSEROVERRIDE_FLAG] dwFlags, LPCTSTR lpValue, const NUMBERFMT* lpFormat, LPTSTR lpNumberStr, int cchNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwFlags", "lpValue", "lpFormat", "lpNumberStr", "cchNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNumberFormatA(jitter):
    kernel32_GetNumberFormat(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetNumberFormatW(jitter):
    kernel32_GetNumberFormat(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetNumberFormatEx(jitter):
    """"
    [Kernel32.dll] int GetNumberFormatEx(LPCWSTR lpLocaleName, [LOCALE_NOUSEROVERRIDE_FLAG] dwFlags, LPCWSTR lpValue, const NUMBERFMT* lpFormat, LPWSTR lpNumberStr, int cchNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName", "dwFlags", "lpValue", "lpFormat", "lpNumberStr", "cchNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetOEMCP(jitter):
    """"
    [Kernel32.dll] UINT GetOEMCP()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetStringScripts(jitter):
    """"
    [Kernel32.dll] int GetStringScripts([GET_STRING_SCRIPTS_FLAGS] dwFlags, LPCWSTR lpString, int cchString, LPWSTR lpScripts, int cchScripts)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpString", "cchString", "lpScripts", "cchScripts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetStringTypeA(jitter):
    """"
    [Kernel32.dll] BOOL GetStringTypeA(LCID Locale, [CharacterTypeFlag] dwInfoType, LPCSTR lpSrcStr, int cchSrc, LPWORD lpCharType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwInfoType", "lpSrcStr", "cchSrc", "lpCharType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetStringTypeEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetStringTypeEx(LCID Locale, [CharacterTypeFlag] dwInfoType, LPCTSTR lpSrcStr, int cchSrc, LPWORD lpCharType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwInfoType", "lpSrcStr", "cchSrc", "lpCharType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetStringTypeExA(jitter):
    kernel32_GetStringTypeEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetStringTypeExW(jitter):
    kernel32_GetStringTypeEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetStringTypeW(jitter):
    """"
    [Kernel32.dll] BOOL GetStringTypeW([CharacterTypeFlag] dwInfoType, LPCWSTR lpSrcStr, int cchSrc, LPWORD lpCharType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwInfoType", "lpSrcStr", "cchSrc", "lpCharType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemDefaultLangID(jitter):
    """"
    [Kernel32.dll] LANGID GetSystemDefaultLangID()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemDefaultLCID(jitter):
    """"
    [Kernel32.dll] LCID GetSystemDefaultLCID()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemDefaultLocaleName(jitter):
    """"
    [Kernel32.dll] int GetSystemDefaultLocaleName(LPWSTR lpLocaleName, int cchLocaleName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName", "cchLocaleName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadLocale(jitter):
    """"
    [Kernel32.dll] LCID GetThreadLocale()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetTimeFormat(jitter, get_str, set_str):
    """"
    [Kernel32.dll] int GetTimeFormat(LCID Locale, [NLS_TIME_FLAGS] dwFlags, const SYSTEMTIME* lpTime, LPCTSTR lpFormat, LPTSTR lpTimeStr, int cchTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwFlags", "lpTime", "lpFormat", "lpTimeStr", "cchTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetTimeFormatA(jitter):
    kernel32_GetTimeFormat(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetTimeFormatW(jitter):
    kernel32_GetTimeFormat(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetTimeFormatEx(jitter):
    """"
    [Kernel32.dll] int GetTimeFormatEx(LPCWSTR lpLocaleName, [NLS_TIME_FLAGS] dwFlags, const SYSTEMTIME* lpTime, LPCWSTR lpFormat, LPWSTR lpTimeStr, int cchTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName", "dwFlags", "lpTime", "lpFormat", "lpTimeStr", "cchTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetUserDefaultLangID(jitter):
    """"
    [Kernel32.dll] LANGID GetUserDefaultLangID()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetUserDefaultLCID(jitter):
    """"
    [Kernel32.dll] LCID GetUserDefaultLCID()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetUserDefaultLocaleName(jitter):
    """"
    [Kernel32.dll] int GetUserDefaultLocaleName(LPWSTR lpLocaleName, int cchLocaleName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName", "cchLocaleName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetUserGeoID(jitter):
    """"
    [Kernel32.dll] GEOID GetUserGeoID(GEOCLASS GeoClass)
    """"
    ret_ad, args = jitter.func_args_stdcall(["GeoClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsCalendarLeapYear(jitter):
    """"
    [Kernel32.dll] BOOL IsCalendarLeapYear(CALID calId, UINT year, UINT era)
    """"
    ret_ad, args = jitter.func_args_stdcall(["calId", "year", "era"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsNLSDefinedString(jitter):
    """"
    [Kernel32.dll] BOOL IsNLSDefinedString(NLS_FUNCTION Function, DWORD dwFlags, LPNLSVERSIONINFO lpVersionInformation, LPCWSTR lpString, INT cchStr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Function", "dwFlags", "lpVersionInformation", "lpString", "cchStr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsValidCodePage(jitter):
    """"
    [Kernel32.dll] BOOL IsValidCodePage([CodePageEnum] CodePage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CodePage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsValidLanguageGroup(jitter):
    """"
    [Kernel32.dll] BOOL IsValidLanguageGroup(LGRPID LanguageGroup, [LANGUAGE_GROUP_FLAGS] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LanguageGroup", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsValidLocale(jitter):
    """"
    [Kernel32.dll] BOOL IsValidLocale(LCID Locale, [LocaleEnumerationFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsValidLocaleName(jitter):
    """"
    [Kernel32.dll] BOOL IsValidLocaleName(LPCWSTR lpLocaleName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsValidNLSVersion(jitter):
    """"
    [Kernel32.dll] DWORD IsValidNLSVersion(NLS_FUNCTION function, LPCWSTR lpLocaleName, LPNLSVERSIONINFOEX lpVersionInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["function", "lpLocaleName", "lpVersionInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LCIDToLocaleName(jitter):
    """"
    [Kernel32.dll] int LCIDToLocaleName(LCID Locale, LPWSTR lpName, int cchName, [LOCALE_NAME_FLAGS] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "lpName", "cchName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LCMapString(jitter, get_str, set_str):
    """"
    [Kernel32.dll] int LCMapString(LCID Locale, [LocaleMappingFlags] dwMapFlags, LPCTSTR lpSrcStr, int cchSrc, LPTSTR lpDestStr, int cchDest)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwMapFlags", "lpSrcStr", "cchSrc", "lpDestStr", "cchDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LCMapStringA(jitter):
    kernel32_LCMapString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_LCMapStringW(jitter):
    kernel32_LCMapString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_LCMapStringEx(jitter):
    """"
    [Kernel32.dll] int LCMapStringEx(LPCWSTR lpLocaleName, [LocaleMappingFlags] dwMapFlags, LPCWSTR lpSrcStr, int cchSrc, LPWSTR lpDestStr, int cchDest, LPNLSVERSIONINFO lpVersionInformation, LPVOID lpReserved, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocaleName", "dwMapFlags", "lpSrcStr", "cchSrc", "lpDestStr", "cchDest", "lpVersionInformation", "lpReserved", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LoadStringByReference(jitter):
    """"
    [Kernel32.dll] BOOL LoadStringByReference([LoadStringByReference_Flags] Flags, PCWSTR Language, PCWSTR SourceString, PWSTR Buffer, ULONG cchBuffer, PCWSTR Directory, PULONG pcchBufferOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Language", "SourceString", "Buffer", "cchBuffer", "Directory", "pcchBufferOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LocaleNameToLCID(jitter):
    """"
    [Kernel32.dll] LCID LocaleNameToLCID(LPCWSTR lpName, [LOCALE_NAME_FLAGS] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_NotifyUILanguageChange(jitter):
    """"
    [Kernel32.dll] BOOL NotifyUILanguageChange(DWORD dwFlags, PCWSTR pcwstrNewLanguage, PCWSTR pcwstrPreviousLanguage, DWORD dwReserved, PDWORD pdwStatusRtrn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pcwstrNewLanguage", "pcwstrPreviousLanguage", "dwReserved", "pdwStatusRtrn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ResolveLocaleName(jitter):
    """"
    [Kernel32.dll] int ResolveLocaleName(LPCWSTR lpNameToResolve, LPWSTR lpLocaleName, int cchLocaleName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpNameToResolve", "lpLocaleName", "cchLocaleName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetCalendarInfo(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetCalendarInfo(LCID Locale, CALID Calendar, CALTYPE CalType, LPCTSTR lpCalData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "Calendar", "CalType", "lpCalData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetCalendarInfoA(jitter):
    kernel32_SetCalendarInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetCalendarInfoW(jitter):
    kernel32_SetCalendarInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetLocaleInfo(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetLocaleInfo(LCID Locale, LCTYPE LCType, LPCTSTR lpLCData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "LCType", "lpLCData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetLocaleInfoA(jitter):
    kernel32_SetLocaleInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetLocaleInfoW(jitter):
    kernel32_SetLocaleInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetThreadLocale(jitter):
    """"
    [Kernel32.dll] BOOL SetThreadLocale(LCID Locale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetUserGeoID(jitter):
    """"
    [Kernel32.dll] BOOL SetUserGeoID(GEOID GeoId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["GeoId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_UpdateCalendarDayOfWeek(jitter):
    """"
    [Kernel32.dll] BOOL UpdateCalendarDayOfWeek(LPCALDATETIME lpCalDateTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCalDateTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VerifyScripts(jitter):
    """"
    [Kernel32.dll] BOOL VerifyScripts([VERIFY_SCRIPTS_FLAGS] dwFlags, LPCWSTR lpLocaleScripts, int cchLocaleScripts, LPCWSTR lpTestScripts, int cchTestScripts)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpLocaleScripts", "cchLocaleScripts", "lpTestScripts", "cchTestScripts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDevicePowerState(jitter):
    """"
    [Kernel32.dll] BOOL GetDevicePowerState(HANDLE hDevice, BOOL* pfOn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDevice", "pfOn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemPowerStatus(jitter):
    """"
    [Kernel32.dll] BOOL GetSystemPowerStatus(LPSYSTEM_POWER_STATUS lpSystemPowerStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemPowerStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsSystemResumeAutomatic(jitter):
    """"
    [Kernel32.dll] BOOL IsSystemResumeAutomatic()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PowerClearRequest(jitter):
    """"
    [Kernel32.dll] BOOL PowerClearRequest(HANDLE PowerRequest, POWER_REQUEST_TYPE RequestType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PowerRequest", "RequestType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PowerCreateRequest(jitter):
    """"
    [Kernel32.dll] HANDLE PowerCreateRequest(PREASON_CONTEXT Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PowerSetRequest(jitter):
    """"
    [Kernel32.dll] BOOL PowerSetRequest(HANDLE PowerRequest, POWER_REQUEST_TYPE RequestType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PowerRequest", "RequestType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryUnbiasedInterruptTime(jitter):
    """"
    [Kernel32.dll] BOOL QueryUnbiasedInterruptTime(PULONGLONG UnbiasedTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UnbiasedTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadExecutionState(jitter):
    """"
    [Kernel32.dll] EXECUTION_STATE SetThreadExecutionState(EXECUTION_STATE esFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["esFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RequestWakeupLatency(jitter):
    """"
    [Kernel32.dll] BOOL RequestWakeupLatency(LATENCY_TIME latency)
    """"
    ret_ad, args = jitter.func_args_stdcall(["latency"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetSystemPowerState(jitter):
    """"
    [Kernel32.dll] BOOL SetSystemPowerState(BOOL fSuspend, BOOL fForce)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fSuspend", "fForce"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_BeginUpdateResource(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE BeginUpdateResource(LPCTSTR pFileName, BOOL bDeleteExistingResources)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pFileName", "bDeleteExistingResources"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_BeginUpdateResourceA(jitter):
    kernel32_BeginUpdateResource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_BeginUpdateResourceW(jitter):
    kernel32_BeginUpdateResource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EndUpdateResource(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EndUpdateResource(HANDLE hUpdate, BOOL fDiscard)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hUpdate", "fDiscard"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EndUpdateResourceA(jitter):
    kernel32_EndUpdateResource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EndUpdateResourceW(jitter):
    kernel32_EndUpdateResource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumResourceLanguages(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumResourceLanguages(HMODULE hModule, LPCTSTR lpType, LPCTSTR lpName, ENUMRESLANGPROC lpEnumFunc, LONG_PTR lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "lpType", "lpName", "lpEnumFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumResourceLanguagesA(jitter):
    kernel32_EnumResourceLanguages(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumResourceLanguagesW(jitter):
    kernel32_EnumResourceLanguages(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumResourceLanguagesEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumResourceLanguagesEx(HMODULE hModule, LPCTSTR lpType, LPCTSTR lpName, ENUMRESLANGPROC lpEnumFunc, LONG_PTR lParam, [RESOURCE_ENUM_FLAGS] dwFlags, LANGID LangId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "lpType", "lpName", "lpEnumFunc", "lParam", "dwFlags", "LangId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumResourceLanguagesExA(jitter):
    kernel32_EnumResourceLanguagesEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumResourceLanguagesExW(jitter):
    kernel32_EnumResourceLanguagesEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumResourceNames(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumResourceNames(HMODULE hModule, LPCTSTR lpszType, ENUMRESNAMEPROC lpEnumFunc, LONG_PTR lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "lpszType", "lpEnumFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumResourceNamesA(jitter):
    kernel32_EnumResourceNames(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumResourceNamesW(jitter):
    kernel32_EnumResourceNames(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumResourceNamesEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumResourceNamesEx(HMODULE hModule, LPCTSTR lpszType, ENUMRESNAMEPROC lpEnumFunc, LONG_PTR lParam, [RESOURCE_ENUM_FLAGS] dwFlags, LANGID LangId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "lpszType", "lpEnumFunc", "lParam", "dwFlags", "LangId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumResourceNamesExA(jitter):
    kernel32_EnumResourceNamesEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumResourceNamesExW(jitter):
    kernel32_EnumResourceNamesEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumResourceTypes(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumResourceTypes(HMODULE hModule, ENUMRESTYPEPROC lpEnumFunc, LONG_PTR lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "lpEnumFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumResourceTypesA(jitter):
    kernel32_EnumResourceTypes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumResourceTypesW(jitter):
    kernel32_EnumResourceTypes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumResourceTypesEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumResourceTypesEx(HMODULE hModule, ENUMRESTYPEPROC lpEnumFunc, LONG_PTR lParam, [RESOURCE_ENUM_FLAGS] dwFlags, LANGID LangId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "lpEnumFunc", "lParam", "dwFlags", "LangId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumResourceTypesExA(jitter):
    kernel32_EnumResourceTypesEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumResourceTypesExW(jitter):
    kernel32_EnumResourceTypesEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindResource(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HRSRC FindResource(HMODULE hModule, LPCTSTR lpName, LPCTSTR lpType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "lpName", "lpType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindResourceA(jitter):
    kernel32_FindResource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FindResourceW(jitter):
    kernel32_FindResource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindResourceEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HRSRC FindResourceEx(HMODULE hModule, LPCTSTR lpType, LPCTSTR lpName, WORD wLanguage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "lpType", "lpName", "wLanguage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindResourceExA(jitter):
    kernel32_FindResourceEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FindResourceExW(jitter):
    kernel32_FindResourceEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FreeResource(jitter):
    """"
    [Kernel32.dll] BOOL FreeResource(HGLOBAL hglbResource)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hglbResource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LoadResource(jitter):
    """"
    [Kernel32.dll] HGLOBAL LoadResource(HMODULE hModule, HRSRC hResInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "hResInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LockResource(jitter):
    """"
    [Kernel32.dll] LPVOID LockResource(HGLOBAL hResData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hResData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SizeofResource(jitter):
    """"
    [Kernel32.dll] DWORD SizeofResource(HMODULE hModule, HRSRC hResInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "hResInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_UpdateResource(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL UpdateResource(HANDLE hUpdate, LPCTSTR lpType, LPCTSTR lpName, WORD wLanguage, LPVOID lpData, DWORD cbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hUpdate", "lpType", "lpName", "wLanguage", "lpData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_UpdateResourceA(jitter):
    kernel32_UpdateResource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_UpdateResourceW(jitter):
    kernel32_UpdateResource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_lstrcat(jitter):
    """"
    [Kernel32.dll] LPSTR lstrcat(LPSTR lpString1, LPSTR lpString2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString1", "lpString2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_lstrcat(jitter, get_str, set_str):
    """"
    [Kernel32.dll] LPTSTR lstrcat(LPTSTR lpString1, LPTSTR lpString2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString1", "lpString2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_lstrcatA(jitter):
    kernel32_lstrcat(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_lstrcatW(jitter):
    kernel32_lstrcat(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_lstrcmp(jitter):
    """"
    [Kernel32.dll] int lstrcmp(LPCSTR lpString1, LPCSTR lpString2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString1", "lpString2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_lstrcmp(jitter, get_str, set_str):
    """"
    [Kernel32.dll] int lstrcmp(LPCTSTR lpString1, LPCTSTR lpString2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString1", "lpString2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_lstrcmpA(jitter):
    kernel32_lstrcmp(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_lstrcmpW(jitter):
    kernel32_lstrcmp(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_lstrcmpi(jitter):
    """"
    [Kernel32.dll] int lstrcmpi(LPCSTR lpString1, LPCSTR lpString2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString1", "lpString2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_lstrcmpi(jitter, get_str, set_str):
    """"
    [Kernel32.dll] int lstrcmpi(LPCTSTR lpString1, LPCTSTR lpString2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString1", "lpString2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_lstrcmpiA(jitter):
    kernel32_lstrcmpi(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_lstrcmpiW(jitter):
    kernel32_lstrcmpi(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_lstrcpy(jitter):
    """"
    [Kernel32.dll] LPSTR lstrcpy(LPSTR lpString1, LPSTR lpString2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString1", "lpString2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_lstrcpy(jitter, get_str, set_str):
    """"
    [Kernel32.dll] LPTSTR lstrcpy(LPTSTR lpString1, LPTSTR lpString2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString1", "lpString2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_lstrcpyA(jitter):
    kernel32_lstrcpy(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_lstrcpyW(jitter):
    kernel32_lstrcpy(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_lstrcpyn(jitter):
    """"
    [Kernel32.dll] LPSTR lstrcpyn(LPSTR lpString1, LPCSTR lpString2, int iMaxLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString1", "lpString2", "iMaxLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_lstrcpyn(jitter, get_str, set_str):
    """"
    [Kernel32.dll] LPTSTR lstrcpyn(LPTSTR lpString1, LPCTSTR lpString2, int iMaxLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString1", "lpString2", "iMaxLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_lstrcpynA(jitter):
    kernel32_lstrcpyn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_lstrcpynW(jitter):
    kernel32_lstrcpyn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_lstrlen(jitter):
    """"
    [Kernel32.dll] int lstrlen(LPCSTR lpString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_lstrlen(jitter, get_str, set_str):
    """"
    [Kernel32.dll] int lstrlen(LPCTSTR lpString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_lstrlenA(jitter):
    kernel32_lstrlen(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_lstrlenW(jitter):
    kernel32_lstrlen(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_AddVectoredContinueHandler(jitter):
    """"
    [Kernel32.dll] PVOID AddVectoredContinueHandler(ULONG FirstHandler, PVECTORED_EXCEPTION_HANDLER VectoredHandler)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FirstHandler", "VectoredHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AddVectoredExceptionHandler(jitter):
    """"
    [Kernel32.dll] PVOID AddVectoredExceptionHandler(ULONG FirstHandler, PVECTORED_EXCEPTION_HANDLER VectoredHandler)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FirstHandler", "VectoredHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RemoveVectoredContinueHandler(jitter):
    """"
    [Kernel32.dll] ULONG RemoveVectoredContinueHandler(PVOID Handler)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Handler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RemoveVectoredExceptionHandler(jitter):
    """"
    [Kernel32.dll] ULONG RemoveVectoredExceptionHandler(PVOID Handler)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Handler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetUnhandledExceptionFilter(jitter):
    """"
    [Kernel32.dll] LPTOP_LEVEL_EXCEPTION_FILTER SetUnhandledExceptionFilter(LPTOP_LEVEL_EXCEPTION_FILTER lpTopLevelExceptionFilter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTopLevelExceptionFilter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_UnhandledExceptionFilter(jitter):
    """"
    [Kernel32.dll] LONG UnhandledExceptionFilter(EXCEPTION_POINTERS* ExceptionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExceptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RtlAddFunctionTable(jitter):
    """"
    [Kernel32.dll] BOOLEAN RtlAddFunctionTable(PRUNTIME_FUNCTION FunctionTable, DWORD EntryCount, DWORD64 BaseAddress)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FunctionTable", "EntryCount", "BaseAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RtlCaptureContext(jitter):
    """"
    [Kernel32.dll] VOID RtlCaptureContext(PCONTEXT ContextRecord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RtlDeleteFunctionTable(jitter):
    """"
    [Kernel32.dll] BOOLEAN RtlDeleteFunctionTable(PRUNTIME_FUNCTION FunctionTable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FunctionTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RtlInstallFunctionTableCallback(jitter):
    """"
    [Kernel32.dll] BOOLEAN RtlInstallFunctionTableCallback(DWORD64 TableIdentifier, DWORD64 BaseAddress, DWORD Length, PGET_RUNTIME_FUNCTION_CALLBACK Callback, PVOID Context, PCWSTR OutOfProcessCallbackDll)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TableIdentifier", "BaseAddress", "Length", "Callback", "Context", "OutOfProcessCallbackDll"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RtlRestoreContext(jitter):
    """"
    [Kernel32.dll] VOID RtlRestoreContext(PCONTEXT ContextRecord, PEXCEPTION_RECORD ExceptionRecord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextRecord", "ExceptionRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetOverlappedResult(jitter):
    """"
    [Kernel32.dll] BOOL GetOverlappedResult(HANDLE hFile, LPOVERLAPPED lpOverlapped, LPDWORD lpNumberOfBytesTransferred, BOOL bWait)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpOverlapped", "lpNumberOfBytesTransferred", "bWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetOverlappedResultEx(jitter):
    """"
    [Kernel32.dll] BOOL GetOverlappedResultEx(HANDLE hFile, LPOVERLAPPED lpOverlapped, LPDWORD lpNumberOfBytesTransferred, DWORD dwMilliseconds, BOOL bAlertable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpOverlapped", "lpNumberOfBytesTransferred", "dwMilliseconds", "bAlertable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueueUserAPC(jitter):
    """"
    [Kernel32.dll] DWORD QueueUserAPC(PAPCFUNC pfnAPC, [ThreadHandle] hThread, ULONG_PTR dwData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfnAPC", "hThread", "dwData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AcquireSRWLockExclusive(jitter):
    """"
    [Kernel32.dll] VOID AcquireSRWLockExclusive(PSRWLOCK SRWLock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AcquireSRWLockShared(jitter):
    """"
    [Kernel32.dll] VOID AcquireSRWLockShared(PSRWLOCK SRWLock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitializeConditionVariable(jitter):
    """"
    [Kernel32.dll] VOID InitializeConditionVariable(PCONDITION_VARIABLE ConditionVariable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ConditionVariable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitializeSRWLock(jitter):
    """"
    [Kernel32.dll] VOID InitializeSRWLock(PSRWLOCK SRWLock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReleaseSRWLockExclusive(jitter):
    """"
    [Kernel32.dll] VOID ReleaseSRWLockExclusive(PSRWLOCK SRWLock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReleaseSRWLockShared(jitter):
    """"
    [Kernel32.dll] VOID ReleaseSRWLockShared(PSRWLOCK SRWLock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SleepConditionVariableCS(jitter):
    """"
    [Kernel32.dll] BOOL SleepConditionVariableCS(PCONDITION_VARIABLE ConditionVariable, PCRITICAL_SECTION CriticalSection, [WaitTimeout] dwMilliseconds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ConditionVariable", "CriticalSection", "dwMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SleepConditionVariableSRW(jitter):
    """"
    [Kernel32.dll] BOOL SleepConditionVariableSRW(PCONDITION_VARIABLE ConditionVariable, PSRWLOCK SRWLock, [WaitTimeout] dwMilliseconds, [CONDITION_VARIABLE_FLAGS] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ConditionVariable", "SRWLock", "dwMilliseconds", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TryAcquireSRWLockExclusive(jitter):
    """"
    [Kernel32.dll] BOOLEAN TryAcquireSRWLockExclusive(PSRWLOCK SRWLock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TryAcquireSRWLockShared(jitter):
    """"
    [Kernel32.dll] BOOLEAN TryAcquireSRWLockShared(PSRWLOCK SRWLock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WakeAllConditionVariable(jitter):
    """"
    [Kernel32.dll] VOID WakeAllConditionVariable(PCONDITION_VARIABLE ConditionVariable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ConditionVariable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WakeConditionVariable(jitter):
    """"
    [Kernel32.dll] VOID WakeConditionVariable(PCONDITION_VARIABLE ConditionVariable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ConditionVariable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DeleteCriticalSection(jitter):
    """"
    [Kernel32.dll] void DeleteCriticalSection(LPCRITICAL_SECTION lpCriticalSection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnterCriticalSection(jitter):
    """"
    [Kernel32.dll] void EnterCriticalSection(LPCRITICAL_SECTION lpCriticalSection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitializeCriticalSection(jitter):
    """"
    [Kernel32.dll] void InitializeCriticalSection(LPCRITICAL_SECTION lpCriticalSection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitializeCriticalSectionAndSpinCount(jitter):
    """"
    [Kernel32.dll] BOOL InitializeCriticalSectionAndSpinCount(LPCRITICAL_SECTION lpCriticalSection, DWORD dwSpinCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCriticalSection", "dwSpinCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitializeCriticalSectionEx(jitter):
    """"
    [Kernel32.dll] BOOL InitializeCriticalSectionEx(LPCRITICAL_SECTION lpCriticalSection, DWORD dwSpinCount, [CRITICAL_SECTION_FLAGS] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCriticalSection", "dwSpinCount", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LeaveCriticalSection(jitter):
    """"
    [Kernel32.dll] void LeaveCriticalSection(LPCRITICAL_SECTION lpCriticalSection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetCriticalSectionSpinCount(jitter):
    """"
    [Kernel32.dll] DWORD SetCriticalSectionSpinCount(LPCRITICAL_SECTION lpCriticalSection, DWORD dwSpinCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCriticalSection", "dwSpinCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TryEnterCriticalSection(jitter):
    """"
    [Kernel32.dll] BOOL TryEnterCriticalSection(LPCRITICAL_SECTION lpCriticalSection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateEvent(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateEvent(LPSECURITY_ATTRIBUTES lpEventAttributes, BOOL bManualReset, BOOL bInitialState, LPCTSTR lpName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpEventAttributes", "bManualReset", "bInitialState", "lpName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateEventA(jitter):
    kernel32_CreateEvent(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateEventW(jitter):
    kernel32_CreateEvent(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateEventEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateEventEx(LPSECURITY_ATTRIBUTES lpEventAttributes, LPCTSTR lpName, [CREATE_EVENT_FLAGS] dwFlags, [EventAccessRights] dwDesiredAccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpEventAttributes", "lpName", "dwFlags", "dwDesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateEventExA(jitter):
    kernel32_CreateEventEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateEventExW(jitter):
    kernel32_CreateEventEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_OpenEvent(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE OpenEvent([EventAccessRights] dwDesiredAccess, BOOL bInheritHandle, LPCTSTR lpName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDesiredAccess", "bInheritHandle", "lpName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OpenEventA(jitter):
    kernel32_OpenEvent(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_OpenEventW(jitter):
    kernel32_OpenEvent(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_PulseEvent(jitter):
    """"
    [Kernel32.dll] BOOL PulseEvent(HANDLE hEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ResetEvent(jitter):
    """"
    [Kernel32.dll] BOOL ResetEvent(HANDLE hEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetEvent(jitter):
    """"
    [Kernel32.dll] BOOL SetEvent(HANDLE hEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitOnceBeginInitialize(jitter):
    """"
    [Kernel32.dll] BOOL InitOnceBeginInitialize(LPINIT_ONCE lpInitOnce, [INIT_ONCE_FLAGS] dwFlags, PBOOL fPending, LPVOID* lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpInitOnce", "dwFlags", "fPending", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitOnceComplete(jitter):
    """"
    [Kernel32.dll] BOOL InitOnceComplete(LPINIT_ONCE lpInitOnce, [INIT_ONCE_FLAGS] dwFlags, LPVOID lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpInitOnce", "dwFlags", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitOnceExecuteOnce(jitter):
    """"
    [Kernel32.dll] BOOL InitOnceExecuteOnce(PINIT_ONCE InitOnce, PINIT_ONCE_FN InitFn, PVOID Parameter, LPVOID* Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InitOnce", "InitFn", "Parameter", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitOnceInitialize(jitter):
    """"
    [Kernel32.dll] VOID InitOnceInitialize(PINIT_ONCE InitOnce)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InitOnce"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InterlockedCompareExchange(jitter):
    """"
    [Kernel32.dll] LONG InterlockedCompareExchange(LONG volatile* Destination, LONG Exchange, LONG Comparand)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Destination", "Exchange", "Comparand"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InterlockedCompareExchange64(jitter):
    """"
    [Kernel32.dll] LONGLONG InterlockedCompareExchange64(LONGLONG volatile* Destination, LONGLONG Exchange, LONGLONG Comparand)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Destination", "Exchange", "Comparand"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InterlockedDecrement(jitter):
    """"
    [Kernel32.dll] LONG InterlockedDecrement(LONG volatile* Addend)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Addend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InterlockedExchange(jitter):
    """"
    [Kernel32.dll] LONG InterlockedExchange(LONG volatile* Target, LONG Value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Target", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InterlockedExchangeAdd(jitter):
    """"
    [Kernel32.dll] LONG InterlockedExchangeAdd(LONG volatile* Addend, LONG Value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Addend", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InterlockedIncrement(jitter):
    """"
    [Kernel32.dll] LONG InterlockedIncrement(LONG volatile* Addend)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Addend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateMutex(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateMutex(LPSECURITY_ATTRIBUTES lpMutexAttributes, BOOL bInitialOwner, LPCTSTR lpName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMutexAttributes", "bInitialOwner", "lpName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateMutexA(jitter):
    kernel32_CreateMutex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateMutexW(jitter):
    kernel32_CreateMutex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateMutexEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateMutexEx(LPSECURITY_ATTRIBUTES lpMutexAttributes, LPCTSTR lpName, [CREATE_MUTEX_FLAGS] dwFlags, [MutexAccessRights] dwDesiredAccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMutexAttributes", "lpName", "dwFlags", "dwDesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateMutexExA(jitter):
    kernel32_CreateMutexEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateMutexExW(jitter):
    kernel32_CreateMutexEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_OpenMutex(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE OpenMutex([MutexAccessRights] dwDesiredAccess, BOOL bInheritHandle, LPCTSTR lpName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDesiredAccess", "bInheritHandle", "lpName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OpenMutexA(jitter):
    kernel32_OpenMutex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_OpenMutexW(jitter):
    kernel32_OpenMutex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_ReleaseMutex(jitter):
    """"
    [Kernel32.dll] BOOL ReleaseMutex(HANDLE hMutex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMutex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AddSIDToBoundaryDescriptor(jitter):
    """"
    [Kernel32.dll] BOOL AddSIDToBoundaryDescriptor(HANDLE* BoundaryDescriptor, PSID RequiredSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BoundaryDescriptor", "RequiredSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AddIntegrityLabelToBoundaryDescriptor(jitter):
    """"
    [Kernel32.dll] BOOL AddIntegrityLabelToBoundaryDescriptor(HANDLE* BoundaryDescriptor, PSID IntegrityLabel)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BoundaryDescriptor", "IntegrityLabel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ClosePrivateNamespace(jitter):
    """"
    [Kernel32.dll] BOOLEAN ClosePrivateNamespace(HANDLE Handle, [PrivateNamespaceFlag] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Handle", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateBoundaryDescriptor(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateBoundaryDescriptor(LPCTSTR Name, ULONG Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Name", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateBoundaryDescriptorA(jitter):
    kernel32_CreateBoundaryDescriptor(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateBoundaryDescriptorW(jitter):
    kernel32_CreateBoundaryDescriptor(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreatePrivateNamespace(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreatePrivateNamespace(LPSECURITY_ATTRIBUTES lpPrivateNamespaceAttributes, LPVOID lpBoundaryDescriptor, LPCTSTR lpAliasPrefix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPrivateNamespaceAttributes", "lpBoundaryDescriptor", "lpAliasPrefix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreatePrivateNamespaceA(jitter):
    kernel32_CreatePrivateNamespace(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreatePrivateNamespaceW(jitter):
    kernel32_CreatePrivateNamespace(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_DeleteBoundaryDescriptor(jitter):
    """"
    [Kernel32.dll] VOID DeleteBoundaryDescriptor(HANDLE BoundaryDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BoundaryDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OpenPrivateNamespace(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE OpenPrivateNamespace(LPVOID lpBoundaryDescriptor, LPCTSTR lpAliasPrefix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBoundaryDescriptor", "lpAliasPrefix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OpenPrivateNamespaceA(jitter):
    kernel32_OpenPrivateNamespace(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_OpenPrivateNamespaceW(jitter):
    kernel32_OpenPrivateNamespace(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateSemaphore(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateSemaphore(LPSECURITY_ATTRIBUTES lpSemaphoreAttributes, LONG lInitialCount, LONG lMaximumCount, LPCTSTR lpName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSemaphoreAttributes", "lInitialCount", "lMaximumCount", "lpName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateSemaphoreA(jitter):
    kernel32_CreateSemaphore(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateSemaphoreW(jitter):
    kernel32_CreateSemaphore(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateSemaphoreEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateSemaphoreEx(LPSECURITY_ATTRIBUTES lpSemaphoreAttributes, LONG lInitialCount, LONG lMaximumCount, LPCTSTR lpName, DWORD dwFlags, [SemaphoreAccessRights] dwDesiredAccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSemaphoreAttributes", "lInitialCount", "lMaximumCount", "lpName", "dwFlags", "dwDesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateSemaphoreExA(jitter):
    kernel32_CreateSemaphoreEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateSemaphoreExW(jitter):
    kernel32_CreateSemaphoreEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_OpenSemaphore(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE OpenSemaphore([SemaphoreAccessRights] dwDesiredAccess, BOOL bInheritHandle, LPCTSTR lpName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDesiredAccess", "bInheritHandle", "lpName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OpenSemaphoreA(jitter):
    kernel32_OpenSemaphore(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_OpenSemaphoreW(jitter):
    kernel32_OpenSemaphore(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_ReleaseSemaphore(jitter):
    """"
    [Kernel32.dll] BOOL ReleaseSemaphore(HANDLE hSemaphore, LONG lReleaseCount, LPLONG lpPreviousCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSemaphore", "lReleaseCount", "lpPreviousCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitializeSListHead(jitter):
    """"
    [Kernel32.dll] void InitializeSListHead(PSLIST_HEADER ListHead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ListHead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InterlockedFlushSList(jitter):
    """"
    [Kernel32.dll] PSLIST_ENTRY InterlockedFlushSList(PSLIST_HEADER ListHead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ListHead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InterlockedPopEntrySList(jitter):
    """"
    [Kernel32.dll] PSLIST_ENTRY InterlockedPopEntrySList(PSLIST_HEADER ListHead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ListHead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InterlockedPushEntrySList(jitter):
    """"
    [Kernel32.dll] PSLIST_ENTRY InterlockedPushEntrySList(PSLIST_HEADER ListHead, PSLIST_ENTRY ListEntry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ListHead", "ListEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InterlockedPushListSList(jitter):
    """"
    [Kernel32.dll] PSLIST_ENTRY InterlockedPushListSList(PSLIST_HEADER ListHead, PSLIST_ENTRY List, PSLIST_ENTRY ListEnd, ULONG Count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ListHead", "List", "ListEnd", "Count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InterlockedPushListSListEx(jitter):
    """"
    [Kernel32.dll] PSLIST_ENTRY InterlockedPushListSListEx(PSLIST_HEADER ListHead, PSLIST_ENTRY List, PSLIST_ENTRY ListEnd, ULONG Count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ListHead", "List", "ListEnd", "Count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryDepthSList(jitter):
    """"
    [Kernel32.dll] USHORT QueryDepthSList(PSLIST_HEADER ListHead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ListHead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DeleteSynchronizationBarrier(jitter):
    """"
    [Kernel32.dll] BOOL DeleteSynchronizationBarrier(LPSYNCHRONIZATION_BARRIER lpBarrier)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBarrier"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnterSynchronizationBarrier(jitter):
    """"
    [Kernel32.dll] BOOL EnterSynchronizationBarrier(LPSYNCHRONIZATION_BARRIER lpBarrier, [SYNCHRONIZATION_BARRIER_FLAGS] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBarrier", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitializeSynchronizationBarrier(jitter):
    """"
    [Kernel32.dll] BOOL InitializeSynchronizationBarrier(LPSYNCHRONIZATION_BARRIER lpBarrier, LONG lTotalThreads, LONG lSpinCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBarrier", "lTotalThreads", "lSpinCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ChangeTimerQueueTimer(jitter):
    """"
    [Kernel32.dll] BOOL ChangeTimerQueueTimer(HANDLE TimerQueue, HANDLE Timer, ULONG DueTime, ULONG Period)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TimerQueue", "Timer", "DueTime", "Period"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateTimerQueue(jitter):
    """"
    [Kernel32.dll] HANDLE CreateTimerQueue()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateTimerQueueTimer(jitter):
    """"
    [Kernel32.dll] BOOL CreateTimerQueueTimer(PHANDLE phNewTimer, HANDLE TimerQueue, WAITORTIMERCALLBACK Callback, PVOID Parameter, DWORD DueTime, DWORD Period, [WorkItemFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phNewTimer", "TimerQueue", "Callback", "Parameter", "DueTime", "Period", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DeleteTimerQueue(jitter):
    """"
    [Kernel32.dll] BOOL DeleteTimerQueue(HANDLE TimerQueue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TimerQueue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DeleteTimerQueueEx(jitter):
    """"
    [Kernel32.dll] BOOL DeleteTimerQueueEx(HANDLE TimerQueue, HANDLE CompletionEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TimerQueue", "CompletionEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DeleteTimerQueueTimer(jitter):
    """"
    [Kernel32.dll] BOOL DeleteTimerQueueTimer(HANDLE TimerQueue, HANDLE Timer, HANDLE CompletionEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TimerQueue", "Timer", "CompletionEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RegisterWaitForSingleObject(jitter):
    """"
    [Kernel32.dll] BOOL RegisterWaitForSingleObject(PHANDLE phNewWaitObject, HANDLE hObject, WAITORTIMERCALLBACK Callback, PVOID Context, [WaitTimeout] dwMilliseconds, [WorkItemFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phNewWaitObject", "hObject", "Callback", "Context", "dwMilliseconds", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SignalObjectAndWait(jitter):
    """"
    [Kernel32.dll] DWORD SignalObjectAndWait(HANDLE hObjectToSignal, HANDLE hObjectToWaitOn, [WaitTimeout] dwMilliseconds, BOOL bAlertable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hObjectToSignal", "hObjectToWaitOn", "dwMilliseconds", "bAlertable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_UnregisterWait(jitter):
    """"
    [Kernel32.dll] BOOL UnregisterWait(HANDLE WaitHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["WaitHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_UnregisterWaitEx(jitter):
    """"
    [Kernel32.dll] BOOL UnregisterWaitEx(HANDLE WaitHandle, HANDLE CompletionEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["WaitHandle", "CompletionEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WaitForMultipleObjects(jitter):
    """"
    [Kernel32.dll] [WAIT_RESULT] WaitForMultipleObjects(DWORD nCount, const HANDLE* lpHandles, BOOL bWaitAll, [WaitTimeout] dwMilliseconds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nCount", "lpHandles", "bWaitAll", "dwMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WaitForMultipleObjectsEx(jitter):
    """"
    [Kernel32.dll] [WAIT_RESULT] WaitForMultipleObjectsEx(DWORD nCount, const HANDLE* lpHandles, BOOL bWaitAll, [WaitTimeout] dwMilliseconds, BOOL bAlertable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nCount", "lpHandles", "bWaitAll", "dwMilliseconds", "bAlertable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WaitForSingleObject(jitter):
    """"
    [Kernel32.dll] [WAIT_RESULT] WaitForSingleObject(HANDLE hHandle, [WaitTimeout] dwMilliseconds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHandle", "dwMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WaitForSingleObjectEx(jitter):
    """"
    [Kernel32.dll] [WAIT_RESULT] WaitForSingleObjectEx(HANDLE hHandle, [WaitTimeout] dwMilliseconds, BOOL bAlertable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHandle", "dwMilliseconds", "bAlertable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WaitOnAddress(jitter):
    """"
    [Kernel32.dll] BOOL WaitOnAddress(VOID volatile* Address, PVOID CompareAddress, SIZE_T AddressSize, DWORD dwMilliseconds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Address", "CompareAddress", "AddressSize", "dwMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WakeByAddressAll(jitter):
    """"
    [Kernel32.dll] VOID WakeByAddressAll(PVOID Address)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WakeByAddressSingle(jitter):
    """"
    [Kernel32.dll] VOID WakeByAddressSingle(PVOID Address)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CancelWaitableTimer(jitter):
    """"
    [Kernel32.dll] BOOL CancelWaitableTimer(HANDLE hTimer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTimer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateWaitableTimer(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateWaitableTimer(LPSECURITY_ATTRIBUTES lpTimerAttributes, BOOL bManualReset, LPCTSTR lpTimerName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTimerAttributes", "bManualReset", "lpTimerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateWaitableTimerA(jitter):
    kernel32_CreateWaitableTimer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateWaitableTimerW(jitter):
    kernel32_CreateWaitableTimer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateWaitableTimerEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateWaitableTimerEx(LPSECURITY_ATTRIBUTES lpTimerAttributes, LPCTSTR lpTimerName, [CREATE_WAITABLE_TIMER_FLAGS] dwFlags, [TimerAccessRights] dwDesiredAccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTimerAttributes", "lpTimerName", "dwFlags", "dwDesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateWaitableTimerExA(jitter):
    kernel32_CreateWaitableTimerEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateWaitableTimerExW(jitter):
    kernel32_CreateWaitableTimerEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_OpenWaitableTimer(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE OpenWaitableTimer([TimerAccessRights] dwDesiredAccess, BOOL bInheritHandle, LPCTSTR lpTimerName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDesiredAccess", "bInheritHandle", "lpTimerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OpenWaitableTimerA(jitter):
    kernel32_OpenWaitableTimer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_OpenWaitableTimerW(jitter):
    kernel32_OpenWaitableTimer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetWaitableTimer(jitter):
    """"
    [Kernel32.dll] BOOL SetWaitableTimer(HANDLE hTimer, const LARGE_INTEGER* pDueTime, LONG lPeriod, PTIMERAPCROUTINE pfnCompletionRoutine, LPVOID lpArgToCompletionRoutine, BOOL fResume)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTimer", "pDueTime", "lPeriod", "pfnCompletionRoutine", "lpArgToCompletionRoutine", "fResume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetWaitableTimerEx(jitter):
    """"
    [Kernel32.dll] BOOL SetWaitableTimerEx(HANDLE hTimer, const LARGE_INTEGER* lpDueTime, LONG lPeriod, PTIMERAPCROUTINE pfnCompletionRoutine, LPVOID lpArgToCompletionRoutine, PREASON_CONTEXT WakeContext, ULONG TolerableDelay)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTimer", "lpDueTime", "lPeriod", "pfnCompletionRoutine", "lpArgToCompletionRoutine", "WakeContext", "TolerableDelay"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DnsHostnameToComputerName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL DnsHostnameToComputerName(LPCTSTR Hostname, LPTSTR ComputerName, LPDWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Hostname", "ComputerName", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DnsHostnameToComputerNameA(jitter):
    kernel32_DnsHostnameToComputerName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_DnsHostnameToComputerNameW(jitter):
    kernel32_DnsHostnameToComputerName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_EnumSystemFirmwareTables(jitter):
    """"
    [Kernel32.dll] UINT EnumSystemFirmwareTables(DWORD FirmwareTableProviderSignature, PVOID pFirmwareTableBuffer, DWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FirmwareTableProviderSignature", "pFirmwareTableBuffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ExpandEnvironmentStrings(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD ExpandEnvironmentStrings(LPCTSTR lpSrc, LPTSTR lpDst, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSrc", "lpDst", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ExpandEnvironmentStringsA(jitter):
    kernel32_ExpandEnvironmentStrings(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_ExpandEnvironmentStringsW(jitter):
    kernel32_ExpandEnvironmentStrings(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetComputerName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetComputerName(LPTSTR lpBuffer, LPDWORD lpnSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBuffer", "lpnSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetComputerNameA(jitter):
    kernel32_GetComputerName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetComputerNameW(jitter):
    kernel32_GetComputerName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetComputerNameEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetComputerNameEx(COMPUTER_NAME_FORMAT NameType, LPTSTR lpBuffer, LPDWORD lpnSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["NameType", "lpBuffer", "lpnSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetComputerNameExA(jitter):
    kernel32_GetComputerNameEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetComputerNameExW(jitter):
    kernel32_GetComputerNameEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetFirmwareEnvironmentVariable(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetFirmwareEnvironmentVariable(LPCTSTR lpName, LPCTSTR lpGuid, PVOID pBuffer, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpName", "lpGuid", "pBuffer", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFirmwareEnvironmentVariableA(jitter):
    kernel32_GetFirmwareEnvironmentVariable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetFirmwareEnvironmentVariableW(jitter):
    kernel32_GetFirmwareEnvironmentVariable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetFirmwareEnvironmentVariableEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetFirmwareEnvironmentVariableEx(LPCTSTR lpName, LPCTSTR lpGuid, PVOID pBuffer, DWORD nSize, PDWORD pdwAttribubutes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpName", "lpGuid", "pBuffer", "nSize", "pdwAttribubutes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFirmwareEnvironmentVariableExA(jitter):
    kernel32_GetFirmwareEnvironmentVariableEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetFirmwareEnvironmentVariableExW(jitter):
    kernel32_GetFirmwareEnvironmentVariableEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetFirmwareType(jitter):
    """"
    [Kernel32.dll] BOOL GetFirmwareType(PFIRMWARE_TYPE FirmwareType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FirmwareType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNativeSystemInfo(jitter):
    """"
    [Kernel32.dll] void GetNativeSystemInfo(LPSYSTEM_INFO lpSystemInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProductInfo(jitter):
    """"
    [Kernel32.dll] BOOL GetProductInfo(DWORD dwOSMajorVersion, DWORD dwOSMinorVersion, DWORD dwSpMajorVersion, DWORD dwSpMinorVersion, [ProductType*] pdwReturnedProductType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwOSMajorVersion", "dwOSMinorVersion", "dwSpMajorVersion", "dwSpMinorVersion", "pdwReturnedProductType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemDirectory(jitter, get_str, set_str):
    """"
    [Kernel32.dll] UINT GetSystemDirectory(LPTSTR lpBuffer, UINT uSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBuffer", "uSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemDirectoryA(jitter):
    kernel32_GetSystemDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetSystemDirectoryW(jitter):
    kernel32_GetSystemDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetSystemFirmwareTable(jitter):
    """"
    [Kernel32.dll] UINT GetSystemFirmwareTable(DWORD FirmwareTableProviderSignature, DWORD FirmwareTableID, PVOID pFirmwareTableBuffer, DWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FirmwareTableProviderSignature", "FirmwareTableID", "pFirmwareTableBuffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemInfo(jitter):
    """"
    [Kernel32.dll] void GetSystemInfo(LPSYSTEM_INFO lpSystemInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemRegistryQuota(jitter):
    """"
    [Kernel32.dll] BOOL GetSystemRegistryQuota(PDWORD pdwQuotaAllowed, PDWORD pdwQuotaUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pdwQuotaAllowed", "pdwQuotaUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemWindowsDirectory(jitter, get_str, set_str):
    """"
    [Kernel32.dll] UINT GetSystemWindowsDirectory(LPTSTR lpBuffer, UINT uSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBuffer", "uSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemWindowsDirectoryA(jitter):
    kernel32_GetSystemWindowsDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetSystemWindowsDirectoryW(jitter):
    kernel32_GetSystemWindowsDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetSystemWow64Directory(jitter, get_str, set_str):
    """"
    [Kernel32.dll] UINT GetSystemWow64Directory(LPTSTR lpBuffer, UINT uSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBuffer", "uSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemWow64DirectoryA(jitter):
    kernel32_GetSystemWow64Directory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetSystemWow64DirectoryW(jitter):
    kernel32_GetSystemWow64Directory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetVersion(jitter):
    """"
    [Kernel32.dll] DWORD GetVersion()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetVersionEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetVersionEx(LPOSVERSIONINFO lpVersionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpVersionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetVersionExA(jitter):
    kernel32_GetVersionEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetVersionExW(jitter):
    kernel32_GetVersionEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetWindowsDirectory(jitter, get_str, set_str):
    """"
    [Kernel32.dll] UINT GetWindowsDirectory(LPTSTR lpBuffer, UINT uSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBuffer", "uSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetWindowsDirectoryA(jitter):
    kernel32_GetWindowsDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetWindowsDirectoryW(jitter):
    kernel32_GetWindowsDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_IsProcessorFeaturePresent(jitter):
    """"
    [Kernel32.dll] BOOL IsProcessorFeaturePresent([ProcessorFeatureEnum] ProcessorFeature)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProcessorFeature"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetComputerName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetComputerName(LPCTSTR lpComputerName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpComputerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetComputerNameA(jitter):
    kernel32_SetComputerName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetComputerNameW(jitter):
    kernel32_SetComputerName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetComputerNameEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetComputerNameEx(COMPUTER_NAME_FORMAT NameType, LPCTSTR lpBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["NameType", "lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetComputerNameExA(jitter):
    kernel32_SetComputerNameEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetComputerNameExW(jitter):
    kernel32_SetComputerNameEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetFirmwareEnvironmentVariable(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetFirmwareEnvironmentVariable(LPCTSTR lpName, LPCTSTR lpGuid, PVOID pBuffer, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpName", "lpGuid", "pBuffer", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetFirmwareEnvironmentVariableA(jitter):
    kernel32_SetFirmwareEnvironmentVariable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetFirmwareEnvironmentVariableW(jitter):
    kernel32_SetFirmwareEnvironmentVariable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_VerifyVersionInfo(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL VerifyVersionInfo(LPOSVERSIONINFOEX lpVersionInfo, [NtVerType] dwTypeMask, DWORDLONG dwlConditionMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpVersionInfo", "dwTypeMask", "dwlConditionMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VerifyVersionInfoA(jitter):
    kernel32_VerifyVersionInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_VerifyVersionInfoW(jitter):
    kernel32_VerifyVersionInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_VerSetConditionMask(jitter):
    """"
    [Kernel32.dll] ULONGLONG VerSetConditionMask(ULONGLONG dwlConditionMask, [NtVerType] dwTypeBitMask, [VerOperator] dwConditionMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwlConditionMask", "dwTypeBitMask", "dwConditionMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_BackupRead(jitter):
    """"
    [Kernel32.dll] BOOL BackupRead(HANDLE hFile, LPBYTE lpBuffer, DWORD nNumberOfBytesToRead, LPDWORD lpNumberOfBytesRead, BOOL bAbort, BOOL bProcessSecurity, LPVOID* lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffer", "nNumberOfBytesToRead", "lpNumberOfBytesRead", "bAbort", "bProcessSecurity", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_BackupSeek(jitter):
    """"
    [Kernel32.dll] BOOL BackupSeek(HANDLE hFile, DWORD dwLowBytesToSeek, DWORD dwHighBytesToSeek, LPDWORD lpdwLowByteSeeked, LPDWORD lpdwHighByteSeeked, LPVOID* lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "dwLowBytesToSeek", "dwHighBytesToSeek", "lpdwLowByteSeeked", "lpdwHighByteSeeked", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_BackupWrite(jitter):
    """"
    [Kernel32.dll] BOOL BackupWrite(HANDLE hFile, LPBYTE lpBuffer, DWORD nNumberOfBytesToWrite, LPDWORD lpNumberOfBytesWritten, BOOL bAbort, BOOL bProcessSecurity, LPVOID* lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffer", "nNumberOfBytesToWrite", "lpNumberOfBytesWritten", "bAbort", "bProcessSecurity", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateTapePartition(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] CreateTapePartition(HANDLE hDevice, DWORD dwPartitionMethod, DWORD dwCount, DWORD dwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDevice", "dwPartitionMethod", "dwCount", "dwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EraseTape(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] EraseTape(HANDLE hDevice, DWORD dwEraseType, BOOL bImmediate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDevice", "dwEraseType", "bImmediate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetTapeParameters(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] GetTapeParameters(HANDLE hDevice, DWORD dwOperation, LPDWORD lpdwSize, LPVOID lpTapeInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDevice", "dwOperation", "lpdwSize", "lpTapeInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetTapePosition(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] GetTapePosition(HANDLE hDevice, DWORD dwPositionType, LPDWORD lpdwPartition, LPDWORD lpdwOffsetLow, LPDWORD lpdwOffsetHigh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDevice", "dwPositionType", "lpdwPartition", "lpdwOffsetLow", "lpdwOffsetHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetTapeStatus(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] GetTapeStatus(HANDLE hDevice)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDevice"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PrepareTape(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] PrepareTape(HANDLE hDevice, DWORD dwOperation, BOOL bImmediate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDevice", "dwOperation", "bImmediate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetTapeParameters(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] SetTapeParameters(HANDLE hDevice, DWORD dwOperation, LPVOID lpTapeInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDevice", "dwOperation", "lpTapeInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetTapePosition(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] SetTapePosition(HANDLE hDevice, DWORD dwPositionMethod, DWORD dwPartition, DWORD dwOffsetLow, DWORD dwOffsetHigh, BOOL bImmediate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDevice", "dwPositionMethod", "dwPartition", "dwOffsetLow", "dwOffsetHigh", "bImmediate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WriteTapemark(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] WriteTapemark(HANDLE hDevice, DWORD dwTapemarkType, DWORD dwTapemarkCount, BOOL bImmediate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDevice", "dwTapemarkType", "dwTapemarkCount", "bImmediate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ProcessIdToSessionId(jitter):
    """"
    [Kernel32.dll] BOOL ProcessIdToSessionId(DWORD dwProcessId, DWORD* pSessionId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwProcessId", "pSessionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WTSGetActiveConsoleSessionId(jitter):
    """"
    [Kernel32.dll] DWORD WTSGetActiveConsoleSessionId()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemTime(jitter):
    """"
    [Kernel32.dll] void GetSystemTime(LPSYSTEMTIME lpSystemTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemTimeAdjustment(jitter):
    """"
    [Kernel32.dll] BOOL GetSystemTimeAdjustment(PDWORD lpTimeAdjustment, PDWORD lpTimeIncrement, PBOOL lpTimeAdjustmentDisabled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTimeAdjustment", "lpTimeIncrement", "lpTimeAdjustmentDisabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetSystemTime(jitter):
    """"
    [Kernel32.dll] BOOL SetSystemTime(const SYSTEMTIME* lpSystemTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetSystemTimeAdjustment(jitter):
    """"
    [Kernel32.dll] BOOL SetSystemTimeAdjustment(DWORD dwTimeAdjustment, BOOL bTimeAdjustmentDisabled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTimeAdjustment", "bTimeAdjustmentDisabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FileTimeToLocalFileTime(jitter):
    """"
    [Kernel32.dll] BOOL FileTimeToLocalFileTime(const FILETIME* lpFileTime, LPFILETIME lpLocalFileTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileTime", "lpLocalFileTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDynamicTimeZoneInformation(jitter):
    """"
    [Kernel32.dll] DWORD GetDynamicTimeZoneInformation(PDYNAMIC_TIME_ZONE_INFORMATION pTimeZoneInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTimeZoneInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetLocalTime(jitter):
    """"
    [Kernel32.dll] void GetLocalTime(LPSYSTEMTIME lpSystemTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetTimeZoneInformation(jitter):
    """"
    [Kernel32.dll] DWORD GetTimeZoneInformation(LPTIME_ZONE_INFORMATION lpTimeZoneInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTimeZoneInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetTimeZoneInformationForYear(jitter):
    """"
    [Kernel32.dll] BOOL GetTimeZoneInformationForYear(USHORT wYear, PDYNAMIC_TIME_ZONE_INFORMATION pdtzi, LPTIME_ZONE_INFORMATION ptzi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["wYear", "pdtzi", "ptzi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetDynamicTimeZoneInformation(jitter):
    """"
    [Kernel32.dll] BOOL SetDynamicTimeZoneInformation(const DYNAMIC_TIME_ZONE_INFORMATION* lpTimeZoneInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTimeZoneInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetLocalTime(jitter):
    """"
    [Kernel32.dll] BOOL SetLocalTime(const SYSTEMTIME* lpSystemTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetTimeZoneInformation(jitter):
    """"
    [Kernel32.dll] BOOL SetTimeZoneInformation(const TIME_ZONE_INFORMATION* lpTimeZoneInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTimeZoneInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SystemTimeToTzSpecificLocalTime(jitter):
    """"
    [Kernel32.dll] BOOL SystemTimeToTzSpecificLocalTime(LPTIME_ZONE_INFORMATION lpTimeZone, LPSYSTEMTIME lpUniversalTime, LPSYSTEMTIME lpLocalTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTimeZone", "lpUniversalTime", "lpLocalTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TzSpecificLocalTimeToSystemTime(jitter):
    """"
    [Kernel32.dll] BOOL TzSpecificLocalTimeToSystemTime(LPTIME_ZONE_INFORMATION lpTimeZoneInformation, LPSYSTEMTIME lpLocalTime, LPSYSTEMTIME lpUniversalTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTimeZoneInformation", "lpLocalTime", "lpUniversalTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CompareFileTime(jitter):
    """"
    [Kernel32.dll] LONG CompareFileTime(const FILETIME* lpFileTime1, const FILETIME* lpFileTime2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileTime1", "lpFileTime2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FileTimeToSystemTime(jitter):
    """"
    [Kernel32.dll] BOOL FileTimeToSystemTime(const FILETIME* lpFileTime, LPSYSTEMTIME lpSystemTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileTime", "lpSystemTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFileTime(jitter):
    """"
    [Kernel32.dll] BOOL GetFileTime(HANDLE hFile, LPFILETIME lpCreationTime, LPFILETIME lpLastAccessTime, LPFILETIME lpLastWriteTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpCreationTime", "lpLastAccessTime", "lpLastWriteTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemTimeAsFileTime(jitter):
    """"
    [Kernel32.dll] void GetSystemTimeAsFileTime(LPFILETIME lpSystemTimeAsFileTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemTimeAsFileTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemTimePreciseAsFileTime(jitter):
    """"
    [Kernel32.dll] VOID GetSystemTimePreciseAsFileTime(LPFILETIME lpSystemTimeAsFileTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemTimeAsFileTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LocalFileTimeToFileTime(jitter):
    """"
    [Kernel32.dll] BOOL LocalFileTimeToFileTime(const FILETIME* lpLocalFileTime, LPFILETIME lpFileTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocalFileTime", "lpFileTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetFileTime(jitter):
    """"
    [Kernel32.dll] BOOL SetFileTime(HANDLE hFile, const FILETIME* lpCreationTime, const FILETIME* lpLastAccessTime, const FILETIME* lpLastWriteTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpCreationTime", "lpLastAccessTime", "lpLastWriteTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SystemTimeToFileTime(jitter):
    """"
    [Kernel32.dll] BOOL SystemTimeToFileTime(const SYSTEMTIME* lpSystemTime, LPFILETIME lpFileTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemTime", "lpFileTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DosDateTimeToFileTime(jitter):
    """"
    [Kernel32.dll] BOOL DosDateTimeToFileTime(WORD wFatDate, WORD wFatTime, LPFILETIME lpFileTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["wFatDate", "wFatTime", "lpFileTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FileTimeToDosDateTime(jitter):
    """"
    [Kernel32.dll] BOOL FileTimeToDosDateTime(const FILETIME* lpFileTime, LPWORD lpFatDate, LPWORD lpFatTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileTime", "lpFatDate", "lpFatTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemTimes(jitter):
    """"
    [Kernel32.dll] BOOL GetSystemTimes(LPFILETIME lpIdleTime, LPFILETIME lpKernelTime, LPFILETIME lpUserTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpIdleTime", "lpKernelTime", "lpUserTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetTickCount(jitter):
    """"
    [Kernel32.dll] DWORD GetTickCount()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetTickCount64(jitter):
    """"
    [Kernel32.dll] ULONGLONG GetTickCount64()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryPerformanceCounter(jitter):
    """"
    [Kernel32.dll] BOOL QueryPerformanceCounter(LARGE_INTEGER* lpPerformanceCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPerformanceCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryPerformanceFrequency(jitter):
    """"
    [Kernel32.dll] BOOL QueryPerformanceFrequency(LARGE_INTEGER* lpFrequency)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFrequency"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsDBCSLeadByte(jitter):
    """"
    [Kernel32.dll] BOOL IsDBCSLeadByte(BYTE TestChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TestChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_IsDBCSLeadByteEx(jitter):
    """"
    [Kernel32.dll] BOOL IsDBCSLeadByteEx([CodePageEnum] CodePage, BYTE TestChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CodePage", "TestChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_MultiByteToWideChar(jitter):
    """"
    [Kernel32.dll] int MultiByteToWideChar([CodePageEnum] CodePage, [MultiByteFlags] dwFlags, LPCSTR lpMultiByteStr, int cbMultiByte, LPWSTR lpWideCharStr, int cchWideChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CodePage", "dwFlags", "lpMultiByteStr", "cbMultiByte", "lpWideCharStr", "cchWideChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WideCharToMultiByte(jitter):
    """"
    [Kernel32.dll] int WideCharToMultiByte([CodePageEnum] CodePage, [WideCharFlags] dwFlags, LPCWSTR lpWideCharStr, int cchWideChar, LPSTR lpMultiByteStr, int cbMultiByte, LPCSTR lpDefaultChar, LPBOOL lpUsedDefaultChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CodePage", "dwFlags", "lpWideCharStr", "cchWideChar", "lpMultiByteStr", "cbMultiByte", "lpDefaultChar", "lpUsedDefaultChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VerLanguageName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD VerLanguageName(DWORD wLang, LPTSTR szLang, DWORD cchLang)
    """"
    ret_ad, args = jitter.func_args_stdcall(["wLang", "szLang", "cchLang"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_VerLanguageNameA(jitter):
    kernel32_VerLanguageName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_VerLanguageNameW(jitter):
    kernel32_VerLanguageName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_RaiseFailFastException(jitter):
    """"
    [Kernel32.dll] VOID RaiseFailFastException(PEXCEPTION_RECORD pExceptionRecord, PCONTEXT pContextRecord, [FAIL_FAST_EXCEPTION_FLAGS] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pExceptionRecord", "pContextRecord", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WerGetFlags(jitter):
    """"
    [Kernel32.dll] HRESULT WerGetFlags([ProcessHandle] hProcess, [WER_FAULT_REPORTING_FLAGS*] pdwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "pdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WerRegisterFile(jitter):
    """"
    [Kernel32.dll] HRESULT WerRegisterFile(PCWSTR pwzFile, WER_REGISTER_FILE_TYPE regFileType, [WerFileFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwzFile", "regFileType", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WerRegisterMemoryBlock(jitter):
    """"
    [Kernel32.dll] HRESULT WerRegisterMemoryBlock(PVOID pvAddress, DWORD dwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvAddress", "dwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WerRegisterRuntimeExceptionModule(jitter):
    """"
    [Kernel32.dll] HRESULT WerRegisterRuntimeExceptionModule(PCWSTR pwszOutOfProcessCallbackDll, PVOID pContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszOutOfProcessCallbackDll", "pContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WerSetFlags(jitter):
    """"
    [Kernel32.dll] HRESULT WerSetFlags([WER_FAULT_REPORTING_FLAGS] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WerUnregisterFile(jitter):
    """"
    [Kernel32.dll] HRESULT WerUnregisterFile(PCWSTR pwzFilePath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwzFilePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WerUnregisterMemoryBlock(jitter):
    """"
    [Kernel32.dll] HRESULT WerUnregisterMemoryBlock(PVOID pvAddress)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WerUnregisterRuntimeExceptionModule(jitter):
    """"
    [Kernel32.dll] HRESULT WerUnregisterRuntimeExceptionModule(PCWSTR pwszOutOfProcessCallbackDll, PVOID pContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszOutOfProcessCallbackDll", "pContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateDirectory(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL CreateDirectory(LPCTSTR lpPathName, LPSECURITY_ATTRIBUTES lpSecurityAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPathName", "lpSecurityAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateDirectoryA(jitter):
    kernel32_CreateDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateDirectoryW(jitter):
    kernel32_CreateDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateDirectoryEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL CreateDirectoryEx(LPCTSTR lpTemplateDirectory, LPCTSTR lpNewDirectory, LPSECURITY_ATTRIBUTES lpSecurityAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTemplateDirectory", "lpNewDirectory", "lpSecurityAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateDirectoryExA(jitter):
    kernel32_CreateDirectoryEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateDirectoryExW(jitter):
    kernel32_CreateDirectoryEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreateDirectoryTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL CreateDirectoryTransacted(LPCTSTR lpTemplateDirectory, LPCTSTR lpNewDirectory, LPSECURITY_ATTRIBUTES lpSecurityAttributes, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpTemplateDirectory", "lpNewDirectory", "lpSecurityAttributes", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateDirectoryTransactedA(jitter):
    kernel32_CreateDirectoryTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateDirectoryTransactedW(jitter):
    kernel32_CreateDirectoryTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindCloseChangeNotification(jitter):
    """"
    [Kernel32.dll] BOOL FindCloseChangeNotification(HANDLE hChangeHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hChangeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindFirstChangeNotification(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE FindFirstChangeNotification(LPCTSTR lpPathName, BOOL bWatchSubtree, [FILE_NOTIFY_CHANGE_FLAGS] dwNotifyFilter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPathName", "bWatchSubtree", "dwNotifyFilter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindFirstChangeNotificationA(jitter):
    kernel32_FindFirstChangeNotification(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FindFirstChangeNotificationW(jitter):
    kernel32_FindFirstChangeNotification(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindNextChangeNotification(jitter):
    """"
    [Kernel32.dll] BOOL FindNextChangeNotification(HANDLE hChangeHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hChangeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentDirectory(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetCurrentDirectory(DWORD nBufferLength, LPTSTR lpBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nBufferLength", "lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentDirectoryA(jitter):
    kernel32_GetCurrentDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetCurrentDirectoryW(jitter):
    kernel32_GetCurrentDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_ReadDirectoryChangesW(jitter):
    """"
    [Kernel32.dll] BOOL ReadDirectoryChangesW(HANDLE hDirectory, LPVOID lpBuffer, DWORD nBufferLength, BOOL bWatchSubtree, [FILE_NOTIFY_CHANGE_FLAGS] dwNotifyFilter, LPDWORD lpBytesReturned, LPOVERLAPPED lpOverlapped, LPOVERLAPPED_COMPLETION_ROUTINE lpCompletionRoutine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDirectory", "lpBuffer", "nBufferLength", "bWatchSubtree", "dwNotifyFilter", "lpBytesReturned", "lpOverlapped", "lpCompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RemoveDirectory(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL RemoveDirectory(LPCTSTR lpPathName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPathName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RemoveDirectoryA(jitter):
    kernel32_RemoveDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_RemoveDirectoryW(jitter):
    kernel32_RemoveDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_RemoveDirectoryTransacted(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL RemoveDirectoryTransacted(LPCTSTR lpPathName, HANDLE hTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPathName", "hTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_RemoveDirectoryTransactedA(jitter):
    kernel32_RemoveDirectoryTransacted(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_RemoveDirectoryTransactedW(jitter):
    kernel32_RemoveDirectoryTransacted(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetCurrentDirectory(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetCurrentDirectory(LPCTSTR lpPathName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPathName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetCurrentDirectoryA(jitter):
    kernel32_SetCurrentDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetCurrentDirectoryW(jitter):
    kernel32_SetCurrentDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetDiskFreeSpace(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetDiskFreeSpace(LPCTSTR lpRootPathName, LPDWORD lpSectorsPerCluster, LPDWORD lpBytesPerSector, LPDWORD lpNumberOfFreeClusters, LPDWORD lpTotalNumberOfClusters)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpRootPathName", "lpSectorsPerCluster", "lpBytesPerSector", "lpNumberOfFreeClusters", "lpTotalNumberOfClusters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDiskFreeSpaceA(jitter):
    kernel32_GetDiskFreeSpace(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetDiskFreeSpaceW(jitter):
    kernel32_GetDiskFreeSpace(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetDiskFreeSpaceEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetDiskFreeSpaceEx(LPCTSTR lpDirectoryName, PULARGE_INTEGER lpFreeBytesAvailable, PULARGE_INTEGER lpTotalNumberOfBytes, PULARGE_INTEGER lpTotalNumberOfFreeBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpDirectoryName", "lpFreeBytesAvailable", "lpTotalNumberOfBytes", "lpTotalNumberOfFreeBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDiskFreeSpaceExA(jitter):
    kernel32_GetDiskFreeSpaceEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetDiskFreeSpaceExW(jitter):
    kernel32_GetDiskFreeSpaceEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_DefineDosDevice(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL DefineDosDevice([DDD_FLAGS] dwFlags, LPCTSTR lpDeviceName, LPCTSTR lpTargetPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpDeviceName", "lpTargetPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DefineDosDeviceA(jitter):
    kernel32_DefineDosDevice(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_DefineDosDeviceW(jitter):
    kernel32_DefineDosDevice(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_DeleteVolumeMountPoint(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL DeleteVolumeMountPoint(LPCTSTR lpszVolumeMountPoint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszVolumeMountPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DeleteVolumeMountPointA(jitter):
    kernel32_DeleteVolumeMountPoint(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_DeleteVolumeMountPointW(jitter):
    kernel32_DeleteVolumeMountPoint(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindFirstVolume(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE FindFirstVolume(LPTSTR lpszVolumeName, DWORD cchBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszVolumeName", "cchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindFirstVolumeA(jitter):
    kernel32_FindFirstVolume(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FindFirstVolumeW(jitter):
    kernel32_FindFirstVolume(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindNextVolume(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL FindNextVolume(HANDLE hFindVolume, LPTSTR lpszVolumeName, DWORD cchBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFindVolume", "lpszVolumeName", "cchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindNextVolumeA(jitter):
    kernel32_FindNextVolume(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FindNextVolumeW(jitter):
    kernel32_FindNextVolume(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindNextVolumeMountPoint(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL FindNextVolumeMountPoint(HANDLE hFindVolumeMountPoint, LPTSTR lpszVolumeMountPoint, DWORD cchBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFindVolumeMountPoint", "lpszVolumeMountPoint", "cchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindNextVolumeMountPointA(jitter):
    kernel32_FindNextVolumeMountPoint(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FindNextVolumeMountPointW(jitter):
    kernel32_FindNextVolumeMountPoint(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindVolumeClose(jitter):
    """"
    [Kernel32.dll] BOOL FindVolumeClose(HANDLE hFindVolume)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFindVolume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindVolumeMountPointClose(jitter):
    """"
    [Kernel32.dll] BOOL FindVolumeMountPointClose(HANDLE hFindVolumeMountPoint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFindVolumeMountPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDriveType(jitter, get_str, set_str):
    """"
    [Kernel32.dll] [DRIVE_TYPE] GetDriveType(LPCTSTR lpRootPathName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpRootPathName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetDriveTypeA(jitter):
    kernel32_GetDriveType(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetDriveTypeW(jitter):
    kernel32_GetDriveType(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetLogicalDrives(jitter):
    """"
    [Kernel32.dll] DWORD GetLogicalDrives()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetLogicalDriveStrings(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD GetLogicalDriveStrings(DWORD nBufferLength, LPTSTR lpBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nBufferLength", "lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetLogicalDriveStringsA(jitter):
    kernel32_GetLogicalDriveStrings(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetLogicalDriveStringsW(jitter):
    kernel32_GetLogicalDriveStrings(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetVolumeInformation(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetVolumeInformation(LPCTSTR lpRootPathName, LPTSTR lpVolumeNameBuffer, DWORD nVolumeNameSize, LPDWORD lpVolumeSerialNumber, LPDWORD lpMaximumComponentLength, [LPFILE_SYSTEM_FLAGS] lpFileSystemFlags, LPTSTR lpFileSystemNameBuffer, DWORD nFileSystemNameSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpRootPathName", "lpVolumeNameBuffer", "nVolumeNameSize", "lpVolumeSerialNumber", "lpMaximumComponentLength", "lpFileSystemFlags", "lpFileSystemNameBuffer", "nFileSystemNameSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetVolumeInformationA(jitter):
    kernel32_GetVolumeInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetVolumeInformationW(jitter):
    kernel32_GetVolumeInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetVolumeInformationByHandleW(jitter):
    """"
    [Kernel32.dll] BOOL GetVolumeInformationByHandleW(HANDLE hFile, LPTSTR lpVolumeNameBuffer, DWORD nVolumeNameSize, LPDWORD lpVolumeSerialNumber, LPDWORD lpMaximumComponentLength, [LPFILE_SYSTEM_FLAGS] lpFileSystemFlags, LPTSTR lpFileSystemNameBuffer, DWORD nFileSystemNameSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpVolumeNameBuffer", "nVolumeNameSize", "lpVolumeSerialNumber", "lpMaximumComponentLength", "lpFileSystemFlags", "lpFileSystemNameBuffer", "nFileSystemNameSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetVolumeNameForVolumeMountPoint(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetVolumeNameForVolumeMountPoint(LPCTSTR lpszVolumeMountPoint, LPTSTR lpszVolumeName, DWORD cchBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszVolumeMountPoint", "lpszVolumeName", "cchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetVolumeNameForVolumeMountPointA(jitter):
    kernel32_GetVolumeNameForVolumeMountPoint(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetVolumeNameForVolumeMountPointW(jitter):
    kernel32_GetVolumeNameForVolumeMountPoint(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetVolumePathName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetVolumePathName(LPCTSTR lpszFileName, LPTSTR lpszVolumePathName, DWORD cchBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszFileName", "lpszVolumePathName", "cchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetVolumePathNameA(jitter):
    kernel32_GetVolumePathName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetVolumePathNameW(jitter):
    kernel32_GetVolumePathName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetVolumePathNamesForVolumeName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetVolumePathNamesForVolumeName(LPCTSTR lpszVolumeName, LPTSTR lpszVolumePathNames, DWORD cchBufferLength, PDWORD lpcchReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszVolumeName", "lpszVolumePathNames", "cchBufferLength", "lpcchReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetVolumePathNamesForVolumeNameA(jitter):
    kernel32_GetVolumePathNamesForVolumeName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetVolumePathNamesForVolumeNameW(jitter):
    kernel32_GetVolumePathNamesForVolumeName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_QueryDosDevice(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD QueryDosDevice(LPCTSTR lpDeviceName, LPTSTR lpTargetPath, DWORD ucchMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpDeviceName", "lpTargetPath", "ucchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryDosDeviceA(jitter):
    kernel32_QueryDosDevice(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_QueryDosDeviceW(jitter):
    kernel32_QueryDosDevice(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetVolumeLabel(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetVolumeLabel(LPCTSTR lpRootPathName, LPCTSTR lpVolumeName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpRootPathName", "lpVolumeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetVolumeLabelA(jitter):
    kernel32_SetVolumeLabel(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetVolumeLabelW(jitter):
    kernel32_SetVolumeLabel(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_FindFirstVolumeMountPoint(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE FindFirstVolumeMountPoint(LPTSTR lpszRootPathName, LPTSTR lpszVolumeMountPoint, DWORD cchBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszRootPathName", "lpszVolumeMountPoint", "cchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_FindFirstVolumeMountPointA(jitter):
    kernel32_FindFirstVolumeMountPoint(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_FindFirstVolumeMountPointW(jitter):
    kernel32_FindFirstVolumeMountPoint(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_SetVolumeMountPoint(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL SetVolumeMountPoint(LPCTSTR lpszVolumeMountPoint, LPCTSTR lpszVolumeName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszVolumeMountPoint", "lpszVolumeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetVolumeMountPointA(jitter):
    kernel32_SetVolumeMountPoint(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_SetVolumeMountPointW(jitter):
    kernel32_SetVolumeMountPoint(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_CreatePipe(jitter):
    """"
    [Kernel32.dll] BOOL CreatePipe(PHANDLE hReadPipe, PHANDLE hWritePipe, LPSECURITY_ATTRIBUTES lpPipeAttributes, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hReadPipe", "hWritePipe", "lpPipeAttributes", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CallNamedPipe(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL CallNamedPipe(LPCTSTR lpNamedPipeName, LPVOID lpInBuffer, DWORD nInBufferSize, LPVOID lpOutBuffer, DWORD nOutBufferSize, LPDWORD lpBytesRead, [NMPWAIT] nTimeOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpNamedPipeName", "lpInBuffer", "nInBufferSize", "lpOutBuffer", "nOutBufferSize", "lpBytesRead", "nTimeOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CallNamedPipeA(jitter):
    kernel32_CallNamedPipe(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CallNamedPipeW(jitter):
    kernel32_CallNamedPipe(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_ConnectNamedPipe(jitter):
    """"
    [Kernel32.dll] BOOL ConnectNamedPipe(HANDLE hNamedPipe, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hNamedPipe", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateNamedPipe(jitter, get_str, set_str):
    """"
    [Kernel32.dll] HANDLE CreateNamedPipe(LPCTSTR lpName, [PIPE_ACCESS] dwOpenMode, [PIPE_MODE] dwPipeMode, DWORD nMaxInstances, DWORD nOutBufferSize, DWORD nInBufferSize, DWORD nDefaultTimeOut, LPSECURITY_ATTRIBUTES lpSecurityAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpName", "dwOpenMode", "dwPipeMode", "nMaxInstances", "nOutBufferSize", "nInBufferSize", "nDefaultTimeOut", "lpSecurityAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CreateNamedPipeA(jitter):
    kernel32_CreateNamedPipe(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_CreateNamedPipeW(jitter):
    kernel32_CreateNamedPipe(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_DisconnectNamedPipe(jitter):
    """"
    [Kernel32.dll] BOOL DisconnectNamedPipe(HANDLE hNamedPipe)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hNamedPipe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNamedPipeClientComputerName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetNamedPipeClientComputerName(HANDLE Pipe, LPTSTR ClientComputerName, ULONG ClientComputerNameLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Pipe", "ClientComputerName", "ClientComputerNameLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNamedPipeClientComputerNameA(jitter):
    kernel32_GetNamedPipeClientComputerName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetNamedPipeClientComputerNameW(jitter):
    kernel32_GetNamedPipeClientComputerName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetNamedPipeClientProcessId(jitter):
    """"
    [Kernel32.dll] BOOL GetNamedPipeClientProcessId(HANDLE Pipe, PULONG ClientProcessId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Pipe", "ClientProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNamedPipeClientSessionId(jitter):
    """"
    [Kernel32.dll] BOOL GetNamedPipeClientSessionId(HANDLE Pipe, PULONG ClientSessionId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Pipe", "ClientSessionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNamedPipeHandleState(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL GetNamedPipeHandleState(HANDLE hNamedPipe, [PIPE_STATE*] lpState, LPDWORD lpCurInstances, LPDWORD lpMaxCollectionCount, LPDWORD lpCollectDataTimeout, LPTSTR lpUserName, DWORD nMaxUserNameSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hNamedPipe", "lpState", "lpCurInstances", "lpMaxCollectionCount", "lpCollectDataTimeout", "lpUserName", "nMaxUserNameSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNamedPipeHandleStateA(jitter):
    kernel32_GetNamedPipeHandleState(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_GetNamedPipeHandleStateW(jitter):
    kernel32_GetNamedPipeHandleState(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetNamedPipeInfo(jitter):
    """"
    [Kernel32.dll] BOOL GetNamedPipeInfo(HANDLE hNamedPipe, [PIPE_TYPE*] lpFlags, LPDWORD lpOutBufferSize, LPDWORD lpInBufferSize, LPDWORD lpMaxInstances)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hNamedPipe", "lpFlags", "lpOutBufferSize", "lpInBufferSize", "lpMaxInstances"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNamedPipeServerProcessId(jitter):
    """"
    [Kernel32.dll] BOOL GetNamedPipeServerProcessId(HANDLE Pipe, PULONG ServerProcessId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Pipe", "ServerProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetNamedPipeServerSessionId(jitter):
    """"
    [Kernel32.dll] BOOL GetNamedPipeServerSessionId(HANDLE Pipe, PULONG ServerSessionId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Pipe", "ServerSessionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PeekNamedPipe(jitter):
    """"
    [Kernel32.dll] BOOL PeekNamedPipe(HANDLE hNamedPipe, LPVOID lpBuffer, DWORD nBufferSize, LPDWORD lpBytesRead, LPDWORD lpTotalBytesAvail, LPDWORD lpBytesLeftThisMessage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hNamedPipe", "lpBuffer", "nBufferSize", "lpBytesRead", "lpTotalBytesAvail", "lpBytesLeftThisMessage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetNamedPipeHandleState(jitter):
    """"
    [Kernel32.dll] BOOL SetNamedPipeHandleState(HANDLE hNamedPipe, [PIPE_MODE*] lpMode, LPDWORD lpMaxCollectionCount, LPDWORD lpCollectDataTimeout)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hNamedPipe", "lpMode", "lpMaxCollectionCount", "lpCollectDataTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_TransactNamedPipe(jitter):
    """"
    [Kernel32.dll] BOOL TransactNamedPipe(HANDLE hNamedPipe, LPVOID lpInBuffer, DWORD nInBufferSize, LPVOID lpOutBuffer, DWORD nOutBufferSize, LPDWORD lpBytesRead, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hNamedPipe", "lpInBuffer", "nInBufferSize", "lpOutBuffer", "nOutBufferSize", "lpBytesRead", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WaitNamedPipe(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL WaitNamedPipe(LPCTSTR lpNamedPipeName, [NMPWAIT] nTimeOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpNamedPipeName", "nTimeOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_WaitNamedPipeA(jitter):
    kernel32_WaitNamedPipe(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_WaitNamedPipeW(jitter):
    kernel32_WaitNamedPipe(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_DisableThreadProfiling(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] DisableThreadProfiling(HANDLE PerformanceDataHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PerformanceDataHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnableThreadProfiling(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] EnableThreadProfiling([ThreadHandle] ThreadHandle, [THREAD_PROFILING_FLAGS] Flags, DWORD64 HardwareCounters, HANDLE PerformanceDataHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "Flags", "HardwareCounters", "PerformanceDataHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_QueryThreadProfiling(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] QueryThreadProfiling([ThreadHandle] ThreadHandle, PBOOLEAN Enabled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "Enabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ReadThreadProfilingData(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] ReadThreadProfilingData(HANDLE PerformanceDataHandle, [READ_THREAD_PROFILING_FLAGS] Flags, PPERFORMANCE_DATA PerformanceData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PerformanceDataHandle", "Flags", "PerformanceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_BaseFormatTimeOut(jitter):
    """"
    [Kernel32.dll] LARGE_INTEGER* BaseFormatTimeOut(LARGE_INTEGER* pLITimeout, DWORD dwMillis)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pLITimeout", "dwMillis"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_BaseGetNamedObjectDirectory(jitter):
    """"
    [Kernel32.dll] NTSTATUS BaseGetNamedObjectDirectory(HANDLE* phDir)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phDir"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_Basep8BitStringToDynamicUnicodeString(jitter):
    """"
    [Kernel32.dll] BOOL Basep8BitStringToDynamicUnicodeString(PUNICODE_STRING pConvertedStr, LPCSTR pszAnsiStr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pConvertedStr", "pszAnsiStr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CheckElevationEnabled(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] CheckElevationEnabled(BOOL* pResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ConsoleMenuControl(jitter):
    """"
    [Kernel32.dll] HMENU ConsoleMenuControl(HANDLE hConOut, DWORD cmdIdLow, DWORD cmdIdHigh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConOut", "cmdIdLow", "cmdIdHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleCursor(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleCursor(HANDLE hConsole, HCURSOR hCursor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsole", "hCursor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetConsoleMaximumWindowSize(jitter):
    """"
    [Kernel32.dll] BOOL SetConsoleMaximumWindowSize(HANDLE hConsole, DWORD dwUnk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsole", "dwUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetStdHandleEx(jitter):
    """"
    [Kernel32.dll] BOOL SetStdHandleEx([StdHandle] dwStdHandle, HANDLE hNewHandle, HANDLE* phOldHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwStdHandle", "hNewHandle", "phOldHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ShowConsoleCursor(jitter):
    """"
    [Kernel32.dll] int ShowConsoleCursor(HANDLE hConsoleOutput, BOOL bShow)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConsoleOutput", "bShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AddLocalAlternateComputerName(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] AddLocalAlternateComputerName(LPCTSTR lpDnsFQHostname, ULONG ulFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpDnsFQHostname", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DelayLoadFailureHook(jitter):
    """"
    [Kernel32.dll] FARPROC DelayLoadFailureHook(LPCSTR pszDllName, LPCSTR pszProcName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszDllName", "pszProcName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ResolveDelayLoadedAPI(jitter):
    """"
    [Kernel32.dll] PVOID ResolveDelayLoadedAPI([HMODULE-PVOID] ParentModuleBase, PCIMAGE_DELAYLOAD_DESCRIPTOR DelayloadDescriptor, PDELAYLOAD_FAILURE_DLL_CALLBACK FailureDllHook, PDELAYLOAD_FAILURE_SYSTEM_ROUTINE FailureSystemHook, PIMAGE_THUNK_DATA ThunkAddress, ULONG Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ParentModuleBase", "DelayloadDescriptor", "FailureDllHook", "FailureSystemHook", "ThunkAddress", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ResolveDelayLoadsFromDll(jitter):
    """"
    [Kernel32.dll] NTSTATUS ResolveDelayLoadsFromDll([HMODULE-PVOID] ParentBase, LPCSTR TargetDllName, ULONG Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ParentBase", "TargetDllName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DecodePointer(jitter):
    """"
    [Kernel32.dll] PVOID DecodePointer(PVOID Ptr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_DecodeSystemPointer(jitter):
    """"
    [Kernel32.dll] PVOID DecodeSystemPointer(PVOID Ptr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EncodePointer(jitter):
    """"
    [Kernel32.dll] PVOID EncodePointer(PVOID Ptr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EncodeSystemPointer(jitter):
    """"
    [Kernel32.dll] PVOID EncodeSystemPointer(PVOID Ptr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_MulDiv(jitter):
    """"
    [Kernel32.dll] int MulDiv(int nNumber, int nNumerator, int nDenominator)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nNumber", "nNumerator", "nDenominator"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CheckTokenCapability(jitter):
    """"
    [Kernel32.dll] BOOL CheckTokenCapability(HANDLE TokenHandle, PSID CapabilitySidToCheck, PBOOL HasCapability)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TokenHandle", "CapabilitySidToCheck", "HasCapability"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CheckTokenMembershipEx(jitter):
    """"
    [Kernel32.dll] BOOL CheckTokenMembershipEx(HANDLE TokenHandle, PSID SidToCheck, [CTM_FLAGS] Flags, PBOOL IsMember)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TokenHandle", "SidToCheck", "Flags", "IsMember"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AddResourceAttributeAce(jitter):
    """"
    [Kernel32.dll] BOOL AddResourceAttributeAce(PACL pAcl, DWORD dwAceRevision, [AceFlags] AceFlags, [ACCESS_MASK_DWORD] AccessMask, PSID pSid, PCLAIM_SECURITY_ATTRIBUTES_INFORMATION pAttributeInfo, PDWORD pReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AceFlags", "AccessMask", "pSid", "pAttributeInfo", "pReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_AddScopedPolicyIDAce(jitter):
    """"
    [Kernel32.dll] BOOL AddScopedPolicyIDAce(PACL pAcl, DWORD dwAceRevision, [AceFlags] AceFlags, [ACCESS_MASK_DWORD] AccessMask, PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AceFlags", "AccessMask", "pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_ClosePackageInfo(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] ClosePackageInfo(PACKAGE_INFO_REFERENCE packageInfoReference)
    """"
    ret_ad, args = jitter.func_args_stdcall(["packageInfoReference"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetApplicationUserModelId(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] GetApplicationUserModelId(HANDLE hProcess, UINT32* applicationUserModelIdLength, PWSTR applicationUserModelId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "applicationUserModelIdLength", "applicationUserModelId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentApplicationUserModelId(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] GetCurrentApplicationUserModelId(UINT32* applicationUserModelIdLength, PWSTR applicationUserModelId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["applicationUserModelIdLength", "applicationUserModelId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentPackageFamilyName(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] GetCurrentPackageFamilyName(UINT32* packageFamilyNameLength, PWSTR packageFamilyName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["packageFamilyNameLength", "packageFamilyName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentPackageFullName(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] GetCurrentPackageFullName(UINT32* packageFullNameLength, PWSTR packageFullName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["packageFullNameLength", "packageFullName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentPackageId(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] GetCurrentPackageId(UINT32* bufferLength, BYTE* buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bufferLength", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentPackageInfo(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] GetCurrentPackageInfo([PACKAGE_FILTER_FLAGS] flags, UINT32* bufferLength, BYTE* buffer, UINT32* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["flags", "bufferLength", "buffer", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetCurrentPackagePath(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] GetCurrentPackagePath(UINT32* pathLength, PWSTR path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pathLength", "path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPackageFamilyName(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] GetPackageFamilyName(HANDLE hProcess, UINT32* packageFamilyNameLength, PWSTR packageFamilyName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "packageFamilyNameLength", "packageFamilyName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPackageFullName(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] GetPackageFullName(HANDLE hProcess, UINT32* packageFullNameLength, PWSTR packageFullName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "packageFullNameLength", "packageFullName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPackageId(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] GetPackageId(HANDLE hProcess, UINT32* bufferLength, BYTE* pBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "bufferLength", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPackageInfo(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] GetPackageInfo(PACKAGE_INFO_REFERENCE packageInfoReference, [PACKAGE_CONSTANTS] flags, UINT32* bufferLength, BYTE* buffer, UINT32* count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["packageInfoReference", "flags", "bufferLength", "buffer", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPackagePath(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] GetPackagePath(const PACKAGE_ID* packageId, const UINT32 reserved, UINT32* pathLength, PWSTR path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["packageId", "reserved", "pathLength", "path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetPackagesByPackageFamily(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] GetPackagesByPackageFamily(PWSTR packageFamilyName, UINT32* count, PWSTR* packageFullNames, UINT32* bufferLength, WCHAR* buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["packageFamilyName", "count", "packageFullNames", "bufferLength", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_OpenPackageInfoByFullName(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] OpenPackageInfoByFullName(PCWSTR packageFullName, const UINT32 reserved, PACKAGE_INFO_REFERENCE* packageInfoReference)
    """"
    ret_ad, args = jitter.func_args_stdcall(["packageFullName", "reserved", "packageInfoReference"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PackageFamilyNameFromFullName(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] PackageFamilyNameFromFullName(PCWSTR packageFullName, UINT32* packageFamilyNameLength, PWSTR packageFamilyName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["packageFullName", "packageFamilyNameLength", "packageFamilyName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PackageFamilyNameFromId(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] PackageFamilyNameFromId(const PACKAGE_ID* packageId, UINT32* packageFamilyNameLength, PWSTR packageFamilyName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["packageId", "packageFamilyNameLength", "packageFamilyName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PackageFullNameFromId(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] PackageFullNameFromId(const PACKAGE_ID* packageId, UINT32* packageFullNameLength, PWSTR packageFullName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["packageId", "packageFullNameLength", "packageFullName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PackageIdFromFullName(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] PackageIdFromFullName(PCWSTR packageFullName, [PACKAGE_INFORMATION_FLAGS] flags, UINT32* bufferLength, BYTE* buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["packageFullName", "flags", "bufferLength", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_PackageNameAndPublisherIdFromFamilyName(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE_LONG] PackageNameAndPublisherIdFromFamilyName(PCWSTR packageFamilyName, UINT32* packageNameLength, PWSTR packageName, UINT32* packagePublisherIdLength, PWSTR packagePublisherId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["packageFamilyName", "packageNameLength", "packageName", "packagePublisherIdLength", "packagePublisherId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32EmptyWorkingSet(jitter):
    """"
    [Kernel32.dll] BOOL K32EmptyWorkingSet([ProcessHandle] hProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32EnumDeviceDrivers(jitter):
    """"
    [Kernel32.dll] BOOL K32EnumDeviceDrivers(LPVOID* lpImageBase, DWORD cb, LPDWORD lpcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpImageBase", "cb", "lpcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32EnumPageFiles(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL K32EnumPageFiles(PENUM_PAGE_CALLBACK pCallbackRoutine, LPVOID lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCallbackRoutine", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32EnumPageFilesA(jitter):
    kernel32_K32EnumPageFiles(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_K32EnumPageFilesW(jitter):
    kernel32_K32EnumPageFiles(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_K32EnumProcesses(jitter):
    """"
    [Kernel32.dll] BOOL K32EnumProcesses(DWORD* pProcessIds, DWORD cb, DWORD* pBytesReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pProcessIds", "cb", "pBytesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32EnumProcessModules(jitter):
    """"
    [Kernel32.dll] BOOL K32EnumProcessModules([ProcessHandle] hProcess, HMODULE* lphModule, DWORD cb, LPDWORD lpcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lphModule", "cb", "lpcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32EnumProcessModulesEx(jitter):
    """"
    [Kernel32.dll] BOOL K32EnumProcessModulesEx([ProcessHandle] hProcess, HMODULE* lphModule, DWORD cb, LPDWORD lpcbNeeded, DWORD dwFilterFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lphModule", "cb", "lpcbNeeded", "dwFilterFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32GetDeviceDriverBaseName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD K32GetDeviceDriverBaseName(LPVOID ImageBase, LPTSTR lpBaseName, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ImageBase", "lpBaseName", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32GetDeviceDriverBaseNameA(jitter):
    kernel32_K32GetDeviceDriverBaseName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_K32GetDeviceDriverBaseNameW(jitter):
    kernel32_K32GetDeviceDriverBaseName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_K32GetDeviceDriverFileName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD K32GetDeviceDriverFileName(LPVOID ImageBase, LPTSTR lpFilename, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ImageBase", "lpFilename", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32GetDeviceDriverFileNameA(jitter):
    kernel32_K32GetDeviceDriverFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_K32GetDeviceDriverFileNameW(jitter):
    kernel32_K32GetDeviceDriverFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_K32GetMappedFileName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD K32GetMappedFileName([ProcessHandle] hProcess, LPVOID lpv, LPTSTR lpFilename, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpv", "lpFilename", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32GetMappedFileNameA(jitter):
    kernel32_K32GetMappedFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_K32GetMappedFileNameW(jitter):
    kernel32_K32GetMappedFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_K32GetModuleBaseName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD K32GetModuleBaseName([ProcessHandle] hProcess, HMODULE hModule, LPTSTR lpBaseName, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hModule", "lpBaseName", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32GetModuleBaseNameA(jitter):
    kernel32_K32GetModuleBaseName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_K32GetModuleBaseNameW(jitter):
    kernel32_K32GetModuleBaseName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_K32GetModuleFileNameEx(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD K32GetModuleFileNameEx([ProcessHandle] hProcess, HMODULE hModule, LPTSTR lpFilename, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hModule", "lpFilename", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32GetModuleFileNameExA(jitter):
    kernel32_K32GetModuleFileNameEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_K32GetModuleFileNameExW(jitter):
    kernel32_K32GetModuleFileNameEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_K32GetModuleInformation(jitter):
    """"
    [Kernel32.dll] BOOL K32GetModuleInformation([ProcessHandle] hProcess, HMODULE hModule, LPMODULEINFO lpmodinfo, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hModule", "lpmodinfo", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32GetPerformanceInfo(jitter):
    """"
    [Kernel32.dll] BOOL K32GetPerformanceInfo(PPERFORMANCE_INFORMATION pPerformanceInformation, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPerformanceInformation", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32GetProcessImageFileName(jitter, get_str, set_str):
    """"
    [Kernel32.dll] DWORD K32GetProcessImageFileName([ProcessHandle] hProcess, LPTSTR lpImageFileName, DWORD nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpImageFileName", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32GetProcessImageFileNameA(jitter):
    kernel32_K32GetProcessImageFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_K32GetProcessImageFileNameW(jitter):
    kernel32_K32GetProcessImageFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_K32GetProcessMemoryInfo(jitter):
    """"
    [Kernel32.dll] BOOL K32GetProcessMemoryInfo(HANDLE Process, PPROCESS_MEMORY_COUNTERS ppsmemCounters, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Process", "ppsmemCounters", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32GetWsChanges(jitter):
    """"
    [Kernel32.dll] BOOL K32GetWsChanges([ProcessHandle] hProcess, PPSAPI_WS_WATCH_INFORMATION lpWatchInfo, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpWatchInfo", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32GetWsChangesEx(jitter):
    """"
    [Kernel32.dll] BOOL K32GetWsChangesEx([ProcessHandle] hProcess, PPSAPI_WS_WATCH_INFORMATION_EX lpWatchInfoEx, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "lpWatchInfoEx", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32InitializeProcessForWsWatch(jitter):
    """"
    [Kernel32.dll] BOOL K32InitializeProcessForWsWatch([ProcessHandle] hProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32QueryWorkingSet(jitter):
    """"
    [Kernel32.dll] BOOL K32QueryWorkingSet([ProcessHandle] hProcess, PVOID pv, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "pv", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_K32QueryWorkingSetEx(jitter):
    """"
    [Kernel32.dll] BOOL K32QueryWorkingSetEx([ProcessHandle] hProcess, PVOID pv, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "pv", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumUILanguages(jitter, get_str, set_str):
    """"
    [Kernel32.dll] BOOL EnumUILanguages(UILANGUAGE_ENUMPROC lpUILanguageEnumProc, [EnumUILanguages_FLAGS] dwFlags, LONG_PTR lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpUILanguageEnumProc", "dwFlags", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_EnumUILanguagesA(jitter):
    kernel32_EnumUILanguages(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def kernel32_EnumUILanguagesW(jitter):
    kernel32_EnumUILanguages(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def kernel32_GetFileMUIInfo(jitter):
    """"
    [Kernel32.dll] BOOL GetFileMUIInfo([GetFileMUIInfo_FLAGS] dwFlags, PCWSTR pcwszFilePath, PFILEMUIINFO pFileMUIInfo, DWORD* pcbFileMUIInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pcwszFilePath", "pFileMUIInfo", "pcbFileMUIInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetFileMUIPath(jitter):
    """"
    [Kernel32.dll] BOOL GetFileMUIPath(DWORD dwFlags, PCWSTR pcwszFilePath, PWSTR pwszLanguage, PULONG pcchLanguage, PWSTR pwszFileMUIPath, PULONG pcchFileMUIPath, PULONGLONG pululEnumerator)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pcwszFilePath", "pwszLanguage", "pcchLanguage", "pwszFileMUIPath", "pcchFileMUIPath", "pululEnumerator"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetProcessPreferredUILanguages(jitter):
    """"
    [Kernel32.dll] BOOL GetProcessPreferredUILanguages([MUI_LANGUAGE_FORMAT_FLAGS] dwFlags, PULONG pulNumLanguages, PZZWSTR pwszLanguagesBuffer, PULONG pcchLanguagesBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pulNumLanguages", "pwszLanguagesBuffer", "pcchLanguagesBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemDefaultUILanguage(jitter):
    """"
    [Kernel32.dll] LANGID GetSystemDefaultUILanguage()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetSystemPreferredUILanguages(jitter):
    """"
    [Kernel32.dll] BOOL GetSystemPreferredUILanguages([GetSystemPreferredUILanguages_FLAGS] dwFlags, PULONG pulNumLanguages, PZZWSTR pwszLanguagesBuffer, PULONG pcchLanguagesBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pulNumLanguages", "pwszLanguagesBuffer", "pcchLanguagesBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadPreferredUILanguages(jitter):
    """"
    [Kernel32.dll] BOOL GetThreadPreferredUILanguages([GetThreadPreferredUILanguages_FLAGS] dwFlags, PULONG pulNumLanguages, PZZWSTR pwszLanguagesBuffer, PULONG pcchLanguagesBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pulNumLanguages", "pwszLanguagesBuffer", "pcchLanguagesBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetThreadUILanguage(jitter):
    """"
    [Kernel32.dll] LANGID GetThreadUILanguage()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetUILanguageInfo(jitter):
    """"
    [Kernel32.dll] BOOL GetUILanguageInfo([MUI_LANGUAGE_FORMAT_FLAGS] dwFlags, PCZZWSTR pwmszLanguage, PZZWSTR pwszFallbackLanguages, PDWORD pcchFallbackLanguages, [MUI_LANGUAGE_ATTRIBUTES*] pdwAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pwmszLanguage", "pwszFallbackLanguages", "pcchFallbackLanguages", "pdwAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetUserDefaultUILanguage(jitter):
    """"
    [Kernel32.dll] LANGID GetUserDefaultUILanguage()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetUserPreferredUILanguages(jitter):
    """"
    [Kernel32.dll] BOOL GetUserPreferredUILanguages([MUI_LANGUAGE_FORMAT_FLAGS] dwFlags, PULONG pulNumLanguages, PZZWSTR pwszLanguagesBuffer, PULONG pcchLanguagesBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pulNumLanguages", "pwszLanguagesBuffer", "pcchLanguagesBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetProcessPreferredUILanguages(jitter):
    """"
    [Kernel32.dll] BOOL SetProcessPreferredUILanguages([MUI_LANGUAGE_FORMAT_FLAGS] dwFlags, PCZZWSTR pwszLanguagesBuffer, PULONG pulNumLanguages)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pwszLanguagesBuffer", "pulNumLanguages"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadPreferredUILanguages(jitter):
    """"
    [Kernel32.dll] BOOL SetThreadPreferredUILanguages([SetThreadPreferredUILanguages_FLAGS] dwFlags, PCZZWSTR pwszLanguagesBuffer, PULONG pulNumLanguages)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pwszLanguagesBuffer", "pulNumLanguages"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetThreadUILanguage(jitter):
    """"
    [Kernel32.dll] LANGID SetThreadUILanguage(LANGID LangId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LangId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CopyContext(jitter):
    """"
    [Kernel32.dll] BOOL CopyContext(PCONTEXT Destination, DWORD ContextFlags, PCONTEXT Source)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Destination", "ContextFlags", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetEnabledXStateFeatures(jitter):
    """"
    [Kernel32.dll] [XSTATE_FEATURE_64] GetEnabledXStateFeatures()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_GetXStateFeaturesMask(jitter):
    """"
    [Kernel32.dll] BOOL GetXStateFeaturesMask(PCONTEXT Context, [XSTATE_MASK*] FeatureMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "FeatureMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_InitializeContext(jitter):
    """"
    [Kernel32.dll] BOOL InitializeContext(PVOID Buffer, DWORD ContextFlags, PCONTEXT* Context, PWORD ContextLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Buffer", "ContextFlags", "Context", "ContextLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_LocateXStateFeature(jitter):
    """"
    [Kernel32.dll] PVOID LocateXStateFeature(PCONTEXT Context, [XSTATE_FEATURE] FeatureId, PDWORD Length)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "FeatureId", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_SetXStateFeaturesMask(jitter):
    """"
    [Kernel32.dll] BOOL SetXStateFeaturesMask(PCONTEXT Context, [XSTATE_MASK] FeatureMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "FeatureMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def kernel32_CheckElevation(jitter):
    """"
    [Kernel32.dll] [ERROR_CODE] CheckElevation(LPCWSTR lpApplicationName, PDWORD pdwFlags, HANDLE hChildToken, PDWORD pdwRunLevel, PDWORD pdwReason)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpApplicationName", "pdwFlags", "hChildToken", "pdwRunLevel", "pdwReason"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
