
def oledlg_OleUIAddVerbMenu(jitter, get_str, set_str):
    """"
    [OleDlg.dll] BOOL OleUIAddVerbMenu(LPOLEOBJECT lpOleObj, LPCTSTR lpszShortType, HMENU hMenu, UINT uPos, UINT uIDVerbMin, UINT uIDVerbMax, BOOL bAddConvert, UINT idConvert, HMENU* lphMenu)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpOleObj", "lpszShortType", "hMenu", "uPos", "uIDVerbMin", "uIDVerbMax", "bAddConvert", "idConvert", "lphMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIAddVerbMenuA(jitter):
    oledlg_OleUIAddVerbMenu(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIAddVerbMenuW(jitter):
    oledlg_OleUIAddVerbMenu(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIBusy(jitter, get_str, set_str):
    """"
    [OleDlg.dll] UINT OleUIBusy(LPOLEUIBUSY lpBZ)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBZ"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIBusyA(jitter):
    oledlg_OleUIBusy(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIBusyW(jitter):
    oledlg_OleUIBusy(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUICanConvertOrActivateAs(jitter):
    """"
    [OleDlg.dll] BOOL OleUICanConvertOrActivateAs(REFCLSID rClsid, BOOL fIsLinkedObject, WORD wFormat)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rClsid", "fIsLinkedObject", "wFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIChangeIcon(jitter, get_str, set_str):
    """"
    [OleDlg.dll] UINT OleUIChangeIcon(LPOLEUICHANGEICON lpCI)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCI"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIChangeIconA(jitter):
    oledlg_OleUIChangeIcon(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIChangeIconW(jitter):
    oledlg_OleUIChangeIcon(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIChangeSource(jitter, get_str, set_str):
    """"
    [OleDlg.dll] UINT OleUIChangeSource(LPOLEUICHANGESOURCE lpCS)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIChangeSourceA(jitter):
    oledlg_OleUIChangeSource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIChangeSourceW(jitter):
    oledlg_OleUIChangeSource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIConvert(jitter, get_str, set_str):
    """"
    [OleDlg.dll] UINT OleUIConvert(LPOLEUICONVERT lpCV)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCV"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIConvertA(jitter):
    oledlg_OleUIConvert(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIConvertW(jitter):
    oledlg_OleUIConvert(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIEditLinks(jitter, get_str, set_str):
    """"
    [OleDlg.dll] UINT OleUIEditLinks(LPOLEUIEDITLINKS lpEL)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpEL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIEditLinksA(jitter):
    oledlg_OleUIEditLinks(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIEditLinksW(jitter):
    oledlg_OleUIEditLinks(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIInsertObject(jitter, get_str, set_str):
    """"
    [OleDlg.dll] UINT OleUIInsertObject(LPOLEUIINSERTOBJECT lpIO)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpIO"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIInsertObjectA(jitter):
    oledlg_OleUIInsertObject(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIInsertObjectW(jitter):
    oledlg_OleUIInsertObject(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIObjectProperties(jitter, get_str, set_str):
    """"
    [OleDlg.dll] UINT OleUIObjectProperties(LPOLEUIOBJECTPROPS lpOF)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpOF"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIObjectPropertiesA(jitter):
    oledlg_OleUIObjectProperties(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIObjectPropertiesW(jitter):
    oledlg_OleUIObjectProperties(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIPasteSpecial(jitter, get_str, set_str):
    """"
    [OleDlg.dll] UINT OleUIPasteSpecial(LPOLEUIPASTESPECIAL lpPS)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIPasteSpecialA(jitter):
    oledlg_OleUIPasteSpecial(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIPasteSpecialW(jitter):
    oledlg_OleUIPasteSpecial(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIPromptUser(jitter, get_str, set_str):
    """"
    [OleDlg.dll] int OleUIPromptUser(int nTemplate, HWND hwndParent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nTemplate", "hwndParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIPromptUserA(jitter):
    oledlg_OleUIPromptUser(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIPromptUserW(jitter):
    oledlg_OleUIPromptUser(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIUpdateLinks(jitter, get_str, set_str):
    """"
    [OleDlg.dll] BOOL OleUIUpdateLinks(LPOLEUILINKCONTAINER lpOleUILinkCntr, HWND hwndParent, LPTSTR lpszTitle, int cLinks)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpOleUILinkCntr", "hwndParent", "lpszTitle", "cLinks"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIUpdateLinksA(jitter):
    oledlg_OleUIUpdateLinks(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIUpdateLinksW(jitter):
    oledlg_OleUIUpdateLinks(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
