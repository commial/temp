
def cabinet_FCIAddFile(jitter):
    """
    [Cabinet.dll] BOOL FCIAddFile(HFCI hfci, LPSTR pszSourceFile, LPSTR pszFileName, BOOL fExecute, PFNFCIGETNEXTCABINET GetNextCab, PFNFCISTATUS pfnProgress, PFNFCIGETOPENINFO pfnOpenInfo, TCOMP typeCompress)
    """
    ret_ad, args = jitter.func_args_cdecl(["hfci", "pszSourceFile", "pszFileName", "fExecute", "GetNextCab", "pfnProgress", "pfnOpenInfo", "typeCompress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FCICreate(jitter):
    """
    [Cabinet.dll] HFCI FCICreate([PERF_FCI] perf, PFNFCIFILEPLACED pfnfiledest, PFNFCIALLOC pfnalloc, PFNFCIFREE pfnfree, PFNFCIOPEN pfnopen, PFNFCIREAD pfnread, PFNFCIWRITE pfnwrite, PFNFCICLOSE pfnclose, PFNFCISEEK pfnseek, PFNFCIDELETE pfndelete, PFNFCIGETTEMPFILE pfnfcigtf, PCCAB pccab, void* pv)
    """
    ret_ad, args = jitter.func_args_cdecl(["perf", "pfnfiledest", "pfnalloc", "pfnfree", "pfnopen", "pfnread", "pfnwrite", "pfnclose", "pfnseek", "pfndelete", "pfnfcigtf", "pccab", "pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FCIDestroy(jitter):
    """
    [Cabinet.dll] BOOL FCIDestroy(HFCI hfci)
    """
    ret_ad, args = jitter.func_args_cdecl(["hfci"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FCIFlushCabinet(jitter):
    """
    [Cabinet.dll] BOOL FCIFlushCabinet(HFCI hfci, BOOL fGetNextCab, PFNFCIGETNEXTCABINET GetNextCab, PFNFCISTATUS pfnProgress)
    """
    ret_ad, args = jitter.func_args_cdecl(["hfci", "fGetNextCab", "GetNextCab", "pfnProgress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FCIFlushFolder(jitter):
    """
    [Cabinet.dll] BOOL FCIFlushFolder(HFCI hfci, PFNFCIGETNEXTCABINET GetNextCab, PFNFCISTATUS pfnProgress)
    """
    ret_ad, args = jitter.func_args_cdecl(["hfci", "GetNextCab", "pfnProgress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FDICopy(jitter):
    """
    [Cabinet.dll] BOOL FDICopy(HFDI hfdi, LPSTR pszCabinet, LPSTR pszCabPath, INT flags, PFNFDINOTIFY pfnfdin, PFNFDIDECRYPT pfnfdid, void* pvUser)
    """
    ret_ad, args = jitter.func_args_cdecl(["hfdi", "pszCabinet", "pszCabPath", "flags", "pfnfdin", "pfnfdid", "pvUser"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FDICreate(jitter):
    """
    [Cabinet.dll] HFDI FDICreate(PFNALLOC pfnalloc, PFNFREE pfnfree, PFNOPEN pfnopen, PFNREAD pfnread, PFNWRITE pfnwrite, PFNCLOSE pfnclose, PFNSEEK pfnseek, int cpuType, [PERF_FDI] perf)
    """
    ret_ad, args = jitter.func_args_cdecl(["pfnalloc", "pfnfree", "pfnopen", "pfnread", "pfnwrite", "pfnclose", "pfnseek", "cpuType", "perf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FDIDestroy(jitter):
    """
    [Cabinet.dll] BOOL FDIDestroy(BOOL hfdi)
    """
    ret_ad, args = jitter.func_args_cdecl(["hfdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FDIIsCabinet(jitter):
    """
    [Cabinet.dll] BOOL FDIIsCabinet(HFDI hfdi, INT_PTR hf, PFDICABINETINFO pfdici)
    """
    ret_ad, args = jitter.func_args_cdecl(["hfdi", "hf", "pfdici"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FDITruncateCabinet(jitter):
    """
    [Cabinet.dll] BOOL FDITruncateCabinet(HFDI hfdi, LPSTR* pszCabinetName, USHORT iFolderToDelete)
    """
    ret_ad, args = jitter.func_args_cdecl(["hfdi", "pszCabinetName", "iFolderToDelete"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_DeleteExtractedFiles(jitter):
    """
    [Cabinet.dll] VOID DeleteExtractedFiles(PSESSION ps)
    """
    ret_ad, args = jitter.func_args_cdecl(["ps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_DllGetVersion(jitter):
    """
    [Cabinet.dll] VOID DllGetVersion(PCABINETDLLVERSIONINFO pcdvi)
    """
    ret_ad, args = jitter.func_args_cdecl(["pcdvi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_Extract(jitter):
    """
    [Cabinet.dll] HRESULT Extract(PSESSION ps, LPCSTR lpCabName)
    """
    ret_ad, args = jitter.func_args_cdecl(["ps", "lpCabName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_GetDllVersion(jitter):
    """
    [Cabinet.dll] LPCSTR GetDllVersion()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_CloseCompressor(jitter):
    """
    [Cabinet.dll] BOOL CloseCompressor(COMPRESSOR_HANDLE CompressorHandle)
    """
    ret_ad, args = jitter.func_args_cdecl(["CompressorHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_CloseDecompressor(jitter):
    """
    [Cabinet.dll] BOOL CloseDecompressor(DECOMPRESSOR_HANDLE DecompressorHandle)
    """
    ret_ad, args = jitter.func_args_cdecl(["DecompressorHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_Compress(jitter):
    """
    [Cabinet.dll] BOOL Compress(COMPRESSOR_HANDLE CompressorHandle, PVOID UncompressedData, SIZE_T UncompressedDataSize, PVOID CompressedBuffer, SIZE_T CompressedBufferSize, PSIZE_T CompressedDataSize)
    """
    ret_ad, args = jitter.func_args_cdecl(["CompressorHandle", "UncompressedData", "UncompressedDataSize", "CompressedBuffer", "CompressedBufferSize", "CompressedDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_CreateCompressor(jitter):
    """
    [Cabinet.dll] BOOL CreateCompressor([COMPRESS_ALGORITHM] Algorithm, PCOMPRESS_ALLOCATION_ROUTINES AllocationRoutines, PCOMPRESSOR_HANDLE CompressorHandle)
    """
    ret_ad, args = jitter.func_args_cdecl(["Algorithm", "AllocationRoutines", "CompressorHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_CreateDecompressor(jitter):
    """
    [Cabinet.dll] BOOL CreateDecompressor([COMPRESS_ALGORITHM] Algorithm, PCOMPRESS_ALLOCATION_ROUTINES AllocationRoutines, PDECOMPRESSOR_HANDLE DecompressorHandle)
    """
    ret_ad, args = jitter.func_args_cdecl(["Algorithm", "AllocationRoutines", "DecompressorHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_Decompress(jitter):
    """
    [Cabinet.dll] BOOL Decompress(DECOMPRESSOR_HANDLE DecompressorHandle, PVOID CompressedData, SIZE_T CompressedDataSize, PVOID UncompressedBuffer, SIZE_T UncompressedBufferSize, PSIZE_T UncompressedDataSize)
    """
    ret_ad, args = jitter.func_args_cdecl(["DecompressorHandle", "CompressedData", "CompressedDataSize", "UncompressedBuffer", "UncompressedBufferSize", "UncompressedDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_QueryCompressorInformation(jitter):
    """
    [Cabinet.dll] BOOL QueryCompressorInformation(COMPRESSOR_HANDLE CompressorHandle, COMPRESS_INFORMATION_CLASS CompressInformationClass, PVOID CompressInformation, SIZE_T CompressInformationSize)
    """
    ret_ad, args = jitter.func_args_cdecl(["CompressorHandle", "CompressInformationClass", "CompressInformation", "CompressInformationSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_QueryDecompressorInformation(jitter):
    """
    [Cabinet.dll] BOOL QueryDecompressorInformation(DECOMPRESSOR_HANDLE DecompressorHandle, COMPRESS_INFORMATION_CLASS CompressInformationClass, PVOID CompressInformation, SIZE_T CompressInformationSize)
    """
    ret_ad, args = jitter.func_args_cdecl(["DecompressorHandle", "CompressInformationClass", "CompressInformation", "CompressInformationSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_ResetCompressor(jitter):
    """
    [Cabinet.dll] BOOL ResetCompressor(COMPRESSOR_HANDLE CompressorHandle)
    """
    ret_ad, args = jitter.func_args_cdecl(["CompressorHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_ResetDecompressor(jitter):
    """
    [Cabinet.dll] BOOL ResetDecompressor(DECOMPRESSOR_HANDLE DecompressorHandle)
    """
    ret_ad, args = jitter.func_args_cdecl(["DecompressorHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_SetCompressorInformation(jitter):
    """
    [Cabinet.dll] BOOL SetCompressorInformation(COMPRESSOR_HANDLE CompressorHandle, COMPRESS_INFORMATION_CLASS CompressInformationClass, PVOID CompressInformation, SIZE_T CompressInformationSize)
    """
    ret_ad, args = jitter.func_args_cdecl(["CompressorHandle", "CompressInformationClass", "CompressInformation", "CompressInformationSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_SetDecompressorInformation(jitter):
    """
    [Cabinet.dll] BOOL SetDecompressorInformation(DECOMPRESSOR_HANDLE DeompressorHandle, COMPRESS_INFORMATION_CLASS CompressInformationClass, PVOID CompressInformation, SIZE_T CompressInformationSize)
    """
    ret_ad, args = jitter.func_args_cdecl(["DeompressorHandle", "CompressInformationClass", "CompressInformation", "CompressInformationSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)
