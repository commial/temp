###### Enums ######

###################

###### Types ######
LPFNOLEUIHOOK = LPVOID
LPOLEUILINKCONTAINER = LPVOID
LPOLEUIOBJINFO = LPVOID
LPOLEUILINKINFO = LPVOID
_ChangeIconFlag_ = DWORD

class OLEUICHANGEICON(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwFlags", _ChangeIconFlag_()),
        ("hWndOwner", HWND()),
        ("lpszCaption", LPCTSTR()),
        ("lpfnHook", LPFNOLEUIHOOK()),
        ("lCustData", LPARAM()),
        ("hInstance", HINSTANCE()),
        ("lpszTemplate", LPCTSTR()),
        ("hResource", HRSRC()),
        ("hMetaPict", HGLOBAL()),
        ("clsid", CLSID()),
        ("szIconExe", TCHAR__MAX_PATH_()),
        ("cchIconExe", int()),
    ]

LPOLEUICHANGEICON = Ptr("<I", OLEUICHANGEICON())
_PasteSpecialFlag_ = DWORD
OLEUIPASTEFLAG = DWORD

class OLEUIPASTEENTRY(MemStruct):
    fields = [
        ("fmtetc", FORMATETC()),
        ("lpstrFormatName", LPCTSTR()),
        ("lpstrResultText", LPCTSTR()),
        ("dwFlags", OLEUIPASTEFLAG()),
        ("dwScratchSpace", DWORD()),
    ]

LPOLEUIPASTEENTRY = Ptr("<I", OLEUIPASTEENTRY())

class OLEUIPASTESPECIAL(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwFlags", _PasteSpecialFlag_()),
        ("hWndOwner", HWND()),
        ("lpszCaption", LPCTSTR()),
        ("lpfnHook", LPFNOLEUIHOOK()),
        ("lCustData", LPARAM()),
        ("hInstance", HINSTANCE()),
        ("lpszTemplate", LPCTSTR()),
        ("hResource", HRSRC()),
        ("lpSrcDataObj", LPDATAOBJECT()),
        ("arrPasteEntries", LPOLEUIPASTEENTRY()),
        ("cPasteEntries", int()),
        ("arrLinkTypes", UINT_PTR()),
        ("cLinkTypes", int()),
        ("cClsidExclude", UINT()),
        ("lpClsidExclude", LPCLSID()),
        ("nSelectedIndex", int()),
        ("fLink", BOOL()),
        ("hMetaPict", HGLOBAL()),
        ("sizel", SIZEL()),
    ]

LPOLEUIPASTESPECIAL = Ptr("<I", OLEUIPASTESPECIAL())
_ObjectPropFlags_ = DWORD

class OLEUIGNRLPROPS(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwFlags", DWORD()),
        ("dwReserved1", DWORD__2_()),
        ("lpfnHook", LPFNOLEUIHOOK()),
        ("lCustData", LPARAM()),
        ("dwReserved2", DWORD__3_()),
        ("lpOP", LPVOID()),
    ]

LPOLEUIGNRLPROPS = Ptr("<I", OLEUIGNRLPROPS())
_ViewPropsFlags_ = DWORD

class OLEUIVIEWPROPS(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwFlags", _ViewPropsFlags_()),
        ("dwReserved1", DWORD__2_()),
        ("lpfnHook", LPFNOLEUIHOOK()),
        ("lCustData", LPARAM()),
        ("dwReserved2", DWORD__3_()),
        ("lpOP", LPVOID()),
        ("nScaleMin", int()),
        ("nScaleMax", int()),
    ]

LPOLEUIVIEWPROPS = Ptr("<I", OLEUIVIEWPROPS())

class OLEUILINKPROPS(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwFlags", DWORD()),
        ("dwReserved1", DWORD__2_()),
        ("lpfnHook", LPFNOLEUIHOOK()),
        ("lCustData", LPARAM()),
        ("dwReserved2", DWORD__3_()),
        ("lpOP", LPVOID()),
    ]

LPOLEUILINKPROPS = Ptr("<I", OLEUILINKPROPS())

class OLEUIOBJECTPROPS(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwFlags", _ObjectPropFlags_()),
        ("lpPS", LPPROPSHEETHEADER()),
        ("dwObject", DWORD()),
        ("lpObjInfo", LPOLEUIOBJINFO()),
        ("dwLink", DWORD()),
        ("lpLinkInfo", LPOLEUILINKINFO()),
        ("lpGP", LPOLEUIGNRLPROPS()),
        ("lpVP", LPOLEUIVIEWPROPS()),
        ("lpLP", LPOLEUILINKPROPS()),
    ]

