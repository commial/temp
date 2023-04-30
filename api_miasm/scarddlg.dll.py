###### Enums ######

###################

###### Types ######
LPOCNCHKPROC = LPVOID
LPOCNCONNPROC = LPVOID
LPOCNDSCPROC = LPVOID
_SC_DLG_FLAGS_ = DWORD

class OPENCARDNAME(MemStruct):
    fields = [
        ("dwStructSize", DWORD()),
        ("hwndOwner", HWND()),
        ("hSCardContext", SCARDCONTEXT()),
        ("lpstrGroupNames", LPTSTR()),
        ("nMaxGroupNames", DWORD()),
        ("lpstrCardNames", LPTSTR()),
        ("nMaxCardNames", DWORD()),
        ("rgguidInterfaces", LPCGUID()),
        ("cguidInterfaces", DWORD()),
        ("lpstrRdr", LPTSTR()),
        ("nMaxRdr", DWORD()),
        ("lpstrCard", LPTSTR()),
        ("nMaxCard", DWORD()),
        ("lpstrTitle", LPCTSTR()),
        ("dwFlags", _SC_DLG_FLAGS_()),
        ("pvUserData", LPVOID()),
        ("dwShareMode", DWORD()),
        ("dwPreferredProtocols", DWORD()),
        ("dwActiveProtocol", DWORD()),
        ("lpfnConnect", LPOCNCONNPROC()),
        ("lpfnCheck", LPOCNCHKPROC()),
        ("lpfnDisconnect", LPOCNDSCPROC()),
        ("hCardHandle", SCARDHANDLE()),
    ]

LPOPENCARDNAME = Ptr("<I", OPENCARDNAME())

class OPENCARD_SEARCH_CRITERIA(MemStruct):
    fields = [
        ("dwStructSize", DWORD()),
        ("lpstrGroupNames", LPTSTR()),
        ("nMaxGroupNames", DWORD()),
        ("rgguidInterfaces", LPCGUID()),
        ("cguidInterfaces", DWORD()),
        ("lpstrCardNames", LPTSTR()),
        ("nMaxCardNames", DWORD()),
        ("lpfnCheck", LPOCNCHKPROC()),
        ("lpfnConnect", LPOCNCONNPROC()),
        ("lpfnDisconnect", LPOCNDSCPROC()),
        ("pvUserData", LPVOID()),
        ("dwShareMode", DWORD()),
        ("dwPreferredProtocols", DWORD()),
    ]

POPENCARD_SEARCH_CRITERIA = Ptr("<I", OPENCARD_SEARCH_CRITERIA())

class OPENCARDNAME_EX(MemStruct):
    fields = [
        ("dwStructSize", DWORD()),
        ("hSCardContext", SCARDCONTEXT()),
        ("hwndOwner", HWND()),
        ("dwFlags", _SC_DLG_FLAGS_()),
        ("lpstrTitle", LPCTSTR()),
        ("lpstrSearchDesc", LPCTSTR()),
        ("hIcon", HICON()),
        ("pOpenCardSearchCriteria", POPENCARD_SEARCH_CRITERIA()),
        ("lpfnConnect", LPOCNCONNPROC()),
        ("pvUserData", LPVOID()),
        ("dwShareMode", DWORD()),
        ("dwPreferredProtocols", DWORD()),
        ("lpstrRdr", LPTSTR()),
        ("nMaxRdr", DWORD()),
        ("lpstrCard", LPTSTR()),
        ("nMaxCard", DWORD()),
        ("dwActiveProtocol", DWORD()),
        ("hCardHandle", SCARDHANDLE()),
    ]

LPOPENCARDNAME_EX = Ptr("<I", OPENCARDNAME_EX())

###################

###### Functions ######

def scarddlg_GetOpenCardName(jitter, get_str, set_str):
    """
    [SCARD_ERROR] GetOpenCardName(
        LPOPENCARDNAME pDlgStruc
    )
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
    [SCARD_ERROR] SCardDlgExtendedError()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def scarddlg_SCardUIDlgSelectCard(jitter, get_str, set_str):
    """
    [SCARD_ERROR] SCardUIDlgSelectCard(
        LPOPENCARDNAME_EX pDlgStruc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDlgStruc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def scarddlg_SCardUIDlgSelectCardA(jitter):
    scarddlg_SCardUIDlgSelectCard(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def scarddlg_SCardUIDlgSelectCardW(jitter):
    scarddlg_SCardUIDlgSelectCard(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
