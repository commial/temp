
def fxsutility_CanSendToFaxRecipient(jitter):
    """
    [FxsUtility.dll] BOOL CanSendToFaxRecipient()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsutility_SendToFaxRecipient(jitter):
    """
    [FxsUtility.dll] DWORD SendToFaxRecipient(SendToMode sndMode, LPCWSTR lpFileName)
    """
    ret_ad, args = jitter.func_args_stdcall(["sndMode", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
