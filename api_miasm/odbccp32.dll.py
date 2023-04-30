
def odbccp32_SQLConfigDataSource(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLConfigDataSource(HWND hwndParent, [ODBC_DSN_REQUEST] fRequest, LPCTSTR lpszDriver, LPCTSTR lpszAttributes)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "fRequest", "lpszDriver", "lpszAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLConfigDataSourceA(jitter):
    odbccp32_SQLConfigDataSource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLConfigDataSourceW(jitter):
    odbccp32_SQLConfigDataSource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLConfigDriver(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLConfigDriver(HWND hwndParent, [ODBC_DRIVER_REQUEST] fRequest, LPCTSTR lpszDriver, LPCTSTR lpszArgs, LPTSTR lpszMsg, WORD cbMsgMax, WORD* pcbMsgOut)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "fRequest", "lpszDriver", "lpszArgs", "lpszMsg", "cbMsgMax", "pcbMsgOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLConfigDriverA(jitter):
    odbccp32_SQLConfigDriver(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLConfigDriverW(jitter):
    odbccp32_SQLConfigDriver(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLCreateDataSource(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLCreateDataSource(HWND hwnd, LPTSTR lpszDS)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpszDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLCreateDataSourceA(jitter):
    odbccp32_SQLCreateDataSource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLCreateDataSourceW(jitter):
    odbccp32_SQLCreateDataSource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLGetConfigMode(jitter):
    """
    [ODBCCP32.DLL] BOOL SQLGetConfigMode([ODBC_CONFIG_MODE*] pwConfigMode)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwConfigMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLGetInstalledDrivers(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLGetInstalledDrivers(LPTSTR lpszBuf, WORD cbBufMax, WORD* pcbBufOut)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszBuf", "cbBufMax", "pcbBufOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLGetInstalledDriversA(jitter):
    odbccp32_SQLGetInstalledDrivers(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLGetInstalledDriversW(jitter):
    odbccp32_SQLGetInstalledDrivers(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLGetPrivateProfileString(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] int SQLGetPrivateProfileString(LPCTSTR lpszSection, LPCTSTR lpszEntry, LPCTSTR lpszDefault, LPCTSTR RetBuffer, INT cbRetBuffer, LPCTSTR lpszFilename)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszSection", "lpszEntry", "lpszDefault", "RetBuffer", "cbRetBuffer", "lpszFilename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLGetPrivateProfileStringA(jitter):
    odbccp32_SQLGetPrivateProfileString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLGetPrivateProfileStringW(jitter):
    odbccp32_SQLGetPrivateProfileString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLGetTranslator(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLGetTranslator(HWND hwndParent, LPTSTR lpszName, WORD cbNameMax, WORD* pcbNameOut, LPTSTR lpszPath, WORD cbPathMax, WORD* pcbPathOut, DWORD* pvOption)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "lpszName", "cbNameMax", "pcbNameOut", "lpszPath", "cbPathMax", "pcbPathOut", "pvOption"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLGetTranslatorA(jitter):
    odbccp32_SQLGetTranslator(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLGetTranslatorW(jitter):
    odbccp32_SQLGetTranslator(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLInstallDriverEx(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLInstallDriverEx(LPCTSTR lpszDriver, LPCTSTR lpszPathIn, LPTSTR lpszPathOut, WORD cbPathOutMax, WORD* pcbPathOut, [ODBC_INSTALL_REQUEST] fRequest, LPDWORD lpdwUsageCount)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDriver", "lpszPathIn", "lpszPathOut", "cbPathOutMax", "pcbPathOut", "fRequest", "lpdwUsageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLInstallDriverExA(jitter):
    odbccp32_SQLInstallDriverEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLInstallDriverExW(jitter):
    odbccp32_SQLInstallDriverEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLInstallDriverManager(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLInstallDriverManager(LPTSTR lpszPath, WORD cbPathMax, WORD* pcbPathOut)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPath", "cbPathMax", "pcbPathOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLInstallDriverManagerA(jitter):
    odbccp32_SQLInstallDriverManager(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLInstallDriverManagerW(jitter):
    odbccp32_SQLInstallDriverManager(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLInstallerError(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] SQLRETURN SQLInstallerError(WORD iError, [ODBC_ERROR_CODE*] pfErrorCode, LPTSTR lpszErrorMsg, WORD cbErrorMsgMax, WORD* pcbErrorMsg)
    """
    ret_ad, args = jitter.func_args_stdcall(["iError", "pfErrorCode", "lpszErrorMsg", "cbErrorMsgMax", "pcbErrorMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLInstallerErrorA(jitter):
    odbccp32_SQLInstallerError(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLInstallerErrorW(jitter):
    odbccp32_SQLInstallerError(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLInstallTranslator(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLInstallTranslator(LPCTSTR lpszInfFile, LPCTSTR lpszTranslator, LPCTSTR lpszPathIn, LPTSTR lpszPathOut, WORD cbPathOutMax, WORD* pcbPathOut, WORD fRequest, LPDWORD lpdwUsageCount)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszInfFile", "lpszTranslator", "lpszPathIn", "lpszPathOut", "cbPathOutMax", "pcbPathOut", "fRequest", "lpdwUsageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLInstallTranslatorA(jitter):
    odbccp32_SQLInstallTranslator(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLInstallTranslatorW(jitter):
    odbccp32_SQLInstallTranslator(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLInstallTranslatorEx(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLInstallTranslatorEx(LPCTSTR lpszTranslator, LPCTSTR lpszPathIn, LPTSTR lpszPathOut, WORD cbPathOutMax, WORD* pcbPathOut, WORD fRequest, LPDWORD lpdwUsageCount)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszTranslator", "lpszPathIn", "lpszPathOut", "cbPathOutMax", "pcbPathOut", "fRequest", "lpdwUsageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLInstallTranslatorExA(jitter):
    odbccp32_SQLInstallTranslatorEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLInstallTranslatorExW(jitter):
    odbccp32_SQLInstallTranslatorEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLManageDataSources(jitter):
    """
    [ODBCCP32.DLL] BOOL SQLManageDataSources(HWND hwnd)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLPostInstallerError(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] SQLRETURN SQLPostInstallerError([ODBC_ERROR_CODE] fErrorCode, LPTSTR szErrorMsg)
    """
    ret_ad, args = jitter.func_args_stdcall(["fErrorCode", "szErrorMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLPostInstallerErrorA(jitter):
    odbccp32_SQLPostInstallerError(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLPostInstallerErrorW(jitter):
    odbccp32_SQLPostInstallerError(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLReadFileDSN(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLReadFileDSN(LPCTSTR lpszFileName, LPCTSTR lpszAppName, LPCTSTR lpszKeyName, LPTSTR lpszString, WORD cbString, WORD* pcbString)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFileName", "lpszAppName", "lpszKeyName", "lpszString", "cbString", "pcbString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLReadFileDSNA(jitter):
    odbccp32_SQLReadFileDSN(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLReadFileDSNW(jitter):
    odbccp32_SQLReadFileDSN(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLRemoveDriver(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLRemoveDriver(LPCTSTR lpszDriver, BOOL fRemoveDSN, LPDWORD lpdwUsageCount)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDriver", "fRemoveDSN", "lpdwUsageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLRemoveDriverA(jitter):
    odbccp32_SQLRemoveDriver(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLRemoveDriverW(jitter):
    odbccp32_SQLRemoveDriver(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLRemoveDriverManager(jitter):
    """
    [ODBCCP32.DLL] BOOL SQLRemoveDriverManager(LPDWORD pdwUsageCount)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwUsageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLRemoveDSNFromIni(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLRemoveDSNFromIni(LPCTSTR lpszDSN)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDSN"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLRemoveDSNFromIniA(jitter):
    odbccp32_SQLRemoveDSNFromIni(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLRemoveDSNFromIniW(jitter):
    odbccp32_SQLRemoveDSNFromIni(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLRemoveTranslator(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLRemoveTranslator(LPCTSTR lpszTranslator, LPDWORD lpdwUsageCount)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszTranslator", "lpdwUsageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLRemoveTranslatorA(jitter):
    odbccp32_SQLRemoveTranslator(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLRemoveTranslatorW(jitter):
    odbccp32_SQLRemoveTranslator(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLSetConfigMode(jitter):
    """
    [ODBCCP32.DLL] BOOL SQLSetConfigMode([ODBC_CONFIG_MODE] wConfigMode)
    """
    ret_ad, args = jitter.func_args_stdcall(["wConfigMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLValidDSN(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLValidDSN(LPCTSTR lpszDSN)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDSN"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLValidDSNA(jitter):
    odbccp32_SQLValidDSN(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLValidDSNW(jitter):
    odbccp32_SQLValidDSN(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLWriteDSNToIni(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLWriteDSNToIni(LPCTSTR lpszDSN, LPCTSTR lpszDriver)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDSN", "lpszDriver"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLWriteDSNToIniA(jitter):
    odbccp32_SQLWriteDSNToIni(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLWriteDSNToIniW(jitter):
    odbccp32_SQLWriteDSNToIni(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLWriteFileDSN(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLWriteFileDSN(LPCTSTR lpszFileName, LPCTSTR lpszAppName, LPCTSTR lpszKeyName, LPCTSTR lpszString)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFileName", "lpszAppName", "lpszKeyName", "lpszString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLWriteFileDSNA(jitter):
    odbccp32_SQLWriteFileDSN(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLWriteFileDSNW(jitter):
    odbccp32_SQLWriteFileDSN(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbccp32_SQLWritePrivateProfileString(jitter, get_str, set_str):
    """
    [ODBCCP32.DLL] BOOL SQLWritePrivateProfileString(LPCTSTR lpszSection, LPCTSTR lpszEntry, LPCTSTR lpszString, LPCTSTR lpszFilename)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszSection", "lpszEntry", "lpszString", "lpszFilename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLWritePrivateProfileStringA(jitter):
    odbccp32_SQLWritePrivateProfileString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbccp32_SQLWritePrivateProfileStringW(jitter):
    odbccp32_SQLWritePrivateProfileString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
