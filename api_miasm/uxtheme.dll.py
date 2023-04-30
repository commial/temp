
def uxtheme_BeginBufferedAnimation(jitter):
    """"
    [UxTheme.dll] HANIMATIONBUFFER BeginBufferedAnimation(HWND hwnd, HDC hdcTarget, const RECT* rcTarget, BP_BUFFERFORMAT dwFormat, BP_PAINTPARAMS* pPaintParams, BP_ANIMATIONPARAMS* pAnimationParams, HDC* phdcFrom, HDC* phdcTo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdcTarget", "rcTarget", "dwFormat", "pPaintParams", "pAnimationParams", "phdcFrom", "phdcTo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BeginBufferedPaint(jitter):
    """"
    [UxTheme.dll] HPAINTBUFFER BeginBufferedPaint(HDC hdcTarget, const RECT* prcTarget, BP_BUFFERFORMAT dwFormat, BP_PAINTPARAMS* pPaintParams, HDC* phdc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdcTarget", "prcTarget", "dwFormat", "pPaintParams", "phdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BufferedPaintClear(jitter):
    """"
    [UxTheme.dll] HRESULT BufferedPaintClear(HPAINTBUFFER hBufferedPaint, const RECT* prc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint", "prc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BufferedPaintInit(jitter):
    """"
    [UxTheme.dll] HRESULT BufferedPaintInit()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BufferedPaintRenderAnimation(jitter):
    """"
    [UxTheme.dll] BOOL BufferedPaintRenderAnimation(HWND hwnd, HDC hdcTarget)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdcTarget"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BufferedPaintSetAlpha(jitter):
    """"
    [UxTheme.dll] HRESULT BufferedPaintSetAlpha(HPAINTBUFFER hBufferedPaint, const RECT* prc, BYTE alpha)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint", "prc", "alpha"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BufferedPaintStopAllAnimations(jitter):
    """"
    [UxTheme.dll] HRESULT BufferedPaintStopAllAnimations(HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BufferedPaintUnInit(jitter):
    """"
    [UxTheme.dll] HRESULT BufferedPaintUnInit()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_CloseThemeData(jitter):
    """"
    [UxTheme.dll] HRESULT CloseThemeData(HTHEME hTheme)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeBackground(jitter):
    """"
    [UxTheme.dll] HRESULT DrawThemeBackground(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, const RECT* pRect, const RECT* pClipRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pRect", "pClipRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeBackgroundEx(jitter):
    """"
    [UxTheme.dll] HRESULT DrawThemeBackgroundEx(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, const RECT* pRect, const DTBGOPTS* pOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pRect", "pOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeEdge(jitter):
    """"
    [UxTheme.dll] HRESULT DrawThemeEdge(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, LPCRECT pDestRect, [BorderEdge] uEdge, [BorderFlag] uFlags, LPRECT pContentRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pDestRect", "uEdge", "uFlags", "pContentRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeIcon(jitter):
    """"
    [UxTheme.dll] HRESULT DrawThemeIcon(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, LPCRECT pRect, HIMAGELIST himl, int iImageIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pRect", "himl", "iImageIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeParentBackground(jitter):
    """"
    [UxTheme.dll] HRESULT DrawThemeParentBackground(HWND hwnd, HDC hdc, const RECT* prc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdc", "prc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeParentBackgroundEx(jitter):
    """"
    [UxTheme.dll] HRESULT DrawThemeParentBackgroundEx(HWND hwnd, HDC hdc, [DrawThemeParentBackgroundFlags] dwFlags, const RECT* prc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hdc", "dwFlags", "prc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeText(jitter):
    """"
    [UxTheme.dll] HRESULT DrawThemeText(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, LPCWSTR pszText, int iCharCount, [DrawTextFlags] dwTextFlags, DWORD dwTextFlags2, LPCRECT pRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pszText", "iCharCount", "dwTextFlags", "dwTextFlags2", "pRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_DrawThemeTextEx(jitter):
    """"
    [UxTheme.dll] HRESULT DrawThemeTextEx(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, LPCWSTR pszText, int iCharCount, [DrawTextFlags] dwFlags, LPRECT pRect, const DTTOPTS* pOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pszText", "iCharCount", "dwFlags", "pRect", "pOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_EnableThemeDialogTexture(jitter):
    """"
    [UxTheme.dll] HRESULT EnableThemeDialogTexture(HWND hwnd, [EnableThemeDialogTextureFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_EnableTheming(jitter):
    """"
    [UxTheme.dll] HRESULT EnableTheming(BOOL fEnable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_EndBufferedAnimation(jitter):
    """"
    [UxTheme.dll] HRESULT EndBufferedAnimation(HANIMATIONBUFFER hbpAnimation, BOOL fUpdateTarget)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbpAnimation", "fUpdateTarget"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_EndBufferedPaint(jitter):
    """"
    [UxTheme.dll] HRESULT EndBufferedPaint(HPAINTBUFFER hBufferedPaint, BOOL fUpdateTarget)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint", "fUpdateTarget"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetBufferedPaintBits(jitter):
    """"
    [UxTheme.dll] HRESULT GetBufferedPaintBits(HPAINTBUFFER hBufferedPaint, RGBQUAD** ppbBuffer, int* pcxRow)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint", "ppbBuffer", "pcxRow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetBufferedPaintDC(jitter):
    """"
    [UxTheme.dll] HDC GetBufferedPaintDC(HPAINTBUFFER hBufferedPaint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetBufferedPaintTargetDC(jitter):
    """"
    [UxTheme.dll] HDC GetBufferedPaintTargetDC(HPAINTBUFFER hBufferedPaint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetBufferedPaintTargetRect(jitter):
    """"
    [UxTheme.dll] HRESULT GetBufferedPaintTargetRect(HPAINTBUFFER hBufferedPaint, RECT* prc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hBufferedPaint", "prc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetCurrentThemeName(jitter):
    """"
    [UxTheme.dll] HRESULT GetCurrentThemeName(LPWSTR pszThemeFileName, int dwMaxNameChars, LPWSTR pszColorBuff, int cchMaxColorChars, LPWSTR pszSizeBuff, int cchMaxSizeChars)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszThemeFileName", "dwMaxNameChars", "pszColorBuff", "cchMaxColorChars", "pszSizeBuff", "cchMaxSizeChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeAnimationTransform(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeAnimationTransform(HTHEME hTheme, int iStoryboardId, int iTargetId, DWORD dwTransformIndex, TA_TRANSFORM* pTransform, DWORD cbSize, DWORD pcbSizeOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iStoryboardId", "iTargetId", "dwTransformIndex", "pTransform", "cbSize", "pcbSizeOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeAppProperties(jitter):
    """"
    [UxTheme.dll] DWORD GetThemeAppProperties()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeBackgroundContentRect(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeBackgroundContentRect(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, LPCRECT pBoundingRect, LPRECT pContentRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pBoundingRect", "pContentRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeBackgroundExtent(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeBackgroundExtent(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, LPCRECT pContentRect, LPRECT pExtentRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pContentRect", "pExtentRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeBackgroundRegion(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeBackgroundRegion(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, LPCRECT pRect, HRGN* pRegion)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pRect", "pRegion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeBitmap(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeBitmap(HTHEME hTheme, int iPartId, int iStateId, int iPropId, ULONG dwFlags, HBITMAP* phBitmap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "dwFlags", "phBitmap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeBool(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeBool(HTHEME hTheme, int iPartId, int iStateId, int iPropId, BOOL* pfVal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pfVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeColor(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeColor(HTHEME hTheme, int iPartId, int iStateId, int iPropId, COLORREF* pColor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pColor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeDocumentationProperty(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeDocumentationProperty(LPCWSTR pszThemeName, LPCWSTR pszPropertyName, LPWSTR pszValueBuff, int cchMaxValChars)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszThemeName", "pszPropertyName", "pszValueBuff", "cchMaxValChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeEnumValue(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeEnumValue(HTHEME hTheme, int iPartId, int iStateId, int iPropId, int* piVal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "piVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeFilename(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeFilename(HTHEME hTheme, int iPartId, int iStateId, int iPropId, LPWSTR pszThemeFilename, int cchMaxBuffChars)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pszThemeFilename", "cchMaxBuffChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeFont(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeFont(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, int iPropId, LOGFONTW* pFont)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "iPropId", "pFont"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeInt(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeInt(HTHEME hTheme, int iPartId, int iStateId, int iPropId, int* piVal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "piVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeIntList(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeIntList(HTHEME hTheme, int iPartId, int iStateId, int iPropId, INTLIST* pIntList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pIntList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeMargins(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeMargins(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, int iPropId, LPRECT prc, MARGINS* pMargins)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "iPropId", "prc", "pMargins"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeMetric(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeMetric(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, int iPropId, int* piVal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "iPropId", "piVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemePartSize(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemePartSize(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, LPCRECT prc, THEMESIZE eSize, SIZE* psz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "prc", "eSize", "psz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemePosition(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemePosition(HTHEME hTheme, int iPartId, int iStateId, int iPropId, POINT* pPoint)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemePropertyOrigin(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemePropertyOrigin(HTHEME hTheme, int iPartId, int iStateId, int iPropId, PROPERTYORIGIN* pOrigin)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pOrigin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeRect(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeRect(HTHEME hTheme, int iPartId, int iStateId, int iPropId, LPRECT pRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeStream(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeStream(HTHEME hTheme, int iPartId, int iStateId, int iPropId, VOID** ppvStream, DWORD* pcbStream, HINSTANCE hInst)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "ppvStream", "pcbStream", "hInst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeString(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeString(HTHEME hTheme, int iPartId, int iStateId, int iPropId, LPWSTR pszBuff, int cchMaxBuffChars)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId", "iPropId", "pszBuff", "cchMaxBuffChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysBool(jitter):
    """"
    [UxTheme.dll] BOOL GetThemeSysBool(HTHEME hTheme, int iBoolID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iBoolID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysColor(jitter):
    """"
    [UxTheme.dll] COLORREF GetThemeSysColor(HTHEME hTheme, [SysColorIndex] iColorID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iColorID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysColorBrush(jitter):
    """"
    [UxTheme.dll] HBRUSH GetThemeSysColorBrush(HTHEME hTheme, int iColorID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iColorID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysFont(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeSysFont(HTHEME hTheme, int iFontID, LOGFONTW* plf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iFontID", "plf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysInt(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeSysInt(HTHEME hTheme, int iIntID, int* piValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iIntID", "piValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysSize(jitter):
    """"
    [UxTheme.dll] int GetThemeSysSize(HTHEME hTheme, int iSizeID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iSizeID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeSysString(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeSysString(HTHEME hTheme, int iStringID, LPWSTR pszStringBuff, int cchMaxStringChars)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iStringID", "pszStringBuff", "cchMaxStringChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeTextExtent(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeTextExtent(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, LPCWSTR pszText, int iCharCount, [DrawTextFlags] dwTextFlags, LPCRECT pBoundingRect, LPRECT pExtentRect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "pszText", "iCharCount", "dwTextFlags", "pBoundingRect", "pExtentRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeTextMetrics(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeTextMetrics(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, TEXTMETRIC* ptm)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "ptm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeTimingFunction(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeTimingFunction(HTHEME hTheme, int iTimingFunctionId, TA_TIMINGFUNCTION* pTimingFunction, DWORD cbSize, DWORD pcbSizeOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iTimingFunctionId", "pTimingFunction", "cbSize", "pcbSizeOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeTransitionDuration(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeTransitionDuration(HTHEME hTheme, int iPartId, int iStateIdFrom, int iStateIdTo, int iPropId, DWORD* pdwDuration)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateIdFrom", "iStateIdTo", "iPropId", "pdwDuration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetWindowTheme(jitter):
    """"
    [UxTheme.dll] HTHEME GetWindowTheme(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_HitTestThemeBackground(jitter):
    """"
    [UxTheme.dll] HRESULT HitTestThemeBackground(HTHEME hTheme, HDC hdc, int iPartId, int iStateId, [HitTestThemeBackgroundOptions] dwOptions, LPCRECT pRect, HRGN hrgn, POINT ptTest, [HitTestReturnCode*] pwHitTestCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "hdc", "iPartId", "iStateId", "dwOptions", "pRect", "hrgn", "ptTest", "pwHitTestCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_IsAppThemed(jitter):
    """"
    [UxTheme.dll] BOOL IsAppThemed()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_IsCompositionActive(jitter):
    """"
    [UxTheme.dll] BOOL IsCompositionActive()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_IsThemeActive(jitter):
    """"
    [UxTheme.dll] BOOL IsThemeActive()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_IsThemeBackgroundPartiallyTransparent(jitter):
    """"
    [UxTheme.dll] BOOL IsThemeBackgroundPartiallyTransparent(HTHEME hTheme, int iPartId, int iStateId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_IsThemeDialogTextureEnabled(jitter):
    """"
    [UxTheme.dll] BOOL IsThemeDialogTextureEnabled(HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_IsThemePartDefined(jitter):
    """"
    [UxTheme.dll] BOOL IsThemePartDefined(HTHEME hTheme, int iPartId, int iStateId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iPartId", "iStateId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_OpenThemeData(jitter):
    """"
    [UxTheme.dll] HTHEME OpenThemeData(HWND hwnd, LPCWSTR pszClassList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszClassList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_OpenThemeDataEx(jitter):
    """"
    [UxTheme.dll] HTHEME OpenThemeDataEx(HWND hwnd, LPCWSTR pszClassIdList, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszClassIdList", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_SetThemeAppProperties(jitter):
    """"
    [UxTheme.dll] void SetThemeAppProperties(DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_SetWindowTheme(jitter):
    """"
    [UxTheme.dll] HRESULT SetWindowTheme(HWND hwnd, LPCWSTR pszSubAppName, LPCWSTR pszSubIdList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszSubAppName", "pszSubIdList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_SetWindowThemeAttribute(jitter):
    """"
    [UxTheme.dll] HRESULT SetWindowThemeAttribute(HWND hwnd, WINDOWTHEMEATTRIBUTETYPE eAttribute, PVOID pvAttribute, DWORD cbAttribute)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "eAttribute", "pvAttribute", "cbAttribute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_GetThemeAnimationProperty(jitter):
    """"
    [UxTheme.dll] HRESULT GetThemeAnimationProperty(HTHEME hTheme, int iStoryboardId, int iTargetId, TA_PROPERTY eProperty, VOID* pvProperty, DWORD cbSize, DWORD pcbSizeOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTheme", "iStoryboardId", "iTargetId", "eProperty", "pvProperty", "cbSize", "pcbSizeOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_BeginPanningFeedback(jitter):
    """"
    [UxTheme.dll] BOOL BeginPanningFeedback(HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_EndPanningFeedback(jitter):
    """"
    [UxTheme.dll] BOOL EndPanningFeedback(HWND hwnd, BOOL fAnimateBack)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "fAnimateBack"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def uxtheme_UpdatePanningFeedback(jitter):
    """"
    [UxTheme.dll] BOOL UpdatePanningFeedback(HWND hwnd, LONG lTotalOverpanOffsetX, LONG lTotalOverpanOffsetY, BOOL fInInertia)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lTotalOverpanOffsetX", "lTotalOverpanOffsetY", "fInInertia"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
