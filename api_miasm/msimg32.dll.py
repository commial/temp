_GradientFillMode_ = {
    "GRADIENT_FILL_RECT_H": 0x00000000,
    "GRADIENT_FILL_RECT_V": 0x00000001,
    "GRADIENT_FILL_TRIANGLE": 0x00000002,
}

def msimg32_AlphaBlend(jitter):
    """
    BOOL AlphaBlend(
        HDC hdcDest,
        int xoriginDest,
        int yoriginDest,
        int wDest,
        int hDest,
        HDC hdcSrc,
        int xoriginSrc,
        int yoriginSrc,
        int wSrc,
        int hSrc,
        BLENDFUNCTION ftn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdcDest", "xoriginDest", "yoriginDest", "wDest", "hDest", "hdcSrc", "xoriginSrc", "yoriginSrc", "wSrc", "hSrc", "ftn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msimg32_GradientFill(jitter):
    """
    BOOL GradientFill(
        HDC hdc,
        PTRIVERTEX pVertex,
        ULONG nVertex,
        PVOID pMesh,
        ULONG nMesh,
        [GradientFillMode] ulMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "pVertex", "nVertex", "pMesh", "nMesh", "ulMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msimg32_TransparentBlt(jitter):
    """
    BOOL TransparentBlt(
        HDC hdcDest,
        int xoriginDest,
        int yoriginDest,
        int wDest,
        int hDest,
        HDC hdcSrc,
        int xoriginSrc,
        int yoriginSrc,
        int wSrc,
        int hSrc,
        UINT crTransparent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdcDest", "xoriginDest", "yoriginDest", "wDest", "hDest", "hdcSrc", "xoriginSrc", "yoriginSrc", "wSrc", "hSrc", "crTransparent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
