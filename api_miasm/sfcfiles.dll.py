
def sfcfiles_SfcGetFiles(jitter):
    """
    [Sfcfiles.dll] NTSTATUS SfcGetFiles(PPROTECT_FILE_ENTRY* ProtFileData, PULONG FileCount)
    """
    ret_ad, args = jitter.func_args_stdcall(["ProtFileData", "FileCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
