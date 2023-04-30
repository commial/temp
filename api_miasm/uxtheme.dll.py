BP_ANIMATIONSTYLE = {
    "BPAS_NONE": 0,
    "BPAS_LINEAR": 1,
    "BPAS_CUBIC": 2,
    "BPAS_SINE": 3,
}
BP_ANIMATIONSTYLE_INV = {
    0: "BPAS_NONE",
    1: "BPAS_LINEAR",
    2: "BPAS_CUBIC",
    3: "BPAS_SINE",
}
TEXTSHADOWTYPE = {
    "TST_NONE": 0,
    "TST_SINGLE": 1,
    "TST_CONTINUOUS": 2,
}
TEXTSHADOWTYPE_INV = {
    0: "TST_NONE",
    1: "TST_SINGLE",
    2: "TST_CONTINUOUS",
}
THEMESIZE = {
    "TS_MIN": 0,
    "TS_TRUE": 1,
    "TS_DRAW": 2,
}
THEMESIZE_INV = {
    0: "TS_MIN",
    1: "TS_TRUE",
    2: "TS_DRAW",
}
PROPERTYORIGIN = {
    "PO_STATE": 0,
    "PO_PART": 1,
    "PO_CLASS": 2,
    "PO_GLOBAL": 3,
    "PO_NOTFOUND": 4,
}
PROPERTYORIGIN_INV = {
    0: "PO_STATE",
    1: "PO_PART",
    2: "PO_CLASS",
    3: "PO_GLOBAL",
    4: "PO_NOTFOUND",
}
_HitTestReturnCode_ = {
    "HTERROR": -2,
    "HTTRANSPARENT": -1,
    "HTNOWHERE": 0,
    "HTCLIENT": 1,
    "HTCAPTION": 2,
    "HTSYSMENU": 3,
    "HTGROWBOX": 4,
    "HTMENU": 5,
    "HTHSCROLL": 6,
    "HTVSCROLL": 7,
    "HTMINBUTTON": 8,
    "HTMAXBUTTON": 9,
    "HTLEFT": 10,
    "HTRIGHT": 11,
    "HTTOP": 12,
    "HTTOPLEFT": 13,
    "HTTOPRIGHT": 14,
    "HTBOTTOM": 15,
    "HTBOTTOMLEFT": 16,
    "HTBOTTOMRIGHT": 17,
    "HTBORDER": 18,
    "HTOBJECT": 19,
    "HTCLOSE": 20,
    "HTHELP": 21,
}
_HitTestReturnCode__INV = {
    -2: "HTERROR",
    -1: "HTTRANSPARENT",
    0: "HTNOWHERE",
    1: "HTCLIENT",
    2: "HTCAPTION",
    3: "HTSYSMENU",
    4: "HTGROWBOX",
    5: "HTMENU",
    6: "HTHSCROLL",
    7: "HTVSCROLL",
    8: "HTMINBUTTON",
    9: "HTMAXBUTTON",
    10: "HTLEFT",
    11: "HTRIGHT",
    12: "HTTOP",
    13: "HTTOPLEFT",
    14: "HTTOPRIGHT",
    15: "HTBOTTOM",
    16: "HTBOTTOMLEFT",
    17: "HTBOTTOMRIGHT",
    18: "HTBORDER",
    19: "HTOBJECT",
    20: "HTCLOSE",
    21: "HTHELP",
}
BP_BUFFERFORMAT = {
    "BPBF_COMPATIBLEBITMAP": 0,
    "BPBF_DIB": 1,
    "BPBF_TOPDOWNDIB": 2,
    "BPBF_TOPDOWNMONODIB": 3,
}
BP_BUFFERFORMAT_INV = {
    0: "BPBF_COMPATIBLEBITMAP",
    1: "BPBF_DIB",
    2: "BPBF_TOPDOWNDIB",
    3: "BPBF_TOPDOWNMONODIB",
}
WINDOWTHEMEATTRIBUTETYPE = {
    "WTA_NONCLIENT": 1,
}
WINDOWTHEMEATTRIBUTETYPE_INV = {
    1: "WTA_NONCLIENT",
}
TA_TRANSFORM_TYPE = {
    "TATT_TRANSLATE_2D": 0,
    "TATT_SCALE_2D": 1,
    "TATT_OPACITY": 2,
    "TATT_CLIP": 3,
}
TA_TRANSFORM_TYPE_INV = {
    0: "TATT_TRANSLATE_2D",
    1: "TATT_SCALE_2D",
    2: "TATT_OPACITY",
    3: "TATT_CLIP",
}
TA_PROPERTY = {
    "TAP_FLAGS": 0,
    "TAP_TRANSFORMCOUNT": 1,
    "TAP_STAGGERDELAY": 2,
    "TAP_STAGGERDELAYCAP": 3,
    "TAP_STAGGERDELAYFACTOR": 4,
    "TAP_ZORDER": 5,
}
TA_PROPERTY_INV = {
    0: "TAP_FLAGS",
    1: "TAP_TRANSFORMCOUNT",
    2: "TAP_STAGGERDELAY",
    3: "TAP_STAGGERDELAYCAP",
    4: "TAP_STAGGERDELAYFACTOR",
    5: "TAP_ZORDER",
}
TA_TIMINGFUNCTION_TYPE = {
    "TTFT_UNDEFINED": 0,
    "TTFT_CUBIC_BEZIER": 1,
}
TA_TIMINGFUNCTION_TYPE_INV = {
    0: "TTFT_UNDEFINED",
    1: "TTFT_CUBIC_BEZIER",
}

