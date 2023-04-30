###### Enums ######
_RASMDPAGE_ = {
    "RASMDPAGE_Status": 0,
    "RASMDPAGE_Summary": 1,
    "RASMDPAGE_Preferences": 2,
}
_RASMDPAGE__INV = {
    0: "RASMDPAGE_Status",
    1: "RASMDPAGE_Summary",
    2: "RASMDPAGE_Preferences",
}

###################

###### Types ######
RASPBDLGFUNC = LPVOID
_RASDDFLAG_ = DWORD

class RASENTRYDLG(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("hwndOwner", HWND()),
        ("dwFlags", _RASDDFLAG_()),
        ("xDlg", LONG()),
        ("yDlg", LONG()),
        ("szEntry", TCHAR__RAS_MaxEntryName_+_1_()),
        ("dwError", DWORD()),
        ("reserved", ULONG_PTR()),
        ("reserved2", ULONG_PTR()),
    ]

LPRASENTRYDLG = Ptr("<I", RASENTRYDLG())
_RASMDFLAG_ = DWORD
_RASMDPAGE_ = DWORD

class RASMONITORDLG(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("hwndOwner", HWND()),
        ("dwFlags", _RASMDFLAG_()),
        ("dwStartPage", _RASMDPAGE_()),
        ("xDlg", LONG()),
        ("yDlg", LONG()),
        ("dwError", DWORD()),
        ("reserved", ULONG_PTR()),
        ("reserved2", ULONG_PTR()),
    ]

LPRASMONITORDLG = Ptr("<I", RASMONITORDLG())

class RASDIALDLG(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("hwndOwner", HWND()),
        ("dwFlags", DWORD()),
        ("xDlg", LONG()),
        ("yDlg", LONG()),
        ("dwSubEntry", DWORD()),
        ("dwError", DWORD()),
        ("reserved", ULONG_PTR()),
        ("reserved2", ULONG_PTR()),
    ]

LPRASDIALDLG = Ptr("<I", RASDIALDLG())

class RASPBDLG(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("hwndOwner", HWND()),
        ("dwFlags", DWORD()),
        ("xDlg", LONG()),
        ("yDlg", LONG()),
        ("dwCallbackId", ULONG_PTR()),
        ("pCallback", RASPBDLGFUNC()),
        ("dwError", DWORD()),
        ("reserved", ULONG_PTR()),
        ("reserved2", ULONG_PTR()),
    ]

LPRASPBDLG = Ptr("<I", RASPBDLG())

###################

###### Functions ######

def rasdlg_RasDialDlg(jitter, get_str, set_str):
    """
    BOOL RasDialDlg(
        LPTSTR lpszPhonebook,
        LPTSTR lpszEntry,
        LPTSTR lpszPhoneNumber,
        LPRASDIALDLG lpInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpszPhoneNumber", "lpInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasdlg_RasDialDlgA(jitter):
    rasdlg_RasDialDlg(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasdlg_RasDialDlgW(jitter):
    rasdlg_RasDialDlg(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasdlg_RasEntryDlg(jitter, get_str, set_str):
    """
    BOOL RasEntryDlg(
        LPTSTR lpszPhonebook,
        LPTSTR lpszEntry,
        LPRASENTRYDLG lpInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasdlg_RasEntryDlgA(jitter):
    rasdlg_RasEntryDlg(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasdlg_RasEntryDlgW(jitter):
    rasdlg_RasEntryDlg(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasdlg_RasMonitorDlg(jitter, get_str, set_str):
    """
    BOOL RasMonitorDlg(
        LPTSTR lpszDeviceName,
        LPRASMONITORDLG lpInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDeviceName", "lpInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasdlg_RasMonitorDlgA(jitter):
    rasdlg_RasMonitorDlg(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasdlg_RasMonitorDlgW(jitter):
    rasdlg_RasMonitorDlg(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rasdlg_RasPhonebookDlg(jitter, get_str, set_str):
    """
    BOOL RasPhonebookDlg(
        LPTSTR lpszPhonebook,
        LPTSTR lpszEntry,
        LPRASPBDLG lpInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasdlg_RasPhonebookDlgA(jitter):
    rasdlg_RasPhonebookDlg(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rasdlg_RasPhonebookDlgW(jitter):
    rasdlg_RasPhonebookDlg(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
