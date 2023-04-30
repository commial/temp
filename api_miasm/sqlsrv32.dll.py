
def sqlsrv32_ConfigDriver(jitter):
    """"
    [SQLSRV32.DLL] BOOL ConfigDriver(HWND hwndParent, [ODBC_DRIVER_REQUEST] fRequest, LPCTSTR lpszDriver, LPCTSTR lpszArgs, LPTSTR lpszMsg, WORD cbMsgMax, WORD* pcbMsgOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "fRequest", "lpszDriver", "lpszArgs", "lpszMsg", "cbMsgMax", "pcbMsgOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sqlsrv32_ConfigDSN(jitter):
    """"
    [SQLSRV32.DLL] BOOL ConfigDSN(HWND hwndParent, [ODBC_DSN_REQUEST] fRequest, LPCTSTR lpszDriver, LPCTSTR lpszAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "fRequest", "lpszDriver", "lpszAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sqlsrv32_ConfigTranslator(jitter):
    """"
    [SQLSRV32.DLL] BOOL ConfigTranslator(HWND hwndParent, DWORD* pvOption)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "pvOption"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
