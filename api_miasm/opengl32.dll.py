###### Enums ######

###################

###### Types ######
HGLRC = HANDLE
PROC = LPVOID

class LAYERPLANEDESCRIPTOR(MemStruct):
    fields = [
        ("nSize", WORD()),
        ("nVersion", WORD()),
        ("dwFlags", DWORD()),
        ("iPixelType", BYTE()),
        ("cColorBits", BYTE()),
        ("cRedBits", BYTE()),
        ("cRedShift", BYTE()),
        ("cGreenBits", BYTE()),
        ("cGreenShift", BYTE()),
        ("cBlueBits", BYTE()),
        ("cBlueShift", BYTE()),
        ("cAlphaBits", BYTE()),
        ("cAlphaShift", BYTE()),
        ("cAccumBits", BYTE()),
        ("cAccumRedBits", BYTE()),
        ("cAccumGreenBits", BYTE()),
        ("cAccumBlueBits", BYTE()),
        ("cAccumAlphaBits", BYTE()),
        ("cDepthBits", BYTE()),
        ("cStencilBits", BYTE()),
        ("cAuxBuffers", BYTE()),
        ("iLayerPlane", BYTE()),
        ("bReserved", BYTE()),
        ("crTransparent", COLORREF()),
    ]

LPLAYERPLANEDESCRIPTOR = Ptr("<I", LAYERPLANEDESCRIPTOR())

class POINTFLOAT(MemStruct):
    fields = [
        ("x", FLOAT()),
        ("y", FLOAT()),
    ]


class GLYPHMETRICSFLOAT(MemStruct):
    fields = [
        ("gmfBlackBoxX", FLOAT()),
        ("gmfBlackBoxY", FLOAT()),
        ("gmfptGlyphOrigin", POINTFLOAT()),
        ("gmfCellIncX", FLOAT()),
        ("gmfCellIncY", FLOAT()),
    ]

LPGLYPHMETRICSFLOAT = Ptr("<I", GLYPHMETRICSFLOAT())

###################

###### Functions ######

def opengl32_wglCreateContext(jitter):
    """
    HGLRC wglCreateContext(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglCreateLayerContext(jitter):
    """
    HGLRC wglCreateLayerContext(
        HDC hdc,
        int iLayerPlane
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iLayerPlane"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglCopyContext(jitter):
    """
    BOOL wglCopyContext(
        HGLRC hglrcSrc,
        HGLRC hglrcDst,
        UINT mask
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hglrcSrc", "hglrcDst", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglDeleteContext(jitter):
    """
    BOOL wglDeleteContext(
        HGLRC hglrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hglrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglDescribeLayerPlane(jitter):
    """
    BOOL wglDescribeLayerPlane(
        HDC hdc,
        int iPixelFormat,
        int iLayerPlane,
        UINT nBytes,
        LPLAYERPLANEDESCRIPTOR plpd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iPixelFormat", "iLayerPlane", "nBytes", "plpd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglGetCurrentContext(jitter):
    """
    HGLRC wglGetCurrentContext()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglGetCurrentDC(jitter):
    """
    HDC wglGetCurrentDC()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglGetLayerPaletteEntries(jitter):
    """
    int wglGetLayerPaletteEntries(
        HDC hdc,
        int iLayerPlane,
        int iStart,
        int cEntries,
        const COLORREF* pcr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iLayerPlane", "iStart", "cEntries", "pcr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglGetProcAddress(jitter):
    """
    PROC wglGetProcAddress(
        LPCSTR lpszProc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszProc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglMakeCurrent(jitter):
    """
    BOOL wglMakeCurrent(
        HDC hdc,
        HGLRC hglrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hglrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglRealizeLayerPalette(jitter):
    """
    BOOL wglRealizeLayerPalette(
        HDC hdc,
        int iLayerPlane,
        BOOL bRealize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iLayerPlane", "bRealize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglSetLayerPaletteEntries(jitter):
    """
    int wglSetLayerPaletteEntries(
        HDC hdc,
        int iLayerPlane,
        int iStart,
        int cEntries,
        const COLORREF* pcr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iLayerPlane", "iStart", "cEntries", "pcr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglShareLists(jitter):
    """
    BOOL wglShareLists(
        HGLRC hglrc1,
        HGLRC hglrc2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hglrc1", "hglrc2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglSwapLayerBuffers(jitter):
    """
    BOOL wglSwapLayerBuffers(
        HDC hdc,
        UINT fuPlanes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "fuPlanes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglUseFontBitmaps(jitter, get_str, set_str):
    """
    BOOL wglUseFontBitmaps(
        HDC hdc,
        DWORD first,
        DWORD count,
        DWORD listBase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "first", "count", "listBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglUseFontBitmapsA(jitter):
    opengl32_wglUseFontBitmaps(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def opengl32_wglUseFontBitmapsW(jitter):
    opengl32_wglUseFontBitmaps(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def opengl32_wglUseFontOutlines(jitter, get_str, set_str):
    """
    BOOL wglUseFontOutlines(
        HDC hdc,
        DWORD first,
        DWORD count,
        DWORD listBase,
        FLOAT deviation,
        FLOAT extrusion,
        int format,
        LPGLYPHMETRICSFLOAT lpgmf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "first", "count", "listBase", "deviation", "extrusion", "format", "lpgmf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def opengl32_wglUseFontOutlinesA(jitter):
    opengl32_wglUseFontOutlines(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def opengl32_wglUseFontOutlinesW(jitter):
    opengl32_wglUseFontOutlines(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
