
def oledlg_OleUIAddVerbMenu(jitter):
    """"
    [OleDlg.dll] BOOL OleUIAddVerbMenu(LPOLEOBJECT lpOleObj, LPCTSTR lpszShortType, HMENU hMenu, UINT uPos, UINT uIDVerbMin, UINT uIDVerbMax, BOOL bAddConvert, UINT idConvert, HMENU* lphMenu)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpOleObj", "lpszShortType", "hMenu", "uPos", "uIDVerbMin", "uIDVerbMax", "bAddConvert", "idConvert", "lphMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIBusy(jitter):
    """"
    [OleDlg.dll] UINT OleUIBusy(LPOLEUIBUSY lpBZ)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBZ"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUICanConvertOrActivateAs(jitter):
    """"
    [OleDlg.dll] BOOL OleUICanConvertOrActivateAs(REFCLSID rClsid, BOOL fIsLinkedObject, WORD wFormat)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rClsid", "fIsLinkedObject", "wFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIChangeIcon(jitter):
    """"
    [OleDlg.dll] UINT OleUIChangeIcon(LPOLEUICHANGEICON lpCI)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCI"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIChangeSource(jitter):
    """"
    [OleDlg.dll] UINT OleUIChangeSource(LPOLEUICHANGESOURCE lpCS)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIConvert(jitter):
    """"
    [OleDlg.dll] UINT OleUIConvert(LPOLEUICONVERT lpCV)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpCV"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIEditLinks(jitter):
    """"
    [OleDlg.dll] UINT OleUIEditLinks(LPOLEUIEDITLINKS lpEL)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpEL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIInsertObject(jitter):
    """"
    [OleDlg.dll] UINT OleUIInsertObject(LPOLEUIINSERTOBJECT lpIO)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpIO"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIObjectProperties(jitter):
    """"
    [OleDlg.dll] UINT OleUIObjectProperties(LPOLEUIOBJECTPROPS lpOF)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpOF"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIPasteSpecial(jitter):
    """"
    [OleDlg.dll] UINT OleUIPasteSpecial(LPOLEUIPASTESPECIAL lpPS)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIPromptUser(jitter):
    """"
    [OleDlg.dll] int OleUIPromptUser(int nTemplate, HWND hwndParent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nTemplate", "hwndParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIUpdateLinks(jitter):
    """"
    [OleDlg.dll] BOOL OleUIUpdateLinks(LPOLEUILINKCONTAINER lpOleUILinkCntr, HWND hwndParent, LPTSTR lpszTitle, int cLinks)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpOleUILinkCntr", "hwndParent", "lpszTitle", "cLinks"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
