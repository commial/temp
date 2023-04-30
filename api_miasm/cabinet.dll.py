FCIERROR = {
    "FCIERR_NONE": 0,
    "FCIERR_OPEN_SRC": 1,
    "FCIERR_READ_SRC": 2,
    "FCIERR_ALLOC_FAIL": 3,
    "FCIERR_TEMP_FILE": 4,
    "FCIERR_BAD_COMPR_TYPE": 5,
    "FCIERR_CAB_FILE": 6,
    "FCIERR_USER_ABORT": 7,
    "FCIERR_MCI_FAIL": 8,
    "FCIERR_CAB_FORMAT_LIMIT": 9,
}
FDIERROR = {
    "FDIERROR_NONE": 0,
    "FDIERROR_CABINET_NOT_FOUND": 1,
    "FDIERROR_NOT_A_CABINET": 2,
    "FDIERROR_UNKNOWN_CABINET_VERSION": 3,
    "FDIERROR_CORRUPT_CABINET": 4,
    "FDIERROR_ALLOC_FAIL": 5,
    "FDIERROR_BAD_COMPR_TYPE": 6,
    "FDIERROR_MDI_FAIL": 7,
    "FDIERROR_TARGET_FILE": 8,
    "FDIERROR_RESERVE_MISMATCH": 9,
    "FDIERROR_WRONG_CABINET": 10,
    "FDIERROR_USER_ABORT": 11,
}
COMPRESS_INFORMATION_CLASS = {
    "COMPRESS_INFORMATION_CLASS_INVALID": 0,
    "COMPRESS_INFORMATION_CLASS_BLOCK_SIZE": 1,
    "COMPRESS_INFORMATION_CLASS_LEVEL": 2,
}

