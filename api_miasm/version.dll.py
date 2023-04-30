
def version_GetFileVersionInfo(jitter, get_str, set_str):
    """"
    [version.dll] BOOL GetFileVersionInfo(LPCTSTR lptstrFilename, DWORD dwHandle, DWORD dwLen, LPVOID lpData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lptstrFilename", "dwHandle", "dwLen", "lpData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def version_GetFileVersionInfoA(jitter):
    version_GetFileVersionInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def version_GetFileVersionInfoW(jitter):
    version_GetFileVersionInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def version_GetFileVersionInfoExW(jitter):
    """"
    [version.dll] BOOL GetFileVersionInfoExW([FILE_VER_GET_FLAGS] dwFlags, LPCWSTR lptstrFilename, DWORD dwHandle, DWORD dwLen, LPVOID lpData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lptstrFilename", "dwHandle", "dwLen", "lpData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def version_GetFileVersionInfoSize(jitter, get_str, set_str):
    """"
    [version.dll] DWORD GetFileVersionInfoSize(LPCTSTR lptstrFilename, LPDWORD lpdwHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lptstrFilename", "lpdwHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def version_GetFileVersionInfoSizeA(jitter):
    version_GetFileVersionInfoSize(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def version_GetFileVersionInfoSizeW(jitter):
    version_GetFileVersionInfoSize(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def version_GetFileVersionInfoSizeExW(jitter):
    """"
    [version.dll] DWORD GetFileVersionInfoSizeExW([FILE_VER_GET_FLAGS] dwFlags, LPCTSTR lptstrFilename, LPDWORD lpdwHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lptstrFilename", "lpdwHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def version_VerFindFile(jitter, get_str, set_str):
    """"
    [version.dll] [VFF_RESULT] VerFindFile([VFF_FLAGS] dwFlags, LPCTSTR szFileName, LPCTSTR szWinDir, LPCTSTR szAppDir, LPCSTR szCurDir, PUINT lpuCurDirLen, LPTSTR szDestDir, PUINT lpuDestDirLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "szFileName", "szWinDir", "szAppDir", "szCurDir", "lpuCurDirLen", "szDestDir", "lpuDestDirLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def version_VerFindFileA(jitter):
    version_VerFindFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def version_VerFindFileW(jitter):
    version_VerFindFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def version_VerInstallFile(jitter, get_str, set_str):
    """"
    [version.dll] [VIF_RESULT] VerInstallFile([VIF_FLAGS] uFlags, LPCTSTR szSrcFileName, LPCTSTR szDestFileName, LPCTSTR szSrcDir, LPCTSTR szDestDir, LPCTSTR szCurDir, LPTSTR szTmpFile, PUINT lpuTmpFileLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uFlags", "szSrcFileName", "szDestFileName", "szSrcDir", "szDestDir", "szCurDir", "szTmpFile", "lpuTmpFileLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def version_VerInstallFileA(jitter):
    version_VerInstallFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def version_VerInstallFileW(jitter):
    version_VerInstallFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def version_VerQueryValue(jitter, get_str, set_str):
    """"
    [version.dll] BOOL VerQueryValue(LPCVOID pBlock, LPCTSTR lpSubBlock, LPVOID* lplpBuffer, PUINT puLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBlock", "lpSubBlock", "lplpBuffer", "puLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def version_VerQueryValueA(jitter):
    version_VerQueryValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def version_VerQueryValueW(jitter):
    version_VerQueryValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
