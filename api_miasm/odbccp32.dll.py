
def odbccp32_SQLConfigDataSource(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLConfigDataSource(HWND hwndParent, [ODBC_DSN_REQUEST] fRequest, LPCTSTR lpszDriver, LPCTSTR lpszAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "fRequest", "lpszDriver", "lpszAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLConfigDriver(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLConfigDriver(HWND hwndParent, [ODBC_DRIVER_REQUEST] fRequest, LPCTSTR lpszDriver, LPCTSTR lpszArgs, LPTSTR lpszMsg, WORD cbMsgMax, WORD* pcbMsgOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "fRequest", "lpszDriver", "lpszArgs", "lpszMsg", "cbMsgMax", "pcbMsgOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLCreateDataSource(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLCreateDataSource(HWND hwnd, LPTSTR lpszDS)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpszDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLGetConfigMode(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLGetConfigMode([ODBC_CONFIG_MODE*] pwConfigMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwConfigMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLGetInstalledDrivers(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLGetInstalledDrivers(LPTSTR lpszBuf, WORD cbBufMax, WORD* pcbBufOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszBuf", "cbBufMax", "pcbBufOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLGetPrivateProfileString(jitter):
    """"
    [ODBCCP32.DLL] int SQLGetPrivateProfileString(LPCTSTR lpszSection, LPCTSTR lpszEntry, LPCTSTR lpszDefault, LPCTSTR RetBuffer, INT cbRetBuffer, LPCTSTR lpszFilename)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszSection", "lpszEntry", "lpszDefault", "RetBuffer", "cbRetBuffer", "lpszFilename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLGetTranslator(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLGetTranslator(HWND hwndParent, LPTSTR lpszName, WORD cbNameMax, WORD* pcbNameOut, LPTSTR lpszPath, WORD cbPathMax, WORD* pcbPathOut, DWORD* pvOption)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "lpszName", "cbNameMax", "pcbNameOut", "lpszPath", "cbPathMax", "pcbPathOut", "pvOption"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLInstallDriverEx(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLInstallDriverEx(LPCTSTR lpszDriver, LPCTSTR lpszPathIn, LPTSTR lpszPathOut, WORD cbPathOutMax, WORD* pcbPathOut, [ODBC_INSTALL_REQUEST] fRequest, LPDWORD lpdwUsageCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDriver", "lpszPathIn", "lpszPathOut", "cbPathOutMax", "pcbPathOut", "fRequest", "lpdwUsageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLInstallDriverManager(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLInstallDriverManager(LPTSTR lpszPath, WORD cbPathMax, WORD* pcbPathOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPath", "cbPathMax", "pcbPathOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLInstallerError(jitter):
    """"
    [ODBCCP32.DLL] SQLRETURN SQLInstallerError(WORD iError, [ODBC_ERROR_CODE*] pfErrorCode, LPTSTR lpszErrorMsg, WORD cbErrorMsgMax, WORD* pcbErrorMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iError", "pfErrorCode", "lpszErrorMsg", "cbErrorMsgMax", "pcbErrorMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLInstallTranslator(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLInstallTranslator(LPCTSTR lpszInfFile, LPCTSTR lpszTranslator, LPCTSTR lpszPathIn, LPTSTR lpszPathOut, WORD cbPathOutMax, WORD* pcbPathOut, WORD fRequest, LPDWORD lpdwUsageCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszInfFile", "lpszTranslator", "lpszPathIn", "lpszPathOut", "cbPathOutMax", "pcbPathOut", "fRequest", "lpdwUsageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLInstallTranslatorEx(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLInstallTranslatorEx(LPCTSTR lpszTranslator, LPCTSTR lpszPathIn, LPTSTR lpszPathOut, WORD cbPathOutMax, WORD* pcbPathOut, WORD fRequest, LPDWORD lpdwUsageCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszTranslator", "lpszPathIn", "lpszPathOut", "cbPathOutMax", "pcbPathOut", "fRequest", "lpdwUsageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLManageDataSources(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLManageDataSources(HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLPostInstallerError(jitter):
    """"
    [ODBCCP32.DLL] SQLRETURN SQLPostInstallerError([ODBC_ERROR_CODE] fErrorCode, LPTSTR szErrorMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fErrorCode", "szErrorMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLReadFileDSN(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLReadFileDSN(LPCTSTR lpszFileName, LPCTSTR lpszAppName, LPCTSTR lpszKeyName, LPTSTR lpszString, WORD cbString, WORD* pcbString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszFileName", "lpszAppName", "lpszKeyName", "lpszString", "cbString", "pcbString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLRemoveDriver(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLRemoveDriver(LPCTSTR lpszDriver, BOOL fRemoveDSN, LPDWORD lpdwUsageCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDriver", "fRemoveDSN", "lpdwUsageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLRemoveDriverManager(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLRemoveDriverManager(LPDWORD pdwUsageCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pdwUsageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLRemoveDSNFromIni(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLRemoveDSNFromIni(LPCTSTR lpszDSN)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDSN"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLRemoveTranslator(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLRemoveTranslator(LPCTSTR lpszTranslator, LPDWORD lpdwUsageCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszTranslator", "lpdwUsageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLSetConfigMode(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLSetConfigMode([ODBC_CONFIG_MODE] wConfigMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["wConfigMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLValidDSN(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLValidDSN(LPCTSTR lpszDSN)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDSN"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLWriteDSNToIni(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLWriteDSNToIni(LPCTSTR lpszDSN, LPCTSTR lpszDriver)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDSN", "lpszDriver"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLWriteFileDSN(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLWriteFileDSN(LPCTSTR lpszFileName, LPCTSTR lpszAppName, LPCTSTR lpszKeyName, LPCTSTR lpszString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszFileName", "lpszAppName", "lpszKeyName", "lpszString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbccp32_SQLWritePrivateProfileString(jitter):
    """"
    [ODBCCP32.DLL] BOOL SQLWritePrivateProfileString(LPCTSTR lpszSection, LPCTSTR lpszEntry, LPCTSTR lpszString, LPCTSTR lpszFilename)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszSection", "lpszEntry", "lpszString", "lpszFilename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
