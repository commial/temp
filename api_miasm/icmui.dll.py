###### Enums ######

###################

###### Types ######
PCMSCALLBACK = LPVOID
_CMS_FLAGS_ = DWORD

class COLORMATCHSETUP(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("dwVersion", DWORD()),
        ("dwFlags", _CMS_FLAGS_()),
        ("hwndOwner", HWND()),
        ("pSourceName", PCTSTR()),
        ("pDisplayName", PCTSTR()),
        ("pPrinterName", PCTSTR()),
        ("dwRenderIntent", DWORD()),
        ("dwProofingIntent", DWORD()),
        ("pMonitorProfile", PTSTR()),
        ("ccMonitorProfile", DWORD()),
        ("pPrinterProfile", PTSTR()),
        ("ccPrinterProfile", DWORD()),
        ("pTargetProfile", PTSTR()),
        ("ccTargetProfile", DWORD()),
        ("lpfnHook", DLGPROC()),
        ("lParam", LPARAM()),
        ("lpfnApplyCallback", PCMSCALLBACK()),
        ("lParamApplyCallback", LPARAM()),
    ]

PCOLORMATCHSETUP = Ptr("<I", COLORMATCHSETUP())

###################

###### Functions ######

def icmui_SetupColorMatching(jitter, get_str, set_str):
    """
    BOOL SetupColorMatching(
        PCOLORMATCHSETUP pcms
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcms"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icmui_SetupColorMatchingA(jitter):
    icmui_SetupColorMatching(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def icmui_SetupColorMatchingW(jitter):
    icmui_SetupColorMatching(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
