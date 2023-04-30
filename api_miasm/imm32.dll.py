_IME_CAND_ = {
    "IME_CAND_UNKNOWN": 0x0000,
    "IME_CAND_READ": 0x0001,
    "IME_CAND_CODE": 0x0002,
    "IME_CAND_MEANING": 0x0003,
    "IME_CAND_RADICAL": 0x0004,
    "IME_CAND_STROKE": 0x0005,
}
_ImmNotifyAction_ = {
    "NI_OPENCANDIDATE": 0x0010,
    "NI_CLOSECANDIDATE": 0x0011,
    "NI_SELECTCANDIDATESTR": 0x0012,
    "NI_CHANGECANDIDATELIST": 0x0013,
    "NI_FINALIZECONVERSIONRESULT": 0x0014,
    "NI_COMPOSITIONSTR": 0x0015,
    "NI_SETCANDIDATE_PAGESTART": 0x0016,
    "NI_SETCANDIDATE_PAGESIZE": 0x0017,
    "NI_IMEMENUSELECTED": 0x0018,
}
_CompositionString_ = {
    "CPS_COMPLETE": 0x0001,
    "CPS_CONVERT": 0x0002,
    "CPS_REVERT": 0x0003,
    "CPS_CANCEL": 0x0004,
}
_ImmGetPropertyIndex_ = {
    "IGP_GETIMEVERSION": -4,
    "IGP_PROPERTY": 0x00000004,
    "IGP_CONVERSION": 0x00000008,
    "IGP_SENTENCE": 0x0000000c,
    "IGP_UI": 0x00000010,
    "IGP_SETCOMPSTR": 0x00000014,
    "IGP_SELECT": 0x00000018,
}