def cabinet_FCIAddFile(jitter):
    """
    BOOL FCIAddFile(
        HFCI hfci,
        LPSTR pszSourceFile,
        LPSTR pszFileName,
        BOOL fExecute,
        PFNFCIGETNEXTCABINET GetNextCab,
        PFNFCISTATUS pfnProgress,
        PFNFCIGETOPENINFO pfnOpenInfo,
        TCOMP typeCompress
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["hfci", "pszSourceFile", "pszFileName", "fExecute", "GetNextCab", "pfnProgress", "pfnOpenInfo", "typeCompress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FCICreate(jitter):
    """
    HFCI FCICreate(
        [PERF_FCI] perf,
        PFNFCIFILEPLACED pfnfiledest,
        PFNFCIALLOC pfnalloc,
        PFNFCIFREE pfnfree,
        PFNFCIOPEN pfnopen,
        PFNFCIREAD pfnread,
        PFNFCIWRITE pfnwrite,
        PFNFCICLOSE pfnclose,
        PFNFCISEEK pfnseek,
        PFNFCIDELETE pfndelete,
        PFNFCIGETTEMPFILE pfnfcigtf,
        PCCAB pccab,
        void* pv
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["perf", "pfnfiledest", "pfnalloc", "pfnfree", "pfnopen", "pfnread", "pfnwrite", "pfnclose", "pfnseek", "pfndelete", "pfnfcigtf", "pccab", "pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FCIDestroy(jitter):
    """
    BOOL FCIDestroy(
        HFCI hfci
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["hfci"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FCIFlushCabinet(jitter):
    """
    BOOL FCIFlushCabinet(
        HFCI hfci,
        BOOL fGetNextCab,
        PFNFCIGETNEXTCABINET GetNextCab,
        PFNFCISTATUS pfnProgress
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["hfci", "fGetNextCab", "GetNextCab", "pfnProgress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FCIFlushFolder(jitter):
    """
    BOOL FCIFlushFolder(
        HFCI hfci,
        PFNFCIGETNEXTCABINET GetNextCab,
        PFNFCISTATUS pfnProgress
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["hfci", "GetNextCab", "pfnProgress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FDICopy(jitter):
    """
    BOOL FDICopy(
        HFDI hfdi,
        LPSTR pszCabinet,
        LPSTR pszCabPath,
        INT flags,
        PFNFDINOTIFY pfnfdin,
        PFNFDIDECRYPT pfnfdid,
        void* pvUser
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["hfdi", "pszCabinet", "pszCabPath", "flags", "pfnfdin", "pfnfdid", "pvUser"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FDICreate(jitter):
    """
    HFDI FDICreate(
        PFNALLOC pfnalloc,
        PFNFREE pfnfree,
        PFNOPEN pfnopen,
        PFNREAD pfnread,
        PFNWRITE pfnwrite,
        PFNCLOSE pfnclose,
        PFNSEEK pfnseek,
        int cpuType,
        [PERF_FDI] perf
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pfnalloc", "pfnfree", "pfnopen", "pfnread", "pfnwrite", "pfnclose", "pfnseek", "cpuType", "perf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FDIDestroy(jitter):
    """
    BOOL FDIDestroy(
        BOOL hfdi
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["hfdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FDIIsCabinet(jitter):
    """
    BOOL FDIIsCabinet(
        HFDI hfdi,
        INT_PTR hf,
        PFDICABINETINFO pfdici
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["hfdi", "hf", "pfdici"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_FDITruncateCabinet(jitter):
    """
    BOOL FDITruncateCabinet(
        HFDI hfdi,
        LPSTR* pszCabinetName,
        USHORT iFolderToDelete
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["hfdi", "pszCabinetName", "iFolderToDelete"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_DeleteExtractedFiles(jitter):
    """
    VOID DeleteExtractedFiles(
        PSESSION ps
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["ps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_DllGetVersion(jitter):
    """
    VOID DllGetVersion(
        PCABINETDLLVERSIONINFO pcdvi
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pcdvi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_Extract(jitter):
    """
    HRESULT Extract(
        PSESSION ps,
        LPCSTR lpCabName
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["ps", "lpCabName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_GetDllVersion(jitter):
    """
    LPCSTR GetDllVersion()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_CloseCompressor(jitter):
    """
    BOOL CloseCompressor(
        COMPRESSOR_HANDLE CompressorHandle
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["CompressorHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_CloseDecompressor(jitter):
    """
    BOOL CloseDecompressor(
        DECOMPRESSOR_HANDLE DecompressorHandle
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["DecompressorHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_Compress(jitter):
    """
    BOOL Compress(
        COMPRESSOR_HANDLE CompressorHandle,
        PVOID UncompressedData,
        SIZE_T UncompressedDataSize,
        PVOID CompressedBuffer,
        SIZE_T CompressedBufferSize,
        PSIZE_T CompressedDataSize
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["CompressorHandle", "UncompressedData", "UncompressedDataSize", "CompressedBuffer", "CompressedBufferSize", "CompressedDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_CreateCompressor(jitter):
    """
    BOOL CreateCompressor(
        [COMPRESS_ALGORITHM] Algorithm,
        PCOMPRESS_ALLOCATION_ROUTINES AllocationRoutines,
        PCOMPRESSOR_HANDLE CompressorHandle
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["Algorithm", "AllocationRoutines", "CompressorHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_CreateDecompressor(jitter):
    """
    BOOL CreateDecompressor(
        [COMPRESS_ALGORITHM] Algorithm,
        PCOMPRESS_ALLOCATION_ROUTINES AllocationRoutines,
        PDECOMPRESSOR_HANDLE DecompressorHandle
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["Algorithm", "AllocationRoutines", "DecompressorHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_Decompress(jitter):
    """
    BOOL Decompress(
        DECOMPRESSOR_HANDLE DecompressorHandle,
        PVOID CompressedData,
        SIZE_T CompressedDataSize,
        PVOID UncompressedBuffer,
        SIZE_T UncompressedBufferSize,
        PSIZE_T UncompressedDataSize
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["DecompressorHandle", "CompressedData", "CompressedDataSize", "UncompressedBuffer", "UncompressedBufferSize", "UncompressedDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_QueryCompressorInformation(jitter):
    """
    BOOL QueryCompressorInformation(
        COMPRESSOR_HANDLE CompressorHandle,
        COMPRESS_INFORMATION_CLASS CompressInformationClass,
        PVOID CompressInformation,
        SIZE_T CompressInformationSize
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["CompressorHandle", "CompressInformationClass", "CompressInformation", "CompressInformationSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_QueryDecompressorInformation(jitter):
    """
    BOOL QueryDecompressorInformation(
        DECOMPRESSOR_HANDLE DecompressorHandle,
        COMPRESS_INFORMATION_CLASS CompressInformationClass,
        PVOID CompressInformation,
        SIZE_T CompressInformationSize
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["DecompressorHandle", "CompressInformationClass", "CompressInformation", "CompressInformationSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_ResetCompressor(jitter):
    """
    BOOL ResetCompressor(
        COMPRESSOR_HANDLE CompressorHandle
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["CompressorHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_ResetDecompressor(jitter):
    """
    BOOL ResetDecompressor(
        DECOMPRESSOR_HANDLE DecompressorHandle
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["DecompressorHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_SetCompressorInformation(jitter):
    """
    BOOL SetCompressorInformation(
        COMPRESSOR_HANDLE CompressorHandle,
        COMPRESS_INFORMATION_CLASS CompressInformationClass,
        PVOID CompressInformation,
        SIZE_T CompressInformationSize
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["CompressorHandle", "CompressInformationClass", "CompressInformation", "CompressInformationSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def cabinet_SetDecompressorInformation(jitter):
    """
    BOOL SetDecompressorInformation(
        DECOMPRESSOR_HANDLE DeompressorHandle,
        COMPRESS_INFORMATION_CLASS CompressInformationClass,
        PVOID CompressInformation,
        SIZE_T CompressInformationSize
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["DeompressorHandle", "CompressInformationClass", "CompressInformation", "CompressInformationSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)
