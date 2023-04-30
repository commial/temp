IMAGEHLP_SYMBOL_TYPE_INFO = {
    "TI_GET_SYMTAG": 0,
    "TI_GET_SYMNAME": 1,
    "TI_GET_LENGTH": 2,
    "TI_GET_TYPE": 3,
    "TI_GET_TYPEID": 4,
    "TI_GET_BASETYPE": 5,
    "TI_GET_ARRAYINDEXTYPEID": 6,
    "TI_FINDCHILDREN": 7,
    "TI_GET_DATAKIND": 8,
    "TI_GET_ADDRESSOFFSET": 9,
    "TI_GET_OFFSET": 10,
    "TI_GET_VALUE": 11,
    "TI_GET_COUNT": 12,
    "TI_GET_CHILDRENCOUNT": 13,
    "TI_GET_BITPOSITION": 14,
    "TI_GET_VIRTUALBASECLASS": 15,
    "TI_GET_VIRTUALTABLESHAPEID": 16,
    "TI_GET_VIRTUALBASEPOINTEROFFSET": 17,
    "TI_GET_CLASSPARENTID": 18,
    "TI_GET_NESTED": 19,
    "TI_GET_SYMINDEX": 20,
    "TI_GET_LEXICALPARENT": 21,
    "TI_GET_ADDRESS": 22,
    "TI_GET_THISADJUST": 23,
    "TI_GET_UDTKIND": 24,
    "TI_IS_EQUIV_TO": 25,
    "TI_GET_CALLING_CONVENTION": 26,
    "TI_IS_CLOSE_EQUIV_TO": 27,
    "TI_GTIEX_REQS_VALID": 28,
    "TI_GET_VIRTUALBASEOFFSET": 29,
    "TI_GET_VIRTUALBASEDISPINDEX": 30,
    "TI_GET_IS_REFERENCE": 31,
}
SYM_TYPE = {
    "SymNone": 0,
    "SymCoff": 1,
    "SymCv": 2,
    "SymPdb": 3,
    "SymExport": 4,
    "SymDeferred": 5,
    "SymSym": 6,
    "SymDia": 7,
    "SymVirtual": 8,
}
ADDRESS_MODE = {
    "AddrMode1616": 0,
    "AddrMode1632": 1,
    "AddrModeReal": 2,
    "AddrModeFlat": 3,
}
_IMAGE_DEBUG_TYPE_ = {
    "IMAGE_DEBUG_TYPE_UNKNOWN": 0,
    "IMAGE_DEBUG_TYPE_COFF": 1,
    "IMAGE_DEBUG_TYPE_CODEVIEW": 2,
    "IMAGE_DEBUG_TYPE_FPO": 3,
    "IMAGE_DEBUG_TYPE_MISC": 4,
    "IMAGE_DEBUG_TYPE_EXCEPTION": 5,
    "IMAGE_DEBUG_TYPE_FIXUP": 6,
    "IMAGE_DEBUG_TYPE_OMAP_TO_SRC": 7,
    "IMAGE_DEBUG_TYPE_OMAP_FROM_SRC": 8,
    "IMAGE_DEBUG_TYPE_BORLAND": 9,
    "IMAGE_DEBUG_TYPE_RESERVED10": 10,
    "IMAGE_DEBUG_TYPE_CLSID": 11,
}

