###### Enums ######

###################

###### Types ######

class PPROTECT_FILE_ENTRY(MemStruct):
    fields = [
        ("SourceFileName", PWSTR()),
        ("FileName", PWSTR()),
        ("InfName", PWSTR()),
    ]

PPROTECT_FILE_ENTRY_PTR = Ptr("<I", PPROTECT_FILE_ENTRY())

###################

###### Functions ######

def sfcfiles_SfcGetFiles(jitter):
    """
    NTSTATUS SfcGetFiles(
        PPROTECT_FILE_ENTRY* ProtFileData,
        PULONG FileCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProtFileData", "FileCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
