###### Enums ######

###################

###### Types ######
DIGEST_FUNCTION = LPVOID
DIGEST_HANDLE = PVOID
PIMAGEHLP_STATUS_ROUTINE = LPVOID
PIMAGE_LOAD_CONFIG_DIRECTORY = Ptr("<I", IMAGE_LOAD_CONFIG_DIRECTORY())
_WIN_CERT_TYPE_ = WORD

class WIN_CERTIFICATE(MemStruct):
    fields = [
        ("dwLength", DWORD()),
        ("wRevision", WORD()),
        ("wCertificateType", _WIN_CERT_TYPE_()),
        ("bCertificate", BYTE__ANYSIZE_ARRAY_()),
    ]

LPWIN_CERTIFICATE = Ptr("<I", WIN_CERTIFICATE())

class LOADED_IMAGE(MemStruct):
    fields = [
        ("ModuleName", PSTR()),
        ("hFile", HANDLE()),
        ("MappedAddress", PUCHAR()),
        ("FileHeader", PIMAGE_NT_HEADERS()),
        ("LastRvaSection", PIMAGE_SECTION_HEADER()),
        ("NumberOfSections", ULONG()),
        ("Sections", PIMAGE_SECTION_HEADER()),
        ("Characteristics", _IMAGE_FILE_CHARACTERISTICS_ULONG_()),
        ("fSystemImage", BOOLEAN()),
        ("fDOSImage", BOOLEAN()),
        ("fReadOnly", BOOLEAN()),
        ("Version", UCHAR()),
        ("Links", LIST_ENTRY()),
        ("SizeOfImage", ULONG()),
    ]

PLOADED_IMAGE = Ptr("<I", LOADED_IMAGE())

###################

###### Functions ######