def dbghelp_EnumDirTree(jitter, get_str, set_str):
    """
    BOOL EnumDirTree(
        [ProcessHandle] hProcess,
        PCTSTR RootPath,
        PCTSTR InputPathName,
        PTSTR OutputPathBuffer,
        PENUMDIRTREE_CALLBACK Callback,
        PVOID CallbackData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "RootPath", "InputPathName", "OutputPathBuffer", "Callback", "CallbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_EnumDirTreeA(jitter):
    dbghelp_EnumDirTree(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_EnumDirTreeW(jitter):
    dbghelp_EnumDirTree(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_ImagehlpApiVersion(jitter):
    """
    LPAPI_VERSION ImagehlpApiVersion()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_ImagehlpApiVersionEx(jitter):
    """
    LPAPI_VERSION ImagehlpApiVersionEx(
        LPAPI_VERSION AppVersion
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AppVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_MakeSureDirectoryPathExists(jitter):
    """
    BOOL MakeSureDirectoryPathExists(
        PCSTR DirPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DirPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SearchTreeForFile(jitter, get_str, set_str):
    """
    BOOL SearchTreeForFile(
        PCTSTR RootPath,
        PCTSTR InputPathName,
        PTSTR OutputPathBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPath", "InputPathName", "OutputPathBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SearchTreeForFileA(jitter):
    dbghelp_SearchTreeForFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SearchTreeForFileW(jitter):
    dbghelp_SearchTreeForFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_EnumerateLoadedModules(jitter):
    """
    BOOL EnumerateLoadedModules(
        [ProcessHandle] hProcess,
        PENUMLOADED_MODULES_CALLBACK EnumLoadedModulesCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumLoadedModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_EnumerateLoadedModules64(jitter):
    """
    BOOL EnumerateLoadedModules64(
        [ProcessHandle] hProcess,
        PENUMLOADED_MODULES_CALLBACK64 EnumLoadedModulesCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumLoadedModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_EnumerateLoadedModulesW64(jitter):
    """
    BOOL EnumerateLoadedModulesW64(
        [ProcessHandle] hProcess,
        PENUMLOADED_MODULES_CALLBACKW64 EnumLoadedModulesCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumLoadedModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_EnumerateLoadedModulesEx(jitter, get_str, set_str):
    """
    BOOL EnumerateLoadedModulesEx(
        [ProcessHandle] hProcess,
        PENUMLOADED_MODULES_CALLBACK64 EnumLoadedModulesCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumLoadedModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_EnumerateLoadedModulesExA(jitter):
    dbghelp_EnumerateLoadedModulesEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_EnumerateLoadedModulesExW(jitter):
    dbghelp_EnumerateLoadedModulesEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_FindDebugInfoFile(jitter):
    """
    HANDLE FindDebugInfoFile(
        PCSTR FileName,
        PCSTR SymbolPath,
        PSTR DebugFilePath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "SymbolPath", "DebugFilePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_FindDebugInfoFileEx(jitter, get_str, set_str):
    """
    HANDLE FindDebugInfoFileEx(
        PCTSTR FileName,
        PCTSTR SymbolPath,
        PTSTR DebugFilePath,
        PFIND_DEBUG_FILE_CALLBACK Callback,
        PVOID CallerData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "SymbolPath", "DebugFilePath", "Callback", "CallerData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_FindDebugInfoFileExA(jitter):
    dbghelp_FindDebugInfoFileEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_FindDebugInfoFileExW(jitter):
    dbghelp_FindDebugInfoFileEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_FindExecutableImage(jitter):
    """
    HANDLE FindExecutableImage(
        PCSTR FileName,
        PCSTR SymbolPath,
        PSTR ImageFilePath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "SymbolPath", "ImageFilePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_FindExecutableImageEx(jitter, get_str, set_str):
    """
    HANDLE FindExecutableImageEx(
        PCTSTR FileName,
        PCTSTR SymbolPath,
        PTSTR ImageFilePath,
        PFIND_EXE_FILE_CALLBACK Callback,
        PVOID CallerData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "SymbolPath", "ImageFilePath", "Callback", "CallerData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_FindExecutableImageExA(jitter):
    dbghelp_FindExecutableImageEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_FindExecutableImageExW(jitter):
    dbghelp_FindExecutableImageEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_StackWalk(jitter):
    """
    BOOL StackWalk(
        [IMAGE_FILE_MACHINE] MachineType,
        [ProcessHandle] hProcess,
        [ThreadHandle] hThread,
        LPSTACKFRAME StackFrame,
        PVOID ContextRecord,
        PREAD_PROCESS_MEMORY_ROUTINE ReadMemoryRoutine,
        PFUNCTION_TABLE_ACCESS_ROUTINE FunctionTableAccessRoutine,
        PGET_MODULE_BASE_ROUTINE GetModuleBaseRoutine,
        PTRANSLATE_ADDRESS_ROUTINE TranslateAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MachineType", "hProcess", "hThread", "StackFrame", "ContextRecord", "ReadMemoryRoutine", "FunctionTableAccessRoutine", "GetModuleBaseRoutine", "TranslateAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_StackWalk64(jitter):
    """
    BOOL StackWalk64(
        [IMAGE_FILE_MACHINE] MachineType,
        [ProcessHandle] hProcess,
        [ThreadHandle] hThread,
        LPSTACKFRAME64 StackFrame,
        PVOID ContextRecord,
        PREAD_PROCESS_MEMORY_ROUTINE64 ReadMemoryRoutine,
        PFUNCTION_TABLE_ACCESS_ROUTINE64 FunctionTableAccessRoutine,
        PGET_MODULE_BASE_ROUTINE64 GetModuleBaseRoutine,
        PTRANSLATE_ADDRESS_ROUTINE64 TranslateAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MachineType", "hProcess", "hThread", "StackFrame", "ContextRecord", "ReadMemoryRoutine", "FunctionTableAccessRoutine", "GetModuleBaseRoutine", "TranslateAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetParentWindow(jitter):
    """
    BOOL SymSetParentWindow(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_UnDecorateSymbolName(jitter, get_str, set_str):
    """
    DWORD UnDecorateSymbolName(
        PCTSTR DecoratedName,
        PTSTR UnDecoratedName,
        DWORD UndecoratedLength,
        [UNDNAME_FLAGS] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DecoratedName", "UnDecoratedName", "UndecoratedLength", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_UnDecorateSymbolNameA(jitter):
    dbghelp_UnDecorateSymbolName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_UnDecorateSymbolNameW(jitter):
    dbghelp_UnDecorateSymbolName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_GetTimestampForLoadedLibrary(jitter):
    """
    DWORD GetTimestampForLoadedLibrary(
        HMODULE ImageBase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_ImageDirectoryEntryToData(jitter):
    """
    PVOID ImageDirectoryEntryToData(
        PVOID Base,
        BOOLEAN MappedAsImage,
        USHORT DirectoryEntry,
        PULONG Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Base", "MappedAsImage", "DirectoryEntry", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_ImageDirectoryEntryToDataEx(jitter):
    """
    PVOID ImageDirectoryEntryToDataEx(
        PVOID Base,
        BOOLEAN MappedAsImage,
        USHORT DirectoryEntry,
        PULONG Size,
        PIMAGE_SECTION_HEADER* FoundHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Base", "MappedAsImage", "DirectoryEntry", "Size", "FoundHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_ImageNtHeader(jitter):
    """
    PIMAGE_NT_HEADERS ImageNtHeader(
        PVOID ImageBase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_ImageRvaToSection(jitter):
    """
    PIMAGE_SECTION_HEADER ImageRvaToSection(
        PIMAGE_NT_HEADERS NtHeaders,
        PVOID Base,
        ULONG Rva
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NtHeaders", "Base", "Rva"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_ImageRvaToVa(jitter):
    """
    PVOID ImageRvaToVa(
        PIMAGE_NT_HEADERS NtHeaders,
        PVOID Base,
        ULONG Rva,
        PIMAGE_SECTION_HEADER* LastRvaSection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NtHeaders", "Base", "Rva", "LastRvaSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymAddSourceStream(jitter):
    """
    BOOL SymAddSourceStream(
        [ProcessHandle] hProcess,
        ULONG64 Base,
        PCSTR StreamFile,
        PBYTE Buffer,
        size_t Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "StreamFile", "Buffer", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymAddSourceStream(jitter, get_str, set_str):
    """
    BOOL SymAddSourceStream(
        [ProcessHandle] hProcess,
        ULONG64 Base,
        PCTSTR StreamFile,
        PBYTE Buffer,
        size_t Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "StreamFile", "Buffer", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymAddSourceStreamA(jitter):
    dbghelp_SymAddSourceStream(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymAddSourceStreamW(jitter):
    dbghelp_SymAddSourceStream(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymAddSymbol(jitter, get_str, set_str):
    """
    BOOL SymAddSymbol(
        [ProcessHandle] hProcess,
        ULONG64 BaseOfDll,
        PCTSTR Name,
        DWORD64 Address,
        DWORD Size,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Name", "Address", "Size", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymAddSymbolA(jitter):
    dbghelp_SymAddSymbol(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymAddSymbolW(jitter):
    dbghelp_SymAddSymbol(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymCleanup(jitter):
    """
    BOOL SymCleanup(
        [ProcessHandle] hProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymDeleteSymbol(jitter, get_str, set_str):
    """
    BOOL SymDeleteSymbol(
        [ProcessHandle] hProcess,
        ULONG64 BaseOfDll,
        PCTSTR Name,
        DWORD64 Address,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Name", "Address", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymDeleteSymbolA(jitter):
    dbghelp_SymDeleteSymbol(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymDeleteSymbolW(jitter):
    dbghelp_SymDeleteSymbol(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymEnumLines(jitter, get_str, set_str):
    """
    BOOL SymEnumLines(
        [ProcessHandle] hProcess,
        ULONG64 Base,
        PCTSTR Obj,
        PCTSTR File,
        PSYM_ENUMLINES_CALLBACK EnumLinesCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "Obj", "File", "EnumLinesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumLinesA(jitter):
    dbghelp_SymEnumLines(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymEnumLinesW(jitter):
    dbghelp_SymEnumLines(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymEnumProcesses(jitter):
    """
    BOOL SymEnumProcesses(
        PSYM_ENUMPROCESSES_CALLBACK EnumProcessesCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnumProcessesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumSourceFiles(jitter, get_str, set_str):
    """
    BOOL SymEnumSourceFiles(
        [ProcessHandle] hProcess,
        ULONG64 ModBase,
        PCTSTR Mask,
        PSYM_ENUMSOURCEFILES_CALLBACK EnumSymbolsCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModBase", "Mask", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumSourceFilesA(jitter):
    dbghelp_SymEnumSourceFiles(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymEnumSourceFilesW(jitter):
    dbghelp_SymEnumSourceFiles(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymEnumSourceFileTokens(jitter, get_str, set_str):
    """
    BOOL SymEnumSourceFileTokens(
        [ProcessHandle] hProcess,
        ULONG64 Base,
        PENUMSOURCEFILETOKENSCALLBACK Callback
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "Callback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumSourceFileTokensA(jitter):
    dbghelp_SymEnumSourceFileTokens(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymEnumSourceFileTokensW(jitter):
    dbghelp_SymEnumSourceFileTokens(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymEnumSourceLines(jitter, get_str, set_str):
    """
    BOOL SymEnumSourceLines(
        [ProcessHandle] hProcess,
        ULONG64 Base,
        PCTSTR Obj,
        PCTSTR File,
        DWORD Line,
        [ESLFLAG] Flags,
        PSYM_ENUMLINES_CALLBACK EnumLinesCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "Obj", "File", "Line", "Flags", "EnumLinesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumSourceLinesA(jitter):
    dbghelp_SymEnumSourceLines(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymEnumSourceLinesW(jitter):
    dbghelp_SymEnumSourceLines(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymEnumSymbols(jitter, get_str, set_str):
    """
    BOOL SymEnumSymbols(
        [ProcessHandle] hProcess,
        ULONG64 BaseOfDll,
        PCTSTR Mask,
        PSYM_ENUMERATESYMBOLS_CALLBACK EnumSymbolsCallback,
        const PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Mask", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumSymbolsA(jitter):
    dbghelp_SymEnumSymbols(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymEnumSymbolsW(jitter):
    dbghelp_SymEnumSymbols(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymEnumSymbolsForAddr(jitter, get_str, set_str):
    """
    BOOL SymEnumSymbolsForAddr(
        [ProcessHandle] hProcess,
        DWORD64 Address,
        PSYM_ENUMERATESYMBOLS_CALLBACK EnumSymbolsCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Address", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumSymbolsForAddrA(jitter):
    dbghelp_SymEnumSymbolsForAddr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymEnumSymbolsForAddrW(jitter):
    dbghelp_SymEnumSymbolsForAddr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymEnumTypes(jitter, get_str, set_str):
    """
    BOOL SymEnumTypes(
        [ProcessHandle] hProcess,
        ULONG64 BaseOfDll,
        PSYM_ENUMERATESYMBOLS_CALLBACK EnumSymbolsCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumTypesA(jitter):
    dbghelp_SymEnumTypes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymEnumTypesW(jitter):
    dbghelp_SymEnumTypes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymEnumTypesByName(jitter, get_str, set_str):
    """
    BOOL SymEnumTypesByName(
        [ProcessHandle] hProcess,
        ULONG64 BaseOfDll,
        PCSTR mask,
        PSYM_ENUMERATESYMBOLS_CALLBACK EnumSymbolsCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "mask", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumTypesByNameA(jitter):
    dbghelp_SymEnumTypesByName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymEnumTypesByNameW(jitter):
    dbghelp_SymEnumTypesByName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymFindDebugInfoFile(jitter, get_str, set_str):
    """
    HANDLE SymFindDebugInfoFile(
        [ProcessHandle] hProcess,
        PCTSTR FileName,
        PTSTR DebugFilePath,
        PFIND_DEBUG_FILE_CALLBACK Callback,
        PVOID CallerData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "FileName", "DebugFilePath", "Callback", "CallerData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFindDebugInfoFileA(jitter):
    dbghelp_SymFindDebugInfoFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymFindDebugInfoFileW(jitter):
    dbghelp_SymFindDebugInfoFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymFindExecutableImage(jitter, get_str, set_str):
    """
    HANDLE SymFindExecutableImage(
        [ProcessHandle] hProcess,
        PCTSTR FileName,
        PTSTR ImageFilePath,
        PFIND_EXE_FILE_CALLBACK Callback,
        PVOID CallerData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "FileName", "ImageFilePath", "Callback", "CallerData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFindExecutableImageA(jitter):
    dbghelp_SymFindExecutableImage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymFindExecutableImageW(jitter):
    dbghelp_SymFindExecutableImage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymFindFileInPath(jitter, get_str, set_str):
    """
    BOOL SymFindFileInPath(
        [ProcessHandle] hProcess,
        PCTSTR SearchPath,
        PCTSTR FileName,
        PVOID id,
        DWORD two,
        DWORD three,
        [SSRVOPT] flags,
        PTSTR FilePath,
        PFINDFILEINPATHCALLBACK callback,
        PVOID context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SearchPath", "FileName", "id", "two", "three", "flags", "FilePath", "callback", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFindFileInPathA(jitter):
    dbghelp_SymFindFileInPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymFindFileInPathW(jitter):
    dbghelp_SymFindFileInPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymFromAddr(jitter, get_str, set_str):
    """
    BOOL SymFromAddr(
        [ProcessHandle] hProcess,
        DWORD64 Address,
        PDWORD64 Displacement,
        PSYMBOL_INFO Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Address", "Displacement", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFromAddrA(jitter):
    dbghelp_SymFromAddr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymFromAddrW(jitter):
    dbghelp_SymFromAddr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymFromIndex(jitter, get_str, set_str):
    """
    BOOL SymFromIndex(
        [ProcessHandle] hProcess,
        ULONG64 BaseOfDll,
        DWORD Index,
        PSYMBOL_INFO Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Index", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFromIndexA(jitter):
    dbghelp_SymFromIndex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymFromIndexW(jitter):
    dbghelp_SymFromIndex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymFromName(jitter, get_str, set_str):
    """
    BOOL SymFromName(
        [ProcessHandle] hProcess,
        PCTSTR Name,
        PSYMBOL_INFO Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Name", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFromNameA(jitter):
    dbghelp_SymFromName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymFromNameW(jitter):
    dbghelp_SymFromName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymFromToken(jitter, get_str, set_str):
    """
    BOOL SymFromToken(
        [ProcessHandle] hProcess,
        DWORD64 Base,
        DWORD Token,
        PSYMBOL_INFO Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "Token", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFromTokenA(jitter):
    dbghelp_SymFromToken(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymFromTokenW(jitter):
    dbghelp_SymFromToken(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymFunctionTableAccess(jitter):
    """
    PVOID SymFunctionTableAccess(
        [ProcessHandle] hProcess,
        DWORD AddrBase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "AddrBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymFunctionTableAccess64(jitter):
    """
    PVOID SymFunctionTableAccess64(
        [ProcessHandle] hProcess,
        DWORD64 AddrBase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "AddrBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetFileLineOffsets64(jitter):
    """
    ULONG SymGetFileLineOffsets64(
        [ProcessHandle] hProcess,
        PCSTR ModuleName,
        PCSTR FileName,
        PDWORD64 Buffer,
        ULONG BufferLines
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModuleName", "FileName", "Buffer", "BufferLines"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetHomeDirectory(jitter, get_str, set_str):
    """
    PTCHAR SymGetHomeDirectory(
        DWORD type,
        PTSTR dir,
        size_t size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["type", "dir", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetHomeDirectoryA(jitter):
    dbghelp_SymGetHomeDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetHomeDirectoryW(jitter):
    dbghelp_SymGetHomeDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetLineFromAddr(jitter, get_str, set_str):
    """
    BOOL SymGetLineFromAddr(
        [ProcessHandle] hProcess,
        DWORD dwAddr,
        PDWORD pdwDisplacement,
        PIMAGEHLP_LINE Line
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "pdwDisplacement", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineFromAddrA(jitter):
    dbghelp_SymGetLineFromAddr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetLineFromAddrW(jitter):
    dbghelp_SymGetLineFromAddr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetLineFromAddr64(jitter):
    """
    BOOL SymGetLineFromAddr64(
        [ProcessHandle] hProcess,
        DWORD64 dwAddr,
        PDWORD pdwDisplacement,
        PIMAGEHLP_LINE64 Line
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "pdwDisplacement", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineFromAddrW64(jitter):
    """
    BOOL SymGetLineFromAddrW64(
        [ProcessHandle] hProcess,
        DWORD64 dwAddr,
        PDWORD pdwDisplacement,
        PIMAGEHLP_LINEW64 Line
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "pdwDisplacement", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineFromName(jitter):
    """
    BOOL SymGetLineFromName(
        [ProcessHandle] hProcess,
        PCSTR ModuleName,
        PCSTR FileName,
        DWORD dwLineNumber,
        PLONG plDisplacement,
        PIMAGEHLP_LINE Line
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModuleName", "FileName", "dwLineNumber", "plDisplacement", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineFromName64(jitter):
    """
    BOOL SymGetLineFromName64(
        [ProcessHandle] hProcess,
        PCSTR ModuleName,
        PCSTR FileName,
        DWORD dwLineNumber,
        PLONG lpDisplacement,
        PIMAGEHLP_LINE64 Line
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModuleName", "FileName", "dwLineNumber", "lpDisplacement", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineFromNameW64(jitter):
    """
    BOOL SymGetLineFromNameW64(
        [ProcessHandle] hProcess,
        PCWSTR ModuleName,
        PCWSTR FileName,
        DWORD dwLineNumber,
        PLONG lpDisplacement,
        PIMAGEHLP_LINEW64 Line
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModuleName", "FileName", "dwLineNumber", "lpDisplacement", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineNext(jitter, get_str, set_str):
    """
    BOOL SymGetLineNext(
        [ProcessHandle] hProcess,
        PIMAGEHLP_LINE Line
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineNextA(jitter):
    dbghelp_SymGetLineNext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetLineNextW(jitter):
    dbghelp_SymGetLineNext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetLineNext64(jitter):
    """
    BOOL SymGetLineNext64(
        [ProcessHandle] hProcess,
        PIMAGEHLP_LINE64 Line
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLineNextW64(jitter):
    """
    BOOL SymGetLineNextW64(
        [ProcessHandle] hProcess,
        PIMAGEHLP_LINEW64 Line
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLinePrev(jitter, get_str, set_str):
    """
    BOOL SymGetLinePrev(
        [ProcessHandle] hProcess,
        PIMAGEHLP_LINE Line
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLinePrevA(jitter):
    dbghelp_SymGetLinePrev(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetLinePrevW(jitter):
    dbghelp_SymGetLinePrev(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetLinePrev64(jitter):
    """
    BOOL SymGetLinePrev64(
        [ProcessHandle] hProcess,
        PIMAGEHLP_LINE64 Line
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetLinePrevW64(jitter):
    """
    BOOL SymGetLinePrevW64(
        [ProcessHandle] hProcess,
        PIMAGEHLP_LINEW64 Line
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Line"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetModuleBase(jitter):
    """
    DWORD SymGetModuleBase(
        [ProcessHandle] hProcess,
        DWORD dwAddr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetModuleBase64(jitter):
    """
    DWORD64 SymGetModuleBase64(
        [ProcessHandle] hProcess,
        DWORD64 dwAddr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetModuleInfo(jitter, get_str, set_str):
    """
    BOOL SymGetModuleInfo(
        [ProcessHandle] hProcess,
        DWORD dwAddr,
        PIMAGEHLP_MODULE ModuleInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "ModuleInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetModuleInfoA(jitter):
    dbghelp_SymGetModuleInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetModuleInfoW(jitter):
    dbghelp_SymGetModuleInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetModuleInfo64(jitter):
    """
    BOOL SymGetModuleInfo64(
        [ProcessHandle] hProcess,
        DWORD64 dwAddr,
        PIMAGEHLP_MODULE64 ModuleInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "ModuleInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetModuleInfoW64(jitter):
    """
    BOOL SymGetModuleInfoW64(
        [ProcessHandle] hProcess,
        DWORD64 dwAddr,
        PIMAGEHLP_MODULEW64 ModuleInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "ModuleInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetOmaps(jitter):
    """
    BOOL SymGetOmaps(
        [ProcessHandle] hProcess,
        ULONG64 BaseOfDll,
        POMAP* OmapTo,
        PDWORD64 cOmapTo,
        POMAP* OmapFrom,
        PDWORD64 cOmapFrom
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "OmapTo", "cOmapTo", "OmapFrom", "cOmapFrom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetOptions(jitter):
    """
    [SYMOPT_FLAGS] SymGetOptions()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetScope(jitter, get_str, set_str):
    """
    BOOL SymGetScope(
        [ProcessHandle] hProcess,
        ULONG64 BaseOfDll,
        DWORD Index,
        PSYMBOL_INFO Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Index", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetScopeA(jitter):
    dbghelp_SymGetScope(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetScopeW(jitter):
    dbghelp_SymGetScope(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetSearchPath(jitter, get_str, set_str):
    """
    BOOL SymGetSearchPath(
        [ProcessHandle] hProcess,
        PTSTR SearchPath,
        DWORD SearchPathLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SearchPath", "SearchPathLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSearchPathA(jitter):
    dbghelp_SymGetSearchPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetSearchPathW(jitter):
    dbghelp_SymGetSearchPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetSymbolFile(jitter, get_str, set_str):
    """
    BOOL SymGetSymbolFile(
        [ProcessHandle] hProcess,
        PCTSTR SymPath,
        PCTSTR ImageFile,
        DWORD Type,
        PTSTR SymbolFile,
        size_t cSymbolFile,
        PTSTR DbgFile,
        size_t cDbgFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SymPath", "ImageFile", "Type", "SymbolFile", "cSymbolFile", "DbgFile", "cDbgFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymbolFileA(jitter):
    dbghelp_SymGetSymbolFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetSymbolFileW(jitter):
    dbghelp_SymGetSymbolFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetTypeFromName(jitter, get_str, set_str):
    """
    BOOL SymGetTypeFromName(
        [ProcessHandle] hProcess,
        ULONG64 BaseOfDll,
        PCTSTR Name,
        PSYMBOL_INFO Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Name", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetTypeFromNameA(jitter):
    dbghelp_SymGetTypeFromName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetTypeFromNameW(jitter):
    dbghelp_SymGetTypeFromName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetTypeInfo(jitter):
    """
    BOOL SymGetTypeInfo(
        [ProcessHandle] hProcess,
        DWORD64 ModBase,
        ULONG TypeId,
        IMAGEHLP_SYMBOL_TYPE_INFO GetType,
        PVOID pInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModBase", "TypeId", "GetType", "pInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetTypeInfoEx(jitter):
    """
    BOOL SymGetTypeInfoEx(
        [ProcessHandle] hProcess,
        DWORD64 ModBase,
        PIMAGEHLP_GET_TYPE_INFO_PARAMS Params
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ModBase", "Params"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymInitialize(jitter, get_str, set_str):
    """
    BOOL SymInitialize(
        [ProcessHandle] hProcess,
        PCTSTR UserSearchPath,
        BOOL fInvadeProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "UserSearchPath", "fInvadeProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymInitializeA(jitter):
    dbghelp_SymInitialize(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymInitializeW(jitter):
    dbghelp_SymInitialize(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymLoadModule(jitter):
    """
    DWORD SymLoadModule(
        [ProcessHandle] hProcess,
        HANDLE hFile,
        PCSTR ImageName,
        PCSTR ModuleName,
        DWORD BaseOfDll,
        DWORD SizeOfDll
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hFile", "ImageName", "ModuleName", "BaseOfDll", "SizeOfDll"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymLoadModule64(jitter):
    """
    DWORD64 SymLoadModule64(
        [ProcessHandle] hProcess,
        HANDLE hFile,
        PCSTR ImageName,
        PCSTR ModuleName,
        DWORD64 BaseOfDll,
        DWORD SizeOfDll
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hFile", "ImageName", "ModuleName", "BaseOfDll", "SizeOfDll"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymLoadModuleEx(jitter, get_str, set_str):
    """
    DWORD64 SymLoadModuleEx(
        [ProcessHandle] hProcess,
        HANDLE hFile,
        PCTSTR ImageName,
        PCTSTR ModuleName,
        DWORD64 BaseOfDll,
        DWORD DllSize,
        PMODLOAD_DATA Data,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "hFile", "ImageName", "ModuleName", "BaseOfDll", "DllSize", "Data", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymLoadModuleExA(jitter):
    dbghelp_SymLoadModuleEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymLoadModuleExW(jitter):
    dbghelp_SymLoadModuleEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymMatchFileName(jitter, get_str, set_str):
    """
    BOOL SymMatchFileName(
        PCTSTR FileName,
        PCTSTR Match,
        PTSTR* FileNameStop,
        PTSTR* MatchStop
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "Match", "FileNameStop", "MatchStop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymMatchFileNameA(jitter):
    dbghelp_SymMatchFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymMatchFileNameW(jitter):
    dbghelp_SymMatchFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymMatchString(jitter):
    """
    BOOL SymMatchString(
        PCSTR string,
        PCSTR expression,
        BOOL fCase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "expression", "fCase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymMatchString(jitter, get_str, set_str):
    """
    BOOL SymMatchString(
        PCTSTR string,
        PCTSTR expression,
        BOOL fCase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "expression", "fCase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymMatchStringA(jitter):
    dbghelp_SymMatchString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymMatchStringW(jitter):
    dbghelp_SymMatchString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymNext(jitter, get_str, set_str):
    """
    BOOL SymNext(
        [ProcessHandle] hProcess,
        PSYMBOL_INFO Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymNextA(jitter):
    dbghelp_SymNext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymNextW(jitter):
    dbghelp_SymNext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymPrev(jitter, get_str, set_str):
    """
    BOOL SymPrev(
        [ProcessHandle] hProcess,
        PSYMBOL_INFO Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymPrevA(jitter):
    dbghelp_SymPrev(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymPrevW(jitter):
    dbghelp_SymPrev(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymRefreshModuleList(jitter):
    """
    BOOL SymRefreshModuleList(
        [ProcessHandle] hProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymRegisterCallback(jitter):
    """
    BOOL SymRegisterCallback(
        [ProcessHandle] hProcess,
        PSYMBOL_REGISTERED_CALLBACK CallbackFunction,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "CallbackFunction", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymRegisterCallback64(jitter):
    """
    BOOL SymRegisterCallback64(
        [ProcessHandle] hProcess,
        PSYMBOL_REGISTERED_CALLBACK64 CallbackFunction,
        ULONG64 UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "CallbackFunction", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymRegisterCallbackW64(jitter):
    """
    BOOL SymRegisterCallbackW64(
        [ProcessHandle] hProcess,
        PSYMBOL_REGISTERED_CALLBACKW64 CallbackFunction,
        ULONG64 UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "CallbackFunction", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymRegisterFunctionEntryCallback(jitter):
    """
    BOOL SymRegisterFunctionEntryCallback(
        [ProcessHandle] hProcess,
        PSYMBOL_FUNCENTRY_CALLBACK CallbackFunction,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "CallbackFunction", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymRegisterFunctionEntryCallback64(jitter):
    """
    BOOL SymRegisterFunctionEntryCallback64(
        [ProcessHandle] hProcess,
        PSYMBOL_FUNCENTRY_CALLBACK64 CallbackFunction,
        ULONG64 UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "CallbackFunction", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSearch(jitter, get_str, set_str):
    """
    BOOL SymSearch(
        [ProcessHandle] hProcess,
        ULONG64 BaseOfDll,
        DWORD Index,
        DWORD SymTag,
        PCTSTR Mask,
        DWORD64 Address,
        PSYM_ENUMERATESYMBOLS_CALLBACK EnumSymbolsCallback,
        PVOID UserContext,
        [SYMSEARCH_FLAGS] Options
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Index", "SymTag", "Mask", "Address", "EnumSymbolsCallback", "UserContext", "Options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSearchA(jitter):
    dbghelp_SymSearch(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymSearchW(jitter):
    dbghelp_SymSearch(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymSetContext(jitter):
    """
    BOOL SymSetContext(
        [ProcessHandle] hProcess,
        PIMAGEHLP_STACK_FRAME StackFrame,
        PIMAGEHLP_CONTEXT Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "StackFrame", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetHomeDirectory(jitter, get_str, set_str):
    """
    PTCHAR SymSetHomeDirectory(
        [ProcessHandle] hProcess,
        PCTSTR dir
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dir"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetHomeDirectoryA(jitter):
    dbghelp_SymSetHomeDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymSetHomeDirectoryW(jitter):
    dbghelp_SymSetHomeDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymSetOptions(jitter):
    """
    DWORD SymSetOptions(
        [SYMOPT_FLAGS] SymOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SymOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetScopeFromAddr(jitter):
    """
    BOOL SymSetScopeFromAddr(
        [ProcessHandle] hProcess,
        ULONG64 Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetScopeFromIndex(jitter):
    """
    BOOL SymSetScopeFromIndex(
        [ProcessHandle] hProcess,
        ULONG64 BaseOfDll,
        DWORD Index
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "Index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumerateModules(jitter):
    """
    BOOL SymEnumerateModules(
        [ProcessHandle] hProcess,
        PSYM_ENUMMODULES_CALLBACK EnumModulesCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumerateModules64(jitter):
    """
    BOOL SymEnumerateModules64(
        [ProcessHandle] hProcess,
        PSYM_ENUMMODULES_CALLBACK64 EnumModulesCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumerateModulesW64(jitter):
    """
    BOOL SymEnumerateModulesW64(
        [ProcessHandle] hProcess,
        PSYM_ENUMMODULES_CALLBACKW64 EnumModulesCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "EnumModulesCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetSearchPath(jitter, get_str, set_str):
    """
    BOOL SymSetSearchPath(
        [ProcessHandle] hProcess,
        PCTSTR SearchPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SearchPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSetSearchPathA(jitter):
    dbghelp_SymSetSearchPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymSetSearchPathW(jitter):
    dbghelp_SymSetSearchPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymUnDName(jitter):
    """
    BOOL SymUnDName(
        PIMAGEHLP_SYMBOL sym,
        PSTR UnDecName,
        DWORD UnDecNameLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sym", "UnDecName", "UnDecNameLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymUnDName64(jitter):
    """
    BOOL SymUnDName64(
        PIMAGEHLP_SYMBOL64 sym,
        PSTR UnDecName,
        DWORD UnDecNameLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sym", "UnDecName", "UnDecNameLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymUnloadModule(jitter):
    """
    BOOL SymUnloadModule(
        [ProcessHandle] hProcess,
        DWORD BaseOfDll
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymUnloadModule64(jitter):
    """
    BOOL SymUnloadModule64(
        [ProcessHandle] hProcess,
        DWORD64 BaseOfDll
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvDeltaName(jitter, get_str, set_str):
    """
    PCTSTR SymSrvDeltaName(
        [ProcessHandle] hProcess,
        PCTSTR SymPath,
        PCTSTR Type,
        PCTSTR File1,
        PCTSTR File2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SymPath", "Type", "File1", "File2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvDeltaNameA(jitter):
    dbghelp_SymSrvDeltaName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymSrvDeltaNameW(jitter):
    dbghelp_SymSrvDeltaName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymSrvGetFileIndexes(jitter, get_str, set_str):
    """
    BOOL SymSrvGetFileIndexes(
        PCTSTR File,
        GUID* Id,
        DWORD* Val1,
        DWORD* Val2,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["File", "Id", "Val1", "Val2", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvGetFileIndexesA(jitter):
    dbghelp_SymSrvGetFileIndexes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymSrvGetFileIndexesW(jitter):
    dbghelp_SymSrvGetFileIndexes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymSrvGetFileIndexInfo(jitter, get_str, set_str):
    """
    BOOL SymSrvGetFileIndexInfo(
        PCTSTR File,
        PSYMSRV_INDEX_INFO Info,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["File", "Info", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvGetFileIndexInfoA(jitter):
    dbghelp_SymSrvGetFileIndexInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymSrvGetFileIndexInfoW(jitter):
    dbghelp_SymSrvGetFileIndexInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymSrvGetFileIndexString(jitter, get_str, set_str):
    """
    BOOL SymSrvGetFileIndexString(
        [ProcessHandle] hProcess,
        PCTSTR SrvPath,
        PCTSTR File,
        PTSTR Index,
        size_t Size,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SrvPath", "File", "Index", "Size", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvGetFileIndexStringA(jitter):
    dbghelp_SymSrvGetFileIndexString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymSrvGetFileIndexStringW(jitter):
    dbghelp_SymSrvGetFileIndexString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymSrvGetSupplement(jitter, get_str, set_str):
    """
    PCTSTR SymSrvGetSupplement(
        [ProcessHandle] hProcess,
        PCTSTR SymPath,
        PCTSTR Node,
        PCTSTR File
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SymPath", "Node", "File"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvGetSupplementA(jitter):
    dbghelp_SymSrvGetSupplement(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymSrvGetSupplementW(jitter):
    dbghelp_SymSrvGetSupplement(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymSrvIsStore(jitter, get_str, set_str):
    """
    BOOL SymSrvIsStore(
        [ProcessHandle] hProcess,
        PCTSTR path
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvIsStoreA(jitter):
    dbghelp_SymSrvIsStore(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymSrvIsStoreW(jitter):
    dbghelp_SymSrvIsStore(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymSrvStoreFile(jitter, get_str, set_str):
    """
    PCTSTR SymSrvStoreFile(
        [ProcessHandle] hProcess,
        PCTSTR SrvPath,
        PCTSTR File,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SrvPath", "File", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvStoreFileA(jitter):
    dbghelp_SymSrvStoreFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymSrvStoreFileW(jitter):
    dbghelp_SymSrvStoreFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymSrvStoreSupplement(jitter, get_str, set_str):
    """
    PCTSTR SymSrvStoreSupplement(
        [ProcessHandle] hProcess,
        const PCTSTR SymPath,
        PCTSTR Node,
        PCTSTR File,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "SymPath", "Node", "File", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymSrvStoreSupplementA(jitter):
    dbghelp_SymSrvStoreSupplement(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymSrvStoreSupplementW(jitter):
    dbghelp_SymSrvStoreSupplement(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_MiniDumpReadDumpStream(jitter):
    """
    BOOL MiniDumpReadDumpStream(
        PVOID BaseOfDump,
        ULONG StreamNumber,
        PMINIDUMP_DIRECTORY* Dir,
        PVOID* StreamPointer,
        ULONG* StreamSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseOfDump", "StreamNumber", "Dir", "StreamPointer", "StreamSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_MiniDumpWriteDump(jitter):
    """
    BOOL MiniDumpWriteDump(
        [ProcessHandle] hProcess,
        DWORD ProcessId,
        HANDLE hFile,
        MINIDUMP_TYPE DumpType,
        PMINIDUMP_EXCEPTION_INFORMATION ExceptionParam,
        PMINIDUMP_USER_STREAM_INFORMATION UserStreamParam,
        PMINIDUMP_CALLBACK_INFORMATION CallbackParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "ProcessId", "hFile", "DumpType", "ExceptionParam", "UserStreamParam", "CallbackParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSourceFile(jitter, get_str, set_str):
    """
    BOOL SymGetSourceFile(
        [ProcessHandle] hProcess,
        ULONG64 Base,
        PCTSTR Params,
        PCTSTR FileSpec,
        PTSTR FilePath,
        DWORD Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "Params", "FileSpec", "FilePath", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSourceFileA(jitter):
    dbghelp_SymGetSourceFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetSourceFileW(jitter):
    dbghelp_SymGetSourceFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetSourceFileFromToken(jitter, get_str, set_str):
    """
    BOOL SymGetSourceFileFromToken(
        [ProcessHandle] hProcess,
        PVOID Token,
        PCTSTR Params,
        PTSTR FilePath,
        DWORD Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Token", "Params", "FilePath", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSourceFileFromTokenA(jitter):
    dbghelp_SymGetSourceFileFromToken(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetSourceFileFromTokenW(jitter):
    dbghelp_SymGetSourceFileFromToken(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetSourceFileToken(jitter, get_str, set_str):
    """
    BOOL SymGetSourceFileToken(
        [ProcessHandle] hProcess,
        ULONG64 Base,
        PCTSTR FileSpec,
        PVOID* Token,
        DWORD* Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Base", "FileSpec", "Token", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSourceFileTokenA(jitter):
    dbghelp_SymGetSourceFileToken(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetSourceFileTokenW(jitter):
    dbghelp_SymGetSourceFileToken(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetSourceVarFromToken(jitter, get_str, set_str):
    """
    BOOL SymGetSourceVarFromToken(
        [ProcessHandle] hProcess,
        PVOID Token,
        PCTSTR Params,
        PCTSTR VarName,
        PTSTR Value,
        DWORD Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Token", "Params", "VarName", "Value", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSourceVarFromTokenA(jitter):
    dbghelp_SymGetSourceVarFromToken(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetSourceVarFromTokenW(jitter):
    dbghelp_SymGetSourceVarFromToken(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_MapDebugInformation(jitter):
    """
    PIMAGE_DEBUG_INFORMATION MapDebugInformation(
        HANDLE FileHandle,
        PCSTR FileName,
        PCSTR SymbolPath,
        ULONG ImageBase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "FileName", "SymbolPath", "ImageBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumerateSymbols(jitter, get_str, set_str):
    """
    BOOL SymEnumerateSymbols(
        [ProcessHandle] hProcess,
        ULONG BaseOfDll,
        PSYM_ENUMSYMBOLS_CALLBACK EnumSymbolsCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumerateSymbolsA(jitter):
    dbghelp_SymEnumerateSymbols(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymEnumerateSymbolsW(jitter):
    dbghelp_SymEnumerateSymbols(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymEnumerateSymbols64(jitter):
    """
    BOOL SymEnumerateSymbols64(
        [ProcessHandle] hProcess,
        ULONG64 BaseOfDll,
        PSYM_ENUMSYMBOLS_CALLBACK64 EnumSymbolsCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymEnumerateSymbolsW64(jitter):
    """
    BOOL SymEnumerateSymbolsW64(
        [ProcessHandle] hProcess,
        ULONG64 BaseOfDll,
        PSYM_ENUMSYMBOLS_CALLBACKW64 EnumSymbolsCallback,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "BaseOfDll", "EnumSymbolsCallback", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymFromAddr(jitter):
    """
    BOOL SymGetSymFromAddr(
        [ProcessHandle] hProcess,
        DWORD dwAddr,
        PDWORD pdwDisplacement,
        PIMAGEHLP_SYMBOL Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwAddr", "pdwDisplacement", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymFromAddr64(jitter):
    """
    BOOL SymGetSymFromAddr64(
        [ProcessHandle] hProcess,
        DWORD64 Address,
        PDWORD64 Displacement,
        PIMAGEHLP_SYMBOL64 Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Address", "Displacement", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymFromName(jitter):
    """
    BOOL SymGetSymFromName(
        [ProcessHandle] hProcess,
        PCSTR Name,
        PIMAGEHLP_SYMBOL Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Name", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymFromName64(jitter):
    """
    BOOL SymGetSymFromName64(
        [ProcessHandle] hProcess,
        PCSTR Name,
        PIMAGEHLP_SYMBOL64 Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Name", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymNext(jitter, get_str, set_str):
    """
    BOOL SymGetSymNext(
        [ProcessHandle] hProcess,
        PIMAGEHLP_SYMBOL Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymNextA(jitter):
    dbghelp_SymGetSymNext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetSymNextW(jitter):
    dbghelp_SymGetSymNext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetSymNext64(jitter):
    """
    BOOL SymGetSymNext64(
        [ProcessHandle] hProcess,
        PIMAGEHLP_SYMBOL64 Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymPrev(jitter, get_str, set_str):
    """
    BOOL SymGetSymPrev(
        [ProcessHandle] hProcess,
        PIMAGEHLP_SYMBOL Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_SymGetSymPrevA(jitter):
    dbghelp_SymGetSymPrev(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dbghelp_SymGetSymPrevW(jitter):
    dbghelp_SymGetSymPrev(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dbghelp_SymGetSymPrev64(jitter):
    """
    BOOL SymGetSymPrev64(
        [ProcessHandle] hProcess,
        PIMAGEHLP_SYMBOL64 Symbol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "Symbol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dbghelp_UnmapDebugInformation(jitter):
    """
    BOOL UnmapDebugInformation(
        PIMAGE_DEBUG_INFORMATION DebugInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DebugInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
