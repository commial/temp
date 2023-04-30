
def avicap32_capCreateCaptureWindow(jitter):
    """"
    [avicap32.dll] HWND capCreateCaptureWindow(LPCTSTR lpszWindowName, DWORD dwStyle, int x, int y, int nWidth, int nHeight, HWND hWnd, int nID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszWindowName", "dwStyle", "x", "y", "nWidth", "nHeight", "hWnd", "nID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avicap32_capGetDriverDescription(jitter):
    """"
    [avicap32.dll] BOOL capGetDriverDescription(WORD wDriverIndex, LPTSTR lpszName, INT cbName, LPTSTR lpszVer, INT cbVer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["wDriverIndex", "lpszName", "cbName", "lpszVer", "cbVer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