LPOLEUIOBJECTPROPS = Ptr("<I", OLEUIOBJECTPROPS())
_ChangeSourceFlags_ = DWORD

class OLEUICHANGESOURCE(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwFlags", _ChangeSourceFlags_()),
        ("hWndOwner", HWND()),
        ("lpszCaption", LPCTSTR()),
        ("lpfnHook", LPFNOLEUIHOOK()),
        ("lCustData", LPARAM()),
        ("hInstance", HINSTANCE()),
        ("lpszTemplate", LPCTSTR()),
        ("hResource", HRSRC()),
        ("lpOFN", OPENFILENAME_PTR()),
        ("dwReserved1", DWORD__4_()),
        ("lpOleUILinkContainer", LPOLEUILINKCONTAINER()),
        ("dwLink", DWORD()),
        ("lpszDisplayName", LPTSTR()),
        ("nFileLength", ULONG()),
        ("lpszFrom", LPTSTR()),
        ("lpszTo", LPSTR()),
    ]

LPOLEUICHANGESOURCE = Ptr("<I", OLEUICHANGESOURCE())

class OLEUIBUSY(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwFlags", DWORD()),
        ("hWndOwner", HWND()),
        ("lpszCaption", LPCTSTR()),
        ("lpfnHook", LPFNOLEUIHOOK()),
        ("lCustData", LPARAM()),
        ("hInstance", HINSTANCE()),
        ("lpszTemplate", LPCTSTR()),
        ("hResource", HRSRC()),
        ("hTask", HTASK()),
        ("lphWndDialog", HWND_PTR()),
    ]

LPOLEUIBUSY = Ptr("<I", OLEUIBUSY())

class OLEUICONVERT(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwFlags", DWORD()),
        ("hWndOwner", HWND()),
        ("lpszCaption", LPCTSTR()),
        ("lpfnHook", LPFNOLEUIHOOK()),
        ("lCustData", LPARAM()),
        ("hInstance", HINSTANCE()),
        ("lpszTemplate", LPCTSTR()),
        ("hResource", HRSRC()),
        ("clsid", CLSID()),
        ("clsidConvertDefault", CLSID()),
        ("clsidActivateDefault", CLSID()),
        ("clsidNew", CLSID()),
        ("dvAspect", DWORD()),
        ("wFormat", WORD()),
        ("fIsLinkedObject", BOOL()),
        ("hMetaPict", HGLOBAL()),
        ("lpszUserType", LPTSTR()),
        ("fObjectsIconChanged", BOOL()),
        ("lpszDefLabel", LPTSTR()),
        ("cClsidExclude", UINT()),
        ("lpClsidExclude", LPCLSID()),
    ]

LPOLEUICONVERT = Ptr("<I", OLEUICONVERT())

class OLEUIEDITLINKS(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwFlags", DWORD()),
        ("hWndOwner", HWND()),
        ("lpszCaption", LPCTSTR()),
        ("lpfnHook", LPFNOLEUIHOOK()),
        ("lCustData", LPARAM()),
        ("hInstance", HINSTANCE()),
        ("lpszTemplate", LPCTSTR()),
        ("hResource", HRSRC()),
        ("lpOleUILinkContainer", LPOLEUILINKCONTAINER()),
    ]

LPOLEUIEDITLINKS = Ptr("<I", OLEUIEDITLINKS())

class OLEUIINSERTOBJECT(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwFlags", DWORD()),
        ("hWndOwner", HWND()),
        ("lpszCaption", LPCTSTR()),
        ("lpfnHook", LPFNOLEUIHOOK()),
        ("lCustData", LPARAM()),
        ("hInstance", HINSTANCE()),
        ("lpszTemplate", LPCTSTR()),
        ("hResource", HRSRC()),
        ("clsid", CLSID()),
        ("lpszFile", LPTSTR()),
        ("cchFile", UINT()),
        ("cClsidExclude", UINT()),
        ("lpClsidExclude", LPCLSID()),
        ("iid", IID()),
        ("oleRender", DWORD()),
        ("lpFormatEtc", LPFORMATETC()),
        ("lpIOleClientSite", LPOLECLIENTSITE()),
        ("lpIStorage", LPSTORAGE()),
        ("ppvObj", LPVOID_PTR()),
        ("sc", SCODE()),
        ("hMetaPict", HGLOBAL()),
    ]

LPOLEUIINSERTOBJECT = Ptr("<I", OLEUIINSERTOBJECT())

