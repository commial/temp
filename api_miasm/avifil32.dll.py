
def avifil32_AVIBuildFilter(jitter, get_str, set_str):
    """
    STDAPI AVIBuildFilter(
        LPTSTR lpszFilter,
        LONG cbFilter,
        BOOL fSaving
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFilter", "cbFilter", "fSaving"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIBuildFilterA(jitter):
    avifil32_AVIBuildFilter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avifil32_AVIBuildFilterW(jitter):
    avifil32_AVIBuildFilter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def avifil32_AVIClearClipboard(jitter):
    """
    STDAPI AVIClearClipboard()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIFileAddRef(jitter):
    """
    STDAPI_(ULONG) AVIFileAddRef(
        PAVIFILE pfile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIFileCreateStream(jitter, get_str, set_str):
    """
    STDAPI AVIFileCreateStream(
        PAVIFILE pfile,
        PAVISTREAM* ppavi,
        AVISTREAMINFO* psi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfile", "ppavi", "psi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIFileCreateStreamA(jitter):
    avifil32_AVIFileCreateStream(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avifil32_AVIFileCreateStreamW(jitter):
    avifil32_AVIFileCreateStream(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def avifil32_AVIFileEndRecord(jitter):
    """
    STDAPI AVIFileEndRecord(
        PAVIFILE pfile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIFileExit(jitter):
    """
    STDAPI_(VOID) AVIFileExit()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIFileGetStream(jitter):
    """
    STDAPI AVIFileGetStream(
        PAVIFILE pfile,
        PAVISTREAM* ppavi,
        DWORD fccType,
        LONG lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfile", "ppavi", "fccType", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIFileInfo(jitter, get_str, set_str):
    """
    STDAPI AVIFileInfo(
        PAVIFILE pfile,
        AVIFILEINFO* pfi,
        LONG lSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfile", "pfi", "lSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIFileInfoA(jitter):
    avifil32_AVIFileInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avifil32_AVIFileInfoW(jitter):
    avifil32_AVIFileInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def avifil32_AVIFileInit(jitter):
    """
    STDAPI_(VOID) AVIFileInit()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIFileOpen(jitter, get_str, set_str):
    """
    STDAPI AVIFileOpen(
        PAVIFILE* ppfile,
        LPCTSTR szFile,
        UINT mode,
        CLSID pclsidHandler
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppfile", "szFile", "mode", "pclsidHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIFileOpenA(jitter):
    avifil32_AVIFileOpen(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avifil32_AVIFileOpenW(jitter):
    avifil32_AVIFileOpen(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def avifil32_AVIFileReadData(jitter):
    """
    STDAPI AVIFileReadData(
        PAVIFILE pfile,
        DWORD ckid,
        LPVOID lpData,
        LONG* lpcbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfile", "ckid", "lpData", "lpcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIFileRelease(jitter):
    """
    STDAPI_(ULONG) AVIFileRelease(
        PAVIFILE pfile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIFileWriteData(jitter):
    """
    STDAPI AVIFileWriteData(
        PAVIFILE pfile,
        DWORD ckid,
        LPVOID lpData,
        LONG cbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfile", "ckid", "lpData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIGetFromClipboard(jitter):
    """
    STDAPI AVIGetFromClipboard(
        PAVIFILE* lppf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lppf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIMakeCompressedStream(jitter):
    """
    STDAPI AVIMakeCompressedStream(
        PAVISTREAM* ppsCompressed,
        PAVISTREAM psSource,
        AVICOMPRESSOPTIONS* lpOptions,
        CLSID* pclsidHandler
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppsCompressed", "psSource", "lpOptions", "pclsidHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIMakeFileFromStreams(jitter):
    """
    STDAPI AVIMakeFileFromStreams(
        PAVIFILE* ppfile,
        int nStreams,
        PAVISTREAM* papStreams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppfile", "nStreams", "papStreams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIMakeStreamFromClipboard(jitter):
    """
    STDAPI AVIMakeStreamFromClipboard(
        UINT cfFormat,
        HANDLE hGlobal,
        PAVISTREAM* ppstream
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cfFormat", "hGlobal", "ppstream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIPutFileOnClipboard(jitter):
    """
    STDAPI AVIPutFileOnClipboard(
        PAVIFILE pf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVISave(jitter, get_str, set_str):
    """
    HRESULT AVISave(
        LPCTSTR szFile,
        CLSID* pclsidHandler,
        AVISAVECALLBACK lpfnCallback,
        int nStreams,
        PAVISTREAM pavi,
        LPAVICOMPRESSOPTIONS lpOptions,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szFile", "pclsidHandler", "lpfnCallback", "nStreams", "pavi", "lpOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVISaveA(jitter):
    avifil32_AVISave(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avifil32_AVISaveW(jitter):
    avifil32_AVISave(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def avifil32_AVISaveOptions(jitter):
    """
    BOOL AVISaveOptions(
        HWND hwnd,
        UINT uiFlags,
        int nStreams,
        PAVISTREAM* ppavi,
        LPAVICOMPRESSOPTIONS* plpOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "uiFlags", "nStreams", "ppavi", "plpOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVISaveOptionsFree(jitter):
    """
    LONG AVISaveOptionsFree(
        int nStreams,
        LPAVICOMPRESSOPTIONS* plpOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nStreams", "plpOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVISaveV(jitter, get_str, set_str):
    """
    STDAPI AVISaveV(
        LPCTSTR szFile,
        CLSID* pclsidHandler,
        AVISAVECALLBACK lpfnCallback,
        int nStreams,
        PAVISTREAM* ppavi,
        LPAVICOMPRESSOPTIONS* plpOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szFile", "pclsidHandler", "lpfnCallback", "nStreams", "ppavi", "plpOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVISaveVA(jitter):
    avifil32_AVISaveV(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avifil32_AVISaveVW(jitter):
    avifil32_AVISaveV(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def avifil32_AVIStreamAddRef(jitter):
    """
    STDAPI_(LONG) AVIStreamAddRef(
        PAVISTREAM pavi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamBeginStreaming(jitter):
    """
    STDAPI AVIStreamBeginStreaming(
        PAVISTREAM pavi,
        LONG lStart,
        LONG lEnd,
        LONG lRate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "lStart", "lEnd", "lRate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamCreate(jitter):
    """
    STDAPI AVIStreamCreate(
        PAVISTREAM* ppavi,
        LONG lParam1,
        LONG lParam2,
        CLSID* pclsidHandler
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppavi", "lParam1", "lParam2", "pclsidHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamEndStreaming(jitter):
    """
    STDAPI AVIStreamEndStreaming(
        PAVISTREAM pavi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamFindSample(jitter):
    """
    STDAPI_(LONG) AVIStreamFindSample(
        PAVISTREAM pavi,
        LONG lPos,
        LONG lFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "lPos", "lFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamGetFrame(jitter):
    """
    STDAPI_(LPVOID) AVIStreamGetFrame(
        PGETFRAME pgf,
        LONG lPos
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pgf", "lPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamGetFrameClose(jitter):
    """
    STDAPI AVIStreamGetFrameClose(
        PGETFRAME pget
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pget"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamGetFrameOpen(jitter):
    """
    STDAPI_(PGETFRAME) AVIStreamGetFrameOpen(
        PAVISTREAM pavi,
        LPBITMAPINFOHEADER lpbiWanted
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "lpbiWanted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamInfo(jitter, get_str, set_str):
    """
    STDAPI AVIStreamInfo(
        PAVISTREAM pavi,
        AVISTREAMINFO* psi,
        LONG lSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "psi", "lSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamInfoA(jitter):
    avifil32_AVIStreamInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avifil32_AVIStreamInfoW(jitter):
    avifil32_AVIStreamInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def avifil32_AVIStreamLength(jitter):
    """
    STDAPI_(LONG) AVIStreamLength(
        PAVISTREAM pavi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamOpenFromFile(jitter, get_str, set_str):
    """
    STDAPI AVIStreamOpenFromFile(
        PAVISTREAM* ppavi,
        LPCTSTR szFile,
        DWORD fccType,
        LONG lParam,
        UINT mode,
        CLSID* pclsidHandler
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppavi", "szFile", "fccType", "lParam", "mode", "pclsidHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamOpenFromFileA(jitter):
    avifil32_AVIStreamOpenFromFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avifil32_AVIStreamOpenFromFileW(jitter):
    avifil32_AVIStreamOpenFromFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def avifil32_AVIStreamRead(jitter):
    """
    STDAPI AVIStreamRead(
        PAVISTREAM pavi,
        LONG lStart,
        LONG lSamples,
        LPVOID lpBuffer,
        LONG cbBuffer,
        LONG* plBytes,
        LONG* plSamples
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "lStart", "lSamples", "lpBuffer", "cbBuffer", "plBytes", "plSamples"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamReadData(jitter):
    """
    STDAPI AVIStreamReadData(
        PAVISTREAM pavi,
        DWORD ckid,
        LPVOID lpData,
        LONG* lpcbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "ckid", "lpData", "lpcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamReadFormat(jitter):
    """
    STDAPI AVIStreamReadFormat(
        PAVISTREAM pavi,
        LONG lPos,
        LPVOID lpFormat,
        LONG* lpcbFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "lPos", "lpFormat", "lpcbFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamRelease(jitter):
    """
    STDAPI_(LONG) AVIStreamRelease(
        PAVISTREAM pavi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamSampleToTime(jitter):
    """
    STDAPI_(LONG) AVIStreamSampleToTime(
        PAVISTREAM pavi,
        LONG lSample
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "lSample"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamSetFormat(jitter):
    """
    STDAPI AVIStreamSetFormat(
        PAVISTREAM pavi,
        LONG lPos,
        LPVOID lpFormat,
        LONG cbFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "lPos", "lpFormat", "cbFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamStart(jitter):
    """
    STDAPI_(LONG) AVIStreamStart(
        PAVISTREAM pavi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamTimeToSample(jitter):
    """
    STDAPI_(LONG) AVIStreamTimeToSample(
        PAVISTREAM pavi,
        LONG lTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "lTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamWrite(jitter):
    """
    STDAPI AVIStreamWrite(
        PAVISTREAM pavi,
        LONG lStart,
        LONG lSamples,
        LPVOID lpBuffer,
        LONG cbBuffer,
        DWORD dwFlags,
        LONG* plSampWritten,
        LONG* plBytesWritten
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "lStart", "lSamples", "lpBuffer", "cbBuffer", "dwFlags", "plSampWritten", "plBytesWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_AVIStreamWriteData(jitter):
    """
    STDAPI AVIStreamWriteData(
        PAVISTREAM pavi,
        DWORD ckid,
        LPVOID lpData,
        LONG cbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "ckid", "lpData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_CreateEditableStream(jitter):
    """
    STDAPI CreateEditableStream(
        PAVISTREAM* ppsEditable,
        PAVISTREAM psSource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppsEditable", "psSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_EditStreamClone(jitter):
    """
    STDAPI EditStreamClone(
        PAVISTREAM pavi,
        PAVISTREAM* ppResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "ppResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_EditStreamCopy(jitter):
    """
    STDAPI EditStreamCopy(
        PAVISTREAM pavi,
        LONG* plStart,
        LONG* plLength,
        PAVISTREAM* ppResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "plStart", "plLength", "ppResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_EditStreamCut(jitter):
    """
    STDAPI EditStreamCut(
        PAVISTREAM pavi,
        LONG* plStart,
        LONG* plLength,
        PAVISTREAM* ppResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "plStart", "plLength", "ppResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_EditStreamPaste(jitter):
    """
    STDAPI EditStreamPaste(
        PAVISTREAM pavi,
        LONG* plPos,
        LONG* plLength,
        PAVISTREAM pstream,
        LONG lStart,
        LONG lLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "plPos", "plLength", "pstream", "lStart", "lLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_EditStreamSetInfo(jitter, get_str, set_str):
    """
    STDAPI EditStreamSetInfo(
        PAVISTREAM pavi,
        AVISTREAMINFO* lpInfo,
        LONG cbInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "lpInfo", "cbInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_EditStreamSetInfoA(jitter):
    avifil32_EditStreamSetInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avifil32_EditStreamSetInfoW(jitter):
    avifil32_EditStreamSetInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def avifil32_EditStreamSetName(jitter, get_str, set_str):
    """
    STDAPI EditStreamSetName(
        PAVISTREAM pavi,
        LPCTSTR lpszName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pavi", "lpszName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def avifil32_EditStreamSetNameA(jitter):
    avifil32_EditStreamSetName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def avifil32_EditStreamSetNameW(jitter):
    avifil32_EditStreamSetName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
