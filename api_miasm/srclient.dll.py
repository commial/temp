
def srclient_SRRemoveRestorePoint(jitter):
    """"
    [SrClient.dll] [ERROR_CODE] SRRemoveRestorePoint(DWORD dwRPNum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwRPNum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def srclient_SRSetRestorePointA(jitter):
    """"
    [SrClient.dll] BOOL SRSetRestorePointA(PRESTOREPOINTINFOA pRestorePtSpec, PSTATEMGRSTATUS pSMgrStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRestorePtSpec", "pSMgrStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def srclient_SRSetRestorePointW(jitter):
    """"
    [SrClient.dll] BOOL SRSetRestorePointW(PRESTOREPOINTINFOW pRestorePtSpec, PSTATEMGRSTATUS pSMgrStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRestorePtSpec", "pSMgrStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def srclient_SRSetRestorePointInternal(jitter):
    """"
    [SrClient.dll] BOOL SRSetRestorePointInternal(PRESTOREPOINTINFOW pRestorePtSpec, PSTATEMGRSTATUS pSMgrStatus, BOOL fForceSurrogate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRestorePtSpec", "pSMgrStatus", "fForceSurrogate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)