def imagehlp_GetImageConfigInformation(jitter):
    """
    BOOL GetImageConfigInformation(
        PLOADED_IMAGE LoadedImage,
        PIMAGE_LOAD_CONFIG_DIRECTORY ImageConfigInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LoadedImage", "ImageConfigInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_GetImageUnusedHeaderBytes(jitter):
    """
    DWORD GetImageUnusedHeaderBytes(
        PLOADED_IMAGE LoadedImage,
        PDWORD SizeUnusedHeaderBytes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LoadedImage", "SizeUnusedHeaderBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageLoad(jitter):
    """
    PLOADED_IMAGE ImageLoad(
        PSTR DllName,
        PSTR DllPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DllName", "DllPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageUnload(jitter):
    """
    BOOL ImageUnload(
        PLOADED_IMAGE LoadedImage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LoadedImage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_MapAndLoad(jitter):
    """
    BOOL MapAndLoad(
        PSTR ImageName,
        PSTR DllPath,
        PLOADED_IMAGE LoadedImage,
        BOOL DotDll,
        BOOL ReadOnly
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageName", "DllPath", "LoadedImage", "DotDll", "ReadOnly"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_SetImageConfigInformation(jitter):
    """
    BOOL SetImageConfigInformation(
        PLOADED_IMAGE LoadedImage,
        PIMAGE_LOAD_CONFIG_DIRECTORY ImageConfigInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LoadedImage", "ImageConfigInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_UnMapAndLoad(jitter):
    """
    BOOL UnMapAndLoad(
        PLOADED_IMAGE LoadedImage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LoadedImage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageAddCertificate(jitter):
    """
    BOOL ImageAddCertificate(
        HANDLE FileHandle,
        LPWIN_CERTIFICATE Certificate,
        PDWORD Index
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Certificate", "Index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageEnumerateCertificates(jitter):
    """
    BOOL ImageEnumerateCertificates(
        HANDLE FileHandle,
        WORD TypeFilter,
        PDWORD CertificateCount,
        PDWORD Indices,
        DWORD IndexCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "TypeFilter", "CertificateCount", "Indices", "IndexCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageGetCertificateData(jitter):
    """
    BOOL ImageGetCertificateData(
        HANDLE FileHandle,
        DWORD CertificateIndex,
        LPWIN_CERTIFICATE Certificate,
        PDWORD RequiredLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "CertificateIndex", "Certificate", "RequiredLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageGetCertificateHeader(jitter):
    """
    BOOL ImageGetCertificateHeader(
        HANDLE FileHandle,
        DWORD CertificateIndex,
        LPWIN_CERTIFICATE CertificateHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "CertificateIndex", "CertificateHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageGetDigestStream(jitter):
    """
    BOOL ImageGetDigestStream(
        HANDLE FileHandle,
        DWORD DigestLevel,
        DIGEST_FUNCTION DigestFunction,
        DIGEST_HANDLE DigestHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "DigestLevel", "DigestFunction", "DigestHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_ImageRemoveCertificate(jitter):
    """
    BOOL ImageRemoveCertificate(
        HANDLE FileHandle,
        DWORD Index
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_BindImage(jitter):
    """
    BOOL BindImage(
        PSTR ImageName,
        PSTR DllPath,
        PSTR SymbolPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageName", "DllPath", "SymbolPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_BindImageEx(jitter):
    """
    BOOL BindImageEx(
        DWORD Flags,
        PSTR ImageName,
        PSTR DllPath,
        PSTR SymbolPath,
        PIMAGEHLP_STATUS_ROUTINE StatusRoutine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "ImageName", "DllPath", "SymbolPath", "StatusRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_CheckSumMappedFile(jitter):
    """
    PIMAGE_NT_HEADERS CheckSumMappedFile(
        PVOID BaseAddress,
        DWORD FileLength,
        PDWORD HeaderSum,
        PDWORD CheckSum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress", "FileLength", "HeaderSum", "CheckSum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_MapFileAndCheckSum(jitter, get_str, set_str):
    """
    DWORD MapFileAndCheckSum(
        PTSTR Filename,
        PDWORD HeaderSum,
        PDWORD CheckSum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Filename", "HeaderSum", "CheckSum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_MapFileAndCheckSumA(jitter):
    imagehlp_MapFileAndCheckSum(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def imagehlp_MapFileAndCheckSumW(jitter):
    imagehlp_MapFileAndCheckSum(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def imagehlp_ReBaseImage(jitter):
    """
    BOOL ReBaseImage(
        PCSTR CurrentImageName,
        PCSTR SymbolPath,
        BOOL fReBase,
        BOOL fRebaseSysfileOk,
        BOOL fGoingDown,
        ULONG CheckImageSize,
        ULONG* OldImageSize,
        ULONG_PTR* OldImageBase,
        ULONG* NewImageSize,
        ULONG_PTR* NewImageBase,
        ULONG TimeStamp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CurrentImageName", "SymbolPath", "fReBase", "fRebaseSysfileOk", "fGoingDown", "CheckImageSize", "OldImageSize", "OldImageBase", "NewImageSize", "NewImageBase", "TimeStamp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_SplitSymbols(jitter):
    """
    BOOL SplitSymbols(
        PSTR ImageName,
        PSTR SymbolsPath,
        PSTR SymbolFilePath,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageName", "SymbolsPath", "SymbolFilePath", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_TouchFileTimes(jitter):
    """
    BOOL TouchFileTimes(
        HANDLE FileHandle,
        PSYSTEMTIME pSystemTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "pSystemTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_UpdateDebugInfoFile(jitter):
    """
    BOOL UpdateDebugInfoFile(
        PSTR ImageFileName,
        PSTR SymbolPath,
        PSTR DebugFilePath,
        PIMAGE_NT_HEADERS NtHeaders
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageFileName", "SymbolPath", "DebugFilePath", "NtHeaders"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def imagehlp_UpdateDebugInfoFileEx(jitter):
    """
    BOOL UpdateDebugInfoFileEx(
        PSTR ImageFileName,
        PSTR SymbolPath,
        PSTR DebugFilePath,
        PIMAGE_NT_HEADERS NtHeaders,
        DWORD OldChecksum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageFileName", "SymbolPath", "DebugFilePath", "NtHeaders", "OldChecksum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