def imm32_ImmAssociateContext(jitter):
    """
    HIMC ImmAssociateContext(
        HWND hWnd,
        HIMC hIMC
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hIMC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmAssociateContextEx(jitter):
    """
    BOOL ImmAssociateContextEx(
        HWND hWnd,
        HIMC hIMC,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hIMC", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmConfigureIME(jitter, get_str, set_str):
    """
    BOOL ImmConfigureIME(
        HKL hKL,
        HWND hWnd,
        DWORD dwMode,
        LPVOID lpData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKL", "hWnd", "dwMode", "lpData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmConfigureIMEA(jitter):
    imm32_ImmConfigureIME(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmConfigureIMEW(jitter):
    imm32_ImmConfigureIME(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmCreateContext(jitter):
    """
    HIMC ImmCreateContext()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmDestroyContext(jitter):
    """
    BOOL ImmDestroyContext(
        HIMC hIMC
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmDisableIME(jitter):
    """
    BOOL ImmDisableIME(
        DWORD idThread
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmDisableTextFrameService(jitter):
    """
    BOOL ImmDisableTextFrameService(
        DWORD idThread
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmEnumInputContext(jitter):
    """
    BOOL ImmEnumInputContext(
        DWORD idThread,
        IMCENUMPROC lpfn,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["idThread", "lpfn", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmEnumRegisterWord(jitter, get_str, set_str):
    """
    UINT ImmEnumRegisterWord(
        HKL hKL,
        REGISTERWORDENUMPROC lpfnEnumProc,
        LPCTSTR lpszReading,
        DWORD dwStyle,
        LPCTSTR lpszRegister,
        LPVOID lpData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKL", "lpfnEnumProc", "lpszReading", "dwStyle", "lpszRegister", "lpData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmEnumRegisterWordA(jitter):
    imm32_ImmEnumRegisterWord(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmEnumRegisterWordW(jitter):
    imm32_ImmEnumRegisterWord(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmEscape(jitter, get_str, set_str):
    """
    LRESULT ImmEscape(
        HKL hKL,
        HIMC hIMC,
        UINT uEscape,
        LPVOID lpData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKL", "hIMC", "uEscape", "lpData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmEscapeA(jitter):
    imm32_ImmEscape(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmEscapeW(jitter):
    imm32_ImmEscape(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmGetCandidateList(jitter, get_str, set_str):
    """
    DWORD ImmGetCandidateList(
        HIMC hIMC,
        DWORD dwIndex,
        LPCANDIDATELIST lpCandList,
        DWORD dwBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "dwIndex", "lpCandList", "dwBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetCandidateListA(jitter):
    imm32_ImmGetCandidateList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmGetCandidateListW(jitter):
    imm32_ImmGetCandidateList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmGetCandidateListCount(jitter, get_str, set_str):
    """
    DWORD ImmGetCandidateListCount(
        HIMC hIMC,
        LPDWORD lpdwListCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "lpdwListCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetCandidateListCountA(jitter):
    imm32_ImmGetCandidateListCount(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmGetCandidateListCountW(jitter):
    imm32_ImmGetCandidateListCount(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmGetCandidateWindow(jitter):
    """
    BOOL ImmGetCandidateWindow(
        HIMC hIMC,
        DWORD dwIndex,
        LPCANDIDATEFORM lpCandidate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "dwIndex", "lpCandidate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetCompositionFont(jitter, get_str, set_str):
    """
    BOOL ImmGetCompositionFont(
        HIMC hIMC,
        LPLOGFONT lplf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "lplf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetCompositionFontA(jitter):
    imm32_ImmGetCompositionFont(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmGetCompositionFontW(jitter):
    imm32_ImmGetCompositionFont(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmGetCompositionString(jitter, get_str, set_str):
    """
    LONG ImmGetCompositionString(
        HIMC hIMC,
        DWORD dwIndex,
        LPVOID lpBuf,
        DWORD dwBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "dwIndex", "lpBuf", "dwBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetCompositionStringA(jitter):
    imm32_ImmGetCompositionString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmGetCompositionStringW(jitter):
    imm32_ImmGetCompositionString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmGetCompositionWindow(jitter):
    """
    BOOL ImmGetCompositionWindow(
        HIMC hIMC,
        LPCOMPOSITIONFORM lpCompForm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "lpCompForm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetContext(jitter):
    """
    HIMC ImmGetContext(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetConversionList(jitter, get_str, set_str):
    """
    DWORD ImmGetConversionList(
        HKL hKL,
        HIMC hIMC,
        LPCTSTR lpSrc,
        LPCANDIDATELIST lpDst,
        DWORD dwBufLen,
        UINT uFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKL", "hIMC", "lpSrc", "lpDst", "dwBufLen", "uFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetConversionListA(jitter):
    imm32_ImmGetConversionList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmGetConversionListW(jitter):
    imm32_ImmGetConversionList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmGetConversionStatus(jitter):
    """
    BOOL ImmGetConversionStatus(
        HIMC hIMC,
        LPDWORD lpfdwConversion,
        LPDWORD lpfdwSentence
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "lpfdwConversion", "lpfdwSentence"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetDefaultIMEWnd(jitter):
    """
    HWND ImmGetDefaultIMEWnd(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetDescription(jitter, get_str, set_str):
    """
    UINT ImmGetDescription(
        HKL hKL,
        LPTSTR lpszDescription,
        UINT uBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKL", "lpszDescription", "uBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetDescriptionA(jitter):
    imm32_ImmGetDescription(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmGetDescriptionW(jitter):
    imm32_ImmGetDescription(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmGetGuideLine(jitter, get_str, set_str):
    """
    DWORD ImmGetGuideLine(
        HIMC hIMC,
        DWORD dwIndex,
        LPTSTR lpBuf,
        DWORD dwBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "dwIndex", "lpBuf", "dwBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetGuideLineA(jitter):
    imm32_ImmGetGuideLine(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmGetGuideLineW(jitter):
    imm32_ImmGetGuideLine(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmGetIMEFileName(jitter, get_str, set_str):
    """
    UINT ImmGetIMEFileName(
        HKL hKL,
        LPTSTR lpszFileName,
        UINT uBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKL", "lpszFileName", "uBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetIMEFileNameA(jitter):
    imm32_ImmGetIMEFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmGetIMEFileNameW(jitter):
    imm32_ImmGetIMEFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmGetImeMenuItems(jitter, get_str, set_str):
    """
    DWORD ImmGetImeMenuItems(
        HIMC hIMC,
        DWORD dwFlags,
        DWORD dwType,
        LPIMEMENUITEMINFO lpImeParentMenu,
        LPIMEMENUITEMINFO lpImeMenu,
        DWORD dwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "dwFlags", "dwType", "lpImeParentMenu", "lpImeMenu", "dwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetImeMenuItemsA(jitter):
    imm32_ImmGetImeMenuItems(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmGetImeMenuItemsW(jitter):
    imm32_ImmGetImeMenuItems(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmGetOpenStatus(jitter):
    """
    BOOL ImmGetOpenStatus(
        HIMC hIMC
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetProperty(jitter):
    """
    DWORD ImmGetProperty(
        HKL hKL,
        [ImmGetPropertyIndex] fdwIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKL", "fdwIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetRegisterWordStyle(jitter, get_str, set_str):
    """
    UINT ImmGetRegisterWordStyle(
        HKL hKL,
        UINT nItem,
        LPSTYLEBUF lpStyleBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKL", "nItem", "lpStyleBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetRegisterWordStyleA(jitter):
    imm32_ImmGetRegisterWordStyle(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmGetRegisterWordStyleW(jitter):
    imm32_ImmGetRegisterWordStyle(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmGetStatusWindowPos(jitter):
    """
    BOOL ImmGetStatusWindowPos(
        HIMC hIMC,
        LPPOINT lpptPos
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "lpptPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmGetVirtualKey(jitter):
    """
    UINT ImmGetVirtualKey(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmInstallIME(jitter, get_str, set_str):
    """
    HKL ImmInstallIME(
        LPCTSTR lpszIMEFileName,
        LPCTSTR lpszLayoutText
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszIMEFileName", "lpszLayoutText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmInstallIMEA(jitter):
    imm32_ImmInstallIME(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmInstallIMEW(jitter):
    imm32_ImmInstallIME(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmIsIME(jitter):
    """
    BOOL ImmIsIME(
        HKL hKL
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmIsUIMessage(jitter, get_str, set_str):
    """
    BOOL ImmIsUIMessage(
        HWND hWndIME,
        UINT msg,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndIME", "msg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmIsUIMessageA(jitter):
    imm32_ImmIsUIMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmIsUIMessageW(jitter):
    imm32_ImmIsUIMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmNotifyIME(jitter):
    """
    BOOL ImmNotifyIME(
        HIMC hIMC,
        [ImmNotifyAction] dwAction,
        [CompositionString] dwIndex,
        DWORD dwValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "dwAction", "dwIndex", "dwValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmRegisterWord(jitter, get_str, set_str):
    """
    BOOL ImmRegisterWord(
        HKL hKL,
        LPCTSTR lpszReading,
        DWORD dwStyle,
        LPCTSTR lpszRegister
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKL", "lpszReading", "dwStyle", "lpszRegister"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmRegisterWordA(jitter):
    imm32_ImmRegisterWord(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmRegisterWordW(jitter):
    imm32_ImmRegisterWord(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmReleaseContext(jitter):
    """
    BOOL ImmReleaseContext(
        HWND hWnd,
        HIMC hIMC
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hIMC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmRequestMessage(jitter, get_str, set_str):
    """
    LRESULT ImmRequestMessage(
        HIMC hIMC,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmRequestMessageA(jitter):
    imm32_ImmRequestMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmRequestMessageW(jitter):
    imm32_ImmRequestMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmSetCandidateWindow(jitter):
    """
    BOOL ImmSetCandidateWindow(
        HIMC hIMC,
        LPCANDIDATEFORM lpCandidate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "lpCandidate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmSetCompositionFont(jitter, get_str, set_str):
    """
    BOOL ImmSetCompositionFont(
        HIMC hIMC,
        LPLOGFONT lplf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "lplf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmSetCompositionFontA(jitter):
    imm32_ImmSetCompositionFont(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmSetCompositionFontW(jitter):
    imm32_ImmSetCompositionFont(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmSetCompositionString(jitter, get_str, set_str):
    """
    BOOL ImmSetCompositionString(
        HIMC hIMC,
        DWORD dwIndex,
        LPVOID lpComp,
        DWORD dwCompLen,
        LPVOID lpRead,
        DWORD dwReadLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "dwIndex", "lpComp", "dwCompLen", "lpRead", "dwReadLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmSetCompositionStringA(jitter):
    imm32_ImmSetCompositionString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmSetCompositionStringW(jitter):
    imm32_ImmSetCompositionString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_ImmSetCompositionWindow(jitter):
    """
    BOOL ImmSetCompositionWindow(
        HIMC hIMC,
        LPCOMPOSITIONFORM lpCompForm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "lpCompForm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmSetConversionStatus(jitter):
    """
    BOOL ImmSetConversionStatus(
        HIMC hIMC,
        DWORD fdwConversion,
        DWORD fdwSentence
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "fdwConversion", "fdwSentence"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmSetOpenStatus(jitter):
    """
    BOOL ImmSetOpenStatus(
        HIMC hIMC,
        BOOL fOpen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "fOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmSetStatusWindowPos(jitter):
    """
    BOOL ImmSetStatusWindowPos(
        HIMC hIMC,
        LPPOINT lpptPos
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIMC", "lpptPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmSimulateHotKey(jitter):
    """
    BOOL ImmSimulateHotKey(
        HWND hWnd,
        DWORD dwHotKeyID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "dwHotKeyID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmUnregisterWord(jitter, get_str, set_str):
    """
    BOOL ImmUnregisterWord(
        HKL hKL,
        LPCTSTR lpszReading,
        DWORD dwStyle,
        LPCTSTR lpszUnregister
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKL", "lpszReading", "dwStyle", "lpszUnregister"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imm32_ImmUnregisterWordA(jitter):
    imm32_ImmUnregisterWord(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imm32_ImmUnregisterWordW(jitter):
    imm32_ImmUnregisterWord(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imm32_IMMDisableLegacyIME(jitter):
    """
    BOOL IMMDisableLegacyIME()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
