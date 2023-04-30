
def ieframe_IECancelSaveFile(jitter):
    """"
    [ieframe.dll] HRESULT IECancelSaveFile(HANDLE hState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IECreateDirectory(jitter):
    """"
    [ieframe.dll] BOOL IECreateDirectory(LPCWSTR lpPathName, LPSECURITY_ATTRIBUTES lpSecurityAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPathName", "lpSecurityAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IECreateFile(jitter):
    """"
    [ieframe.dll] HANDLE IECreateFile(LPCWSTR lpFileName, DWORD dwDesiredAccess, DWORD dwShareMode, LPSECURITY_ATTRIBUTES lpSecurityAttributes, DWORD dwCreationDisposition, DWORD dwFlagsAndAttributes, HANDLE hTemplateFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "dwDesiredAccess", "dwShareMode", "lpSecurityAttributes", "dwCreationDisposition", "dwFlagsAndAttributes", "hTemplateFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IEDeleteFile(jitter):
    """"
    [ieframe.dll] BOOL IEDeleteFile(LPCWSTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IEFindFirstFile(jitter):
    """"
    [ieframe.dll] HANDLE IEFindFirstFile(LPCWSTR lpFileName, LPWIN32_FIND_DATA lpFindFileData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "lpFindFileData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IEGetFileAttributesEx(jitter):
    """"
    [ieframe.dll] BOOL IEGetFileAttributesEx(LPCWSTR lpFileName, GET_FILEEX_INFO_LEVELS fInfoLevelId, LPVOID lpFileInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "fInfoLevelId", "lpFileInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IEGetProtectedModeCookie(jitter):
    """"
    [ieframe.dll] HRESULT IEGetProtectedModeCookie(LPCWSTR lpszURL, LPCWSTR lpszCookieName, LPWSTR pszCookieData, DWORD* pcchCookieData, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszURL", "lpszCookieName", "pszCookieData", "pcchCookieData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IEGetWriteableFolderPath(jitter):
    """"
    [ieframe.dll] HRESULT IEGetWriteableFolderPath(GUID clsidFolderID, LPWSTR* lppwstrPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clsidFolderID", "lppwstrPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IEGetWriteableHKCU(jitter):
    """"
    [ieframe.dll] HRESULT IEGetWriteableHKCU(HKEY* phKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IEIsProtectedModeProcess(jitter):
    """"
    [ieframe.dll] HRESULT IEIsProtectedModeProcess(BOOL* pbResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pbResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IEIsProtectedModeURL(jitter):
    """"
    [ieframe.dll] HRESULT IEIsProtectedModeURL(LPCWSTR pszUrl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszUrl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IELaunchURL(jitter):
    """"
    [ieframe.dll] HRESULT IELaunchURL(LPCWSTR pszUrl, LPPROCESS_INFORMATION pProcInfo, LPIELAUNCHURLINFO lpInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszUrl", "pProcInfo", "lpInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IEMoveFileEx(jitter):
    """"
    [ieframe.dll] BOOL IEMoveFileEx(LPCWSTR lpExistingFileName, LPCWSTR lpNewFileName, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpExistingFileName", "lpNewFileName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IERefreshElevationPolicy(jitter):
    """"
    [ieframe.dll] HRESULT IERefreshElevationPolicy()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IERegCreateKeyEx(jitter):
    """"
    [ieframe.dll] HRESULT IERegCreateKeyEx(LPCWSTR lpSubKey, DWORD reserved, LPWSTR lpClass, DWORD dwOptions, REGSAM samDesired, LPSECURITY_ATTRIBUTES lpSecurityAttributes, PHKEY phkResult, LPDWORD lpdwDisposition)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSubKey", "reserved", "lpClass", "dwOptions", "samDesired", "lpSecurityAttributes", "phkResult", "lpdwDisposition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IERegisterWritableRegistryKey(jitter):
    """"
    [ieframe.dll] HRESULT IERegisterWritableRegistryKey(GUID guid, LPCWSTR lpSubkey, BOOL fSubkeyAllowed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["guid", "lpSubkey", "fSubkeyAllowed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IERegisterWritableRegistryValue(jitter):
    """"
    [ieframe.dll] HRESULT IERegisterWritableRegistryValue(GUID guid, LPCWSTR lpPath, LPCWSTR lpValueName, DWORD dwType, const BYTE* lpData, DWORD cbMaxData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["guid", "lpPath", "lpValueName", "dwType", "lpData", "cbMaxData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IERegSetValueEx(jitter):
    """"
    [ieframe.dll] HRESULT IERegSetValueEx(LPCWSTR lpSubKey, LPCWSTR lpValueName, DWORD Reserved, DWORD dwType, const BYTE* lpData, DWORD cbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSubKey", "lpValueName", "Reserved", "dwType", "lpData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IERemoveDirectory(jitter):
    """"
    [ieframe.dll] BOOL IERemoveDirectory(LPCWSTR lpPathName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPathName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IESaveFile(jitter):
    """"
    [ieframe.dll] HRESULT IESaveFile(HANDLE hState, LPWSTR lpwstrSourceFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hState", "lpwstrSourceFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IESetProtectedModeCookie(jitter):
    """"
    [ieframe.dll] HRESULT IESetProtectedModeCookie(LPCWSTR lpszURL, LPCWSTR lpszCookieName, LPWSTR pszCookieData, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszURL", "lpszCookieName", "pszCookieData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IEShowSaveFileDialog(jitter):
    """"
    [ieframe.dll] HRESULT IEShowSaveFileDialog(HWND hwnd, LPWSTR lpwstrInitialFileName, LPWSTR lpwstrInitialDir, LPCWSTR lpwstrFilter, LPCWSTR lpwstrDefExt, DWORD dwFilterIndex, DWORD dwFlags, LPWSTR* lppwstrDestinationFilePath, HANDLE* phState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpwstrInitialFileName", "lpwstrInitialDir", "lpwstrFilter", "lpwstrDefExt", "dwFilterIndex", "dwFlags", "lppwstrDestinationFilePath", "phState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ieframe_IEUnregisterWritableRegistry(jitter):
    """"
    [ieframe.dll] HRESULT IEUnregisterWritableRegistry(GUID guid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["guid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