###################

###### Functions ######

def oledlg_OleUIAddVerbMenu(jitter, get_str, set_str):
    """
    BOOL OleUIAddVerbMenu(
        LPOLEOBJECT lpOleObj,
        LPCTSTR lpszShortType,
        HMENU hMenu,
        UINT uPos,
        UINT uIDVerbMin,
        UINT uIDVerbMax,
        BOOL bAddConvert,
        UINT idConvert,
        HMENU* lphMenu
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpOleObj", "lpszShortType", "hMenu", "uPos", "uIDVerbMin", "uIDVerbMax", "bAddConvert", "idConvert", "lphMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIAddVerbMenuA(jitter):
    oledlg_OleUIAddVerbMenu(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIAddVerbMenuW(jitter):
    oledlg_OleUIAddVerbMenu(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIBusy(jitter, get_str, set_str):
    """
    UINT OleUIBusy(
        LPOLEUIBUSY lpBZ
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpBZ"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIBusyA(jitter):
    oledlg_OleUIBusy(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIBusyW(jitter):
    oledlg_OleUIBusy(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUICanConvertOrActivateAs(jitter):
    """
    BOOL OleUICanConvertOrActivateAs(
        REFCLSID rClsid,
        BOOL fIsLinkedObject,
        WORD wFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rClsid", "fIsLinkedObject", "wFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIChangeIcon(jitter, get_str, set_str):
    """
    UINT OleUIChangeIcon(
        LPOLEUICHANGEICON lpCI
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpCI"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIChangeIconA(jitter):
    oledlg_OleUIChangeIcon(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIChangeIconW(jitter):
    oledlg_OleUIChangeIcon(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIChangeSource(jitter, get_str, set_str):
    """
    UINT OleUIChangeSource(
        LPOLEUICHANGESOURCE lpCS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpCS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIChangeSourceA(jitter):
    oledlg_OleUIChangeSource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIChangeSourceW(jitter):
    oledlg_OleUIChangeSource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIConvert(jitter, get_str, set_str):
    """
    UINT OleUIConvert(
        LPOLEUICONVERT lpCV
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpCV"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIConvertA(jitter):
    oledlg_OleUIConvert(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIConvertW(jitter):
    oledlg_OleUIConvert(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIEditLinks(jitter, get_str, set_str):
    """
    UINT OleUIEditLinks(
        LPOLEUIEDITLINKS lpEL
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpEL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIEditLinksA(jitter):
    oledlg_OleUIEditLinks(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIEditLinksW(jitter):
    oledlg_OleUIEditLinks(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIInsertObject(jitter, get_str, set_str):
    """
    UINT OleUIInsertObject(
        LPOLEUIINSERTOBJECT lpIO
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpIO"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIInsertObjectA(jitter):
    oledlg_OleUIInsertObject(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIInsertObjectW(jitter):
    oledlg_OleUIInsertObject(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIObjectProperties(jitter, get_str, set_str):
    """
    UINT OleUIObjectProperties(
        LPOLEUIOBJECTPROPS lpOF
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpOF"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIObjectPropertiesA(jitter):
    oledlg_OleUIObjectProperties(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIObjectPropertiesW(jitter):
    oledlg_OleUIObjectProperties(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIPasteSpecial(jitter, get_str, set_str):
    """
    UINT OleUIPasteSpecial(
        LPOLEUIPASTESPECIAL lpPS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpPS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIPasteSpecialA(jitter):
    oledlg_OleUIPasteSpecial(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIPasteSpecialW(jitter):
    oledlg_OleUIPasteSpecial(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIPromptUser(jitter, get_str, set_str):
    """
    int OleUIPromptUser(
        int nTemplate,
        HWND hwndParent,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nTemplate", "hwndParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIPromptUserA(jitter):
    oledlg_OleUIPromptUser(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIPromptUserW(jitter):
    oledlg_OleUIPromptUser(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oledlg_OleUIUpdateLinks(jitter, get_str, set_str):
    """
    BOOL OleUIUpdateLinks(
        LPOLEUILINKCONTAINER lpOleUILinkCntr,
        HWND hwndParent,
        LPTSTR lpszTitle,
        int cLinks
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpOleUILinkCntr", "hwndParent", "lpszTitle", "cLinks"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oledlg_OleUIUpdateLinksA(jitter):
    oledlg_OleUIUpdateLinks(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oledlg_OleUIUpdateLinksW(jitter):
    oledlg_OleUIUpdateLinks(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
