SHREGENUM_FLAGS = {
    "SHREGENUM_DEFAULT": 0x00000000,
    "SHREGENUM_HKCU": 0x00000001,
    "SHREGENUM_HKLM": 0x00000010,
    "SHREGENUM_BOTH": 0x00000011,
}
SHREGENUM_FLAGS_INV = {
    0x00000000: "SHREGENUM_DEFAULT",
    0x00000001: "SHREGENUM_HKCU",
    0x00000010: "SHREGENUM_HKLM",
    0x00000011: "SHREGENUM_BOTH",
}
SHREGDEL_FLAGS = {
    "SHREGDEL_DEFAULT": 0x00000000,
    "SHREGDEL_HKCU": 0x00000001,
    "SHREGDEL_HKLM": 0x00000010,
    "SHREGDEL_BOTH": 0x00000011,
}
SHREGDEL_FLAGS_INV = {
    0x00000000: "SHREGDEL_DEFAULT",
    0x00000001: "SHREGDEL_HKCU",
    0x00000010: "SHREGDEL_HKLM",
    0x00000011: "SHREGDEL_BOTH",
}
URLIS = {
    "URLIS_URL": 0,
    "URLIS_OPAQUE": 1,
    "URLIS_NOHISTORY": 2,
    "URLIS_FILEURL": 3,
    "URLIS_APPLIABLE": 4,
    "URLIS_DIRECTORY": 5,
    "URLIS_HASQUERY": 6,
}
URLIS_INV = {
    0: "URLIS_URL",
    1: "URLIS_OPAQUE",
    2: "URLIS_NOHISTORY",
    3: "URLIS_FILEURL",
    4: "URLIS_APPLIABLE",
    5: "URLIS_DIRECTORY",
    6: "URLIS_HASQUERY",
}
SHGLOBALCOUNTER = {
    "GLOBALCOUNTER_SEARCHMANAGER": 0,
    "GLOBALCOUNTER_SEARCHOPTIONS": 1,
    "GLOBALCOUNTER_FOLDERSETTINGSCHANGE": 2,
    "GLOBALCOUNTER_RATINGS": 3,
    "GLOBALCOUNTER_APPROVEDSITES": 4,
    "GLOBALCOUNTER_RESTRICTIONS": 5,
    "GLOBALCOUNTER_SHELLSETTINGSCHANGED": 6,
    "GLOBALCOUNTER_SYSTEMPIDLCHANGE": 7,
    "GLOBALCOUNTER_OVERLAYMANAGER": 8,
    "GLOBALCOUNTER_QUERYASSOCIATIONS": 9,
    "GLOBALCOUNTER_IESESSIONS": 10,
    "GLOBALCOUNTER_IEONLY_SESSIONS": 11,
    "GLOBALCOUNTER_APPLICATION_DESTINATIONS": 12,
    "GLOBALCOUNTER_CSCSYNCINPROGRESS": 13,
    "GLOBALCOUNTER_BITBUCKETNUMDELETERS": 14,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_SHARES": 15,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_A": 16,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_B": 17,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_C": 18,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_D": 19,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_E": 20,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_F": 21,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_G": 22,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_H": 23,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_I": 24,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_J": 25,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_K": 26,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_L": 27,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_M": 28,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_N": 29,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_O": 30,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_P": 31,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Q": 32,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_R": 33,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_S": 34,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_T": 35,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_U": 36,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_V": 37,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_W": 38,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_X": 39,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Y": 40,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Z": 41,
    "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_SERVERDRIVE": 42,
    "GLOBALCOUNTER_RECYCLEGLOBALDIRTYCOUNT": 43,
    "GLOBALCOUNTER_RECYCLEBINENUM": 44,
    "GLOBALCOUNTER_RECYCLEBINCORRUPTED": 45,
    "GLOBALCOUNTER_RATINGS_STATECOUNTER": 46,
    "GLOBALCOUNTER_PRIVATE_PROFILE_CACHE": 47,
    "GLOBALCOUNTER_INTERNETTOOLBAR_LAYOUT": 48,
    "GLOBALCOUNTER_FOLDERDEFINITION_CACHE": 49,
    "GLOBALCOUNTER_COMMONPLACES_LIST_CACHE": 50,
    "GLOBALCOUNTER_PRIVATE_PROFILE_CACHE_MACHINEWIDE": 51,
    "GLOBALCOUNTER_ASSOCCHANGED": 52,
    "GLOBALCOUNTER_APP_ITEMS_STATE_STORE_CACHE": 53,
    "GLOBALCOUNTER_SETTINGSYNC_ENABLED": 54,
    "GLOBALCOUNTER_APPSFOLDER_FILETYPEASSOCIATION_COUNTER": 55,
    "GLOBALCOUNTER_USERINFOCHANGED": 56,
}
SHGLOBALCOUNTER_INV = {
    0: "GLOBALCOUNTER_SEARCHMANAGER",
    1: "GLOBALCOUNTER_SEARCHOPTIONS",
    2: "GLOBALCOUNTER_FOLDERSETTINGSCHANGE",
    3: "GLOBALCOUNTER_RATINGS",
    4: "GLOBALCOUNTER_APPROVEDSITES",
    5: "GLOBALCOUNTER_RESTRICTIONS",
    6: "GLOBALCOUNTER_SHELLSETTINGSCHANGED",
    7: "GLOBALCOUNTER_SYSTEMPIDLCHANGE",
    8: "GLOBALCOUNTER_OVERLAYMANAGER",
    9: "GLOBALCOUNTER_QUERYASSOCIATIONS",
    10: "GLOBALCOUNTER_IESESSIONS",
    11: "GLOBALCOUNTER_IEONLY_SESSIONS",
    12: "GLOBALCOUNTER_APPLICATION_DESTINATIONS",
    13: "GLOBALCOUNTER_CSCSYNCINPROGRESS",
    14: "GLOBALCOUNTER_BITBUCKETNUMDELETERS",
    15: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_SHARES",
    16: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_A",
    17: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_B",
    18: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_C",
    19: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_D",
    20: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_E",
    21: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_F",
    22: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_G",
    23: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_H",
    24: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_I",
    25: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_J",
    26: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_K",
    27: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_L",
    28: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_M",
    29: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_N",
    30: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_O",
    31: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_P",
    32: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Q",
    33: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_R",
    34: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_S",
    35: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_T",
    36: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_U",
    37: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_V",
    38: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_W",
    39: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_X",
    40: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Y",
    41: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Z",
    42: "GLOBALCOUNTER_RECYCLEDIRTYCOUNT_SERVERDRIVE",
    43: "GLOBALCOUNTER_RECYCLEGLOBALDIRTYCOUNT",
    44: "GLOBALCOUNTER_RECYCLEBINENUM",
    45: "GLOBALCOUNTER_RECYCLEBINCORRUPTED",
    46: "GLOBALCOUNTER_RATINGS_STATECOUNTER",
    47: "GLOBALCOUNTER_PRIVATE_PROFILE_CACHE",
    48: "GLOBALCOUNTER_INTERNETTOOLBAR_LAYOUT",
    49: "GLOBALCOUNTER_FOLDERDEFINITION_CACHE",
    50: "GLOBALCOUNTER_COMMONPLACES_LIST_CACHE",
    51: "GLOBALCOUNTER_PRIVATE_PROFILE_CACHE_MACHINEWIDE",
    52: "GLOBALCOUNTER_ASSOCCHANGED",
    53: "GLOBALCOUNTER_APP_ITEMS_STATE_STORE_CACHE",
    54: "GLOBALCOUNTER_SETTINGSYNC_ENABLED",
    55: "GLOBALCOUNTER_APPSFOLDER_FILETYPEASSOCIATION_COUNTER",
    56: "GLOBALCOUNTER_USERINFOCHANGED",
}

