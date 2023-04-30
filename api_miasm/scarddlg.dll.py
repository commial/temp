
def scarddlg_GetOpenCardName(jitter, get_str, set_str):
    """
    [SCardDlg.dll] [SCARD_ERROR] GetOpenCardName(LPOPENCARDNAME pDlgStruc)
    """
    ret_ad, args = jitter.func_args_stdcall(["pDlgStruc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def scarddlg_GetOpenCardNameA(jitter):
    scarddlg_GetOpenCardName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def scarddlg_GetOpenCardNameW(jitter):
    scarddlg_GetOpenCardName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def scarddlg_SCardDlgExtendedError(jitter):
    """
    [SCardDlg.dll] [SCARD_ERROR] SCardDlgExtendedError()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def scarddlg_SCardUIDlgSelectCard(jitter, get_str, set_str):
    """
    [SCardDlg.dll] [SCARD_ERROR] SCardUIDlgSelectCard(LPOPENCARDNAME_EX pDlgStruc)
    """
    ret_ad, args = jitter.func_args_stdcall(["pDlgStruc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def scarddlg_SCardUIDlgSelectCardA(jitter):
    scarddlg_SCardUIDlgSelectCard(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def scarddlg_SCardUIDlgSelectCardW(jitter):
    scarddlg_SCardUIDlgSelectCard(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
