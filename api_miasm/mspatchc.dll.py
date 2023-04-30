
def mspatchc_CreatePatchFile(jitter):
    """"
    [mspatchc.dll] BOOL CreatePatchFile(LPCTSTR OldFileName, LPCTSTR NewFileName, LPCTSTR PatchFileName, [PatchOptionFlags] OptionFlags, PPATCH_OPTION_DATA OptionData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["OldFileName", "NewFileName", "PatchFileName", "OptionFlags", "OptionData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_CreatePatchFileByHandles(jitter):
    """"
    [mspatchc.dll] BOOL CreatePatchFileByHandles(HANDLE OldFileHandle, HANDLE NewFileHandle, HANDLE PatchFileHandle, [PatchOptionFlags] OptionFlags, PPATCH_OPTION_DATA OptionData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["OldFileHandle", "NewFileHandle", "PatchFileHandle", "OptionFlags", "OptionData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_CreatePatchFileByHandlesEx(jitter):
    """"
    [mspatchc.dll] BOOL CreatePatchFileByHandlesEx(ULONG OldFileCount, PPATCH_OLD_FILE_INFO_H OldFileInfoArray, HANDLE NewFileHandle, HANDLE PatchFileHandle, [PatchOptionFlags] OptionFlags, PPATCH_OPTION_DATA OptionData, PPATCH_PROGRESS_CALLBACK ProgressCallback, PVOID CallbackContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["OldFileCount", "OldFileInfoArray", "NewFileHandle", "PatchFileHandle", "OptionFlags", "OptionData", "ProgressCallback", "CallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_CreatePatchFileEx(jitter):
    """"
    [mspatchc.dll] BOOL CreatePatchFileEx(ULONG OldFileCount, PPATCH_OLD_FILE_INFO OldFileInfoArray, LPCTSTR NewFileName, LPCTSTR PatchFileName, [PatchOptionFlags] OptionFlags, PPATCH_OPTION_DATA OptionData, PPATCH_PROGRESS_CALLBACK ProgressCallback, PVOID CallbackContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["OldFileCount", "OldFileInfoArray", "NewFileName", "PatchFileName", "OptionFlags", "OptionData", "ProgressCallback", "CallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_ExtractPatchHeaderToFile(jitter):
    """"
    [mspatchc.dll] BOOL ExtractPatchHeaderToFile(LPCTSTR PatchFileName, LPCTSTR PatchHeaderFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PatchFileName", "PatchHeaderFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_ExtractPatchHeaderToFileByHandles(jitter):
    """"
    [mspatchc.dll] BOOL ExtractPatchHeaderToFileByHandles(HANDLE PatchFileHandle, HANDLE PatchHeaderFileHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PatchFileHandle", "PatchHeaderFileHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_GetFilePatchSignature(jitter):
    """"
    [mspatchc.dll] BOOL GetFilePatchSignature(LPCTSTR FileName, [PatchOptionFlags] OptionFlags, PVOID OptionData, ULONG IgnoreRangeCount, PPATCH_IGNORE_RANGE IgnoreRangeArray, ULONG RetainRangeCount, PPATCH_RETAIN_RANGE RetainRangeArray, ULONG SignatureBufferSize, PVOID SignatureBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileName", "OptionFlags", "OptionData", "IgnoreRangeCount", "IgnoreRangeArray", "RetainRangeCount", "RetainRangeArray", "SignatureBufferSize", "SignatureBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_GetFilePatchSignatureByBuffer(jitter):
    """"
    [mspatchc.dll] BOOL GetFilePatchSignatureByBuffer(PBYTE FileBufferWritable, ULONG FileSize, ULONG OptionFlags, PVOID OptionData, ULONG IgnoreRangeCount, PPATCH_IGNORE_RANGE IgnoreRangeArray, ULONG RetainRangeCount, PPATCH_RETAIN_RANGE RetainRangeArray, ULONG SignatureBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileBufferWritable", "FileSize", "OptionFlags", "OptionData", "IgnoreRangeCount", "IgnoreRangeArray", "RetainRangeCount", "RetainRangeArray", "SignatureBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_GetFilePatchSignatureByHandle(jitter):
    """"
    [mspatchc.dll] BOOL GetFilePatchSignatureByHandle(HANDLE FileHandle, [PatchOptionFlags] OptionFlags, PVOID OptionData, ULONG IgnoreRangeCount, PPATCH_IGNORE_RANGE IgnoreRangeArray, ULONG RetainRangeCount, PPATCH_RETAIN_RANGE RetainRangeArray, ULONG SignatureBufferSize, PVOID SignatureBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "OptionFlags", "OptionData", "IgnoreRangeCount", "IgnoreRangeArray", "RetainRangeCount", "RetainRangeArray", "SignatureBufferSize", "SignatureBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mspatchc_NormalizeFileForPatchSignature(jitter):
    """"
    [mspatchc.dll] BOOL NormalizeFileForPatchSignature(PVOID FileBuffer, ULONG FileSize, ULONG OptionFlags, PATCH_OPTION_DATA* OptionData, ULONG NewFileCoffBase, ULONG NewFileCoffTime, ULONG IgnoreRangeCount, PPATCH_IGNORE_RANGE IgnoreRangeArray, ULONG RetainRangeCount, PPATCH_RETAIN_RANGE RetainRangeArray)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileBuffer", "FileSize", "OptionFlags", "OptionData", "NewFileCoffBase", "NewFileCoffTime", "IgnoreRangeCount", "IgnoreRangeArray", "RetainRangeCount", "RetainRangeArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
