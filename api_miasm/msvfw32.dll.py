_ICMessage_ = {
    "ICM_COMPRESS_GET_FORMAT": 0x00004004,
    "ICM_COMPRESS_GET_SIZE": 0x00004005,
    "ICM_COMPRESS_QUERY": 0x00004006,
    "ICM_COMPRESS_BEGIN": 0x00004007,
    "ICM_COMPRESS": 0x00004008,
    "ICM_COMPRESS_END": 0x00004009,
    "ICM_DECOMPRESS_GET_FORMAT": 0x0000400a,
    "ICM_DECOMPRESS_QUERY": 0x0000400b,
    "ICM_DECOMPRESS_BEGIN": 0x0000400c,
    "ICM_DECOMPRESS": 0x0000400d,
    "ICM_DECOMPRESS_END": 0x0000400e,
    "ICM_DECOMPRESS_SET_PALETTE": 0x0000401d,
    "ICM_DECOMPRESS_GET_PALETTE": 0x0000401e,
    "ICM_DRAW_QUERY": 0x0000401f,
    "ICM_DRAW_BEGIN": 0x0000400f,
    "ICM_DRAW_GET_PALETTE": 0x00004010,
    "ICM_DRAW_UPDATE": 0x00004011,
    "ICM_DRAW_START": 0x00004012,
    "ICM_DRAW_STOP": 0x00004013,
    "ICM_DRAW_BITS": 0x00004014,
    "ICM_DRAW_END": 0x00004015,
    "ICM_DRAW_GETTIME": 0x00004020,
    "ICM_DRAW": 0x00004021,
    "ICM_DRAW_WINDOW": 0x00004022,
    "ICM_DRAW_SETTIME": 0x00004023,
    "ICM_DRAW_REALIZE": 0x00004024,
    "ICM_DRAW_FLUSH": 0x00004025,
    "ICM_DRAW_RENDERBUFFER": 0x00004026,
    "ICM_DRAW_START_PLAY": 0x00004027,
    "ICM_DRAW_STOP_PLAY": 0x00004028,
    "ICM_DRAW_SUGGESTFORMAT": 0x00004032,
    "ICM_DRAW_CHANGEPALETTE": 0x00004033,
    "ICM_DRAW_IDLE": 0x00004034,
    "ICM_GETBUFFERSWANTED": 0x00004029,
    "ICM_GETDEFAULTKEYFRAMERATE": 0x0000402a,
    "ICM_DECOMPRESSEX_BEGIN": 0x0000403c,
    "ICM_DECOMPRESSEX_QUERY": 0x0000403d,
    "ICM_DECOMPRESSEX": 0x0000403e,
    "ICM_DECOMPRESSEX_END": 0x0000403f,
    "ICM_COMPRESS_FRAMES_INFO": 0x00004046,
    "ICM_COMPRESS_FRAMES": 0x00004047,
    "ICM_SET_STATUS_PROC": 0x00004048,
}
_ICMessage__INV = {
    0x00004004: "ICM_COMPRESS_GET_FORMAT",
    0x00004005: "ICM_COMPRESS_GET_SIZE",
    0x00004006: "ICM_COMPRESS_QUERY",
    0x00004007: "ICM_COMPRESS_BEGIN",
    0x00004008: "ICM_COMPRESS",
    0x00004009: "ICM_COMPRESS_END",
    0x0000400a: "ICM_DECOMPRESS_GET_FORMAT",
    0x0000400b: "ICM_DECOMPRESS_QUERY",
    0x0000400c: "ICM_DECOMPRESS_BEGIN",
    0x0000400d: "ICM_DECOMPRESS",
    0x0000400e: "ICM_DECOMPRESS_END",
    0x0000401d: "ICM_DECOMPRESS_SET_PALETTE",
    0x0000401e: "ICM_DECOMPRESS_GET_PALETTE",
    0x0000401f: "ICM_DRAW_QUERY",
    0x0000400f: "ICM_DRAW_BEGIN",
    0x00004010: "ICM_DRAW_GET_PALETTE",
    0x00004011: "ICM_DRAW_UPDATE",
    0x00004012: "ICM_DRAW_START",
    0x00004013: "ICM_DRAW_STOP",
    0x00004014: "ICM_DRAW_BITS",
    0x00004015: "ICM_DRAW_END",
    0x00004020: "ICM_DRAW_GETTIME",
    0x00004021: "ICM_DRAW",
    0x00004022: "ICM_DRAW_WINDOW",
    0x00004023: "ICM_DRAW_SETTIME",
    0x00004024: "ICM_DRAW_REALIZE",
    0x00004025: "ICM_DRAW_FLUSH",
    0x00004026: "ICM_DRAW_RENDERBUFFER",
    0x00004027: "ICM_DRAW_START_PLAY",
    0x00004028: "ICM_DRAW_STOP_PLAY",
    0x00004032: "ICM_DRAW_SUGGESTFORMAT",
    0x00004033: "ICM_DRAW_CHANGEPALETTE",
    0x00004034: "ICM_DRAW_IDLE",
    0x00004029: "ICM_GETBUFFERSWANTED",
    0x0000402a: "ICM_GETDEFAULTKEYFRAMERATE",
    0x0000403c: "ICM_DECOMPRESSEX_BEGIN",
    0x0000403d: "ICM_DECOMPRESSEX_QUERY",
    0x0000403e: "ICM_DECOMPRESSEX",
    0x0000403f: "ICM_DECOMPRESSEX_END",
    0x00004046: "ICM_COMPRESS_FRAMES_INFO",
    0x00004047: "ICM_COMPRESS_FRAMES",
    0x00004048: "ICM_SET_STATUS_PROC",
}
_ICERR_ = {
    "ICERR_OK": 0,
    "ICERR_DONTDRAW": 1,
    "ICERR_NEWPALETTE": 2,
    "ICERR_GOTOKEYFRAME": 3,
    "ICERR_STOPDRAWING": 4,
    "ICERR_UNSUPPORTED": -1,
    "ICERR_BADFORMAT": -2,
    "ICERR_MEMORY": -3,
    "ICERR_INTERNAL": -4,
    "ICERR_BADFLAGS": -5,
    "ICERR_BADPARAM": -6,
    "ICERR_BADSIZE": -7,
    "ICERR_BADHANDLE": -8,
    "ICERR_CANTUPDATE": -9,
    "ICERR_ABORT": -10,
    "ICERR_ERROR": -100,
    "ICERR_BADBITDEPTH": -200,
    "ICERR_BADIMAGESIZE": -201,
}
_ICERR__INV = {
    0: "ICERR_OK",
    1: "ICERR_DONTDRAW",
    2: "ICERR_NEWPALETTE",
    3: "ICERR_GOTOKEYFRAME",
    4: "ICERR_STOPDRAWING",
    -1: "ICERR_UNSUPPORTED",
    -2: "ICERR_BADFORMAT",
    -3: "ICERR_MEMORY",
    -4: "ICERR_INTERNAL",
    -5: "ICERR_BADFLAGS",
    -6: "ICERR_BADPARAM",
    -7: "ICERR_BADSIZE",
    -8: "ICERR_BADHANDLE",
    -9: "ICERR_CANTUPDATE",
    -10: "ICERR_ABORT",
    -100: "ICERR_ERROR",
    -200: "ICERR_BADBITDEPTH",
    -201: "ICERR_BADIMAGESIZE",
}

