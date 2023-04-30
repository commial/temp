
def msvfw32_DrawDibOpen(jitter):
    """"
    [msvfw32.dll] HDRAWDIB DrawDibOpen()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibClose(jitter):
    """"
    [msvfw32.dll] BOOL DrawDibClose(HDRAWDIB hdd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibProfileDisplay(jitter):
    """"
    [msvfw32.dll] BOOL DrawDibProfileDisplay(LPBITMAPINFOHEADER lpbi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpbi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibDraw(jitter):
    """"
    [msvfw32.dll] BOOL DrawDibDraw(HDRAWDIB hdd, HDC hdc, int xDst, int yDst, int dxDst, int dyDst, LPBITMAPINFOHEADER lpbi, LPVOID lpBits, int xSrc, int ySrc, int dxSrc, int dySrc, UINT wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdd", "hdc", "xDst", "yDst", "dxDst", "dyDst", "lpbi", "lpBits", "xSrc", "ySrc", "dxSrc", "dySrc", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibGetBuffer(jitter):
    """"
    [msvfw32.dll] LPVOID DrawDibGetBuffer(HDRAWDIB hdd, LPBITMAPINFOHEADER lpbi, DWORD dwSize, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdd", "lpbi", "dwSize", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_StretchDIB(jitter):
    """"
    [msvfw32.dll] void StretchDIB(LPBITMAPINFOHEADER biDst, LPVOID lpvDst, int DstX, int DstY, int DstXE, int DstYE, LPBITMAPINFOHEADER biSrc, LPVOID lpvSrc, int SrcX, int SrcY, int SrcXE, int SrcYE)
    """"
    ret_ad, args = jitter.func_args_stdcall(["biDst", "lpvDst", "DstX", "DstY", "DstXE", "DstYE", "biSrc", "lpvSrc", "SrcX", "SrcY", "SrcXE", "SrcYE"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibBegin(jitter):
    """"
    [msvfw32.dll] BOOL DrawDibBegin(HDRAWDIB hdd, HDC hdc, int dxDest, int dyDest, LPBITMAPINFOHEADER lpbi, int dxSrc, int dySrc, UINT wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdd", "hdc", "dxDest", "dyDest", "lpbi", "dxSrc", "dySrc", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibEnd(jitter):
    """"
    [msvfw32.dll] BOOL DrawDibEnd(HDRAWDIB hdd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibStart(jitter):
    """"
    [msvfw32.dll] BOOL DrawDibStart(HDRAWDIB hdd, LONG rate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdd", "rate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibStop(jitter):
    """"
    [msvfw32.dll] BOOL DrawDibStop(HDRAWDIB hdd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibRealize(jitter):
    """"
    [msvfw32.dll] UINT DrawDibRealize(HDRAWDIB hdd, HDC hdc, BOOL fBackground)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdd", "hdc", "fBackground"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibSetPalette(jitter):
    """"
    [msvfw32.dll] BOOL DrawDibSetPalette(HDRAWDIB hdd, HPALETTE hpal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdd", "hpal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibGetPalette(jitter):
    """"
    [msvfw32.dll] HPALETTE DrawDibGetPalette(HDRAWDIB hdd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibChangePalette(jitter):
    """"
    [msvfw32.dll] BOOL DrawDibChangePalette(HDRAWDIB hdd, int iStart, int iLen, LPPALETTEENTRY lppe)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdd", "iStart", "iLen", "lppe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_DrawDibTime(jitter):
    """"
    [msvfw32.dll] BOOL DrawDibTime(HDRAWDIB hdd, LPDRAWDIBTIME lpddtime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdd", "lpddtime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_GetOpenFileNamePreview(jitter):
    """"
    [msvfw32.dll] BOOL GetOpenFileNamePreview(LPOPENFILENAME lpofn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpofn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_GetSaveFileNamePreview(jitter):
    """"
    [msvfw32.dll] BOOL GetSaveFileNamePreview(LPOPENFILENAME lpofn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpofn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_MCIWndCreate(jitter):
    """"
    [msvfw32.dll] HWND MCIWndCreate(HWND hwndParent, HINSTANCE hInstance, DWORD dwStyle, LPCTSTR szFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hInstance", "dwStyle", "szFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_MCIWndRegisterClass(jitter):
    """"
    [msvfw32.dll] BOOL MCIWndRegisterClass(HINSTANCE hInstance)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICClose(jitter):
    """"
    [msvfw32.dll] [ICERR] ICClose(HIC hic)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hic"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICCompress(jitter):
    """"
    [msvfw32.dll] [ICERR] ICCompress(HIC hic, DWORD dwFlags, LPBITMAPINFOHEADER lpbiOutput, LPVOID lpData, LPBITMAPINFOHEADER lpbiInput, LPVOID lpBits, LPDWORD lpckid, LPDWORD lpdwFlags, LONG lFrameNum, DWORD dwFrameSize, DWORD dwQuality, LPBITMAPINFOHEADER lpbiPrev, LPVOID lpPrev)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hic", "dwFlags", "lpbiOutput", "lpData", "lpbiInput", "lpBits", "lpckid", "lpdwFlags", "lFrameNum", "dwFrameSize", "dwQuality", "lpbiPrev", "lpPrev"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICCompressorChoose(jitter):
    """"
    [msvfw32.dll] BOOL ICCompressorChoose(HWND hwnd, UINT uiFlags, LPVOID pvIn, LPVOID lpData, PCOMPVARS pc, LPSTR lpszTitle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "uiFlags", "pvIn", "lpData", "pc", "lpszTitle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICCompressorFree(jitter):
    """"
    [msvfw32.dll] void ICCompressorFree(PCOMPVARS pc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICDecompress(jitter):
    """"
    [msvfw32.dll] [ICERR] ICDecompress(HIC hic, DWORD dwFlags, LPBITMAPINFOHEADER lpbiFormat, LPVOID lpData, LPBITMAPINFOHEADER lpbi, LPVOID lpBits)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hic", "dwFlags", "lpbiFormat", "lpData", "lpbi", "lpBits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICDraw(jitter):
    """"
    [msvfw32.dll] [ICERR] ICDraw(HIC hic, DWORD dwFlags, LPVOID lpFormat, LPVOID lpData, DWORD cbData, LONG lTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hic", "dwFlags", "lpFormat", "lpData", "cbData", "lTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICDrawBegin(jitter):
    """"
    [msvfw32.dll] [ICERR] ICDrawBegin(HIC hic, DWORD dwFlags, HPALETTE hpal, HWND hwnd, HDC hdc, int xDst, int yDst, int dxDst, int dyDst, LPBITMAPINFOHEADER lpbi, int xSrc, int ySrc, int dxSrc, int dySrc, DWORD dwRate, DWORD dwScale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hic", "dwFlags", "hpal", "hwnd", "hdc", "xDst", "yDst", "dxDst", "dyDst", "lpbi", "xSrc", "ySrc", "dxSrc", "dySrc", "dwRate", "dwScale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICGetDisplayFormat(jitter):
    """"
    [msvfw32.dll] HIC ICGetDisplayFormat(HIC hic, LPBITMAPINFOHEADER lpbiIn, LPBITMAPINFOHEADER lpbiOut, int BitDepth, int dx, int dy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hic", "lpbiIn", "lpbiOut", "BitDepth", "dx", "dy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICGetInfo(jitter):
    """"
    [msvfw32.dll] LRESULT ICGetInfo(HIC hic, ICINFO* lpicinfo, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hic", "lpicinfo", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICImageCompress(jitter):
    """"
    [msvfw32.dll] HANDLE ICImageCompress(HIC hic, UINT uiFlags, LPBITMAPINFO lpbiIn, LPVOID lpBits, LPBITMAPINFO lpbiOut, LONG lQuality, LONG* plSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hic", "uiFlags", "lpbiIn", "lpBits", "lpbiOut", "lQuality", "plSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICImageDecompress(jitter):
    """"
    [msvfw32.dll] HANDLE ICImageDecompress(HIC hic, UINT uiFlags, LPBITMAPINFO lpbiIn, LPVOID lpBits, LPBITMAPINFO lpbiOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hic", "uiFlags", "lpbiIn", "lpBits", "lpbiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICInfo(jitter):
    """"
    [msvfw32.dll] BOOL ICInfo(DWORD fccType, DWORD fccHandler, ICINFO* lpicinfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fccType", "fccHandler", "lpicinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICInstall(jitter):
    """"
    [msvfw32.dll] BOOL ICInstall(DWORD fccType, DWORD fccHandler, LPARAM lParam, LPSTR szDesc, UINT wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fccType", "fccHandler", "lParam", "szDesc", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICLocate(jitter):
    """"
    [msvfw32.dll] HIC ICLocate(DWORD fccType, DWORD fccHandler, LPBITMAPINFOHEADER lpbiIn, LPBITMAPINFOHEADER lpbiOut, [ICOpenFlags] wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fccType", "fccHandler", "lpbiIn", "lpbiOut", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICOpen(jitter):
    """"
    [msvfw32.dll] HIC ICOpen(DWORD fccType, DWORD fccHandler, [ICOpenFlags] wMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fccType", "fccHandler", "wMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICOpenFunction(jitter):
    """"
    [msvfw32.dll] HIC ICOpenFunction(DWORD fccType, DWORD fccHandler, [ICOpenFlags] wMode, FARPROC lpfnHandler)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fccType", "fccHandler", "wMode", "lpfnHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICRemove(jitter):
    """"
    [msvfw32.dll] BOOL ICRemove(DWORD fccType, DWORD fccHandler, UINT wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fccType", "fccHandler", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICSendMessage(jitter):
    """"
    [msvfw32.dll] LRESULT ICSendMessage(HIC hic, [ICMessage] wMsg, DWORD dw1, DWORD dw2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hic", "wMsg", "dw1", "dw2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICSeqCompressFrame(jitter):
    """"
    [msvfw32.dll] LPVOID ICSeqCompressFrame(PCOMPVARS pc, UINT uiFlags, LPVOID lpBits, BOOL* pfKey, LONG* plSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pc", "uiFlags", "lpBits", "pfKey", "plSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICSeqCompressFrameEnd(jitter):
    """"
    [msvfw32.dll] void ICSeqCompressFrameEnd(PCOMPVARS pc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msvfw32_ICSeqCompressFrameStart(jitter):
    """"
    [msvfw32.dll] BOOL ICSeqCompressFrameStart(PCOMPVARS pc, LPBITMAPINFO lpbiIn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pc", "lpbiIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
