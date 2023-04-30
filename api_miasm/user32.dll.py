
def user32_CreateDialogIndirectParam(jitter):
    """"
    [User32.dll] HWND CreateDialogIndirectParam(HINSTANCE hInstance, LPCDLGTEMPLATE lpTemplate, HWND hWndParent, DLGPROC lpDialogFunc, LPARAM lParamInit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpTemplate", "hWndParent", "lpDialogFunc", "lParamInit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateDialogParam(jitter):
    """"
    [User32.dll] HWND CreateDialogParam(HINSTANCE hInstance, LPCTSTR lpTemplateName, HWND hWndParent, DLGPROC lpDialogFunc, LPARAM lParamInit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpTemplateName", "hWndParent", "lpDialogFunc", "lParamInit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DefDlgProc(jitter):
    """"
    [User32.dll] LRESULT DefDlgProc(HWND hDlg, [WinMsg] Msg, WPARAM wParam, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DialogBoxIndirectParam(jitter):
    """"
    [User32.dll] INT_PTR DialogBoxIndirectParam(HINSTANCE hInstance, LPCDLGTEMPLATE hDialogTemplate, HWND hWndParent, DLGPROC lpDialogFunc, LPARAM dwInitParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "hDialogTemplate", "hWndParent", "lpDialogFunc", "dwInitParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DialogBoxParam(jitter):
    """"
    [User32.dll] INT_PTR DialogBoxParam(HINSTANCE hInstance, LPCTSTR lpTemplateName, HWND hWndParent, DLGPROC lpDialogFunc, LPARAM dwInitParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpTemplateName", "hWndParent", "lpDialogFunc", "dwInitParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EndDialog(jitter):
    """"
    [User32.dll] BOOL EndDialog(HWND hDlg, INT_PTR nResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDialogBaseUnits(jitter):
    """"
    [User32.dll] LONG GetDialogBaseUnits()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDlgCtrlID(jitter):
    """"
    [User32.dll] int GetDlgCtrlID(HWND hwndCtl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndCtl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDlgItem(jitter):
    """"
    [User32.dll] HWND GetDlgItem(HWND hDlg, int nIDDlgItem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDDlgItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDlgItemInt(jitter):
    """"
    [User32.dll] UINT GetDlgItemInt(HWND hDlg, int nIDDlgItem, BOOL* lpTranslated, BOOL bSigned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDDlgItem", "lpTranslated", "bSigned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDlgItemText(jitter):
    """"
    [User32.dll] UINT GetDlgItemText(HWND hDlg, int nIDDlgItem, LPTSTR lpString, int nMaxCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDDlgItem", "lpString", "nMaxCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetNextDlgGroupItem(jitter):
    """"
    [User32.dll] HWND GetNextDlgGroupItem(HWND hDlg, HWND hCtl, BOOL bPrevious)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "hCtl", "bPrevious"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetNextDlgTabItem(jitter):
    """"
    [User32.dll] HWND GetNextDlgTabItem(HWND hDlg, HWND hCtl, BOOL bPrevious)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "hCtl", "bPrevious"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsDialogMessage(jitter):
    """"
    [User32.dll] BOOL IsDialogMessage(HWND hDlg, LPMSG lpMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "lpMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MapDialogRect(jitter):
    """"
    [User32.dll] BOOL MapDialogRect(HWND hDlg, LPRECT lpRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MessageBox(jitter):
    """"
    [User32.dll] [MessageBoxResult] MessageBox(HWND hWnd, LPCTSTR lpText, LPCTSTR lpCaption, [MessageBoxType] uType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpText", "lpCaption", "uType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MessageBoxEx(jitter):
    """"
    [User32.dll] [MessageBoxResult] MessageBoxEx(HWND hWnd, LPCTSTR lpText, LPCTSTR lpCaption, [MessageBoxType] uType, WORD wLanguageId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpText", "lpCaption", "uType", "wLanguageId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MessageBoxIndirect(jitter):
    """"
    [User32.dll] int MessageBoxIndirect(const LPMSGBOXPARAMS lpMsgBoxParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMsgBoxParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MessageBoxTimeout(jitter):
    """"
    [User32.dll] [MessageBoxResult] MessageBoxTimeout(HWND hWnd, LPCTSTR lpText, LPCTSTR lpCaption, [MessageBoxType] uType, WORD wLanguageId, [WaitTimeout] dwMilliseconds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpText", "lpCaption", "uType", "wLanguageId", "dwMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SendDlgItemMessage(jitter):
    """"
    [User32.dll] LRESULT SendDlgItemMessage(HWND hDlg, int nIDDlgItem, [WinMsg] Msg, WPARAM wParam, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDDlgItem", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetDlgItemInt(jitter):
    """"
    [User32.dll] BOOL SetDlgItemInt(HWND hDlg, int nIDDlgItem, UINT uValue, BOOL bSigned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDDlgItem", "uValue", "bSigned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetDlgItemText(jitter):
    """"
    [User32.dll] BOOL SetDlgItemText(HWND hDlg, int nIDDlgItem, LPCTSTR lpString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDDlgItem", "lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BroadcastSystemMessage(jitter):
    """"
    [User32.dll] long BroadcastSystemMessage(DWORD dwFlags, LPDWORD lpdwRecipients, UINT uiMessage, WPARAM wParam, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpdwRecipients", "uiMessage", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BroadcastSystemMessageEx(jitter):
    """"
    [User32.dll] long BroadcastSystemMessageEx(DWORD dwFlags, LPDWORD lpdwRecipients, UINT uiMessage, WPARAM wParam, LPARAM lParam, PBSMINFO pBSMInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpdwRecipients", "uiMessage", "wParam", "lParam", "pBSMInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DispatchMessage(jitter):
    """"
    [User32.dll] LRESULT DispatchMessage(const MSG* lpmsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpmsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetInputState(jitter):
    """"
    [User32.dll] BOOL GetInputState()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMessage(jitter):
    """"
    [User32.dll] [BOOL_NUMBER] GetMessage(LPMSG lpMsg, HWND hWnd, UINT wMsgFilterMin, UINT wMsgFilterMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMsg", "hWnd", "wMsgFilterMin", "wMsgFilterMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMessageExtraInfo(jitter):
    """"
    [User32.dll] LPARAM GetMessageExtraInfo()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMessagePos(jitter):
    """"
    [User32.dll] DWORD GetMessagePos()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMessageTime(jitter):
    """"
    [User32.dll] LONG GetMessageTime()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetQueueStatus(jitter):
    """"
    [User32.dll] DWORD GetQueueStatus([QueueStatusFlag] flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InSendMessage(jitter):
    """"
    [User32.dll] BOOL InSendMessage()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InSendMessageEx(jitter):
    """"
    [User32.dll] DWORD InSendMessageEx(LPVOID lpReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PeekMessage(jitter):
    """"
    [User32.dll] BOOL PeekMessage(LPMSG lpMsg, HWND hWnd, UINT wMsgFilterMin, UINT wMsgFilterMax, [PeekMessageFlag] wRemoveMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMsg", "hWnd", "wMsgFilterMin", "wMsgFilterMax", "wRemoveMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PostMessage(jitter):
    """"
    [User32.dll] BOOL PostMessage(HWND hWnd, [WinMsg] Msg, WPARAM wParam, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PostQuitMessage(jitter):
    """"
    [User32.dll] VOID PostQuitMessage(int nExitCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nExitCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PostThreadMessage(jitter):
    """"
    [User32.dll] BOOL PostThreadMessage(DWORD idThread, [WinMsg] Msg, WPARAM wParam, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idThread", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterWindowMessage(jitter):
    """"
    [User32.dll] UINT RegisterWindowMessage(LPCTSTR lpString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ReplyMessage(jitter):
    """"
    [User32.dll] BOOL ReplyMessage(LRESULT lResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SendMessage(jitter):
    """"
    [User32.dll] LRESULT SendMessage(HWND hWnd, [WinMsg] Msg, WPARAM wParam, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SendMessageCallback(jitter):
    """"
    [User32.dll] BOOL SendMessageCallback(HWND hWnd, [WinMsg] Msg, WPARAM wParam, LPARAM lParam, SENDASYNCPROC lpCallBack, ULONG_PTR dwData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "Msg", "wParam", "lParam", "lpCallBack", "dwData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SendMessageTimeout(jitter):
    """"
    [User32.dll] LRESULT SendMessageTimeout(HWND hWnd, [WinMsg] Msg, WPARAM wParam, LPARAM lParam, [SendMessageTimeoutFlags] fuFlags, UINT uTimeout, PDWORD_PTR lpdwResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "Msg", "wParam", "lParam", "fuFlags", "uTimeout", "lpdwResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SendNotifyMessage(jitter):
    """"
    [User32.dll] BOOL SendNotifyMessage(HWND hWnd, [WinMsg] Msg, WPARAM wParam, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMessageExtraInfo(jitter):
    """"
    [User32.dll] LPARAM SetMessageExtraInfo(LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TranslateMessage(jitter):
    """"
    [User32.dll] BOOL TranslateMessage(const MSG* lpMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_WaitMessage(jitter):
    """"
    [User32.dll] BOOL WaitMessage()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetGuiResources(jitter):
    """"
    [User32.dll] DWORD GetGuiResources([ProcessHandle] hProcess, DWORD uiFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "uiFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsImmersiveProcess(jitter):
    """"
    [User32.dll] BOOL IsImmersiveProcess(HANDLE hProcess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetProcessRestrictionExemption(jitter):
    """"
    [User32.dll] BOOL SetProcessRestrictionExemption(BOOL fEnableExemption)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fEnableExemption"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AttachThreadInput(jitter):
    """"
    [User32.dll] BOOL AttachThreadInput(DWORD idAttach, DWORD idAttachTo, BOOL fAttach)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idAttach", "idAttachTo", "fAttach"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_WaitForInputIdle(jitter):
    """"
    [User32.dll] DWORD WaitForInputIdle([ProcessHandle] hProcess, [WaitTimeout] dwMilliseconds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProcess", "dwMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWow64Message(jitter):
    """"
    [User32.dll] BOOL IsWow64Message()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UserHandleGrantAccess(jitter):
    """"
    [User32.dll] BOOL UserHandleGrantAccess(HANDLE hUserHandle, HANDLE hJob, BOOL bGrant)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hUserHandle", "hJob", "bGrant"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AdjustWindowRect(jitter):
    """"
    [User32.dll] BOOL AdjustWindowRect(LPRECT lpRect, [WindowStyle] dwStyle, BOOL bMenu)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpRect", "dwStyle", "bMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AdjustWindowRectEx(jitter):
    """"
    [User32.dll] BOOL AdjustWindowRectEx(LPRECT lpRect, [WindowStyle] dwStyle, BOOL bMenu, [WindowExStyle] dwExStyle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpRect", "dwStyle", "bMenu", "dwExStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AllowActivateDetachQueuesSetFocus(jitter):
    """"
    [User32.dll] VOID AllowActivateDetachQueuesSetFocus()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AllowSetForegroundWindow(jitter):
    """"
    [User32.dll] BOOL AllowSetForegroundWindow(DWORD dwProcessId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AnimateWindow(jitter):
    """"
    [User32.dll] BOOL AnimateWindow(HWND hwnd, DWORD dwTime, [AnimateWindowFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwTime", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AnyPopup(jitter):
    """"
    [User32.dll] BOOL AnyPopup()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ArrangeIconicWindows(jitter):
    """"
    [User32.dll] UINT ArrangeIconicWindows(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BeginDeferWindowPos(jitter):
    """"
    [User32.dll] HDWP BeginDeferWindowPos(int nNumWindows)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nNumWindows"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BringWindowToTop(jitter):
    """"
    [User32.dll] BOOL BringWindowToTop(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CalculatePopupWindowPosition(jitter):
    """"
    [User32.dll] BOOL CalculatePopupWindowPosition(const POINT* anchorPoint, const SIZE* windowSize, [TrackPopupMenuFlags] flags, RECT* excludeRect, RECT* popupWindowPosition)
    """"
    ret_ad, args = jitter.func_args_stdcall(["anchorPoint", "windowSize", "flags", "excludeRect", "popupWindowPosition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CascadeWindows(jitter):
    """"
    [User32.dll] WORD CascadeWindows(HWND hwndParent, [MDITILE_CASCADE] wHow, const RECT* lpRect, UINT cKids, const HWND* lpKids)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "wHow", "lpRect", "cKids", "lpKids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChangeWindowMessageFilter(jitter):
    """"
    [User32.dll] BOOL ChangeWindowMessageFilter([WinMsg] message, [WindowMessageFilterEnum] dwFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["message", "dwFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChangeWindowMessageFilterEx(jitter):
    """"
    [User32.dll] BOOL ChangeWindowMessageFilterEx(HWND hWnd, [WinMsg] message, [MSGFLT_ACTION] action, PCHANGEFILTERSTRUCT pChangeFilterStruct)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "message", "action", "pChangeFilterStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChildWindowFromPoint(jitter):
    """"
    [User32.dll] HWND ChildWindowFromPoint(HWND hWndParent, POINT Point)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndParent", "Point"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChildWindowFromPointEx(jitter):
    """"
    [User32.dll] HWND ChildWindowFromPointEx(HWND hwndParent, POINT pt, [CWP_FLAGS] uFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "pt", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CloseWindow(jitter):
    """"
    [User32.dll] BOOL CloseWindow(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateWindow(jitter):
    """"
    [User32.dll] HWND CreateWindow(LPCTSTR lpClassName, LPCTSTR lpWindowName, DWORD dwStyle, [CreateWindow_CW] x, [CreateWindow_CW] y, [CreateWindow_CW] nWidth, [CreateWindow_CW] nHeight, HWND hWndParent, HMENU hMenu, HINSTANCE hInstance, LPVOID lpParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpClassName", "lpWindowName", "dwStyle", "x", "y", "nWidth", "nHeight", "hWndParent", "hMenu", "hInstance", "lpParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateWindowEx(jitter):
    """"
    [User32.dll] HWND CreateWindowEx([WindowExStyle] dwExStyle, LPCTSTR lpClassName, LPCTSTR lpWindowName, [WindowStyle] dwStyle, [CreateWindow_CW] x, [CreateWindow_CW] y, [CreateWindow_CW] nWidth, [CreateWindow_CW] nHeight, HWND hWndParent, HMENU hMenu, HINSTANCE hInstance, LPVOID lpParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwExStyle", "lpClassName", "lpWindowName", "dwStyle", "x", "y", "nWidth", "nHeight", "hWndParent", "hMenu", "hInstance", "lpParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DeferWindowPos(jitter):
    """"
    [User32.dll] HDWP DeferWindowPos(HDWP hWinPosInfo, HWND hWnd, [HwndInsertAfterEnum] hWndInsertAfter, int x, int y, int cx, int cy, [SetWindowPosFlags] uFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWinPosInfo", "hWnd", "hWndInsertAfter", "x", "y", "cx", "cy", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DeregisterShellHookWindow(jitter):
    """"
    [User32.dll] BOOL DeregisterShellHookWindow(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DestroyWindow(jitter):
    """"
    [User32.dll] BOOL DestroyWindow(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EndDeferWindowPos(jitter):
    """"
    [User32.dll] BOOL EndDeferWindowPos(HDWP hWinPosInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWinPosInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EndTask(jitter):
    """"
    [User32.dll] BOOL EndTask(HWND hWnd, BOOL fShutDown, BOOL fForce)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "fShutDown", "fForce"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumChildWindows(jitter):
    """"
    [User32.dll] BOOL EnumChildWindows(HWND hWndParent, WNDENUMPROC lpEnumFunc, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndParent", "lpEnumFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumThreadWindows(jitter):
    """"
    [User32.dll] BOOL EnumThreadWindows(DWORD dwThreadId, WNDENUMPROC lpfn, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwThreadId", "lpfn", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumWindows(jitter):
    """"
    [User32.dll] BOOL EnumWindows(WNDENUMPROC lpEnumFunc, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpEnumFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FindWindow(jitter):
    """"
    [User32.dll] HWND FindWindow(LPCTSTR lpClassName, LPCTSTR lpWindowName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpClassName", "lpWindowName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FindWindowEx(jitter):
    """"
    [User32.dll] HWND FindWindowEx(HWND hwndParent, HWND hwndChildAfter, LPCTSTR lpszClass, LPCTSTR lpszWindow)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hwndChildAfter", "lpszClass", "lpszWindow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetAltTabInfo(jitter):
    """"
    [User32.dll] BOOL GetAltTabInfo(HWND hwnd, int iItem, PALTTABINFO pati, LPTSTR pszItemText, UINT cchItemText)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "iItem", "pati", "pszItemText", "cchItemText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetAncestor(jitter):
    """"
    [User32.dll] HWND GetAncestor(HWND hwnd, [GetAncestorEnum] gaFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "gaFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClientRect(jitter):
    """"
    [User32.dll] BOOL GetClientRect(HWND hWnd, LPRECT lpRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDesktopWindow(jitter):
    """"
    [User32.dll] HWND GetDesktopWindow()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetForegroundWindow(jitter):
    """"
    [User32.dll] HWND GetForegroundWindow()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetGUIThreadInfo(jitter):
    """"
    [User32.dll] BOOL GetGUIThreadInfo(DWORD idThread, LPGUITHREADINFO lpgui)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idThread", "lpgui"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetLastActivePopup(jitter):
    """"
    [User32.dll] HWND GetLastActivePopup(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetLayeredWindowAttributes(jitter):
    """"
    [User32.dll] BOOL GetLayeredWindowAttributes(HWND hwnd, COLORREF* pcrKey, BYTE* pbAlpha, [LayeredWindowAttribute*] pdwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pcrKey", "pbAlpha", "pdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetParent(jitter):
    """"
    [User32.dll] HWND GetParent(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetProcessDefaultLayout(jitter):
    """"
    [User32.dll] BOOL GetProcessDefaultLayout(DWORD* pdwDefaultLayout)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pdwDefaultLayout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetShellWindow(jitter):
    """"
    [User32.dll] HWND GetShellWindow()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetTitleBarInfo(jitter):
    """"
    [User32.dll] BOOL GetTitleBarInfo(HWND hwnd, PTITLEBARINFO pti)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pti"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetTopWindow(jitter):
    """"
    [User32.dll] HWND GetTopWindow(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindow(jitter):
    """"
    [User32.dll] HWND GetWindow(HWND hWnd, [GetWindowEnum] uCmd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "uCmd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowDisplayAffinity(jitter):
    """"
    [User32.dll] BOOL GetWindowDisplayAffinity(HWND hWnd, DWORD* dwAffinity)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "dwAffinity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowInfo(jitter):
    """"
    [User32.dll] BOOL GetWindowInfo(HWND hwnd, PWINDOWINFO pwi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pwi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowModuleFileName(jitter):
    """"
    [User32.dll] UINT GetWindowModuleFileName(HWND hwnd, LPTSTR lpszFileName, UINT cchFileNameMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpszFileName", "cchFileNameMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowPlacement(jitter):
    """"
    [User32.dll] BOOL GetWindowPlacement(HWND hWnd, WINDOWPLACEMENT* lpwndpl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpwndpl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowRect(jitter):
    """"
    [User32.dll] BOOL GetWindowRect(HWND hWnd, LPRECT lpRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowText(jitter):
    """"
    [User32.dll] int GetWindowText(HWND hWnd, LPTSTR lpString, int nMaxCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpString", "nMaxCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowTextLength(jitter):
    """"
    [User32.dll] int GetWindowTextLength(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowThreadProcessId(jitter):
    """"
    [User32.dll] DWORD GetWindowThreadProcessId(HWND hWnd, LPDWORD lpdwProcessId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpdwProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InternalGetWindowText(jitter):
    """"
    [User32.dll] int InternalGetWindowText(HWND hWnd, LPWSTR lpString, int nMaxCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpString", "nMaxCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsChild(jitter):
    """"
    [User32.dll] BOOL IsChild(HWND hWndParent, HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndParent", "hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsGUIThread(jitter):
    """"
    [User32.dll] BOOL IsGUIThread(BOOL bConvert)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bConvert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsHungAppWindow(jitter):
    """"
    [User32.dll] BOOL IsHungAppWindow(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsIconic(jitter):
    """"
    [User32.dll] BOOL IsIconic(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsProcessDPIAware(jitter):
    """"
    [User32.dll] BOOL IsProcessDPIAware()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWindow(jitter):
    """"
    [User32.dll] BOOL IsWindow(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWindowUnicode(jitter):
    """"
    [User32.dll] BOOL IsWindowUnicode(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWindowVisible(jitter):
    """"
    [User32.dll] BOOL IsWindowVisible(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsZoomed(jitter):
    """"
    [User32.dll] BOOL IsZoomed(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LockSetForegroundWindow(jitter):
    """"
    [User32.dll] BOOL LockSetForegroundWindow([LockSetForegroundWindowCode] uLockCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uLockCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LogicalToPhysicalPoint(jitter):
    """"
    [User32.dll] void LogicalToPhysicalPoint(HWND hWnd, LPPOINT lpPoint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MoveWindow(jitter):
    """"
    [User32.dll] BOOL MoveWindow(HWND hWnd, int X, int Y, int nWidth, int nHeight, BOOL bRepaint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "X", "Y", "nWidth", "nHeight", "bRepaint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OpenIcon(jitter):
    """"
    [User32.dll] BOOL OpenIcon(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PhysicalToLogicalPoint(jitter):
    """"
    [User32.dll] void PhysicalToLogicalPoint(HWND hWnd, LPPOINT lpPoint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RealChildWindowFromPoint(jitter):
    """"
    [User32.dll] HWND RealChildWindowFromPoint(HWND hwndParent, POINT ptParentClientCoords)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "ptParentClientCoords"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RealGetWindowClass(jitter):
    """"
    [User32.dll] UINT RealGetWindowClass(HWND hwnd, LPTSTR pszType, UINT cchType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszType", "cchType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterShellHookWindow(jitter):
    """"
    [User32.dll] BOOL RegisterShellHookWindow(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetForegroundWindow(jitter):
    """"
    [User32.dll] BOOL SetForegroundWindow(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetLayeredWindowAttributes(jitter):
    """"
    [User32.dll] BOOL SetLayeredWindowAttributes(HWND hwnd, COLORREF crKey, BYTE bAlpha, [LayeredWindowAttribute] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "crKey", "bAlpha", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetParent(jitter):
    """"
    [User32.dll] HWND SetParent(HWND hWndChild, HWND hWndNewParent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndChild", "hWndNewParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetProcessDefaultLayout(jitter):
    """"
    [User32.dll] BOOL SetProcessDefaultLayout(DWORD dwDefaultLayout)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDefaultLayout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetProcessDPIAware(jitter):
    """"
    [User32.dll] BOOL SetProcessDPIAware()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowDisplayAffinity(jitter):
    """"
    [User32.dll] BOOL SetWindowDisplayAffinity(HWND hWnd, DWORD dwAffinity)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "dwAffinity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowPlacement(jitter):
    """"
    [User32.dll] BOOL SetWindowPlacement(HWND hWnd, WINDOWPLACEMENT* lpwndpl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpwndpl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowPos(jitter):
    """"
    [User32.dll] BOOL SetWindowPos(HWND hWnd, [HwndInsertAfterEnum] hWndInsertAfter, int X, int Y, int cx, int cy, [SetWindowPosFlags] uFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hWndInsertAfter", "X", "Y", "cx", "cy", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowText(jitter):
    """"
    [User32.dll] BOOL SetWindowText(HWND hWnd, LPCTSTR lpString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShowOwnedPopups(jitter):
    """"
    [User32.dll] BOOL ShowOwnedPopups(HWND hWnd, BOOL fShow)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "fShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShowWindow(jitter):
    """"
    [User32.dll] BOOL ShowWindow(HWND hWnd, [ShowWindowCmd] nCmdShow)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nCmdShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShowWindowAsync(jitter):
    """"
    [User32.dll] BOOL ShowWindowAsync(HWND hWnd, int nCmdShow)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nCmdShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SoundSentry(jitter):
    """"
    [User32.dll] BOOL SoundSentry()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SwitchToThisWindow(jitter):
    """"
    [User32.dll] VOID SwitchToThisWindow(HWND hWnd, BOOL fAltTab)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "fAltTab"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TileWindows(jitter):
    """"
    [User32.dll] WORD TileWindows(HWND hwndParent, [MDITILE_TILE] wHow, RECT* lpRect, UINT cKids, const HWND* lpKids)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "wHow", "lpRect", "cKids", "lpKids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UpdateLayeredWindow(jitter):
    """"
    [User32.dll] BOOL UpdateLayeredWindow(HWND hwnd, HDC hdcDst, POINT* pptDst, SIZE* psize, HDC hdcSrc, POINT* pptSrc, COLORREF crKey, BLENDFUNCTION* pblend, [UpdateLayeredWindowFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdcDst", "pptDst", "psize", "hdcSrc", "pptSrc", "crKey", "pblend", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UpdateLayeredWindowIndirect(jitter):
    """"
    [User32.dll] BOOL UpdateLayeredWindowIndirect(HWND hwnd, const UPDATELAYEREDWINDOWINFO* pULWInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pULWInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_WindowFromPhysicalPoint(jitter):
    """"
    [User32.dll] HWND WindowFromPhysicalPoint(POINT Point)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Point"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_WindowFromPoint(jitter):
    """"
    [User32.dll] HWND WindowFromPoint(POINT Point)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Point"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ExitWindowsEx(jitter):
    """"
    [User32.dll] BOOL ExitWindowsEx([EWX_FLAGS] uFlags, [SHTDN_REASON] dwReason)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uFlags", "dwReason"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LockWorkStation(jitter):
    """"
    [User32.dll] BOOL LockWorkStation()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShutdownBlockReasonCreate(jitter):
    """"
    [User32.dll] BOOL ShutdownBlockReasonCreate(HWND hWnd, LPCWSTR pwszReason)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pwszReason"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShutdownBlockReasonDestroy(jitter):
    """"
    [User32.dll] BOOL ShutdownBlockReasonDestroy(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShutdownBlockReasonQuery(jitter):
    """"
    [User32.dll] BOOL ShutdownBlockReasonQuery(HWND hWnd, LPWSTR pwszBuff, DWORD* pcchBuff)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pwszBuff", "pcchBuff"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadBitmap(jitter):
    """"
    [User32.dll] HBITMAP LoadBitmap(HINSTANCE hInstance, [LoadBitmapString/LPCTSTR] lpBitmapName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpBitmapName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetSysColorBrush(jitter):
    """"
    [User32.dll] HBRUSH GetSysColorBrush([SysColorIndex] nIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CheckDlgButton(jitter):
    """"
    [User32.dll] BOOL CheckDlgButton(HWND hDlg, int nIDButton, [ButtonState] uCheck)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDButton", "uCheck"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CheckRadioButton(jitter):
    """"
    [User32.dll] BOOL CheckRadioButton(HWND hDlg, int nIDFirstButton, int nIDLastButton, int nIDCheckButton)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDFirstButton", "nIDLastButton", "nIDCheckButton"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsDlgButtonChecked(jitter):
    """"
    [User32.dll] [ButtonState] IsDlgButtonChecked(HWND hDlg, int nIDButton)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "nIDButton"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateCaret(jitter):
    """"
    [User32.dll] BOOL CreateCaret(HWND hWnd, HBITMAP hBitmap, int nWidth, int nHeight)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hBitmap", "nWidth", "nHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DestroyCaret(jitter):
    """"
    [User32.dll] BOOL DestroyCaret()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCaretBlinkTime(jitter):
    """"
    [User32.dll] UINT GetCaretBlinkTime()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCaretPos(jitter):
    """"
    [User32.dll] BOOL GetCaretPos(LPPOINT lpPoint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_HideCaret(jitter):
    """"
    [User32.dll] BOOL HideCaret(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetCaretBlinkTime(jitter):
    """"
    [User32.dll] BOOL SetCaretBlinkTime(UINT uMSeconds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uMSeconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetCaretPos(jitter):
    """"
    [User32.dll] BOOL SetCaretPos(int X, int Y)
    """"
    ret_ad, args = jitter.func_args_stdcall(["X", "Y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShowCaret(jitter):
    """"
    [User32.dll] BOOL ShowCaret(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AddClipboardFormatListener(jitter):
    """"
    [User32.dll] BOOL AddClipboardFormatListener(HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChangeClipboardChain(jitter):
    """"
    [User32.dll] BOOL ChangeClipboardChain(HWND hWndRemove, HWND hWndNewNext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndRemove", "hWndNewNext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CloseClipboard(jitter):
    """"
    [User32.dll] BOOL CloseClipboard()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CountClipboardFormats(jitter):
    """"
    [User32.dll] int CountClipboardFormats()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EmptyClipboard(jitter):
    """"
    [User32.dll] BOOL EmptyClipboard()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumClipboardFormats(jitter):
    """"
    [User32.dll] UINT EnumClipboardFormats(UINT format)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClipboardData(jitter):
    """"
    [User32.dll] HANDLE GetClipboardData([ClipboardFormat] uFormat)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClipboardFormatName(jitter):
    """"
    [User32.dll] int GetClipboardFormatName(UINT format, LPTSTR lpszFormatName, int cchMaxCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format", "lpszFormatName", "cchMaxCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClipboardOwner(jitter):
    """"
    [User32.dll] HWND GetClipboardOwner()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClipboardSequenceNumber(jitter):
    """"
    [User32.dll] DWORD GetClipboardSequenceNumber()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClipboardViewer(jitter):
    """"
    [User32.dll] HWND GetClipboardViewer()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetOpenClipboardWindow(jitter):
    """"
    [User32.dll] HWND GetOpenClipboardWindow()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPriorityClipboardFormat(jitter):
    """"
    [User32.dll] int GetPriorityClipboardFormat(UINT* paFormatPriorityList, int cFormats)
    """"
    ret_ad, args = jitter.func_args_stdcall(["paFormatPriorityList", "cFormats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetUpdatedClipboardFormats(jitter):
    """"
    [User32.dll] BOOL GetUpdatedClipboardFormats(PUINT lpuiFormats, UINT cFormats, PUINT pcFormatsOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpuiFormats", "cFormats", "pcFormatsOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsClipboardFormatAvailable(jitter):
    """"
    [User32.dll] BOOL IsClipboardFormatAvailable([ClipboardFormat] format)
    """"
    ret_ad, args = jitter.func_args_stdcall(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OpenClipboard(jitter):
    """"
    [User32.dll] BOOL OpenClipboard(HWND hWndNewOwner)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndNewOwner"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterClipboardFormat(jitter):
    """"
    [User32.dll] UINT RegisterClipboardFormat(LPCTSTR lpszFormat)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RemoveClipboardFormatListener(jitter):
    """"
    [User32.dll] BOOL RemoveClipboardFormatListener(HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetClipboardData(jitter):
    """"
    [User32.dll] HANDLE SetClipboardData([ClipboardFormat] uFormat, HANDLE hMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uFormat", "hMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetClipboardViewer(jitter):
    """"
    [User32.dll] HWND SetClipboardViewer(HWND hWndNewViewer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndNewViewer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DlgDirListComboBox(jitter):
    """"
    [User32.dll] int DlgDirListComboBox(HWND hDlg, LPTSTR lpPathSpec, int nIDComboBox, int nIDStaticPath, UINT uFiletype)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "lpPathSpec", "nIDComboBox", "nIDStaticPath", "uFiletype"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DlgDirSelectComboBoxEx(jitter):
    """"
    [User32.dll] BOOL DlgDirSelectComboBoxEx(HWND hDlg, LPTSTR lpString, int nCount, int nIDComboBox)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "lpString", "nCount", "nIDComboBox"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetComboBoxInfo(jitter):
    """"
    [User32.dll] BOOL GetComboBoxInfo(HWND hwndCombo, PCOMBOBOXINFO pcbi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndCombo", "pcbi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ClientToScreen(jitter):
    """"
    [User32.dll] BOOL ClientToScreen(HWND hWnd, LPPOINT lpPoint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MapWindowPoints(jitter):
    """"
    [User32.dll] int MapWindowPoints(HWND hWndFrom, HWND hWndTo, LPPOINT lpPoints, UINT cPoints)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndFrom", "hWndTo", "lpPoints", "cPoints"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ScreenToClient(jitter):
    """"
    [User32.dll] BOOL ScreenToClient(HWND hWnd, LPPOINT lpPoint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ClipCursor(jitter):
    """"
    [User32.dll] BOOL ClipCursor(const RECT* lpRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CopyCursor(jitter):
    """"
    [User32.dll] HCURSOR CopyCursor(HCURSOR pcur)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pcur"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateCursor(jitter):
    """"
    [User32.dll] HCURSOR CreateCursor(HINSTANCE hInst, int xHotSpot, int yHotSpot, int nWidth, int nHeight, const VOID* pvANDPlane, const VOID* pvXORPlane)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInst", "xHotSpot", "yHotSpot", "nWidth", "nHeight", "pvANDPlane", "pvXORPlane"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DestroyCursor(jitter):
    """"
    [User32.dll] BOOL DestroyCursor(HCURSOR hCursor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCursor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClipCursor(jitter):
    """"
    [User32.dll] BOOL GetClipCursor(LPRECT lpRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCursor(jitter):
    """"
    [User32.dll] HCURSOR GetCursor()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCursorInfo(jitter):
    """"
    [User32.dll] BOOL GetCursorInfo(PCURSORINFO pci)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pci"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCursorPos(jitter):
    """"
    [User32.dll] BOOL GetCursorPos(LPPOINT lpPoint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPhysicalCursorPos(jitter):
    """"
    [User32.dll] BOOL GetPhysicalCursorPos(LPPOINT lpPoint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadCursor(jitter):
    """"
    [User32.dll] HCURSOR LoadCursor(HINSTANCE hInstance, [LoadCursorString/LPCTSTR] lpCursorName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpCursorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadCursorFromFile(jitter):
    """"
    [User32.dll] HCURSOR LoadCursorFromFile(LPCTSTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetCursor(jitter):
    """"
    [User32.dll] HCURSOR SetCursor(HCURSOR hCursor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCursor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetCursorPos(jitter):
    """"
    [User32.dll] BOOL SetCursorPos(int X, int Y)
    """"
    ret_ad, args = jitter.func_args_stdcall(["X", "Y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetPhysicalCursorPos(jitter):
    """"
    [User32.dll] BOOL SetPhysicalCursorPos(int X, int Y)
    """"
    ret_ad, args = jitter.func_args_stdcall(["X", "Y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetSystemCursor(jitter):
    """"
    [User32.dll] BOOL SetSystemCursor(HCURSOR hcur, [CursorId] id)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hcur", "id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShowCursor(jitter):
    """"
    [User32.dll] int ShowCursor(BOOL bShow)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChangeDisplaySettings(jitter):
    """"
    [User32.dll] LONG ChangeDisplaySettings(DEVMODE* lpDevMode, DWORD dwflags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpDevMode", "dwflags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ChangeDisplaySettingsEx(jitter):
    """"
    [User32.dll] LONG ChangeDisplaySettingsEx(LPCTSTR lpszDeviceName, DEVMODE* lpDevMode, HWND hwnd, DWORD dwflags, LPVOID lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDeviceName", "lpDevMode", "hwnd", "dwflags", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumDisplayDevices(jitter):
    """"
    [User32.dll] BOOL EnumDisplayDevices(LPCTSTR lpDevice, DWORD iDevNum, PDISPLAY_DEVICE lpDisplayDevice, [EnumDisplayDevicesFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpDevice", "iDevNum", "lpDisplayDevice", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumDisplaySettings(jitter):
    """"
    [User32.dll] BOOL EnumDisplaySettings(LPCTSTR lpszDeviceName, [EnumDisplaySettingsEnum] iModeNum, DEVMODE* lpDevMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDeviceName", "iModeNum", "lpDevMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumDisplaySettingsEx(jitter):
    """"
    [User32.dll] BOOL EnumDisplaySettingsEx(LPCTSTR lpszDeviceName, DWORD iModeNum, DEVMODE* lpDevMode, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDeviceName", "iModeNum", "lpDevMode", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDC(jitter):
    """"
    [User32.dll] HDC GetDC(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDCEx(jitter):
    """"
    [User32.dll] HDC GetDCEx(HWND hWnd, HRGN hrgnClip, [DCExFlags] flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hrgnClip", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ReleaseDC(jitter):
    """"
    [User32.dll] int ReleaseDC(HWND hWnd, HDC hDC)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hDC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterDeviceNotification(jitter):
    """"
    [User32.dll] HDEVNOTIFY RegisterDeviceNotification(HANDLE hRecipient, LPVOID NotificationFilter, [DeviceNotificationFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRecipient", "NotificationFilter", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnregisterDeviceNotification(jitter):
    """"
    [User32.dll] BOOL UnregisterDeviceNotification(HDEVNOTIFY Handle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeSetQualityOfService(jitter):
    """"
    [User32.dll] BOOL DdeSetQualityOfService(HWND hwndClient, const SECURITY_QUALITY_OF_SERVICE* pqosNew, PSECURITY_QUALITY_OF_SERVICE pqosPrev)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndClient", "pqosNew", "pqosPrev"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FreeDDElParam(jitter):
    """"
    [User32.dll] BOOL FreeDDElParam(UINT msg, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["msg", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ImpersonateDdeClientWindow(jitter):
    """"
    [User32.dll] BOOL ImpersonateDdeClientWindow(HWND hWndClient, HWND hWndServer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndClient", "hWndServer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PackDDElParam(jitter):
    """"
    [User32.dll] LPARAM PackDDElParam(UINT msg, UINT_PTR uiLo, UINT_PTR uiHi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["msg", "uiLo", "uiHi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ReuseDDElParam(jitter):
    """"
    [User32.dll] LPARAM ReuseDDElParam(LPARAM lParam, UINT msgIn, UINT msgOut, UINT_PTR uiLo, UINT_PTR uiHi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lParam", "msgIn", "msgOut", "uiLo", "uiHi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnpackDDElParam(jitter):
    """"
    [User32.dll] BOOL UnpackDDElParam(UINT msg, LPARAM lParam, PUINT_PTR puiLo, PUINT_PTR puiHi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["msg", "lParam", "puiLo", "puiHi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeAbandonTransaction(jitter):
    """"
    [User32.dll] BOOL DdeAbandonTransaction(DWORD idInst, HCONV hConv, DWORD idTransaction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hConv", "idTransaction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeAccessData(jitter):
    """"
    [User32.dll] LPBYTE DdeAccessData(HDDEDATA hData, LPDWORD pcbDataSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hData", "pcbDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeAddData(jitter):
    """"
    [User32.dll] HDDEDATA DdeAddData(HDDEDATA hData, LPBYTE pSrc, DWORD cb, DWORD cbOff)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hData", "pSrc", "cb", "cbOff"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeClientTransaction(jitter):
    """"
    [User32.dll] HDDEDATA DdeClientTransaction(LPBYTE pData, DWORD cbData, HCONV hConv, HSZ hszItem, UINT wFmt, UINT wType, DWORD dwTimeout, LPDWORD pdwResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pData", "cbData", "hConv", "hszItem", "wFmt", "wType", "dwTimeout", "pdwResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeCmpStringHandles(jitter):
    """"
    [User32.dll] int DdeCmpStringHandles(HSZ hsz1, HSZ hsz2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hsz1", "hsz2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeConnect(jitter):
    """"
    [User32.dll] HCONV DdeConnect(DWORD idInst, HSZ hszService, HSZ hszTopic, PCONVCONTEXT pCC)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hszService", "hszTopic", "pCC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeConnectList(jitter):
    """"
    [User32.dll] HCONVLIST DdeConnectList(DWORD idInst, HSZ hszService, HSZ hszTopic, HCONVLIST hConvList, PCONVCONTEXT pCC)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hszService", "hszTopic", "hConvList", "pCC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeCreateDataHandle(jitter):
    """"
    [User32.dll] HDDEDATA DdeCreateDataHandle(DWORD idInst, LPBYTE pSrc, DWORD cb, DWORD cbOff, HSZ hszItem, UINT wFmt, UINT afCmd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idInst", "pSrc", "cb", "cbOff", "hszItem", "wFmt", "afCmd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeCreateStringHandle(jitter):
    """"
    [User32.dll] HSZ DdeCreateStringHandle(DWORD idInst, LPTSTR psz, [CODE_PAGE|int] iCodePage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idInst", "psz", "iCodePage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeDisconnect(jitter):
    """"
    [User32.dll] BOOL DdeDisconnect(HCONV hConv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeDisconnectList(jitter):
    """"
    [User32.dll] BOOL DdeDisconnectList(HCONVLIST hConvList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConvList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeEnableCallback(jitter):
    """"
    [User32.dll] BOOL DdeEnableCallback(DWORD idInst, HCONV hConv, UINT wCmd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hConv", "wCmd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeFreeDataHandle(jitter):
    """"
    [User32.dll] BOOL DdeFreeDataHandle(HDDEDATA hData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeFreeStringHandle(jitter):
    """"
    [User32.dll] BOOL DdeFreeStringHandle(DWORD idInst, HSZ hsz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeGetData(jitter):
    """"
    [User32.dll] DWORD DdeGetData(HDDEDATA hData, LPBYTE pDst, DWORD cbMax, DWORD cbOff)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hData", "pDst", "cbMax", "cbOff"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeGetLastError(jitter):
    """"
    [User32.dll] UINT DdeGetLastError(DWORD idInst)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idInst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeImpersonateClient(jitter):
    """"
    [User32.dll] BOOL DdeImpersonateClient(HCONV hConv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeInitialize(jitter):
    """"
    [User32.dll] UINT DdeInitialize(LPDWORD pidInst, PFNCALLBACK pfnCallback, [DDE_INITIALIZE_FLAGS] afCmd, DWORD ulRes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pidInst", "pfnCallback", "afCmd", "ulRes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeKeepStringHandle(jitter):
    """"
    [User32.dll] BOOL DdeKeepStringHandle(DWORD idInst, HSZ hsz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeNameService(jitter):
    """"
    [User32.dll] HDDEDATA DdeNameService(DWORD idInst, UINT hsz1, UINT hsz2, UINT afCmd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hsz1", "hsz2", "afCmd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdePostAdvise(jitter):
    """"
    [User32.dll] BOOL DdePostAdvise(DWORD idInst, HSZ hszTopic, HSZ hszItem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hszTopic", "hszItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeQueryConvInfo(jitter):
    """"
    [User32.dll] UINT DdeQueryConvInfo(HCONV hConv, DWORD idTransaction, PCONVINFO pConvInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConv", "idTransaction", "pConvInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeQueryNextServer(jitter):
    """"
    [User32.dll] HCONV DdeQueryNextServer(HCONVLIST hConvList, HCONV hConvPrev)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConvList", "hConvPrev"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeQueryString(jitter):
    """"
    [User32.dll] DWORD DdeQueryString(DWORD idInst, HSZ hsz, LPTSTR psz, DWORD cchMax, [CODE_PAGE|int] iCodePage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idInst", "hsz", "psz", "cchMax", "iCodePage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeReconnect(jitter):
    """"
    [User32.dll] HCONV DdeReconnect(HCONV hConv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeSetUserHandle(jitter):
    """"
    [User32.dll] BOOL DdeSetUserHandle(HCONV hConv, DWORD id, DWORD_PTR hUser)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hConv", "id", "hUser"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeUnaccessData(jitter):
    """"
    [User32.dll] BOOL DdeUnaccessData(HDDEDATA hData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DdeUninitialize(jitter):
    """"
    [User32.dll] BOOL DdeUninitialize(DWORD idInst)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idInst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FlashWindow(jitter):
    """"
    [User32.dll] BOOL FlashWindow(HWND hWnd, BOOL bInvert)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "bInvert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FlashWindowEx(jitter):
    """"
    [User32.dll] BOOL FlashWindowEx(PFLASHWINFO pfwi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfwi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MessageBeep(jitter):
    """"
    [User32.dll] BOOL MessageBeep(UINT uType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetLastErrorEx(jitter):
    """"
    [User32.dll] void SetLastErrorEx([ERROR_CODE] dwErrCode, [SET_LAST_ERROR_EX_TYPE] dwType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwErrCode", "dwType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FillRect(jitter):
    """"
    [User32.dll] int FillRect(HDC hDC, const RECT* lprc, HBRUSH hbr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lprc", "hbr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FrameRect(jitter):
    """"
    [User32.dll] int FrameRect(HDC hDC, const RECT* lprc, HBRUSH hbr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lprc", "hbr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InvertRect(jitter):
    """"
    [User32.dll] BOOL InvertRect(HDC hDC, const RECT* lprc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawText(jitter):
    """"
    [User32.dll] int DrawText(HDC hDC, LPCTSTR lpchText, int nCount, LPRECT lpRect, [DrawTextFlags] uFormat)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lpchText", "nCount", "lpRect", "uFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawTextEx(jitter):
    """"
    [User32.dll] int DrawTextEx(HDC hdc, LPTSTR lpchText, int cchText, LPRECT lprc, [DrawTextFlags] dwDTFormat, LPDRAWTEXTPARAMS lpDTParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpchText", "cchText", "lprc", "dwDTFormat", "lpDTParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetTabbedTextExtent(jitter):
    """"
    [User32.dll] DWORD GetTabbedTextExtent(HDC hDC, LPCTSTR lpString, int nCount, int nTabPositions, const LPINT lpnTabStopPositions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lpString", "nCount", "nTabPositions", "lpnTabStopPositions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TabbedTextOut(jitter):
    """"
    [User32.dll] LONG TabbedTextOut(HDC hDC, int X, int Y, LPCTSTR lpString, int nCount, int nTabPositions, const LPINT lpnTabStopPositions, int nTabOrigin)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDC", "X", "Y", "lpString", "nCount", "nTabPositions", "lpnTabStopPositions", "nTabOrigin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CallMsgFilter(jitter):
    """"
    [User32.dll] BOOL CallMsgFilter(LPMSG lpMsg, int nCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMsg", "nCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CallNextHookEx(jitter):
    """"
    [User32.dll] LRESULT CallNextHookEx(HHOOK hhk, int nCode, WPARAM wParam, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hhk", "nCode", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowsHookEx(jitter):
    """"
    [User32.dll] HHOOK SetWindowsHookEx([WindowsHook] idHook, HOOKPROC lpfn, HINSTANCE hMod, DWORD dwThreadId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idHook", "lpfn", "hMod", "dwThreadId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnhookWindowsHookEx(jitter):
    """"
    [User32.dll] BOOL UnhookWindowsHookEx(HHOOK hhk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hhk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CopyIcon(jitter):
    """"
    [User32.dll] HICON CopyIcon(HICON hIcon)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateIcon(jitter):
    """"
    [User32.dll] HICON CreateIcon(HINSTANCE hInstance, int nWidth, int nHeight, BYTE cPlanes, BYTE cBitsPixel, const BYTE* lpbANDbits, const BYTE* lpbXORbits)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "nWidth", "nHeight", "cPlanes", "cBitsPixel", "lpbANDbits", "lpbXORbits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateIconFromResource(jitter):
    """"
    [User32.dll] HICON CreateIconFromResource(PBYTE presbits, DWORD dwResSize, BOOL fIcon, DWORD dwVer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["presbits", "dwResSize", "fIcon", "dwVer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateIconFromResourceEx(jitter):
    """"
    [User32.dll] HICON CreateIconFromResourceEx(PBYTE pbIconBits, DWORD cbIconBits, BOOL fIcon, DWORD dwVersion, int cxDesired, int cyDesired, UINT uFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pbIconBits", "cbIconBits", "fIcon", "dwVersion", "cxDesired", "cyDesired", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateIconIndirect(jitter):
    """"
    [User32.dll] HICON CreateIconIndirect(PICONINFO piconinfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["piconinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DestroyIcon(jitter):
    """"
    [User32.dll] BOOL DestroyIcon(HICON hIcon)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawIcon(jitter):
    """"
    [User32.dll] BOOL DrawIcon(HDC hDC, int X, int Y, HICON hIcon)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDC", "X", "Y", "hIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawIconEx(jitter):
    """"
    [User32.dll] BOOL DrawIconEx(HDC hdc, int xLeft, int yTop, HICON hIcon, int cxWidth, int cyWidth, UINT istepIfAniCur, HBRUSH hbrFlickerFreeDraw, [DrawIconFlags] diFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdc", "xLeft", "yTop", "hIcon", "cxWidth", "cyWidth", "istepIfAniCur", "hbrFlickerFreeDraw", "diFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetIconInfo(jitter):
    """"
    [User32.dll] BOOL GetIconInfo(HICON hIcon, PICONINFO piconinfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIcon", "piconinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetIconInfoEx(jitter):
    """"
    [User32.dll] BOOL GetIconInfoEx(HICON hIcon, PICONINFOEX piconinfoex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIcon", "piconinfoex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadIcon(jitter):
    """"
    [User32.dll] HICON LoadIcon(HINSTANCE hInstance, [LoadIconString/LPCTSTR] lpIconName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpIconName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LookupIconIdFromDirectory(jitter):
    """"
    [User32.dll] int LookupIconIdFromDirectory(PBYTE presbits, BOOL fIcon)
    """"
    ret_ad, args = jitter.func_args_stdcall(["presbits", "fIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LookupIconIdFromDirectoryEx(jitter):
    """"
    [User32.dll] int LookupIconIdFromDirectoryEx(PBYTE presbits, BOOL fIcon, int cxDesired, int cyDesired, [LRFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["presbits", "fIcon", "cxDesired", "cyDesired", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PrivateExtractIcons(jitter):
    """"
    [User32.dll] UINT PrivateExtractIcons(LPCTSTR lpszFile, int nIconIndex, int cxIcon, int cyIcon, HICON* phicon, UINT* piconid, UINT nIcons, [LRFlags] flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszFile", "nIconIndex", "cxIcon", "cyIcon", "phicon", "piconid", "nIcons", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CopyAcceleratorTable(jitter):
    """"
    [User32.dll] int CopyAcceleratorTable(HACCEL hAccelSrc, LPACCEL lpAccelDst, int cAccelEntries)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hAccelSrc", "lpAccelDst", "cAccelEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateAcceleratorTable(jitter):
    """"
    [User32.dll] HACCEL CreateAcceleratorTable(LPACCEL lpaccl, int cEntries)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpaccl", "cEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DestroyAcceleratorTable(jitter):
    """"
    [User32.dll] BOOL DestroyAcceleratorTable(HACCEL hAccel)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hAccel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadAccelerators(jitter):
    """"
    [User32.dll] HACCEL LoadAccelerators(HINSTANCE hInstance, LPCTSTR lpTableName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpTableName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TranslateAccelerator(jitter):
    """"
    [User32.dll] int TranslateAccelerator(HWND hWnd, HACCEL hAccTable, LPMSG lpMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hAccTable", "lpMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ActivateKeyboardLayout(jitter):
    """"
    [User32.dll] HKL ActivateKeyboardLayout([KeyboardLayoutHandle] hkl, [KeyboardLayoutFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkl", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BlockInput(jitter):
    """"
    [User32.dll] BOOL BlockInput(BOOL fBlockIt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fBlockIt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnableWindow(jitter):
    """"
    [User32.dll] BOOL EnableWindow(HWND hWnd, BOOL bEnable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "bEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetActiveWindow(jitter):
    """"
    [User32.dll] HWND GetActiveWindow()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetAsyncKeyState(jitter):
    """"
    [User32.dll] SHORT GetAsyncKeyState([VirtKeyCode] vKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["vKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetFocus(jitter):
    """"
    [User32.dll] HWND GetFocus()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKBCodePage(jitter):
    """"
    [User32.dll] UINT GetKBCodePage()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyboardLayout(jitter):
    """"
    [User32.dll] HKL GetKeyboardLayout(DWORD idThread)
    """"
    ret_ad, args = jitter.func_args_stdcall(["idThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyboardLayoutList(jitter):
    """"
    [User32.dll] UINT GetKeyboardLayoutList(int nBuff, HKL* lpList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nBuff", "lpList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyboardLayoutName(jitter):
    """"
    [User32.dll] BOOL GetKeyboardLayoutName(LPTSTR pwszKLID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszKLID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyboardState(jitter):
    """"
    [User32.dll] BOOL GetKeyboardState(PBYTE lpKeyState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpKeyState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyNameText(jitter):
    """"
    [User32.dll] int GetKeyNameText(LONG lParam, LPTSTR lpString, int nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lParam", "lpString", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyState(jitter):
    """"
    [User32.dll] SHORT GetKeyState([VirtKeyCode] nVirtKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nVirtKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetLastInputInfo(jitter):
    """"
    [User32.dll] BOOL GetLastInputInfo(PLASTINPUTINFO plii)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plii"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWindowEnabled(jitter):
    """"
    [User32.dll] BOOL IsWindowEnabled(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_keybd_event(jitter):
    """"
    [User32.dll] VOID keybd_event(BYTE bVk, BYTE bScan, DWORD dwFlags, ULONG_PTR dwExtraInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bVk", "bScan", "dwFlags", "dwExtraInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadKeyboardLayout(jitter):
    """"
    [User32.dll] HKL LoadKeyboardLayout(LPCTSTR pwszKLID, [KeyboardLayoutFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszKLID", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MapVirtualKey(jitter):
    """"
    [User32.dll] UINT MapVirtualKey(UINT uCode, [MapVirtualKeyType] uMapType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uCode", "uMapType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MapVirtualKeyEx(jitter):
    """"
    [User32.dll] UINT MapVirtualKeyEx(UINT uCode, [MapVirtualKeyType] uMapType, HKL dwhkl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uCode", "uMapType", "dwhkl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OemKeyScan(jitter):
    """"
    [User32.dll] DWORD OemKeyScan(WORD wOemChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["wOemChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterHotKey(jitter):
    """"
    [User32.dll] BOOL RegisterHotKey(HWND hWnd, int id, UINT fsModifiers, UINT vk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "id", "fsModifiers", "vk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SendInput(jitter):
    """"
    [User32.dll] UINT SendInput(UINT nInputs, LPINPUT pInputs, int cbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nInputs", "pInputs", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetActiveWindow(jitter):
    """"
    [User32.dll] HWND SetActiveWindow(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetFocus(jitter):
    """"
    [User32.dll] HWND SetFocus(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetKeyboardState(jitter):
    """"
    [User32.dll] BOOL SetKeyboardState(LPBYTE lpKeyState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpKeyState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ToAscii(jitter):
    """"
    [User32.dll] int ToAscii(UINT uVirtKey, UINT uScanCode, PBYTE lpKeyState, LPWORD lpChar, UINT uFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uVirtKey", "uScanCode", "lpKeyState", "lpChar", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ToAsciiEx(jitter):
    """"
    [User32.dll] int ToAsciiEx(UINT uVirtKey, UINT uScanCode, PBYTE lpKeyState, LPWORD lpChar, UINT uFlags, HKL dwhkl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uVirtKey", "uScanCode", "lpKeyState", "lpChar", "uFlags", "dwhkl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ToUnicode(jitter):
    """"
    [User32.dll] int ToUnicode(UINT wVirtKey, UINT wScanCode, const PBYTE lpKeyState, LPWSTR pwszBuff, int cchBuff, UINT wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["wVirtKey", "wScanCode", "lpKeyState", "pwszBuff", "cchBuff", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ToUnicodeEx(jitter):
    """"
    [User32.dll] int ToUnicodeEx(UINT wVirtKey, UINT wScanCode, const PBYTE lpKeyState, LPWSTR pwszBuff, int cchBuff, UINT wFlags, HKL dwhkl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["wVirtKey", "wScanCode", "lpKeyState", "pwszBuff", "cchBuff", "wFlags", "dwhkl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnloadKeyboardLayout(jitter):
    """"
    [User32.dll] BOOL UnloadKeyboardLayout(HKL hkl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnregisterHotKey(jitter):
    """"
    [User32.dll] BOOL UnregisterHotKey(HWND hWnd, int id)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_VkKeyScan(jitter):
    """"
    [User32.dll] SHORT VkKeyScan(TCHAR ch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_VkKeyScanEx(jitter):
    """"
    [User32.dll] SHORT VkKeyScanEx(TCHAR ch, HKL dwhkl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ch", "dwhkl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DlgDirList(jitter):
    """"
    [User32.dll] int DlgDirList(HWND hDlg, LPTSTR lpPathSpec, int nIDListBox, int nIDStaticPath, UINT uFileType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "lpPathSpec", "nIDListBox", "nIDStaticPath", "uFileType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DlgDirSelectEx(jitter):
    """"
    [User32.dll] BOOL DlgDirSelectEx(HWND hDlg, LPTSTR lpString, int nCount, int nIDListBox)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "lpString", "nCount", "nIDListBox"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetListBoxInfo(jitter):
    """"
    [User32.dll] DWORD GetListBoxInfo(HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AppendMenu(jitter):
    """"
    [User32.dll] BOOL AppendMenu(HMENU hMenu, UINT uFlags, UINT_PTR uIDNewItem, LPCTSTR lpNewItem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uFlags", "uIDNewItem", "lpNewItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CheckMenuItem(jitter):
    """"
    [User32.dll] DWORD CheckMenuItem(HMENU hmenu, UINT uIDCheckItem, [CheckMenuItemFlag] uCheck)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "uIDCheckItem", "uCheck"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CheckMenuRadioItem(jitter):
    """"
    [User32.dll] BOOL CheckMenuRadioItem(HMENU hmenu, UINT idFirst, UINT idLast, UINT idCheck, [MenuCommandPosFlag] uFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "idFirst", "idLast", "idCheck", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateMenu(jitter):
    """"
    [User32.dll] HMENU CreateMenu()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreatePopupMenu(jitter):
    """"
    [User32.dll] HMENU CreatePopupMenu()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DeleteMenu(jitter):
    """"
    [User32.dll] BOOL DeleteMenu(HMENU hMenu, UINT uPosition, [MenuCommandPosFlag] uFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uPosition", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DestroyMenu(jitter):
    """"
    [User32.dll] BOOL DestroyMenu(HMENU hMenu)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawMenuBar(jitter):
    """"
    [User32.dll] BOOL DrawMenuBar(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnableMenuItem(jitter):
    """"
    [User32.dll] [EnableMenuItemResult] EnableMenuItem(HMENU hMenu, UINT uIDEnableItem, [EnableMenuItemFlag] uEnable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uIDEnableItem", "uEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EndMenu(jitter):
    """"
    [User32.dll] BOOL EndMenu()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenu(jitter):
    """"
    [User32.dll] HMENU GetMenu(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuBarInfo(jitter):
    """"
    [User32.dll] BOOL GetMenuBarInfo(HWND hwnd, [ObjectIdEnum] idObject, LONG idItem, PMENUBARINFO pmbi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "idObject", "idItem", "pmbi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuCheckMarkDimensions(jitter):
    """"
    [User32.dll] LONG GetMenuCheckMarkDimensions()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuDefaultItem(jitter):
    """"
    [User32.dll] UINT GetMenuDefaultItem(HMENU hMenu, UINT fByPos, [GetMenuDefaultItemFlags] gmdiFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "fByPos", "gmdiFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuInfo(jitter):
    """"
    [User32.dll] BOOL GetMenuInfo(HMENU hmenu, LPCMENUINFO lpcmi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "lpcmi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuItemCount(jitter):
    """"
    [User32.dll] int GetMenuItemCount(HMENU hMenu)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuItemID(jitter):
    """"
    [User32.dll] UINT GetMenuItemID(HMENU hMenu, int nPos)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "nPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuItemInfo(jitter):
    """"
    [User32.dll] BOOL GetMenuItemInfo(HMENU hMenu, UINT uItem, BOOL fByPosition, LPMENUITEMINFO lpmii)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uItem", "fByPosition", "lpmii"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuItemRect(jitter):
    """"
    [User32.dll] BOOL GetMenuItemRect(HWND hWnd, HMENU hMenu, UINT uItem, LPRECT lprcItem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hMenu", "uItem", "lprcItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuState(jitter):
    """"
    [User32.dll] UINT GetMenuState(HMENU hMenu, UINT uId, [MenuCommandPosFlag] uFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uId", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuString(jitter):
    """"
    [User32.dll] int GetMenuString(HMENU hMenu, UINT uIDItem, LPTSTR lpString, int nMaxCount, UINT uFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uIDItem", "lpString", "nMaxCount", "uFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetSubMenu(jitter):
    """"
    [User32.dll] HMENU GetSubMenu(HMENU hMenu, int nPos)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "nPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetSystemMenu(jitter):
    """"
    [User32.dll] HMENU GetSystemMenu(HWND hWnd, BOOL bRevert)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "bRevert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_HiliteMenuItem(jitter):
    """"
    [User32.dll] BOOL HiliteMenuItem(HWND hwnd, HMENU hmenu, UINT uItemHilite, UINT uHilite)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hmenu", "uItemHilite", "uHilite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InsertMenu(jitter):
    """"
    [User32.dll] BOOL InsertMenu(HMENU hMenu, UINT uPosition, [InsertMenuFlags] uFlags, UINT_PTR uIDNewItem, LPCTSTR lpNewItem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uPosition", "uFlags", "uIDNewItem", "lpNewItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InsertMenuItem(jitter):
    """"
    [User32.dll] BOOL InsertMenuItem(HMENU hMenu, UINT uItem, BOOL fByPosition, LPCMENUITEMINFO lpmii)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uItem", "fByPosition", "lpmii"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsMenu(jitter):
    """"
    [User32.dll] BOOL IsMenu(HMENU hMenu)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadMenu(jitter):
    """"
    [User32.dll] HMENU LoadMenu(HINSTANCE hInstance, LPCTSTR lpMenuName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpMenuName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadMenuIndirect(jitter):
    """"
    [User32.dll] HMENU LoadMenuIndirect(CONST MENUTEMPLATE* lpMenuTemplate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMenuTemplate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MenuItemFromPoint(jitter):
    """"
    [User32.dll] int MenuItemFromPoint(HWND hWnd, HMENU hMenu, POINT ptScreen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hMenu", "ptScreen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ModifyMenu(jitter):
    """"
    [User32.dll] BOOL ModifyMenu(HMENU hMnu, UINT uPosition, UINT uFlags, UINT_PTR uIDNewItem, LPCTSTR lpNewItem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMnu", "uPosition", "uFlags", "uIDNewItem", "lpNewItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RemoveMenu(jitter):
    """"
    [User32.dll] BOOL RemoveMenu(HMENU hMenu, UINT uPosition, [MenuCommandPosFlag] uFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uPosition", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMenu(jitter):
    """"
    [User32.dll] BOOL SetMenu(HWND hWnd, HMENU hMenu)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMenuDefaultItem(jitter):
    """"
    [User32.dll] BOOL SetMenuDefaultItem(HMENU hMenu, UINT uItem, UINT fByPos)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uItem", "fByPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMenuInfo(jitter):
    """"
    [User32.dll] BOOL SetMenuInfo(HMENU hmenu, LPCMENUINFO lpcmi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "lpcmi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMenuItemBitmaps(jitter):
    """"
    [User32.dll] BOOL SetMenuItemBitmaps(HMENU hMenu, UINT uPosition, UINT uFlags, HBITMAP hBitmapUnchecked, HBITMAP hBitmapChecked)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uPosition", "uFlags", "hBitmapUnchecked", "hBitmapChecked"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMenuItemInfo(jitter):
    """"
    [User32.dll] BOOL SetMenuItemInfo(HMENU hMenu, UINT uItem, BOOL fByPosition, LPMENUITEMINFO lpmii)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uItem", "fByPosition", "lpmii"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TrackPopupMenu(jitter):
    """"
    [User32.dll] BOOL TrackPopupMenu(HMENU hMenu, [TrackPopupMenuFlags] uFlags, int x, int y, int nReserved, HWND hWnd, CONST RECT* prcRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMenu", "uFlags", "x", "y", "nReserved", "hWnd", "prcRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TrackPopupMenuEx(jitter):
    """"
    [User32.dll] BOOL TrackPopupMenuEx(HMENU hmenu, [TrackPopupMenuFlags] fuFlags, int x, int y, HWND hwnd, LPTPMPARAMS lptpm)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "fuFlags", "x", "y", "hwnd", "lptpm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DragDetect(jitter):
    """"
    [User32.dll] BOOL DragDetect(HWND hwnd, POINT pt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCapture(jitter):
    """"
    [User32.dll] HWND GetCapture()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetDoubleClickTime(jitter):
    """"
    [User32.dll] UINT GetDoubleClickTime()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMouseMovePointsEx(jitter):
    """"
    [User32.dll] int GetMouseMovePointsEx(UINT cbSize, LPMOUSEMOVEPOINT lppt, LPMOUSEMOVEPOINT lpptBuf, int nBufPoints, DWORD resolution)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cbSize", "lppt", "lpptBuf", "nBufPoints", "resolution"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_mouse_event(jitter):
    """"
    [User32.dll] VOID mouse_event(DWORD dwFlags, DWORD dx, DWORD dy, DWORD dwData, ULONG_PTR dwExtraInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "dx", "dy", "dwData", "dwExtraInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ReleaseCapture(jitter):
    """"
    [User32.dll] BOOL ReleaseCapture()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetCapture(jitter):
    """"
    [User32.dll] HWND SetCapture(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetDoubleClickTime(jitter):
    """"
    [User32.dll] BOOL SetDoubleClickTime(UINT uInterval)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uInterval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SwapMouseButton(jitter):
    """"
    [User32.dll] BOOL SwapMouseButton(BOOL fSwap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fSwap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TrackMouseEvent(jitter):
    """"
    [User32.dll] BOOL TrackMouseEvent(LPTRACKMOUSEEVENT lpEventTrack)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpEventTrack"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumDisplayMonitors(jitter):
    """"
    [User32.dll] BOOL EnumDisplayMonitors(HDC hdc, LPCRECT lprcClip, MONITORENUMPROC lpfnEnum, LPARAM dwData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lprcClip", "lpfnEnum", "dwData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMonitorInfo(jitter):
    """"
    [User32.dll] BOOL GetMonitorInfo(HMONITOR hMonitor, LPMONITORINFO lpmi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "lpmi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MonitorFromPoint(jitter):
    """"
    [User32.dll] HMONITOR MonitorFromPoint(POINT pt, [MonitorFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pt", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MonitorFromRect(jitter):
    """"
    [User32.dll] HMONITOR MonitorFromRect(LPCRECT lprc, [MonitorFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lprc", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MonitorFromWindow(jitter):
    """"
    [User32.dll] HMONITOR MonitorFromWindow(HWND hwnd, [MonitorFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateMDIWindow(jitter):
    """"
    [User32.dll] HWND CreateMDIWindow(LPCTSTR lpClassName, LPCTSTR lpWindowName, DWORD dwStyle, int X, int Y, int nWidth, int nHeight, HWND hWndParent, HINSTANCE hInstance, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpClassName", "lpWindowName", "dwStyle", "X", "Y", "nWidth", "nHeight", "hWndParent", "hInstance", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DefFrameProc(jitter):
    """"
    [User32.dll] LRESULT DefFrameProc(HWND hWnd, HWND hWndMDIClient, UINT uMsg, WPARAM wParam, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hWndMDIClient", "uMsg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DefMDIChildProc(jitter):
    """"
    [User32.dll] LRESULT DefMDIChildProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "uMsg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_TranslateMDISysAccel(jitter):
    """"
    [User32.dll] BOOL TranslateMDISysAccel(HWND hWndClient, LPMSG lpMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndClient", "lpMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BeginPaint(jitter):
    """"
    [User32.dll] HDC BeginPaint(HWND hwnd, LPPAINTSTRUCT lpPaint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpPaint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawAnimatedRects(jitter):
    """"
    [User32.dll] BOOL DrawAnimatedRects(HWND hwnd, int idAni, const RECT* lprcFrom, const RECT* lprcTo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "idAni", "lprcFrom", "lprcTo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawCaption(jitter):
    """"
    [User32.dll] BOOL DrawCaption(HWND hwnd, HDC hdc, LPCRECT lprc, UINT uFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdc", "lprc", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawEdge(jitter):
    """"
    [User32.dll] BOOL DrawEdge(HDC hdc, LPRECT qrc, [BorderEdge] edge, [BorderFlag] grfFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdc", "qrc", "edge", "grfFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawFocusRect(jitter):
    """"
    [User32.dll] BOOL DrawFocusRect(HDC hDC, const RECT* lprc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawFrameControl(jitter):
    """"
    [User32.dll] BOOL DrawFrameControl(HDC hdc, LPRECT lprc, UINT uType, UINT uState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lprc", "uType", "uState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DrawState(jitter):
    """"
    [User32.dll] BOOL DrawState(HDC hdc, HBRUSH hbr, DRAWSTATEPROC lpOutputFunc, LPARAM lData, WPARAM wData, int x, int y, int cx, int cy, [DrawStateFlags] fuFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hbr", "lpOutputFunc", "lData", "wData", "x", "y", "cx", "cy", "fuFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EndPaint(jitter):
    """"
    [User32.dll] BOOL EndPaint(HWND hWnd, const PAINTSTRUCT* lpPaint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpPaint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ExcludeUpdateRgn(jitter):
    """"
    [User32.dll] [WindowRegion] ExcludeUpdateRgn(HDC hDC, HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDC", "hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetUpdateRect(jitter):
    """"
    [User32.dll] BOOL GetUpdateRect(HWND hWnd, LPRECT lpRect, BOOL bErase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpRect", "bErase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetUpdateRgn(jitter):
    """"
    [User32.dll] [WindowRegion] GetUpdateRgn(HWND hWnd, HRGN hRgn, BOOL bErase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hRgn", "bErase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowDC(jitter):
    """"
    [User32.dll] HDC GetWindowDC(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowRgn(jitter):
    """"
    [User32.dll] [WindowRegion] GetWindowRgn(HWND hWnd, HRGN hRgn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hRgn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowRgnBox(jitter):
    """"
    [User32.dll] [WindowRegion] GetWindowRgnBox(HWND hWnd, LPRECT lprc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GrayString(jitter):
    """"
    [User32.dll] BOOL GrayString(HDC hDC, HBRUSH hBrush, GRAYSTRINGPROC lpOutputFunc, LPARAM lpData, int nCount, int X, int Y, int nWidth, int nHeight)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDC", "hBrush", "lpOutputFunc", "lpData", "nCount", "X", "Y", "nWidth", "nHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InvalidateRect(jitter):
    """"
    [User32.dll] BOOL InvalidateRect(HWND hWnd, const RECT* lpRect, BOOL bErase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpRect", "bErase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InvalidateRgn(jitter):
    """"
    [User32.dll] BOOL InvalidateRgn(HWND hWnd, HRGN hRgn, BOOL bErase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hRgn", "bErase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LockWindowUpdate(jitter):
    """"
    [User32.dll] BOOL LockWindowUpdate(HWND hWndLock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PaintDesktop(jitter):
    """"
    [User32.dll] BOOL PaintDesktop(HDC hdc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RedrawWindow(jitter):
    """"
    [User32.dll] BOOL RedrawWindow(HWND hWnd, const RECT* lprcUpdate, HRGN hrgnUpdate, [RedrawWindowFlags] flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lprcUpdate", "hrgnUpdate", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowRgn(jitter):
    """"
    [User32.dll] int SetWindowRgn(HWND hWnd, HRGN hRgn, BOOL bRedraw)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hRgn", "bRedraw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UpdateWindow(jitter):
    """"
    [User32.dll] BOOL UpdateWindow(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ValidateRect(jitter):
    """"
    [User32.dll] BOOL ValidateRect(HWND hWnd, const RECT* lpRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ValidateRgn(jitter):
    """"
    [User32.dll] BOOL ValidateRgn(HWND hWnd, HRGN hRgn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hRgn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_WindowFromDC(jitter):
    """"
    [User32.dll] HWND WindowFromDC(HDC hDC)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterPowerSettingNotification(jitter):
    """"
    [User32.dll] HPOWERNOTIFY RegisterPowerSettingNotification(HANDLE hRecipient, LPCGUID PowerSettingGuid, [DeviceNotificationFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRecipient", "PowerSettingGuid", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnregisterPowerSettingNotification(jitter):
    """"
    [User32.dll] BOOL UnregisterPowerSettingNotification(HPOWERNOTIFY Handle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PrintWindow(jitter):
    """"
    [User32.dll] BOOL PrintWindow(HWND hwnd, HDC hdcBlt, UINT nFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdcBlt", "nFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DefRawInputProc(jitter):
    """"
    [User32.dll] LRESULT DefRawInputProc(PRAWINPUT* paRawInput, INT nInput, UINT cbSizeHeader)
    """"
    ret_ad, args = jitter.func_args_stdcall(["paRawInput", "nInput", "cbSizeHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetRawInputBuffer(jitter):
    """"
    [User32.dll] UINT GetRawInputBuffer(PRAWINPUT pData, PUINT pcbSize, UINT cbSizeHeader)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pData", "pcbSize", "cbSizeHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetRawInputData(jitter):
    """"
    [User32.dll] UINT GetRawInputData(HRAWINPUT hRawInput, UINT uiCommand, LPVOID pData, PUINT pcbSize, UINT cbSizeHeader)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRawInput", "uiCommand", "pData", "pcbSize", "cbSizeHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetRawInputDeviceInfo(jitter):
    """"
    [User32.dll] UINT GetRawInputDeviceInfo(HANDLE hDevice, UINT uiCommand, LPVOID pData, PUINT pcbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDevice", "uiCommand", "pData", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetRawInputDeviceList(jitter):
    """"
    [User32.dll] UINT GetRawInputDeviceList(PRAWINPUTDEVICELIST pRawInputDeviceList, PUINT puiNumDevices, UINT cbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRawInputDeviceList", "puiNumDevices", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetRegisteredRawInputDevices(jitter):
    """"
    [User32.dll] UINT GetRegisteredRawInputDevices(PRAWINPUTDEVICE pRawInputDevices, PUINT puiNumDevices, UINT cbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRawInputDevices", "puiNumDevices", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterRawInputDevices(jitter):
    """"
    [User32.dll] BOOL RegisterRawInputDevices(PCRAWINPUTDEVICE pRawInputDevices, UINT uiNumDevices, UINT cbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRawInputDevices", "uiNumDevices", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CopyRect(jitter):
    """"
    [User32.dll] BOOL CopyRect(LPRECT lprcDst, const RECT* lprcSrc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lprcDst", "lprcSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EqualRect(jitter):
    """"
    [User32.dll] BOOL EqualRect(const RECT* lprc1, const RECT* lprc2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lprc1", "lprc2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InflateRect(jitter):
    """"
    [User32.dll] BOOL InflateRect(LPRECT lprc, int dx, int dy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lprc", "dx", "dy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IntersectRect(jitter):
    """"
    [User32.dll] BOOL IntersectRect(LPRECT lprcDst, const RECT* lprcSrc1, const RECT* lprcSrc2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lprcDst", "lprcSrc1", "lprcSrc2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsRectEmpty(jitter):
    """"
    [User32.dll] BOOL IsRectEmpty(const RECT* lprc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OffsetRect(jitter):
    """"
    [User32.dll] BOOL OffsetRect(LPRECT lprc, int dx, int dy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lprc", "dx", "dy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PtInRect(jitter):
    """"
    [User32.dll] BOOL PtInRect(const RECT* lprc, POINT pt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lprc", "pt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetRect(jitter):
    """"
    [User32.dll] BOOL SetRect(LPRECT lprc, int xLeft, int yTop, int xRight, int yBottom)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lprc", "xLeft", "yTop", "xRight", "yBottom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetRectEmpty(jitter):
    """"
    [User32.dll] BOOL SetRectEmpty(LPRECT lprc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SubtractRect(jitter):
    """"
    [User32.dll] BOOL SubtractRect(LPRECT lprcDst, const RECT* lprcSrc1, const RECT* lprcSrc2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lprcDst", "lprcSrc1", "lprcSrc2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnionRect(jitter):
    """"
    [User32.dll] BOOL UnionRect(LPRECT lprcDst, const RECT* lprcSrc1, const RECT* lprcSrc2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lprcDst", "lprcSrc1", "lprcSrc2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CopyImage(jitter):
    """"
    [User32.dll] HANDLE CopyImage(HANDLE hImage, [ImageType] uType, int cxDesired, int cyDesired, [LRFlags] fuFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hImage", "uType", "cxDesired", "cyDesired", "fuFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadImage(jitter):
    """"
    [User32.dll] HANDLE LoadImage(HINSTANCE hinst, [LoadImageString/LPCTSTR] lpszName, [ImageType] uType, int cxDesired, int cyDesired, [LRFlags] fuLoad)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hinst", "lpszName", "uType", "cxDesired", "cyDesired", "fuLoad"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnableScrollBar(jitter):
    """"
    [User32.dll] BOOL EnableScrollBar(HWND hWnd, UINT wSBflags, UINT wArrows)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "wSBflags", "wArrows"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetScrollBarInfo(jitter):
    """"
    [User32.dll] BOOL GetScrollBarInfo(HWND hwnd, [ObjectIdEnum] idObject, PSCROLLBARINFO psbi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "idObject", "psbi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetScrollInfo(jitter):
    """"
    [User32.dll] BOOL GetScrollInfo(HWND hwnd, [SBType] fnBar, LPSCROLLINFO lpsi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "fnBar", "lpsi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetScrollPos(jitter):
    """"
    [User32.dll] int GetScrollPos(HWND hWnd, [SBType] nBar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nBar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetScrollRange(jitter):
    """"
    [User32.dll] BOOL GetScrollRange(HWND hWnd, [SBType] nBar, LPINT lpMinPos, LPINT lpMaxPos)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nBar", "lpMinPos", "lpMaxPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ScrollDC(jitter):
    """"
    [User32.dll] BOOL ScrollDC(HDC hDC, int dx, int dy, const RECT* lprcScroll, const RECT* lprcClip, HRGN hrgnUpdate, LPRECT lprcUpdate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDC", "dx", "dy", "lprcScroll", "lprcClip", "hrgnUpdate", "lprcUpdate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ScrollWindow(jitter):
    """"
    [User32.dll] BOOL ScrollWindow(HWND hWnd, int XAmount, int YAmount, const RECT* lpRect, const RECT* lpClipRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "XAmount", "YAmount", "lpRect", "lpClipRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ScrollWindowEx(jitter):
    """"
    [User32.dll] int ScrollWindowEx(HWND hWnd, int dx, int dy, const RECT* prcScroll, const RECT* prcClip, HRGN hrgnUpdate, LPRECT prcUpdate, [ScrollWindowFlags] flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "dx", "dy", "prcScroll", "prcClip", "hrgnUpdate", "prcUpdate", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetScrollInfo(jitter):
    """"
    [User32.dll] int SetScrollInfo(HWND hwnd, [SBType] fnBar, LPCSCROLLINFO lpsi, BOOL fRedraw)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "fnBar", "lpsi", "fRedraw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetScrollPos(jitter):
    """"
    [User32.dll] int SetScrollPos(HWND hWnd, [SBType] nBar, int nPos, BOOL bRedraw)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nBar", "nPos", "bRedraw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetScrollRange(jitter):
    """"
    [User32.dll] BOOL SetScrollRange(HWND hWnd, [SBType] nBar, int nMinPos, int nMaxPos, BOOL bRedraw)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nBar", "nMinPos", "nMaxPos", "bRedraw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ShowScrollBar(jitter):
    """"
    [User32.dll] BOOL ShowScrollBar(HWND hWnd, [SBType] wBar, BOOL bShow)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "wBar", "bShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharLower(jitter):
    """"
    [User32.dll] LPTSTR CharLower(LPTSTR lpsz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharLowerBuff(jitter):
    """"
    [User32.dll] DWORD CharLowerBuff(LPTSTR lpsz, DWORD cchLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpsz", "cchLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharNext(jitter):
    """"
    [User32.dll] LPTSTR CharNext(LPCTSTR lpsz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharNextExA(jitter):
    """"
    [User32.dll] LPSTR CharNextExA([CodePageEnum] CodePage, LPCSTR lpCurrentChar, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CodePage", "lpCurrentChar", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharPrev(jitter):
    """"
    [User32.dll] LPTSTR CharPrev(LPCTSTR lpszStart, LPCTSTR lpszCurrent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszStart", "lpszCurrent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharPrevExA(jitter):
    """"
    [User32.dll] LPSTR CharPrevExA([CodePageEnum] CodePage, LPCSTR lpStart, LPCSTR lpCurrentChar, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CodePage", "lpStart", "lpCurrentChar", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharToOem(jitter):
    """"
    [User32.dll] BOOL CharToOem(LPCTSTR lpszSrc, LPSTR lpszDst)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszSrc", "lpszDst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharToOemBuff(jitter):
    """"
    [User32.dll] BOOL CharToOemBuff(LPCTSTR lpszSrc, LPSTR lpszDst, DWORD cchDstLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszSrc", "lpszDst", "cchDstLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharUpper(jitter):
    """"
    [User32.dll] LPTSTR CharUpper(LPTSTR lpsz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CharUpperBuff(jitter):
    """"
    [User32.dll] DWORD CharUpperBuff(LPTSTR lpsz, DWORD cchLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpsz", "cchLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsCharAlpha(jitter):
    """"
    [User32.dll] BOOL IsCharAlpha(TCHAR ch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsCharAlphaNumeric(jitter):
    """"
    [User32.dll] BOOL IsCharAlphaNumeric(TCHAR ch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsCharLower(jitter):
    """"
    [User32.dll] BOOL IsCharLower(TCHAR ch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsCharUpper(jitter):
    """"
    [User32.dll] BOOL IsCharUpper(TCHAR ch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_LoadString(jitter):
    """"
    [User32.dll] int LoadString(HINSTANCE hInstance, UINT uID, LPTSTR lpBuffer, int nBufferMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "uID", "lpBuffer", "nBufferMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OemToChar(jitter):
    """"
    [User32.dll] BOOL OemToChar(LPCSTR lpszSrc, LPTSTR lpszDst)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszSrc", "lpszDst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OemToCharBuff(jitter):
    """"
    [User32.dll] BOOL OemToCharBuff(LPCTSTR lpszSrc, LPTSTR lpszDst, DWORD cchDstLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszSrc", "lpszDst", "cchDstLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_wsprintf(jitter):
    """"
    [User32.dll] int wsprintf(LPTSTR lpOut, LPCTSTR lpFmt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpOut", "lpFmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_wvsprintf(jitter):
    """"
    [User32.dll] int wvsprintf(LPTSTR lpOutput, LPCTSTR lpFmt, va_list arglist)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpOutput", "lpFmt", "arglist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MsgWaitForMultipleObjects(jitter):
    """"
    [User32.dll] [WAIT_RESULT] MsgWaitForMultipleObjects(DWORD nCount, const HANDLE* pHandles, BOOL bWaitAll, [WaitTimeout] dwMilliseconds, [QueueStatusFlag] dwWakeMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nCount", "pHandles", "bWaitAll", "dwMilliseconds", "dwWakeMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MsgWaitForMultipleObjectsEx(jitter):
    """"
    [User32.dll] [WAIT_RESULT] MsgWaitForMultipleObjectsEx(DWORD nCount, const HANDLE* pHandles, [WaitTimeout] dwMilliseconds, [QueueStatusFlag] dwWakeMask, [MsgWaitForMultipleObjectsFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nCount", "pHandles", "dwMilliseconds", "dwWakeMask", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetKeyboardType(jitter):
    """"
    [User32.dll] int GetKeyboardType(int nTypeFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nTypeFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetSysColor(jitter):
    """"
    [User32.dll] DWORD GetSysColor([SysColorIndex] nIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetSystemMetrics(jitter):
    """"
    [User32.dll] int GetSystemMetrics([SystemMetricIndex] nIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetSysColors(jitter):
    """"
    [User32.dll] BOOL SetSysColors(int cElements, const INT* lpaElements, const COLORREF* lpaRgbValues)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cElements", "lpaElements", "lpaRgbValues"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SystemParametersInfo(jitter):
    """"
    [User32.dll] BOOL SystemParametersInfo([SystemParametersInfoEnum] uiAction, UINT uiParam, PVOID pvParam, [SystemParametersInfoFlags] fWinIni)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uiAction", "uiParam", "pvParam", "fWinIni"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_KillTimer(jitter):
    """"
    [User32.dll] BOOL KillTimer(HWND hWnd, UINT_PTR uIDEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "uIDEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetCoalescableTimer(jitter):
    """"
    [User32.dll] UINT_PTR SetCoalescableTimer(HWND hwnd, UINT_PTR nIDEvent, UINT uElapse, TIMERPROC lpTimerFunc, [TIMERV_COALESCING] uToleranceDelay)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "nIDEvent", "uElapse", "lpTimerFunc", "uToleranceDelay"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetTimer(jitter):
    """"
    [User32.dll] UINT_PTR SetTimer(HWND hWnd, UINT_PTR nIDEvent, UINT uElapse, TIMERPROC lpTimerFunc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIDEvent", "uElapse", "lpTimerFunc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClassInfo(jitter):
    """"
    [User32.dll] BOOL GetClassInfo(HINSTANCE hInstance, LPCTSTR lpClassName, LPWNDCLASS lpWndClass)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "lpClassName", "lpWndClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClassInfoEx(jitter):
    """"
    [User32.dll] BOOL GetClassInfoEx(HINSTANCE hinst, LPCTSTR lpszClass, LPWNDCLASSEX lpwcx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hinst", "lpszClass", "lpwcx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClassLong(jitter):
    """"
    [User32.dll] DWORD GetClassLong(HWND hWnd, [ClassLongIndex] nIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClassName(jitter):
    """"
    [User32.dll] int GetClassName(HWND hWnd, LPTSTR lpClassName, int nMaxCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpClassName", "nMaxCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetClassWord(jitter):
    """"
    [User32.dll] WORD GetClassWord(HWND hWnd, [ClassLongIndex] nIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowLong(jitter):
    """"
    [User32.dll] LONG GetWindowLong(HWND hWnd, [WindowLongIndex] nIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterClass(jitter):
    """"
    [User32.dll] ATOM RegisterClass(CONST WNDCLASS* lpWndClass)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpWndClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterClassEx(jitter):
    """"
    [User32.dll] ATOM RegisterClassEx(CONST WNDCLASSEX* lpwcx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwcx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetClassLong(jitter):
    """"
    [User32.dll] DWORD SetClassLong(HWND hWnd, [ClassLongIndex] nIndex, LONG dwNewLong)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIndex", "dwNewLong"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetClassWord(jitter):
    """"
    [User32.dll] WORD SetClassWord(HWND hWnd, [ClassLongIndex] nIndex, WORD wNewWord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIndex", "wNewWord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowLong(jitter):
    """"
    [User32.dll] LONG SetWindowLong(HWND hWnd, [WindowLongIndex] nIndex, LONG dwNewLong)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "nIndex", "dwNewLong"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnregisterClass(jitter):
    """"
    [User32.dll] BOOL UnregisterClass(LPCTSTR lpClassName, HINSTANCE hInstance)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpClassName", "hInstance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CallWindowProc(jitter):
    """"
    [User32.dll] LRESULT CallWindowProc(WNDPROC lpPrevWndFunc, HWND hWnd, [WinMsg] Msg, WPARAM wParam, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPrevWndFunc", "hWnd", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DefWindowProc(jitter):
    """"
    [User32.dll] LRESULT DefWindowProc(HWND hWnd, [WinMsg] Msg, WPARAM wParam, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "Msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumProps(jitter):
    """"
    [User32.dll] int EnumProps(HWND hWnd, PROPENUMPROC lpEnumFunc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpEnumFunc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumPropsEx(jitter):
    """"
    [User32.dll] int EnumPropsEx(HWND hWnd, PROPENUMPROCEX lpEnumFunc, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpEnumFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetProp(jitter):
    """"
    [User32.dll] HANDLE GetProp(HWND hWnd, LPCTSTR lpString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RemoveProp(jitter):
    """"
    [User32.dll] HANDLE RemoveProp(HWND hWnd, LPCTSTR lpString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetProp(jitter):
    """"
    [User32.dll] BOOL SetProp(HWND hWnd, LPCTSTR lpString, HANDLE hData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lpString", "hData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CloseWindowStation(jitter):
    """"
    [User32.dll] BOOL CloseWindowStation(HWINSTA hWinSta)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWinSta"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateWindowStation(jitter):
    """"
    [User32.dll] HWINSTA CreateWindowStation(LPCTSTR lpwinsta, [CreateWindowStationFlags] dwFlags, [WindowStationAccessRights] dwDesiredAccess, LPSECURITY_ATTRIBUTES lpsa)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpwinsta", "dwFlags", "dwDesiredAccess", "lpsa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumWindowStations(jitter):
    """"
    [User32.dll] BOOL EnumWindowStations(WINSTAENUMPROC lpEnumFunc, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpEnumFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetProcessWindowStation(jitter):
    """"
    [User32.dll] HWINSTA GetProcessWindowStation()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetUserObjectInformation(jitter):
    """"
    [User32.dll] BOOL GetUserObjectInformation(HANDLE hObj, [UserObjectInformationEnum] nIndex, PVOID pvInfo, DWORD nLength, LPDWORD lpnLengthNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hObj", "nIndex", "pvInfo", "nLength", "lpnLengthNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OpenWindowStation(jitter):
    """"
    [User32.dll] HWINSTA OpenWindowStation(LPTSTR lpszWinSta, BOOL fInherit, [WindowStationAccessRights] dwDesiredAccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszWinSta", "fInherit", "dwDesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetProcessWindowStation(jitter):
    """"
    [User32.dll] BOOL SetProcessWindowStation(HWINSTA hWinSta)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWinSta"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CloseDesktop(jitter):
    """"
    [User32.dll] BOOL CloseDesktop(HDESK hDesktop)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDesktop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateDesktop(jitter):
    """"
    [User32.dll] HDESK CreateDesktop(LPCTSTR lpszDesktop, LPCTSTR lpszDevice, LPDEVMODE pDevmode, [DesktopFlags] dwFlags, [DESKTOP_ACCESS_MASK] dwDesiredAccess, LPSECURITY_ATTRIBUTES lpsa)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDesktop", "lpszDevice", "pDevmode", "dwFlags", "dwDesiredAccess", "lpsa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateDesktopEx(jitter):
    """"
    [User32.dll] HDESK CreateDesktopEx(LPCTSTR lpszDesktop, LPCTSTR lpszDevice, LPDEVMODE pDevmode, [DesktopFlags] dwFlags, [DESKTOP_ACCESS_MASK] dwDesiredAccess, LPSECURITY_ATTRIBUTES lpsa, ULONG ulHeapSize, PVOID pvoid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDesktop", "lpszDevice", "pDevmode", "dwFlags", "dwDesiredAccess", "lpsa", "ulHeapSize", "pvoid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumDesktops(jitter):
    """"
    [User32.dll] BOOL EnumDesktops(HWINSTA hwinsta, DESKTOPENUMPROC lpEnumFunc, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwinsta", "lpEnumFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnumDesktopWindows(jitter):
    """"
    [User32.dll] BOOL EnumDesktopWindows(HDESK hDesktop, WNDENUMPROC lpfn, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDesktop", "lpfn", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetThreadDesktop(jitter):
    """"
    [User32.dll] HDESK GetThreadDesktop(DWORD dwThreadId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwThreadId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OpenDesktop(jitter):
    """"
    [User32.dll] HDESK OpenDesktop(LPTSTR lpszDesktop, [DesktopFlags] dwFlags, BOOL fInherit, [DESKTOP_ACCESS_MASK] dwDesiredAccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDesktop", "dwFlags", "fInherit", "dwDesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_OpenInputDesktop(jitter):
    """"
    [User32.dll] HDESK OpenInputDesktop([DesktopFlags] dwFlags, BOOL fInherit, [DESKTOP_ACCESS_MASK] dwDesiredAccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "fInherit", "dwDesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetThreadDesktop(jitter):
    """"
    [User32.dll] BOOL SetThreadDesktop(HDESK hDesktop)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDesktop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetUserObjectInformation(jitter):
    """"
    [User32.dll] BOOL SetUserObjectInformation(HANDLE hObj, [UserObjectInformationEnum] nIndex, PVOID pvInfo, DWORD nLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hObj", "nIndex", "pvInfo", "nLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SwitchDesktop(jitter):
    """"
    [User32.dll] BOOL SwitchDesktop(HDESK hDesktop)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDesktop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMenuContextHelpId(jitter):
    """"
    [User32.dll] DWORD GetMenuContextHelpId(HMENU hmenu)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowContextHelpId(jitter):
    """"
    [User32.dll] DWORD GetWindowContextHelpId(HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMenuContextHelpId(jitter):
    """"
    [User32.dll] BOOL SetMenuContextHelpId(HMENU hmenu, DWORD dwContextHelpId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "dwContextHelpId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowContextHelpId(jitter):
    """"
    [User32.dll] BOOL SetWindowContextHelpId(HWND hwnd, DWORD dwContextHelpId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwContextHelpId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_WinHelp(jitter):
    """"
    [User32.dll] BOOL WinHelp(HWND hWndMain, LPCTSTR lpszHelp, UINT uCommand, ULONG_PTR dwData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndMain", "lpszHelp", "uCommand", "dwData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetUserObjectSecurity(jitter):
    """"
    [User32.dll] BOOL GetUserObjectSecurity(HANDLE hObj, PSECURITY_INFORMATION pSIRequested, PSECURITY_DESCRIPTOR pSD, DWORD nLength, LPDWORD lpnLengthNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hObj", "pSIRequested", "pSD", "nLength", "lpnLengthNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetUserObjectSecurity(jitter):
    """"
    [User32.dll] BOOL SetUserObjectSecurity(HANDLE hObj, PSECURITY_INFORMATION pSIRequested, PSECURITY_DESCRIPTOR pSID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hObj", "pSIRequested", "pSID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWinEventHook(jitter):
    """"
    [User32.dll] HWINEVENTHOOK SetWinEventHook(UINT eventMin, UINT eventMax, HMODULE hmodWinEventProc, WINEVENTPROC lpfnWinEventProc, DWORD idProcess, DWORD idThread, [WinEventFlags] dwflags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["eventMin", "eventMax", "hmodWinEventProc", "lpfnWinEventProc", "idProcess", "idThread", "dwflags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnhookWinEvent(jitter):
    """"
    [User32.dll] BOOL UnhookWinEvent(HWINEVENTHOOK hWinEventHook)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWinEventHook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWinEventHookInstalled(jitter):
    """"
    [User32.dll] BOOL IsWinEventHookInstalled(DWORD event)
    """"
    ret_ad, args = jitter.func_args_stdcall(["event"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_NotifyWinEvent(jitter):
    """"
    [User32.dll] void NotifyWinEvent(DWORD event, HWND hwnd, [ObjectIdEnum] idObject, LONG idChild)
    """"
    ret_ad, args = jitter.func_args_stdcall(["event", "hwnd", "idObject", "idChild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CloseTouchInputHandle(jitter):
    """"
    [User32.dll] BOOL CloseTouchInputHandle(HTOUCHINPUT hTouchInput)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTouchInput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetTouchInputInfo(jitter):
    """"
    [User32.dll] BOOL GetTouchInputInfo(HTOUCHINPUT hTouchInput, UINT cInputs, PTOUCHINPUT pInputs, int cbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTouchInput", "cInputs", "pInputs", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsTouchWindow(jitter):
    """"
    [User32.dll] BOOL IsTouchWindow(HWND hWnd, PULONG pulFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterTouchWindow(jitter):
    """"
    [User32.dll] BOOL RegisterTouchWindow(HWND hWnd, ULONG ulFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnregisterTouchWindow(jitter):
    """"
    [User32.dll] BOOL UnregisterTouchWindow(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CloseGestureInfoHandle(jitter):
    """"
    [User32.dll] BOOL CloseGestureInfoHandle(HGESTUREINFO hGestureInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hGestureInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetGestureExtraArgs(jitter):
    """"
    [User32.dll] BOOL GetGestureExtraArgs(HGESTUREINFO hGestureInfo, UINT cbExtraArgs, PBYTE pExtraArgs)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hGestureInfo", "cbExtraArgs", "pExtraArgs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetGestureInfo(jitter):
    """"
    [User32.dll] BOOL GetGestureInfo(HGESTUREINFO hGestureInfo, PGESTUREINFO pGestureInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hGestureInfo", "pGestureInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetGestureConfig(jitter):
    """"
    [User32.dll] BOOL GetGestureConfig(HWND hwnd, DWORD dwReserved, DWORD dwFlags, PUINT pcIDs, PGESTURECONFIG pGestureConfig, UINT cbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwReserved", "dwFlags", "pcIDs", "pGestureConfig", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetGestureConfig(jitter):
    """"
    [User32.dll] BOOL SetGestureConfig(HWND hwnd, DWORD dwReserved, UINT cIDs, PGESTURECONFIG pGestureConfig, UINT cbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwReserved", "cIDs", "pGestureConfig", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DesktopHasWatermarkText(jitter):
    """"
    [User32.dll] BOOL DesktopHasWatermarkText()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_FrostCrashedWindow(jitter):
    """"
    [User32.dll] HWND FrostCrashedWindow(HWND hwndToReplace, HWND hwndErrorReportOwnerWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndToReplace", "hwndErrorReportOwnerWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetSendMessageReceiver(jitter):
    """"
    [User32.dll] HWND GetSendMessageReceiver(DWORD threadId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["threadId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowCompositionAttribute(jitter):
    """"
    [User32.dll] BOOL GetWindowCompositionAttribute(HWND hwnd, WINCOMPATTRDATA* pAttrData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pAttrData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowMinimizeRect(jitter):
    """"
    [User32.dll] BOOL GetWindowMinimizeRect(HWND hwndToQuery, RECT* pRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndToQuery", "pRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GhostWindowFromHungWindow(jitter):
    """"
    [User32.dll] HWND GhostWindowFromHungWindow(HWND hwndGhost)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndGhost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_HungWindowFromGhostWindow(jitter):
    """"
    [User32.dll] HWND HungWindowFromGhostWindow(HWND hwndGhost)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndGhost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsSETEnabled(jitter):
    """"
    [User32.dll] BOOL IsSETEnabled()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsServerSideWindow(jitter):
    """"
    [User32.dll] BOOL IsServerSideWindow(HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsThreadDesktopComposited(jitter):
    """"
    [User32.dll] BOOL IsThreadDesktopComposited()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsWindowInDestroy(jitter):
    """"
    [User32.dll] BOOL IsWindowInDestroy(HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_MB_GetString(jitter):
    """"
    [User32.dll] LPCWSTR MB_GetString(int strId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["strId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_NtUserSetChildWindowNoActivate(jitter):
    """"
    [User32.dll] BOOL NtUserSetChildWindowNoActivate(HWND hwndChild)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndChild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_QuerySendMessage(jitter):
    """"
    [User32.dll] BOOL QuerySendMessage(MSG* pMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowCompositionAttribute(jitter):
    """"
    [User32.dll] BOOL SetWindowCompositionAttribute(HWND hwnd, WINCOMPATTRDATA* pAttrData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pAttrData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UpdateWindowTransform(jitter):
    """"
    [User32.dll] BOOL UpdateWindowTransform(HWND hwnd, D3DMATRIX* pMatrix, DWORD unk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pMatrix", "unk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InitializeTouchInjection(jitter):
    """"
    [User32.dll] BOOL InitializeTouchInjection(UINT32 maxCount, [TOUCH_FEEDBACK_MODE] dwMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["maxCount", "dwMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_InjectTouchInput(jitter):
    """"
    [User32.dll] BOOL InjectTouchInput(UINT32 count, const POINTER_TOUCH_INFO* contacts)
    """"
    ret_ad, args = jitter.func_args_stdcall(["count", "contacts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_AddPointerInteractionContext(jitter):
    """"
    [User32.dll] HRESULT AddPointerInteractionContext(HINTERACTIONCONTEXT interactionContext, UINT32 pointerId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "pointerId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_BufferPointerPacketsInteractionContext(jitter):
    """"
    [User32.dll] HRESULT BufferPointerPacketsInteractionContext(HINTERACTIONCONTEXT interactionContext, UINT32 entriesCount, const POINTER_INFO* pointerInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "entriesCount", "pointerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_CreateInteractionContext(jitter):
    """"
    [User32.dll] HRESULT CreateInteractionContext(HINTERACTIONCONTEXT* interactionContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_DestroyInteractionContext(jitter):
    """"
    [User32.dll] HRESULT DestroyInteractionContext(HINTERACTIONCONTEXT interactionContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCrossSlideParameterInteractionContext(jitter):
    """"
    [User32.dll] HRESULT GetCrossSlideParameterInteractionContext(HINTERACTIONCONTEXT interactionContext, CROSS_SLIDE_THRESHOLD threshold, float* distance)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "threshold", "distance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetInertiaParameterInteractionContext(jitter):
    """"
    [User32.dll] HRESULT GetInertiaParameterInteractionContext(HINTERACTIONCONTEXT interactionContext, INERTIA_PARAMETER inertiaParameter, float* value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "inertiaParameter", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetInteractionConfigurationInteractionContext(jitter):
    """"
    [User32.dll] HRESULT GetInteractionConfigurationInteractionContext(HINTERACTIONCONTEXT interactionContext, UINT32 configurationCount, INTERACTION_CONTEXT_CONFIGURATION* configuration)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "configurationCount", "configuration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetMouseWheelParameterInteractionContext(jitter):
    """"
    [User32.dll] HRESULT GetMouseWheelParameterInteractionContext(HINTERACTIONCONTEXT interactionContext, MOUSE_WHEEL_PARAMETER parameter, float* value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "parameter", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPropertyInteractionContext(jitter):
    """"
    [User32.dll] HRESULT GetPropertyInteractionContext(HINTERACTIONCONTEXT interactionContext, INTERACTION_CONTEXT_PROPERTY contextProperty, UINT32* value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "contextProperty", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetStateInteractionContext(jitter):
    """"
    [User32.dll] HRESULT GetStateInteractionContext(HINTERACTIONCONTEXT interactionContext, const POINTER_INFO* pointerInfo, INTERACTION_STATE* state)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "pointerInfo", "state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ProcessBufferedPacketsInteractionContext(jitter):
    """"
    [User32.dll] HRESULT ProcessBufferedPacketsInteractionContext(HINTERACTIONCONTEXT interactionContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ProcessInertiaInteractionContext(jitter):
    """"
    [User32.dll] HRESULT ProcessInertiaInteractionContext(HINTERACTIONCONTEXT interactionContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ProcessPointerFramesInteractionContext(jitter):
    """"
    [User32.dll] HRESULT ProcessPointerFramesInteractionContext(HINTERACTIONCONTEXT interactionContext, UINT32 entriesCount, UINT32 pointerCount, const POINTER_INFO* pointerInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "entriesCount", "pointerCount", "pointerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterOutputCallbackInteractionContext(jitter):
    """"
    [User32.dll] HRESULT RegisterOutputCallbackInteractionContext(HINTERACTIONCONTEXT interactionContext, INTERACTION_CONTEXT_OUTPUT_CALLBACK outputCallback, void* clientData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "outputCallback", "clientData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RemovePointerInteractionContext(jitter):
    """"
    [User32.dll] HRESULT RemovePointerInteractionContext(HINTERACTIONCONTEXT interactionContext, UINT32 pointerId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "pointerId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_ResetInteractionContext(jitter):
    """"
    [User32.dll] HRESULT ResetInteractionContext(HINTERACTIONCONTEXT interactionContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetCrossSlideParametersInteractionContext(jitter):
    """"
    [User32.dll] HRESULT SetCrossSlideParametersInteractionContext(HINTERACTIONCONTEXT interactionContext, UINT32 parameterCount, CROSS_SLIDE_PARAMETER* crossSlideParameters)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "parameterCount", "crossSlideParameters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetInertiaParameterInteractionContext(jitter):
    """"
    [User32.dll] HRESULT SetInertiaParameterInteractionContext(HINTERACTIONCONTEXT interactionContext, INERTIA_PARAMETER inertiaParameter, float value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "inertiaParameter", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetInteractionConfigurationInteractionContext(jitter):
    """"
    [User32.dll] HRESULT SetInteractionConfigurationInteractionContext(HINTERACTIONCONTEXT interactionContext, UINT32 configurationCount, const INTERACTION_CONTEXT_CONFIGURATION* configuration)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "configurationCount", "configuration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetMouseWheelParameterInteractionContext(jitter):
    """"
    [User32.dll] HRESULT SetMouseWheelParameterInteractionContext(HINTERACTIONCONTEXT interactionContext, MOUSE_WHEEL_PARAMETER parameter, float value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "parameter", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetPivotInteractionContext(jitter):
    """"
    [User32.dll] HRESULT SetPivotInteractionContext(HINTERACTIONCONTEXT interactionContext, float x, float y, float radius)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "x", "y", "radius"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetPropertyInteractionContext(jitter):
    """"
    [User32.dll] HRESULT SetPropertyInteractionContext(HINTERACTIONCONTEXT interactionContext, INTERACTION_CONTEXT_PROPERTY contextProperty, UINT32 value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext", "contextProperty", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_StopInteractionContext(jitter):
    """"
    [User32.dll] HRESULT StopInteractionContext(HINTERACTIONCONTEXT interactionContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["interactionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EnableMouseInPointer(jitter):
    """"
    [User32.dll] BOOL EnableMouseInPointer(BOOL fEnable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerCursorId(jitter):
    """"
    [User32.dll] BOOL GetPointerCursorId(UINT32 pointerId, UINT32* cursorId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "cursorId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerFrameInfo(jitter):
    """"
    [User32.dll] BOOL GetPointerFrameInfo(UINT32 pointerId, UINT32* pointerCount, POINTER_INFO* pointerInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "pointerCount", "pointerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerFrameInfoHistory(jitter):
    """"
    [User32.dll] BOOL GetPointerFrameInfoHistory(UINT32 pointerId, UINT32* entriesCount, UINT32* pointerCount, POINTER_INFO* pointerInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "entriesCount", "pointerCount", "pointerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerFramePenInfo(jitter):
    """"
    [User32.dll] BOOL GetPointerFramePenInfo(UINT32 pointerId, UINT32* pointerCount, POINTER_PEN_INFO* penInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "pointerCount", "penInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerFramePenInfoHistory(jitter):
    """"
    [User32.dll] BOOL GetPointerFramePenInfoHistory(UINT32 pointerId, UINT32* entriesCount, UINT32* pointerCount, POINTER_PEN_INFO* penInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "entriesCount", "pointerCount", "penInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerFrameTouchInfo(jitter):
    """"
    [User32.dll] BOOL GetPointerFrameTouchInfo(UINT32 pointerId, UINT32* pointerCount, POINTER_TOUCH_INFO* touchInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "pointerCount", "touchInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerFrameTouchInfoHistory(jitter):
    """"
    [User32.dll] BOOL GetPointerFrameTouchInfoHistory(UINT32 pointerId, UINT32* entriesCount, UINT32* pointerCount, POINTER_TOUCH_INFO* touchInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "entriesCount", "pointerCount", "touchInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerInfo(jitter):
    """"
    [User32.dll] BOOL GetPointerInfo(UINT32 pointerId, POINTER_INFO* pointerInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "pointerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerInfoHistory(jitter):
    """"
    [User32.dll] BOOL GetPointerInfoHistory(UINT32 pointerId, UINT32* entriesCount, POINTER_INFO* pointerInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "entriesCount", "pointerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerPenInfo(jitter):
    """"
    [User32.dll] BOOL GetPointerPenInfo(UINT32 pointerId, POINTER_PEN_INFO* penInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "penInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerPenInfoHistory(jitter):
    """"
    [User32.dll] BOOL GetPointerPenInfoHistory(UINT32 pointerId, UINT32* entriesCount, POINTER_PEN_INFO* penInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "entriesCount", "penInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerTouchInfo(jitter):
    """"
    [User32.dll] BOOL GetPointerTouchInfo(UINT32 pointerId, POINTER_TOUCH_INFO* touchInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "touchInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerTouchInfoHistory(jitter):
    """"
    [User32.dll] BOOL GetPointerTouchInfoHistory(UINT32 pointerId, UINT32* entriesCount, POINTER_TOUCH_INFO* touchInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "entriesCount", "touchInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerType(jitter):
    """"
    [User32.dll] BOOL GetPointerType(UINT32 pointerId, POINTER_INPUT_TYPE* pointerType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "pointerType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetUnpredictedMessagePos(jitter):
    """"
    [User32.dll] DWORD GetUnpredictedMessagePos()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_IsMouseInPointerEnabled(jitter):
    """"
    [User32.dll] BOOL IsMouseInPointerEnabled()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SkipPointerFrameMessages(jitter):
    """"
    [User32.dll] BOOL SkipPointerFrameMessages(UINT32 pointerId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EvaluateProximityToPolygon(jitter):
    """"
    [User32.dll] BOOL EvaluateProximityToPolygon(UINT32 numVertices, const POINT* controlPolygon, const TOUCH_HIT_TESTING_INPUT* pHitTestingInput, TOUCH_HIT_TESTING_PROXIMITY_EVALUATION* pProximityEval)
    """"
    ret_ad, args = jitter.func_args_stdcall(["numVertices", "controlPolygon", "pHitTestingInput", "pProximityEval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_EvaluateProximityToRect(jitter):
    """"
    [User32.dll] BOOL EvaluateProximityToRect(const RECT* controlBoundingBox, const TOUCH_HIT_TESTING_INPUT* pHitTestingInput, TOUCH_HIT_TESTING_PROXIMITY_EVALUATION* pProximityEval)
    """"
    ret_ad, args = jitter.func_args_stdcall(["controlBoundingBox", "pHitTestingInput", "pProximityEval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_PackTouchHitTestingProximityEvaluation(jitter):
    """"
    [User32.dll] LRESULT PackTouchHitTestingProximityEvaluation(const TOUCH_HIT_TESTING_INPUT* pHitTestingInput, const TOUCH_HIT_TESTING_PROXIMITY_EVALUATION* pProximityEval)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pHitTestingInput", "pProximityEval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterTouchHitTestingWindow(jitter):
    """"
    [User32.dll] BOOL RegisterTouchHitTestingWindow(HWND hwnd, ULONG value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCIMSSM(jitter):
    """"
    [User32.dll] BOOL GetCIMSSM(INPUT_MESSAGE_SOURCE* inputMessageSource)
    """"
    ret_ad, args = jitter.func_args_stdcall(["inputMessageSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetCurrentInputMessageSource(jitter):
    """"
    [User32.dll] BOOL GetCurrentInputMessageSource(INPUT_MESSAGE_SOURCE* inputMessageSource)
    """"
    ret_ad, args = jitter.func_args_stdcall(["inputMessageSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerDevice(jitter):
    """"
    [User32.dll] BOOL GetPointerDevice(HANDLE device, POINTER_DEVICE_INFO* pointerDevice)
    """"
    ret_ad, args = jitter.func_args_stdcall(["device", "pointerDevice"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerDeviceCursors(jitter):
    """"
    [User32.dll] BOOL GetPointerDeviceCursors(HANDLE device, UINT32* cursorCount, POINTER_DEVICE_CURSOR_INFO* deviceCursors)
    """"
    ret_ad, args = jitter.func_args_stdcall(["device", "cursorCount", "deviceCursors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerDeviceProperties(jitter):
    """"
    [User32.dll] BOOL GetPointerDeviceProperties(HANDLE device, UINT32* propertyCount, POINTER_DEVICE_PROPERTY* pointerProperties)
    """"
    ret_ad, args = jitter.func_args_stdcall(["device", "propertyCount", "pointerProperties"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerDeviceRects(jitter):
    """"
    [User32.dll] BOOL GetPointerDeviceRects(HANDLE device, RECT* pointerDeviceRect, RECT* displayRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["device", "pointerDeviceRect", "displayRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetPointerDevices(jitter):
    """"
    [User32.dll] BOOL GetPointerDevices(UINT32 deviceCount, POINTER_DEVICE_INFO* pointerDevices)
    """"
    ret_ad, args = jitter.func_args_stdcall(["deviceCount", "pointerDevices"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetRawPointerDeviceData(jitter):
    """"
    [User32.dll] BOOL GetRawPointerDeviceData(UINT32 pointerId, UINT32 historyCount, UINT32 propertiesCount, POINTER_DEVICE_PROPERTY* pProperties, LONG* pValues)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pointerId", "historyCount", "propertiesCount", "pProperties", "pValues"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterPointerDeviceNotifications(jitter):
    """"
    [User32.dll] BOOL RegisterPointerDeviceNotifications(HWND window, BOOL notifyRange)
    """"
    ret_ad, args = jitter.func_args_stdcall(["window", "notifyRange"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_RegisterSuspendResumeNotification(jitter):
    """"
    [User32.dll] HPOWERNOTIFY RegisterSuspendResumeNotification(PDEVICE_NOTIFY_SUBSCRIBE_PARAMETERS hRecipient, [POWER_NOTIFICATION_FLAGS] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRecipient", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_UnregisterSuspendResumeNotification(jitter):
    """"
    [User32.dll] BOOL UnregisterSuspendResumeNotification(HPOWERNOTIFY RegistrationHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegistrationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_GetWindowFeedbackSetting(jitter):
    """"
    [User32.dll] BOOL GetWindowFeedbackSetting(HWND hwnd, FEEDBACK_TYPE feedback, [GWFS_FLAGS] dwFlags, UINT32* pSize, VOID* config)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "feedback", "dwFlags", "pSize", "config"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def user32_SetWindowFeedbackSetting(jitter):
    """"
    [User32.dll] BOOL SetWindowFeedbackSetting(HWND hwnd, FEEDBACK_TYPE feedback, DWORD dwFlags, UINT32 size, const VOID* configuration)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "feedback", "dwFlags", "size", "configuration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
