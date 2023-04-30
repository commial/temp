
def imagehlp_GetImageConfigInformation(jitter):
    """"
    [ImageHlp.dll] BOOL GetImageConfigInformation(PLOADED_IMAGE LoadedImage, PIMAGE_LOAD_CONFIG_DIRECTORY ImageConfigInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LoadedImage", "ImageConfigInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_GetImageUnusedHeaderBytes(jitter):
    """"
    [ImageHlp.dll] DWORD GetImageUnusedHeaderBytes(PLOADED_IMAGE LoadedImage, PDWORD SizeUnusedHeaderBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LoadedImage", "SizeUnusedHeaderBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageLoad(jitter):
    """"
    [ImageHlp.dll] PLOADED_IMAGE ImageLoad(PSTR DllName, PSTR DllPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DllName", "DllPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageUnload(jitter):
    """"
    [ImageHlp.dll] BOOL ImageUnload(PLOADED_IMAGE LoadedImage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LoadedImage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_MapAndLoad(jitter):
    """"
    [ImageHlp.dll] BOOL MapAndLoad(PSTR ImageName, PSTR DllPath, PLOADED_IMAGE LoadedImage, BOOL DotDll, BOOL ReadOnly)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ImageName", "DllPath", "LoadedImage", "DotDll", "ReadOnly"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_SetImageConfigInformation(jitter):
    """"
    [ImageHlp.dll] BOOL SetImageConfigInformation(PLOADED_IMAGE LoadedImage, PIMAGE_LOAD_CONFIG_DIRECTORY ImageConfigInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LoadedImage", "ImageConfigInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_UnMapAndLoad(jitter):
    """"
    [ImageHlp.dll] BOOL UnMapAndLoad(PLOADED_IMAGE LoadedImage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LoadedImage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageAddCertificate(jitter):
    """"
    [ImageHlp.dll] BOOL ImageAddCertificate(HANDLE FileHandle, LPWIN_CERTIFICATE Certificate, PDWORD Index)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Certificate", "Index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageEnumerateCertificates(jitter):
    """"
    [ImageHlp.dll] BOOL ImageEnumerateCertificates(HANDLE FileHandle, WORD TypeFilter, PDWORD CertificateCount, PDWORD Indices, DWORD IndexCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "TypeFilter", "CertificateCount", "Indices", "IndexCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageGetCertificateData(jitter):
    """"
    [ImageHlp.dll] BOOL ImageGetCertificateData(HANDLE FileHandle, DWORD CertificateIndex, LPWIN_CERTIFICATE Certificate, PDWORD RequiredLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "CertificateIndex", "Certificate", "RequiredLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageGetCertificateHeader(jitter):
    """"
    [ImageHlp.dll] BOOL ImageGetCertificateHeader(HANDLE FileHandle, DWORD CertificateIndex, LPWIN_CERTIFICATE CertificateHeader)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "CertificateIndex", "CertificateHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageGetDigestStream(jitter):
    """"
    [ImageHlp.dll] BOOL ImageGetDigestStream(HANDLE FileHandle, DWORD DigestLevel, DIGEST_FUNCTION DigestFunction, DIGEST_HANDLE DigestHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "DigestLevel", "DigestFunction", "DigestHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageRemoveCertificate(jitter):
    """"
    [ImageHlp.dll] BOOL ImageRemoveCertificate(HANDLE FileHandle, DWORD Index)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_BindImage(jitter):
    """"
    [ImageHlp.dll] BOOL BindImage(PSTR ImageName, PSTR DllPath, PSTR SymbolPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ImageName", "DllPath", "SymbolPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_BindImageEx(jitter):
    """"
    [ImageHlp.dll] BOOL BindImageEx(DWORD Flags, PSTR ImageName, PSTR DllPath, PSTR SymbolPath, PIMAGEHLP_STATUS_ROUTINE StatusRoutine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "ImageName", "DllPath", "SymbolPath", "StatusRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_CheckSumMappedFile(jitter):
    """"
    [ImageHlp.dll] PIMAGE_NT_HEADERS CheckSumMappedFile(PVOID BaseAddress, DWORD FileLength, PDWORD HeaderSum, PDWORD CheckSum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress", "FileLength", "HeaderSum", "CheckSum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_MapFileAndCheckSum(jitter):
    """"
    [ImageHlp.dll] DWORD MapFileAndCheckSum(PTSTR Filename, PDWORD HeaderSum, PDWORD CheckSum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Filename", "HeaderSum", "CheckSum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ReBaseImage(jitter):
    """"
    [ImageHlp.dll] BOOL ReBaseImage(PCSTR CurrentImageName, PCSTR SymbolPath, BOOL fReBase, BOOL fRebaseSysfileOk, BOOL fGoingDown, ULONG CheckImageSize, ULONG* OldImageSize, ULONG_PTR* OldImageBase, ULONG* NewImageSize, ULONG_PTR* NewImageBase, ULONG TimeStamp)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CurrentImageName", "SymbolPath", "fReBase", "fRebaseSysfileOk", "fGoingDown", "CheckImageSize", "OldImageSize", "OldImageBase", "NewImageSize", "NewImageBase", "TimeStamp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_SplitSymbols(jitter):
    """"
    [ImageHlp.dll] BOOL SplitSymbols(PSTR ImageName, PSTR SymbolsPath, PSTR SymbolFilePath, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ImageName", "SymbolsPath", "SymbolFilePath", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_TouchFileTimes(jitter):
    """"
    [ImageHlp.dll] BOOL TouchFileTimes(HANDLE FileHandle, PSYSTEMTIME pSystemTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "pSystemTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_UpdateDebugInfoFile(jitter):
    """"
    [ImageHlp.dll] BOOL UpdateDebugInfoFile(PSTR ImageFileName, PSTR SymbolPath, PSTR DebugFilePath, PIMAGE_NT_HEADERS NtHeaders)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ImageFileName", "SymbolPath", "DebugFilePath", "NtHeaders"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_UpdateDebugInfoFileEx(jitter):
    """"
    [ImageHlp.dll] BOOL UpdateDebugInfoFileEx(PSTR ImageFileName, PSTR SymbolPath, PSTR DebugFilePath, PIMAGE_NT_HEADERS NtHeaders, DWORD OldChecksum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ImageFileName", "SymbolPath", "DebugFilePath", "NtHeaders", "OldChecksum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