def shlwapi_SHAllocShared(jitter):
    """
    HANDLE SHAllocShared(
        const void* pvData,
        DWORD dwSize,
        DWORD dwDestinationProcessId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvData", "dwSize", "dwDestinationProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ShellMessageBox(jitter, get_str, set_str):
    """
    [MessageBoxResult] ShellMessageBox(
        HINSTANCE hInst,
        HWND hWnd,
        LPCTSTR pszMsg,
        LPCTSTR pszTitle,
        [MessageBoxType] fuStyle,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInst", "hWnd", "pszMsg", "pszTitle", "fuStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ShellMessageBoxA(jitter):
    shlwapi_ShellMessageBox(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_ShellMessageBoxW(jitter):
    shlwapi_ShellMessageBox(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHGetViewStatePropertyBag(jitter):
    """
    HRESULT SHGetViewStatePropertyBag(
        PCIDLIST_ABSOLUTE pidl,
        LPCWSTR pszBagName,
        DWORD dwFlags,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "pszBagName", "dwFlags", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHLockShared(jitter):
    """
    LPVOID SHLockShared(
        HANDLE* hData,
        DWORD dwOtherProcId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hData", "dwOtherProcId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHUnlockShared(jitter):
    """
    BOOL SHUnlockShared(
        void* pvData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHFreeShared(jitter):
    """
    BOOL SHFreeShared(
        HANDLE hData,
        DWORD dwSourceProcId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hData", "dwSourceProcId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrStrNW(jitter):
    """
    LPCWSTR StrStrNW(
        LPCWSTR lpFirst,
        LPCWSTR lpSrch,
        UINT cchMax
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpFirst", "lpSrch", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrStrNIW(jitter):
    """
    LPCWSTR StrStrNIW(
        LPCWSTR lpFirst,
        LPCWSTR lpSrch,
        UINT cchMax
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpFirst", "lpSrch", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ColorAdjustLuma(jitter):
    """
    COLORREF ColorAdjustLuma(
        COLORREF clrRGB,
        int n,
        BOOL fScale
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clrRGB", "n", "fScale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ColorHLSToRGB(jitter):
    """
    COLORREF ColorHLSToRGB(
        WORD wHue,
        WORD wLuminance,
        WORD wSaturation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wHue", "wLuminance", "wSaturation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ColorRGBToHLS(jitter):
    """
    void ColorRGBToHLS(
        COLORREF clrRGB,
        WORD* pwHue,
        WORD* pwLuminance,
        WORD* pwSaturation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clrRGB", "pwHue", "pwLuminance", "pwSaturation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateShellPalette(jitter):
    """
    HPALETTE SHCreateShellPalette(
        HDC hdc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGetInverseCMAP(jitter):
    """
    HRESULT SHGetInverseCMAP(
        BYTE* pbMap,
        ULONG cbMap
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbMap", "cbMap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathAddBackslash(jitter, get_str, set_str):
    """
    LPTSTR PathAddBackslash(
        LPTSTR lpszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathAddBackslashA(jitter):
    shlwapi_PathAddBackslash(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathAddBackslashW(jitter):
    shlwapi_PathAddBackslash(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathAddExtension(jitter, get_str, set_str):
    """
    BOOL PathAddExtension(
        LPTSTR pszPath,
        LPCTSTR pszExtension
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszExtension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathAddExtensionA(jitter):
    shlwapi_PathAddExtension(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathAddExtensionW(jitter):
    shlwapi_PathAddExtension(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathAppend(jitter, get_str, set_str):
    """
    BOOL PathAppend(
        LPTSTR pszPath,
        LPCTSTR pszMore
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszMore"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathAppendA(jitter):
    shlwapi_PathAppend(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathAppendW(jitter):
    shlwapi_PathAppend(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathBuildRoot(jitter, get_str, set_str):
    """
    LPTSTR PathBuildRoot(
        LPTSTR szRoot,
        int iDrive
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szRoot", "iDrive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathBuildRootA(jitter):
    shlwapi_PathBuildRoot(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathBuildRootW(jitter):
    shlwapi_PathBuildRoot(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathCanonicalize(jitter, get_str, set_str):
    """
    BOOL PathCanonicalize(
        LPTSTR lpszDst,
        LPCTSTR lpszSrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDst", "lpszSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathCanonicalizeA(jitter):
    shlwapi_PathCanonicalize(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathCanonicalizeW(jitter):
    shlwapi_PathCanonicalize(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathCombine(jitter, get_str, set_str):
    """
    LPTSTR PathCombine(
        LPTSTR lpszDest,
        LPCTSTR lpszDir,
        LPCTSTR lpszFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDest", "lpszDir", "lpszFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathCombineA(jitter):
    shlwapi_PathCombine(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathCombineW(jitter):
    shlwapi_PathCombine(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathCommonPrefix(jitter, get_str, set_str):
    """
    int PathCommonPrefix(
        LPCTSTR pszFile1,
        LPCTSTR pszFile2,
        LPTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFile1", "pszFile2", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathCommonPrefixA(jitter):
    shlwapi_PathCommonPrefix(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathCommonPrefixW(jitter):
    shlwapi_PathCommonPrefix(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathCompactPath(jitter, get_str, set_str):
    """
    BOOL PathCompactPath(
        HDC hDC,
        LPTSTR lpszPath,
        UINT dx
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lpszPath", "dx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathCompactPathA(jitter):
    shlwapi_PathCompactPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathCompactPathW(jitter):
    shlwapi_PathCompactPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathCompactPathEx(jitter, get_str, set_str):
    """
    BOOL PathCompactPathEx(
        LPTSTR pszOut,
        LPCTSTR pszSrc,
        UINT cchMax,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszOut", "pszSrc", "cchMax", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathCompactPathExA(jitter):
    shlwapi_PathCompactPathEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathCompactPathExW(jitter):
    shlwapi_PathCompactPathEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathCreateFromUrl(jitter, get_str, set_str):
    """
    HRESULT PathCreateFromUrl(
        PCTSTR pszUrl,
        PTSTR pszPath,
        DWORD* pcchPath,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUrl", "pszPath", "pcchPath", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathCreateFromUrlA(jitter):
    shlwapi_PathCreateFromUrl(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathCreateFromUrlW(jitter):
    shlwapi_PathCreateFromUrl(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathCreateFromUrlAlloc(jitter):
    """
    HRESULT PathCreateFromUrlAlloc(
        PCWSTR pszIn,
        PWSTR* ppszOut,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszIn", "ppszOut", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathFileExists(jitter, get_str, set_str):
    """
    BOOL PathFileExists(
        LPCTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathFileExistsA(jitter):
    shlwapi_PathFileExists(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathFileExistsW(jitter):
    shlwapi_PathFileExists(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathFindExtension(jitter, get_str, set_str):
    """
    PTSTR PathFindExtension(
        PTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathFindExtensionA(jitter):
    shlwapi_PathFindExtension(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathFindExtensionW(jitter):
    shlwapi_PathFindExtension(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathFindFileName(jitter, get_str, set_str):
    """
    PTSTR PathFindFileName(
        PTSTR pPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathFindFileNameA(jitter):
    shlwapi_PathFindFileName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathFindFileNameW(jitter):
    shlwapi_PathFindFileName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathFindNextComponent(jitter, get_str, set_str):
    """
    PTSTR PathFindNextComponent(
        PTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathFindNextComponentA(jitter):
    shlwapi_PathFindNextComponent(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathFindNextComponentW(jitter):
    shlwapi_PathFindNextComponent(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathFindOnPath(jitter, get_str, set_str):
    """
    BOOL PathFindOnPath(
        LPTSTR pszFile,
        LPCTSTR* ppszOtherDirs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFile", "ppszOtherDirs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathFindOnPathA(jitter):
    shlwapi_PathFindOnPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathFindOnPathW(jitter):
    shlwapi_PathFindOnPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathFindSuffixArray(jitter, get_str, set_str):
    """
    LPCTSTR PathFindSuffixArray(
        LPCTSTR pszPath,
        const LPCTSTR* apszSuffix,
        int iArraySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "apszSuffix", "iArraySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathFindSuffixArrayA(jitter):
    shlwapi_PathFindSuffixArray(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathFindSuffixArrayW(jitter):
    shlwapi_PathFindSuffixArray(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathGetArgs(jitter, get_str, set_str):
    """
    PTSTR PathGetArgs(
        PTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathGetArgsA(jitter):
    shlwapi_PathGetArgs(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathGetArgsW(jitter):
    shlwapi_PathGetArgs(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathGetCharType(jitter, get_str, set_str):
    """
    UINT PathGetCharType(
        TCHAR ch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathGetCharTypeA(jitter):
    shlwapi_PathGetCharType(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathGetCharTypeW(jitter):
    shlwapi_PathGetCharType(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathGetDriveNumber(jitter, get_str, set_str):
    """
    int PathGetDriveNumber(
        LPCTSTR lpsz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathGetDriveNumberA(jitter):
    shlwapi_PathGetDriveNumber(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathGetDriveNumberW(jitter):
    shlwapi_PathGetDriveNumber(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsContentType(jitter, get_str, set_str):
    """
    BOOL PathIsContentType(
        LPCTSTR pszPath,
        LPCTSTR pszContentType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszContentType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsContentTypeA(jitter):
    shlwapi_PathIsContentType(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsContentTypeW(jitter):
    shlwapi_PathIsContentType(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsDirectory(jitter, get_str, set_str):
    """
    BOOL PathIsDirectory(
        LPCTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsDirectoryA(jitter):
    shlwapi_PathIsDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsDirectoryW(jitter):
    shlwapi_PathIsDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsDirectoryEmpty(jitter, get_str, set_str):
    """
    BOOL PathIsDirectoryEmpty(
        LPCTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsDirectoryEmptyA(jitter):
    shlwapi_PathIsDirectoryEmpty(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsDirectoryEmptyW(jitter):
    shlwapi_PathIsDirectoryEmpty(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsFileSpec(jitter, get_str, set_str):
    """
    BOOL PathIsFileSpec(
        LPCTSTR lpszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsFileSpecA(jitter):
    shlwapi_PathIsFileSpec(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsFileSpecW(jitter):
    shlwapi_PathIsFileSpec(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsHTMLFile(jitter, get_str, set_str):
    """
    BOOL PathIsHTMLFile(
        LPCTSTR pszFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsHTMLFileA(jitter):
    shlwapi_PathIsHTMLFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsHTMLFileW(jitter):
    shlwapi_PathIsHTMLFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsLFNFileSpec(jitter, get_str, set_str):
    """
    BOOL PathIsLFNFileSpec(
        LPCTSTR pszName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsLFNFileSpecA(jitter):
    shlwapi_PathIsLFNFileSpec(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsLFNFileSpecW(jitter):
    shlwapi_PathIsLFNFileSpec(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsNetworkPath(jitter, get_str, set_str):
    """
    BOOL PathIsNetworkPath(
        LPCTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsNetworkPathA(jitter):
    shlwapi_PathIsNetworkPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsNetworkPathW(jitter):
    shlwapi_PathIsNetworkPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsPrefix(jitter, get_str, set_str):
    """
    BOOL PathIsPrefix(
        LPCTSTR pszPrefix,
        LPCTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPrefix", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsPrefixA(jitter):
    shlwapi_PathIsPrefix(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsPrefixW(jitter):
    shlwapi_PathIsPrefix(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsRelative(jitter, get_str, set_str):
    """
    BOOL PathIsRelative(
        LPCTSTR lpszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsRelativeA(jitter):
    shlwapi_PathIsRelative(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsRelativeW(jitter):
    shlwapi_PathIsRelative(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsRoot(jitter, get_str, set_str):
    """
    BOOL PathIsRoot(
        LPCTSTR pPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsRootA(jitter):
    shlwapi_PathIsRoot(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsRootW(jitter):
    shlwapi_PathIsRoot(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsSameRoot(jitter, get_str, set_str):
    """
    BOOL PathIsSameRoot(
        LPCTSTR pszPath1,
        LPCTSTR pszPath2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath1", "pszPath2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsSameRootA(jitter):
    shlwapi_PathIsSameRoot(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsSameRootW(jitter):
    shlwapi_PathIsSameRoot(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsSystemFolder(jitter, get_str, set_str):
    """
    BOOL PathIsSystemFolder(
        LPCTSTR pszPath,
        DWORD dwAttrb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "dwAttrb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsSystemFolderA(jitter):
    shlwapi_PathIsSystemFolder(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsSystemFolderW(jitter):
    shlwapi_PathIsSystemFolder(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsUNC(jitter, get_str, set_str):
    """
    BOOL PathIsUNC(
        LPCTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsUNCA(jitter):
    shlwapi_PathIsUNC(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsUNCW(jitter):
    shlwapi_PathIsUNC(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsUNCServer(jitter, get_str, set_str):
    """
    BOOL PathIsUNCServer(
        LPCTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsUNCServerA(jitter):
    shlwapi_PathIsUNCServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsUNCServerW(jitter):
    shlwapi_PathIsUNCServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsUNCServerShare(jitter, get_str, set_str):
    """
    BOOL PathIsUNCServerShare(
        LPCTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsUNCServerShareA(jitter):
    shlwapi_PathIsUNCServerShare(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsUNCServerShareW(jitter):
    shlwapi_PathIsUNCServerShare(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathIsURL(jitter, get_str, set_str):
    """
    BOOL PathIsURL(
        LPCTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsURLA(jitter):
    shlwapi_PathIsURL(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathIsURLW(jitter):
    shlwapi_PathIsURL(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathMakePretty(jitter, get_str, set_str):
    """
    BOOL PathMakePretty(
        LPTSTR lpPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathMakePrettyA(jitter):
    shlwapi_PathMakePretty(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathMakePrettyW(jitter):
    shlwapi_PathMakePretty(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathMakeSystemFolder(jitter, get_str, set_str):
    """
    BOOL PathMakeSystemFolder(
        LPTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathMakeSystemFolderA(jitter):
    shlwapi_PathMakeSystemFolder(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathMakeSystemFolderW(jitter):
    shlwapi_PathMakeSystemFolder(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathMatchSpec(jitter, get_str, set_str):
    """
    BOOL PathMatchSpec(
        LPCSTR pszFile,
        LPCSTR pszSpec
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFile", "pszSpec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathMatchSpecA(jitter):
    shlwapi_PathMatchSpec(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathMatchSpecW(jitter):
    shlwapi_PathMatchSpec(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathMatchSpecEx(jitter, get_str, set_str):
    """
    HRESULT PathMatchSpecEx(
        LPCTSTR pszFile,
        LPCTSTR pszSpec,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFile", "pszSpec", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathMatchSpecExA(jitter):
    shlwapi_PathMatchSpecEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathMatchSpecExW(jitter):
    shlwapi_PathMatchSpecEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathParseIconLocation(jitter, get_str, set_str):
    """
    int PathParseIconLocation(
        LPTSTR pszIconFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszIconFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathParseIconLocationA(jitter):
    shlwapi_PathParseIconLocation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathParseIconLocationW(jitter):
    shlwapi_PathParseIconLocation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathQuoteSpaces(jitter, get_str, set_str):
    """
    BOOL PathQuoteSpaces(
        LPTSTR lpsz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathQuoteSpacesA(jitter):
    shlwapi_PathQuoteSpaces(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathQuoteSpacesW(jitter):
    shlwapi_PathQuoteSpaces(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathRelativePathTo(jitter, get_str, set_str):
    """
    BOOL PathRelativePathTo(
        LPTSTR pszPath,
        LPCTSTR pszFrom,
        DWORD dwAttrFrom,
        LPCTSTR pszTo,
        DWORD dwAttrTo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszFrom", "dwAttrFrom", "pszTo", "dwAttrTo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRelativePathToA(jitter):
    shlwapi_PathRelativePathTo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathRelativePathToW(jitter):
    shlwapi_PathRelativePathTo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathRemoveArgs(jitter, get_str, set_str):
    """
    void PathRemoveArgs(
        LPTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRemoveArgsA(jitter):
    shlwapi_PathRemoveArgs(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathRemoveArgsW(jitter):
    shlwapi_PathRemoveArgs(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathRemoveBackslash(jitter, get_str, set_str):
    """
    LPTSTR PathRemoveBackslash(
        LPTSTR lpszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRemoveBackslashA(jitter):
    shlwapi_PathRemoveBackslash(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathRemoveBackslashW(jitter):
    shlwapi_PathRemoveBackslash(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathRemoveBlanks(jitter, get_str, set_str):
    """
    void PathRemoveBlanks(
        LPTSTR lpszString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRemoveBlanksA(jitter):
    shlwapi_PathRemoveBlanks(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathRemoveBlanksW(jitter):
    shlwapi_PathRemoveBlanks(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathRemoveExtension(jitter, get_str, set_str):
    """
    void PathRemoveExtension(
        LPTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRemoveExtensionA(jitter):
    shlwapi_PathRemoveExtension(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathRemoveExtensionW(jitter):
    shlwapi_PathRemoveExtension(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathRemoveFileSpec(jitter, get_str, set_str):
    """
    BOOL PathRemoveFileSpec(
        LPTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRemoveFileSpecA(jitter):
    shlwapi_PathRemoveFileSpec(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathRemoveFileSpecW(jitter):
    shlwapi_PathRemoveFileSpec(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathRenameExtension(jitter, get_str, set_str):
    """
    BOOL PathRenameExtension(
        LPTSTR pszPath,
        LPCTSTR pszExt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszExt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRenameExtensionA(jitter):
    shlwapi_PathRenameExtension(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathRenameExtensionW(jitter):
    shlwapi_PathRenameExtension(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathSearchAndQualify(jitter, get_str, set_str):
    """
    BOOL PathSearchAndQualify(
        LPCTSTR pcszPath,
        LPTSTR pszFullyQualifiedPath,
        UINT cchFullyQualifiedPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcszPath", "pszFullyQualifiedPath", "cchFullyQualifiedPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathSearchAndQualifyA(jitter):
    shlwapi_PathSearchAndQualify(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathSearchAndQualifyW(jitter):
    shlwapi_PathSearchAndQualify(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathSetDlgItemPath(jitter, get_str, set_str):
    """
    void PathSetDlgItemPath(
        HWND hDlg,
        int id,
        LPCSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "id", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathSetDlgItemPathA(jitter):
    shlwapi_PathSetDlgItemPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathSetDlgItemPathW(jitter):
    shlwapi_PathSetDlgItemPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathSkipRoot(jitter, get_str, set_str):
    """
    PTSTR PathSkipRoot(
        PTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathSkipRootA(jitter):
    shlwapi_PathSkipRoot(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathSkipRootW(jitter):
    shlwapi_PathSkipRoot(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathStripPath(jitter, get_str, set_str):
    """
    void PathStripPath(
        LPTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathStripPathA(jitter):
    shlwapi_PathStripPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathStripPathW(jitter):
    shlwapi_PathStripPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathStripToRoot(jitter, get_str, set_str):
    """
    BOOL PathStripToRoot(
        LPTSTR szRoot
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szRoot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathStripToRootA(jitter):
    shlwapi_PathStripToRoot(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathStripToRootW(jitter):
    shlwapi_PathStripToRoot(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathUndecorate(jitter, get_str, set_str):
    """
    void PathUndecorate(
        LPTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathUndecorateA(jitter):
    shlwapi_PathUndecorate(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathUndecorateW(jitter):
    shlwapi_PathUndecorate(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathUnExpandEnvStrings(jitter, get_str, set_str):
    """
    BOOL PathUnExpandEnvStrings(
        LPCTSTR pszPath,
        LPTSTR pszBuf,
        UINT cchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathUnExpandEnvStringsA(jitter):
    shlwapi_PathUnExpandEnvStrings(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathUnExpandEnvStringsW(jitter):
    shlwapi_PathUnExpandEnvStrings(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathUnmakeSystemFolder(jitter, get_str, set_str):
    """
    BOOL PathUnmakeSystemFolder(
        LPTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathUnmakeSystemFolderA(jitter):
    shlwapi_PathUnmakeSystemFolder(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathUnmakeSystemFolderW(jitter):
    shlwapi_PathUnmakeSystemFolder(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_PathUnquoteSpaces(jitter, get_str, set_str):
    """
    void PathUnquoteSpaces(
        LPTSTR lpsz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathUnquoteSpacesA(jitter):
    shlwapi_PathUnquoteSpaces(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_PathUnquoteSpacesW(jitter):
    shlwapi_PathUnquoteSpaces(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHSkipJunction(jitter):
    """
    BOOL SHSkipJunction(
        IBindCtx* pbc,
        const CLSID* pclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbc", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlApplyScheme(jitter, get_str, set_str):
    """
    HRESULT UrlApplyScheme(
        PCTSTR pszIn,
        PTSTR pszOut,
        DWORD* pcchOut,
        [URL_APPLY_FLAGS] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszIn", "pszOut", "pcchOut", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlApplySchemeA(jitter):
    shlwapi_UrlApplyScheme(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlApplySchemeW(jitter):
    shlwapi_UrlApplyScheme(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlCanonicalize(jitter, get_str, set_str):
    """
    HRESULT UrlCanonicalize(
        PCTSTR pszUrl,
        PTSTR pszCanonicalized,
        DWORD* pcchCanonicalized,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUrl", "pszCanonicalized", "pcchCanonicalized", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlCanonicalizeA(jitter):
    shlwapi_UrlCanonicalize(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlCanonicalizeW(jitter):
    shlwapi_UrlCanonicalize(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlCombine(jitter, get_str, set_str):
    """
    HRESULT UrlCombine(
        PCTSTR pszBase,
        PCTSTR pszRelative,
        PTSTR pszCombined,
        DWORD* pcchCombined,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszBase", "pszRelative", "pszCombined", "pcchCombined", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlCombineA(jitter):
    shlwapi_UrlCombine(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlCombineW(jitter):
    shlwapi_UrlCombine(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlCompare(jitter, get_str, set_str):
    """
    int UrlCompare(
        PCTSTR psz1,
        PCTSTR psz2,
        BOOL fIgnoreSlash
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2", "fIgnoreSlash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlCompareA(jitter):
    shlwapi_UrlCompare(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlCompareW(jitter):
    shlwapi_UrlCompare(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlCreateFromPath(jitter, get_str, set_str):
    """
    HRESULT UrlCreateFromPath(
        PCTSTR pszPath,
        PTSTR pszUrl,
        DWORD* pcchUrl,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszUrl", "pcchUrl", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlCreateFromPathA(jitter):
    shlwapi_UrlCreateFromPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlCreateFromPathW(jitter):
    shlwapi_UrlCreateFromPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlEscape(jitter, get_str, set_str):
    """
    HRESULT UrlEscape(
        PCTSTR pszURL,
        PTSTR pszEscaped,
        DWORD* pcchEscaped,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszURL", "pszEscaped", "pcchEscaped", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlEscapeA(jitter):
    shlwapi_UrlEscape(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlEscapeW(jitter):
    shlwapi_UrlEscape(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlEscapeSpaces(jitter):
    """
    HRESULT UrlEscapeSpaces(
        LPCTSTR pszURL,
        LPTSTR pszEscaped,
        LPDWORD pcchEscaped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszURL", "pszEscaped", "pcchEscaped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlFixupW(jitter):
    """
    HRESULT UrlFixupW(
        PCWSTR pcszUrl,
        PWSTR pszTranslatedUrl,
        DWORD cchMax
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcszUrl", "pszTranslatedUrl", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlGetLocation(jitter, get_str, set_str):
    """
    LPCTSTR UrlGetLocation(
        PCTSTR pszURL
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszURL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlGetLocationA(jitter):
    shlwapi_UrlGetLocation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlGetLocationW(jitter):
    shlwapi_UrlGetLocation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlGetPart(jitter, get_str, set_str):
    """
    HRESULT UrlGetPart(
        PCTSTR pszIn,
        PTSTR pszOut,
        DWORD* pcchOut,
        DWORD dwPart,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszIn", "pszOut", "pcchOut", "dwPart", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlGetPartA(jitter):
    shlwapi_UrlGetPart(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlGetPartW(jitter):
    shlwapi_UrlGetPart(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlHash(jitter, get_str, set_str):
    """
    HRESULT UrlHash(
        PCTSTR pszURL,
        BYTE* pbHash,
        DWORD cbHash
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszURL", "pbHash", "cbHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlHashA(jitter):
    shlwapi_UrlHash(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlHashW(jitter):
    shlwapi_UrlHash(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlIs(jitter, get_str, set_str):
    """
    BOOL UrlIs(
        PCTSTR pszUrl,
        URLIS UrlIs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUrl", "UrlIs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlIsA(jitter):
    shlwapi_UrlIs(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlIsW(jitter):
    shlwapi_UrlIs(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlIsFileUrl(jitter, get_str, set_str):
    """
    BOOL UrlIsFileUrl(
        LPCTSTR pszUrl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUrl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlIsFileUrlA(jitter):
    shlwapi_UrlIsFileUrl(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlIsFileUrlW(jitter):
    shlwapi_UrlIsFileUrl(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlIsNoHistory(jitter, get_str, set_str):
    """
    BOOL UrlIsNoHistory(
        PCTSTR pszURL
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszURL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlIsNoHistoryA(jitter):
    shlwapi_UrlIsNoHistory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlIsNoHistoryW(jitter):
    shlwapi_UrlIsNoHistory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlIsOpaque(jitter, get_str, set_str):
    """
    BOOL UrlIsOpaque(
        PCTSTR pszURL
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszURL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlIsOpaqueA(jitter):
    shlwapi_UrlIsOpaque(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlIsOpaqueW(jitter):
    shlwapi_UrlIsOpaque(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlUnescape(jitter, get_str, set_str):
    """
    HRESULT UrlUnescape(
        PTSTR pszURL,
        PTSTR pszUnescaped,
        DWORD* pcchUnescaped,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszURL", "pszUnescaped", "pcchUnescaped", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlUnescapeA(jitter):
    shlwapi_UrlUnescape(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_UrlUnescapeW(jitter):
    shlwapi_UrlUnescape(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_UrlUnescapeInPlace(jitter):
    """
    HRESULT UrlUnescapeInPlace(
        LPTSTR pszURL,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszURL", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_AssocCreate(jitter):
    """
    HRESULT AssocCreate(
        CLSID clsid,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsid", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_AssocGetPerceivedType(jitter):
    """
    HRESULT AssocGetPerceivedType(
        PCWSTR pszExt,
        PERCEIVED* ptype,
        PERCEIVEDFLAG* pflag,
        PWSTR* ppszType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszExt", "ptype", "pflag", "ppszType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_AssocIsDangerous(jitter):
    """
    BOOL AssocIsDangerous(
        PCWSTR pszAssoc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszAssoc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_AssocQueryKey(jitter, get_str, set_str):
    """
    HRESULT AssocQueryKey(
        ASSOCF flags,
        ASSOCKEY key,
        LPCTSTR pszAssoc,
        LPCTSTR pszExtra,
        HKEY* phkeyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "key", "pszAssoc", "pszExtra", "phkeyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_AssocQueryKeyA(jitter):
    shlwapi_AssocQueryKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_AssocQueryKeyW(jitter):
    shlwapi_AssocQueryKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_AssocQueryString(jitter, get_str, set_str):
    """
    HRESULT AssocQueryString(
        ASSOCF flags,
        ASSOCSTR str,
        LPCTSTR pszAssoc,
        LPCTSTR pszExtra,
        LPTSTR pszOut,
        DWORD* pcchOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "str", "pszAssoc", "pszExtra", "pszOut", "pcchOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_AssocQueryStringA(jitter):
    shlwapi_AssocQueryString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_AssocQueryStringW(jitter):
    shlwapi_AssocQueryString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_AssocQueryStringByKey(jitter, get_str, set_str):
    """
    HRESULT AssocQueryStringByKey(
        ASSOCF flags,
        ASSOCSTR str,
        HKEY hkAssoc,
        LPCTSTR pszExtra,
        LPTSTR pszOut,
        DWORD* pcchOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "str", "hkAssoc", "pszExtra", "pszOut", "pcchOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_AssocQueryStringByKeyA(jitter):
    shlwapi_AssocQueryStringByKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_AssocQueryStringByKeyW(jitter):
    shlwapi_AssocQueryStringByKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHCopyKey(jitter, get_str, set_str):
    """
    LSTATUS SHCopyKey(
        HKEY hkeySrc,
        LPCTSTR pszSrcSubKey,
        HKEY hkeyDest,
        DWORD fReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkeySrc", "pszSrcSubKey", "hkeyDest", "fReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCopyKeyA(jitter):
    shlwapi_SHCopyKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHCopyKeyW(jitter):
    shlwapi_SHCopyKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHDeleteEmptyKey(jitter, get_str, set_str):
    """
    LSTATUS SHDeleteEmptyKey(
        HKEY hkey,
        LPCTSTR pszSubKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHDeleteEmptyKeyA(jitter):
    shlwapi_SHDeleteEmptyKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHDeleteEmptyKeyW(jitter):
    shlwapi_SHDeleteEmptyKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHDeleteKey(jitter, get_str, set_str):
    """
    LSTATUS SHDeleteKey(
        HKEY hkey,
        LPCTSTR pszSubKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHDeleteKeyA(jitter):
    shlwapi_SHDeleteKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHDeleteKeyW(jitter):
    shlwapi_SHDeleteKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHDeleteValue(jitter, get_str, set_str):
    """
    LSTATUS SHDeleteValue(
        HKEY hkey,
        LPCTSTR pszSubKey,
        LPCTSTR pszValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey", "pszValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHDeleteValueA(jitter):
    shlwapi_SHDeleteValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHDeleteValueW(jitter):
    shlwapi_SHDeleteValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHEnumKeyEx(jitter, get_str, set_str):
    """
    LSTATUS SHEnumKeyEx(
        HKEY hkey,
        DWORD dwIndex,
        LPTSTR pszName,
        LPDWORD pcchName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "dwIndex", "pszName", "pcchName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHEnumKeyExA(jitter):
    shlwapi_SHEnumKeyEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHEnumKeyExW(jitter):
    shlwapi_SHEnumKeyEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHEnumValue(jitter, get_str, set_str):
    """
    LSTATUS SHEnumValue(
        HKEY hkey,
        DWORD dwIndex,
        LPTSTR pszValueName,
        LPDWORD pcchValueName,
        [RegType*] pdwType,
        LPVOID pvData,
        LPDWORD pcbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "dwIndex", "pszValueName", "pcchValueName", "pdwType", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHEnumValueA(jitter):
    shlwapi_SHEnumValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHEnumValueW(jitter):
    shlwapi_SHEnumValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHGetValue(jitter, get_str, set_str):
    """
    LSTATUS SHGetValue(
        HKEY hkey,
        LPCTSTR pszSubKey,
        LPCTSTR pszValue,
        [RegType*] pdwType,
        LPVOID pvData,
        LPDWORD pcbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey", "pszValue", "pdwType", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGetValueA(jitter):
    shlwapi_SHGetValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHGetValueW(jitter):
    shlwapi_SHGetValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHOpenRegStream(jitter, get_str, set_str):
    """
    IStream* SHOpenRegStream(
        HKEY hkey,
        LPCTSTR pszSubkey,
        LPCTSTR pszValue,
        [STGM_FLAGS] grfMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubkey", "pszValue", "grfMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHOpenRegStreamA(jitter):
    shlwapi_SHOpenRegStream(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHOpenRegStreamW(jitter):
    shlwapi_SHOpenRegStream(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHOpenRegStream2(jitter, get_str, set_str):
    """
    IStream* SHOpenRegStream2(
        HKEY hkey,
        LPCTSTR pszSubkey,
        LPCTSTR pszValue,
        [STGM_FLAGS] grfMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubkey", "pszValue", "grfMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHOpenRegStream2A(jitter):
    shlwapi_SHOpenRegStream2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHOpenRegStream2W(jitter):
    shlwapi_SHOpenRegStream2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHQueryInfoKey(jitter, get_str, set_str):
    """
    LSTATUS SHQueryInfoKey(
        HKEY hkey,
        LPDWORD pcSubKeys,
        LPDWORD pcchMaxSubKeyLen,
        LPDWORD pcValues,
        LPDWORD pcchMaxValueNameLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pcSubKeys", "pcchMaxSubKeyLen", "pcValues", "pcchMaxValueNameLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHQueryInfoKeyA(jitter):
    shlwapi_SHQueryInfoKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHQueryInfoKeyW(jitter):
    shlwapi_SHQueryInfoKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHQueryValueEx(jitter, get_str, set_str):
    """
    [ERROR_CODE] SHQueryValueEx(
        HKEY hkey,
        LPCTSTR pszValue,
        LPDWORD pdwReserved,
        [RegType*] pdwType,
        LPVOID pvData,
        LPDWORD pcbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszValue", "pdwReserved", "pdwType", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHQueryValueExA(jitter):
    shlwapi_SHQueryValueEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHQueryValueExW(jitter):
    shlwapi_SHQueryValueEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegCloseUSKey(jitter):
    """
    LSTATUS SHRegCloseUSKey(
        HUSKEY hUSKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUSKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegCreateUSKey(jitter, get_str, set_str):
    """
    LSTATUS SHRegCreateUSKey(
        LPCTSTR pszPath,
        REGSAM samDesired,
        HUSKEY hRelativeUSKey,
        PHUSKEY phNewUSKey,
        [ShRegSetFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "samDesired", "hRelativeUSKey", "phNewUSKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegCreateUSKeyA(jitter):
    shlwapi_SHRegCreateUSKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegCreateUSKeyW(jitter):
    shlwapi_SHRegCreateUSKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegDeleteEmptyUSKey(jitter, get_str, set_str):
    """
    LSTATUS SHRegDeleteEmptyUSKey(
        HUSKEY hUSKey,
        LPCSTR pszValue,
        SHREGDEL_FLAGS delRegFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "pszValue", "delRegFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegDeleteEmptyUSKeyA(jitter):
    shlwapi_SHRegDeleteEmptyUSKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegDeleteEmptyUSKeyW(jitter):
    shlwapi_SHRegDeleteEmptyUSKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegDeleteUSValue(jitter, get_str, set_str):
    """
    LSTATUS SHRegDeleteUSValue(
        HUSKEY hUSKey,
        LPCTSTR pszValue,
        SHREGDEL_FLAGS delRegFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "pszValue", "delRegFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegDeleteUSValueA(jitter):
    shlwapi_SHRegDeleteUSValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegDeleteUSValueW(jitter):
    shlwapi_SHRegDeleteUSValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegDuplicateHKey(jitter):
    """
    HKEY SHRegDuplicateHKey(
        HKEY hkey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegEnumUSKey(jitter, get_str, set_str):
    """
    LSTATUS SHRegEnumUSKey(
        HUSKEY hUSKey,
        DWORD dwIndex,
        LPTSTR pszName,
        LPDWORD pcchName,
        SHREGENUM_FLAGS enumRegFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "dwIndex", "pszName", "pcchName", "enumRegFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegEnumUSKeyA(jitter):
    shlwapi_SHRegEnumUSKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegEnumUSKeyW(jitter):
    shlwapi_SHRegEnumUSKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegEnumUSValue(jitter, get_str, set_str):
    """
    LSTATUS SHRegEnumUSValue(
        HUSKEY hUSKey,
        DWORD dwIndex,
        LPTSTR pszValueName,
        LPDWORD pcchValueNameLen,
        [RegType*] pdwType,
        void* pvData,
        LPDWORD pcbData,
        SHREGENUM_FLAGS enumRegFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "dwIndex", "pszValueName", "pcchValueNameLen", "pdwType", "pvData", "pcbData", "enumRegFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegEnumUSValueA(jitter):
    shlwapi_SHRegEnumUSValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegEnumUSValueW(jitter):
    shlwapi_SHRegEnumUSValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegGetBoolUSValue(jitter, get_str, set_str):
    """
    BOOL SHRegGetBoolUSValue(
        LPCTSTR pszSubKey,
        LPCTSTR pszValue,
        BOOL fIgnoreHKCU,
        BOOL fDefault
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSubKey", "pszValue", "fIgnoreHKCU", "fDefault"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegGetBoolUSValueA(jitter):
    shlwapi_SHRegGetBoolUSValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegGetBoolUSValueW(jitter):
    shlwapi_SHRegGetBoolUSValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegGetIntW(jitter):
    """
    int SHRegGetIntW(
        HKEY hk,
        LPCWSTR szKey,
        int nDefault
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hk", "szKey", "nDefault"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegGetPath(jitter, get_str, set_str):
    """
    LSTATUS SHRegGetPath(
        HKEY hkey,
        LPCTSTR pszSubkey,
        LPCTSTR pszValue,
        LPTSTR pszPath,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubkey", "pszValue", "pszPath", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegGetPathA(jitter):
    shlwapi_SHRegGetPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegGetPathW(jitter):
    shlwapi_SHRegGetPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegGetUSValue(jitter, get_str, set_str):
    """
    LSTATUS SHRegGetUSValue(
        LPCTSTR pszSubKey,
        LPCTSTR pszValue,
        DWORD* pdwType,
        void* pvData,
        DWORD* pcbData,
        BOOL fIgnoreHKCU,
        void* pvDefaultData,
        DWORD dwDefaultDataSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSubKey", "pszValue", "pdwType", "pvData", "pcbData", "fIgnoreHKCU", "pvDefaultData", "dwDefaultDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegGetUSValueA(jitter):
    shlwapi_SHRegGetUSValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegGetUSValueW(jitter):
    shlwapi_SHRegGetUSValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegGetValue(jitter, get_str, set_str):
    """
    LSTATUS SHRegGetValue(
        HKEY hkey,
        LPCTSTR pszSubKey,
        LPCTSTR pszValue,
        SRRF srrfFlags,
        LPDWORD pdwType,
        LPVOID pvData,
        LPDWORD pcbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey", "pszValue", "srrfFlags", "pdwType", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegGetValueA(jitter):
    shlwapi_SHRegGetValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegGetValueW(jitter):
    shlwapi_SHRegGetValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegOpenUSKey(jitter, get_str, set_str):
    """
    LSTATUS SHRegOpenUSKey(
        LPCTSTR pszPath,
        REGSAM samDesired,
        HUSKEY hRelativeUSKey,
        PHUSKEY phNewUSKey,
        BOOL fIgnoreHKCU
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "samDesired", "hRelativeUSKey", "phNewUSKey", "fIgnoreHKCU"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegOpenUSKeyA(jitter):
    shlwapi_SHRegOpenUSKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegOpenUSKeyW(jitter):
    shlwapi_SHRegOpenUSKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegQueryInfoUSKey(jitter, get_str, set_str):
    """
    LSTATUS SHRegQueryInfoUSKey(
        HUSKEY hUSKey,
        LPDWORD pcSubKeys,
        LPDWORD pcchMaxSubKeyLen,
        LPDWORD pcValues,
        LPDWORD pcchMaxValueNameLen,
        SHREGENUM_FLAGS enumRegFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "pcSubKeys", "pcchMaxSubKeyLen", "pcValues", "pcchMaxValueNameLen", "enumRegFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegQueryInfoUSKeyA(jitter):
    shlwapi_SHRegQueryInfoUSKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegQueryInfoUSKeyW(jitter):
    shlwapi_SHRegQueryInfoUSKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegQueryUSValue(jitter, get_str, set_str):
    """
    LSTATUS SHRegQueryUSValue(
        HUSKEY hUSKey,
        LPCTSTR pszValue,
        [RegType*] pdwType,
        LPVOID pvData,
        LPDWORD pcbData,
        BOOL fIgnoreHKCU,
        LPVOID pvDefaultData,
        DWORD dwDefaultDataSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "pszValue", "pdwType", "pvData", "pcbData", "fIgnoreHKCU", "pvDefaultData", "dwDefaultDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegQueryUSValueA(jitter):
    shlwapi_SHRegQueryUSValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegQueryUSValueW(jitter):
    shlwapi_SHRegQueryUSValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegSetPath(jitter, get_str, set_str):
    """
    LSTATUS SHRegSetPath(
        HKEY hkey,
        LPCTSTR pszSubkey,
        LPCTSTR pszValue,
        LPCTSTR pszPath,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubkey", "pszValue", "pszPath", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegSetPathA(jitter):
    shlwapi_SHRegSetPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegSetPathW(jitter):
    shlwapi_SHRegSetPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegSetUSValue(jitter, get_str, set_str):
    """
    LSTATUS SHRegSetUSValue(
        LPCTSTR pszSubKey,
        LPCTSTR pszValue,
        DWORD dwType,
        LPVOID pvData,
        DWORD cbData,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSubKey", "pszValue", "dwType", "pvData", "cbData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegSetUSValueA(jitter):
    shlwapi_SHRegSetUSValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegSetUSValueW(jitter):
    shlwapi_SHRegSetUSValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegSetValue(jitter, get_str, set_str):
    """
    LSTATUS SHRegSetValue(
        HKEY hkey,
        LPCTSTR pszSubKey,
        LPCTSTR pszValue,
        SRRF srrfFlags,
        DWORD dwType,
        LPCVOID pvData,
        DWORD cbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey", "pszValue", "srrfFlags", "dwType", "pvData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegSetValueA(jitter):
    shlwapi_SHRegSetValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegSetValueW(jitter):
    shlwapi_SHRegSetValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHRegWriteUSValue(jitter, get_str, set_str):
    """
    LSTATUS SHRegWriteUSValue(
        HUSKEY hUSKey,
        LPCTSTR pszValue,
        DWORD dwType,
        LPVOID pvData,
        DWORD cbData,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "pszValue", "dwType", "pvData", "cbData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegWriteUSValueA(jitter):
    shlwapi_SHRegWriteUSValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHRegWriteUSValueW(jitter):
    shlwapi_SHRegWriteUSValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHSetValue(jitter, get_str, set_str):
    """
    LSTATUS SHSetValue(
        HKEY hkey,
        LPCTSTR pszSubKey,
        LPCTSTR pszValue,
        [RegType] dwType,
        LPCVOID pvData,
        DWORD cbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey", "pszValue", "dwType", "pvData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHSetValueA(jitter):
    shlwapi_SHSetValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHSetValueW(jitter):
    shlwapi_SHSetValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_CharLowerWrapW(jitter):
    """
    LPWSTR CharLowerWrapW(
        LPWSTR pch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_CharUpperBuffWrapW(jitter):
    """
    DWORD CharUpperBuffWrapW(
        LPWSTR pch,
        DWORD cchLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pch", "cchLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ChrCmpI(jitter, get_str, set_str):
    """
    BOOL ChrCmpI(
        TCHAR w1,
        TCHAR w2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["w1", "w2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ChrCmpIA(jitter):
    shlwapi_ChrCmpI(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_ChrCmpIW(jitter):
    shlwapi_ChrCmpI(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_CompareStringWrapW(jitter):
    """
    int CompareStringWrapW(
        LCID Locale,
        DWORD dwCmpFlags,
        LPCWSTR lpString1,
        int cchCount1,
        LPCWSTR lpString2,
        int cchCount2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwCmpFlags", "lpString1", "cchCount1", "lpString2", "cchCount2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_GetAcceptLanguages(jitter, get_str, set_str):
    """
    HRESULT GetAcceptLanguages(
        LPTSTR pszLanguages,
        DWORD* pcchLanguages
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszLanguages", "pcchLanguages"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_GetAcceptLanguagesA(jitter):
    shlwapi_GetAcceptLanguages(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_GetAcceptLanguagesW(jitter):
    shlwapi_GetAcceptLanguages(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_GetDateFormatWrapW(jitter):
    """
    int GetDateFormatWrapW(
        LCID Locale,
        DWORD dwFlags,
        const SYSTEMTIME* lpDate,
        LPCWSTR pwzFormat,
        LPWSTR pwzDateStr,
        int cchDate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwFlags", "lpDate", "pwzFormat", "pwzDateStr", "cchDate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_GetTimeFormatWrapW(jitter):
    """
    int GetTimeFormatWrapW(
        LCID Locale,
        DWORD dwFlags,
        const SYSTEMTIME* lpTime,
        LPCWSTR pwzFormat,
        LPWSTR pwzTimeStr,
        int cchTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwFlags", "lpTime", "pwzFormat", "pwzTimeStr", "cchTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IntlStrEqN(jitter, get_str, set_str):
    """
    BOOL IntlStrEqN(
        LPCTSTR pszStr1,
        LPCTSTR pszStr2,
        int nChar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszStr1", "pszStr2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IntlStrEqNA(jitter):
    shlwapi_IntlStrEqN(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_IntlStrEqNW(jitter):
    shlwapi_IntlStrEqN(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_IntlStrEqNI(jitter, get_str, set_str):
    """
    BOOL IntlStrEqNI(
        LPCTSTR pszStr1,
        LPCTSTR pszStr2,
        int nChar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszStr1", "pszStr2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IntlStrEqNIA(jitter):
    shlwapi_IntlStrEqNI(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_IntlStrEqNIW(jitter):
    shlwapi_IntlStrEqNI(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_IntlStrEqWorker(jitter, get_str, set_str):
    """
    BOOL IntlStrEqWorker(
        BOOL fCaseSens,
        LPCTSTR pszStr1,
        LPCTSTR pszStr2,
        int nChar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fCaseSens", "pszStr1", "pszStr2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IntlStrEqWorkerA(jitter):
    shlwapi_IntlStrEqWorker(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_IntlStrEqWorkerW(jitter):
    shlwapi_IntlStrEqWorker(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_IsCharAlphaNumericWrapW(jitter):
    """
    BOOL IsCharAlphaNumericWrapW(
        WCHAR ch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IsCharSpace(jitter, get_str, set_str):
    """
    BOOL IsCharSpace(
        TCHAR wch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IsCharSpaceA(jitter):
    shlwapi_IsCharSpace(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_IsCharSpaceW(jitter):
    shlwapi_IsCharSpace(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_OutputDebugStringWrapW(jitter):
    """
    void OutputDebugStringWrapW(
        LPCWSTR lpOutputString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpOutputString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHLoadIndirectString(jitter):
    """
    HRESULT SHLoadIndirectString(
        PCWSTR pszSource,
        PWSTR pszOutBuf,
        UINT cchOutBuf,
        void** ppvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSource", "pszOutBuf", "cchOutBuf", "ppvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHStrDup(jitter, get_str, set_str):
    """
    HRESULT SHStrDup(
        LPCTSTR pszSource,
        LPTSTR* ppwsz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSource", "ppwsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHStrDupA(jitter):
    shlwapi_SHStrDup(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHStrDupW(jitter):
    shlwapi_SHStrDup(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCat(jitter, get_str, set_str):
    """
    PTSTR StrCat(
        PTSTR psz1,
        PCTSTR psz2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCatA(jitter):
    shlwapi_StrCat(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCatW(jitter):
    shlwapi_StrCat(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCatBuff(jitter, get_str, set_str):
    """
    PTSTR StrCatBuff(
        PTSTR pszDest,
        PCTSTR pszSrc,
        int cchDestBuffSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDest", "pszSrc", "cchDestBuffSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCatBuffA(jitter):
    shlwapi_StrCatBuff(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCatBuffW(jitter):
    shlwapi_StrCatBuff(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCatChainW(jitter):
    """
    DWORD StrCatChainW(
        PWSTR pszDst,
        DWORD cchDst,
        DWORD ichAt,
        PCWSTR pszSrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDst", "cchDst", "ichAt", "pszSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrChr(jitter, get_str, set_str):
    """
    PTSTR StrChr(
        PTSTR pszStart,
        TCHAR wMatch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszStart", "wMatch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrChrA(jitter):
    shlwapi_StrChr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrChrW(jitter):
    shlwapi_StrChr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrChrI(jitter, get_str, set_str):
    """
    PTSTR StrChrI(
        PTSTR pszStart,
        TCHAR wMatch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszStart", "wMatch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrChrIA(jitter):
    shlwapi_StrChrI(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrChrIW(jitter):
    shlwapi_StrChrI(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrChrNIW(jitter):
    """
    PWSTR StrChrNIW(
        PCWSTR pszStart,
        WCHAR wMatch,
        UINT cchMax
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszStart", "wMatch", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrChrNW(jitter):
    """
    PWSTR StrChrNW(
        PWSTR pszStart,
        WCHAR wMatch,
        UINT cchMax
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszStart", "wMatch", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmp(jitter, get_str, set_str):
    """
    int StrCmp(
        PCTSTR psz1,
        PCTSTR psz2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpA(jitter):
    shlwapi_StrCmp(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCmpW(jitter):
    shlwapi_StrCmp(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCmpC(jitter, get_str, set_str):
    """
    int StrCmpC(
        LPCTSTR lpStr1,
        LPCTSTR lpStr2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpStr1", "lpStr2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpCA(jitter):
    shlwapi_StrCmpC(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCmpCW(jitter):
    shlwapi_StrCmpC(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCmpI(jitter, get_str, set_str):
    """
    int StrCmpI(
        PCTSTR psz1,
        PCTSTR psz2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpIA(jitter):
    shlwapi_StrCmpI(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCmpIW(jitter):
    shlwapi_StrCmpI(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCmpIC(jitter, get_str, set_str):
    """
    int StrCmpIC(
        LPCTSTR lpStr1,
        LPCTSTR lpStr2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpStr1", "lpStr2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpICA(jitter):
    shlwapi_StrCmpIC(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCmpICW(jitter):
    shlwapi_StrCmpIC(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCmpLogicalW(jitter):
    """
    int StrCmpLogicalW(
        PCWSTR psz1,
        PCWSTR psz2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpN(jitter, get_str, set_str):
    """
    int StrCmpN(
        PCTSTR psz1,
        PCTSTR psz2,
        int nChar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpNA(jitter):
    shlwapi_StrCmpN(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCmpNW(jitter):
    shlwapi_StrCmpN(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCmpNC(jitter, get_str, set_str):
    """
    int StrCmpNC(
        LPCTSTR pszStr1,
        LPCTSTR pszStr2,
        int nChar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszStr1", "pszStr2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpNCA(jitter):
    shlwapi_StrCmpNC(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCmpNCW(jitter):
    shlwapi_StrCmpNC(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCmpNI(jitter, get_str, set_str):
    """
    int StrCmpNI(
        PCTSTR psz1,
        PCTSTR psz2,
        int nChar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpNIA(jitter):
    shlwapi_StrCmpNI(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCmpNIW(jitter):
    shlwapi_StrCmpNI(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCmpNIC(jitter, get_str, set_str):
    """
    int StrCmpNIC(
        LPCTSTR pszStr1,
        LPCTSTR pszStr2,
        int nChar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszStr1", "pszStr2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpNICA(jitter):
    shlwapi_StrCmpNIC(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCmpNICW(jitter):
    shlwapi_StrCmpNIC(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCpy(jitter, get_str, set_str):
    """
    PTSTR StrCpy(
        PTSTR psz1,
        PCTSTR psz2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCpyA(jitter):
    shlwapi_StrCpy(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCpyW(jitter):
    shlwapi_StrCpy(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCpyN(jitter, get_str, set_str):
    """
    PTSTR StrCpyN(
        PTSTR pszDst,
        PCTSTR pszSrc,
        int cchMax
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDst", "pszSrc", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCpyNA(jitter):
    shlwapi_StrCpyN(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCpyNW(jitter):
    shlwapi_StrCpyN(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCSpn(jitter, get_str, set_str):
    """
    int StrCSpn(
        PCTSTR pszStr,
        PCTSTR pszSet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszStr", "pszSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCSpnA(jitter):
    shlwapi_StrCSpn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCSpnW(jitter):
    shlwapi_StrCSpn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrCSpnI(jitter, get_str, set_str):
    """
    int StrCSpnI(
        PCTSTR pszStr,
        PCTSTR pszSet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszStr", "pszSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCSpnIA(jitter):
    shlwapi_StrCSpnI(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrCSpnIW(jitter):
    shlwapi_StrCSpnI(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrDup(jitter, get_str, set_str):
    """
    PTSTR StrDup(
        PCTSTR pszSrch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSrch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrDupA(jitter):
    shlwapi_StrDup(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrDupW(jitter):
    shlwapi_StrDup(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrFormatByteSize64(jitter, get_str, set_str):
    """
    PTSTR StrFormatByteSize64(
        LONGLONG qdw,
        PTSTR pszBuf,
        UINT cchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["qdw", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrFormatByteSize64A(jitter):
    shlwapi_StrFormatByteSize64(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrFormatByteSize64W(jitter):
    shlwapi_StrFormatByteSize64(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrFormatByteSizeA(jitter):
    """
    PSTR StrFormatByteSizeA(
        DWORD dw,
        PSTR pszBuf,
        UINT cchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dw", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrFormatByteSizeW(jitter):
    """
    PWSTR StrFormatByteSizeW(
        LONGLONG qdw,
        PWSTR pszBuf,
        UINT cchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["qdw", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrFormatByteSizeEx(jitter):
    """
    HRESULT StrFormatByteSizeEx(
        ULONGLONG ull,
        SFBS_FLAGS flags,
        LPWSTR pszBuf,
        UINT cchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ull", "flags", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrFormatKBSize(jitter, get_str, set_str):
    """
    PTSTR StrFormatKBSize(
        LONGLONG qdw,
        PTSTR pszBuf,
        UINT cchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["qdw", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrFormatKBSizeA(jitter):
    shlwapi_StrFormatKBSize(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrFormatKBSizeW(jitter):
    shlwapi_StrFormatKBSize(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrFromTimeInterval(jitter, get_str, set_str):
    """
    int StrFromTimeInterval(
        PTSTR pszOut,
        UINT cchMax,
        DWORD dwTimeMS,
        int digits
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszOut", "cchMax", "dwTimeMS", "digits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrFromTimeIntervalA(jitter):
    shlwapi_StrFromTimeInterval(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrFromTimeIntervalW(jitter):
    shlwapi_StrFromTimeInterval(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrIsIntlEqual(jitter, get_str, set_str):
    """
    BOOL StrIsIntlEqual(
        BOOL fCaseSens,
        PCTSTR pszString1,
        PCTSTR pszString2,
        int nChar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fCaseSens", "pszString1", "pszString2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrIsIntlEqualA(jitter):
    shlwapi_StrIsIntlEqual(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrIsIntlEqualW(jitter):
    shlwapi_StrIsIntlEqual(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrNCat(jitter, get_str, set_str):
    """
    PTSTR StrNCat(
        PTSTR psz1,
        PCTSTR psz2,
        int cchMax
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrNCatA(jitter):
    shlwapi_StrNCat(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrNCatW(jitter):
    shlwapi_StrNCat(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrPBrk(jitter, get_str, set_str):
    """
    PTSTR StrPBrk(
        PTSTR psz,
        PCTSTR pszSet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "pszSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrPBrkA(jitter):
    shlwapi_StrPBrk(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrPBrkW(jitter):
    shlwapi_StrPBrk(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrRChr(jitter, get_str, set_str):
    """
    PTSTR StrRChr(
        PTSTR pszStart,
        PCTSTR pszEnd,
        TCHAR wMatch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszStart", "pszEnd", "wMatch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrRChrA(jitter):
    shlwapi_StrRChr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrRChrW(jitter):
    shlwapi_StrRChr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrRChrI(jitter, get_str, set_str):
    """
    PTSTR StrRChrI(
        PTSTR pszStart,
        PCTSTR pszEnd,
        TCHAR wMatch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszStart", "pszEnd", "wMatch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrRChrIA(jitter):
    shlwapi_StrRChrI(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrRChrIW(jitter):
    shlwapi_StrRChrI(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrRetToBSTR(jitter):
    """
    HRESULT StrRetToBSTR(
        STRRET* pstr,
        PCUITEMID_CHILD pidl,
        BSTR* pbstr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstr", "pidl", "pbstr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrRetToBuf(jitter, get_str, set_str):
    """
    HRESULT StrRetToBuf(
        STRRET* pstr,
        PCUITEMID_CHILD pidl,
        LPTSTR pszBuf,
        UINT cchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstr", "pidl", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrRetToBufA(jitter):
    shlwapi_StrRetToBuf(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrRetToBufW(jitter):
    shlwapi_StrRetToBuf(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrRetToStr(jitter, get_str, set_str):
    """
    HRESULT StrRetToStr(
        STRRET* pstr,
        PCUITEMID_CHILD pidl,
        LPTSTR* ppszName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstr", "pidl", "ppszName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrRetToStrA(jitter):
    shlwapi_StrRetToStr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrRetToStrW(jitter):
    shlwapi_StrRetToStr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrRStrI(jitter, get_str, set_str):
    """
    PTSTR StrRStrI(
        PTSTR pszSource,
        PCTSTR pszLast,
        PCTSTR pszSrch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSource", "pszLast", "pszSrch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrRStrIA(jitter):
    shlwapi_StrRStrI(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrRStrIW(jitter):
    shlwapi_StrRStrI(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrSpn(jitter, get_str, set_str):
    """
    int StrSpn(
        PCTSTR psz,
        PCTSTR pszSet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "pszSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrSpnA(jitter):
    shlwapi_StrSpn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrSpnW(jitter):
    shlwapi_StrSpn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrStr(jitter, get_str, set_str):
    """
    PTSTR StrStr(
        PTSTR pszFirst,
        PCTSTR pszSrch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFirst", "pszSrch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrStrA(jitter):
    shlwapi_StrStr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrStrW(jitter):
    shlwapi_StrStr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrStrI(jitter, get_str, set_str):
    """
    PTSTR StrStrI(
        PTSTR pszFirst,
        PCTSTR pszSrch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFirst", "pszSrch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrStrIA(jitter):
    shlwapi_StrStrI(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrStrIW(jitter):
    shlwapi_StrStrI(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrToInt(jitter, get_str, set_str):
    """
    int StrToInt(
        PCTSTR pszSrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrToIntA(jitter):
    shlwapi_StrToInt(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrToIntW(jitter):
    shlwapi_StrToInt(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrToInt64Ex(jitter, get_str, set_str):
    """
    BOOL StrToInt64Ex(
        PCTSTR pszString,
        STIF_FLAGS dwFlags,
        LONGLONG* pllRet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszString", "dwFlags", "pllRet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrToInt64ExA(jitter):
    shlwapi_StrToInt64Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrToInt64ExW(jitter):
    shlwapi_StrToInt64Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrToIntEx(jitter, get_str, set_str):
    """
    BOOL StrToIntEx(
        PCTSTR pszString,
        STIF_FLAGS dwFlags,
        int* piRet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszString", "dwFlags", "piRet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrToIntExA(jitter):
    shlwapi_StrToIntEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrToIntExW(jitter):
    shlwapi_StrToIntEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_StrTrim(jitter, get_str, set_str):
    """
    BOOL StrTrim(
        PTSTR psz,
        PCTSTR pszTrimChars
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "pszTrimChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrTrimA(jitter):
    shlwapi_StrTrim(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_StrTrimW(jitter):
    shlwapi_StrTrim(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_wnsprintf(jitter, get_str, set_str):
    """
    int wnsprintf(
        PTSTR pszDest,
        int cchDest,
        PCTSTR pszFmt,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDest", "cchDest", "pszFmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_wnsprintfA(jitter):
    shlwapi_wnsprintf(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_wnsprintfW(jitter):
    shlwapi_wnsprintf(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_wvnsprintf(jitter, get_str, set_str):
    """
    int wvnsprintf(
        PTSTR pszDest,
        int cchDest,
        PCTSTR pszFmt,
        va_list arglist
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDest", "cchDest", "pszFmt", "arglist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_wvnsprintfA(jitter):
    shlwapi_wvnsprintf(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_wvnsprintfW(jitter):
    shlwapi_wvnsprintf(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_ConnectToConnectionPoint(jitter):
    """
    HRESULT ConnectToConnectionPoint(
        IUnknown* punk,
        REFIID riidEvent,
        BOOL fConnect,
        IUnknown* punkTarget,
        DWORD* pdwCookie,
        IConnectionPoint** ppcpOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk", "riidEvent", "fConnect", "punkTarget", "pdwCookie", "ppcpOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_DllInstall(jitter):
    """
    HRESULT DllInstall(
        BOOL bInstall,
        PCWSTR pszCmdLine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bInstall", "pszCmdLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_FindResourceWrapW(jitter):
    """
    HRSRC FindResourceWrapW(
        HMODULE hModule,
        LPCWSTR lpName,
        LPCWSTR lpType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hModule", "lpName", "lpType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_GetMenuPosFromID(jitter):
    """
    int GetMenuPosFromID(
        HMENU hmenu,
        UINT id
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_HashData(jitter):
    """
    HRESULT HashData(
        BYTE* pbData,
        DWORD cbData,
        BYTE* pbHash,
        DWORD cbHash
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbData", "cbData", "pbHash", "cbHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_GUIDFromString(jitter, get_str, set_str):
    """
    BOOL GUIDFromString(
        LPCTSTR psz,
        LPGUID pguid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "pguid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_GUIDFromStringA(jitter):
    shlwapi_GUIDFromString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_GUIDFromStringW(jitter):
    shlwapi_GUIDFromString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_IsInternetESCEnabled(jitter):
    """
    BOOL IsInternetESCEnabled()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IsOS(jitter):
    """
    BOOL IsOS(
        DWORD dwOS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwOS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_Copy(jitter):
    """
    HRESULT IStream_Copy(
        IStream* pstmFrom,
        IStream* pstmTo,
        DWORD cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstmFrom", "pstmTo", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_Read(jitter):
    """
    HRESULT IStream_Read(
        IStream* pstm,
        VOID* pv,
        ULONG cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "pv", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_ReadPidl(jitter):
    """
    HRESULT IStream_ReadPidl(
        IStream* pstm,
        PIDLIST_RELATIVE* ppidlOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "ppidlOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_ReadStr(jitter):
    """
    HRESULT IStream_ReadStr(
        IStream* pstm,
        PWSTR* ppsz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "ppsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_Reset(jitter):
    """
    HRESULT IStream_Reset(
        IStream* pstm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_Size(jitter):
    """
    HRESULT IStream_Size(
        IStream* pstm,
        ULARGE_INTEGER* pui
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "pui"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_Write(jitter):
    """
    HRESULT IStream_Write(
        IStream* pstm,
        const void* pv,
        ULONG cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "pv", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_WritePidl(jitter):
    """
    HRESULT IStream_WritePidl(
        IStream* pstm,
        PCUIDLIST_RELATIVE pidlWrite
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "pidlWrite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_WriteStr(jitter):
    """
    HRESULT IStream_WriteStr(
        IStream* pstm,
        PCWSTR psz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "psz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_AtomicRelease(jitter):
    """
    void IUnknown_AtomicRelease(
        void** ppunk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppunk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_GetSite(jitter):
    """
    HRESULT IUnknown_GetSite(
        IUnknown* punk,
        REFIID riid,
        VOID** ppvSite
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk", "riid", "ppvSite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_GetWindow(jitter):
    """
    HRESULT IUnknown_GetWindow(
        IUnknown* punk,
        HWND* phwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk", "phwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_QueryService(jitter):
    """
    HRESULT IUnknown_QueryService(
        IUnknown* punk,
        REFGUID guidService,
        REFIID riid,
        void** ppvOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk", "guidService", "riid", "ppvOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_Set(jitter):
    """
    void IUnknown_Set(
        IUnknown* ppunk,
        IUnknown* punk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppunk", "punk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_SetSite(jitter):
    """
    HRESULT IUnknown_SetSite(
        IUnknown* punk,
        IUnknown* punkSite
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk", "punkSite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_MLFreeLibrary(jitter):
    """
    BOOL MLFreeLibrary(
        HMODULE hModule
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hModule"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_MLLoadLibrary(jitter, get_str, set_str):
    """
    HINSTANCE MLLoadLibrary(
        LPCTSTR lpszLibFileName,
        HMODULE hModule,
        DWORD dwCrossCodePage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszLibFileName", "hModule", "dwCrossCodePage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_MLLoadLibraryA(jitter):
    shlwapi_MLLoadLibrary(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_MLLoadLibraryW(jitter):
    shlwapi_MLLoadLibrary(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_MLHtmlHelp(jitter, get_str, set_str):
    """
    HWND MLHtmlHelp(
        HWND hwndCaller,
        LPCTSTR pszFile,
        UINT uCommand,
        DWORD_PTR dwData,
        DWORD dwCrossCodePage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndCaller", "pszFile", "uCommand", "dwData", "dwCrossCodePage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_MLHtmlHelpA(jitter):
    shlwapi_MLHtmlHelp(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_MLHtmlHelpW(jitter):
    shlwapi_MLHtmlHelp(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_MLWinHelp(jitter, get_str, set_str):
    """
    BOOL MLWinHelp(
        HWND hWndMain,
        LPCTSTR lpszHelp,
        UINT uCommand,
        DWORD_PTR dwData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndMain", "lpszHelp", "uCommand", "dwData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_MLWinHelpA(jitter):
    shlwapi_MLWinHelp(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_MLWinHelpW(jitter):
    shlwapi_MLWinHelp(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_ParseURL(jitter, get_str, set_str):
    """
    HRESULT ParseURL(
        LPCTSTR pcszUrl,
        PARSEDURL* ppu
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcszUrl", "ppu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ParseURLA(jitter):
    shlwapi_ParseURL(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_ParseURLW(jitter):
    shlwapi_ParseURL(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_QISearch(jitter):
    """
    HRESULT QISearch(
        void* that,
        LPCQITAB pqit,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["that", "pqit", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHAnsiToAnsi(jitter):
    """
    int SHAnsiToAnsi(
        LPCSTR pszSrc,
        LPWSTR pszDst,
        int cchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSrc", "pszDst", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHAnsiToUnicode(jitter):
    """
    int SHAnsiToUnicode(
        PCSTR pszSrc,
        PWSTR pwszDst,
        int cwchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSrc", "pwszDst", "cwchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHAutoComplete(jitter):
    """
    HRESULT SHAutoComplete(
        HWND hwndEdit,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndEdit", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateMemStream(jitter):
    """
    IStream* SHCreateMemStream(
        const BYTE* pInit,
        UINT cbInit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pInit", "cbInit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateStreamOnFile(jitter, get_str, set_str):
    """
    HRESULT SHCreateStreamOnFile(
        LPCTSTR pszFile,
        [STGM_FLAGS] grfMode,
        IStream** ppstm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFile", "grfMode", "ppstm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateStreamOnFileA(jitter):
    shlwapi_SHCreateStreamOnFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHCreateStreamOnFileW(jitter):
    shlwapi_SHCreateStreamOnFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHCreateStreamOnFileEx(jitter):
    """
    HRESULT SHCreateStreamOnFileEx(
        LPCWSTR pszFile,
        [STGM_FLAGS] grfMode,
        DWORD dwAttributes,
        BOOL fCreate,
        IStream* pstmTemplate,
        IStream** ppstm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFile", "grfMode", "dwAttributes", "fCreate", "pstmTemplate", "ppstm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateThread(jitter):
    """
    BOOL SHCreateThread(
        LPTHREAD_START_ROUTINE pfnThreadProc,
        void* pData,
        SHCT_FLAGS dwFlags,
        LPTHREAD_START_ROUTINE pfnCallback
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfnThreadProc", "pData", "dwFlags", "pfnCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateThreadRef(jitter):
    """
    HRESULT SHCreateThreadRef(
        LONG* pcRef,
        IUnknown** ppunk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcRef", "ppunk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateThreadWithHandle(jitter):
    """
    BOOL SHCreateThreadWithHandle(
        LPTHREAD_START_ROUTINE pfnThreadProc,
        void* pData,
        SHCT_FLAGS flags,
        LPTHREAD_START_ROUTINE pfnCallback,
        HANDLE* pHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfnThreadProc", "pData", "flags", "pfnCallback", "pHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHFormatDateTime(jitter, get_str, set_str):
    """
    int SHFormatDateTime(
        const FILETIME* pft,
        DWORD* pdwFlags,
        LPTSTR pszBuf,
        UINT cchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pft", "pdwFlags", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHFormatDateTimeA(jitter):
    shlwapi_SHFormatDateTime(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHFormatDateTimeW(jitter):
    shlwapi_SHFormatDateTime(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHGetThreadRef(jitter):
    """
    HRESULT SHGetThreadRef(
        IUnknown** ppunk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppunk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHSetThreadRef(jitter):
    """
    HRESULT SHSetThreadRef(
        IUnknown* punk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHReleaseThreadRef(jitter):
    """
    HRESULT SHReleaseThreadRef()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGlobalCounterDecrement(jitter):
    """
    long SHGlobalCounterDecrement(
        const SHGLOBALCOUNTER id
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGlobalCounterGetValue(jitter):
    """
    long SHGlobalCounterGetValue(
        const SHGLOBALCOUNTER id
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGlobalCounterIncrement(jitter):
    """
    long SHGlobalCounterIncrement(
        const SHGLOBALCOUNTER id
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHIsChildOrSelf(jitter):
    """
    HRESULT SHIsChildOrSelf(
        HWND hwndParent,
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHIsLowMemoryMachine(jitter):
    """
    BOOL SHIsLowMemoryMachine(
        DWORD dwType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHMessageBoxCheck(jitter, get_str, set_str):
    """
    int SHMessageBoxCheck(
        HWND hwnd,
        LPCTSTR pszText,
        LPCTSTR pszCaption,
        UINT uType,
        int iDefault,
        LPCTSTR pszRegVal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszText", "pszCaption", "uType", "iDefault", "pszRegVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHMessageBoxCheckA(jitter):
    shlwapi_SHMessageBoxCheck(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHMessageBoxCheckW(jitter):
    shlwapi_SHMessageBoxCheck(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHSendMessageBroadcast(jitter, get_str, set_str):
    """
    LRESULT SHSendMessageBroadcast(
        UINT uMsg,
        WPARAM wParam,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uMsg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHSendMessageBroadcastA(jitter):
    shlwapi_SHSendMessageBroadcast(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHSendMessageBroadcastW(jitter):
    shlwapi_SHSendMessageBroadcast(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHStripMneumonic(jitter, get_str, set_str):
    """
    TCHAR SHStripMneumonic(
        LPTSTR* pszMenu
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHStripMneumonicA(jitter):
    shlwapi_SHStripMneumonic(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shlwapi_SHStripMneumonicW(jitter):
    shlwapi_SHStripMneumonic(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shlwapi_SHUnicodeToAnsi(jitter):
    """
    int SHUnicodeToAnsi(
        PCWSTR pwszSrc,
        PSTR pszDst,
        int cchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszSrc", "pszDst", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHUnicodeToUnicode(jitter):
    """
    int SHUnicodeToUnicode(
        PCWSTR pwzSrc,
        PWSTR pwzDst,
        int cwchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzSrc", "pwzDst", "cwchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StopWatchFlush(jitter):
    """
    [ERROR_CODE] StopWatchFlush()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StopWatchMode(jitter):
    """
    DWORD StopWatchMode()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_WhichPlatform(jitter):
    """
    UINT WhichPlatform()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_GetProcessReference(jitter):
    """
    HRESULT GetProcessReference(
        IUnknown** punk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SetProcessReference(jitter):
    """
    void SetProcessReference(
        IUnknown* punk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRunIndirectRegClientCommand(jitter):
    """
    HRESULT SHRunIndirectRegClientCommand(
        HWND hwnd,
        LPCWSTR pszClientType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszClientType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_DupWideToAnsi(jitter):
    """
    HRESULT DupWideToAnsi(
        LPCWSTR pwszString,
        LPSTR* ppszStr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszString", "ppszStr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_ReadStrLong(jitter):
    """
    HRESULT IStream_ReadStrLong(
        IStream* pStream,
        LPWSTR* ppwszString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStream", "ppwszString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_WriteStrLong(jitter):
    """
    HRESULT IStream_WriteStrLong(
        IStream* pStream,
        LPCWSTR pwszString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStream", "pwszString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_RemoveBackReferences(jitter):
    """
    HRESULT IUnknown_RemoveBackReferences(
        IUnknown* pUnk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_TranslateAcceleratorGlobal(jitter):
    """
    HRESULT IUnknown_TranslateAcceleratorGlobal(
        IUnknown* pUnk,
        MSG* pMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "pMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_TranslateAcceleratorIO(jitter):
    """
    HRESULT IUnknown_TranslateAcceleratorIO(
        IUnknown* pUnk,
        MSG* pMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "pMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_MapWin32ErrorToSTG(jitter):
    """
    HRESULT MapWin32ErrorToSTG(
        HRESULT hrWin32
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrWin32"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ModeToCreateFileFlags(jitter):
    """
    HRESULT ModeToCreateFileFlags(
        [STGM_FLAGS] grfFlags,
        BOOL bCreate,
        DWORD* pDesiredAccess,
        DWORD* pShareMode,
        DWORD* pDisposition
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["grfFlags", "bCreate", "pDesiredAccess", "pShareMode", "pDisposition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathUnExpandEnvStringsForUserW(jitter):
    """
    BOOL PathUnExpandEnvStringsForUserW(
        HANDLE hUserToken,
        LPCWSTR pwszPath,
        LPWSTR pwszBuf,
        UINT cchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hUserToken", "pwszPath", "pwszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathUnExpandSystemEnvStringsW(jitter):
    """
    BOOL PathUnExpandSystemEnvStringsW(
        LPCWSTR pwszPath,
        LPWSTR pwszBuf,
        UINT cchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszPath", "pwszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_QuerySourceCreateFromKey(jitter):
    """
    HRESULT QuerySourceCreateFromKey(
        HKEY hKey,
        LPCWSTR pwszSubKey,
        BOOL shouldCreate,
        REFIID riid,
        LPVOID* ppInterface
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pwszSubKey", "shouldCreate", "riid", "ppInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_QuerySourceCreateFromKeyEx(jitter):
    """
    HRESULT QuerySourceCreateFromKeyEx(
        HKEY hKey,
        LPCWSTR pwszSubKey,
        BOOL shouldCreate,
        ACCESS_MASK amDesired,
        REFIID riid,
        LPVOID* ppInterface
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pwszSubKey", "shouldCreate", "amDesired", "riid", "ppInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHAnsiToUnicodeCPAlloc(jitter):
    """
    HRESULT SHAnsiToUnicodeCPAlloc(
        UINT codePage,
        LPCSTR pszString,
        LPWSTR* ppwszConverted
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["codePage", "pszString", "ppwszConverted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHAreIconsEqual(jitter):
    """
    BOOL SHAreIconsEqual(
        HICON hIcon1,
        HICON hIcon2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIcon1", "hIcon2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHBoolSystemParametersInfo(jitter):
    """
    BOOL SHBoolSystemParametersInfo(
        [SystemParametersInfoEnum] uiAction,
        PVOID pData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiAction", "pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreatePropertyBagOnMemory(jitter):
    """
    HRESULT SHCreatePropertyBagOnMemory(
        PVOID pUnused,
        REFIID riid,
        PVOID* ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnused", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreatePropertyStoreOnXML(jitter):
    """
    HRESULT SHCreatePropertyStoreOnXML(
        IXMLDOMNode* pXmlDomNode,
        [STGM_FLAGS] grfMode,
        IPropertyBag* pPropBagInit,
        REFIID riid,
        PVOID* ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pXmlDomNode", "grfMode", "pPropBagInit", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateStreamOnDllResourceW(jitter):
    """
    HRESULT SHCreateStreamOnDllResourceW(
        LPCWSTR pwszModule,
        LPCWSTR pwszName,
        LPCWSTR pwszType,
        IStream** ppStream
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszModule", "pwszName", "pwszType", "ppStream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateStreamOnModuleResourceW(jitter):
    """
    HRESULT SHCreateStreamOnModuleResourceW(
        HMODULE hModule,
        LPCWSTR pwszName,
        LPCWSTR pwszType,
        IStream** ppStream
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hModule", "pwszName", "pwszType", "ppStream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHExpandEnvironmentStringsAlloc(jitter):
    """
    HRESULT SHExpandEnvironmentStringsAlloc(
        LPCWSTR pwszExpandableString,
        LPWSTR* ppwszExpanded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszExpandableString", "ppwszExpanded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHForwardContextMenuMsg(jitter):
    """
    HRESULT SHForwardContextMenuMsg(
        IUnknown* pUnk,
        UINT uMsg,
        WPARAM wParam,
        LPARAM lParam,
        LRESULT* pResult,
        BOOL useIContextMenu2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "uMsg", "wParam", "lParam", "pResult", "useIContextMenu2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGetSizeShared(jitter):
    """
    DWORD SHGetSizeShared(
        PVOID pData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHInvokeCommandOnContextMenu(jitter):
    """
    HRESULT SHInvokeCommandOnContextMenu(
        HWND hwnd,
        IObjectWithSite* pSite,
        IContextMenu* pCtxMenu,
        [CMIC_Mask] fMask,
        LPCSTR pszVerb,
        LPCWSTR pwszDirectory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pSite", "pCtxMenu", "fMask", "pszVerb", "pwszDirectory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHInvokeCommandOnContextMenuEx(jitter):
    """
    HRESULT SHInvokeCommandOnContextMenuEx(
        HWND hwnd,
        IObjectWithSite* pSite,
        IContextMenu* pCtxMenu,
        [CMIC_Mask] fMask,
        UINT queryFlags,
        LPCSTR pszVerb,
        LPCWSTR pwszDirectory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pSite", "pCtxMenu", "fMask", "queryFlags", "pszVerb", "pwszDirectory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHInvokeCommandWithFlagsAndSite(jitter):
    """
    HRESULT SHInvokeCommandWithFlagsAndSite(
        HWND hwnd,
        IObjectWithSite* pSite,
        IShellFolder* pShellFolder,
        LPITEMIDLIST pidl,
        [CMIC_Mask] fMask,
        LPCSTR pszVerb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pSite", "pShellFolder", "pidl", "fMask", "pszVerb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHInvokeCommandsOnContextMenuEx(jitter):
    """
    HRESULT SHInvokeCommandsOnContextMenuEx(
        HWND hwnd,
        IObjectWithSite* pSite,
        IContextMenu* pCtxMenu,
        [CMIC_Mask] fMask,
        UINT queryFlags,
        LPCSTR* ppszVerbs,
        UINT numVerbs,
        LPCWSTR pwszDirectory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pSite", "pCtxMenu", "fMask", "queryFlags", "ppszVerbs", "numVerbs", "pwszDirectory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegSetValue(jitter):
    """
    LSTATUS SHRegSetValue(
        HKEY hKey,
        LPCWSTR pwszSubKey,
        LPCWSTR pwszValue,
        SRRF srrfFlags,
        DWORD dwType,
        LPCVOID pvData,
        DWORD cbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pwszSubKey", "pwszValue", "srrfFlags", "dwType", "pvData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHUnicodeToAnsiCPAlloc(jitter):
    """
    HRESULT SHUnicodeToAnsiCPAlloc(
        UINT codePage,
        LPCWSTR pwszString,
        LPSTR* ppszConverted
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["codePage", "pwszString", "ppszConverted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
