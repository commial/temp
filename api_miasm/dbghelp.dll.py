
def dbghelp_EnumDirTree(jitter):
    """"
    [DbgHelp.dll] BOOL EnumDirTree([ProcessHandle] hProcess, PCTSTR RootPath, PCTSTR InputPathName, PTSTR OutputPathBuffer, PENUMDIRTREE_CALLBACK Callback, PVOID CallbackData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "RootPath", "InputPathName", "OutputPathBuffer", "Callback", "CallbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_ImagehlpApiVersion(jitter):
    """"
    [DbgHelp.dll] LPAPI_VERSION ImagehlpApiVersion()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_ImagehlpApiVersionEx(jitter):
    """"
    [DbgHelp.dll] LPAPI_VERSION ImagehlpApiVersionEx(LPAPI_VERSION AppVersion)
    """"
    ret_ad, args = jitter.func_args_stdcall(["AppVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_MakeSureDirectoryPathExists(jitter):
    """"
    [DbgHelp.dll] BOOL MakeSureDirectoryPathExists(PCSTR DirPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DirPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SearchTreeForFile(jitter):
    """"
    [DbgHelp.dll] BOOL SearchTreeForFile(PCTSTR RootPath, PCTSTR InputPathName, PTSTR OutputPathBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPath", "InputPathName", "OutputPathBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_EnumerateLoadedModules(jitter):
    """"
    [DbgHelp.dll] BOOL EnumerateLoadedModules([ProcessHandle] hProcess, PENUMLOADED_MODULES_CALLBACK EnumLoadedModulesCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumLoadedModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_EnumerateLoadedModules64(jitter):
    """"
    [DbgHelp.dll] BOOL EnumerateLoadedModules64([ProcessHandle] hProcess, PENUMLOADED_MODULES_CALLBACK64 EnumLoadedModulesCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumLoadedModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_EnumerateLoadedModulesW64(jitter):
    """"
    [DbgHelp.dll] BOOL EnumerateLoadedModulesW64([ProcessHandle] hProcess, PENUMLOADED_MODULES_CALLBACKW64 EnumLoadedModulesCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumLoadedModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_EnumerateLoadedModulesEx(jitter):
    """"
    [DbgHelp.dll] BOOL EnumerateLoadedModulesEx([ProcessHandle] hProcess, PENUMLOADED_MODULES_CALLBACK64 EnumLoadedModulesCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumLoadedModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_FindDebugInfoFile(jitter):
    """"
    [DbgHelp.dll] HANDLE FindDebugInfoFile(PCSTR FileName, PCSTR SymbolPath, PSTR DebugFilePath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileName", "SymbolPath", "DebugFilePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_FindDebugInfoFileEx(jitter):
    """"
    [DbgHelp.dll] HANDLE FindDebugInfoFileEx(PCTSTR FileName, PCTSTR SymbolPath, PTSTR DebugFilePath, PFIND_DEBUG_FILE_CALLBACK Callback, PVOID CallerData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileName", "SymbolPath", "DebugFilePath", "Callback", "CallerData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_FindExecutableImage(jitter):
    """"
    [DbgHelp.dll] HANDLE FindExecutableImage(PCSTR FileName, PCSTR SymbolPath, PSTR ImageFilePath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileName", "SymbolPath", "ImageFilePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_FindExecutableImageEx(jitter):
    """"
    [DbgHelp.dll] HANDLE FindExecutableImageEx(PCTSTR FileName, PCTSTR SymbolPath, PTSTR ImageFilePath, PFIND_EXE_FILE_CALLBACK Callback, PVOID CallerData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileName", "SymbolPath", "ImageFilePath", "Callback", "CallerData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_StackWalk(jitter):
    """"
    [DbgHelp.dll] BOOL StackWalk([IMAGE_FILE_MACHINE] MachineType, [ProcessHandle] hProcess, [ThreadHandle] hThread, LPSTACKFRAME StackFrame, PVOID ContextRecord, PREAD_PROCESS_MEMORY_ROUTINE ReadMemoryRoutine, PFUNCTION_TABLE_ACCESS_ROUTINE FunctionTableAccessRoutine, PGET_MODULE_BASE_ROUTINE GetModuleBaseRoutine, PTRANSLATE_ADDRESS_ROUTINE TranslateAddress)
    """"
    ret_ad, args = jitter.func_args_stdcall(["MachineType", "hProcess", "hThread", "StackFrame", "ContextRecord", "ReadMemoryRoutine", "FunctionTableAccessRoutine", "GetModuleBaseRoutine", "TranslateAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_StackWalk64(jitter):
    """"
    [DbgHelp.dll] BOOL StackWalk64([IMAGE_FILE_MACHINE] MachineType, [ProcessHandle] hProcess, [ThreadHandle] hThread, LPSTACKFRAME64 StackFrame, PVOID ContextRecord, PREAD_PROCESS_MEMORY_ROUTINE64 ReadMemoryRoutine, PFUNCTION_TABLE_ACCESS_ROUTINE64 FunctionTableAccessRoutine, PGET_MODULE_BASE_ROUTINE64 GetModuleBaseRoutine, PTRANSLATE_ADDRESS_ROUTINE64 TranslateAddress)
    """"
    ret_ad, args = jitter.func_args_stdcall(["MachineType", "hProcess", "hThread", "StackFrame", "ContextRecord", "ReadMemoryRoutine", "FunctionTableAccessRoutine", "GetModuleBaseRoutine", "TranslateAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetParentWindow(jitter):
    """"
    [DbgHelp.dll] BOOL SymSetParentWindow(HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_UnDecorateSymbolName(jitter):
    """"
    [DbgHelp.dll] DWORD UnDecorateSymbolName(PCTSTR DecoratedName, PTSTR UnDecoratedName, DWORD UndecoratedLength, [UNDNAME_FLAGS] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DecoratedName", "UnDecoratedName", "UndecoratedLength", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_GetTimestampForLoadedLibrary(jitter):
    """"
    [DbgHelp.dll] DWORD GetTimestampForLoadedLibrary(HMODULE ImageBase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ImageBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_ImageDirectoryEntryToData(jitter):
    """"
    [DbgHelp.dll] PVOID ImageDirectoryEntryToData(PVOID Base, BOOLEAN MappedAsImage, USHORT DirectoryEntry, PULONG Size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Base", "MappedAsImage", "DirectoryEntry", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_ImageDirectoryEntryToDataEx(jitter):
    """"
    [DbgHelp.dll] PVOID ImageDirectoryEntryToDataEx(PVOID Base, BOOLEAN MappedAsImage, USHORT DirectoryEntry, PULONG Size, PIMAGE_SECTION_HEADER* FoundHeader)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Base", "MappedAsImage", "DirectoryEntry", "Size", "FoundHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_ImageNtHeader(jitter):
    """"
    [DbgHelp.dll] PIMAGE_NT_HEADERS ImageNtHeader(PVOID ImageBase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ImageBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_ImageRvaToSection(jitter):
    """"
    [DbgHelp.dll] PIMAGE_SECTION_HEADER ImageRvaToSection(PIMAGE_NT_HEADERS NtHeaders, PVOID Base, ULONG Rva)
    """"
    ret_ad, args = jitter.func_args_stdcall(["NtHeaders", "Base", "Rva"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_ImageRvaToVa(jitter):
    """"
    [DbgHelp.dll] PVOID ImageRvaToVa(PIMAGE_NT_HEADERS NtHeaders, PVOID Base, ULONG Rva, PIMAGE_SECTION_HEADER* LastRvaSection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["NtHeaders", "Base", "Rva", "LastRvaSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymAddSourceStream(jitter):
    """"
    [DbgHelp.dll] BOOL SymAddSourceStream([ProcessHandle] hProcess, ULONG64 Base, PCSTR StreamFile, PBYTE Buffer, size_t Size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "StreamFile", "Buffer", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymAddSourceStream(jitter):
    """"
    [DbgHelp.dll] BOOL SymAddSourceStream([ProcessHandle] hProcess, ULONG64 Base, PCTSTR StreamFile, PBYTE Buffer, size_t Size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "StreamFile", "Buffer", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymAddSymbol(jitter):
    """"
    [DbgHelp.dll] BOOL SymAddSymbol([ProcessHandle] hProcess, ULONG64 BaseOfDll, PCTSTR Name, DWORD64 Address, DWORD Size, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Name", "Address", "Size", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymCleanup(jitter):
    """"
    [DbgHelp.dll] BOOL SymCleanup([ProcessHandle] hProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymDeleteSymbol(jitter):
    """"
    [DbgHelp.dll] BOOL SymDeleteSymbol([ProcessHandle] hProcess, ULONG64 BaseOfDll, PCTSTR Name, DWORD64 Address, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Name", "Address", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumLines(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumLines([ProcessHandle] hProcess, ULONG64 Base, PCTSTR Obj, PCTSTR File, PSYM_ENUMLINES_CALLBACK EnumLinesCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "Obj", "File", "EnumLinesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumProcesses(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumProcesses(PSYM_ENUMPROCESSES_CALLBACK EnumProcessesCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["EnumProcessesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumSourceFiles(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumSourceFiles([ProcessHandle] hProcess, ULONG64 ModBase, PCTSTR Mask, PSYM_ENUMSOURCEFILES_CALLBACK EnumSymbolsCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModBase", "Mask", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumSourceFileTokens(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumSourceFileTokens([ProcessHandle] hProcess, ULONG64 Base, PENUMSOURCEFILETOKENSCALLBACK Callback)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "Callback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumSourceLines(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumSourceLines([ProcessHandle] hProcess, ULONG64 Base, PCTSTR Obj, PCTSTR File, DWORD Line, [ESLFLAG] Flags, PSYM_ENUMLINES_CALLBACK EnumLinesCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "Obj", "File", "Line", "Flags", "EnumLinesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumSymbols(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumSymbols([ProcessHandle] hProcess, ULONG64 BaseOfDll, PCTSTR Mask, PSYM_ENUMERATESYMBOLS_CALLBACK EnumSymbolsCallback, const PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Mask", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumSymbolsForAddr(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumSymbolsForAddr([ProcessHandle] hProcess, DWORD64 Address, PSYM_ENUMERATESYMBOLS_CALLBACK EnumSymbolsCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Address", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumTypes(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumTypes([ProcessHandle] hProcess, ULONG64 BaseOfDll, PSYM_ENUMERATESYMBOLS_CALLBACK EnumSymbolsCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumTypesByName(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumTypesByName([ProcessHandle] hProcess, ULONG64 BaseOfDll, PCSTR mask, PSYM_ENUMERATESYMBOLS_CALLBACK EnumSymbolsCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "mask", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFindDebugInfoFile(jitter):
    """"
    [DbgHelp.dll] HANDLE SymFindDebugInfoFile([ProcessHandle] hProcess, PCTSTR FileName, PTSTR DebugFilePath, PFIND_DEBUG_FILE_CALLBACK Callback, PVOID CallerData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "FileName", "DebugFilePath", "Callback", "CallerData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFindExecutableImage(jitter):
    """"
    [DbgHelp.dll] HANDLE SymFindExecutableImage([ProcessHandle] hProcess, PCTSTR FileName, PTSTR ImageFilePath, PFIND_EXE_FILE_CALLBACK Callback, PVOID CallerData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "FileName", "ImageFilePath", "Callback", "CallerData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFindFileInPath(jitter):
    """"
    [DbgHelp.dll] BOOL SymFindFileInPath([ProcessHandle] hProcess, PCTSTR SearchPath, PCTSTR FileName, PVOID id, DWORD two, DWORD three, [SSRVOPT] flags, PTSTR FilePath, PFINDFILEINPATHCALLBACK callback, PVOID context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SearchPath", "FileName", "id", "two", "three", "flags", "FilePath", "callback", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFromAddr(jitter):
    """"
    [DbgHelp.dll] BOOL SymFromAddr([ProcessHandle] hProcess, DWORD64 Address, PDWORD64 Displacement, PSYMBOL_INFO Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Address", "Displacement", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFromIndex(jitter):
    """"
    [DbgHelp.dll] BOOL SymFromIndex([ProcessHandle] hProcess, ULONG64 BaseOfDll, DWORD Index, PSYMBOL_INFO Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Index", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFromName(jitter):
    """"
    [DbgHelp.dll] BOOL SymFromName([ProcessHandle] hProcess, PCTSTR Name, PSYMBOL_INFO Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Name", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFromToken(jitter):
    """"
    [DbgHelp.dll] BOOL SymFromToken([ProcessHandle] hProcess, DWORD64 Base, DWORD Token, PSYMBOL_INFO Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "Token", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFunctionTableAccess(jitter):
    """"
    [DbgHelp.dll] PVOID SymFunctionTableAccess([ProcessHandle] hProcess, DWORD AddrBase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "AddrBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFunctionTableAccess64(jitter):
    """"
    [DbgHelp.dll] PVOID SymFunctionTableAccess64([ProcessHandle] hProcess, DWORD64 AddrBase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "AddrBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetFileLineOffsets64(jitter):
    """"
    [DbgHelp.dll] ULONG SymGetFileLineOffsets64([ProcessHandle] hProcess, PCSTR ModuleName, PCSTR FileName, PDWORD64 Buffer, ULONG BufferLines)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModuleName", "FileName", "Buffer", "BufferLines"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetHomeDirectory(jitter):
    """"
    [DbgHelp.dll] PTCHAR SymGetHomeDirectory(DWORD type, PTSTR dir, size_t size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["type", "dir", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineFromAddr(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetLineFromAddr([ProcessHandle] hProcess, DWORD dwAddr, PDWORD pdwDisplacement, PIMAGEHLP_LINE Line)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "pdwDisplacement", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineFromAddr64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetLineFromAddr64([ProcessHandle] hProcess, DWORD64 dwAddr, PDWORD pdwDisplacement, PIMAGEHLP_LINE64 Line)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "pdwDisplacement", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineFromAddrW64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetLineFromAddrW64([ProcessHandle] hProcess, DWORD64 dwAddr, PDWORD pdwDisplacement, PIMAGEHLP_LINEW64 Line)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "pdwDisplacement", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineFromName(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetLineFromName([ProcessHandle] hProcess, PCSTR ModuleName, PCSTR FileName, DWORD dwLineNumber, PLONG plDisplacement, PIMAGEHLP_LINE Line)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModuleName", "FileName", "dwLineNumber", "plDisplacement", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineFromName64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetLineFromName64([ProcessHandle] hProcess, PCSTR ModuleName, PCSTR FileName, DWORD dwLineNumber, PLONG lpDisplacement, PIMAGEHLP_LINE64 Line)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModuleName", "FileName", "dwLineNumber", "lpDisplacement", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineFromNameW64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetLineFromNameW64([ProcessHandle] hProcess, PCWSTR ModuleName, PCWSTR FileName, DWORD dwLineNumber, PLONG lpDisplacement, PIMAGEHLP_LINEW64 Line)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModuleName", "FileName", "dwLineNumber", "lpDisplacement", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineNext(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetLineNext([ProcessHandle] hProcess, PIMAGEHLP_LINE Line)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineNext64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetLineNext64([ProcessHandle] hProcess, PIMAGEHLP_LINE64 Line)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineNextW64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetLineNextW64([ProcessHandle] hProcess, PIMAGEHLP_LINEW64 Line)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLinePrev(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetLinePrev([ProcessHandle] hProcess, PIMAGEHLP_LINE Line)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLinePrev64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetLinePrev64([ProcessHandle] hProcess, PIMAGEHLP_LINE64 Line)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLinePrevW64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetLinePrevW64([ProcessHandle] hProcess, PIMAGEHLP_LINEW64 Line)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetModuleBase(jitter):
    """"
    [DbgHelp.dll] DWORD SymGetModuleBase([ProcessHandle] hProcess, DWORD dwAddr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetModuleBase64(jitter):
    """"
    [DbgHelp.dll] DWORD64 SymGetModuleBase64([ProcessHandle] hProcess, DWORD64 dwAddr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetModuleInfo(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetModuleInfo([ProcessHandle] hProcess, DWORD dwAddr, PIMAGEHLP_MODULE ModuleInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "ModuleInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetModuleInfo64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetModuleInfo64([ProcessHandle] hProcess, DWORD64 dwAddr, PIMAGEHLP_MODULE64 ModuleInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "ModuleInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetModuleInfoW64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetModuleInfoW64([ProcessHandle] hProcess, DWORD64 dwAddr, PIMAGEHLP_MODULEW64 ModuleInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "ModuleInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetOmaps(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetOmaps([ProcessHandle] hProcess, ULONG64 BaseOfDll, POMAP* OmapTo, PDWORD64 cOmapTo, POMAP* OmapFrom, PDWORD64 cOmapFrom)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "OmapTo", "cOmapTo", "OmapFrom", "cOmapFrom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetOptions(jitter):
    """"
    [DbgHelp.dll] [SYMOPT_FLAGS] SymGetOptions()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetScope(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetScope([ProcessHandle] hProcess, ULONG64 BaseOfDll, DWORD Index, PSYMBOL_INFO Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Index", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSearchPath(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSearchPath([ProcessHandle] hProcess, PTSTR SearchPath, DWORD SearchPathLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SearchPath", "SearchPathLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymbolFile(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSymbolFile([ProcessHandle] hProcess, PCTSTR SymPath, PCTSTR ImageFile, DWORD Type, PTSTR SymbolFile, size_t cSymbolFile, PTSTR DbgFile, size_t cDbgFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SymPath", "ImageFile", "Type", "SymbolFile", "cSymbolFile", "DbgFile", "cDbgFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetTypeFromName(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetTypeFromName([ProcessHandle] hProcess, ULONG64 BaseOfDll, PCTSTR Name, PSYMBOL_INFO Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Name", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetTypeInfo(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetTypeInfo([ProcessHandle] hProcess, DWORD64 ModBase, ULONG TypeId, IMAGEHLP_SYMBOL_TYPE_INFO GetType, PVOID pInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModBase", "TypeId", "GetType", "pInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetTypeInfoEx(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetTypeInfoEx([ProcessHandle] hProcess, DWORD64 ModBase, PIMAGEHLP_GET_TYPE_INFO_PARAMS Params)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModBase", "Params"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymInitialize(jitter):
    """"
    [DbgHelp.dll] BOOL SymInitialize([ProcessHandle] hProcess, PCTSTR UserSearchPath, BOOL fInvadeProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "UserSearchPath", "fInvadeProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymLoadModule(jitter):
    """"
    [DbgHelp.dll] DWORD SymLoadModule([ProcessHandle] hProcess, HANDLE hFile, PCSTR ImageName, PCSTR ModuleName, DWORD BaseOfDll, DWORD SizeOfDll)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hFile", "ImageName", "ModuleName", "BaseOfDll", "SizeOfDll"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymLoadModule64(jitter):
    """"
    [DbgHelp.dll] DWORD64 SymLoadModule64([ProcessHandle] hProcess, HANDLE hFile, PCSTR ImageName, PCSTR ModuleName, DWORD64 BaseOfDll, DWORD SizeOfDll)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hFile", "ImageName", "ModuleName", "BaseOfDll", "SizeOfDll"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymLoadModuleEx(jitter):
    """"
    [DbgHelp.dll] DWORD64 SymLoadModuleEx([ProcessHandle] hProcess, HANDLE hFile, PCTSTR ImageName, PCTSTR ModuleName, DWORD64 BaseOfDll, DWORD DllSize, PMODLOAD_DATA Data, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hFile", "ImageName", "ModuleName", "BaseOfDll", "DllSize", "Data", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymMatchFileName(jitter):
    """"
    [DbgHelp.dll] BOOL SymMatchFileName(PCTSTR FileName, PCTSTR Match, PTSTR* FileNameStop, PTSTR* MatchStop)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileName", "Match", "FileNameStop", "MatchStop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymMatchString(jitter):
    """"
    [DbgHelp.dll] BOOL SymMatchString(PCSTR string, PCSTR expression, BOOL fCase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["string", "expression", "fCase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymMatchString(jitter):
    """"
    [DbgHelp.dll] BOOL SymMatchString(PCTSTR string, PCTSTR expression, BOOL fCase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["string", "expression", "fCase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymNext(jitter):
    """"
    [DbgHelp.dll] BOOL SymNext([ProcessHandle] hProcess, PSYMBOL_INFO Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymPrev(jitter):
    """"
    [DbgHelp.dll] BOOL SymPrev([ProcessHandle] hProcess, PSYMBOL_INFO Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymRefreshModuleList(jitter):
    """"
    [DbgHelp.dll] BOOL SymRefreshModuleList([ProcessHandle] hProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymRegisterCallback(jitter):
    """"
    [DbgHelp.dll] BOOL SymRegisterCallback([ProcessHandle] hProcess, PSYMBOL_REGISTERED_CALLBACK CallbackFunction, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "CallbackFunction", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymRegisterCallback64(jitter):
    """"
    [DbgHelp.dll] BOOL SymRegisterCallback64([ProcessHandle] hProcess, PSYMBOL_REGISTERED_CALLBACK64 CallbackFunction, ULONG64 UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "CallbackFunction", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymRegisterCallbackW64(jitter):
    """"
    [DbgHelp.dll] BOOL SymRegisterCallbackW64([ProcessHandle] hProcess, PSYMBOL_REGISTERED_CALLBACKW64 CallbackFunction, ULONG64 UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "CallbackFunction", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymRegisterFunctionEntryCallback(jitter):
    """"
    [DbgHelp.dll] BOOL SymRegisterFunctionEntryCallback([ProcessHandle] hProcess, PSYMBOL_FUNCENTRY_CALLBACK CallbackFunction, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "CallbackFunction", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymRegisterFunctionEntryCallback64(jitter):
    """"
    [DbgHelp.dll] BOOL SymRegisterFunctionEntryCallback64([ProcessHandle] hProcess, PSYMBOL_FUNCENTRY_CALLBACK64 CallbackFunction, ULONG64 UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "CallbackFunction", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSearch(jitter):
    """"
    [DbgHelp.dll] BOOL SymSearch([ProcessHandle] hProcess, ULONG64 BaseOfDll, DWORD Index, DWORD SymTag, PCTSTR Mask, DWORD64 Address, PSYM_ENUMERATESYMBOLS_CALLBACK EnumSymbolsCallback, PVOID UserContext, [SYMSEARCH_FLAGS] Options)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Index", "SymTag", "Mask", "Address", "EnumSymbolsCallback", "UserContext", "Options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetContext(jitter):
    """"
    [DbgHelp.dll] BOOL SymSetContext([ProcessHandle] hProcess, PIMAGEHLP_STACK_FRAME StackFrame, PIMAGEHLP_CONTEXT Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "StackFrame", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetHomeDirectory(jitter):
    """"
    [DbgHelp.dll] PTCHAR SymSetHomeDirectory([ProcessHandle] hProcess, PCTSTR dir)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dir"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetOptions(jitter):
    """"
    [DbgHelp.dll] DWORD SymSetOptions([SYMOPT_FLAGS] SymOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SymOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetScopeFromAddr(jitter):
    """"
    [DbgHelp.dll] BOOL SymSetScopeFromAddr([ProcessHandle] hProcess, ULONG64 Address)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetScopeFromIndex(jitter):
    """"
    [DbgHelp.dll] BOOL SymSetScopeFromIndex([ProcessHandle] hProcess, ULONG64 BaseOfDll, DWORD Index)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumerateModules(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumerateModules([ProcessHandle] hProcess, PSYM_ENUMMODULES_CALLBACK EnumModulesCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumerateModules64(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumerateModules64([ProcessHandle] hProcess, PSYM_ENUMMODULES_CALLBACK64 EnumModulesCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumerateModulesW64(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumerateModulesW64([ProcessHandle] hProcess, PSYM_ENUMMODULES_CALLBACKW64 EnumModulesCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetSearchPath(jitter):
    """"
    [DbgHelp.dll] BOOL SymSetSearchPath([ProcessHandle] hProcess, PCTSTR SearchPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SearchPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymUnDName(jitter):
    """"
    [DbgHelp.dll] BOOL SymUnDName(PIMAGEHLP_SYMBOL sym, PSTR UnDecName, DWORD UnDecNameLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sym", "UnDecName", "UnDecNameLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymUnDName64(jitter):
    """"
    [DbgHelp.dll] BOOL SymUnDName64(PIMAGEHLP_SYMBOL64 sym, PSTR UnDecName, DWORD UnDecNameLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sym", "UnDecName", "UnDecNameLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymUnloadModule(jitter):
    """"
    [DbgHelp.dll] BOOL SymUnloadModule([ProcessHandle] hProcess, DWORD BaseOfDll)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymUnloadModule64(jitter):
    """"
    [DbgHelp.dll] BOOL SymUnloadModule64([ProcessHandle] hProcess, DWORD64 BaseOfDll)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvDeltaName(jitter):
    """"
    [DbgHelp.dll] PCTSTR SymSrvDeltaName([ProcessHandle] hProcess, PCTSTR SymPath, PCTSTR Type, PCTSTR File1, PCTSTR File2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SymPath", "Type", "File1", "File2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvGetFileIndexes(jitter):
    """"
    [DbgHelp.dll] BOOL SymSrvGetFileIndexes(PCTSTR File, GUID* Id, DWORD* Val1, DWORD* Val2, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["File", "Id", "Val1", "Val2", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvGetFileIndexInfo(jitter):
    """"
    [DbgHelp.dll] BOOL SymSrvGetFileIndexInfo(PCTSTR File, PSYMSRV_INDEX_INFO Info, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["File", "Info", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvGetFileIndexString(jitter):
    """"
    [DbgHelp.dll] BOOL SymSrvGetFileIndexString([ProcessHandle] hProcess, PCTSTR SrvPath, PCTSTR File, PTSTR Index, size_t Size, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SrvPath", "File", "Index", "Size", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvGetSupplement(jitter):
    """"
    [DbgHelp.dll] PCTSTR SymSrvGetSupplement([ProcessHandle] hProcess, PCTSTR SymPath, PCTSTR Node, PCTSTR File)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SymPath", "Node", "File"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvIsStore(jitter):
    """"
    [DbgHelp.dll] BOOL SymSrvIsStore([ProcessHandle] hProcess, PCTSTR path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvStoreFile(jitter):
    """"
    [DbgHelp.dll] PCTSTR SymSrvStoreFile([ProcessHandle] hProcess, PCTSTR SrvPath, PCTSTR File, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SrvPath", "File", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvStoreSupplement(jitter):
    """"
    [DbgHelp.dll] PCTSTR SymSrvStoreSupplement([ProcessHandle] hProcess, const PCTSTR SymPath, PCTSTR Node, PCTSTR File, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SymPath", "Node", "File", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_MiniDumpReadDumpStream(jitter):
    """"
    [DbgHelp.dll] BOOL MiniDumpReadDumpStream(PVOID BaseOfDump, ULONG StreamNumber, PMINIDUMP_DIRECTORY* Dir, PVOID* StreamPointer, ULONG* StreamSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BaseOfDump", "StreamNumber", "Dir", "StreamPointer", "StreamSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_MiniDumpWriteDump(jitter):
    """"
    [DbgHelp.dll] BOOL MiniDumpWriteDump([ProcessHandle] hProcess, DWORD ProcessId, HANDLE hFile, MINIDUMP_TYPE DumpType, PMINIDUMP_EXCEPTION_INFORMATION ExceptionParam, PMINIDUMP_USER_STREAM_INFORMATION UserStreamParam, PMINIDUMP_CALLBACK_INFORMATION CallbackParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ProcessId", "hFile", "DumpType", "ExceptionParam", "UserStreamParam", "CallbackParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSourceFile(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSourceFile([ProcessHandle] hProcess, ULONG64 Base, PCTSTR Params, PCTSTR FileSpec, PTSTR FilePath, DWORD Size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "Params", "FileSpec", "FilePath", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSourceFileFromToken(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSourceFileFromToken([ProcessHandle] hProcess, PVOID Token, PCTSTR Params, PTSTR FilePath, DWORD Size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Token", "Params", "FilePath", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSourceFileToken(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSourceFileToken([ProcessHandle] hProcess, ULONG64 Base, PCTSTR FileSpec, PVOID* Token, DWORD* Size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "FileSpec", "Token", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSourceVarFromToken(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSourceVarFromToken([ProcessHandle] hProcess, PVOID Token, PCTSTR Params, PCTSTR VarName, PTSTR Value, DWORD Size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Token", "Params", "VarName", "Value", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_MapDebugInformation(jitter):
    """"
    [DbgHelp.dll] PIMAGE_DEBUG_INFORMATION MapDebugInformation(HANDLE FileHandle, PCSTR FileName, PCSTR SymbolPath, ULONG ImageBase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "FileName", "SymbolPath", "ImageBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumerateSymbols(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumerateSymbols([ProcessHandle] hProcess, ULONG BaseOfDll, PSYM_ENUMSYMBOLS_CALLBACK EnumSymbolsCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumerateSymbols64(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumerateSymbols64([ProcessHandle] hProcess, ULONG64 BaseOfDll, PSYM_ENUMSYMBOLS_CALLBACK64 EnumSymbolsCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumerateSymbolsW64(jitter):
    """"
    [DbgHelp.dll] BOOL SymEnumerateSymbolsW64([ProcessHandle] hProcess, ULONG64 BaseOfDll, PSYM_ENUMSYMBOLS_CALLBACKW64 EnumSymbolsCallback, PVOID UserContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymFromAddr(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSymFromAddr([ProcessHandle] hProcess, DWORD dwAddr, PDWORD pdwDisplacement, PIMAGEHLP_SYMBOL Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "pdwDisplacement", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymFromAddr64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSymFromAddr64([ProcessHandle] hProcess, DWORD64 Address, PDWORD64 Displacement, PIMAGEHLP_SYMBOL64 Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Address", "Displacement", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymFromName(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSymFromName([ProcessHandle] hProcess, PCSTR Name, PIMAGEHLP_SYMBOL Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Name", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymFromName64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSymFromName64([ProcessHandle] hProcess, PCSTR Name, PIMAGEHLP_SYMBOL64 Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Name", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymNext(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSymNext([ProcessHandle] hProcess, PIMAGEHLP_SYMBOL Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymNext64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSymNext64([ProcessHandle] hProcess, PIMAGEHLP_SYMBOL64 Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymPrev(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSymPrev([ProcessHandle] hProcess, PIMAGEHLP_SYMBOL Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymPrev64(jitter):
    """"
    [DbgHelp.dll] BOOL SymGetSymPrev64([ProcessHandle] hProcess, PIMAGEHLP_SYMBOL64 Symbol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_UnmapDebugInformation(jitter):
    """"
    [DbgHelp.dll] BOOL UnmapDebugInformation(PIMAGE_DEBUG_INFORMATION DebugInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DebugInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
