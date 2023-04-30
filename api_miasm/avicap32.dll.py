###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def avicap32_capCreateCaptureWindow(jitter, get_str, set_str):
    """
    HWND capCreateCaptureWindow(
        LPCTSTR lpszWindowName,
        DWORD dwStyle,
        int x,
        int y,
        int nWidth,
        int nHeight,
        HWND hWnd,
        int nID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszWindowName", "dwStyle", "x", "y", "nWidth", "nHeight", "hWnd", "nID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avicap32_capCreateCaptureWindowA(jitter):
    avicap32_capCreateCaptureWindow(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avicap32_capCreateCaptureWindowW(jitter):
    avicap32_capCreateCaptureWindow(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def avicap32_capGetDriverDescription(jitter, get_str, set_str):
    """
    BOOL capGetDriverDescription(
        WORD wDriverIndex,
        LPTSTR lpszName,
        INT cbName,
        LPTSTR lpszVer,
        INT cbVer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wDriverIndex", "lpszName", "cbName", "lpszVer", "cbVer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avicap32_capGetDriverDescriptionA(jitter):
    avicap32_capGetDriverDescription(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avicap32_capGetDriverDescriptionW(jitter):
    avicap32_capGetDriverDescription(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
