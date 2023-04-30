
def scarddlg_GetOpenCardName(jitter):
    """"
    [SCardDlg.dll] [SCARD_ERROR] GetOpenCardName(LPOPENCARDNAME pDlgStruc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pDlgStruc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def scarddlg_SCardDlgExtendedError(jitter):
    """"
    [SCardDlg.dll] [SCARD_ERROR] SCardDlgExtendedError()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def scarddlg_SCardUIDlgSelectCard(jitter):
    """"
    [SCardDlg.dll] [SCARD_ERROR] SCardUIDlgSelectCard(LPOPENCARDNAME_EX pDlgStruc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pDlgStruc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
