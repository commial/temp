
def gdi32_BitBlt(jitter):
    """
    BOOL BitBlt(
        HDC hdcDest,
        int nXDest,
        int nYDest,
        int nWidth,
        int nHeight,
        HDC hdcSrc,
        int nXSrc,
        int nYSrc,
        [RasterOperationEnum] dwRop
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdcDest", "nXDest", "nYDest", "nWidth", "nHeight", "hdcSrc", "nXSrc", "nYSrc", "dwRop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateBitmap(jitter):
    """
    HBITMAP CreateBitmap(
        int nWidth,
        int nHeight,
        UINT cPlanes,
        UINT cBitsPerPel,
        const VOID* lpvBits
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nWidth", "nHeight", "cPlanes", "cBitsPerPel", "lpvBits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateBitmapIndirect(jitter):
    """
    HBITMAP CreateBitmapIndirect(
        const BITMAP* lpbm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpbm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateCompatibleBitmap(jitter):
    """
    HBITMAP CreateCompatibleBitmap(
        HDC hdc,
        int nWidth,
        int nHeight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nWidth", "nHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateDIBitmap(jitter):
    """
    HBITMAP CreateDIBitmap(
        HDC hdc,
        const BITMAPINFOHEADER* lpbmih,
        [CreateBitmapInitFlag] fdwInit,
        const VOID* lpbInit,
        const BITMAPINFO* lpbmi,
        [ColorUseEnum] fuUsage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpbmih", "fdwInit", "lpbInit", "lpbmi", "fuUsage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateDIBSection(jitter):
    """
    HBITMAP CreateDIBSection(
        HDC hdc,
        const BITMAPINFO* pbmi,
        [ColorUseEnum] iUsage,
        VOID** ppvBits,
        HANDLE hSection,
        DWORD dwOffset
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "pbmi", "iUsage", "ppvBits", "hSection", "dwOffset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ExtFloodFill(jitter):
    """
    BOOL ExtFloodFill(
        HDC hdc,
        int nXStart,
        int nYStart,
        COLORREF crColor,
        UINT fuFillType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nXStart", "nYStart", "crColor", "fuFillType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetBitmapDimensionEx(jitter):
    """
    BOOL GetBitmapDimensionEx(
        HBITMAP hBitmap,
        LPSIZE lpDimension
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hBitmap", "lpDimension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetDIBColorTable(jitter):
    """
    UINT GetDIBColorTable(
        HDC hdc,
        UINT uStartIndex,
        UINT cEntries,
        RGBQUAD* pColors
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "uStartIndex", "cEntries", "pColors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetDIBits(jitter):
    """
    int GetDIBits(
        HDC hdc,
        HBITMAP hbmp,
        UINT uStartScan,
        UINT cScanLines,
        LPVOID lpvBits,
        LPBITMAPINFO lpbi,
        [ColorUseEnum] uUsage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hbmp", "uStartScan", "cScanLines", "lpvBits", "lpbi", "uUsage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetPixel(jitter):
    """
    COLORREF GetPixel(
        HDC hdc,
        int nXPos,
        int nYPos
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nXPos", "nYPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetStretchBltMode(jitter):
    """
    int GetStretchBltMode(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_MaskBlt(jitter):
    """
    BOOL MaskBlt(
        HDC hdcDest,
        int nXDest,
        int nYDest,
        int nWidth,
        int nHeight,
        HDC hdcSrc,
        int nXSrc,
        int nYSrc,
        HBITMAP hbmMask,
        int xMask,
        int yMask,
        [RasterOperationEnum] dwRop
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdcDest", "nXDest", "nYDest", "nWidth", "nHeight", "hdcSrc", "nXSrc", "nYSrc", "hbmMask", "xMask", "yMask", "dwRop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PlgBlt(jitter):
    """
    BOOL PlgBlt(
        HDC hdcDest,
        const POINT* lpPoint,
        HDC hdcSrc,
        int nXSrc,
        int nYSrc,
        int nWidth,
        int nHeight,
        HBITMAP hbmMask,
        int xMask,
        int yMask
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdcDest", "lpPoint", "hdcSrc", "nXSrc", "nYSrc", "nWidth", "nHeight", "hbmMask", "xMask", "yMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetBitmapDimensionEx(jitter):
    """
    BOOL SetBitmapDimensionEx(
        HBITMAP hBitmap,
        int nWidth,
        int nHeight,
        LPSIZE lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hBitmap", "nWidth", "nHeight", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetDIBColorTable(jitter):
    """
    UINT SetDIBColorTable(
        HDC hdc,
        UINT uStartIndex,
        UINT cEntries,
        const RGBQUAD* pColors
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "uStartIndex", "cEntries", "pColors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetDIBits(jitter):
    """
    int SetDIBits(
        HDC hdc,
        HBITMAP hbmp,
        UINT uStartScan,
        UINT cScanLines,
        const VOID* lpvBits,
        const BITMAPINFO* lpbmi,
        [ColorUseEnum] fuColorUse
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hbmp", "uStartScan", "cScanLines", "lpvBits", "lpbmi", "fuColorUse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetDIBitsToDevice(jitter):
    """
    int SetDIBitsToDevice(
        HDC hdc,
        int XDest,
        int YDest,
        DWORD dwWidth,
        DWORD dwHeight,
        int XSrc,
        int YSrc,
        UINT uStartScan,
        UINT cScanLines,
        const VOID* lpvBits,
        const BITMAPINFO* lpbmi,
        [ColorUseEnum] fuColorUse
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "XDest", "YDest", "dwWidth", "dwHeight", "XSrc", "YSrc", "uStartScan", "cScanLines", "lpvBits", "lpbmi", "fuColorUse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetPixel(jitter):
    """
    COLORREF SetPixel(
        HDC hdc,
        int X,
        int Y,
        COLORREF crColor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "X", "Y", "crColor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetPixelV(jitter):
    """
    BOOL SetPixelV(
        HDC hdc,
        int X,
        int Y,
        COLORREF crColor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "X", "Y", "crColor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetStretchBltMode(jitter):
    """
    int SetStretchBltMode(
        HDC hdc,
        [StretchModeEnum] iStretchMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iStretchMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_StretchBlt(jitter):
    """
    BOOL StretchBlt(
        HDC hdcDest,
        int nXOriginDest,
        int nYOriginDest,
        int nWidthDest,
        int nHeightDest,
        HDC hdcSrc,
        int nXOriginSrc,
        int nYOriginSrc,
        int nWidthSrc,
        int nHeightSrc,
        [RasterOperationEnum] dwRop
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdcDest", "nXOriginDest", "nYOriginDest", "nWidthDest", "nHeightDest", "hdcSrc", "nXOriginSrc", "nYOriginSrc", "nWidthSrc", "nHeightSrc", "dwRop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_StretchDIBits(jitter):
    """
    int StretchDIBits(
        HDC hdc,
        int XDest,
        int YDest,
        int nDestWidth,
        int nDestHeight,
        int XSrc,
        int YSrc,
        int nSrcWidth,
        int nSrcHeight,
        const VOID* lpBits,
        const BITMAPINFO* lpBitsInfo,
        [ColorUseEnum] iUsage,
        [RasterOperationEnum] dwRop
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "XDest", "YDest", "nDestWidth", "nDestHeight", "XSrc", "YSrc", "nSrcWidth", "nSrcHeight", "lpBits", "lpBitsInfo", "iUsage", "dwRop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateDiscardableBitmap(jitter):
    """
    HBITMAP CreateDiscardableBitmap(
        HDC hdc,
        int nWidth,
        int nHeight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nWidth", "nHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_FloodFill(jitter):
    """
    BOOL FloodFill(
        HDC hdc,
        int nXStart,
        int nYStart,
        COLORREF crFill
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nXStart", "nYStart", "crFill"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetBitmapBits(jitter):
    """
    LONG GetBitmapBits(
        HBITMAP hbmp,
        LONG cbBuffer,
        LPVOID lpvBits
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbmp", "cbBuffer", "lpvBits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetBitmapBits(jitter):
    """
    LONG SetBitmapBits(
        HBITMAP hbmp,
        DWORD cBytes,
        const VOID* lpBits
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbmp", "cBytes", "lpBits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateBrushIndirect(jitter):
    """
    HBRUSH CreateBrushIndirect(
        const LOGBRUSH* lplb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lplb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateDIBPatternBrushPt(jitter):
    """
    HBRUSH CreateDIBPatternBrushPt(
        const VOID* lpPackedDIB,
        [ColorUseEnum] iUsage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpPackedDIB", "iUsage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateHatchBrush(jitter):
    """
    HBRUSH CreateHatchBrush(
        [HatchStyle] fnStyle,
        COLORREF clrref
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fnStyle", "clrref"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreatePatternBrush(jitter):
    """
    HBRUSH CreatePatternBrush(
        HBITMAP hbmp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbmp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateSolidBrush(jitter):
    """
    HBRUSH CreateSolidBrush(
        COLORREF crColor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["crColor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetBrushOrgEx(jitter):
    """
    BOOL GetBrushOrgEx(
        HDC hdc,
        LPPOINT lppt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lppt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PatBlt(jitter):
    """
    BOOL PatBlt(
        HDC hdc,
        int nXLeft,
        int nYLeft,
        int nWidth,
        int nHeight,
        [RasterOperationEnum] dwRop
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nXLeft", "nYLeft", "nWidth", "nHeight", "dwRop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetBrushOrgEx(jitter):
    """
    BOOL SetBrushOrgEx(
        HDC hdc,
        int nXOrg,
        int nYOrg,
        LPPOINT lppt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nXOrg", "nYOrg", "lppt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateDIBPatternBrush(jitter):
    """
    HBRUSH CreateDIBPatternBrush(
        HGLOBAL hglbDIBPacked,
        UINT fuColorSpec
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hglbDIBPacked", "fuColorSpec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ExcludeClipRect(jitter):
    """
    int ExcludeClipRect(
        HDC hdc,
        int nLeftRect,
        int nTopRect,
        int nRightRect,
        int nBottomRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nLeftRect", "nTopRect", "nRightRect", "nBottomRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ExtSelectClipRgn(jitter):
    """
    int ExtSelectClipRgn(
        HDC hdc,
        HRGN hrgn,
        [RgnMode] fnMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hrgn", "fnMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetClipBox(jitter):
    """
    int GetClipBox(
        HDC hdc,
        LPRECT lprc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetClipRgn(jitter):
    """
    int GetClipRgn(
        HDC hdc,
        HRGN hrgn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hrgn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetMetaRgn(jitter):
    """
    int GetMetaRgn(
        HDC hdc,
        HRGN hrgn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hrgn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetRandomRgn(jitter):
    """
    int GetRandomRgn(
        HDC hdc,
        HRGN hrgn,
        [RandomRgnEnum] iNum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hrgn", "iNum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_IntersectClipRect(jitter):
    """
    int IntersectClipRect(
        HDC hdc,
        int nLeftRect,
        int nTopRect,
        int nRightRect,
        int nBottomRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nLeftRect", "nTopRect", "nRightRect", "nBottomRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_OffsetClipRgn(jitter):
    """
    int OffsetClipRgn(
        HDC hdc,
        int nXOffset,
        int nYOffset
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nXOffset", "nYOffset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PtVisible(jitter):
    """
    [BOOL_NUMBER] PtVisible(
        HDC hdc,
        int X,
        int Y
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "X", "Y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_RectVisible(jitter):
    """
    [BOOL_NUMBER] RectVisible(
        HDC hdc,
        const RECT* lprc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SelectClipPath(jitter):
    """
    BOOL SelectClipPath(
        HDC hdc,
        int iMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SelectClipRgn(jitter):
    """
    int SelectClipRgn(
        HDC hdc,
        HRGN hrgn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hrgn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetMetaRgn(jitter):
    """
    int SetMetaRgn(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_AnimatePalette(jitter):
    """
    BOOL AnimatePalette(
        HPALETTE hpal,
        UINT iStartIndex,
        UINT cEntries,
        const PALETTEENTRY* ppe
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hpal", "iStartIndex", "cEntries", "ppe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateHalftonePalette(jitter):
    """
    HPALETTE CreateHalftonePalette(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreatePalette(jitter):
    """
    HPALETTE CreatePalette(
        const LOGPALETTE* lplgpl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lplgpl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetColorAdjustment(jitter):
    """
    BOOL GetColorAdjustment(
        HDC hdc,
        LPCOLORADJUSTMENT lpca
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpca"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetNearestColor(jitter):
    """
    COLORREF GetNearestColor(
        HDC hdc,
        COLORREF crColor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "crColor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetNearestPaletteIndex(jitter):
    """
    UINT GetNearestPaletteIndex(
        HPALETTE hpal,
        COLORREF crColor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hpal", "crColor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetPaletteEntries(jitter):
    """
    UINT GetPaletteEntries(
        HPALETTE hpal,
        UINT iStartIndex,
        UINT nEntries,
        LPPALETTEENTRY lppe
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hpal", "iStartIndex", "nEntries", "lppe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetSystemPaletteEntries(jitter):
    """
    UINT GetSystemPaletteEntries(
        HDC hdc,
        UINT iStartIndex,
        UINT nEntries,
        LPPALETTEENTRY lppe
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iStartIndex", "nEntries", "lppe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetSystemPaletteUse(jitter):
    """
    UINT GetSystemPaletteUse(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_RealizePalette(jitter):
    """
    UINT RealizePalette(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ResizePalette(jitter):
    """
    BOOL ResizePalette(
        HPALETTE hpal,
        UINT nEntries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hpal", "nEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SelectPalette(jitter):
    """
    HPALETTE SelectPalette(
        HDC hdc,
        HPALETTE hpal,
        BOOL bForceBackground
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hpal", "bForceBackground"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetColorAdjustment(jitter):
    """
    BOOL SetColorAdjustment(
        HDC hdc,
        const COLORADJUSTMENT* lpca
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpca"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetPaletteEntries(jitter):
    """
    UINT SetPaletteEntries(
        HPALETTE hpal,
        UINT iStart,
        UINT cEntries,
        const PALETTEENTRY* lppe
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hpal", "iStart", "cEntries", "lppe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetSystemPaletteUse(jitter):
    """
    UINT SetSystemPaletteUse(
        HDC hdc,
        UINT uUsage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "uUsage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_UnrealizeObject(jitter):
    """
    BOOL UnrealizeObject(
        HGDIOBJ hgdiobj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hgdiobj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_UpdateColors(jitter):
    """
    BOOL UpdateColors(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CombineTransform(jitter):
    """
    BOOL CombineTransform(
        LPXFORM lpxformResult,
        const XFORM* lpxform1,
        const XFORM* lpxform2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpxformResult", "lpxform1", "lpxform2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_DPtoLP(jitter):
    """
    BOOL DPtoLP(
        HDC hdc,
        LPPOINT lpPoints,
        int nCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpPoints", "nCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetCurrentPositionEx(jitter):
    """
    BOOL GetCurrentPositionEx(
        HDC hdc,
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetGraphicsMode(jitter):
    """
    int GetGraphicsMode(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetMapMode(jitter):
    """
    int GetMapMode(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetViewportExtEx(jitter):
    """
    BOOL GetViewportExtEx(
        HDC hdc,
        LPSIZE lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetViewportOrgEx(jitter):
    """
    BOOL GetViewportOrgEx(
        HDC hdc,
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetWindowExtEx(jitter):
    """
    BOOL GetWindowExtEx(
        HDC hdc,
        LPSIZE lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetWindowOrgEx(jitter):
    """
    BOOL GetWindowOrgEx(
        HDC hdc,
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetWorldTransform(jitter):
    """
    BOOL GetWorldTransform(
        HDC hdc,
        LPXFORM lpXform
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpXform"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_LPtoDP(jitter):
    """
    BOOL LPtoDP(
        HDC hdc,
        LPPOINT lpPoints,
        int nCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpPoints", "nCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ModifyWorldTransform(jitter):
    """
    BOOL ModifyWorldTransform(
        HDC hdc,
        const XFORM* lpXform,
        [ModifyWorldTransformMode] iMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpXform", "iMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_OffsetViewportOrgEx(jitter):
    """
    BOOL OffsetViewportOrgEx(
        HDC hdc,
        int nXOffset,
        int nYOffset,
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nXOffset", "nYOffset", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_OffsetWindowOrgEx(jitter):
    """
    BOOL OffsetWindowOrgEx(
        HDC hdc,
        int nXOffset,
        int nYOffset,
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nXOffset", "nYOffset", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ScaleViewportExtEx(jitter):
    """
    BOOL ScaleViewportExtEx(
        HDC hdc,
        int Xnum,
        int Xdenom,
        int Ynum,
        int Ydenom,
        LPSIZE lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "Xnum", "Xdenom", "Ynum", "Ydenom", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ScaleWindowExtEx(jitter):
    """
    BOOL ScaleWindowExtEx(
        HDC hdc,
        int Xnum,
        int Xdenom,
        int Ynum,
        int Ydenom,
        LPSIZE lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "Xnum", "Xdenom", "Ynum", "Ydenom", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetGraphicsMode(jitter):
    """
    int SetGraphicsMode(
        HDC hdc,
        [GraphicsModes] iMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetMapMode(jitter):
    """
    int SetMapMode(
        HDC hdc,
        [MappingMode] fnMapMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "fnMapMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetViewportExtEx(jitter):
    """
    BOOL SetViewportExtEx(
        HDC hdc,
        int nXExtent,
        int nYExtent,
        LPSIZE lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nXExtent", "nYExtent", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetViewportOrgEx(jitter):
    """
    BOOL SetViewportOrgEx(
        HDC hdc,
        int X,
        int Y,
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "X", "Y", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetWindowExtEx(jitter):
    """
    BOOL SetWindowExtEx(
        HDC hdc,
        int nXExtent,
        int nYExtent,
        LPSIZE lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nXExtent", "nYExtent", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetWindowOrgEx(jitter):
    """
    BOOL SetWindowOrgEx(
        HDC hdc,
        int X,
        int Y,
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "X", "Y", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetWorldTransform(jitter):
    """
    BOOL SetWorldTransform(
        HDC hdc,
        const XFORM* lpXform
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpXform"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CancelDC(jitter):
    """
    BOOL CancelDC(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateCompatibleDC(jitter):
    """
    HDC CreateCompatibleDC(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateDC(jitter, get_str, set_str):
    """
    HDC CreateDC(
        LPCTSTR lpszDriver,
        LPCTSTR lpszDevice,
        LPCTSTR lpszOutput,
        const DEVMODE* lpInitData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDriver", "lpszDevice", "lpszOutput", "lpInitData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateDCA(jitter):
    gdi32_CreateDC(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_CreateDCW(jitter):
    gdi32_CreateDC(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_CreateIC(jitter, get_str, set_str):
    """
    HDC CreateIC(
        LPCTSTR lpszDriver,
        LPCTSTR lpszDevice,
        LPCTSTR lpszOutput,
        const DEVMODE* lpdvmInit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDriver", "lpszDevice", "lpszOutput", "lpdvmInit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateICA(jitter):
    gdi32_CreateIC(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_CreateICW(jitter):
    gdi32_CreateIC(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_DeleteDC(jitter):
    """
    BOOL DeleteDC(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_DeleteObject(jitter):
    """
    BOOL DeleteObject(
        HGDIOBJ hObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_DrawEscape(jitter):
    """
    int DrawEscape(
        HDC hdc,
        int nEscape,
        int cbInput,
        LPCSTR lpszInData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nEscape", "cbInput", "lpszInData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_EnumObjects(jitter):
    """
    int EnumObjects(
        HDC hdc,
        int nObjectType,
        GOBJENUMPROC lpObjectFunc,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nObjectType", "lpObjectFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetCurrentObject(jitter):
    """
    HGDIOBJ GetCurrentObject(
        HDC hdc,
        [ObjectType] uObjectType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "uObjectType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetDCBrushColor(jitter):
    """
    COLORREF GetDCBrushColor(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetDCOrgEx(jitter):
    """
    BOOL GetDCOrgEx(
        HDC hdc,
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetDCPenColor(jitter):
    """
    COLORREF GetDCPenColor(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetDeviceCaps(jitter):
    """
    int GetDeviceCaps(
        HDC hdc,
        [DeviceCapsEnum] nIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetLayout(jitter):
    """
    DWORD GetLayout(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetObject(jitter, get_str, set_str):
    """
    int GetObject(
        HGDIOBJ hgdiobj,
        int cbBuffer,
        LPVOID lpvObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hgdiobj", "cbBuffer", "lpvObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetObjectA(jitter):
    gdi32_GetObject(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetObjectW(jitter):
    gdi32_GetObject(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetObjectType(jitter):
    """
    DWORD GetObjectType(
        HGDIOBJ h
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["h"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetStockObject(jitter):
    """
    HGDIOBJ GetStockObject(
        [STOCK_OBJECT] fnObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fnObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ResetDC(jitter, get_str, set_str):
    """
    HDC ResetDC(
        HDC hdc,
        const DEVMODE* lpInitData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpInitData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ResetDCA(jitter):
    gdi32_ResetDC(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_ResetDCW(jitter):
    gdi32_ResetDC(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_RestoreDC(jitter):
    """
    BOOL RestoreDC(
        HDC hdc,
        int nSavedDC
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nSavedDC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SaveDC(jitter):
    """
    int SaveDC(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SelectObject(jitter):
    """
    HGDIOBJ SelectObject(
        HDC hdc,
        HGDIOBJ hgdiobj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hgdiobj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetDCBrushColor(jitter):
    """
    COLORREF SetDCBrushColor(
        HDC hdc,
        COLORREF crColor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "crColor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetDCPenColor(jitter):
    """
    COLORREF SetDCPenColor(
        HDC hdc,
        COLORREF crColor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "crColor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetLayout(jitter):
    """
    DWORD SetLayout(
        HDC hdc,
        [LayoutFlags] dwLayout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "dwLayout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_Chord(jitter):
    """
    BOOL Chord(
        HDC hdc,
        int nLeftRect,
        int nTopRect,
        int nRightRect,
        int nBottomRect,
        int nXRadial1,
        int nYRadial1,
        int nXRadial2,
        int nYRadial2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nLeftRect", "nTopRect", "nRightRect", "nBottomRect", "nXRadial1", "nYRadial1", "nXRadial2", "nYRadial2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_Ellipse(jitter):
    """
    BOOL Ellipse(
        HDC hdc,
        int nLeftRect,
        int nTopRect,
        int nRightRect,
        int nBottomRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nLeftRect", "nTopRect", "nRightRect", "nBottomRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_Pie(jitter):
    """
    BOOL Pie(
        HDC hdc,
        int nLeftRect,
        int nTopRect,
        int nRightRect,
        int nBottomRect,
        int nXRadial1,
        int nYRadial1,
        int nXRadial2,
        int nYRadial2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nLeftRect", "nTopRect", "nRightRect", "nBottomRect", "nXRadial1", "nYRadial1", "nXRadial2", "nYRadial2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_Polygon(jitter):
    """
    BOOL Polygon(
        HDC hdc,
        const POINT* lpPoints,
        int nCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpPoints", "nCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PolyPolygon(jitter):
    """
    BOOL PolyPolygon(
        HDC hdc,
        const POINT* lpPoints,
        const INT* lpPolyCounts,
        int nCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpPoints", "lpPolyCounts", "nCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_Rectangle(jitter):
    """
    BOOL Rectangle(
        HDC hdc,
        int nLeftRect,
        int nTopRect,
        int nRightRect,
        int nBottomRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nLeftRect", "nTopRect", "nRightRect", "nBottomRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_RoundRect(jitter):
    """
    BOOL RoundRect(
        HDC hdc,
        int nLeftRect,
        int nTopRect,
        int nRightRect,
        int nBottomRect,
        int nWidth,
        int nHeight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nLeftRect", "nTopRect", "nRightRect", "nBottomRect", "nWidth", "nHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_AddFontMemResourceEx(jitter):
    """
    HANDLE AddFontMemResourceEx(
        PVOID pbFont,
        DWORD cbFont,
        PVOID pdv,
        DWORD* pcFonts
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbFont", "cbFont", "pdv", "pcFonts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_AddFontResource(jitter, get_str, set_str):
    """
    int AddFontResource(
        LPCTSTR lpszFilename
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFilename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_AddFontResourceA(jitter):
    gdi32_AddFontResource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_AddFontResourceW(jitter):
    gdi32_AddFontResource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_AddFontResourceEx(jitter, get_str, set_str):
    """
    int AddFontResourceEx(
        LPCTSTR lpszFilename,
        DWORD fl,
        PVOID pdv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFilename", "fl", "pdv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_AddFontResourceExA(jitter):
    gdi32_AddFontResourceEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_AddFontResourceExW(jitter):
    gdi32_AddFontResourceEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_CreateFont(jitter, get_str, set_str):
    """
    HFONT CreateFont(
        int nHeight,
        int nWidth,
        int nEscapement,
        int nOrientation,
        [FontWeight] fnWeight,
        DWORD fdwItalic,
        DWORD fdwUnderline,
        DWORD fdwStrikeOut,
        [FontCharset] fdwCharSet,
        [FontOutputPrecision] fdwOutputPrecision,
        [FontClipPrecision] fdwClipPrecision,
        [FontQuality] fdwQuality,
        [FontPitchAndFamily] fdwPitchAndFamily,
        LPCTSTR lpszFace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nHeight", "nWidth", "nEscapement", "nOrientation", "fnWeight", "fdwItalic", "fdwUnderline", "fdwStrikeOut", "fdwCharSet", "fdwOutputPrecision", "fdwClipPrecision", "fdwQuality", "fdwPitchAndFamily", "lpszFace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateFontA(jitter):
    gdi32_CreateFont(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_CreateFontW(jitter):
    gdi32_CreateFont(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_CreateFontIndirect(jitter, get_str, set_str):
    """
    HFONT CreateFontIndirect(
        const LOGFONT* lplf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lplf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateFontIndirectA(jitter):
    gdi32_CreateFontIndirect(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_CreateFontIndirectW(jitter):
    gdi32_CreateFontIndirect(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_CreateFontIndirectEx(jitter, get_str, set_str):
    """
    HFONT CreateFontIndirectEx(
        const ENUMLOGFONTEXDV* penumlfex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["penumlfex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateFontIndirectExA(jitter):
    gdi32_CreateFontIndirectEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_CreateFontIndirectExW(jitter):
    gdi32_CreateFontIndirectEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_CreateScalableFontResource(jitter, get_str, set_str):
    """
    BOOL CreateScalableFontResource(
        DWORD fdwHidden,
        LPCTSTR lpszFontRes,
        LPCTSTR lpszFontFile,
        LPCTSTR lpszCurrentPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fdwHidden", "lpszFontRes", "lpszFontFile", "lpszCurrentPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateScalableFontResourceA(jitter):
    gdi32_CreateScalableFontResource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_CreateScalableFontResourceW(jitter):
    gdi32_CreateScalableFontResource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_EnumFontFamiliesEx(jitter, get_str, set_str):
    """
    int EnumFontFamiliesEx(
        HDC hdc,
        LPLOGFONT lpLogfont,
        FONTENUMPROC lpEnumFontFamExProc,
        LPARAM lParam,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpLogfont", "lpEnumFontFamExProc", "lParam", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_EnumFontFamiliesExA(jitter):
    gdi32_EnumFontFamiliesEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_EnumFontFamiliesExW(jitter):
    gdi32_EnumFontFamiliesEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_ExtTextOut(jitter, get_str, set_str):
    """
    BOOL ExtTextOut(
        HDC hdc,
        int X,
        int Y,
        [ExtTextOutFlags] fuOptions,
        const RECT* lprc,
        LPCTSTR lpString,
        UINT cbCount,
        const INT* lpDx
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "X", "Y", "fuOptions", "lprc", "lpString", "cbCount", "lpDx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ExtTextOutA(jitter):
    gdi32_ExtTextOut(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_ExtTextOutW(jitter):
    gdi32_ExtTextOut(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetAspectRatioFilterEx(jitter):
    """
    BOOL GetAspectRatioFilterEx(
        HDC hdc,
        LPSIZE lpAspectRatio
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpAspectRatio"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetCharABCWidths(jitter, get_str, set_str):
    """
    BOOL GetCharABCWidths(
        HDC hdc,
        UINT uFirstChar,
        UINT uLastChar,
        LPABC lpabc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "uFirstChar", "uLastChar", "lpabc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetCharABCWidthsA(jitter):
    gdi32_GetCharABCWidths(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetCharABCWidthsW(jitter):
    gdi32_GetCharABCWidths(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetCharABCWidthsFloat(jitter, get_str, set_str):
    """
    BOOL GetCharABCWidthsFloat(
        HDC hdc,
        UINT iFirstChar,
        UINT iLastChar,
        LPABCFLOAT lpABCF
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iFirstChar", "iLastChar", "lpABCF"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetCharABCWidthsFloatA(jitter):
    gdi32_GetCharABCWidthsFloat(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetCharABCWidthsFloatW(jitter):
    gdi32_GetCharABCWidthsFloat(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetCharABCWidthsI(jitter):
    """
    BOOL GetCharABCWidthsI(
        HDC hdc,
        UINT giFirst,
        UINT cgi,
        LPWORD pgi,
        LPABC lpabc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "giFirst", "cgi", "pgi", "lpabc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetCharacterPlacement(jitter, get_str, set_str):
    """
    DWORD GetCharacterPlacement(
        HDC hdc,
        LPCTSTR lpString,
        int nCount,
        int nMaxExtent,
        LPGCP_RESULTS lpResults,
        [GCP_FLAGS] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpString", "nCount", "nMaxExtent", "lpResults", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetCharacterPlacementA(jitter):
    gdi32_GetCharacterPlacement(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetCharacterPlacementW(jitter):
    gdi32_GetCharacterPlacement(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetCharWidth32(jitter, get_str, set_str):
    """
    BOOL GetCharWidth32(
        HDC hdc,
        UINT iFirstChar,
        UINT iLastChar,
        LPINT lpBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iFirstChar", "iLastChar", "lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetCharWidth32A(jitter):
    gdi32_GetCharWidth32(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetCharWidth32W(jitter):
    gdi32_GetCharWidth32(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetCharWidthFloat(jitter, get_str, set_str):
    """
    BOOL GetCharWidthFloat(
        HDC hdc,
        UINT iFirstChar,
        UINT iLastChar,
        PFLOAT pxBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iFirstChar", "iLastChar", "pxBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetCharWidthFloatA(jitter):
    gdi32_GetCharWidthFloat(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetCharWidthFloatW(jitter):
    gdi32_GetCharWidthFloat(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetCharWidthI(jitter):
    """
    BOOL GetCharWidthI(
        HDC hdc,
        UINT giFirst,
        UINT cgi,
        LPWORD pgi,
        LPINT lpBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "giFirst", "cgi", "pgi", "lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetFontData(jitter):
    """
    DWORD GetFontData(
        HDC hdc,
        DWORD dwTable,
        DWORD dwOffset,
        LPVOID lpvBuffer,
        DWORD cbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "dwTable", "dwOffset", "lpvBuffer", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetFontLanguageInfo(jitter):
    """
    DWORD GetFontLanguageInfo(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetFontUnicodeRanges(jitter):
    """
    DWORD GetFontUnicodeRanges(
        HDC hdc,
        LPGLYPHSET lpgs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpgs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetGlyphIndices(jitter, get_str, set_str):
    """
    DWORD GetGlyphIndices(
        HDC hdc,
        LPCTSTR lpstr,
        int c,
        LPWORD pgi,
        [GetGlyphIndicesFlag] fl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpstr", "c", "pgi", "fl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetGlyphIndicesA(jitter):
    gdi32_GetGlyphIndices(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetGlyphIndicesW(jitter):
    gdi32_GetGlyphIndices(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetGlyphOutline(jitter, get_str, set_str):
    """
    DWORD GetGlyphOutline(
        HDC hdc,
        UINT uChar,
        [GetGlyphOutlineFormat] uFormat,
        LPGLYPHMETRICS lpgm,
        DWORD cbBuffer,
        LPVOID lpvBuffer,
        const MAT2* lpmat2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "uChar", "uFormat", "lpgm", "cbBuffer", "lpvBuffer", "lpmat2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetGlyphOutlineA(jitter):
    gdi32_GetGlyphOutline(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetGlyphOutlineW(jitter):
    gdi32_GetGlyphOutline(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetKerningPairs(jitter, get_str, set_str):
    """
    DWORD GetKerningPairs(
        HDC hdc,
        DWORD nNumPairs,
        LPKERNINGPAIR lpkrnpair
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nNumPairs", "lpkrnpair"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetKerningPairsA(jitter):
    gdi32_GetKerningPairs(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetKerningPairsW(jitter):
    gdi32_GetKerningPairs(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetOutlineTextMetrics(jitter, get_str, set_str):
    """
    UINT GetOutlineTextMetrics(
        HDC hdc,
        UINT cbData,
        LPOUTLINETEXTMETRIC lpOTM
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "cbData", "lpOTM"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetOutlineTextMetricsA(jitter):
    gdi32_GetOutlineTextMetrics(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetOutlineTextMetricsW(jitter):
    gdi32_GetOutlineTextMetrics(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetRasterizerCaps(jitter):
    """
    BOOL GetRasterizerCaps(
        LPRASTERIZER_STATUS lprs,
        UINT cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprs", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetTextAlign(jitter):
    """
    [TextAlignFlag] GetTextAlign(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetTextCharacterExtra(jitter):
    """
    int GetTextCharacterExtra(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetTextColor(jitter):
    """
    COLORREF GetTextColor(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetTextExtentExPoint(jitter, get_str, set_str):
    """
    BOOL GetTextExtentExPoint(
        HDC hdc,
        LPCTSTR lpszStr,
        int cchString,
        int nMaxExtent,
        LPINT lpnFit,
        LPINT alpDx,
        LPSIZE lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpszStr", "cchString", "nMaxExtent", "lpnFit", "alpDx", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetTextExtentExPointA(jitter):
    gdi32_GetTextExtentExPoint(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetTextExtentExPointW(jitter):
    gdi32_GetTextExtentExPoint(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetTextExtentExPointI(jitter):
    """
    BOOL GetTextExtentExPointI(
        HDC hdc,
        LPWORD pgiIn,
        int cgi,
        int nMaxExtent,
        LPINT lpnFit,
        LPINT alpDx,
        LPSIZE lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "pgiIn", "cgi", "nMaxExtent", "lpnFit", "alpDx", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetTextExtentPoint32(jitter, get_str, set_str):
    """
    BOOL GetTextExtentPoint32(
        HDC hdc,
        LPCTSTR lpString,
        int c,
        LPSIZE lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpString", "c", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetTextExtentPoint32A(jitter):
    gdi32_GetTextExtentPoint32(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetTextExtentPoint32W(jitter):
    gdi32_GetTextExtentPoint32(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetTextExtentPointI(jitter):
    """
    BOOL GetTextExtentPointI(
        HDC hdc,
        LPWORD pgiIn,
        int cgi,
        LPSIZE lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "pgiIn", "cgi", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetTextFace(jitter, get_str, set_str):
    """
    int GetTextFace(
        HDC hdc,
        int nCount,
        LPTSTR lpFaceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nCount", "lpFaceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetTextFaceA(jitter):
    gdi32_GetTextFace(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetTextFaceW(jitter):
    gdi32_GetTextFace(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetTextMetrics(jitter, get_str, set_str):
    """
    BOOL GetTextMetrics(
        HDC hdc,
        LPTEXTMETRIC lptm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lptm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetTextMetricsA(jitter):
    gdi32_GetTextMetrics(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetTextMetricsW(jitter):
    gdi32_GetTextMetrics(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_PolyTextOut(jitter, get_str, set_str):
    """
    BOOL PolyTextOut(
        HDC hdc,
        const POLYTEXT* pptxt,
        int cStrings
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "pptxt", "cStrings"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PolyTextOutA(jitter):
    gdi32_PolyTextOut(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_PolyTextOutW(jitter):
    gdi32_PolyTextOut(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_RemoveFontMemResourceEx(jitter):
    """
    BOOL RemoveFontMemResourceEx(
        HANDLE fh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_RemoveFontResource(jitter, get_str, set_str):
    """
    BOOL RemoveFontResource(
        LPCTSTR lpFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_RemoveFontResourceA(jitter):
    gdi32_RemoveFontResource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_RemoveFontResourceW(jitter):
    gdi32_RemoveFontResource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_RemoveFontResourceEx(jitter, get_str, set_str):
    """
    BOOL RemoveFontResourceEx(
        LPCTSTR lpFileName,
        DWORD fl,
        PVOID pdv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "fl", "pdv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_RemoveFontResourceExA(jitter):
    gdi32_RemoveFontResourceEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_RemoveFontResourceExW(jitter):
    gdi32_RemoveFontResourceEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_SetMapperFlags(jitter):
    """
    DWORD SetMapperFlags(
        HDC hdc,
        DWORD dwFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "dwFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetTextAlign(jitter):
    """
    [TextAlignFlag] SetTextAlign(
        HDC hdc,
        [TextAlignFlag] fMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "fMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetTextCharacterExtra(jitter):
    """
    int SetTextCharacterExtra(
        HDC hdc,
        int nCharExtra
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nCharExtra"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetTextColor(jitter):
    """
    COLORREF SetTextColor(
        HDC hdc,
        COLORREF crColor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "crColor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetTextJustification(jitter):
    """
    BOOL SetTextJustification(
        HDC hdc,
        int nBreakExtra,
        int nBreakCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nBreakExtra", "nBreakCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_TextOut(jitter, get_str, set_str):
    """
    BOOL TextOut(
        HDC hdc,
        int nXStart,
        int nYStart,
        LPCTSTR lpString,
        int cbString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nXStart", "nYStart", "lpString", "cbString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_TextOutA(jitter):
    gdi32_TextOut(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_TextOutW(jitter):
    gdi32_TextOut(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_EnumFontFamilies(jitter, get_str, set_str):
    """
    int EnumFontFamilies(
        HDC hdc,
        LPCTSTR lpszFamily,
        FONTENUMPROC lpEnumFontFamProc,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpszFamily", "lpEnumFontFamProc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_EnumFontFamiliesA(jitter):
    gdi32_EnumFontFamilies(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_EnumFontFamiliesW(jitter):
    gdi32_EnumFontFamilies(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_EnumFonts(jitter, get_str, set_str):
    """
    int EnumFonts(
        HDC hdc,
        LPCTSTR lpFaceName,
        FONTENUMPROC lpFontFunc,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpFaceName", "lpFontFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_EnumFontsA(jitter):
    gdi32_EnumFonts(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_EnumFontsW(jitter):
    gdi32_EnumFonts(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetCharWidth(jitter, get_str, set_str):
    """
    BOOL GetCharWidth(
        HDC hdc,
        UINT iFirstChar,
        UINT iLastChar,
        LPINT lpBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iFirstChar", "iLastChar", "lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetCharWidthA(jitter):
    gdi32_GetCharWidth(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetCharWidthW(jitter):
    gdi32_GetCharWidth(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetTextExtentPoint(jitter, get_str, set_str):
    """
    BOOL GetTextExtentPoint(
        HDC hdc,
        LPCTSTR lpString,
        int cbString,
        LPSIZE lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpString", "cbString", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetTextExtentPointA(jitter):
    gdi32_GetTextExtentPoint(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetTextExtentPointW(jitter):
    gdi32_GetTextExtentPoint(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_AngleArc(jitter):
    """
    BOOL AngleArc(
        HDC hdc,
        int X,
        int Y,
        DWORD dwRadius,
        FLOAT eStartAngle,
        FLOAT eSweepAngle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "X", "Y", "dwRadius", "eStartAngle", "eSweepAngle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_Arc(jitter):
    """
    BOOL Arc(
        HDC hdc,
        int nLeftRect,
        int nTopRect,
        int nRightRect,
        int nBottomRect,
        int nXStartArc,
        int nYStartArc,
        int nXEndArc,
        int nYEndArc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nLeftRect", "nTopRect", "nRightRect", "nBottomRect", "nXStartArc", "nYStartArc", "nXEndArc", "nYEndArc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ArcTo(jitter):
    """
    BOOL ArcTo(
        HDC hdc,
        int nLeftRect,
        int nTopRect,
        int nRightRect,
        int nBottomRect,
        int nXRadial1,
        int nYRadial1,
        int nXRadial2,
        int nYRadial2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nLeftRect", "nTopRect", "nRightRect", "nBottomRect", "nXRadial1", "nYRadial1", "nXRadial2", "nYRadial2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetArcDirection(jitter):
    """
    int GetArcDirection(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_LineDDA(jitter):
    """
    BOOL LineDDA(
        int nXStart,
        int nYStart,
        int nXEnd,
        int nYEnd,
        LINEDDAPROC lpLineFunc,
        LPARAM lpData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nXStart", "nYStart", "nXEnd", "nYEnd", "lpLineFunc", "lpData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_LineTo(jitter):
    """
    BOOL LineTo(
        HDC hdc,
        int nXEnd,
        int nYEnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nXEnd", "nYEnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_MoveToEx(jitter):
    """
    BOOL MoveToEx(
        HDC hdc,
        int X,
        int Y,
        LPPOINT lpPoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "X", "Y", "lpPoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PolyBezier(jitter):
    """
    BOOL PolyBezier(
        HDC hdc,
        const POINT* lppt,
        DWORD cPoints
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lppt", "cPoints"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PolyBezierTo(jitter):
    """
    BOOL PolyBezierTo(
        HDC hdc,
        const POINT* lppt,
        DWORD cCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lppt", "cCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PolyDraw(jitter):
    """
    BOOL PolyDraw(
        HDC hdc,
        const POINT* lppt,
        [POINT_TYPE*] lpbTypes,
        int cCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lppt", "lpbTypes", "cCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_Polyline(jitter):
    """
    BOOL Polyline(
        HDC hdc,
        const POINT* lppt,
        int cPoints
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lppt", "cPoints"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PolylineTo(jitter):
    """
    BOOL PolylineTo(
        HDC hdc,
        const POINT* lppt,
        DWORD cCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lppt", "cCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PolyPolyline(jitter):
    """
    BOOL PolyPolyline(
        HDC hdc,
        const POINT* lppt,
        const DWORD* lpdwPolyPoints,
        DWORD cCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lppt", "lpdwPolyPoints", "cCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetArcDirection(jitter):
    """
    int SetArcDirection(
        HDC hdc,
        int ArcDirection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "ArcDirection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CloseEnhMetaFile(jitter):
    """
    HENHMETAFILE CloseEnhMetaFile(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CopyEnhMetaFile(jitter, get_str, set_str):
    """
    HENHMETAFILE CopyEnhMetaFile(
        HENHMETAFILE hemfSrc,
        LPCTSTR lpszFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hemfSrc", "lpszFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CopyEnhMetaFileA(jitter):
    gdi32_CopyEnhMetaFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_CopyEnhMetaFileW(jitter):
    gdi32_CopyEnhMetaFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_CreateEnhMetaFile(jitter, get_str, set_str):
    """
    HDC CreateEnhMetaFile(
        HDC hdcRef,
        LPCTSTR lpFilename,
        const RECT* lpRect,
        LPCTSTR lpDescription
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdcRef", "lpFilename", "lpRect", "lpDescription"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateEnhMetaFileA(jitter):
    gdi32_CreateEnhMetaFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_CreateEnhMetaFileW(jitter):
    gdi32_CreateEnhMetaFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_DeleteEnhMetaFile(jitter):
    """
    BOOL DeleteEnhMetaFile(
        HENHMETAFILE hemf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hemf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_EnumEnhMetaFile(jitter):
    """
    BOOL EnumEnhMetaFile(
        HDC hdc,
        HENHMETAFILE hemf,
        ENHMFENUMPROC lpEnhMetaFunc,
        LPVOID lpData,
        const RECT* lpRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hemf", "lpEnhMetaFunc", "lpData", "lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GdiComment(jitter):
    """
    BOOL GdiComment(
        HDC hdc,
        UINT cbSize,
        const BYTE* lpData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "cbSize", "lpData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetEnhMetaFile(jitter, get_str, set_str):
    """
    HENHMETAFILE GetEnhMetaFile(
        LPCTSTR lpszMetaFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszMetaFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetEnhMetaFileA(jitter):
    gdi32_GetEnhMetaFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetEnhMetaFileW(jitter):
    gdi32_GetEnhMetaFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetEnhMetaFileBits(jitter):
    """
    UINT GetEnhMetaFileBits(
        HENHMETAFILE hemf,
        UINT cbBuffer,
        LPBYTE lpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hemf", "cbBuffer", "lpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetEnhMetaFileDescription(jitter, get_str, set_str):
    """
    UINT GetEnhMetaFileDescription(
        HENHMETAFILE hemf,
        UINT cchBuffer,
        LPTSTR lpszDescription
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hemf", "cchBuffer", "lpszDescription"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetEnhMetaFileDescriptionA(jitter):
    gdi32_GetEnhMetaFileDescription(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetEnhMetaFileDescriptionW(jitter):
    gdi32_GetEnhMetaFileDescription(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetEnhMetaFileHeader(jitter):
    """
    UINT GetEnhMetaFileHeader(
        HENHMETAFILE hemf,
        UINT cbBuffer,
        LPENHMETAHEADER lpemh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hemf", "cbBuffer", "lpemh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetEnhMetaFilePaletteEntries(jitter):
    """
    UINT GetEnhMetaFilePaletteEntries(
        HENHMETAFILE hemf,
        UINT cEntries,
        LPPALETTEENTRY lppe
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hemf", "cEntries", "lppe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetWinMetaFileBits(jitter):
    """
    UINT GetWinMetaFileBits(
        HENHMETAFILE hemf,
        UINT cbBuffer,
        LPBYTE lpbBuffer,
        [MappingMode] fnMapMode,
        HDC hdcRef
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hemf", "cbBuffer", "lpbBuffer", "fnMapMode", "hdcRef"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PlayEnhMetaFile(jitter):
    """
    BOOL PlayEnhMetaFile(
        HDC hdc,
        HENHMETAFILE hemf,
        const RECT* lpRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hemf", "lpRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PlayEnhMetaFileRecord(jitter):
    """
    BOOL PlayEnhMetaFileRecord(
        HDC hdc,
        LPHANDLETABLE lpHandletable,
        const ENHMETARECORD* lpEnhMetaRecord,
        UINT nHandles
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpHandletable", "lpEnhMetaRecord", "nHandles"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetEnhMetaFileBits(jitter):
    """
    HENHMETAFILE SetEnhMetaFileBits(
        UINT cbBuffer,
        const BYTE* lpData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cbBuffer", "lpData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetWinMetaFileBits(jitter):
    """
    HENHMETAFILE SetWinMetaFileBits(
        UINT cbBuffer,
        const BYTE* lpbBuffer,
        HDC hdcRef,
        const METAFILEPICT* lpmfp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cbBuffer", "lpbBuffer", "hdcRef", "lpmfp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CloseMetaFile(jitter):
    """
    HMETAFILE CloseMetaFile(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CopyMetaFile(jitter, get_str, set_str):
    """
    HMETAFILE CopyMetaFile(
        HMETAFILE hmfSrc,
        LPCTSTR lpszFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmfSrc", "lpszFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CopyMetaFileA(jitter):
    gdi32_CopyMetaFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_CopyMetaFileW(jitter):
    gdi32_CopyMetaFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_CreateMetaFile(jitter, get_str, set_str):
    """
    HDC CreateMetaFile(
        LPCTSTR lpszFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateMetaFileA(jitter):
    gdi32_CreateMetaFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_CreateMetaFileW(jitter):
    gdi32_CreateMetaFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_DeleteMetaFile(jitter):
    """
    BOOL DeleteMetaFile(
        HMETAFILE hmf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_EnumMetaFile(jitter):
    """
    BOOL EnumMetaFile(
        HDC hdc,
        HMETAFILE hmf,
        MFENUMPROC lpMetaFunc,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hmf", "lpMetaFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetMetaFileBitsEx(jitter):
    """
    UINT GetMetaFileBitsEx(
        HMETAFILE hmf,
        UINT nSize,
        LPVOID lpvData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmf", "nSize", "lpvData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PlayMetaFile(jitter):
    """
    BOOL PlayMetaFile(
        HDC hdc,
        HMETAFILE hmf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hmf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PlayMetaFileRecord(jitter):
    """
    BOOL PlayMetaFileRecord(
        HDC hdc,
        LPHANDLETABLE lpHandletable,
        LPMETARECORD lpMetaRecord,
        UINT nHandles
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpHandletable", "lpMetaRecord", "nHandles"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetMetaFileBitsEx(jitter):
    """
    HMETAFILE SetMetaFileBitsEx(
        UINT nSize,
        const BYTE* lpData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nSize", "lpData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GdiFlush(jitter):
    """
    BOOL GdiFlush()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GdiGetBatchLimit(jitter):
    """
    DWORD GdiGetBatchLimit()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GdiSetBatchLimit(jitter):
    """
    DWORD GdiSetBatchLimit(
        DWORD dwLimit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwLimit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetBkColor(jitter):
    """
    COLORREF GetBkColor(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetBkMode(jitter):
    """
    int GetBkMode(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetBoundsRect(jitter):
    """
    UINT GetBoundsRect(
        HDC hdc,
        LPRECT lprcBounds,
        [BoundsAccumulationFlags] flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lprcBounds", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetROP2(jitter):
    """
    int GetROP2(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetBkColor(jitter):
    """
    COLORREF SetBkColor(
        HDC hdc,
        COLORREF crColor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "crColor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetBkMode(jitter):
    """
    int SetBkMode(
        HDC hdc,
        [BkModeEnum] iBkMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iBkMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetBoundsRect(jitter):
    """
    UINT SetBoundsRect(
        HDC hdc,
        const RECT* lprcBounds,
        [BoundsAccumulationFlags] flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lprcBounds", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetROP2(jitter):
    """
    int SetROP2(
        HDC hdc,
        [ROP2ModeEnum] fnDrawMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "fnDrawMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_AbortPath(jitter):
    """
    BOOL AbortPath(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_BeginPath(jitter):
    """
    BOOL BeginPath(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CloseFigure(jitter):
    """
    BOOL CloseFigure(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_EndPath(jitter):
    """
    BOOL EndPath(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_FillPath(jitter):
    """
    BOOL FillPath(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_FlattenPath(jitter):
    """
    BOOL FlattenPath(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetMiterLimit(jitter):
    """
    BOOL GetMiterLimit(
        HDC hdc,
        PFLOAT peLimit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "peLimit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetPath(jitter):
    """
    int GetPath(
        HDC hdc,
        LPPOINT lpPoints,
        [POINT_TYPE*] lpTypes,
        int nSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpPoints", "lpTypes", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PathToRegion(jitter):
    """
    HRGN PathToRegion(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetMiterLimit(jitter):
    """
    BOOL SetMiterLimit(
        HDC hdc,
        FLOAT eNewLimit,
        PFLOAT peOldLimit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "eNewLimit", "peOldLimit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_StrokeAndFillPath(jitter):
    """
    BOOL StrokeAndFillPath(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_StrokePath(jitter):
    """
    BOOL StrokePath(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_WidenPath(jitter):
    """
    BOOL WidenPath(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_AbortDoc(jitter):
    """
    int AbortDoc(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_StartDoc(jitter, get_str, set_str):
    """
    int StartDoc(
        HDC hdc,
        const DOCINFO* lpdi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_StartDocA(jitter):
    gdi32_StartDoc(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_StartDocW(jitter):
    gdi32_StartDoc(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_EndDoc(jitter):
    """
    int EndDoc(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_EndPage(jitter):
    """
    int EndPage(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_Escape(jitter):
    """
    int Escape(
        HDC hdc,
        [GdiEscapeFunction] nEscape,
        int cbInput,
        LPCSTR lpvInData,
        LPVOID lpvOutData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nEscape", "cbInput", "lpvInData", "lpvOutData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ExtEscape(jitter):
    """
    int ExtEscape(
        HDC hdc,
        int nEscape,
        int cbInput,
        LPCSTR lpszInData,
        int cbOutput,
        LPSTR lpszOutData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "nEscape", "cbInput", "lpszInData", "cbOutput", "lpszOutData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetAbortProc(jitter):
    """
    int SetAbortProc(
        HDC hdc,
        ABORTPROC lpAbortProc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpAbortProc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_StartPage(jitter):
    """
    int StartPage(
        HDC hDC
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CombineRgn(jitter):
    """
    int CombineRgn(
        HRGN hrgnDest,
        HRGN hrgnSrc1,
        HRGN hrgnSrc2,
        [RgnMode] fnCombineMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrgnDest", "hrgnSrc1", "hrgnSrc2", "fnCombineMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateEllipticRgn(jitter):
    """
    HRGN CreateEllipticRgn(
        int nLeftRect,
        int nTopRect,
        int nRightRect,
        int nBottomRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nLeftRect", "nTopRect", "nRightRect", "nBottomRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateEllipticRgnIndirect(jitter):
    """
    HRGN CreateEllipticRgnIndirect(
        const RECT* lprc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreatePolygonRgn(jitter):
    """
    HRGN CreatePolygonRgn(
        const POINT* lppt,
        int cPoints,
        [PolyFillModes] fnPolyFillMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lppt", "cPoints", "fnPolyFillMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreatePolyPolygonRgn(jitter):
    """
    HRGN CreatePolyPolygonRgn(
        const POINT* lppt,
        const INT* lpPolyCounts,
        int nCount,
        [PolyFillModes] fnPolyFillMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lppt", "lpPolyCounts", "nCount", "fnPolyFillMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateRectRgn(jitter):
    """
    HRGN CreateRectRgn(
        int nLeftRect,
        int nTopRect,
        int nRightRect,
        int nBottomRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nLeftRect", "nTopRect", "nRightRect", "nBottomRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateRectRgnIndirect(jitter):
    """
    HRGN CreateRectRgnIndirect(
        const RECT* lprc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateRoundRectRgn(jitter):
    """
    HRGN CreateRoundRectRgn(
        int nLeftRect,
        int nTopRect,
        int nRightRect,
        int nBottomRect,
        int nWidthEllipse,
        int nHeightEllipse
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nLeftRect", "nTopRect", "nRightRect", "nBottomRect", "nWidthEllipse", "nHeightEllipse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_EqualRgn(jitter):
    """
    BOOL EqualRgn(
        HRGN hSrcRgn1,
        HRGN hSrcRgn2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSrcRgn1", "hSrcRgn2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ExtCreateRegion(jitter):
    """
    HRGN ExtCreateRegion(
        const XFORM* lpXform,
        DWORD nCount,
        const RGNDATA* lpRgnData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpXform", "nCount", "lpRgnData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_FillRgn(jitter):
    """
    BOOL FillRgn(
        HDC hdc,
        HRGN hrgn,
        HBRUSH hbr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hrgn", "hbr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_FrameRgn(jitter):
    """
    BOOL FrameRgn(
        HDC hdc,
        HRGN hrgn,
        HBRUSH hbr,
        int nWidth,
        int nHeight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hrgn", "hbr", "nWidth", "nHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetPolyFillMode(jitter):
    """
    int GetPolyFillMode(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetRegionData(jitter):
    """
    DWORD GetRegionData(
        HRGN hRgn,
        DWORD dwCount,
        LPRGNDATA lpRgnData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRgn", "dwCount", "lpRgnData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetRgnBox(jitter):
    """
    int GetRgnBox(
        HRGN hrgn,
        LPRECT lprc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrgn", "lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_InvertRgn(jitter):
    """
    BOOL InvertRgn(
        HDC hdc,
        HRGN hrgn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hrgn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_OffsetRgn(jitter):
    """
    int OffsetRgn(
        HRGN hrgn,
        int nXOffset,
        int nYOffset
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrgn", "nXOffset", "nYOffset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PaintRgn(jitter):
    """
    BOOL PaintRgn(
        HDC hdc,
        HRGN hrgn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "hrgn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_PtInRegion(jitter):
    """
    BOOL PtInRegion(
        HRGN hrgn,
        int X,
        int Y
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrgn", "X", "Y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_RectInRegion(jitter):
    """
    BOOL RectInRegion(
        HRGN hrgn,
        const RECT* lprc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrgn", "lprc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetPolyFillMode(jitter):
    """
    int SetPolyFillMode(
        HDC hdc,
        [PolyFillModes] iPolyFillMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iPolyFillMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetRectRgn(jitter):
    """
    BOOL SetRectRgn(
        HRGN hrgn,
        int nLeftRect,
        int nTopRect,
        int nRightRect,
        int nBottomRect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrgn", "nLeftRect", "nTopRect", "nRightRect", "nBottomRect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetTextCharset(jitter):
    """
    [FontCharset-int] GetTextCharset(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetTextCharsetInfo(jitter):
    """
    [FontCharset-int] GetTextCharsetInfo(
        HDC hdc,
        LPFONTSIGNATURE lpSig,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpSig", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_TranslateCharsetInfo(jitter):
    """
    BOOL TranslateCharsetInfo(
        DWORD* lpSrc,
        LPCHARSETINFO lpCs,
        [TranslateCharsetInfoFlag] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpSrc", "lpCs", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ChoosePixelFormat(jitter):
    """
    int ChoosePixelFormat(
        HDC hdc,
        const PIXELFORMATDESCRIPTOR* ppfd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "ppfd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_DescribePixelFormat(jitter):
    """
    int DescribePixelFormat(
        HDC hdc,
        int iPixelFormat,
        UINT nBytes,
        LPPIXELFORMATDESCRIPTOR ppfd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iPixelFormat", "nBytes", "ppfd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetPixelFormat(jitter):
    """
    int GetPixelFormat(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetPixelFormat(jitter):
    """
    BOOL SetPixelFormat(
        HDC hdc,
        int iPixelFormat,
        const PIXELFORMATDESCRIPTOR* ppfd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "iPixelFormat", "ppfd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetEnhMetaFilePixelFormat(jitter):
    """
    UINT GetEnhMetaFilePixelFormat(
        HENHMETAFILE hemf,
        DWORD cbBuffer,
        const PIXELFORMATDESCRIPTOR* ppfd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hemf", "cbBuffer", "ppfd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SwapBuffers(jitter):
    """
    BOOL SwapBuffers(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CheckColorsInGamut(jitter):
    """
    BOOL CheckColorsInGamut(
        HDC hDC,
        LPVOID lpRGBTriples,
        LPVOID lpBuffer,
        UINT nCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lpRGBTriples", "lpBuffer", "nCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ColorCorrectPalette(jitter):
    """
    BOOL ColorCorrectPalette(
        HDC hDC,
        HPALETTE hPalette,
        DWORD dwFirstEntry,
        DWORD dwNumOfEntries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "hPalette", "dwFirstEntry", "dwNumOfEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_ColorMatchToTarget(jitter):
    """
    BOOL ColorMatchToTarget(
        HDC hDC,
        HDC hdcTarget,
        [CS_ACTION] uiAction
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "hdcTarget", "uiAction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateColorSpace(jitter, get_str, set_str):
    """
    HCOLORSPACE CreateColorSpace(
        LPLOGCOLORSPACE lpLogColorSpace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpLogColorSpace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_CreateColorSpaceA(jitter):
    gdi32_CreateColorSpace(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_CreateColorSpaceW(jitter):
    gdi32_CreateColorSpace(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_DeleteColorSpace(jitter):
    """
    BOOL DeleteColorSpace(
        HCOLORSPACE hColorSpace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hColorSpace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_EnumICMProfiles(jitter, get_str, set_str):
    """
    int EnumICMProfiles(
        HDC hDC,
        ICMENUMPROC lpEnumICMProfilesFunc,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lpEnumICMProfilesFunc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_EnumICMProfilesA(jitter):
    gdi32_EnumICMProfiles(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_EnumICMProfilesW(jitter):
    gdi32_EnumICMProfiles(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetColorSpace(jitter):
    """
    HCOLORSPACE GetColorSpace(
        HDC hDC
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetICMProfile(jitter, get_str, set_str):
    """
    BOOL GetICMProfile(
        HDC hDC,
        LPDWORD lpcbName,
        LPTSTR lpszFilename
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lpcbName", "lpszFilename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetICMProfileA(jitter):
    gdi32_GetICMProfile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetICMProfileW(jitter):
    gdi32_GetICMProfile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetLogColorSpace(jitter, get_str, set_str):
    """
    BOOL GetLogColorSpace(
        HCOLORSPACE hColorSpace,
        LPLOGCOLORSPACE lpBuffer,
        DWORD nSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hColorSpace", "lpBuffer", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_GetLogColorSpaceA(jitter):
    gdi32_GetLogColorSpace(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_GetLogColorSpaceW(jitter):
    gdi32_GetLogColorSpace(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_SetColorSpace(jitter):
    """
    HCOLORSPACE SetColorSpace(
        HDC hDC,
        HCOLORSPACE hColorSpace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "hColorSpace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetICMMode(jitter):
    """
    int SetICMMode(
        HDC hDC,
        [ICM_MODE] iEnableICM
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "iEnableICM"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetICMProfile(jitter, get_str, set_str):
    """
    BOOL SetICMProfile(
        HDC hDC,
        LPTSTR lpFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetICMProfileA(jitter):
    gdi32_SetICMProfile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_SetICMProfileW(jitter):
    gdi32_SetICMProfile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def gdi32_GetDeviceGammaRamp(jitter):
    """
    BOOL GetDeviceGammaRamp(
        HDC hDC,
        LPVOID lpRamp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lpRamp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_SetDeviceGammaRamp(jitter):
    """
    BOOL SetDeviceGammaRamp(
        HDC hDC,
        LPVOID lpRamp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lpRamp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_UpdateICMRegKey(jitter, get_str, set_str):
    """
    BOOL UpdateICMRegKey(
        DWORD dwReserved,
        LPTSTR lpszCMID,
        LPTSTR lpszFileName,
        [ICM_COMMAND] nCommand
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwReserved", "lpszCMID", "lpszFileName", "nCommand"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def gdi32_UpdateICMRegKeyA(jitter):
    gdi32_UpdateICMRegKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def gdi32_UpdateICMRegKeyW(jitter):
    gdi32_UpdateICMRegKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
