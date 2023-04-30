
def comdlg32_ChooseColor(jitter):
    """"
    [comdlg32.dll] BOOL ChooseColor(LPCHOOSECOLOR lpcc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpcc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_ChooseFont(jitter):
    """"
    [comdlg32.dll] BOOL ChooseFont(LPCHOOSEFONT lpcf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpcf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_CommDlgExtendedError(jitter):
    """"
    [comdlg32.dll] DWORD CommDlgExtendedError()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_FindText(jitter):
    """"
    [comdlg32.dll] HWND FindText(LPFINDREPLACE lpfr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpfr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_GetFileTitle(jitter):
    """"
    [comdlg32.dll] short GetFileTitle(LPCTSTR lpszFile, LPTSTR lpszTitle, WORD cbBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszFile", "lpszTitle", "cbBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_GetOpenFileName(jitter):
    """"
    [comdlg32.dll] BOOL GetOpenFileName(LPOPENFILENAME lpofn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpofn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_GetSaveFileName(jitter):
    """"
    [comdlg32.dll] BOOL GetSaveFileName(LPOPENFILENAME lpofn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpofn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_PageSetupDlg(jitter):
    """"
    [comdlg32.dll] BOOL PageSetupDlg(LPPAGESETUPDLG lppsd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lppsd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_PrintDlg(jitter):
    """"
    [comdlg32.dll] BOOL PrintDlg(LPPRINTDLG lppd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lppd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_PrintDlgEx(jitter):
    """"
    [comdlg32.dll] HRESULT PrintDlgEx(LPPRINTDLGEX lppd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lppd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_ReplaceText(jitter):
    """"
    [comdlg32.dll] HWND ReplaceText(LPFINDREPLACE lpfr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpfr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
