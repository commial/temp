
def magnification_MagGetColorEffect(jitter):
    """
    [Magnification.dll] BOOL MagGetColorEffect(HWND hwnd, PMAGCOLOREFFECT pEffect)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pEffect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagGetFullscreenColorEffect(jitter):
    """
    [Magnification.dll] BOOL MagGetFullscreenColorEffect(PMAGCOLOREFFECT pEffect)
    """
    ret_ad, args = jitter.func_args_stdcall(["pEffect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagGetFullscreenTransform(jitter):
    """
    [Magnification.dll] BOOL MagGetFullscreenTransform(float* pMagLevel, int* pxOffset, int* pyOffset)
    """
    ret_ad, args = jitter.func_args_stdcall(["pMagLevel", "pxOffset", "pyOffset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagGetImageScalingCallback(jitter):
    """
    [Magnification.dll] MagImageScalingCallback MagGetImageScalingCallback(HWND hwnd)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagGetInputTransform(jitter):
    """
    [Magnification.dll] BOOL MagGetInputTransform(BOOL* pfEnabled, LPRECT prcSource, LPRECT prcDest)
    """
    ret_ad, args = jitter.func_args_stdcall(["pfEnabled", "prcSource", "prcDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagGetWindowFilterList(jitter):
    """
    [Magnification.dll] int MagGetWindowFilterList(HWND hwnd, DWORD* pdwFilterMode, int count, HWND* pHWND)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pdwFilterMode", "count", "pHWND"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagGetWindowSource(jitter):
    """
    [Magnification.dll] BOOL MagGetWindowSource(HWND hwnd, RECT* pRect)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagGetWindowTransform(jitter):
    """
    [Magnification.dll] BOOL MagGetWindowTransform(HWND hwnd, PMAGTRANSFORM pTransform)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pTransform"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagInitialize(jitter):
    """
    [Magnification.dll] BOOL MagInitialize()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagSetColorEffect(jitter):
    """
    [Magnification.dll] BOOL MagSetColorEffect(HWND hwnd, PMAGCOLOREFFECT pEffect)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pEffect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagSetFullscreenColorEffect(jitter):
    """
    [Magnification.dll] BOOL MagSetFullscreenColorEffect(PMAGCOLOREFFECT pEffect)
    """
    ret_ad, args = jitter.func_args_stdcall(["pEffect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagSetFullscreenTransform(jitter):
    """
    [Magnification.dll] BOOL MagSetFullscreenTransform(float magLevel, int xOffset, int yOffset)
    """
    ret_ad, args = jitter.func_args_stdcall(["magLevel", "xOffset", "yOffset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagSetImageScalingCallback(jitter):
    """
    [Magnification.dll] BOOL MagSetImageScalingCallback(HWND hwnd, MagImageScalingCallback callback)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "callback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagSetInputTransform(jitter):
    """
    [Magnification.dll] BOOL MagSetInputTransform(BOOL fEnabled, const LPRECT prcSource, const LPRECT prcDest)
    """
    ret_ad, args = jitter.func_args_stdcall(["fEnabled", "prcSource", "prcDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagSetWindowFilterList(jitter):
    """
    [Magnification.dll] BOOL MagSetWindowFilterList(HWND hwnd, DWORD dwFilterMode, int count, HWND* pHWND)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwFilterMode", "count", "pHWND"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagSetWindowSource(jitter):
    """
    [Magnification.dll] BOOL MagSetWindowSource(HWND hwnd, RECT rect)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "rect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagSetWindowTransform(jitter):
    """
    [Magnification.dll] BOOL MagSetWindowTransform(HWND hwnd, PMAGTRANSFORM pTransform)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pTransform"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagShowSystemCursor(jitter):
    """
    [Magnification.dll] BOOL MagShowSystemCursor(BOOL fShowCursor)
    """
    ret_ad, args = jitter.func_args_stdcall(["fShowCursor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def magnification_MagUninitialize(jitter):
    """
    [Magnification.dll] BOOL MagUninitialize()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
