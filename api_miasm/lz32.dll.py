
def lz32_GetExpandedName(jitter, get_str, set_str):
    """
    INT GetExpandedName(
        LPTSTR lpszSource,
        LPTSTR lpszBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszSource", "lpszBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def lz32_GetExpandedNameA(jitter):
    lz32_GetExpandedName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def lz32_GetExpandedNameW(jitter):
    lz32_GetExpandedName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def lz32_LZClose(jitter):
    """
    void LZClose(
        INT hFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def lz32_LZCopy(jitter):
    """
    LONG LZCopy(
        INT hfSource,
        INT hfDest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hfSource", "hfDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def lz32_LZInit(jitter):
    """
    INT LZInit(
        INT hfSource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hfSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def lz32_LZOpenFile(jitter, get_str, set_str):
    """
    INT LZOpenFile(
        LPTSTR lpFileName,
        LPOFSTRUCT lpReOpenBuf,
        [OpenFlags] wStyle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "lpReOpenBuf", "wStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def lz32_LZOpenFileA(jitter):
    lz32_LZOpenFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def lz32_LZOpenFileW(jitter):
    lz32_LZOpenFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def lz32_LZRead(jitter):
    """
    INT LZRead(
        INT hFile,
        LPBYTE lpBuffer,
        INT cbRead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lpBuffer", "cbRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def lz32_LZSeek(jitter):
    """
    LONG LZSeek(
        INT hFile,
        LONG lOffset,
        INT iOrigin
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "lOffset", "iOrigin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def lz32_CopyLZFile(jitter):
    """
    LONG CopyLZFile(
        INT hfSource,
        INT hfDest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hfSource", "hfDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def lz32_LZDone(jitter):
    """
    VOID LZDone()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def lz32_LZStart(jitter):
    """
    INT LZStart()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def lz32_LZCloseFile(jitter):
    """
    VOID LZCloseFile(
        INT hFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def lz32_LZCreateFileW(jitter):
    """
    ULONG LZCreateFileW(
        [FILE_ACCESS_MASK] dwDesiredAccess,
        [FILE_SHARE_MODE] dwShareMode,
        [CreationDisposition] dwCreationDisposition,
        LPWSTR lpString1
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwDesiredAccess", "dwShareMode", "dwCreationDisposition", "lpString1"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
