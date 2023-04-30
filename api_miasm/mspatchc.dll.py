
def mspatchc_CreatePatchFile(jitter, get_str, set_str):
    """
    BOOL CreatePatchFile(
        LPCTSTR OldFileName,
        LPCTSTR NewFileName,
        LPCTSTR PatchFileName,
        [PatchOptionFlags] OptionFlags,
        PPATCH_OPTION_DATA OptionData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OldFileName", "NewFileName", "PatchFileName", "OptionFlags", "OptionData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_CreatePatchFileA(jitter):
    mspatchc_CreatePatchFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mspatchc_CreatePatchFileW(jitter):
    mspatchc_CreatePatchFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mspatchc_CreatePatchFileByHandles(jitter):
    """
    BOOL CreatePatchFileByHandles(
        HANDLE OldFileHandle,
        HANDLE NewFileHandle,
        HANDLE PatchFileHandle,
        [PatchOptionFlags] OptionFlags,
        PPATCH_OPTION_DATA OptionData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OldFileHandle", "NewFileHandle", "PatchFileHandle", "OptionFlags", "OptionData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_CreatePatchFileByHandlesEx(jitter):
    """
    BOOL CreatePatchFileByHandlesEx(
        ULONG OldFileCount,
        PPATCH_OLD_FILE_INFO_H OldFileInfoArray,
        HANDLE NewFileHandle,
        HANDLE PatchFileHandle,
        [PatchOptionFlags] OptionFlags,
        PPATCH_OPTION_DATA OptionData,
        PPATCH_PROGRESS_CALLBACK ProgressCallback,
        PVOID CallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OldFileCount", "OldFileInfoArray", "NewFileHandle", "PatchFileHandle", "OptionFlags", "OptionData", "ProgressCallback", "CallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_CreatePatchFileEx(jitter, get_str, set_str):
    """
    BOOL CreatePatchFileEx(
        ULONG OldFileCount,
        PPATCH_OLD_FILE_INFO OldFileInfoArray,
        LPCTSTR NewFileName,
        LPCTSTR PatchFileName,
        [PatchOptionFlags] OptionFlags,
        PPATCH_OPTION_DATA OptionData,
        PPATCH_PROGRESS_CALLBACK ProgressCallback,
        PVOID CallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OldFileCount", "OldFileInfoArray", "NewFileName", "PatchFileName", "OptionFlags", "OptionData", "ProgressCallback", "CallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_CreatePatchFileExA(jitter):
    mspatchc_CreatePatchFileEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mspatchc_CreatePatchFileExW(jitter):
    mspatchc_CreatePatchFileEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mspatchc_ExtractPatchHeaderToFile(jitter, get_str, set_str):
    """
    BOOL ExtractPatchHeaderToFile(
        LPCTSTR PatchFileName,
        LPCTSTR PatchHeaderFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PatchFileName", "PatchHeaderFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_ExtractPatchHeaderToFileA(jitter):
    mspatchc_ExtractPatchHeaderToFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mspatchc_ExtractPatchHeaderToFileW(jitter):
    mspatchc_ExtractPatchHeaderToFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mspatchc_ExtractPatchHeaderToFileByHandles(jitter):
    """
    BOOL ExtractPatchHeaderToFileByHandles(
        HANDLE PatchFileHandle,
        HANDLE PatchHeaderFileHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PatchFileHandle", "PatchHeaderFileHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_GetFilePatchSignature(jitter, get_str, set_str):
    """
    BOOL GetFilePatchSignature(
        LPCTSTR FileName,
        [PatchOptionFlags] OptionFlags,
        PVOID OptionData,
        ULONG IgnoreRangeCount,
        PPATCH_IGNORE_RANGE IgnoreRangeArray,
        ULONG RetainRangeCount,
        PPATCH_RETAIN_RANGE RetainRangeArray,
        ULONG SignatureBufferSize,
        PVOID SignatureBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "OptionFlags", "OptionData", "IgnoreRangeCount", "IgnoreRangeArray", "RetainRangeCount", "RetainRangeArray", "SignatureBufferSize", "SignatureBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_GetFilePatchSignatureA(jitter):
    mspatchc_GetFilePatchSignature(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mspatchc_GetFilePatchSignatureW(jitter):
    mspatchc_GetFilePatchSignature(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mspatchc_GetFilePatchSignatureByBuffer(jitter):
    """
    BOOL GetFilePatchSignatureByBuffer(
        PBYTE FileBufferWritable,
        ULONG FileSize,
        ULONG OptionFlags,
        PVOID OptionData,
        ULONG IgnoreRangeCount,
        PPATCH_IGNORE_RANGE IgnoreRangeArray,
        ULONG RetainRangeCount,
        PPATCH_RETAIN_RANGE RetainRangeArray,
        ULONG SignatureBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileBufferWritable", "FileSize", "OptionFlags", "OptionData", "IgnoreRangeCount", "IgnoreRangeArray", "RetainRangeCount", "RetainRangeArray", "SignatureBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_GetFilePatchSignatureByHandle(jitter):
    """
    BOOL GetFilePatchSignatureByHandle(
        HANDLE FileHandle,
        [PatchOptionFlags] OptionFlags,
        PVOID OptionData,
        ULONG IgnoreRangeCount,
        PPATCH_IGNORE_RANGE IgnoreRangeArray,
        ULONG RetainRangeCount,
        PPATCH_RETAIN_RANGE RetainRangeArray,
        ULONG SignatureBufferSize,
        PVOID SignatureBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "OptionFlags", "OptionData", "IgnoreRangeCount", "IgnoreRangeArray", "RetainRangeCount", "RetainRangeArray", "SignatureBufferSize", "SignatureBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_NormalizeFileForPatchSignature(jitter):
    """
    BOOL NormalizeFileForPatchSignature(
        PVOID FileBuffer,
        ULONG FileSize,
        ULONG OptionFlags,
        PATCH_OPTION_DATA* OptionData,
        ULONG NewFileCoffBase,
        ULONG NewFileCoffTime,
        ULONG IgnoreRangeCount,
        PPATCH_IGNORE_RANGE IgnoreRangeArray,
        ULONG RetainRangeCount,
        PPATCH_RETAIN_RANGE RetainRangeArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileBuffer", "FileSize", "OptionFlags", "OptionData", "NewFileCoffBase", "NewFileCoffTime", "IgnoreRangeCount", "IgnoreRangeArray", "RetainRangeCount", "RetainRangeArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
