
def sisbkup_SisCreateBackupStructure(jitter):
    """"
    [Sisbkup.dll] BOOL SisCreateBackupStructure(PWCHAR volumeRoot, PVOID* sisBackupStructure, PWCHAR* commonStoreRootPathname, PULONG countOfCommonStoreFilesToBackUp, PWCHAR** commonStoreFilesToBackUp)
    """"
    ret_ad, args = jitter.func_args_stdcall(["volumeRoot", "sisBackupStructure", "commonStoreRootPathname", "countOfCommonStoreFilesToBackUp", "commonStoreFilesToBackUp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sisbkup_SisCreateRestoreStructure(jitter):
    """"
    [Sisbkup.dll] BOOL SisCreateRestoreStructure(PWCHAR volumeRoot, PVOID* sisRestoreStructure, PWCHAR* commonStoreRootPathname, PULONG countOfCommonStoreFilesToRestore, PWCHAR** commonStoreFilesToRestore)
    """"
    ret_ad, args = jitter.func_args_stdcall(["volumeRoot", "sisRestoreStructure", "commonStoreRootPathname", "countOfCommonStoreFilesToRestore", "commonStoreFilesToRestore"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sisbkup_SisCSFilesToBackupForLink(jitter):
    """"
    [Sisbkup.dll] BOOL SisCSFilesToBackupForLink(PVOID sisBackupStructure, PVOID reparseData, ULONG reparseDataSize, PVOID thisFileContext, PVOID* matchingFileContext, PULONG countOfCommonStoreFilesToBackUp, PWCHAR** commonStoreFilesToBackUp)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sisBackupStructure", "reparseData", "reparseDataSize", "thisFileContext", "matchingFileContext", "countOfCommonStoreFilesToBackUp", "commonStoreFilesToBackUp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sisbkup_SisFreeAllocatedMemory(jitter):
    """"
    [Sisbkup.dll] void SisFreeAllocatedMemory(PVOID allocatedSpace)
    """"
    ret_ad, args = jitter.func_args_stdcall(["allocatedSpace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sisbkup_SisFreeBackupStructure(jitter):
    """"
    [Sisbkup.dll] BOOL SisFreeBackupStructure(PVOID sisBackupStructure)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sisBackupStructure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sisbkup_SisFreeRestoreStructure(jitter):
    """"
    [Sisbkup.dll] BOOL SisFreeRestoreStructure(PVOID sisRestoreStructure)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sisRestoreStructure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sisbkup_SisRestoredLink(jitter):
    """"
    [Sisbkup.dll] BOOL SisRestoredLink(PVOID sisRestoreStructure, PWCHAR restoredFileName, PVOID reparseData, ULONG reparseDataSize, PULONG countOfCommonStoreFilesToRestore, PWCHAR** commonStoreFilesToRestore)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sisRestoreStructure", "restoredFileName", "reparseData", "reparseDataSize", "countOfCommonStoreFilesToRestore", "commonStoreFilesToRestore"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
