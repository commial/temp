
def user32_CreateDialogIndirectParam(jitter, get_str, set_str):
    """
    HWND CreateDialogIndirectParam(
        HINSTANCE hInstance,
        LPCDLGTEMPLATE lpTemplate,
        HWND hWndParent,
        DLGPROC lpDialogFunc,
        LPARAM lParamInit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpTemplate", "hWndParent", "lpDialogFunc", "lParamInit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateDialogIndirectParamA(jitter):
    user32_CreateDialogIndirectParam(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CreateDialogIndirectParamW(jitter):
    user32_CreateDialogIndirectParam(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CreateDialogParam(jitter, get_str, set_str):
    """
    HWND CreateDialogParam(
        HINSTANCE hInstance,
        LPCTSTR lpTemplateName,
        HWND hWndParent,
        DLGPROC lpDialogFunc,
        LPARAM lParamInit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpTemplateName", "hWndParent", "lpDialogFunc", "lParamInit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateDialogParamA(jitter):
    user32_CreateDialogParam(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CreateDialogParamW(jitter):
    user32_CreateDialogParam(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DefDlgProc(jitter, get_str, set_str):
    """
    LRESULT DefDlgProc(
        HWND hDlg,
        [WinMsg] Msg,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DefDlgProcA(jitter):
    user32_DefDlgProc(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DefDlgProcW(jitter):
    user32_DefDlgProc(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DialogBoxIndirectParam(jitter, get_str, set_str):
    """
    INT_PTR DialogBoxIndirectParam(
        HINSTANCE hInstance,
        LPCDLGTEMPLATE hDialogTemplate,
        HWND hWndParent,
        DLGPROC lpDialogFunc,
        LPARAM dwInitParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "hDialogTemplate", "hWndParent", "lpDialogFunc", "dwInitParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DialogBoxIndirectParamA(jitter):
    user32_DialogBoxIndirectParam(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DialogBoxIndirectParamW(jitter):
    user32_DialogBoxIndirectParam(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DialogBoxParam(jitter, get_str, set_str):
    """
    INT_PTR DialogBoxParam(
        HINSTANCE hInstance,
        LPCTSTR lpTemplateName,
        HWND hWndParent,
        DLGPROC lpDialogFunc,
        LPARAM dwInitParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpTemplateName", "hWndParent", "lpDialogFunc", "dwInitParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DialogBoxParamA(jitter):
    user32_DialogBoxParam(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DialogBoxParamW(jitter):
    user32_DialogBoxParam(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_EndDialog(jitter):
    """
    BOOL EndDialog(
        HWND hDlg,
        INT_PTR nResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDialogBaseUnits(jitter):
    """
    LONG GetDialogBaseUnits()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDlgCtrlID(jitter):
    """
    int GetDlgCtrlID(
        HWND hwndCtl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndCtl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDlgItem(jitter):
    """
    HWND GetDlgItem(
        HWND hDlg,
        int nIDDlgItem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDDlgItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDlgItemInt(jitter):
    """
    UINT GetDlgItemInt(
        HWND hDlg,
        int nIDDlgItem,
        BOOL* lpTranslated,
        BOOL bSigned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDDlgItem", "lpTranslated", "bSigned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDlgItemText(jitter, get_str, set_str):
    """
    UINT GetDlgItemText(
        HWND hDlg,
        int nIDDlgItem,
        LPTSTR lpString,
        int nMaxCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDDlgItem", "lpString", "nMaxCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDlgItemTextA(jitter):
    user32_GetDlgItemText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetDlgItemTextW(jitter):
    user32_GetDlgItemText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetNextDlgGroupItem(jitter):
    """
    HWND GetNextDlgGroupItem(
        HWND hDlg,
        HWND hCtl,
        BOOL bPrevious
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "hCtl", "bPrevious"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetNextDlgTabItem(jitter):
    """
    HWND GetNextDlgTabItem(
        HWND hDlg,
        HWND hCtl,
        BOOL bPrevious
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "hCtl", "bPrevious"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsDialogMessage(jitter, get_str, set_str):
    """
    BOOL IsDialogMessage(
        HWND hDlg,
        LPMSG lpMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "lpMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsDialogMessageA(jitter):
    user32_IsDialogMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_IsDialogMessageW(jitter):
    user32_IsDialogMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_MapDialogRect(jitter):
    """
    BOOL MapDialogRect(
        HWND hDlg,
        LPRECT lpRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MessageBox(jitter, get_str, set_str):
    """
    [MessageBoxResult] MessageBox(
        HWND hWnd,
        LPCTSTR lpText,
        LPCTSTR lpCaption,
        [MessageBoxType] uType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpText", "lpCaption", "uType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MessageBoxA(jitter):
    user32_MessageBox(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_MessageBoxW(jitter):
    user32_MessageBox(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_MessageBoxEx(jitter, get_str, set_str):
    """
    [MessageBoxResult] MessageBoxEx(
        HWND hWnd,
        LPCTSTR lpText,
        LPCTSTR lpCaption,
        [MessageBoxType] uType,
        WORD wLanguageId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpText", "lpCaption", "uType", "wLanguageId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MessageBoxExA(jitter):
    user32_MessageBoxEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_MessageBoxExW(jitter):
    user32_MessageBoxEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_MessageBoxIndirect(jitter, get_str, set_str):
    """
    int MessageBoxIndirect(
        const LPMSGBOXPARAMS lpMsgBoxParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpMsgBoxParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MessageBoxIndirectA(jitter):
    user32_MessageBoxIndirect(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_MessageBoxIndirectW(jitter):
    user32_MessageBoxIndirect(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_MessageBoxTimeout(jitter, get_str, set_str):
    """
    [MessageBoxResult] MessageBoxTimeout(
        HWND hWnd,
        LPCTSTR lpText,
        LPCTSTR lpCaption,
        [MessageBoxType] uType,
        WORD wLanguageId,
        [WaitTimeout] dwMilliseconds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpText", "lpCaption", "uType", "wLanguageId", "dwMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MessageBoxTimeoutA(jitter):
    user32_MessageBoxTimeout(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_MessageBoxTimeoutW(jitter):
    user32_MessageBoxTimeout(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_SendDlgItemMessage(jitter, get_str, set_str):
    """
    LRESULT SendDlgItemMessage(
        HWND hDlg,
        int nIDDlgItem,
        [WinMsg] Msg,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDDlgItem", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SendDlgItemMessageA(jitter):
    user32_SendDlgItemMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SendDlgItemMessageW(jitter):
    user32_SendDlgItemMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_SetDlgItemInt(jitter):
    """
    BOOL SetDlgItemInt(
        HWND hDlg,
        int nIDDlgItem,
        UINT uValue,
        BOOL bSigned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDDlgItem", "uValue", "bSigned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetDlgItemText(jitter, get_str, set_str):
    """
    BOOL SetDlgItemText(
        HWND hDlg,
        int nIDDlgItem,
        LPCTSTR lpString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDDlgItem", "lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetDlgItemTextA(jitter):
    user32_SetDlgItemText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SetDlgItemTextW(jitter):
    user32_SetDlgItemText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_BroadcastSystemMessage(jitter):
    """
    long BroadcastSystemMessage(
        DWORD dwFlags,
        LPDWORD lpdwRecipients,
        UINT uiMessage,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpdwRecipients", "uiMessage", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BroadcastSystemMessageEx(jitter, get_str, set_str):
    """
    long BroadcastSystemMessageEx(
        DWORD dwFlags,
        LPDWORD lpdwRecipients,
        UINT uiMessage,
        WPARAM wParam,
        LPARAM lParam,
        PBSMINFO pBSMInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpdwRecipients", "uiMessage", "wParam", "lParam", "pBSMInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BroadcastSystemMessageExA(jitter):
    user32_BroadcastSystemMessageEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_BroadcastSystemMessageExW(jitter):
    user32_BroadcastSystemMessageEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DispatchMessage(jitter, get_str, set_str):
    """
    LRESULT DispatchMessage(
        const MSG* lpmsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpmsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DispatchMessageA(jitter):
    user32_DispatchMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DispatchMessageW(jitter):
    user32_DispatchMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetInputState(jitter):
    """
    BOOL GetInputState()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMessage(jitter, get_str, set_str):
    """
    [BOOL_NUMBER] GetMessage(
        LPMSG lpMsg,
        HWND hWnd,
        UINT wMsgFilterMin,
        UINT wMsgFilterMax
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpMsg", "hWnd", "wMsgFilterMin", "wMsgFilterMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMessageA(jitter):
    user32_GetMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetMessageW(jitter):
    user32_GetMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetMessageExtraInfo(jitter):
    """
    LPARAM GetMessageExtraInfo()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMessagePos(jitter):
    """
    DWORD GetMessagePos()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMessageTime(jitter):
    """
    LONG GetMessageTime()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetQueueStatus(jitter):
    """
    DWORD GetQueueStatus(
        [QueueStatusFlag] flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InSendMessage(jitter):
    """
    BOOL InSendMessage()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InSendMessageEx(jitter):
    """
    DWORD InSendMessageEx(
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PeekMessage(jitter, get_str, set_str):
    """
    BOOL PeekMessage(
        LPMSG lpMsg,
        HWND hWnd,
        UINT wMsgFilterMin,
        UINT wMsgFilterMax,
        [PeekMessageFlag] wRemoveMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpMsg", "hWnd", "wMsgFilterMin", "wMsgFilterMax", "wRemoveMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PeekMessageA(jitter):
    user32_PeekMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_PeekMessageW(jitter):
    user32_PeekMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_PostMessage(jitter, get_str, set_str):
    """
    BOOL PostMessage(
        HWND hWnd,
        [WinMsg] Msg,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PostMessageA(jitter):
    user32_PostMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_PostMessageW(jitter):
    user32_PostMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_PostQuitMessage(jitter):
    """
    VOID PostQuitMessage(
        int nExitCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nExitCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PostThreadMessage(jitter, get_str, set_str):
    """
    BOOL PostThreadMessage(
        DWORD idThread,
        [WinMsg] Msg,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idThread", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PostThreadMessageA(jitter):
    user32_PostThreadMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_PostThreadMessageW(jitter):
    user32_PostThreadMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_RegisterWindowMessage(jitter, get_str, set_str):
    """
    UINT RegisterWindowMessage(
        LPCTSTR lpString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterWindowMessageA(jitter):
    user32_RegisterWindowMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_RegisterWindowMessageW(jitter):
    user32_RegisterWindowMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_ReplyMessage(jitter):
    """
    BOOL ReplyMessage(
        LRESULT lResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SendMessage(jitter, get_str, set_str):
    """
    LRESULT SendMessage(
        HWND hWnd,
        [WinMsg] Msg,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SendMessageA(jitter):
    user32_SendMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SendMessageW(jitter):
    user32_SendMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_SendMessageCallback(jitter, get_str, set_str):
    """
    BOOL SendMessageCallback(
        HWND hWnd,
        [WinMsg] Msg,
        WPARAM wParam,
        LPARAM lParam,
        SENDASYNCPROC lpCallBack,
        ULONG_PTR dwData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "Msg", "wParam", "lParam", "lpCallBack", "dwData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SendMessageCallbackA(jitter):
    user32_SendMessageCallback(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SendMessageCallbackW(jitter):
    user32_SendMessageCallback(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_SendMessageTimeout(jitter, get_str, set_str):
    """
    LRESULT SendMessageTimeout(
        HWND hWnd,
        [WinMsg] Msg,
        WPARAM wParam,
        LPARAM lParam,
        [SendMessageTimeoutFlags] fuFlags,
        UINT uTimeout,
        PDWORD_PTR lpdwResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "Msg", "wParam", "lParam", "fuFlags", "uTimeout", "lpdwResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SendMessageTimeoutA(jitter):
    user32_SendMessageTimeout(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SendMessageTimeoutW(jitter):
    user32_SendMessageTimeout(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_SendNotifyMessage(jitter, get_str, set_str):
    """
    BOOL SendNotifyMessage(
        HWND hWnd,
        [WinMsg] Msg,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SendNotifyMessageA(jitter):
    user32_SendNotifyMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SendNotifyMessageW(jitter):
    user32_SendNotifyMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_SetMessageExtraInfo(jitter):
    """
    LPARAM SetMessageExtraInfo(
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TranslateMessage(jitter):
    """
    BOOL TranslateMessage(
        const MSG* lpMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_WaitMessage(jitter):
    """
    BOOL WaitMessage()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetGuiResources(jitter):
    """
    DWORD GetGuiResources(
        [ProcessHandle] hProcess,
        DWORD uiFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "uiFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsImmersiveProcess(jitter):
    """
    BOOL IsImmersiveProcess(
        HANDLE hProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetProcessRestrictionExemption(jitter):
    """
    BOOL SetProcessRestrictionExemption(
        BOOL fEnableExemption
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fEnableExemption"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AttachThreadInput(jitter):
    """
    BOOL AttachThreadInput(
        DWORD idAttach,
        DWORD idAttachTo,
        BOOL fAttach
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idAttach", "idAttachTo", "fAttach"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_WaitForInputIdle(jitter):
    """
    DWORD WaitForInputIdle(
        [ProcessHandle] hProcess,
        [WaitTimeout] dwMilliseconds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWow64Message(jitter):
    """
    BOOL IsWow64Message()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UserHandleGrantAccess(jitter):
    """
    BOOL UserHandleGrantAccess(
        HANDLE hUserHandle,
        HANDLE hJob,
        BOOL bGrant
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUserHandle", "hJob", "bGrant"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AdjustWindowRect(jitter):
    """
    BOOL AdjustWindowRect(
        LPRECT lpRect,
        [WindowStyle] dwStyle,
        BOOL bMenu
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpRect", "dwStyle", "bMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AdjustWindowRectEx(jitter):
    """
    BOOL AdjustWindowRectEx(
        LPRECT lpRect,
        [WindowStyle] dwStyle,
        BOOL bMenu,
        [WindowExStyle] dwExStyle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpRect", "dwStyle", "bMenu", "dwExStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AllowActivateDetachQueuesSetFocus(jitter):
    """
    VOID AllowActivateDetachQueuesSetFocus()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AllowSetForegroundWindow(jitter):
    """
    BOOL AllowSetForegroundWindow(
        DWORD dwProcessId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AnimateWindow(jitter):
    """
    BOOL AnimateWindow(
        HWND hwnd,
        DWORD dwTime,
        [AnimateWindowFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwTime", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AnyPopup(jitter):
    """
    BOOL AnyPopup()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ArrangeIconicWindows(jitter):
    """
    UINT ArrangeIconicWindows(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BeginDeferWindowPos(jitter):
    """
    HDWP BeginDeferWindowPos(
        int nNumWindows
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nNumWindows"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BringWindowToTop(jitter):
    """
    BOOL BringWindowToTop(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CalculatePopupWindowPosition(jitter):
    """
    BOOL CalculatePopupWindowPosition(
        const POINT* anchorPoint,
        const SIZE* windowSize,
        [TrackPopupMenuFlags] flags,
        RECT* excludeRect,
        RECT* popupWindowPosition
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["anchorPoint", "windowSize", "flags", "excludeRect", "popupWindowPosition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CascadeWindows(jitter):
    """
    WORD CascadeWindows(
        HWND hwndParent,
        [MDITILE_CASCADE] wHow,
        const RECT* lpRect,
        UINT cKids,
        const HWND* lpKids
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "wHow", "lpRect", "cKids", "lpKids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChangeWindowMessageFilter(jitter):
    """
    BOOL ChangeWindowMessageFilter(
        [WinMsg] message,
        [WindowMessageFilterEnum] dwFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["message", "dwFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChangeWindowMessageFilterEx(jitter):
    """
    BOOL ChangeWindowMessageFilterEx(
        HWND hWnd,
        [WinMsg] message,
        [MSGFLT_ACTION] action,
        PCHANGEFILTERSTRUCT pChangeFilterStruct
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "message", "action", "pChangeFilterStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChildWindowFromPoint(jitter):
    """
    HWND ChildWindowFromPoint(
        HWND hWndParent,
        POINT Point
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndParent", "Point"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChildWindowFromPointEx(jitter):
    """
    HWND ChildWindowFromPointEx(
        HWND hwndParent,
        POINT pt,
        [CWP_FLAGS] uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "pt", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CloseWindow(jitter):
    """
    BOOL CloseWindow(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateWindow(jitter, get_str, set_str):
    """
    HWND CreateWindow(
        LPCTSTR lpClassName,
        LPCTSTR lpWindowName,
        DWORD dwStyle,
        [CreateWindow_CW] x,
        [CreateWindow_CW] y,
        [CreateWindow_CW] nWidth,
        [CreateWindow_CW] nHeight,
        HWND hWndParent,
        HMENU hMenu,
        HINSTANCE hInstance,
        LPVOID lpParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpClassName", "lpWindowName", "dwStyle", "x", "y", "nWidth", "nHeight", "hWndParent", "hMenu", "hInstance", "lpParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateWindowA(jitter):
    user32_CreateWindow(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CreateWindowW(jitter):
    user32_CreateWindow(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CreateWindowEx(jitter, get_str, set_str):
    """
    HWND CreateWindowEx(
        [WindowExStyle] dwExStyle,
        LPCTSTR lpClassName,
        LPCTSTR lpWindowName,
        [WindowStyle] dwStyle,
        [CreateWindow_CW] x,
        [CreateWindow_CW] y,
        [CreateWindow_CW] nWidth,
        [CreateWindow_CW] nHeight,
        HWND hWndParent,
        HMENU hMenu,
        HINSTANCE hInstance,
        LPVOID lpParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwExStyle", "lpClassName", "lpWindowName", "dwStyle", "x", "y", "nWidth", "nHeight", "hWndParent", "hMenu", "hInstance", "lpParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateWindowExA(jitter):
    user32_CreateWindowEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CreateWindowExW(jitter):
    user32_CreateWindowEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DeferWindowPos(jitter):
    """
    HDWP DeferWindowPos(
        HDWP hWinPosInfo,
        HWND hWnd,
        [HwndInsertAfterEnum] hWndInsertAfter,
        int x,
        int y,
        int cx,
        int cy,
        [SetWindowPosFlags] uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWinPosInfo", "hWnd", "hWndInsertAfter", "x", "y", "cx", "cy", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DeregisterShellHookWindow(jitter):
    """
    BOOL DeregisterShellHookWindow(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DestroyWindow(jitter):
    """
    BOOL DestroyWindow(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EndDeferWindowPos(jitter):
    """
    BOOL EndDeferWindowPos(
        HDWP hWinPosInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWinPosInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EndTask(jitter):
    """
    BOOL EndTask(
        HWND hWnd,
        BOOL fShutDown,
        BOOL fForce
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "fShutDown", "fForce"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumChildWindows(jitter):
    """
    BOOL EnumChildWindows(
        HWND hWndParent,
        WNDENUMPROC lpEnumFunc,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndParent", "lpEnumFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumThreadWindows(jitter):
    """
    BOOL EnumThreadWindows(
        DWORD dwThreadId,
        WNDENUMPROC lpfn,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwThreadId", "lpfn", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumWindows(jitter):
    """
    BOOL EnumWindows(
        WNDENUMPROC lpEnumFunc,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpEnumFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FindWindow(jitter, get_str, set_str):
    """
    HWND FindWindow(
        LPCTSTR lpClassName,
        LPCTSTR lpWindowName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpClassName", "lpWindowName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FindWindowA(jitter):
    user32_FindWindow(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_FindWindowW(jitter):
    user32_FindWindow(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_FindWindowEx(jitter, get_str, set_str):
    """
    HWND FindWindowEx(
        HWND hwndParent,
        HWND hwndChildAfter,
        LPCTSTR lpszClass,
        LPCTSTR lpszWindow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hwndChildAfter", "lpszClass", "lpszWindow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FindWindowExA(jitter):
    user32_FindWindowEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_FindWindowExW(jitter):
    user32_FindWindowEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetAltTabInfo(jitter, get_str, set_str):
    """
    BOOL GetAltTabInfo(
        HWND hwnd,
        int iItem,
        PALTTABINFO pati,
        LPTSTR pszItemText,
        UINT cchItemText
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "iItem", "pati", "pszItemText", "cchItemText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetAltTabInfoA(jitter):
    user32_GetAltTabInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetAltTabInfoW(jitter):
    user32_GetAltTabInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetAncestor(jitter):
    """
    HWND GetAncestor(
        HWND hwnd,
        [GetAncestorEnum] gaFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "gaFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClientRect(jitter):
    """
    BOOL GetClientRect(
        HWND hWnd,
        LPRECT lpRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDesktopWindow(jitter):
    """
    HWND GetDesktopWindow()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetForegroundWindow(jitter):
    """
    HWND GetForegroundWindow()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetGUIThreadInfo(jitter):
    """
    BOOL GetGUIThreadInfo(
        DWORD idThread,
        LPGUITHREADINFO lpgui
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idThread", "lpgui"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetLastActivePopup(jitter):
    """
    HWND GetLastActivePopup(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetLayeredWindowAttributes(jitter):
    """
    BOOL GetLayeredWindowAttributes(
        HWND hwnd,
        COLORREF* pcrKey,
        BYTE* pbAlpha,
        [LayeredWindowAttribute*] pdwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pcrKey", "pbAlpha", "pdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetParent(jitter):
    """
    HWND GetParent(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetProcessDefaultLayout(jitter):
    """
    BOOL GetProcessDefaultLayout(
        DWORD* pdwDefaultLayout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwDefaultLayout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetShellWindow(jitter):
    """
    HWND GetShellWindow()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetTitleBarInfo(jitter):
    """
    BOOL GetTitleBarInfo(
        HWND hwnd,
        PTITLEBARINFO pti
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pti"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetTopWindow(jitter):
    """
    HWND GetTopWindow(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindow(jitter):
    """
    HWND GetWindow(
        HWND hWnd,
        [GetWindowEnum] uCmd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "uCmd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowDisplayAffinity(jitter):
    """
    BOOL GetWindowDisplayAffinity(
        HWND hWnd,
        DWORD* dwAffinity
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "dwAffinity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowInfo(jitter):
    """
    BOOL GetWindowInfo(
        HWND hwnd,
        PWINDOWINFO pwi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pwi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowModuleFileName(jitter, get_str, set_str):
    """
    UINT GetWindowModuleFileName(
        HWND hwnd,
        LPTSTR lpszFileName,
        UINT cchFileNameMax
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpszFileName", "cchFileNameMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowModuleFileNameA(jitter):
    user32_GetWindowModuleFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetWindowModuleFileNameW(jitter):
    user32_GetWindowModuleFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetWindowPlacement(jitter):
    """
    BOOL GetWindowPlacement(
        HWND hWnd,
        WINDOWPLACEMENT* lpwndpl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpwndpl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowRect(jitter):
    """
    BOOL GetWindowRect(
        HWND hWnd,
        LPRECT lpRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowText(jitter, get_str, set_str):
    """
    int GetWindowText(
        HWND hWnd,
        LPTSTR lpString,
        int nMaxCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpString", "nMaxCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowTextA(jitter):
    user32_GetWindowText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetWindowTextW(jitter):
    user32_GetWindowText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetWindowTextLength(jitter, get_str, set_str):
    """
    int GetWindowTextLength(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowTextLengthA(jitter):
    user32_GetWindowTextLength(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetWindowTextLengthW(jitter):
    user32_GetWindowTextLength(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetWindowThreadProcessId(jitter):
    """
    DWORD GetWindowThreadProcessId(
        HWND hWnd,
        LPDWORD lpdwProcessId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpdwProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InternalGetWindowText(jitter):
    """
    int InternalGetWindowText(
        HWND hWnd,
        LPWSTR lpString,
        int nMaxCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpString", "nMaxCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsChild(jitter):
    """
    BOOL IsChild(
        HWND hWndParent,
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndParent", "hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsGUIThread(jitter):
    """
    BOOL IsGUIThread(
        BOOL bConvert
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bConvert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsHungAppWindow(jitter):
    """
    BOOL IsHungAppWindow(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsIconic(jitter):
    """
    BOOL IsIconic(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsProcessDPIAware(jitter):
    """
    BOOL IsProcessDPIAware()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWindow(jitter):
    """
    BOOL IsWindow(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWindowUnicode(jitter):
    """
    BOOL IsWindowUnicode(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWindowVisible(jitter):
    """
    BOOL IsWindowVisible(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsZoomed(jitter):
    """
    BOOL IsZoomed(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LockSetForegroundWindow(jitter):
    """
    BOOL LockSetForegroundWindow(
        [LockSetForegroundWindowCode] uLockCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uLockCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LogicalToPhysicalPoint(jitter):
    """
    void LogicalToPhysicalPoint(
        HWND hWnd,
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MoveWindow(jitter):
    """
    BOOL MoveWindow(
        HWND hWnd,
        int X,
        int Y,
        int nWidth,
        int nHeight,
        BOOL bRepaint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "X", "Y", "nWidth", "nHeight", "bRepaint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OpenIcon(jitter):
    """
    BOOL OpenIcon(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PhysicalToLogicalPoint(jitter):
    """
    void PhysicalToLogicalPoint(
        HWND hWnd,
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RealChildWindowFromPoint(jitter):
    """
    HWND RealChildWindowFromPoint(
        HWND hwndParent,
        POINT ptParentClientCoords
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "ptParentClientCoords"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RealGetWindowClass(jitter):
    """
    UINT RealGetWindowClass(
        HWND hwnd,
        LPTSTR pszType,
        UINT cchType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszType", "cchType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterShellHookWindow(jitter):
    """
    BOOL RegisterShellHookWindow(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetForegroundWindow(jitter):
    """
    BOOL SetForegroundWindow(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetLayeredWindowAttributes(jitter):
    """
    BOOL SetLayeredWindowAttributes(
        HWND hwnd,
        COLORREF crKey,
        BYTE bAlpha,
        [LayeredWindowAttribute] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "crKey", "bAlpha", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetParent(jitter):
    """
    HWND SetParent(
        HWND hWndChild,
        HWND hWndNewParent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndChild", "hWndNewParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetProcessDefaultLayout(jitter):
    """
    BOOL SetProcessDefaultLayout(
        DWORD dwDefaultLayout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwDefaultLayout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetProcessDPIAware(jitter):
    """
    BOOL SetProcessDPIAware()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowDisplayAffinity(jitter):
    """
    BOOL SetWindowDisplayAffinity(
        HWND hWnd,
        DWORD dwAffinity
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "dwAffinity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowPlacement(jitter):
    """
    BOOL SetWindowPlacement(
        HWND hWnd,
        WINDOWPLACEMENT* lpwndpl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpwndpl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowPos(jitter):
    """
    BOOL SetWindowPos(
        HWND hWnd,
        [HwndInsertAfterEnum] hWndInsertAfter,
        int X,
        int Y,
        int cx,
        int cy,
        [SetWindowPosFlags] uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hWndInsertAfter", "X", "Y", "cx", "cy", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowText(jitter, get_str, set_str):
    """
    BOOL SetWindowText(
        HWND hWnd,
        LPCTSTR lpString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowTextA(jitter):
    user32_SetWindowText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SetWindowTextW(jitter):
    user32_SetWindowText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_ShowOwnedPopups(jitter):
    """
    BOOL ShowOwnedPopups(
        HWND hWnd,
        BOOL fShow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "fShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShowWindow(jitter):
    """
    BOOL ShowWindow(
        HWND hWnd,
        [ShowWindowCmd] nCmdShow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nCmdShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShowWindowAsync(jitter):
    """
    BOOL ShowWindowAsync(
        HWND hWnd,
        int nCmdShow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nCmdShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SoundSentry(jitter):
    """
    BOOL SoundSentry()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SwitchToThisWindow(jitter):
    """
    VOID SwitchToThisWindow(
        HWND hWnd,
        BOOL fAltTab
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "fAltTab"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TileWindows(jitter):
    """
    WORD TileWindows(
        HWND hwndParent,
        [MDITILE_TILE] wHow,
        RECT* lpRect,
        UINT cKids,
        const HWND* lpKids
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "wHow", "lpRect", "cKids", "lpKids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UpdateLayeredWindow(jitter):
    """
    BOOL UpdateLayeredWindow(
        HWND hwnd,
        HDC hdcDst,
        POINT* pptDst,
        SIZE* psize,
        HDC hdcSrc,
        POINT* pptSrc,
        COLORREF crKey,
        BLENDFUNCTION* pblend,
        [UpdateLayeredWindowFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdcDst", "pptDst", "psize", "hdcSrc", "pptSrc", "crKey", "pblend", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UpdateLayeredWindowIndirect(jitter):
    """
    BOOL UpdateLayeredWindowIndirect(
        HWND hwnd,
        const UPDATELAYEREDWINDOWINFO* pULWInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pULWInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_WindowFromPhysicalPoint(jitter):
    """
    HWND WindowFromPhysicalPoint(
        POINT Point
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Point"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_WindowFromPoint(jitter):
    """
    HWND WindowFromPoint(
        POINT Point
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Point"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ExitWindowsEx(jitter):
    """
    BOOL ExitWindowsEx(
        [EWX_FLAGS] uFlags,
        [SHTDN_REASON] dwReason
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uFlags", "dwReason"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LockWorkStation(jitter):
    """
    BOOL LockWorkStation()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShutdownBlockReasonCreate(jitter):
    """
    BOOL ShutdownBlockReasonCreate(
        HWND hWnd,
        LPCWSTR pwszReason
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pwszReason"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShutdownBlockReasonDestroy(jitter):
    """
    BOOL ShutdownBlockReasonDestroy(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShutdownBlockReasonQuery(jitter):
    """
    BOOL ShutdownBlockReasonQuery(
        HWND hWnd,
        LPWSTR pwszBuff,
        DWORD* pcchBuff
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pwszBuff", "pcchBuff"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadBitmap(jitter, get_str, set_str):
    """
    HBITMAP LoadBitmap(
        HINSTANCE hInstance,
        [LoadBitmapString/LPCTSTR] lpBitmapName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpBitmapName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadBitmapA(jitter):
    user32_LoadBitmap(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_LoadBitmapW(jitter):
    user32_LoadBitmap(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetSysColorBrush(jitter):
    """
    HBRUSH GetSysColorBrush(
        [SysColorIndex] nIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CheckDlgButton(jitter):
    """
    BOOL CheckDlgButton(
        HWND hDlg,
        int nIDButton,
        [ButtonState] uCheck
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDButton", "uCheck"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CheckRadioButton(jitter):
    """
    BOOL CheckRadioButton(
        HWND hDlg,
        int nIDFirstButton,
        int nIDLastButton,
        int nIDCheckButton
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDFirstButton", "nIDLastButton", "nIDCheckButton"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsDlgButtonChecked(jitter):
    """
    [ButtonState] IsDlgButtonChecked(
        HWND hDlg,
        int nIDButton
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDButton"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateCaret(jitter):
    """
    BOOL CreateCaret(
        HWND hWnd,
        HBITMAP hBitmap,
        int nWidth,
        int nHeight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hBitmap", "nWidth", "nHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DestroyCaret(jitter):
    """
    BOOL DestroyCaret()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCaretBlinkTime(jitter):
    """
    UINT GetCaretBlinkTime()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCaretPos(jitter):
    """
    BOOL GetCaretPos(
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_HideCaret(jitter):
    """
    BOOL HideCaret(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetCaretBlinkTime(jitter):
    """
    BOOL SetCaretBlinkTime(
        UINT uMSeconds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uMSeconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetCaretPos(jitter):
    """
    BOOL SetCaretPos(
        int X,
        int Y
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["X", "Y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShowCaret(jitter):
    """
    BOOL ShowCaret(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AddClipboardFormatListener(jitter):
    """
    BOOL AddClipboardFormatListener(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChangeClipboardChain(jitter):
    """
    BOOL ChangeClipboardChain(
        HWND hWndRemove,
        HWND hWndNewNext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndRemove", "hWndNewNext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CloseClipboard(jitter):
    """
    BOOL CloseClipboard()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CountClipboardFormats(jitter):
    """
    int CountClipboardFormats()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EmptyClipboard(jitter):
    """
    BOOL EmptyClipboard()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumClipboardFormats(jitter):
    """
    UINT EnumClipboardFormats(
        UINT format
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClipboardData(jitter):
    """
    HANDLE GetClipboardData(
        [ClipboardFormat] uFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClipboardFormatName(jitter, get_str, set_str):
    """
    int GetClipboardFormatName(
        UINT format,
        LPTSTR lpszFormatName,
        int cchMaxCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["format", "lpszFormatName", "cchMaxCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClipboardFormatNameA(jitter):
    user32_GetClipboardFormatName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetClipboardFormatNameW(jitter):
    user32_GetClipboardFormatName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetClipboardOwner(jitter):
    """
    HWND GetClipboardOwner()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClipboardSequenceNumber(jitter):
    """
    DWORD GetClipboardSequenceNumber()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClipboardViewer(jitter):
    """
    HWND GetClipboardViewer()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetOpenClipboardWindow(jitter):
    """
    HWND GetOpenClipboardWindow()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPriorityClipboardFormat(jitter):
    """
    int GetPriorityClipboardFormat(
        UINT* paFormatPriorityList,
        int cFormats
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["paFormatPriorityList", "cFormats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetUpdatedClipboardFormats(jitter):
    """
    BOOL GetUpdatedClipboardFormats(
        PUINT lpuiFormats,
        UINT cFormats,
        PUINT pcFormatsOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpuiFormats", "cFormats", "pcFormatsOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsClipboardFormatAvailable(jitter):
    """
    BOOL IsClipboardFormatAvailable(
        [ClipboardFormat] format
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OpenClipboard(jitter):
    """
    BOOL OpenClipboard(
        HWND hWndNewOwner
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndNewOwner"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterClipboardFormat(jitter, get_str, set_str):
    """
    UINT RegisterClipboardFormat(
        LPCTSTR lpszFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterClipboardFormatA(jitter):
    user32_RegisterClipboardFormat(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_RegisterClipboardFormatW(jitter):
    user32_RegisterClipboardFormat(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_RemoveClipboardFormatListener(jitter):
    """
    BOOL RemoveClipboardFormatListener(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetClipboardData(jitter):
    """
    HANDLE SetClipboardData(
        [ClipboardFormat] uFormat,
        HANDLE hMem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uFormat", "hMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetClipboardViewer(jitter):
    """
    HWND SetClipboardViewer(
        HWND hWndNewViewer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndNewViewer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DlgDirListComboBox(jitter, get_str, set_str):
    """
    int DlgDirListComboBox(
        HWND hDlg,
        LPTSTR lpPathSpec,
        int nIDComboBox,
        int nIDStaticPath,
        UINT uFiletype
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "lpPathSpec", "nIDComboBox", "nIDStaticPath", "uFiletype"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DlgDirListComboBoxA(jitter):
    user32_DlgDirListComboBox(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DlgDirListComboBoxW(jitter):
    user32_DlgDirListComboBox(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DlgDirSelectComboBoxEx(jitter, get_str, set_str):
    """
    BOOL DlgDirSelectComboBoxEx(
        HWND hDlg,
        LPTSTR lpString,
        int nCount,
        int nIDComboBox
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "lpString", "nCount", "nIDComboBox"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DlgDirSelectComboBoxExA(jitter):
    user32_DlgDirSelectComboBoxEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DlgDirSelectComboBoxExW(jitter):
    user32_DlgDirSelectComboBoxEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetComboBoxInfo(jitter):
    """
    BOOL GetComboBoxInfo(
        HWND hwndCombo,
        PCOMBOBOXINFO pcbi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndCombo", "pcbi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ClientToScreen(jitter):
    """
    BOOL ClientToScreen(
        HWND hWnd,
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MapWindowPoints(jitter):
    """
    int MapWindowPoints(
        HWND hWndFrom,
        HWND hWndTo,
        LPPOINT lpPoints,
        UINT cPoints
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndFrom", "hWndTo", "lpPoints", "cPoints"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ScreenToClient(jitter):
    """
    BOOL ScreenToClient(
        HWND hWnd,
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ClipCursor(jitter):
    """
    BOOL ClipCursor(
        const RECT* lpRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CopyCursor(jitter):
    """
    HCURSOR CopyCursor(
        HCURSOR pcur
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcur"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateCursor(jitter):
    """
    HCURSOR CreateCursor(
        HINSTANCE hInst,
        int xHotSpot,
        int yHotSpot,
        int nWidth,
        int nHeight,
        const VOID* pvANDPlane,
        const VOID* pvXORPlane
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInst", "xHotSpot", "yHotSpot", "nWidth", "nHeight", "pvANDPlane", "pvXORPlane"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DestroyCursor(jitter):
    """
    BOOL DestroyCursor(
        HCURSOR hCursor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCursor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClipCursor(jitter):
    """
    BOOL GetClipCursor(
        LPRECT lpRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCursor(jitter):
    """
    HCURSOR GetCursor()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCursorInfo(jitter):
    """
    BOOL GetCursorInfo(
        PCURSORINFO pci
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pci"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCursorPos(jitter):
    """
    BOOL GetCursorPos(
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPhysicalCursorPos(jitter):
    """
    BOOL GetPhysicalCursorPos(
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadCursor(jitter, get_str, set_str):
    """
    HCURSOR LoadCursor(
        HINSTANCE hInstance,
        [LoadCursorString/LPCTSTR] lpCursorName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpCursorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadCursorA(jitter):
    user32_LoadCursor(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_LoadCursorW(jitter):
    user32_LoadCursor(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_LoadCursorFromFile(jitter, get_str, set_str):
    """
    HCURSOR LoadCursorFromFile(
        LPCTSTR lpFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadCursorFromFileA(jitter):
    user32_LoadCursorFromFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_LoadCursorFromFileW(jitter):
    user32_LoadCursorFromFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_SetCursor(jitter):
    """
    HCURSOR SetCursor(
        HCURSOR hCursor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCursor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetCursorPos(jitter):
    """
    BOOL SetCursorPos(
        int X,
        int Y
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["X", "Y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetPhysicalCursorPos(jitter):
    """
    BOOL SetPhysicalCursorPos(
        int X,
        int Y
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["X", "Y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetSystemCursor(jitter):
    """
    BOOL SetSystemCursor(
        HCURSOR hcur,
        [CursorId] id
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hcur", "id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShowCursor(jitter):
    """
    int ShowCursor(
        BOOL bShow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChangeDisplaySettings(jitter, get_str, set_str):
    """
    LONG ChangeDisplaySettings(
        DEVMODE* lpDevMode,
        DWORD dwflags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpDevMode", "dwflags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChangeDisplaySettingsA(jitter):
    user32_ChangeDisplaySettings(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_ChangeDisplaySettingsW(jitter):
    user32_ChangeDisplaySettings(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_ChangeDisplaySettingsEx(jitter, get_str, set_str):
    """
    LONG ChangeDisplaySettingsEx(
        LPCTSTR lpszDeviceName,
        DEVMODE* lpDevMode,
        HWND hwnd,
        DWORD dwflags,
        LPVOID lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDeviceName", "lpDevMode", "hwnd", "dwflags", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChangeDisplaySettingsExA(jitter):
    user32_ChangeDisplaySettingsEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_ChangeDisplaySettingsExW(jitter):
    user32_ChangeDisplaySettingsEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_EnumDisplayDevices(jitter, get_str, set_str):
    """
    BOOL EnumDisplayDevices(
        LPCTSTR lpDevice,
        DWORD iDevNum,
        PDISPLAY_DEVICE lpDisplayDevice,
        [EnumDisplayDevicesFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpDevice", "iDevNum", "lpDisplayDevice", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumDisplayDevicesA(jitter):
    user32_EnumDisplayDevices(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_EnumDisplayDevicesW(jitter):
    user32_EnumDisplayDevices(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_EnumDisplaySettings(jitter, get_str, set_str):
    """
    BOOL EnumDisplaySettings(
        LPCTSTR lpszDeviceName,
        [EnumDisplaySettingsEnum] iModeNum,
        DEVMODE* lpDevMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDeviceName", "iModeNum", "lpDevMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumDisplaySettingsA(jitter):
    user32_EnumDisplaySettings(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_EnumDisplaySettingsW(jitter):
    user32_EnumDisplaySettings(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_EnumDisplaySettingsEx(jitter, get_str, set_str):
    """
    BOOL EnumDisplaySettingsEx(
        LPCTSTR lpszDeviceName,
        DWORD iModeNum,
        DEVMODE* lpDevMode,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDeviceName", "iModeNum", "lpDevMode", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumDisplaySettingsExA(jitter):
    user32_EnumDisplaySettingsEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_EnumDisplaySettingsExW(jitter):
    user32_EnumDisplaySettingsEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetDC(jitter):
    """
    HDC GetDC(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDCEx(jitter):
    """
    HDC GetDCEx(
        HWND hWnd,
        HRGN hrgnClip,
        [DCExFlags] flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hrgnClip", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ReleaseDC(jitter):
    """
    int ReleaseDC(
        HWND hWnd,
        HDC hDC
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hDC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterDeviceNotification(jitter, get_str, set_str):
    """
    HDEVNOTIFY RegisterDeviceNotification(
        HANDLE hRecipient,
        LPVOID NotificationFilter,
        [DeviceNotificationFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRecipient", "NotificationFilter", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterDeviceNotificationA(jitter):
    user32_RegisterDeviceNotification(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_RegisterDeviceNotificationW(jitter):
    user32_RegisterDeviceNotification(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_UnregisterDeviceNotification(jitter):
    """
    BOOL UnregisterDeviceNotification(
        HDEVNOTIFY Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeSetQualityOfService(jitter):
    """
    BOOL DdeSetQualityOfService(
        HWND hwndClient,
        const SECURITY_QUALITY_OF_SERVICE* pqosNew,
        PSECURITY_QUALITY_OF_SERVICE pqosPrev
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndClient", "pqosNew", "pqosPrev"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FreeDDElParam(jitter):
    """
    BOOL FreeDDElParam(
        UINT msg,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["msg", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ImpersonateDdeClientWindow(jitter):
    """
    BOOL ImpersonateDdeClientWindow(
        HWND hWndClient,
        HWND hWndServer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndClient", "hWndServer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PackDDElParam(jitter):
    """
    LPARAM PackDDElParam(
        UINT msg,
        UINT_PTR uiLo,
        UINT_PTR uiHi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["msg", "uiLo", "uiHi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ReuseDDElParam(jitter):
    """
    LPARAM ReuseDDElParam(
        LPARAM lParam,
        UINT msgIn,
        UINT msgOut,
        UINT_PTR uiLo,
        UINT_PTR uiHi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lParam", "msgIn", "msgOut", "uiLo", "uiHi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnpackDDElParam(jitter):
    """
    BOOL UnpackDDElParam(
        UINT msg,
        LPARAM lParam,
        PUINT_PTR puiLo,
        PUINT_PTR puiHi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["msg", "lParam", "puiLo", "puiHi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeAbandonTransaction(jitter):
    """
    BOOL DdeAbandonTransaction(
        DWORD idInst,
        HCONV hConv,
        DWORD idTransaction
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hConv", "idTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeAccessData(jitter):
    """
    LPBYTE DdeAccessData(
        HDDEDATA hData,
        LPDWORD pcbDataSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hData", "pcbDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeAddData(jitter):
    """
    HDDEDATA DdeAddData(
        HDDEDATA hData,
        LPBYTE pSrc,
        DWORD cb,
        DWORD cbOff
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hData", "pSrc", "cb", "cbOff"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeClientTransaction(jitter):
    """
    HDDEDATA DdeClientTransaction(
        LPBYTE pData,
        DWORD cbData,
        HCONV hConv,
        HSZ hszItem,
        UINT wFmt,
        UINT wType,
        DWORD dwTimeout,
        LPDWORD pdwResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pData", "cbData", "hConv", "hszItem", "wFmt", "wType", "dwTimeout", "pdwResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeCmpStringHandles(jitter):
    """
    int DdeCmpStringHandles(
        HSZ hsz1,
        HSZ hsz2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hsz1", "hsz2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeConnect(jitter):
    """
    HCONV DdeConnect(
        DWORD idInst,
        HSZ hszService,
        HSZ hszTopic,
        PCONVCONTEXT pCC
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hszService", "hszTopic", "pCC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeConnectList(jitter):
    """
    HCONVLIST DdeConnectList(
        DWORD idInst,
        HSZ hszService,
        HSZ hszTopic,
        HCONVLIST hConvList,
        PCONVCONTEXT pCC
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hszService", "hszTopic", "hConvList", "pCC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeCreateDataHandle(jitter):
    """
    HDDEDATA DdeCreateDataHandle(
        DWORD idInst,
        LPBYTE pSrc,
        DWORD cb,
        DWORD cbOff,
        HSZ hszItem,
        UINT wFmt,
        UINT afCmd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idInst", "pSrc", "cb", "cbOff", "hszItem", "wFmt", "afCmd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeCreateStringHandle(jitter, get_str, set_str):
    """
    HSZ DdeCreateStringHandle(
        DWORD idInst,
        LPTSTR psz,
        [CODE_PAGE|int] iCodePage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idInst", "psz", "iCodePage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeCreateStringHandleA(jitter):
    user32_DdeCreateStringHandle(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DdeCreateStringHandleW(jitter):
    user32_DdeCreateStringHandle(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DdeDisconnect(jitter):
    """
    BOOL DdeDisconnect(
        HCONV hConv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeDisconnectList(jitter):
    """
    BOOL DdeDisconnectList(
        HCONVLIST hConvList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConvList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeEnableCallback(jitter):
    """
    BOOL DdeEnableCallback(
        DWORD idInst,
        HCONV hConv,
        UINT wCmd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hConv", "wCmd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeFreeDataHandle(jitter):
    """
    BOOL DdeFreeDataHandle(
        HDDEDATA hData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeFreeStringHandle(jitter):
    """
    BOOL DdeFreeStringHandle(
        DWORD idInst,
        HSZ hsz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeGetData(jitter):
    """
    DWORD DdeGetData(
        HDDEDATA hData,
        LPBYTE pDst,
        DWORD cbMax,
        DWORD cbOff
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hData", "pDst", "cbMax", "cbOff"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeGetLastError(jitter):
    """
    UINT DdeGetLastError(
        DWORD idInst
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idInst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeImpersonateClient(jitter):
    """
    BOOL DdeImpersonateClient(
        HCONV hConv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeInitialize(jitter, get_str, set_str):
    """
    UINT DdeInitialize(
        LPDWORD pidInst,
        PFNCALLBACK pfnCallback,
        [DDE_INITIALIZE_FLAGS] afCmd,
        DWORD ulRes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidInst", "pfnCallback", "afCmd", "ulRes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeInitializeA(jitter):
    user32_DdeInitialize(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DdeInitializeW(jitter):
    user32_DdeInitialize(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DdeKeepStringHandle(jitter):
    """
    BOOL DdeKeepStringHandle(
        DWORD idInst,
        HSZ hsz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeNameService(jitter):
    """
    HDDEDATA DdeNameService(
        DWORD idInst,
        UINT hsz1,
        UINT hsz2,
        UINT afCmd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hsz1", "hsz2", "afCmd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdePostAdvise(jitter):
    """
    BOOL DdePostAdvise(
        DWORD idInst,
        HSZ hszTopic,
        HSZ hszItem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hszTopic", "hszItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeQueryConvInfo(jitter):
    """
    UINT DdeQueryConvInfo(
        HCONV hConv,
        DWORD idTransaction,
        PCONVINFO pConvInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConv", "idTransaction", "pConvInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeQueryNextServer(jitter):
    """
    HCONV DdeQueryNextServer(
        HCONVLIST hConvList,
        HCONV hConvPrev
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConvList", "hConvPrev"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeQueryString(jitter, get_str, set_str):
    """
    DWORD DdeQueryString(
        DWORD idInst,
        HSZ hsz,
        LPTSTR psz,
        DWORD cchMax,
        [CODE_PAGE|int] iCodePage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hsz", "psz", "cchMax", "iCodePage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeQueryStringA(jitter):
    user32_DdeQueryString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DdeQueryStringW(jitter):
    user32_DdeQueryString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DdeReconnect(jitter):
    """
    HCONV DdeReconnect(
        HCONV hConv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeSetUserHandle(jitter):
    """
    BOOL DdeSetUserHandle(
        HCONV hConv,
        DWORD id,
        DWORD_PTR hUser
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hConv", "id", "hUser"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeUnaccessData(jitter):
    """
    BOOL DdeUnaccessData(
        HDDEDATA hData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeUninitialize(jitter):
    """
    BOOL DdeUninitialize(
        DWORD idInst
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idInst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FlashWindow(jitter):
    """
    BOOL FlashWindow(
        HWND hWnd,
        BOOL bInvert
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "bInvert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FlashWindowEx(jitter):
    """
    BOOL FlashWindowEx(
        PFLASHWINFO pfwi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfwi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MessageBeep(jitter):
    """
    BOOL MessageBeep(
        UINT uType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetLastErrorEx(jitter):
    """
    void SetLastErrorEx(
        [ERROR_CODE] dwErrCode,
        [SET_LAST_ERROR_EX_TYPE] dwType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwErrCode", "dwType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FillRect(jitter):
    """
    int FillRect(
        HDC hDC,
        const RECT* lprc,
        HBRUSH hbr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lprc", "hbr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FrameRect(jitter):
    """
    int FrameRect(
        HDC hDC,
        const RECT* lprc,
        HBRUSH hbr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lprc", "hbr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InvertRect(jitter):
    """
    BOOL InvertRect(
        HDC hDC,
        const RECT* lprc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawText(jitter, get_str, set_str):
    """
    int DrawText(
        HDC hDC,
        LPCTSTR lpchText,
        int nCount,
        LPRECT lpRect,
        [DrawTextFlags] uFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lpchText", "nCount", "lpRect", "uFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawTextA(jitter):
    user32_DrawText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DrawTextW(jitter):
    user32_DrawText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DrawTextEx(jitter, get_str, set_str):
    """
    int DrawTextEx(
        HDC hdc,
        LPTSTR lpchText,
        int cchText,
        LPRECT lprc,
        [DrawTextFlags] dwDTFormat,
        LPDRAWTEXTPARAMS lpDTParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpchText", "cchText", "lprc", "dwDTFormat", "lpDTParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawTextExA(jitter):
    user32_DrawTextEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DrawTextExW(jitter):
    user32_DrawTextEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetTabbedTextExtent(jitter, get_str, set_str):
    """
    DWORD GetTabbedTextExtent(
        HDC hDC,
        LPCTSTR lpString,
        int nCount,
        int nTabPositions,
        const LPINT lpnTabStopPositions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lpString", "nCount", "nTabPositions", "lpnTabStopPositions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetTabbedTextExtentA(jitter):
    user32_GetTabbedTextExtent(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetTabbedTextExtentW(jitter):
    user32_GetTabbedTextExtent(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_TabbedTextOut(jitter, get_str, set_str):
    """
    LONG TabbedTextOut(
        HDC hDC,
        int X,
        int Y,
        LPCTSTR lpString,
        int nCount,
        int nTabPositions,
        const LPINT lpnTabStopPositions,
        int nTabOrigin
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "X", "Y", "lpString", "nCount", "nTabPositions", "lpnTabStopPositions", "nTabOrigin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TabbedTextOutA(jitter):
    user32_TabbedTextOut(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_TabbedTextOutW(jitter):
    user32_TabbedTextOut(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CallMsgFilter(jitter, get_str, set_str):
    """
    BOOL CallMsgFilter(
        LPMSG lpMsg,
        int nCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpMsg", "nCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CallMsgFilterA(jitter):
    user32_CallMsgFilter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CallMsgFilterW(jitter):
    user32_CallMsgFilter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CallNextHookEx(jitter):
    """
    LRESULT CallNextHookEx(
        HHOOK hhk,
        int nCode,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hhk", "nCode", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowsHookEx(jitter, get_str, set_str):
    """
    HHOOK SetWindowsHookEx(
        [WindowsHook] idHook,
        HOOKPROC lpfn,
        HINSTANCE hMod,
        DWORD dwThreadId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idHook", "lpfn", "hMod", "dwThreadId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowsHookExA(jitter):
    user32_SetWindowsHookEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SetWindowsHookExW(jitter):
    user32_SetWindowsHookEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_UnhookWindowsHookEx(jitter):
    """
    BOOL UnhookWindowsHookEx(
        HHOOK hhk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hhk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CopyIcon(jitter):
    """
    HICON CopyIcon(
        HICON hIcon
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateIcon(jitter):
    """
    HICON CreateIcon(
        HINSTANCE hInstance,
        int nWidth,
        int nHeight,
        BYTE cPlanes,
        BYTE cBitsPixel,
        const BYTE* lpbANDbits,
        const BYTE* lpbXORbits
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "nWidth", "nHeight", "cPlanes", "cBitsPixel", "lpbANDbits", "lpbXORbits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateIconFromResource(jitter):
    """
    HICON CreateIconFromResource(
        PBYTE presbits,
        DWORD dwResSize,
        BOOL fIcon,
        DWORD dwVer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["presbits", "dwResSize", "fIcon", "dwVer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateIconFromResourceEx(jitter):
    """
    HICON CreateIconFromResourceEx(
        PBYTE pbIconBits,
        DWORD cbIconBits,
        BOOL fIcon,
        DWORD dwVersion,
        int cxDesired,
        int cyDesired,
        UINT uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbIconBits", "cbIconBits", "fIcon", "dwVersion", "cxDesired", "cyDesired", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateIconIndirect(jitter):
    """
    HICON CreateIconIndirect(
        PICONINFO piconinfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["piconinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DestroyIcon(jitter):
    """
    BOOL DestroyIcon(
        HICON hIcon
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawIcon(jitter):
    """
    BOOL DrawIcon(
        HDC hDC,
        int X,
        int Y,
        HICON hIcon
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "X", "Y", "hIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawIconEx(jitter):
    """
    BOOL DrawIconEx(
        HDC hdc,
        int xLeft,
        int yTop,
        HICON hIcon,
        int cxWidth,
        int cyWidth,
        UINT istepIfAniCur,
        HBRUSH hbrFlickerFreeDraw,
        [DrawIconFlags] diFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "xLeft", "yTop", "hIcon", "cxWidth", "cyWidth", "istepIfAniCur", "hbrFlickerFreeDraw", "diFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetIconInfo(jitter):
    """
    BOOL GetIconInfo(
        HICON hIcon,
        PICONINFO piconinfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIcon", "piconinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetIconInfoEx(jitter, get_str, set_str):
    """
    BOOL GetIconInfoEx(
        HICON hIcon,
        PICONINFOEX piconinfoex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIcon", "piconinfoex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetIconInfoExA(jitter):
    user32_GetIconInfoEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetIconInfoExW(jitter):
    user32_GetIconInfoEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_LoadIcon(jitter, get_str, set_str):
    """
    HICON LoadIcon(
        HINSTANCE hInstance,
        [LoadIconString/LPCTSTR] lpIconName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpIconName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadIconA(jitter):
    user32_LoadIcon(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_LoadIconW(jitter):
    user32_LoadIcon(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_LookupIconIdFromDirectory(jitter):
    """
    int LookupIconIdFromDirectory(
        PBYTE presbits,
        BOOL fIcon
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["presbits", "fIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LookupIconIdFromDirectoryEx(jitter):
    """
    int LookupIconIdFromDirectoryEx(
        PBYTE presbits,
        BOOL fIcon,
        int cxDesired,
        int cyDesired,
        [LRFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["presbits", "fIcon", "cxDesired", "cyDesired", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PrivateExtractIcons(jitter, get_str, set_str):
    """
    UINT PrivateExtractIcons(
        LPCTSTR lpszFile,
        int nIconIndex,
        int cxIcon,
        int cyIcon,
        HICON* phicon,
        UINT* piconid,
        UINT nIcons,
        [LRFlags] flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFile", "nIconIndex", "cxIcon", "cyIcon", "phicon", "piconid", "nIcons", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PrivateExtractIconsA(jitter):
    user32_PrivateExtractIcons(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_PrivateExtractIconsW(jitter):
    user32_PrivateExtractIcons(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CopyAcceleratorTable(jitter, get_str, set_str):
    """
    int CopyAcceleratorTable(
        HACCEL hAccelSrc,
        LPACCEL lpAccelDst,
        int cAccelEntries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAccelSrc", "lpAccelDst", "cAccelEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CopyAcceleratorTableA(jitter):
    user32_CopyAcceleratorTable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CopyAcceleratorTableW(jitter):
    user32_CopyAcceleratorTable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CreateAcceleratorTable(jitter, get_str, set_str):
    """
    HACCEL CreateAcceleratorTable(
        LPACCEL lpaccl,
        int cEntries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpaccl", "cEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateAcceleratorTableA(jitter):
    user32_CreateAcceleratorTable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CreateAcceleratorTableW(jitter):
    user32_CreateAcceleratorTable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DestroyAcceleratorTable(jitter):
    """
    BOOL DestroyAcceleratorTable(
        HACCEL hAccel
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAccel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadAccelerators(jitter, get_str, set_str):
    """
    HACCEL LoadAccelerators(
        HINSTANCE hInstance,
        LPCTSTR lpTableName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpTableName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadAcceleratorsA(jitter):
    user32_LoadAccelerators(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_LoadAcceleratorsW(jitter):
    user32_LoadAccelerators(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_TranslateAccelerator(jitter, get_str, set_str):
    """
    int TranslateAccelerator(
        HWND hWnd,
        HACCEL hAccTable,
        LPMSG lpMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hAccTable", "lpMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TranslateAcceleratorA(jitter):
    user32_TranslateAccelerator(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_TranslateAcceleratorW(jitter):
    user32_TranslateAccelerator(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_ActivateKeyboardLayout(jitter):
    """
    HKL ActivateKeyboardLayout(
        [KeyboardLayoutHandle] hkl,
        [KeyboardLayoutFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkl", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BlockInput(jitter):
    """
    BOOL BlockInput(
        BOOL fBlockIt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fBlockIt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnableWindow(jitter):
    """
    BOOL EnableWindow(
        HWND hWnd,
        BOOL bEnable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "bEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetActiveWindow(jitter):
    """
    HWND GetActiveWindow()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetAsyncKeyState(jitter):
    """
    SHORT GetAsyncKeyState(
        [VirtKeyCode] vKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetFocus(jitter):
    """
    HWND GetFocus()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKBCodePage(jitter):
    """
    UINT GetKBCodePage()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyboardLayout(jitter):
    """
    HKL GetKeyboardLayout(
        DWORD idThread
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyboardLayoutList(jitter):
    """
    UINT GetKeyboardLayoutList(
        int nBuff,
        HKL* lpList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nBuff", "lpList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyboardLayoutName(jitter, get_str, set_str):
    """
    BOOL GetKeyboardLayoutName(
        LPTSTR pwszKLID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszKLID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyboardLayoutNameA(jitter):
    user32_GetKeyboardLayoutName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetKeyboardLayoutNameW(jitter):
    user32_GetKeyboardLayoutName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetKeyboardState(jitter):
    """
    BOOL GetKeyboardState(
        PBYTE lpKeyState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpKeyState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyNameText(jitter, get_str, set_str):
    """
    int GetKeyNameText(
        LONG lParam,
        LPTSTR lpString,
        int nSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lParam", "lpString", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyNameTextA(jitter):
    user32_GetKeyNameText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetKeyNameTextW(jitter):
    user32_GetKeyNameText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetKeyState(jitter):
    """
    SHORT GetKeyState(
        [VirtKeyCode] nVirtKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nVirtKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetLastInputInfo(jitter):
    """
    BOOL GetLastInputInfo(
        PLASTINPUTINFO plii
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plii"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWindowEnabled(jitter):
    """
    BOOL IsWindowEnabled(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_keybd_event(jitter):
    """
    VOID keybd_event(
        BYTE bVk,
        BYTE bScan,
        DWORD dwFlags,
        ULONG_PTR dwExtraInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bVk", "bScan", "dwFlags", "dwExtraInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadKeyboardLayout(jitter, get_str, set_str):
    """
    HKL LoadKeyboardLayout(
        LPCTSTR pwszKLID,
        [KeyboardLayoutFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszKLID", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadKeyboardLayoutA(jitter):
    user32_LoadKeyboardLayout(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_LoadKeyboardLayoutW(jitter):
    user32_LoadKeyboardLayout(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_MapVirtualKey(jitter, get_str, set_str):
    """
    UINT MapVirtualKey(
        UINT uCode,
        [MapVirtualKeyType] uMapType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uCode", "uMapType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MapVirtualKeyA(jitter):
    user32_MapVirtualKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_MapVirtualKeyW(jitter):
    user32_MapVirtualKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_MapVirtualKeyEx(jitter, get_str, set_str):
    """
    UINT MapVirtualKeyEx(
        UINT uCode,
        [MapVirtualKeyType] uMapType,
        HKL dwhkl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uCode", "uMapType", "dwhkl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MapVirtualKeyExA(jitter):
    user32_MapVirtualKeyEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_MapVirtualKeyExW(jitter):
    user32_MapVirtualKeyEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_OemKeyScan(jitter):
    """
    DWORD OemKeyScan(
        WORD wOemChar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wOemChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterHotKey(jitter):
    """
    BOOL RegisterHotKey(
        HWND hWnd,
        int id,
        UINT fsModifiers,
        UINT vk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "id", "fsModifiers", "vk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SendInput(jitter):
    """
    UINT SendInput(
        UINT nInputs,
        LPINPUT pInputs,
        int cbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nInputs", "pInputs", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetActiveWindow(jitter):
    """
    HWND SetActiveWindow(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetFocus(jitter):
    """
    HWND SetFocus(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetKeyboardState(jitter):
    """
    BOOL SetKeyboardState(
        LPBYTE lpKeyState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpKeyState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ToAscii(jitter):
    """
    int ToAscii(
        UINT uVirtKey,
        UINT uScanCode,
        PBYTE lpKeyState,
        LPWORD lpChar,
        UINT uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uVirtKey", "uScanCode", "lpKeyState", "lpChar", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ToAsciiEx(jitter):
    """
    int ToAsciiEx(
        UINT uVirtKey,
        UINT uScanCode,
        PBYTE lpKeyState,
        LPWORD lpChar,
        UINT uFlags,
        HKL dwhkl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uVirtKey", "uScanCode", "lpKeyState", "lpChar", "uFlags", "dwhkl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ToUnicode(jitter):
    """
    int ToUnicode(
        UINT wVirtKey,
        UINT wScanCode,
        const PBYTE lpKeyState,
        LPWSTR pwszBuff,
        int cchBuff,
        UINT wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wVirtKey", "wScanCode", "lpKeyState", "pwszBuff", "cchBuff", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ToUnicodeEx(jitter):
    """
    int ToUnicodeEx(
        UINT wVirtKey,
        UINT wScanCode,
        const PBYTE lpKeyState,
        LPWSTR pwszBuff,
        int cchBuff,
        UINT wFlags,
        HKL dwhkl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wVirtKey", "wScanCode", "lpKeyState", "pwszBuff", "cchBuff", "wFlags", "dwhkl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnloadKeyboardLayout(jitter):
    """
    BOOL UnloadKeyboardLayout(
        HKL hkl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnregisterHotKey(jitter):
    """
    BOOL UnregisterHotKey(
        HWND hWnd,
        int id
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_VkKeyScan(jitter, get_str, set_str):
    """
    SHORT VkKeyScan(
        TCHAR ch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_VkKeyScanA(jitter):
    user32_VkKeyScan(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_VkKeyScanW(jitter):
    user32_VkKeyScan(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_VkKeyScanEx(jitter, get_str, set_str):
    """
    SHORT VkKeyScanEx(
        TCHAR ch,
        HKL dwhkl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ch", "dwhkl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_VkKeyScanExA(jitter):
    user32_VkKeyScanEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_VkKeyScanExW(jitter):
    user32_VkKeyScanEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DlgDirList(jitter, get_str, set_str):
    """
    int DlgDirList(
        HWND hDlg,
        LPTSTR lpPathSpec,
        int nIDListBox,
        int nIDStaticPath,
        UINT uFileType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "lpPathSpec", "nIDListBox", "nIDStaticPath", "uFileType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DlgDirListA(jitter):
    user32_DlgDirList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DlgDirListW(jitter):
    user32_DlgDirList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DlgDirSelectEx(jitter, get_str, set_str):
    """
    BOOL DlgDirSelectEx(
        HWND hDlg,
        LPTSTR lpString,
        int nCount,
        int nIDListBox
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "lpString", "nCount", "nIDListBox"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DlgDirSelectExA(jitter):
    user32_DlgDirSelectEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DlgDirSelectExW(jitter):
    user32_DlgDirSelectEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetListBoxInfo(jitter):
    """
    DWORD GetListBoxInfo(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AppendMenu(jitter, get_str, set_str):
    """
    BOOL AppendMenu(
        HMENU hMenu,
        UINT uFlags,
        UINT_PTR uIDNewItem,
        LPCTSTR lpNewItem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uFlags", "uIDNewItem", "lpNewItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AppendMenuA(jitter):
    user32_AppendMenu(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_AppendMenuW(jitter):
    user32_AppendMenu(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CheckMenuItem(jitter):
    """
    DWORD CheckMenuItem(
        HMENU hmenu,
        UINT uIDCheckItem,
        [CheckMenuItemFlag] uCheck
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "uIDCheckItem", "uCheck"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CheckMenuRadioItem(jitter):
    """
    BOOL CheckMenuRadioItem(
        HMENU hmenu,
        UINT idFirst,
        UINT idLast,
        UINT idCheck,
        [MenuCommandPosFlag] uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "idFirst", "idLast", "idCheck", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateMenu(jitter):
    """
    HMENU CreateMenu()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreatePopupMenu(jitter):
    """
    HMENU CreatePopupMenu()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DeleteMenu(jitter):
    """
    BOOL DeleteMenu(
        HMENU hMenu,
        UINT uPosition,
        [MenuCommandPosFlag] uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uPosition", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DestroyMenu(jitter):
    """
    BOOL DestroyMenu(
        HMENU hMenu
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawMenuBar(jitter):
    """
    BOOL DrawMenuBar(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnableMenuItem(jitter):
    """
    [EnableMenuItemResult] EnableMenuItem(
        HMENU hMenu,
        UINT uIDEnableItem,
        [EnableMenuItemFlag] uEnable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uIDEnableItem", "uEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EndMenu(jitter):
    """
    BOOL EndMenu()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenu(jitter):
    """
    HMENU GetMenu(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuBarInfo(jitter):
    """
    BOOL GetMenuBarInfo(
        HWND hwnd,
        [ObjectIdEnum] idObject,
        LONG idItem,
        PMENUBARINFO pmbi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "idObject", "idItem", "pmbi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuCheckMarkDimensions(jitter):
    """
    LONG GetMenuCheckMarkDimensions()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuDefaultItem(jitter):
    """
    UINT GetMenuDefaultItem(
        HMENU hMenu,
        UINT fByPos,
        [GetMenuDefaultItemFlags] gmdiFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "fByPos", "gmdiFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuInfo(jitter):
    """
    BOOL GetMenuInfo(
        HMENU hmenu,
        LPCMENUINFO lpcmi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "lpcmi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuItemCount(jitter):
    """
    int GetMenuItemCount(
        HMENU hMenu
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuItemID(jitter):
    """
    UINT GetMenuItemID(
        HMENU hMenu,
        int nPos
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "nPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuItemInfo(jitter, get_str, set_str):
    """
    BOOL GetMenuItemInfo(
        HMENU hMenu,
        UINT uItem,
        BOOL fByPosition,
        LPMENUITEMINFO lpmii
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uItem", "fByPosition", "lpmii"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuItemInfoA(jitter):
    user32_GetMenuItemInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetMenuItemInfoW(jitter):
    user32_GetMenuItemInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetMenuItemRect(jitter):
    """
    BOOL GetMenuItemRect(
        HWND hWnd,
        HMENU hMenu,
        UINT uItem,
        LPRECT lprcItem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hMenu", "uItem", "lprcItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuState(jitter):
    """
    UINT GetMenuState(
        HMENU hMenu,
        UINT uId,
        [MenuCommandPosFlag] uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uId", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuString(jitter, get_str, set_str):
    """
    int GetMenuString(
        HMENU hMenu,
        UINT uIDItem,
        LPTSTR lpString,
        int nMaxCount,
        UINT uFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uIDItem", "lpString", "nMaxCount", "uFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuStringA(jitter):
    user32_GetMenuString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetMenuStringW(jitter):
    user32_GetMenuString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetSubMenu(jitter):
    """
    HMENU GetSubMenu(
        HMENU hMenu,
        int nPos
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "nPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetSystemMenu(jitter):
    """
    HMENU GetSystemMenu(
        HWND hWnd,
        BOOL bRevert
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "bRevert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_HiliteMenuItem(jitter):
    """
    BOOL HiliteMenuItem(
        HWND hwnd,
        HMENU hmenu,
        UINT uItemHilite,
        UINT uHilite
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hmenu", "uItemHilite", "uHilite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InsertMenu(jitter, get_str, set_str):
    """
    BOOL InsertMenu(
        HMENU hMenu,
        UINT uPosition,
        [InsertMenuFlags] uFlags,
        UINT_PTR uIDNewItem,
        LPCTSTR lpNewItem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uPosition", "uFlags", "uIDNewItem", "lpNewItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InsertMenuA(jitter):
    user32_InsertMenu(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_InsertMenuW(jitter):
    user32_InsertMenu(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_InsertMenuItem(jitter, get_str, set_str):
    """
    BOOL InsertMenuItem(
        HMENU hMenu,
        UINT uItem,
        BOOL fByPosition,
        LPCMENUITEMINFO lpmii
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uItem", "fByPosition", "lpmii"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InsertMenuItemA(jitter):
    user32_InsertMenuItem(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_InsertMenuItemW(jitter):
    user32_InsertMenuItem(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_IsMenu(jitter):
    """
    BOOL IsMenu(
        HMENU hMenu
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadMenu(jitter, get_str, set_str):
    """
    HMENU LoadMenu(
        HINSTANCE hInstance,
        LPCTSTR lpMenuName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpMenuName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadMenuA(jitter):
    user32_LoadMenu(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_LoadMenuW(jitter):
    user32_LoadMenu(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_LoadMenuIndirect(jitter, get_str, set_str):
    """
    HMENU LoadMenuIndirect(
        CONST MENUTEMPLATE* lpMenuTemplate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpMenuTemplate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadMenuIndirectA(jitter):
    user32_LoadMenuIndirect(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_LoadMenuIndirectW(jitter):
    user32_LoadMenuIndirect(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_MenuItemFromPoint(jitter):
    """
    int MenuItemFromPoint(
        HWND hWnd,
        HMENU hMenu,
        POINT ptScreen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hMenu", "ptScreen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ModifyMenu(jitter, get_str, set_str):
    """
    BOOL ModifyMenu(
        HMENU hMnu,
        UINT uPosition,
        UINT uFlags,
        UINT_PTR uIDNewItem,
        LPCTSTR lpNewItem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMnu", "uPosition", "uFlags", "uIDNewItem", "lpNewItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ModifyMenuA(jitter):
    user32_ModifyMenu(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_ModifyMenuW(jitter):
    user32_ModifyMenu(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_RemoveMenu(jitter):
    """
    BOOL RemoveMenu(
        HMENU hMenu,
        UINT uPosition,
        [MenuCommandPosFlag] uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uPosition", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMenu(jitter):
    """
    BOOL SetMenu(
        HWND hWnd,
        HMENU hMenu
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMenuDefaultItem(jitter):
    """
    BOOL SetMenuDefaultItem(
        HMENU hMenu,
        UINT uItem,
        UINT fByPos
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uItem", "fByPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMenuInfo(jitter):
    """
    BOOL SetMenuInfo(
        HMENU hmenu,
        LPCMENUINFO lpcmi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "lpcmi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMenuItemBitmaps(jitter):
    """
    BOOL SetMenuItemBitmaps(
        HMENU hMenu,
        UINT uPosition,
        UINT uFlags,
        HBITMAP hBitmapUnchecked,
        HBITMAP hBitmapChecked
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uPosition", "uFlags", "hBitmapUnchecked", "hBitmapChecked"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMenuItemInfo(jitter, get_str, set_str):
    """
    BOOL SetMenuItemInfo(
        HMENU hMenu,
        UINT uItem,
        BOOL fByPosition,
        LPMENUITEMINFO lpmii
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uItem", "fByPosition", "lpmii"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMenuItemInfoA(jitter):
    user32_SetMenuItemInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SetMenuItemInfoW(jitter):
    user32_SetMenuItemInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_TrackPopupMenu(jitter):
    """
    BOOL TrackPopupMenu(
        HMENU hMenu,
        [TrackPopupMenuFlags] uFlags,
        int x,
        int y,
        int nReserved,
        HWND hWnd,
        CONST RECT* prcRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uFlags", "x", "y", "nReserved", "hWnd", "prcRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TrackPopupMenuEx(jitter):
    """
    BOOL TrackPopupMenuEx(
        HMENU hmenu,
        [TrackPopupMenuFlags] fuFlags,
        int x,
        int y,
        HWND hwnd,
        LPTPMPARAMS lptpm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "fuFlags", "x", "y", "hwnd", "lptpm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DragDetect(jitter):
    """
    BOOL DragDetect(
        HWND hwnd,
        POINT pt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCapture(jitter):
    """
    HWND GetCapture()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDoubleClickTime(jitter):
    """
    UINT GetDoubleClickTime()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMouseMovePointsEx(jitter):
    """
    int GetMouseMovePointsEx(
        UINT cbSize,
        LPMOUSEMOVEPOINT lppt,
        LPMOUSEMOVEPOINT lpptBuf,
        int nBufPoints,
        DWORD resolution
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cbSize", "lppt", "lpptBuf", "nBufPoints", "resolution"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_mouse_event(jitter):
    """
    VOID mouse_event(
        DWORD dwFlags,
        DWORD dx,
        DWORD dy,
        DWORD dwData,
        ULONG_PTR dwExtraInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "dx", "dy", "dwData", "dwExtraInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ReleaseCapture(jitter):
    """
    BOOL ReleaseCapture()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetCapture(jitter):
    """
    HWND SetCapture(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetDoubleClickTime(jitter):
    """
    BOOL SetDoubleClickTime(
        UINT uInterval
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uInterval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SwapMouseButton(jitter):
    """
    BOOL SwapMouseButton(
        BOOL fSwap
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fSwap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TrackMouseEvent(jitter):
    """
    BOOL TrackMouseEvent(
        LPTRACKMOUSEEVENT lpEventTrack
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpEventTrack"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumDisplayMonitors(jitter):
    """
    BOOL EnumDisplayMonitors(
        HDC hdc,
        LPCRECT lprcClip,
        MONITORENUMPROC lpfnEnum,
        LPARAM dwData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lprcClip", "lpfnEnum", "dwData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMonitorInfo(jitter, get_str, set_str):
    """
    BOOL GetMonitorInfo(
        HMONITOR hMonitor,
        LPMONITORINFO lpmi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "lpmi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMonitorInfoA(jitter):
    user32_GetMonitorInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetMonitorInfoW(jitter):
    user32_GetMonitorInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_MonitorFromPoint(jitter):
    """
    HMONITOR MonitorFromPoint(
        POINT pt,
        [MonitorFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pt", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MonitorFromRect(jitter):
    """
    HMONITOR MonitorFromRect(
        LPCRECT lprc,
        [MonitorFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprc", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MonitorFromWindow(jitter):
    """
    HMONITOR MonitorFromWindow(
        HWND hwnd,
        [MonitorFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateMDIWindow(jitter, get_str, set_str):
    """
    HWND CreateMDIWindow(
        LPCTSTR lpClassName,
        LPCTSTR lpWindowName,
        DWORD dwStyle,
        int X,
        int Y,
        int nWidth,
        int nHeight,
        HWND hWndParent,
        HINSTANCE hInstance,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpClassName", "lpWindowName", "dwStyle", "X", "Y", "nWidth", "nHeight", "hWndParent", "hInstance", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateMDIWindowA(jitter):
    user32_CreateMDIWindow(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CreateMDIWindowW(jitter):
    user32_CreateMDIWindow(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DefFrameProc(jitter, get_str, set_str):
    """
    LRESULT DefFrameProc(
        HWND hWnd,
        HWND hWndMDIClient,
        UINT uMsg,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hWndMDIClient", "uMsg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DefFrameProcA(jitter):
    user32_DefFrameProc(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DefFrameProcW(jitter):
    user32_DefFrameProc(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DefMDIChildProc(jitter, get_str, set_str):
    """
    LRESULT DefMDIChildProc(
        HWND hWnd,
        UINT uMsg,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "uMsg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DefMDIChildProcA(jitter):
    user32_DefMDIChildProc(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DefMDIChildProcW(jitter):
    user32_DefMDIChildProc(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_TranslateMDISysAccel(jitter):
    """
    BOOL TranslateMDISysAccel(
        HWND hWndClient,
        LPMSG lpMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndClient", "lpMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BeginPaint(jitter):
    """
    HDC BeginPaint(
        HWND hwnd,
        LPPAINTSTRUCT lpPaint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpPaint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawAnimatedRects(jitter):
    """
    BOOL DrawAnimatedRects(
        HWND hwnd,
        int idAni,
        const RECT* lprcFrom,
        const RECT* lprcTo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "idAni", "lprcFrom", "lprcTo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawCaption(jitter):
    """
    BOOL DrawCaption(
        HWND hwnd,
        HDC hdc,
        LPCRECT lprc,
        UINT uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdc", "lprc", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawEdge(jitter):
    """
    BOOL DrawEdge(
        HDC hdc,
        LPRECT qrc,
        [BorderEdge] edge,
        [BorderFlag] grfFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "qrc", "edge", "grfFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawFocusRect(jitter):
    """
    BOOL DrawFocusRect(
        HDC hDC,
        const RECT* lprc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawFrameControl(jitter):
    """
    BOOL DrawFrameControl(
        HDC hdc,
        LPRECT lprc,
        UINT uType,
        UINT uState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lprc", "uType", "uState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawState(jitter, get_str, set_str):
    """
    BOOL DrawState(
        HDC hdc,
        HBRUSH hbr,
        DRAWSTATEPROC lpOutputFunc,
        LPARAM lData,
        WPARAM wData,
        int x,
        int y,
        int cx,
        int cy,
        [DrawStateFlags] fuFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hbr", "lpOutputFunc", "lData", "wData", "x", "y", "cx", "cy", "fuFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawStateA(jitter):
    user32_DrawState(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DrawStateW(jitter):
    user32_DrawState(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_EndPaint(jitter):
    """
    BOOL EndPaint(
        HWND hWnd,
        const PAINTSTRUCT* lpPaint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpPaint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ExcludeUpdateRgn(jitter):
    """
    [WindowRegion] ExcludeUpdateRgn(
        HDC hDC,
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetUpdateRect(jitter):
    """
    BOOL GetUpdateRect(
        HWND hWnd,
        LPRECT lpRect,
        BOOL bErase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpRect", "bErase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetUpdateRgn(jitter):
    """
    [WindowRegion] GetUpdateRgn(
        HWND hWnd,
        HRGN hRgn,
        BOOL bErase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hRgn", "bErase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowDC(jitter):
    """
    HDC GetWindowDC(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowRgn(jitter):
    """
    [WindowRegion] GetWindowRgn(
        HWND hWnd,
        HRGN hRgn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hRgn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowRgnBox(jitter):
    """
    [WindowRegion] GetWindowRgnBox(
        HWND hWnd,
        LPRECT lprc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GrayString(jitter, get_str, set_str):
    """
    BOOL GrayString(
        HDC hDC,
        HBRUSH hBrush,
        GRAYSTRINGPROC lpOutputFunc,
        LPARAM lpData,
        int nCount,
        int X,
        int Y,
        int nWidth,
        int nHeight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "hBrush", "lpOutputFunc", "lpData", "nCount", "X", "Y", "nWidth", "nHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GrayStringA(jitter):
    user32_GrayString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GrayStringW(jitter):
    user32_GrayString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_InvalidateRect(jitter):
    """
    BOOL InvalidateRect(
        HWND hWnd,
        const RECT* lpRect,
        BOOL bErase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpRect", "bErase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InvalidateRgn(jitter):
    """
    BOOL InvalidateRgn(
        HWND hWnd,
        HRGN hRgn,
        BOOL bErase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hRgn", "bErase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LockWindowUpdate(jitter):
    """
    BOOL LockWindowUpdate(
        HWND hWndLock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PaintDesktop(jitter):
    """
    BOOL PaintDesktop(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RedrawWindow(jitter):
    """
    BOOL RedrawWindow(
        HWND hWnd,
        const RECT* lprcUpdate,
        HRGN hrgnUpdate,
        [RedrawWindowFlags] flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lprcUpdate", "hrgnUpdate", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowRgn(jitter):
    """
    int SetWindowRgn(
        HWND hWnd,
        HRGN hRgn,
        BOOL bRedraw
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hRgn", "bRedraw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UpdateWindow(jitter):
    """
    BOOL UpdateWindow(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ValidateRect(jitter):
    """
    BOOL ValidateRect(
        HWND hWnd,
        const RECT* lpRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ValidateRgn(jitter):
    """
    BOOL ValidateRgn(
        HWND hWnd,
        HRGN hRgn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hRgn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_WindowFromDC(jitter):
    """
    HWND WindowFromDC(
        HDC hDC
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterPowerSettingNotification(jitter):
    """
    HPOWERNOTIFY RegisterPowerSettingNotification(
        HANDLE hRecipient,
        LPCGUID PowerSettingGuid,
        [DeviceNotificationFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRecipient", "PowerSettingGuid", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnregisterPowerSettingNotification(jitter):
    """
    BOOL UnregisterPowerSettingNotification(
        HPOWERNOTIFY Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PrintWindow(jitter):
    """
    BOOL PrintWindow(
        HWND hwnd,
        HDC hdcBlt,
        UINT nFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdcBlt", "nFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DefRawInputProc(jitter):
    """
    LRESULT DefRawInputProc(
        PRAWINPUT* paRawInput,
        INT nInput,
        UINT cbSizeHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["paRawInput", "nInput", "cbSizeHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetRawInputBuffer(jitter):
    """
    UINT GetRawInputBuffer(
        PRAWINPUT pData,
        PUINT pcbSize,
        UINT cbSizeHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pData", "pcbSize", "cbSizeHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetRawInputData(jitter):
    """
    UINT GetRawInputData(
        HRAWINPUT hRawInput,
        UINT uiCommand,
        LPVOID pData,
        PUINT pcbSize,
        UINT cbSizeHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRawInput", "uiCommand", "pData", "pcbSize", "cbSizeHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetRawInputDeviceInfo(jitter, get_str, set_str):
    """
    UINT GetRawInputDeviceInfo(
        HANDLE hDevice,
        UINT uiCommand,
        LPVOID pData,
        PUINT pcbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDevice", "uiCommand", "pData", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetRawInputDeviceInfoA(jitter):
    user32_GetRawInputDeviceInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetRawInputDeviceInfoW(jitter):
    user32_GetRawInputDeviceInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetRawInputDeviceList(jitter):
    """
    UINT GetRawInputDeviceList(
        PRAWINPUTDEVICELIST pRawInputDeviceList,
        PUINT puiNumDevices,
        UINT cbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRawInputDeviceList", "puiNumDevices", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetRegisteredRawInputDevices(jitter):
    """
    UINT GetRegisteredRawInputDevices(
        PRAWINPUTDEVICE pRawInputDevices,
        PUINT puiNumDevices,
        UINT cbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRawInputDevices", "puiNumDevices", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterRawInputDevices(jitter):
    """
    BOOL RegisterRawInputDevices(
        PCRAWINPUTDEVICE pRawInputDevices,
        UINT uiNumDevices,
        UINT cbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRawInputDevices", "uiNumDevices", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CopyRect(jitter):
    """
    BOOL CopyRect(
        LPRECT lprcDst,
        const RECT* lprcSrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprcDst", "lprcSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EqualRect(jitter):
    """
    BOOL EqualRect(
        const RECT* lprc1,
        const RECT* lprc2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprc1", "lprc2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InflateRect(jitter):
    """
    BOOL InflateRect(
        LPRECT lprc,
        int dx,
        int dy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprc", "dx", "dy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IntersectRect(jitter):
    """
    BOOL IntersectRect(
        LPRECT lprcDst,
        const RECT* lprcSrc1,
        const RECT* lprcSrc2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprcDst", "lprcSrc1", "lprcSrc2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsRectEmpty(jitter):
    """
    BOOL IsRectEmpty(
        const RECT* lprc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OffsetRect(jitter):
    """
    BOOL OffsetRect(
        LPRECT lprc,
        int dx,
        int dy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprc", "dx", "dy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PtInRect(jitter):
    """
    BOOL PtInRect(
        const RECT* lprc,
        POINT pt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprc", "pt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetRect(jitter):
    """
    BOOL SetRect(
        LPRECT lprc,
        int xLeft,
        int yTop,
        int xRight,
        int yBottom
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprc", "xLeft", "yTop", "xRight", "yBottom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetRectEmpty(jitter):
    """
    BOOL SetRectEmpty(
        LPRECT lprc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SubtractRect(jitter):
    """
    BOOL SubtractRect(
        LPRECT lprcDst,
        const RECT* lprcSrc1,
        const RECT* lprcSrc2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprcDst", "lprcSrc1", "lprcSrc2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnionRect(jitter):
    """
    BOOL UnionRect(
        LPRECT lprcDst,
        const RECT* lprcSrc1,
        const RECT* lprcSrc2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprcDst", "lprcSrc1", "lprcSrc2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CopyImage(jitter):
    """
    HANDLE CopyImage(
        HANDLE hImage,
        [ImageType] uType,
        int cxDesired,
        int cyDesired,
        [LRFlags] fuFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hImage", "uType", "cxDesired", "cyDesired", "fuFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadImage(jitter, get_str, set_str):
    """
    HANDLE LoadImage(
        HINSTANCE hinst,
        [LoadImageString/LPCTSTR] lpszName,
        [ImageType] uType,
        int cxDesired,
        int cyDesired,
        [LRFlags] fuLoad
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hinst", "lpszName", "uType", "cxDesired", "cyDesired", "fuLoad"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadImageA(jitter):
    user32_LoadImage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_LoadImageW(jitter):
    user32_LoadImage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_EnableScrollBar(jitter):
    """
    BOOL EnableScrollBar(
        HWND hWnd,
        UINT wSBflags,
        UINT wArrows
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "wSBflags", "wArrows"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetScrollBarInfo(jitter):
    """
    BOOL GetScrollBarInfo(
        HWND hwnd,
        [ObjectIdEnum] idObject,
        PSCROLLBARINFO psbi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "idObject", "psbi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetScrollInfo(jitter):
    """
    BOOL GetScrollInfo(
        HWND hwnd,
        [SBType] fnBar,
        LPSCROLLINFO lpsi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "fnBar", "lpsi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetScrollPos(jitter):
    """
    int GetScrollPos(
        HWND hWnd,
        [SBType] nBar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nBar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetScrollRange(jitter):
    """
    BOOL GetScrollRange(
        HWND hWnd,
        [SBType] nBar,
        LPINT lpMinPos,
        LPINT lpMaxPos
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nBar", "lpMinPos", "lpMaxPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ScrollDC(jitter):
    """
    BOOL ScrollDC(
        HDC hDC,
        int dx,
        int dy,
        const RECT* lprcScroll,
        const RECT* lprcClip,
        HRGN hrgnUpdate,
        LPRECT lprcUpdate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "dx", "dy", "lprcScroll", "lprcClip", "hrgnUpdate", "lprcUpdate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ScrollWindow(jitter):
    """
    BOOL ScrollWindow(
        HWND hWnd,
        int XAmount,
        int YAmount,
        const RECT* lpRect,
        const RECT* lpClipRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "XAmount", "YAmount", "lpRect", "lpClipRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ScrollWindowEx(jitter):
    """
    int ScrollWindowEx(
        HWND hWnd,
        int dx,
        int dy,
        const RECT* prcScroll,
        const RECT* prcClip,
        HRGN hrgnUpdate,
        LPRECT prcUpdate,
        [ScrollWindowFlags] flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "dx", "dy", "prcScroll", "prcClip", "hrgnUpdate", "prcUpdate", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetScrollInfo(jitter):
    """
    int SetScrollInfo(
        HWND hwnd,
        [SBType] fnBar,
        LPCSCROLLINFO lpsi,
        BOOL fRedraw
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "fnBar", "lpsi", "fRedraw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetScrollPos(jitter):
    """
    int SetScrollPos(
        HWND hWnd,
        [SBType] nBar,
        int nPos,
        BOOL bRedraw
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nBar", "nPos", "bRedraw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetScrollRange(jitter):
    """
    BOOL SetScrollRange(
        HWND hWnd,
        [SBType] nBar,
        int nMinPos,
        int nMaxPos,
        BOOL bRedraw
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nBar", "nMinPos", "nMaxPos", "bRedraw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShowScrollBar(jitter):
    """
    BOOL ShowScrollBar(
        HWND hWnd,
        [SBType] wBar,
        BOOL bShow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "wBar", "bShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharLower(jitter, get_str, set_str):
    """
    LPTSTR CharLower(
        LPTSTR lpsz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharLowerA(jitter):
    user32_CharLower(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CharLowerW(jitter):
    user32_CharLower(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CharLowerBuff(jitter, get_str, set_str):
    """
    DWORD CharLowerBuff(
        LPTSTR lpsz,
        DWORD cchLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpsz", "cchLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharLowerBuffA(jitter):
    user32_CharLowerBuff(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CharLowerBuffW(jitter):
    user32_CharLowerBuff(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CharNext(jitter, get_str, set_str):
    """
    LPTSTR CharNext(
        LPCTSTR lpsz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharNextA(jitter):
    user32_CharNext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CharNextW(jitter):
    user32_CharNext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CharNextExA(jitter):
    """
    LPSTR CharNextExA(
        [CodePageEnum] CodePage,
        LPCSTR lpCurrentChar,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CodePage", "lpCurrentChar", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharPrev(jitter, get_str, set_str):
    """
    LPTSTR CharPrev(
        LPCTSTR lpszStart,
        LPCTSTR lpszCurrent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszStart", "lpszCurrent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharPrevA(jitter):
    user32_CharPrev(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CharPrevW(jitter):
    user32_CharPrev(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CharPrevExA(jitter):
    """
    LPSTR CharPrevExA(
        [CodePageEnum] CodePage,
        LPCSTR lpStart,
        LPCSTR lpCurrentChar,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CodePage", "lpStart", "lpCurrentChar", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharToOem(jitter, get_str, set_str):
    """
    BOOL CharToOem(
        LPCTSTR lpszSrc,
        LPSTR lpszDst
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszSrc", "lpszDst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharToOemA(jitter):
    user32_CharToOem(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CharToOemW(jitter):
    user32_CharToOem(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CharToOemBuff(jitter, get_str, set_str):
    """
    BOOL CharToOemBuff(
        LPCTSTR lpszSrc,
        LPSTR lpszDst,
        DWORD cchDstLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszSrc", "lpszDst", "cchDstLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharToOemBuffA(jitter):
    user32_CharToOemBuff(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CharToOemBuffW(jitter):
    user32_CharToOemBuff(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CharUpper(jitter, get_str, set_str):
    """
    LPTSTR CharUpper(
        LPTSTR lpsz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharUpperA(jitter):
    user32_CharUpper(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CharUpperW(jitter):
    user32_CharUpper(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CharUpperBuff(jitter, get_str, set_str):
    """
    DWORD CharUpperBuff(
        LPTSTR lpsz,
        DWORD cchLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpsz", "cchLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharUpperBuffA(jitter):
    user32_CharUpperBuff(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CharUpperBuffW(jitter):
    user32_CharUpperBuff(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_IsCharAlpha(jitter, get_str, set_str):
    """
    BOOL IsCharAlpha(
        TCHAR ch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsCharAlphaA(jitter):
    user32_IsCharAlpha(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_IsCharAlphaW(jitter):
    user32_IsCharAlpha(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_IsCharAlphaNumeric(jitter, get_str, set_str):
    """
    BOOL IsCharAlphaNumeric(
        TCHAR ch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsCharAlphaNumericA(jitter):
    user32_IsCharAlphaNumeric(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_IsCharAlphaNumericW(jitter):
    user32_IsCharAlphaNumeric(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_IsCharLower(jitter, get_str, set_str):
    """
    BOOL IsCharLower(
        TCHAR ch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsCharLowerA(jitter):
    user32_IsCharLower(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_IsCharLowerW(jitter):
    user32_IsCharLower(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_IsCharUpper(jitter, get_str, set_str):
    """
    BOOL IsCharUpper(
        TCHAR ch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsCharUpperA(jitter):
    user32_IsCharUpper(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_IsCharUpperW(jitter):
    user32_IsCharUpper(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_LoadString(jitter, get_str, set_str):
    """
    int LoadString(
        HINSTANCE hInstance,
        UINT uID,
        LPTSTR lpBuffer,
        int nBufferMax
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "uID", "lpBuffer", "nBufferMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadStringA(jitter):
    user32_LoadString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_LoadStringW(jitter):
    user32_LoadString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_OemToChar(jitter, get_str, set_str):
    """
    BOOL OemToChar(
        LPCSTR lpszSrc,
        LPTSTR lpszDst
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszSrc", "lpszDst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OemToCharA(jitter):
    user32_OemToChar(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_OemToCharW(jitter):
    user32_OemToChar(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_OemToCharBuff(jitter, get_str, set_str):
    """
    BOOL OemToCharBuff(
        LPCTSTR lpszSrc,
        LPTSTR lpszDst,
        DWORD cchDstLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszSrc", "lpszDst", "cchDstLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OemToCharBuffA(jitter):
    user32_OemToCharBuff(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_OemToCharBuffW(jitter):
    user32_OemToCharBuff(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_wsprintf(jitter, get_str, set_str):
    """
    int wsprintf(
        LPTSTR lpOut,
        LPCTSTR lpFmt,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpOut", "lpFmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_wsprintfA(jitter):
    user32_wsprintf(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_wsprintfW(jitter):
    user32_wsprintf(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_wvsprintf(jitter, get_str, set_str):
    """
    int wvsprintf(
        LPTSTR lpOutput,
        LPCTSTR lpFmt,
        va_list arglist
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpOutput", "lpFmt", "arglist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_wvsprintfA(jitter):
    user32_wvsprintf(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_wvsprintfW(jitter):
    user32_wvsprintf(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_MsgWaitForMultipleObjects(jitter):
    """
    [WAIT_RESULT] MsgWaitForMultipleObjects(
        DWORD nCount,
        const HANDLE* pHandles,
        BOOL bWaitAll,
        [WaitTimeout] dwMilliseconds,
        [QueueStatusFlag] dwWakeMask
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nCount", "pHandles", "bWaitAll", "dwMilliseconds", "dwWakeMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MsgWaitForMultipleObjectsEx(jitter):
    """
    [WAIT_RESULT] MsgWaitForMultipleObjectsEx(
        DWORD nCount,
        const HANDLE* pHandles,
        [WaitTimeout] dwMilliseconds,
        [QueueStatusFlag] dwWakeMask,
        [MsgWaitForMultipleObjectsFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nCount", "pHandles", "dwMilliseconds", "dwWakeMask", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyboardType(jitter):
    """
    int GetKeyboardType(
        int nTypeFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nTypeFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetSysColor(jitter):
    """
    DWORD GetSysColor(
        [SysColorIndex] nIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetSystemMetrics(jitter):
    """
    int GetSystemMetrics(
        [SystemMetricIndex] nIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetSysColors(jitter):
    """
    BOOL SetSysColors(
        int cElements,
        const INT* lpaElements,
        const COLORREF* lpaRgbValues
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cElements", "lpaElements", "lpaRgbValues"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SystemParametersInfo(jitter, get_str, set_str):
    """
    BOOL SystemParametersInfo(
        [SystemParametersInfoEnum] uiAction,
        UINT uiParam,
        PVOID pvParam,
        [SystemParametersInfoFlags] fWinIni
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiAction", "uiParam", "pvParam", "fWinIni"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SystemParametersInfoA(jitter):
    user32_SystemParametersInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SystemParametersInfoW(jitter):
    user32_SystemParametersInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_KillTimer(jitter):
    """
    BOOL KillTimer(
        HWND hWnd,
        UINT_PTR uIDEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "uIDEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetCoalescableTimer(jitter):
    """
    UINT_PTR SetCoalescableTimer(
        HWND hwnd,
        UINT_PTR nIDEvent,
        UINT uElapse,
        TIMERPROC lpTimerFunc,
        [TIMERV_COALESCING] uToleranceDelay
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "nIDEvent", "uElapse", "lpTimerFunc", "uToleranceDelay"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetTimer(jitter):
    """
    UINT_PTR SetTimer(
        HWND hWnd,
        UINT_PTR nIDEvent,
        UINT uElapse,
        TIMERPROC lpTimerFunc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIDEvent", "uElapse", "lpTimerFunc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClassInfo(jitter, get_str, set_str):
    """
    BOOL GetClassInfo(
        HINSTANCE hInstance,
        LPCTSTR lpClassName,
        LPWNDCLASS lpWndClass
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpClassName", "lpWndClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClassInfoA(jitter):
    user32_GetClassInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetClassInfoW(jitter):
    user32_GetClassInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetClassInfoEx(jitter, get_str, set_str):
    """
    BOOL GetClassInfoEx(
        HINSTANCE hinst,
        LPCTSTR lpszClass,
        LPWNDCLASSEX lpwcx
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hinst", "lpszClass", "lpwcx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClassInfoExA(jitter):
    user32_GetClassInfoEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetClassInfoExW(jitter):
    user32_GetClassInfoEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetClassLong(jitter, get_str, set_str):
    """
    DWORD GetClassLong(
        HWND hWnd,
        [ClassLongIndex] nIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClassLongA(jitter):
    user32_GetClassLong(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetClassLongW(jitter):
    user32_GetClassLong(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetClassName(jitter, get_str, set_str):
    """
    int GetClassName(
        HWND hWnd,
        LPTSTR lpClassName,
        int nMaxCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpClassName", "nMaxCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClassNameA(jitter):
    user32_GetClassName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetClassNameW(jitter):
    user32_GetClassName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetClassWord(jitter):
    """
    WORD GetClassWord(
        HWND hWnd,
        [ClassLongIndex] nIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowLong(jitter, get_str, set_str):
    """
    LONG GetWindowLong(
        HWND hWnd,
        [WindowLongIndex] nIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowLongA(jitter):
    user32_GetWindowLong(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetWindowLongW(jitter):
    user32_GetWindowLong(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_RegisterClass(jitter, get_str, set_str):
    """
    ATOM RegisterClass(
        CONST WNDCLASS* lpWndClass
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpWndClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterClassA(jitter):
    user32_RegisterClass(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_RegisterClassW(jitter):
    user32_RegisterClass(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_RegisterClassEx(jitter, get_str, set_str):
    """
    ATOM RegisterClassEx(
        CONST WNDCLASSEX* lpwcx
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwcx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterClassExA(jitter):
    user32_RegisterClassEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_RegisterClassExW(jitter):
    user32_RegisterClassEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_SetClassLong(jitter, get_str, set_str):
    """
    DWORD SetClassLong(
        HWND hWnd,
        [ClassLongIndex] nIndex,
        LONG dwNewLong
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIndex", "dwNewLong"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetClassLongA(jitter):
    user32_SetClassLong(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SetClassLongW(jitter):
    user32_SetClassLong(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_SetClassWord(jitter):
    """
    WORD SetClassWord(
        HWND hWnd,
        [ClassLongIndex] nIndex,
        WORD wNewWord
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIndex", "wNewWord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowLong(jitter, get_str, set_str):
    """
    LONG SetWindowLong(
        HWND hWnd,
        [WindowLongIndex] nIndex,
        LONG dwNewLong
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIndex", "dwNewLong"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowLongA(jitter):
    user32_SetWindowLong(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SetWindowLongW(jitter):
    user32_SetWindowLong(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_UnregisterClass(jitter, get_str, set_str):
    """
    BOOL UnregisterClass(
        LPCTSTR lpClassName,
        HINSTANCE hInstance
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpClassName", "hInstance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnregisterClassA(jitter):
    user32_UnregisterClass(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_UnregisterClassW(jitter):
    user32_UnregisterClass(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CallWindowProc(jitter, get_str, set_str):
    """
    LRESULT CallWindowProc(
        WNDPROC lpPrevWndFunc,
        HWND hWnd,
        [WinMsg] Msg,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpPrevWndFunc", "hWnd", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CallWindowProcA(jitter):
    user32_CallWindowProc(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CallWindowProcW(jitter):
    user32_CallWindowProc(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_DefWindowProc(jitter, get_str, set_str):
    """
    LRESULT DefWindowProc(
        HWND hWnd,
        [WinMsg] Msg,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DefWindowProcA(jitter):
    user32_DefWindowProc(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_DefWindowProcW(jitter):
    user32_DefWindowProc(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_EnumProps(jitter, get_str, set_str):
    """
    int EnumProps(
        HWND hWnd,
        PROPENUMPROC lpEnumFunc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpEnumFunc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumPropsA(jitter):
    user32_EnumProps(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_EnumPropsW(jitter):
    user32_EnumProps(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_EnumPropsEx(jitter, get_str, set_str):
    """
    int EnumPropsEx(
        HWND hWnd,
        PROPENUMPROCEX lpEnumFunc,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpEnumFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumPropsExA(jitter):
    user32_EnumPropsEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_EnumPropsExW(jitter):
    user32_EnumPropsEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetProp(jitter, get_str, set_str):
    """
    HANDLE GetProp(
        HWND hWnd,
        LPCTSTR lpString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPropA(jitter):
    user32_GetProp(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetPropW(jitter):
    user32_GetProp(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_RemoveProp(jitter, get_str, set_str):
    """
    HANDLE RemoveProp(
        HWND hWnd,
        LPCTSTR lpString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RemovePropA(jitter):
    user32_RemoveProp(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_RemovePropW(jitter):
    user32_RemoveProp(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_SetProp(jitter, get_str, set_str):
    """
    BOOL SetProp(
        HWND hWnd,
        LPCTSTR lpString,
        HANDLE hData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpString", "hData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetPropA(jitter):
    user32_SetProp(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SetPropW(jitter):
    user32_SetProp(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CloseWindowStation(jitter):
    """
    BOOL CloseWindowStation(
        HWINSTA hWinSta
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWinSta"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateWindowStation(jitter, get_str, set_str):
    """
    HWINSTA CreateWindowStation(
        LPCTSTR lpwinsta,
        [CreateWindowStationFlags] dwFlags,
        [WindowStationAccessRights] dwDesiredAccess,
        LPSECURITY_ATTRIBUTES lpsa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwinsta", "dwFlags", "dwDesiredAccess", "lpsa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateWindowStationA(jitter):
    user32_CreateWindowStation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CreateWindowStationW(jitter):
    user32_CreateWindowStation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_EnumWindowStations(jitter, get_str, set_str):
    """
    BOOL EnumWindowStations(
        WINSTAENUMPROC lpEnumFunc,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpEnumFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumWindowStationsA(jitter):
    user32_EnumWindowStations(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_EnumWindowStationsW(jitter):
    user32_EnumWindowStations(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetProcessWindowStation(jitter):
    """
    HWINSTA GetProcessWindowStation()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetUserObjectInformation(jitter, get_str, set_str):
    """
    BOOL GetUserObjectInformation(
        HANDLE hObj,
        [UserObjectInformationEnum] nIndex,
        PVOID pvInfo,
        DWORD nLength,
        LPDWORD lpnLengthNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hObj", "nIndex", "pvInfo", "nLength", "lpnLengthNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetUserObjectInformationA(jitter):
    user32_GetUserObjectInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_GetUserObjectInformationW(jitter):
    user32_GetUserObjectInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_OpenWindowStation(jitter, get_str, set_str):
    """
    HWINSTA OpenWindowStation(
        LPTSTR lpszWinSta,
        BOOL fInherit,
        [WindowStationAccessRights] dwDesiredAccess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszWinSta", "fInherit", "dwDesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OpenWindowStationA(jitter):
    user32_OpenWindowStation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_OpenWindowStationW(jitter):
    user32_OpenWindowStation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_SetProcessWindowStation(jitter):
    """
    BOOL SetProcessWindowStation(
        HWINSTA hWinSta
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWinSta"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CloseDesktop(jitter):
    """
    BOOL CloseDesktop(
        HDESK hDesktop
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDesktop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateDesktop(jitter, get_str, set_str):
    """
    HDESK CreateDesktop(
        LPCTSTR lpszDesktop,
        LPCTSTR lpszDevice,
        LPDEVMODE pDevmode,
        [DesktopFlags] dwFlags,
        [DESKTOP_ACCESS_MASK] dwDesiredAccess,
        LPSECURITY_ATTRIBUTES lpsa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDesktop", "lpszDevice", "pDevmode", "dwFlags", "dwDesiredAccess", "lpsa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateDesktopA(jitter):
    user32_CreateDesktop(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CreateDesktopW(jitter):
    user32_CreateDesktop(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_CreateDesktopEx(jitter, get_str, set_str):
    """
    HDESK CreateDesktopEx(
        LPCTSTR lpszDesktop,
        LPCTSTR lpszDevice,
        LPDEVMODE pDevmode,
        [DesktopFlags] dwFlags,
        [DESKTOP_ACCESS_MASK] dwDesiredAccess,
        LPSECURITY_ATTRIBUTES lpsa,
        ULONG ulHeapSize,
        PVOID pvoid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDesktop", "lpszDevice", "pDevmode", "dwFlags", "dwDesiredAccess", "lpsa", "ulHeapSize", "pvoid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateDesktopExA(jitter):
    user32_CreateDesktopEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_CreateDesktopExW(jitter):
    user32_CreateDesktopEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_EnumDesktops(jitter, get_str, set_str):
    """
    BOOL EnumDesktops(
        HWINSTA hwinsta,
        DESKTOPENUMPROC lpEnumFunc,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwinsta", "lpEnumFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumDesktopsA(jitter):
    user32_EnumDesktops(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_EnumDesktopsW(jitter):
    user32_EnumDesktops(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_EnumDesktopWindows(jitter):
    """
    BOOL EnumDesktopWindows(
        HDESK hDesktop,
        WNDENUMPROC lpfn,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDesktop", "lpfn", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetThreadDesktop(jitter):
    """
    HDESK GetThreadDesktop(
        DWORD dwThreadId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwThreadId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OpenDesktop(jitter, get_str, set_str):
    """
    HDESK OpenDesktop(
        LPTSTR lpszDesktop,
        [DesktopFlags] dwFlags,
        BOOL fInherit,
        [DESKTOP_ACCESS_MASK] dwDesiredAccess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDesktop", "dwFlags", "fInherit", "dwDesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OpenDesktopA(jitter):
    user32_OpenDesktop(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_OpenDesktopW(jitter):
    user32_OpenDesktop(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_OpenInputDesktop(jitter):
    """
    HDESK OpenInputDesktop(
        [DesktopFlags] dwFlags,
        BOOL fInherit,
        [DESKTOP_ACCESS_MASK] dwDesiredAccess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "fInherit", "dwDesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetThreadDesktop(jitter):
    """
    BOOL SetThreadDesktop(
        HDESK hDesktop
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDesktop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetUserObjectInformation(jitter, get_str, set_str):
    """
    BOOL SetUserObjectInformation(
        HANDLE hObj,
        [UserObjectInformationEnum] nIndex,
        PVOID pvInfo,
        DWORD nLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hObj", "nIndex", "pvInfo", "nLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetUserObjectInformationA(jitter):
    user32_SetUserObjectInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_SetUserObjectInformationW(jitter):
    user32_SetUserObjectInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_SwitchDesktop(jitter):
    """
    BOOL SwitchDesktop(
        HDESK hDesktop
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDesktop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuContextHelpId(jitter):
    """
    DWORD GetMenuContextHelpId(
        HMENU hmenu
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowContextHelpId(jitter):
    """
    DWORD GetWindowContextHelpId(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMenuContextHelpId(jitter):
    """
    BOOL SetMenuContextHelpId(
        HMENU hmenu,
        DWORD dwContextHelpId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "dwContextHelpId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowContextHelpId(jitter):
    """
    BOOL SetWindowContextHelpId(
        HWND hwnd,
        DWORD dwContextHelpId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwContextHelpId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_WinHelp(jitter, get_str, set_str):
    """
    BOOL WinHelp(
        HWND hWndMain,
        LPCTSTR lpszHelp,
        UINT uCommand,
        ULONG_PTR dwData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndMain", "lpszHelp", "uCommand", "dwData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_WinHelpA(jitter):
    user32_WinHelp(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def user32_WinHelpW(jitter):
    user32_WinHelp(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def user32_GetUserObjectSecurity(jitter):
    """
    BOOL GetUserObjectSecurity(
        HANDLE hObj,
        PSECURITY_INFORMATION pSIRequested,
        PSECURITY_DESCRIPTOR pSD,
        DWORD nLength,
        LPDWORD lpnLengthNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hObj", "pSIRequested", "pSD", "nLength", "lpnLengthNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetUserObjectSecurity(jitter):
    """
    BOOL SetUserObjectSecurity(
        HANDLE hObj,
        PSECURITY_INFORMATION pSIRequested,
        PSECURITY_DESCRIPTOR pSID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hObj", "pSIRequested", "pSID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWinEventHook(jitter):
    """
    HWINEVENTHOOK SetWinEventHook(
        UINT eventMin,
        UINT eventMax,
        HMODULE hmodWinEventProc,
        WINEVENTPROC lpfnWinEventProc,
        DWORD idProcess,
        DWORD idThread,
        [WinEventFlags] dwflags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["eventMin", "eventMax", "hmodWinEventProc", "lpfnWinEventProc", "idProcess", "idThread", "dwflags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnhookWinEvent(jitter):
    """
    BOOL UnhookWinEvent(
        HWINEVENTHOOK hWinEventHook
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWinEventHook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWinEventHookInstalled(jitter):
    """
    BOOL IsWinEventHookInstalled(
        DWORD event
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["event"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_NotifyWinEvent(jitter):
    """
    void NotifyWinEvent(
        DWORD event,
        HWND hwnd,
        [ObjectIdEnum] idObject,
        LONG idChild
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["event", "hwnd", "idObject", "idChild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CloseTouchInputHandle(jitter):
    """
    BOOL CloseTouchInputHandle(
        HTOUCHINPUT hTouchInput
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTouchInput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetTouchInputInfo(jitter):
    """
    BOOL GetTouchInputInfo(
        HTOUCHINPUT hTouchInput,
        UINT cInputs,
        PTOUCHINPUT pInputs,
        int cbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTouchInput", "cInputs", "pInputs", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsTouchWindow(jitter):
    """
    BOOL IsTouchWindow(
        HWND hWnd,
        PULONG pulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterTouchWindow(jitter):
    """
    BOOL RegisterTouchWindow(
        HWND hWnd,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnregisterTouchWindow(jitter):
    """
    BOOL UnregisterTouchWindow(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CloseGestureInfoHandle(jitter):
    """
    BOOL CloseGestureInfoHandle(
        HGESTUREINFO hGestureInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hGestureInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetGestureExtraArgs(jitter):
    """
    BOOL GetGestureExtraArgs(
        HGESTUREINFO hGestureInfo,
        UINT cbExtraArgs,
        PBYTE pExtraArgs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hGestureInfo", "cbExtraArgs", "pExtraArgs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetGestureInfo(jitter):
    """
    BOOL GetGestureInfo(
        HGESTUREINFO hGestureInfo,
        PGESTUREINFO pGestureInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hGestureInfo", "pGestureInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetGestureConfig(jitter):
    """
    BOOL GetGestureConfig(
        HWND hwnd,
        DWORD dwReserved,
        DWORD dwFlags,
        PUINT pcIDs,
        PGESTURECONFIG pGestureConfig,
        UINT cbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwReserved", "dwFlags", "pcIDs", "pGestureConfig", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetGestureConfig(jitter):
    """
    BOOL SetGestureConfig(
        HWND hwnd,
        DWORD dwReserved,
        UINT cIDs,
        PGESTURECONFIG pGestureConfig,
        UINT cbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwReserved", "cIDs", "pGestureConfig", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DesktopHasWatermarkText(jitter):
    """
    BOOL DesktopHasWatermarkText()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FrostCrashedWindow(jitter):
    """
    HWND FrostCrashedWindow(
        HWND hwndToReplace,
        HWND hwndErrorReportOwnerWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndToReplace", "hwndErrorReportOwnerWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetSendMessageReceiver(jitter):
    """
    HWND GetSendMessageReceiver(
        DWORD threadId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["threadId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowCompositionAttribute(jitter):
    """
    BOOL GetWindowCompositionAttribute(
        HWND hwnd,
        WINCOMPATTRDATA* pAttrData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pAttrData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowMinimizeRect(jitter):
    """
    BOOL GetWindowMinimizeRect(
        HWND hwndToQuery,
        RECT* pRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndToQuery", "pRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GhostWindowFromHungWindow(jitter):
    """
    HWND GhostWindowFromHungWindow(
        HWND hwndGhost
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndGhost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_HungWindowFromGhostWindow(jitter):
    """
    HWND HungWindowFromGhostWindow(
        HWND hwndGhost
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndGhost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsSETEnabled(jitter):
    """
    BOOL IsSETEnabled()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsServerSideWindow(jitter):
    """
    BOOL IsServerSideWindow(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsThreadDesktopComposited(jitter):
    """
    BOOL IsThreadDesktopComposited()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWindowInDestroy(jitter):
    """
    BOOL IsWindowInDestroy(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MB_GetString(jitter):
    """
    LPCWSTR MB_GetString(
        int strId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_NtUserSetChildWindowNoActivate(jitter):
    """
    BOOL NtUserSetChildWindowNoActivate(
        HWND hwndChild
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndChild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_QuerySendMessage(jitter):
    """
    BOOL QuerySendMessage(
        MSG* pMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowCompositionAttribute(jitter):
    """
    BOOL SetWindowCompositionAttribute(
        HWND hwnd,
        WINCOMPATTRDATA* pAttrData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pAttrData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UpdateWindowTransform(jitter):
    """
    BOOL UpdateWindowTransform(
        HWND hwnd,
        D3DMATRIX* pMatrix,
        DWORD unk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pMatrix", "unk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InitializeTouchInjection(jitter):
    """
    BOOL InitializeTouchInjection(
        UINT32 maxCount,
        [TOUCH_FEEDBACK_MODE] dwMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["maxCount", "dwMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InjectTouchInput(jitter):
    """
    BOOL InjectTouchInput(
        UINT32 count,
        const POINTER_TOUCH_INFO* contacts
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["count", "contacts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AddPointerInteractionContext(jitter):
    """
    HRESULT AddPointerInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        UINT32 pointerId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "pointerId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BufferPointerPacketsInteractionContext(jitter):
    """
    HRESULT BufferPointerPacketsInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        UINT32 entriesCount,
        const POINTER_INFO* pointerInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "entriesCount", "pointerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateInteractionContext(jitter):
    """
    HRESULT CreateInteractionContext(
        HINTERACTIONCONTEXT* interactionContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DestroyInteractionContext(jitter):
    """
    HRESULT DestroyInteractionContext(
        HINTERACTIONCONTEXT interactionContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCrossSlideParameterInteractionContext(jitter):
    """
    HRESULT GetCrossSlideParameterInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        CROSS_SLIDE_THRESHOLD threshold,
        float* distance
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "threshold", "distance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetInertiaParameterInteractionContext(jitter):
    """
    HRESULT GetInertiaParameterInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        INERTIA_PARAMETER inertiaParameter,
        float* value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "inertiaParameter", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetInteractionConfigurationInteractionContext(jitter):
    """
    HRESULT GetInteractionConfigurationInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        UINT32 configurationCount,
        INTERACTION_CONTEXT_CONFIGURATION* configuration
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "configurationCount", "configuration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMouseWheelParameterInteractionContext(jitter):
    """
    HRESULT GetMouseWheelParameterInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        MOUSE_WHEEL_PARAMETER parameter,
        float* value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "parameter", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPropertyInteractionContext(jitter):
    """
    HRESULT GetPropertyInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        INTERACTION_CONTEXT_PROPERTY contextProperty,
        UINT32* value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "contextProperty", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetStateInteractionContext(jitter):
    """
    HRESULT GetStateInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        const POINTER_INFO* pointerInfo,
        INTERACTION_STATE* state
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "pointerInfo", "state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ProcessBufferedPacketsInteractionContext(jitter):
    """
    HRESULT ProcessBufferedPacketsInteractionContext(
        HINTERACTIONCONTEXT interactionContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ProcessInertiaInteractionContext(jitter):
    """
    HRESULT ProcessInertiaInteractionContext(
        HINTERACTIONCONTEXT interactionContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ProcessPointerFramesInteractionContext(jitter):
    """
    HRESULT ProcessPointerFramesInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        UINT32 entriesCount,
        UINT32 pointerCount,
        const POINTER_INFO* pointerInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "entriesCount", "pointerCount", "pointerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterOutputCallbackInteractionContext(jitter):
    """
    HRESULT RegisterOutputCallbackInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        INTERACTION_CONTEXT_OUTPUT_CALLBACK outputCallback,
        void* clientData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "outputCallback", "clientData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RemovePointerInteractionContext(jitter):
    """
    HRESULT RemovePointerInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        UINT32 pointerId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "pointerId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ResetInteractionContext(jitter):
    """
    HRESULT ResetInteractionContext(
        HINTERACTIONCONTEXT interactionContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetCrossSlideParametersInteractionContext(jitter):
    """
    HRESULT SetCrossSlideParametersInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        UINT32 parameterCount,
        CROSS_SLIDE_PARAMETER* crossSlideParameters
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "parameterCount", "crossSlideParameters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetInertiaParameterInteractionContext(jitter):
    """
    HRESULT SetInertiaParameterInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        INERTIA_PARAMETER inertiaParameter,
        float value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "inertiaParameter", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetInteractionConfigurationInteractionContext(jitter):
    """
    HRESULT SetInteractionConfigurationInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        UINT32 configurationCount,
        const INTERACTION_CONTEXT_CONFIGURATION* configuration
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "configurationCount", "configuration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMouseWheelParameterInteractionContext(jitter):
    """
    HRESULT SetMouseWheelParameterInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        MOUSE_WHEEL_PARAMETER parameter,
        float value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "parameter", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetPivotInteractionContext(jitter):
    """
    HRESULT SetPivotInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        float x,
        float y,
        float radius
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "x", "y", "radius"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetPropertyInteractionContext(jitter):
    """
    HRESULT SetPropertyInteractionContext(
        HINTERACTIONCONTEXT interactionContext,
        INTERACTION_CONTEXT_PROPERTY contextProperty,
        UINT32 value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "contextProperty", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_StopInteractionContext(jitter):
    """
    HRESULT StopInteractionContext(
        HINTERACTIONCONTEXT interactionContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["interactionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnableMouseInPointer(jitter):
    """
    BOOL EnableMouseInPointer(
        BOOL fEnable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerCursorId(jitter):
    """
    BOOL GetPointerCursorId(
        UINT32 pointerId,
        UINT32* cursorId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "cursorId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerFrameInfo(jitter):
    """
    BOOL GetPointerFrameInfo(
        UINT32 pointerId,
        UINT32* pointerCount,
        POINTER_INFO* pointerInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "pointerCount", "pointerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerFrameInfoHistory(jitter):
    """
    BOOL GetPointerFrameInfoHistory(
        UINT32 pointerId,
        UINT32* entriesCount,
        UINT32* pointerCount,
        POINTER_INFO* pointerInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "entriesCount", "pointerCount", "pointerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerFramePenInfo(jitter):
    """
    BOOL GetPointerFramePenInfo(
        UINT32 pointerId,
        UINT32* pointerCount,
        POINTER_PEN_INFO* penInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "pointerCount", "penInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerFramePenInfoHistory(jitter):
    """
    BOOL GetPointerFramePenInfoHistory(
        UINT32 pointerId,
        UINT32* entriesCount,
        UINT32* pointerCount,
        POINTER_PEN_INFO* penInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "entriesCount", "pointerCount", "penInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerFrameTouchInfo(jitter):
    """
    BOOL GetPointerFrameTouchInfo(
        UINT32 pointerId,
        UINT32* pointerCount,
        POINTER_TOUCH_INFO* touchInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "pointerCount", "touchInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerFrameTouchInfoHistory(jitter):
    """
    BOOL GetPointerFrameTouchInfoHistory(
        UINT32 pointerId,
        UINT32* entriesCount,
        UINT32* pointerCount,
        POINTER_TOUCH_INFO* touchInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "entriesCount", "pointerCount", "touchInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerInfo(jitter):
    """
    BOOL GetPointerInfo(
        UINT32 pointerId,
        POINTER_INFO* pointerInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "pointerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerInfoHistory(jitter):
    """
    BOOL GetPointerInfoHistory(
        UINT32 pointerId,
        UINT32* entriesCount,
        POINTER_INFO* pointerInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "entriesCount", "pointerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerPenInfo(jitter):
    """
    BOOL GetPointerPenInfo(
        UINT32 pointerId,
        POINTER_PEN_INFO* penInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "penInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerPenInfoHistory(jitter):
    """
    BOOL GetPointerPenInfoHistory(
        UINT32 pointerId,
        UINT32* entriesCount,
        POINTER_PEN_INFO* penInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "entriesCount", "penInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerTouchInfo(jitter):
    """
    BOOL GetPointerTouchInfo(
        UINT32 pointerId,
        POINTER_TOUCH_INFO* touchInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "touchInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerTouchInfoHistory(jitter):
    """
    BOOL GetPointerTouchInfoHistory(
        UINT32 pointerId,
        UINT32* entriesCount,
        POINTER_TOUCH_INFO* touchInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "entriesCount", "touchInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerType(jitter):
    """
    BOOL GetPointerType(
        UINT32 pointerId,
        POINTER_INPUT_TYPE* pointerType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "pointerType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetUnpredictedMessagePos(jitter):
    """
    DWORD GetUnpredictedMessagePos()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsMouseInPointerEnabled(jitter):
    """
    BOOL IsMouseInPointerEnabled()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SkipPointerFrameMessages(jitter):
    """
    BOOL SkipPointerFrameMessages(
        UINT32 pointerId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EvaluateProximityToPolygon(jitter):
    """
    BOOL EvaluateProximityToPolygon(
        UINT32 numVertices,
        const POINT* controlPolygon,
        const TOUCH_HIT_TESTING_INPUT* pHitTestingInput,
        TOUCH_HIT_TESTING_PROXIMITY_EVALUATION* pProximityEval
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["numVertices", "controlPolygon", "pHitTestingInput", "pProximityEval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EvaluateProximityToRect(jitter):
    """
    BOOL EvaluateProximityToRect(
        const RECT* controlBoundingBox,
        const TOUCH_HIT_TESTING_INPUT* pHitTestingInput,
        TOUCH_HIT_TESTING_PROXIMITY_EVALUATION* pProximityEval
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["controlBoundingBox", "pHitTestingInput", "pProximityEval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PackTouchHitTestingProximityEvaluation(jitter):
    """
    LRESULT PackTouchHitTestingProximityEvaluation(
        const TOUCH_HIT_TESTING_INPUT* pHitTestingInput,
        const TOUCH_HIT_TESTING_PROXIMITY_EVALUATION* pProximityEval
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pHitTestingInput", "pProximityEval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterTouchHitTestingWindow(jitter):
    """
    BOOL RegisterTouchHitTestingWindow(
        HWND hwnd,
        ULONG value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCIMSSM(jitter):
    """
    BOOL GetCIMSSM(
        INPUT_MESSAGE_SOURCE* inputMessageSource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["inputMessageSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCurrentInputMessageSource(jitter):
    """
    BOOL GetCurrentInputMessageSource(
        INPUT_MESSAGE_SOURCE* inputMessageSource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["inputMessageSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerDevice(jitter):
    """
    BOOL GetPointerDevice(
        HANDLE device,
        POINTER_DEVICE_INFO* pointerDevice
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["device", "pointerDevice"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerDeviceCursors(jitter):
    """
    BOOL GetPointerDeviceCursors(
        HANDLE device,
        UINT32* cursorCount,
        POINTER_DEVICE_CURSOR_INFO* deviceCursors
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["device", "cursorCount", "deviceCursors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerDeviceProperties(jitter):
    """
    BOOL GetPointerDeviceProperties(
        HANDLE device,
        UINT32* propertyCount,
        POINTER_DEVICE_PROPERTY* pointerProperties
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["device", "propertyCount", "pointerProperties"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerDeviceRects(jitter):
    """
    BOOL GetPointerDeviceRects(
        HANDLE device,
        RECT* pointerDeviceRect,
        RECT* displayRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["device", "pointerDeviceRect", "displayRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerDevices(jitter):
    """
    BOOL GetPointerDevices(
        UINT32 deviceCount,
        POINTER_DEVICE_INFO* pointerDevices
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["deviceCount", "pointerDevices"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetRawPointerDeviceData(jitter):
    """
    BOOL GetRawPointerDeviceData(
        UINT32 pointerId,
        UINT32 historyCount,
        UINT32 propertiesCount,
        POINTER_DEVICE_PROPERTY* pProperties,
        LONG* pValues
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "historyCount", "propertiesCount", "pProperties", "pValues"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterPointerDeviceNotifications(jitter):
    """
    BOOL RegisterPointerDeviceNotifications(
        HWND window,
        BOOL notifyRange
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["window", "notifyRange"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterSuspendResumeNotification(jitter):
    """
    HPOWERNOTIFY RegisterSuspendResumeNotification(
        PDEVICE_NOTIFY_SUBSCRIBE_PARAMETERS hRecipient,
        [POWER_NOTIFICATION_FLAGS] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRecipient", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnregisterSuspendResumeNotification(jitter):
    """
    BOOL UnregisterSuspendResumeNotification(
        HPOWERNOTIFY RegistrationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RegistrationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowFeedbackSetting(jitter):
    """
    BOOL GetWindowFeedbackSetting(
        HWND hwnd,
        FEEDBACK_TYPE feedback,
        [GWFS_FLAGS] dwFlags,
        UINT32* pSize,
        VOID* config
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "feedback", "dwFlags", "pSize", "config"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowFeedbackSetting(jitter):
    """
    BOOL SetWindowFeedbackSetting(
        HWND hwnd,
        FEEDBACK_TYPE feedback,
        DWORD dwFlags,
        UINT32 size,
        const VOID* configuration
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "feedback", "dwFlags", "size", "configuration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
