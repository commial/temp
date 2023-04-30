
def comdlg32_ChooseColor(jitter, get_str, set_str):
    """
    BOOL ChooseColor(
        LPCHOOSECOLOR lpcc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpcc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_ChooseColorA(jitter):
    comdlg32_ChooseColor(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comdlg32_ChooseColorW(jitter):
    comdlg32_ChooseColor(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comdlg32_ChooseFont(jitter, get_str, set_str):
    """
    BOOL ChooseFont(
        LPCHOOSEFONT lpcf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpcf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_ChooseFontA(jitter):
    comdlg32_ChooseFont(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comdlg32_ChooseFontW(jitter):
    comdlg32_ChooseFont(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comdlg32_CommDlgExtendedError(jitter):
    """
    DWORD CommDlgExtendedError()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_FindText(jitter, get_str, set_str):
    """
    HWND FindText(
        LPFINDREPLACE lpfr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpfr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_FindTextA(jitter):
    comdlg32_FindText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comdlg32_FindTextW(jitter):
    comdlg32_FindText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comdlg32_GetFileTitle(jitter, get_str, set_str):
    """
    short GetFileTitle(
        LPCTSTR lpszFile,
        LPTSTR lpszTitle,
        WORD cbBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFile", "lpszTitle", "cbBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_GetFileTitleA(jitter):
    comdlg32_GetFileTitle(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comdlg32_GetFileTitleW(jitter):
    comdlg32_GetFileTitle(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comdlg32_GetOpenFileName(jitter, get_str, set_str):
    """
    BOOL GetOpenFileName(
        LPOPENFILENAME lpofn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpofn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_GetOpenFileNameA(jitter):
    comdlg32_GetOpenFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comdlg32_GetOpenFileNameW(jitter):
    comdlg32_GetOpenFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comdlg32_GetSaveFileName(jitter, get_str, set_str):
    """
    BOOL GetSaveFileName(
        LPOPENFILENAME lpofn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpofn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_GetSaveFileNameA(jitter):
    comdlg32_GetSaveFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comdlg32_GetSaveFileNameW(jitter):
    comdlg32_GetSaveFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comdlg32_PageSetupDlg(jitter, get_str, set_str):
    """
    BOOL PageSetupDlg(
        LPPAGESETUPDLG lppsd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lppsd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_PageSetupDlgA(jitter):
    comdlg32_PageSetupDlg(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comdlg32_PageSetupDlgW(jitter):
    comdlg32_PageSetupDlg(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comdlg32_PrintDlg(jitter, get_str, set_str):
    """
    BOOL PrintDlg(
        LPPRINTDLG lppd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lppd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_PrintDlgA(jitter):
    comdlg32_PrintDlg(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comdlg32_PrintDlgW(jitter):
    comdlg32_PrintDlg(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comdlg32_PrintDlgEx(jitter, get_str, set_str):
    """
    HRESULT PrintDlgEx(
        LPPRINTDLGEX lppd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lppd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_PrintDlgExA(jitter):
    comdlg32_PrintDlgEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comdlg32_PrintDlgExW(jitter):
    comdlg32_PrintDlgEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comdlg32_ReplaceText(jitter, get_str, set_str):
    """
    HWND ReplaceText(
        LPFINDREPLACE lpfr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpfr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comdlg32_ReplaceTextA(jitter):
    comdlg32_ReplaceText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comdlg32_ReplaceTextW(jitter):
    comdlg32_ReplaceText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
