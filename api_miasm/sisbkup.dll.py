###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def sisbkup_SisCreateBackupStructure(jitter):
    """
    BOOL SisCreateBackupStructure(
        PWCHAR volumeRoot,
        PVOID* sisBackupStructure,
        PWCHAR* commonStoreRootPathname,
        PULONG countOfCommonStoreFilesToBackUp,
        PWCHAR** commonStoreFilesToBackUp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["volumeRoot", "sisBackupStructure", "commonStoreRootPathname", "countOfCommonStoreFilesToBackUp", "commonStoreFilesToBackUp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sisbkup_SisCreateRestoreStructure(jitter):
    """
    BOOL SisCreateRestoreStructure(
        PWCHAR volumeRoot,
        PVOID* sisRestoreStructure,
        PWCHAR* commonStoreRootPathname,
        PULONG countOfCommonStoreFilesToRestore,
        PWCHAR** commonStoreFilesToRestore
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["volumeRoot", "sisRestoreStructure", "commonStoreRootPathname", "countOfCommonStoreFilesToRestore", "commonStoreFilesToRestore"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sisbkup_SisCSFilesToBackupForLink(jitter):
    """
    BOOL SisCSFilesToBackupForLink(
        PVOID sisBackupStructure,
        PVOID reparseData,
        ULONG reparseDataSize,
        PVOID thisFileContext,
        PVOID* matchingFileContext,
        PULONG countOfCommonStoreFilesToBackUp,
        PWCHAR** commonStoreFilesToBackUp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sisBackupStructure", "reparseData", "reparseDataSize", "thisFileContext", "matchingFileContext", "countOfCommonStoreFilesToBackUp", "commonStoreFilesToBackUp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sisbkup_SisFreeAllocatedMemory(jitter):
    """
    void SisFreeAllocatedMemory(
        PVOID allocatedSpace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["allocatedSpace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sisbkup_SisFreeBackupStructure(jitter):
    """
    BOOL SisFreeBackupStructure(
        PVOID sisBackupStructure
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sisBackupStructure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sisbkup_SisFreeRestoreStructure(jitter):
    """
    BOOL SisFreeRestoreStructure(
        PVOID sisRestoreStructure
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sisRestoreStructure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sisbkup_SisRestoredLink(jitter):
    """
    BOOL SisRestoredLink(
        PVOID sisRestoreStructure,
        PWCHAR restoredFileName,
        PVOID reparseData,
        ULONG reparseDataSize,
        PULONG countOfCommonStoreFilesToRestore,
        PWCHAR** commonStoreFilesToRestore
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sisRestoreStructure", "restoredFileName", "reparseData", "reparseDataSize", "countOfCommonStoreFilesToRestore", "commonStoreFilesToRestore"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
