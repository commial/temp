SendToMode = {
    "SEND_TO_FAX_RECIPIENT_ATTACHMENT": 0,
}
SendToMode_INV = {
    0: "SEND_TO_FAX_RECIPIENT_ATTACHMENT",
}

def fxsutility_CanSendToFaxRecipient(jitter):
    """
    BOOL CanSendToFaxRecipient()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsutility_SendToFaxRecipient(jitter):
    """
    DWORD SendToFaxRecipient(
        SendToMode sndMode,
        LPCWSTR lpFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sndMode", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