def uxtheme_BeginBufferedAnimation(jitter):
    """
    HANIMATIONBUFFER BeginBufferedAnimation(
        HWND hwnd,
        HDC hdcTarget,
        const RECT* rcTarget,
        BP_BUFFERFORMAT dwFormat,
        BP_PAINTPARAMS* pPaintParams,
        BP_ANIMATIONPARAMS* pAnimationParams,
        HDC* phdcFrom,
        HDC* phdcTo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdcTarget", "rcTarget", "dwFormat", "pPaintParams", "pAnimationParams", "phdcFrom", "phdcTo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BeginBufferedPaint(jitter):
    """
    HPAINTBUFFER BeginBufferedPaint(
        HDC hdcTarget,
        const RECT* prcTarget,
        BP_BUFFERFORMAT dwFormat,
        BP_PAINTPARAMS* pPaintParams,
        HDC* phdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdcTarget", "prcTarget", "dwFormat", "pPaintParams", "phdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BufferedPaintClear(jitter):
    """
    HRESULT BufferedPaintClear(
        HPAINTBUFFER hBufferedPaint,
        const RECT* prc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint", "prc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BufferedPaintInit(jitter):
    """
    HRESULT BufferedPaintInit()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BufferedPaintRenderAnimation(jitter):
    """
    BOOL BufferedPaintRenderAnimation(
        HWND hwnd,
        HDC hdcTarget
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdcTarget"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BufferedPaintSetAlpha(jitter):
    """
    HRESULT BufferedPaintSetAlpha(
        HPAINTBUFFER hBufferedPaint,
        const RECT* prc,
        BYTE alpha
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint", "prc", "alpha"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BufferedPaintStopAllAnimations(jitter):
    """
    HRESULT BufferedPaintStopAllAnimations(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BufferedPaintUnInit(jitter):
    """
    HRESULT BufferedPaintUnInit()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_CloseThemeData(jitter):
    """
    HRESULT CloseThemeData(
        HTHEME hTheme
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeBackground(jitter):
    """
    HRESULT DrawThemeBackground(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        const RECT* pRect,
        const RECT* pClipRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pRect", "pClipRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeBackgroundEx(jitter):
    """
    HRESULT DrawThemeBackgroundEx(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        const RECT* pRect,
        const DTBGOPTS* pOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pRect", "pOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeEdge(jitter):
    """
    HRESULT DrawThemeEdge(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        LPCRECT pDestRect,
        [BorderEdge] uEdge,
        [BorderFlag] uFlags,
        LPRECT pContentRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pDestRect", "uEdge", "uFlags", "pContentRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeIcon(jitter):
    """
    HRESULT DrawThemeIcon(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        LPCRECT pRect,
        HIMAGELIST himl,
        int iImageIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pRect", "himl", "iImageIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeParentBackground(jitter):
    """
    HRESULT DrawThemeParentBackground(
        HWND hwnd,
        HDC hdc,
        const RECT* prc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdc", "prc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeParentBackgroundEx(jitter):
    """
    HRESULT DrawThemeParentBackgroundEx(
        HWND hwnd,
        HDC hdc,
        [DrawThemeParentBackgroundFlags] dwFlags,
        const RECT* prc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdc", "dwFlags", "prc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeText(jitter):
    """
    HRESULT DrawThemeText(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        LPCWSTR pszText,
        int iCharCount,
        [DrawTextFlags] dwTextFlags,
        DWORD dwTextFlags2,
        LPCRECT pRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pszText", "iCharCount", "dwTextFlags", "dwTextFlags2", "pRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeTextEx(jitter):
    """
    HRESULT DrawThemeTextEx(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        LPCWSTR pszText,
        int iCharCount,
        [DrawTextFlags] dwFlags,
        LPRECT pRect,
        const DTTOPTS* pOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pszText", "iCharCount", "dwFlags", "pRect", "pOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_EnableThemeDialogTexture(jitter):
    """
    HRESULT EnableThemeDialogTexture(
        HWND hwnd,
        [EnableThemeDialogTextureFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_EnableTheming(jitter):
    """
    HRESULT EnableTheming(
        BOOL fEnable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_EndBufferedAnimation(jitter):
    """
    HRESULT EndBufferedAnimation(
        HANIMATIONBUFFER hbpAnimation,
        BOOL fUpdateTarget
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbpAnimation", "fUpdateTarget"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_EndBufferedPaint(jitter):
    """
    HRESULT EndBufferedPaint(
        HPAINTBUFFER hBufferedPaint,
        BOOL fUpdateTarget
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint", "fUpdateTarget"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetBufferedPaintBits(jitter):
    """
    HRESULT GetBufferedPaintBits(
        HPAINTBUFFER hBufferedPaint,
        RGBQUAD** ppbBuffer,
        int* pcxRow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint", "ppbBuffer", "pcxRow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetBufferedPaintDC(jitter):
    """
    HDC GetBufferedPaintDC(
        HPAINTBUFFER hBufferedPaint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetBufferedPaintTargetDC(jitter):
    """
    HDC GetBufferedPaintTargetDC(
        HPAINTBUFFER hBufferedPaint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetBufferedPaintTargetRect(jitter):
    """
    HRESULT GetBufferedPaintTargetRect(
        HPAINTBUFFER hBufferedPaint,
        RECT* prc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint", "prc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetCurrentThemeName(jitter):
    """
    HRESULT GetCurrentThemeName(
        LPWSTR pszThemeFileName,
        int dwMaxNameChars,
        LPWSTR pszColorBuff,
        int cchMaxColorChars,
        LPWSTR pszSizeBuff,
        int cchMaxSizeChars
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszThemeFileName", "dwMaxNameChars", "pszColorBuff", "cchMaxColorChars", "pszSizeBuff", "cchMaxSizeChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeAnimationTransform(jitter):
    """
    HRESULT GetThemeAnimationTransform(
        HTHEME hTheme,
        int iStoryboardId,
        int iTargetId,
        DWORD dwTransformIndex,
        TA_TRANSFORM* pTransform,
        DWORD cbSize,
        DWORD pcbSizeOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iStoryboardId", "iTargetId", "dwTransformIndex", "pTransform", "cbSize", "pcbSizeOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeAppProperties(jitter):
    """
    DWORD GetThemeAppProperties()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeBackgroundContentRect(jitter):
    """
    HRESULT GetThemeBackgroundContentRect(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        LPCRECT pBoundingRect,
        LPRECT pContentRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pBoundingRect", "pContentRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeBackgroundExtent(jitter):
    """
    HRESULT GetThemeBackgroundExtent(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        LPCRECT pContentRect,
        LPRECT pExtentRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pContentRect", "pExtentRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeBackgroundRegion(jitter):
    """
    HRESULT GetThemeBackgroundRegion(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        LPCRECT pRect,
        HRGN* pRegion
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pRect", "pRegion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeBitmap(jitter):
    """
    HRESULT GetThemeBitmap(
        HTHEME hTheme,
        int iPartId,
        int iStateId,
        int iPropId,
        ULONG dwFlags,
        HBITMAP* phBitmap
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "dwFlags", "phBitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeBool(jitter):
    """
    HRESULT GetThemeBool(
        HTHEME hTheme,
        int iPartId,
        int iStateId,
        int iPropId,
        BOOL* pfVal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pfVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeColor(jitter):
    """
    HRESULT GetThemeColor(
        HTHEME hTheme,
        int iPartId,
        int iStateId,
        int iPropId,
        COLORREF* pColor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pColor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeDocumentationProperty(jitter):
    """
    HRESULT GetThemeDocumentationProperty(
        LPCWSTR pszThemeName,
        LPCWSTR pszPropertyName,
        LPWSTR pszValueBuff,
        int cchMaxValChars
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszThemeName", "pszPropertyName", "pszValueBuff", "cchMaxValChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeEnumValue(jitter):
    """
    HRESULT GetThemeEnumValue(
        HTHEME hTheme,
        int iPartId,
        int iStateId,
        int iPropId,
        int* piVal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "piVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeFilename(jitter):
    """
    HRESULT GetThemeFilename(
        HTHEME hTheme,
        int iPartId,
        int iStateId,
        int iPropId,
        LPWSTR pszThemeFilename,
        int cchMaxBuffChars
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pszThemeFilename", "cchMaxBuffChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeFont(jitter):
    """
    HRESULT GetThemeFont(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        int iPropId,
        LOGFONTW* pFont
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "iPropId", "pFont"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeInt(jitter):
    """
    HRESULT GetThemeInt(
        HTHEME hTheme,
        int iPartId,
        int iStateId,
        int iPropId,
        int* piVal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "piVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeIntList(jitter):
    """
    HRESULT GetThemeIntList(
        HTHEME hTheme,
        int iPartId,
        int iStateId,
        int iPropId,
        INTLIST* pIntList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pIntList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeMargins(jitter):
    """
    HRESULT GetThemeMargins(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        int iPropId,
        LPRECT prc,
        MARGINS* pMargins
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "iPropId", "prc", "pMargins"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeMetric(jitter):
    """
    HRESULT GetThemeMetric(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        int iPropId,
        int* piVal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "iPropId", "piVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemePartSize(jitter):
    """
    HRESULT GetThemePartSize(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        LPCRECT prc,
        THEMESIZE eSize,
        SIZE* psz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "prc", "eSize", "psz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemePosition(jitter):
    """
    HRESULT GetThemePosition(
        HTHEME hTheme,
        int iPartId,
        int iStateId,
        int iPropId,
        POINT* pPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemePropertyOrigin(jitter):
    """
    HRESULT GetThemePropertyOrigin(
        HTHEME hTheme,
        int iPartId,
        int iStateId,
        int iPropId,
        PROPERTYORIGIN* pOrigin
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pOrigin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeRect(jitter):
    """
    HRESULT GetThemeRect(
        HTHEME hTheme,
        int iPartId,
        int iStateId,
        int iPropId,
        LPRECT pRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeStream(jitter):
    """
    HRESULT GetThemeStream(
        HTHEME hTheme,
        int iPartId,
        int iStateId,
        int iPropId,
        VOID** ppvStream,
        DWORD* pcbStream,
        HINSTANCE hInst
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "ppvStream", "pcbStream", "hInst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeString(jitter):
    """
    HRESULT GetThemeString(
        HTHEME hTheme,
        int iPartId,
        int iStateId,
        int iPropId,
        LPWSTR pszBuff,
        int cchMaxBuffChars
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pszBuff", "cchMaxBuffChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysBool(jitter):
    """
    BOOL GetThemeSysBool(
        HTHEME hTheme,
        int iBoolID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iBoolID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysColor(jitter):
    """
    COLORREF GetThemeSysColor(
        HTHEME hTheme,
        [SysColorIndex] iColorID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iColorID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysColorBrush(jitter):
    """
    HBRUSH GetThemeSysColorBrush(
        HTHEME hTheme,
        int iColorID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iColorID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysFont(jitter):
    """
    HRESULT GetThemeSysFont(
        HTHEME hTheme,
        int iFontID,
        LOGFONTW* plf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iFontID", "plf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysInt(jitter):
    """
    HRESULT GetThemeSysInt(
        HTHEME hTheme,
        int iIntID,
        int* piValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iIntID", "piValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysSize(jitter):
    """
    int GetThemeSysSize(
        HTHEME hTheme,
        int iSizeID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iSizeID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysString(jitter):
    """
    HRESULT GetThemeSysString(
        HTHEME hTheme,
        int iStringID,
        LPWSTR pszStringBuff,
        int cchMaxStringChars
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iStringID", "pszStringBuff", "cchMaxStringChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeTextExtent(jitter):
    """
    HRESULT GetThemeTextExtent(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        LPCWSTR pszText,
        int iCharCount,
        [DrawTextFlags] dwTextFlags,
        LPCRECT pBoundingRect,
        LPRECT pExtentRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pszText", "iCharCount", "dwTextFlags", "pBoundingRect", "pExtentRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeTextMetrics(jitter):
    """
    HRESULT GetThemeTextMetrics(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        TEXTMETRIC* ptm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "ptm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeTimingFunction(jitter):
    """
    HRESULT GetThemeTimingFunction(
        HTHEME hTheme,
        int iTimingFunctionId,
        TA_TIMINGFUNCTION* pTimingFunction,
        DWORD cbSize,
        DWORD pcbSizeOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iTimingFunctionId", "pTimingFunction", "cbSize", "pcbSizeOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeTransitionDuration(jitter):
    """
    HRESULT GetThemeTransitionDuration(
        HTHEME hTheme,
        int iPartId,
        int iStateIdFrom,
        int iStateIdTo,
        int iPropId,
        DWORD* pdwDuration
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateIdFrom", "iStateIdTo", "iPropId", "pdwDuration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetWindowTheme(jitter):
    """
    HTHEME GetWindowTheme(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_HitTestThemeBackground(jitter):
    """
    HRESULT HitTestThemeBackground(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        [HitTestThemeBackgroundOptions] dwOptions,
        LPCRECT pRect,
        HRGN hrgn,
        POINT ptTest,
        [HitTestReturnCode*] pwHitTestCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "dwOptions", "pRect", "hrgn", "ptTest", "pwHitTestCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_IsAppThemed(jitter):
    """
    BOOL IsAppThemed()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_IsCompositionActive(jitter):
    """
    BOOL IsCompositionActive()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_IsThemeActive(jitter):
    """
    BOOL IsThemeActive()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_IsThemeBackgroundPartiallyTransparent(jitter):
    """
    BOOL IsThemeBackgroundPartiallyTransparent(
        HTHEME hTheme,
        int iPartId,
        int iStateId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_IsThemeDialogTextureEnabled(jitter):
    """
    BOOL IsThemeDialogTextureEnabled(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_IsThemePartDefined(jitter):
    """
    BOOL IsThemePartDefined(
        HTHEME hTheme,
        int iPartId,
        int iStateId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_OpenThemeData(jitter):
    """
    HTHEME OpenThemeData(
        HWND hwnd,
        LPCWSTR pszClassList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszClassList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_OpenThemeDataEx(jitter):
    """
    HTHEME OpenThemeDataEx(
        HWND hwnd,
        LPCWSTR pszClassIdList,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszClassIdList", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_SetThemeAppProperties(jitter):
    """
    void SetThemeAppProperties(
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_SetWindowTheme(jitter):
    """
    HRESULT SetWindowTheme(
        HWND hwnd,
        LPCWSTR pszSubAppName,
        LPCWSTR pszSubIdList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszSubAppName", "pszSubIdList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_SetWindowThemeAttribute(jitter):
    """
    HRESULT SetWindowThemeAttribute(
        HWND hwnd,
        WINDOWTHEMEATTRIBUTETYPE eAttribute,
        PVOID pvAttribute,
        DWORD cbAttribute
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "eAttribute", "pvAttribute", "cbAttribute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeAnimationProperty(jitter):
    """
    HRESULT GetThemeAnimationProperty(
        HTHEME hTheme,
        int iStoryboardId,
        int iTargetId,
        TA_PROPERTY eProperty,
        VOID* pvProperty,
        DWORD cbSize,
        DWORD pcbSizeOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iStoryboardId", "iTargetId", "eProperty", "pvProperty", "cbSize", "pcbSizeOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BeginPanningFeedback(jitter):
    """
    BOOL BeginPanningFeedback(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_EndPanningFeedback(jitter):
    """
    BOOL EndPanningFeedback(
        HWND hwnd,
        BOOL fAnimateBack
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "fAnimateBack"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_UpdatePanningFeedback(jitter):
    """
    BOOL UpdatePanningFeedback(
        HWND hwnd,
        LONG lTotalOverpanOffsetX,
        LONG lTotalOverpanOffsetY,
        BOOL fInInertia
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lTotalOverpanOffsetX", "lTotalOverpanOffsetY", "fInInertia"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
