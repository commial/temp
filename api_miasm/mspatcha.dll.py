
def mspatcha_ApplyPatchToFile(jitter):
    """"
    [mspatcha.dll] BOOL ApplyPatchToFile(LPCTSTR PatchFileName, LPCTSTR OldFileName, LPCTSTR NewFileName, [ApplyOptionFlags] ApplyOptionFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PatchFileName", "OldFileName", "NewFileName", "ApplyOptionFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatcha_ApplyPatchToFileByBuffers(jitter):
    """"
    [mspatcha.dll] BOOL ApplyPatchToFileByBuffers(PBYTE PatchFileMapped, ULONG PatchFileSize, PBYTE OldFileMapped, ULONG OldFileSize, PBYTE* NewFileBuffer, ULONG NewFileBufferSize, ULONG* NewFileActualSize, FILETIME* NewFileTime, [ApplyOptionFlags] ApplyOptionFlags, PPATCH_PROGRESS_CALLBACK ProgressCallback, PVOID CallbackContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PatchFileMapped", "PatchFileSize", "OldFileMapped", "OldFileSize", "NewFileBuffer", "NewFileBufferSize", "NewFileActualSize", "NewFileTime", "ApplyOptionFlags", "ProgressCallback", "CallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatcha_ApplyPatchToFileByHandles(jitter):
    """"
    [mspatcha.dll] BOOL ApplyPatchToFileByHandles(HANDLE PatchFileHandle, HANDLE OldFileHandle, HANDLE NewFileHandle, [ApplyOptionFlags] ApplyOptionFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PatchFileHandle", "OldFileHandle", "NewFileHandle", "ApplyOptionFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatcha_ApplyPatchToFileByHandlesEx(jitter):
    """"
    [mspatcha.dll] BOOL ApplyPatchToFileByHandlesEx(HANDLE PatchFileHandle, HANDLE OldFileHandle, HANDLE NewFileHandle, [ApplyOptionFlags] ApplyOptionFlags, PPATCH_PROGRESS_CALLBACK ProgressCallback, PVOID CallbackContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PatchFileHandle", "OldFileHandle", "NewFileHandle", "ApplyOptionFlags", "ProgressCallback", "CallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatcha_ApplyPatchToFileEx(jitter):
    """"
    [mspatcha.dll] BOOL ApplyPatchToFileEx(LPCTSTR PatchFileName, LPCTSTR OldFileName, LPCTSTR NewFileName, [ApplyOptionFlags] ApplyOptionFlags, PPATCH_PROGRESS_CALLBACK ProgressCallback, PVOID CallbackContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PatchFileName", "OldFileName", "NewFileName", "ApplyOptionFlags", "ProgressCallback", "CallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatcha_GetFilePatchSignature(jitter):
    """"
    [mspatcha.dll] BOOL GetFilePatchSignature(LPCTSTR FileName, [PatchOptionFlags] OptionFlags, PVOID OptionData, ULONG IgnoreRangeCount, PPATCH_IGNORE_RANGE IgnoreRangeArray, ULONG RetainRangeCount, PPATCH_RETAIN_RANGE RetainRangeArray, ULONG SignatureBufferSize, PVOID SignatureBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileName", "OptionFlags", "OptionData", "IgnoreRangeCount", "IgnoreRangeArray", "RetainRangeCount", "RetainRangeArray", "SignatureBufferSize", "SignatureBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatcha_GetFilePatchSignatureByBuffer(jitter):
    """"
    [mspatcha.dll] BOOL GetFilePatchSignatureByBuffer(PBYTE FileBufferWritable, ULONG FileSize, ULONG OptionFlags, PVOID OptionData, ULONG IgnoreRangeCount, PPATCH_IGNORE_RANGE IgnoreRangeArray, ULONG RetainRangeCount, PPATCH_RETAIN_RANGE RetainRangeArray, ULONG SignatureBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileBufferWritable", "FileSize", "OptionFlags", "OptionData", "IgnoreRangeCount", "IgnoreRangeArray", "RetainRangeCount", "RetainRangeArray", "SignatureBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatcha_GetFilePatchSignatureByHandle(jitter):
    """"
    [mspatcha.dll] BOOL GetFilePatchSignatureByHandle(HANDLE FileHandle, [PatchOptionFlags] OptionFlags, PVOID OptionData, ULONG IgnoreRangeCount, PPATCH_IGNORE_RANGE IgnoreRangeArray, ULONG RetainRangeCount, PPATCH_RETAIN_RANGE RetainRangeArray, ULONG SignatureBufferSize, PVOID SignatureBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "OptionFlags", "OptionData", "IgnoreRangeCount", "IgnoreRangeArray", "RetainRangeCount", "RetainRangeArray", "SignatureBufferSize", "SignatureBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatcha_NormalizeFileForPatchSignature(jitter):
    """"
    [mspatcha.dll] BOOL NormalizeFileForPatchSignature(PVOID FileBuffer, ULONG FileSize, ULONG OptionFlags, PATCH_OPTION_DATA* OptionData, ULONG NewFileCoffBase, ULONG NewFileCoffTime, ULONG IgnoreRangeCount, PPATCH_IGNORE_RANGE IgnoreRangeArray, ULONG RetainRangeCount, PPATCH_RETAIN_RANGE RetainRangeArray)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileBuffer", "FileSize", "OptionFlags", "OptionData", "NewFileCoffBase", "NewFileCoffTime", "IgnoreRangeCount", "IgnoreRangeArray", "RetainRangeCount", "RetainRangeArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatcha_TestApplyPatchToFile(jitter):
    """"
    [mspatcha.dll] BOOL TestApplyPatchToFile(LPCTSTR PatchFileName, LPCTSTR OldFileName, [ApplyOptionFlags] ApplyOptionFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PatchFileName", "OldFileName", "ApplyOptionFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatcha_TestApplyPatchToFileByBuffers(jitter):
    """"
    [mspatcha.dll] BOOL TestApplyPatchToFileByBuffers(PBYTE PatchFileBuffer, ULONG PatchFileSize, PBYTE OldFileBuffer, ULONG OldFileSize, ULONG* NewFileSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PatchFileBuffer", "PatchFileSize", "OldFileBuffer", "OldFileSize", "NewFileSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatcha_TestApplyPatchToFileByHandles(jitter):
    """"
    [mspatcha.dll] BOOL TestApplyPatchToFileByHandles(HANDLE PatchFileHandle, HANDLE OldFileHandle, [ApplyOptionFlags] ApplyOptionFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PatchFileHandle", "OldFileHandle", "ApplyOptionFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
