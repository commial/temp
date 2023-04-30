###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def vhdmount_GetSCSIAddress(jitter):
    """
    [ERROR_CODE_ULONG] GetSCSIAddress(
        PWCHAR VHDFileName,
        ULONG Flags,
        ULONG SCSIAddressLength,
        PWCHAR SCSIAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VHDFileName", "Flags", "SCSIAddressLength", "SCSIAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def vhdmount_MountVHD(jitter):
    """
    [ERROR_CODE_ULONG] MountVHD(
        PWCHAR VHDFileName,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VHDFileName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def vhdmount_UnmountVHD(jitter):
    """
    [ERROR_CODE_ULONG] UnmountVHD(
        PWCHAR VHDFileName,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VHDFileName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
