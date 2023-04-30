_RESTOREPOINT_EVENT_ = {
    "BEGIN_SYSTEM_CHANGE": 100,
    "END_SYSTEM_CHANGE": 101,
    "BEGIN_NESTED_SYSTEM_CHANGE": 102,
    "END_NESTED_SYSTEM_CHANGE": 103,
    "BEGIN_NESTED_SYSTEM_CHANGE_NORP": 104,
}
_RESTOREPOINT_TYPE_ = {
    "APPLICATION_INSTALL": 0,
    "APPLICATION_UNINSTALL": 1,
    "RESTORE": 6,
    "CHECKPOINT": 7,
    "DEVICE_DRIVER_INSTALL": 10,
    "FIRSTRUN": 11,
    "MODIFY_SETTINGS": 12,
    "CANCELLED_OPERATION": 13,
    "BACKUP_RECOVERY": 14,
    "BACKUP": 15,
    "MANUAL_CHECKPOINT": 16,
    "WINDOWS_UPDATE": 17,
    "CRITICAL_UPDATE": 18,
}

def srclient_SRRemoveRestorePoint(jitter):
    """
    [ERROR_CODE] SRRemoveRestorePoint(
        DWORD dwRPNum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwRPNum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def srclient_SRSetRestorePointA(jitter):
    """
    BOOL SRSetRestorePointA(
        PRESTOREPOINTINFOA pRestorePtSpec,
        PSTATEMGRSTATUS pSMgrStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRestorePtSpec", "pSMgrStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def srclient_SRSetRestorePointW(jitter):
    """
    BOOL SRSetRestorePointW(
        PRESTOREPOINTINFOW pRestorePtSpec,
        PSTATEMGRSTATUS pSMgrStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRestorePtSpec", "pSMgrStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def srclient_SRSetRestorePointInternal(jitter):
    """
    BOOL SRSetRestorePointInternal(
        PRESTOREPOINTINFOW pRestorePtSpec,
        PSTATEMGRSTATUS pSMgrStatus,
        BOOL fForceSurrogate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRestorePtSpec", "pSMgrStatus", "fForceSurrogate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