def msvfw32_DrawDibOpen(jitter):
    """
    HDRAWDIB DrawDibOpen()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibClose(jitter):
    """
    BOOL DrawDibClose(
        HDRAWDIB hdd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibProfileDisplay(jitter):
    """
    BOOL DrawDibProfileDisplay(
        LPBITMAPINFOHEADER lpbi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpbi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibDraw(jitter):
    """
    BOOL DrawDibDraw(
        HDRAWDIB hdd,
        HDC hdc,
        int xDst,
        int yDst,
        int dxDst,
        int dyDst,
        LPBITMAPINFOHEADER lpbi,
        LPVOID lpBits,
        int xSrc,
        int ySrc,
        int dxSrc,
        int dySrc,
        UINT wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdd", "hdc", "xDst", "yDst", "dxDst", "dyDst", "lpbi", "lpBits", "xSrc", "ySrc", "dxSrc", "dySrc", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibGetBuffer(jitter):
    """
    LPVOID DrawDibGetBuffer(
        HDRAWDIB hdd,
        LPBITMAPINFOHEADER lpbi,
        DWORD dwSize,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdd", "lpbi", "dwSize", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_StretchDIB(jitter):
    """
    void StretchDIB(
        LPBITMAPINFOHEADER biDst,
        LPVOID lpvDst,
        int DstX,
        int DstY,
        int DstXE,
        int DstYE,
        LPBITMAPINFOHEADER biSrc,
        LPVOID lpvSrc,
        int SrcX,
        int SrcY,
        int SrcXE,
        int SrcYE
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["biDst", "lpvDst", "DstX", "DstY", "DstXE", "DstYE", "biSrc", "lpvSrc", "SrcX", "SrcY", "SrcXE", "SrcYE"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibBegin(jitter):
    """
    BOOL DrawDibBegin(
        HDRAWDIB hdd,
        HDC hdc,
        int dxDest,
        int dyDest,
        LPBITMAPINFOHEADER lpbi,
        int dxSrc,
        int dySrc,
        UINT wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdd", "hdc", "dxDest", "dyDest", "lpbi", "dxSrc", "dySrc", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibEnd(jitter):
    """
    BOOL DrawDibEnd(
        HDRAWDIB hdd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibStart(jitter):
    """
    BOOL DrawDibStart(
        HDRAWDIB hdd,
        LONG rate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdd", "rate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibStop(jitter):
    """
    BOOL DrawDibStop(
        HDRAWDIB hdd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibRealize(jitter):
    """
    UINT DrawDibRealize(
        HDRAWDIB hdd,
        HDC hdc,
        BOOL fBackground
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdd", "hdc", "fBackground"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibSetPalette(jitter):
    """
    BOOL DrawDibSetPalette(
        HDRAWDIB hdd,
        HPALETTE hpal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdd", "hpal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibGetPalette(jitter):
    """
    HPALETTE DrawDibGetPalette(
        HDRAWDIB hdd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibChangePalette(jitter):
    """
    BOOL DrawDibChangePalette(
        HDRAWDIB hdd,
        int iStart,
        int iLen,
        LPPALETTEENTRY lppe
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdd", "iStart", "iLen", "lppe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibTime(jitter):
    """
    BOOL DrawDibTime(
        HDRAWDIB hdd,
        LPDRAWDIBTIME lpddtime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdd", "lpddtime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_GetOpenFileNamePreview(jitter, get_str, set_str):
    """
    BOOL GetOpenFileNamePreview(
        LPOPENFILENAME lpofn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpofn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_GetOpenFileNamePreviewA(jitter):
    msvfw32_GetOpenFileNamePreview(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msvfw32_GetOpenFileNamePreviewW(jitter):
    msvfw32_GetOpenFileNamePreview(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msvfw32_GetSaveFileNamePreview(jitter, get_str, set_str):
    """
    BOOL GetSaveFileNamePreview(
        LPOPENFILENAME lpofn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpofn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_GetSaveFileNamePreviewA(jitter):
    msvfw32_GetSaveFileNamePreview(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msvfw32_GetSaveFileNamePreviewW(jitter):
    msvfw32_GetSaveFileNamePreview(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msvfw32_MCIWndCreate(jitter, get_str, set_str):
    """
    HWND MCIWndCreate(
        HWND hwndParent,
        HINSTANCE hInstance,
        DWORD dwStyle,
        LPCTSTR szFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hInstance", "dwStyle", "szFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_MCIWndCreateA(jitter):
    msvfw32_MCIWndCreate(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msvfw32_MCIWndCreateW(jitter):
    msvfw32_MCIWndCreate(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msvfw32_MCIWndRegisterClass(jitter):
    """
    BOOL MCIWndRegisterClass(
        HINSTANCE hInstance
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICClose(jitter):
    """
    [ICERR] ICClose(
        HIC hic
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hic"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICCompress(jitter):
    """
    [ICERR] ICCompress(
        HIC hic,
        DWORD dwFlags,
        LPBITMAPINFOHEADER lpbiOutput,
        LPVOID lpData,
        LPBITMAPINFOHEADER lpbiInput,
        LPVOID lpBits,
        LPDWORD lpckid,
        LPDWORD lpdwFlags,
        LONG lFrameNum,
        DWORD dwFrameSize,
        DWORD dwQuality,
        LPBITMAPINFOHEADER lpbiPrev,
        LPVOID lpPrev
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hic", "dwFlags", "lpbiOutput", "lpData", "lpbiInput", "lpBits", "lpckid", "lpdwFlags", "lFrameNum", "dwFrameSize", "dwQuality", "lpbiPrev", "lpPrev"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICCompressorChoose(jitter):
    """
    BOOL ICCompressorChoose(
        HWND hwnd,
        UINT uiFlags,
        LPVOID pvIn,
        LPVOID lpData,
        PCOMPVARS pc,
        LPSTR lpszTitle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "uiFlags", "pvIn", "lpData", "pc", "lpszTitle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICCompressorFree(jitter):
    """
    void ICCompressorFree(
        PCOMPVARS pc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICDecompress(jitter):
    """
    [ICERR] ICDecompress(
        HIC hic,
        DWORD dwFlags,
        LPBITMAPINFOHEADER lpbiFormat,
        LPVOID lpData,
        LPBITMAPINFOHEADER lpbi,
        LPVOID lpBits
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hic", "dwFlags", "lpbiFormat", "lpData", "lpbi", "lpBits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICDraw(jitter):
    """
    [ICERR] ICDraw(
        HIC hic,
        DWORD dwFlags,
        LPVOID lpFormat,
        LPVOID lpData,
        DWORD cbData,
        LONG lTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hic", "dwFlags", "lpFormat", "lpData", "cbData", "lTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICDrawBegin(jitter):
    """
    [ICERR] ICDrawBegin(
        HIC hic,
        DWORD dwFlags,
        HPALETTE hpal,
        HWND hwnd,
        HDC hdc,
        int xDst,
        int yDst,
        int dxDst,
        int dyDst,
        LPBITMAPINFOHEADER lpbi,
        int xSrc,
        int ySrc,
        int dxSrc,
        int dySrc,
        DWORD dwRate,
        DWORD dwScale
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hic", "dwFlags", "hpal", "hwnd", "hdc", "xDst", "yDst", "dxDst", "dyDst", "lpbi", "xSrc", "ySrc", "dxSrc", "dySrc", "dwRate", "dwScale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICGetDisplayFormat(jitter):
    """
    HIC ICGetDisplayFormat(
        HIC hic,
        LPBITMAPINFOHEADER lpbiIn,
        LPBITMAPINFOHEADER lpbiOut,
        int BitDepth,
        int dx,
        int dy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hic", "lpbiIn", "lpbiOut", "BitDepth", "dx", "dy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICGetInfo(jitter):
    """
    LRESULT ICGetInfo(
        HIC hic,
        ICINFO* lpicinfo,
        DWORD cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hic", "lpicinfo", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICImageCompress(jitter):
    """
    HANDLE ICImageCompress(
        HIC hic,
        UINT uiFlags,
        LPBITMAPINFO lpbiIn,
        LPVOID lpBits,
        LPBITMAPINFO lpbiOut,
        LONG lQuality,
        LONG* plSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hic", "uiFlags", "lpbiIn", "lpBits", "lpbiOut", "lQuality", "plSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICImageDecompress(jitter):
    """
    HANDLE ICImageDecompress(
        HIC hic,
        UINT uiFlags,
        LPBITMAPINFO lpbiIn,
        LPVOID lpBits,
        LPBITMAPINFO lpbiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hic", "uiFlags", "lpbiIn", "lpBits", "lpbiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICInfo(jitter):
    """
    BOOL ICInfo(
        DWORD fccType,
        DWORD fccHandler,
        ICINFO* lpicinfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fccType", "fccHandler", "lpicinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICInstall(jitter):
    """
    BOOL ICInstall(
        DWORD fccType,
        DWORD fccHandler,
        LPARAM lParam,
        LPSTR szDesc,
        UINT wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fccType", "fccHandler", "lParam", "szDesc", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICLocate(jitter):
    """
    HIC ICLocate(
        DWORD fccType,
        DWORD fccHandler,
        LPBITMAPINFOHEADER lpbiIn,
        LPBITMAPINFOHEADER lpbiOut,
        [ICOpenFlags] wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fccType", "fccHandler", "lpbiIn", "lpbiOut", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICOpen(jitter):
    """
    HIC ICOpen(
        DWORD fccType,
        DWORD fccHandler,
        [ICOpenFlags] wMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fccType", "fccHandler", "wMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICOpenFunction(jitter):
    """
    HIC ICOpenFunction(
        DWORD fccType,
        DWORD fccHandler,
        [ICOpenFlags] wMode,
        FARPROC lpfnHandler
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fccType", "fccHandler", "wMode", "lpfnHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICRemove(jitter):
    """
    BOOL ICRemove(
        DWORD fccType,
        DWORD fccHandler,
        UINT wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fccType", "fccHandler", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICSendMessage(jitter):
    """
    LRESULT ICSendMessage(
        HIC hic,
        [ICMessage] wMsg,
        DWORD dw1,
        DWORD dw2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hic", "wMsg", "dw1", "dw2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICSeqCompressFrame(jitter):
    """
    LPVOID ICSeqCompressFrame(
        PCOMPVARS pc,
        UINT uiFlags,
        LPVOID lpBits,
        BOOL* pfKey,
        LONG* plSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pc", "uiFlags", "lpBits", "pfKey", "plSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICSeqCompressFrameEnd(jitter):
    """
    void ICSeqCompressFrameEnd(
        PCOMPVARS pc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICSeqCompressFrameStart(jitter):
    """
    BOOL ICSeqCompressFrameStart(
        PCOMPVARS pc,
        LPBITMAPINFO lpbiIn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pc", "lpbiIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
