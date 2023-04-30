###### Enums ######
ASSOCCLASS = {
    "ASSOCCLASS_SHELL_KEY": 0,
    "ASSOCCLASS_PROGID_KEY": 1,
    "ASSOCCLASS_PROGID_STR": 2,
    "ASSOCCLASS_CLSID_KEY": 3,
    "ASSOCCLASS_CLSID_STR": 4,
    "ASSOCCLASS_APP_KEY": 5,
    "ASSOCCLASS_APP_STR": 6,
    "ASSOCCLASS_SYSTEM_STR": 7,
    "ASSOCCLASS_FOLDER": 8,
    "ASSOCCLASS_STAR": 9,
    "ASSOCCLASS_FIXED_PROGID_STR": 10,
    "ASSOCCLASS_PROTOCOL_STR": 11,
}
ASSOCCLASS_INV = {
    0: "ASSOCCLASS_SHELL_KEY",
    1: "ASSOCCLASS_PROGID_KEY",
    2: "ASSOCCLASS_PROGID_STR",
    3: "ASSOCCLASS_CLSID_KEY",
    4: "ASSOCCLASS_CLSID_STR",
    5: "ASSOCCLASS_APP_KEY",
    6: "ASSOCCLASS_APP_STR",
    7: "ASSOCCLASS_SYSTEM_STR",
    8: "ASSOCCLASS_FOLDER",
    9: "ASSOCCLASS_STAR",
    10: "ASSOCCLASS_FIXED_PROGID_STR",
    11: "ASSOCCLASS_PROTOCOL_STR",
}
_SHGetDataFromIDListFormats_ = {
    "SHGDFIL_FINDDATA": 1,
    "SHGDFIL_NETRESOURCE": 2,
    "SHGDFIL_DESCRIPTIONID": 3,
}
_SHGetDataFromIDListFormats__INV = {
    1: "SHGDFIL_FINDDATA",
    2: "SHGDFIL_NETRESOURCE",
    3: "SHGDFIL_DESCRIPTIONID",
}
_SHGetFolderPathFlags_ = {
    "SHGFP_TYPE_CURRENT": 0,
    "SHGFP_TYPE_DEFAULT": 1,
}
_SHGetFolderPathFlags__INV = {
    0: "SHGFP_TYPE_CURRENT",
    1: "SHGFP_TYPE_DEFAULT",
}
ASSOC_FILTER = {
    "ASSOC_FILTER_NONE": 0,
    "ASSOC_FILTER_RECOMMENDED": 0x1,
}
ASSOC_FILTER_INV = {
    0: "ASSOC_FILTER_NONE",
    0x1: "ASSOC_FILTER_RECOMMENDED",
}
SCNRT_STATUS = {
    "SCNRT_ENABLE": 0,
    "SCNRT_DISABLE": 1,
}
SCNRT_STATUS_INV = {
    0: "SCNRT_ENABLE",
    1: "SCNRT_DISABLE",
}
SHSTOCKICONID = {
    "SIID_DOCNOASSOC": 0,
    "SIID_DOCASSOC": 1,
    "SIID_APPLICATION": 2,
    "SIID_FOLDER": 3,
    "SIID_FOLDEROPEN": 4,
    "SIID_DRIVE525": 5,
    "SIID_DRIVE35": 6,
    "SIID_DRIVEREMOVE": 7,
    "SIID_DRIVEFIXED": 8,
    "SIID_DRIVENET": 9,
    "SIID_DRIVENETDISABLED": 10,
    "SIID_DRIVECD": 11,
    "SIID_DRIVERAM": 12,
    "SIID_WORLD": 13,
    "SIID_SERVER": 15,
    "SIID_PRINTER": 16,
    "SIID_MYNETWORK": 17,
    "SIID_FIND": 22,
    "SIID_HELP": 23,
    "SIID_SHARE": 28,
    "SIID_LINK": 29,
    "SIID_SLOWFILE": 30,
    "SIID_RECYCLER": 31,
    "SIID_RECYCLERFULL": 32,
    "SIID_MEDIACDAUDIO": 40,
    "SIID_LOCK": 47,
    "SIID_AUTOLIST": 49,
    "SIID_PRINTERNET": 50,
    "SIID_SERVERSHARE": 51,
    "SIID_PRINTERFAX": 52,
    "SIID_PRINTERFAXNET": 53,
    "SIID_PRINTERFILE": 54,
    "SIID_STACK": 55,
    "SIID_MEDIASVCD": 56,
    "SIID_STUFFEDFOLDER": 57,
    "SIID_DRIVEUNKNOWN": 58,
    "SIID_DRIVEDVD": 59,
    "SIID_MEDIADVD": 60,
    "SIID_MEDIADVDRAM": 61,
    "SIID_MEDIADVDRW": 62,
    "SIID_MEDIADVDR": 63,
    "SIID_MEDIADVDROM": 64,
    "SIID_MEDIACDAUDIOPLUS": 65,
    "SIID_MEDIACDRW": 66,
    "SIID_MEDIACDR": 67,
    "SIID_MEDIACDBURN": 68,
    "SIID_MEDIABLANKCD": 69,
    "SIID_MEDIACDROM": 70,
    "SIID_AUDIOFILES": 71,
    "SIID_IMAGEFILES": 72,
    "SIID_VIDEOFILES": 73,
    "SIID_MIXEDFILES": 74,
    "SIID_FOLDERBACK": 75,
    "SIID_FOLDERFRONT": 76,
    "SIID_SHIELD": 77,
    "SIID_WARNING": 78,
    "SIID_INFO": 79,
    "SIID_ERROR": 80,
    "SIID_KEY": 81,
    "SIID_SOFTWARE": 82,
    "SIID_RENAME": 83,
    "SIID_DELETE": 84,
    "SIID_MEDIAAUDIODVD": 85,
    "SIID_MEDIAMOVIEDVD": 86,
    "SIID_MEDIAENHANCEDCD": 87,
    "SIID_MEDIAENHANCEDDVD": 88,
    "SIID_MEDIAHDDVD": 89,
    "SIID_MEDIABLURAY": 90,
    "SIID_MEDIAVCD": 91,
    "SIID_MEDIADVDPLUSR": 92,
    "SIID_MEDIADVDPLUSRW": 93,
    "SIID_DESKTOPPC": 94,
    "SIID_MOBILEPC": 95,
    "SIID_USERS": 96,
    "SIID_MEDIASMARTMEDIA": 97,
    "SIID_MEDIACOMPACTFLASH": 98,
    "SIID_DEVICECELLPHONE": 99,
    "SIID_DEVICECAMERA": 100,
    "SIID_DEVICEVIDEOCAMERA": 101,
    "SIID_DEVICEAUDIOPLAYER": 102,
    "SIID_NETWORKCONNECT": 103,
    "SIID_INTERNET": 104,
    "SIID_ZIPFILE": 105,
    "SIID_SETTINGS": 106,
    "SIID_MAX_ICONS": 107,
}
SHSTOCKICONID_INV = {
    0: "SIID_DOCNOASSOC",
    1: "SIID_DOCASSOC",
    2: "SIID_APPLICATION",
    3: "SIID_FOLDER",
    4: "SIID_FOLDEROPEN",
    5: "SIID_DRIVE525",
    6: "SIID_DRIVE35",
    7: "SIID_DRIVEREMOVE",
    8: "SIID_DRIVEFIXED",
    9: "SIID_DRIVENET",
    10: "SIID_DRIVENETDISABLED",
    11: "SIID_DRIVECD",
    12: "SIID_DRIVERAM",
    13: "SIID_WORLD",
    15: "SIID_SERVER",
    16: "SIID_PRINTER",
    17: "SIID_MYNETWORK",
    22: "SIID_FIND",
    23: "SIID_HELP",
    28: "SIID_SHARE",
    29: "SIID_LINK",
    30: "SIID_SLOWFILE",
    31: "SIID_RECYCLER",
    32: "SIID_RECYCLERFULL",
    40: "SIID_MEDIACDAUDIO",
    47: "SIID_LOCK",
    49: "SIID_AUTOLIST",
    50: "SIID_PRINTERNET",
    51: "SIID_SERVERSHARE",
    52: "SIID_PRINTERFAX",
    53: "SIID_PRINTERFAXNET",
    54: "SIID_PRINTERFILE",
    55: "SIID_STACK",
    56: "SIID_MEDIASVCD",
    57: "SIID_STUFFEDFOLDER",
    58: "SIID_DRIVEUNKNOWN",
    59: "SIID_DRIVEDVD",
    60: "SIID_MEDIADVD",
    61: "SIID_MEDIADVDRAM",
    62: "SIID_MEDIADVDRW",
    63: "SIID_MEDIADVDR",
    64: "SIID_MEDIADVDROM",
    65: "SIID_MEDIACDAUDIOPLUS",
    66: "SIID_MEDIACDRW",
    67: "SIID_MEDIACDR",
    68: "SIID_MEDIACDBURN",
    69: "SIID_MEDIABLANKCD",
    70: "SIID_MEDIACDROM",
    71: "SIID_AUDIOFILES",
    72: "SIID_IMAGEFILES",
    73: "SIID_VIDEOFILES",
    74: "SIID_MIXEDFILES",
    75: "SIID_FOLDERBACK",
    76: "SIID_FOLDERFRONT",
    77: "SIID_SHIELD",
    78: "SIID_WARNING",
    79: "SIID_INFO",
    80: "SIID_ERROR",
    81: "SIID_KEY",
    82: "SIID_SOFTWARE",
    83: "SIID_RENAME",
    84: "SIID_DELETE",
    85: "SIID_MEDIAAUDIODVD",
    86: "SIID_MEDIAMOVIEDVD",
    87: "SIID_MEDIAENHANCEDCD",
    88: "SIID_MEDIAENHANCEDDVD",
    89: "SIID_MEDIAHDDVD",
    90: "SIID_MEDIABLURAY",
    91: "SIID_MEDIAVCD",
    92: "SIID_MEDIADVDPLUSR",
    93: "SIID_MEDIADVDPLUSRW",
    94: "SIID_DESKTOPPC",
    95: "SIID_MOBILEPC",
    96: "SIID_USERS",
    97: "SIID_MEDIASMARTMEDIA",
    98: "SIID_MEDIACOMPACTFLASH",
    99: "SIID_DEVICECELLPHONE",
    100: "SIID_DEVICECAMERA",
    101: "SIID_DEVICEVIDEOCAMERA",
    102: "SIID_DEVICEAUDIOPLAYER",
    103: "SIID_NETWORKCONNECT",
    104: "SIID_INTERNET",
    105: "SIID_ZIPFILE",
    106: "SIID_SETTINGS",
    107: "SIID_MAX_ICONS",
}
QUERY_USER_NOTIFICATION_STATE = {
    "QUNS_NOT_PRESENT": 1,
    "QUNS_BUSY": 2,
    "QUNS_RUNNING_D3D_FULL_SCREEN": 3,
    "QUNS_PRESENTATION_MODE": 4,
    "QUNS_ACCEPTS_NOTIFICATIONS": 5,
    "QUNS_QUIET_TIME": 6,
    "QUNS_APP": 7,
}
QUERY_USER_NOTIFICATION_STATE_INV = {
    1: "QUNS_NOT_PRESENT",
    2: "QUNS_BUSY",
    3: "QUNS_RUNNING_D3D_FULL_SCREEN",
    4: "QUNS_PRESENTATION_MODE",
    5: "QUNS_ACCEPTS_NOTIFICATIONS",
    6: "QUNS_QUIET_TIME",
    7: "QUNS_APP",
}
LIBRARYMANAGEDIALOGOPTIONS = {
    "LMD_DEFAULT": 0x00000000,
    "LMD_ALLOWUNINDEXABLENETWORKLOCATIONS": 0x00000001,
}
LIBRARYMANAGEDIALOGOPTIONS_INV = {
    0x00000000: "LMD_DEFAULT",
    0x00000001: "LMD_ALLOWUNINDEXABLENETWORKLOCATIONS",
}
SHARD = {
    "SHARD_PIDL": 0x00000001,
    "SHARD_PATHA": 0x00000002,
    "SHARD_PATHW": 0x00000003,
    "SHARD_APPIDINFO": 0x00000004,
    "SHARD_APPIDINFOIDLIST": 0x00000005,
    "SHARD_LINK": 0x00000006,
    "SHARD_APPIDINFOLINK": 0x00000007,
    "SHARD_SHELLITEM": 0x00000008,
}
SHARD_INV = {
    0x00000001: "SHARD_PIDL",
    0x00000002: "SHARD_PATHA",
    0x00000003: "SHARD_PATHW",
    0x00000004: "SHARD_APPIDINFO",
    0x00000005: "SHARD_APPIDINFOIDLIST",
    0x00000006: "SHARD_LINK",
    0x00000007: "SHARD_APPIDINFOLINK",
    0x00000008: "SHARD_SHELLITEM",
}

###################

###### Types ######
RESTRICTIONS = UINT
LPSHELLSTATE = LPVOID
LPSHELLFLAGSTATE = LPVOID
CABINETSTATE_PTR = LPVOID
FARPROC16 = LPVOID
LPFNDFMCALLBACK = LPVOID
HDROP = HANDLE
HPSXA = HANDLE
LPFNADDPROPSHEETPAGE = LPVOID
LPFNVIEWCALLBACK = LPVOID
PFNASYNCICONTASKBALLBACK = LPVOID
PROPVARIANT__ = Ptr("<I", PROPVARIANT())
HKEY___ = Ptr("<I", HKEY())
TCHAR__80_ = Array(TCHAR, 80)
POINT__NUM_POINTS_ = Array(POINT, 3)
DWORD__NUM_POINTS_ = Array(DWORD, 3)

class AUTO_SCROLL_DATA(MemStruct):
    fields = [
        ("iNextSample", int()),
        ("dwLastScroll", DWORD()),
        ("bFull", BOOL()),
        ("pts", POINT__NUM_POINTS_()),
        ("dwTimes", DWORD__NUM_POINTS_()),
    ]

AUTO_SCROLL_DATA_PTR = Ptr("<I", AUTO_SCROLL_DATA())
_BROWSEINFO_FLAG_ = UINT

class BROWSEINFO(MemStruct):
    fields = [
        ("hwndOwner", HWND()),
        ("pidlRoot", PCIDLIST_ABSOLUTE()),
        ("pszDisplayName", LPTSTR()),
        ("lpszTitle", LPCTSTR()),
        ("ulFlags", _BROWSEINFO_FLAG_()),
        ("lpfn", BFFCALLBACK()),
        ("lParam", LPARAM()),
        ("iImage", int()),
    ]

LPBROWSEINFO = Ptr("<I", BROWSEINFO())
_NOTIFYICONDATA_u_ = Union([
    ("uTimeout", UINT),
    ("uVersion", UINT),
])
_NOTIFYICON_FLAG_ = UINT
_NOTIFYICON_STATE_ = DWORD
_NOTIFYICON_INFO_FLAG_ = DWORD

class NOTIFYICONDATA(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("hWnd", HWND()),
        ("uID", UINT()),
        ("uFlags", _NOTIFYICON_FLAG_()),
        ("uCallbackMessage", UINT()),
        ("hIcon", HICON()),
        ("szTip", TCHAR__128_()),
        ("dwState", _NOTIFYICON_STATE_()),
        ("dwStateMask", _NOTIFYICON_STATE_()),
        ("szInfo", TCHAR__256_()),
        (None, _NOTIFYICONDATA_u_()),
        ("szInfoTitle", TCHAR__64_()),
        ("dwInfoFlags", _NOTIFYICON_INFO_FLAG_()),
        ("guidItem", GUID()),
        ("hBalloonIcon", HICON()),
    ]

PNOTIFYICONDATA = Ptr("<I", NOTIFYICONDATA())
_SFGAOF_DWORD_ = SFGAOF
_SFGAOF_DWORD_PTR_ = Ptr("<I", _SFGAOF_DWORD_())

class SHFILEINFO(MemStruct):
    fields = [
        ("hIcon", HICON()),
        ("iIcon", int()),
        ("dwAttributes", _SFGAOF_DWORD_()),
        ("szDisplayName", TCHAR__MAX_PATH_()),
        ("szTypeName", TCHAR__80_()),
    ]

SHFILEINFO_PTR = Ptr("<I", SHFILEINFO())
_SHFOLDERCUSTOMSETTINGS_MASK_ = DWORD

class SHFOLDERCUSTOMSETTINGS(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("dwMask", _SHFOLDERCUSTOMSETTINGS_MASK_()),
        ("pvid", SHELLVIEWID_PTR()),
        ("pszWebViewTemplate", LPWSTR()),
        ("cchWebViewTemplate", DWORD()),
        ("pszWebViewTemplateVersion", LPWSTR()),
        ("pszInfoTip", LPWSTR()),
        ("cchInfoTip", DWORD()),
        ("pclsid", CLSID_PTR()),
        ("dwFlags", DWORD()),
        ("pszIconFile", LPWSTR()),
        ("cchIconFile", DWORD()),
        ("iIconIndex", int()),
        ("pszLogo", LPWSTR()),
        ("cchLogo", DWORD()),
    ]

LPSHFOLDERCUSTOMSETTINGS = Ptr("<I", SHFOLDERCUSTOMSETTINGS())

class SHSTOCKICONINFO(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("hIcon", HICON()),
        ("iSysImageIndex", int()),
        ("iIcon", int()),
        ("szPath", WCHAR__MAX_PATH_()),
    ]

SHSTOCKICONINFO_PTR = Ptr("<I", SHSTOCKICONINFO())
OPEN_AS_INFO_FLAGS = UINT

class OPENASINFO(MemStruct):
    fields = [
        ("pcszFile", LPCWSTR()),
        ("pcszClass", LPCWSTR()),
        ("oaifInFlags", OPEN_AS_INFO_FLAGS()),
    ]

const_OPENASINFO_PTR = Ptr("<I", OPENASINFO())
ASSOCCLASS = UINT

class ASSOCIATIONELEMENT(MemStruct):
    fields = [
        ("ac", ASSOCCLASS()),
        ("hkClass", HKEY()),
        ("pszClass", PCWSTR()),
    ]

const_ASSOCIATIONELEMENT_PTR = Ptr("<I", ASSOCIATIONELEMENT())

class SHChangeNotifyEntry(MemStruct):
    fields = [
        ("pidl", PCIDLIST_ABSOLUTE()),
        ("fRecursive", BOOL()),
    ]

SHChangeNotifyEntry_PTR = Ptr("<I", SHChangeNotifyEntry())
const_SHChangeNotifyEntry_PTR = Ptr("<I", SHChangeNotifyEntry())

class APPBARDATA(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("hWnd", HWND()),
        ("uCallbackMessage", UINT()),
        ("uEdge", UINT()),
        ("rc", RECT()),
        ("lParam", LPARAM()),
    ]

PAPPBARDATA = Ptr("<I", APPBARDATA())

class DEFCONTEXTMENU(MemStruct):
    fields = [
        ("hwnd", HWND()),
        ("pcmcb", IContextMenuCB_PTR()),
        ("pidlFolder", PCIDLIST_ABSOLUTE()),
        ("psf", IShellFolder_PTR()),
        ("cidl", UINT()),
        ("apidl", PCUITEMID_CHILD_ARRAY()),
        ("punkAssociationInfo", IUnknown_PTR()),
        ("cKeys", UINT()),
        ("aKeys", const_HKEY_PTR()),
    ]

const_DEFCONTEXTMENU_PTR = Ptr("<I", DEFCONTEXTMENU())

class SHCREATEPROCESSINFOW(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("fMask", _SEE_MASK_()),
        ("hwnd", HWND()),
        ("pszFile", LPCWSTR()),
        ("pszParameters", LPCWSTR()),
        ("pszCurrentDirectory", LPCWSTR()),
        ("hUserToken", HANDLE()),
        ("lpProcessAttributes", LPSECURITY_ATTRIBUTES()),
        ("lpThreadAttributes", LPSECURITY_ATTRIBUTES()),
        ("bInheritHandles", BOOL()),
        ("dwCreationFlags", _CreateProcessFlags_()),
        ("lpStartupInfo", LPSTARTUPINFOW()),
        ("lpProcessInformation", LPPROCESS_INFORMATION()),
    ]

PSHCREATEPROCESSINFOW = Ptr("<I", SHCREATEPROCESSINFOW())

class CSFV(MemStruct):
    fields = [
        ("cbSize", UINT()),
        ("pshf", IShellFolder_PTR()),
        ("psvOuter", IShellView_PTR()),
        ("pidl", PCIDLIST_ABSOLUTE()),
        ("lEvents", LONG()),
        ("pfnCallback", LPFNVIEWCALLBACK()),
        ("fvm", FOLDERVIEWMODE()),
    ]

LPCSFV = Ptr("<I", CSFV())

class SFV_CREATE(MemStruct):
    fields = [
        ("cbSize", UINT()),
        ("pshf", IShellFolder_PTR()),
        ("psvOuter", IShellView_PTR()),
        ("psfvcb", IShellFolderViewCB_PTR()),
    ]

const_SFV_CREATE_PTR = Ptr("<I", SFV_CREATE())

class NOTIFYICONIDENTIFIER(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("hWnd", HWND()),
        ("uID", UINT()),
        ("guidItem", GUID()),
    ]

const_NOTIFYICONIDENTIFIER_PTR = Ptr("<I", NOTIFYICONIDENTIFIER())

class SHFILEOPSTRUCT(MemStruct):
    fields = [
        ("hwnd", HWND()),
        ("wFunc", UINT()),
        ("pFrom", LPCTSTR()),
        ("pTo", LPCTSTR()),
        ("fFlags", FILEOP_FLAGS()),
        ("fAnyOperationsAborted", BOOL()),
        ("hNameMappings", LPVOID()),
        ("lpszProgressTitle", LPCTSTR()),
    ]

LPSHFILEOPSTRUCT = Ptr("<I", SHFILEOPSTRUCT())

class SHQUERYRBINFO(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("i64Size", DWORDLONG()),
        ("i64NumItems", DWORDLONG()),
    ]

LPSHQUERYRBINFO = Ptr("<I", SHQUERYRBINFO())
_SHGetDataFromIDListFormats_ = int
_SHGetFolderPathFlags_ = DWORD
_ShellChangeNotifyEvent_ = ULONG
_ShellChangeNotifyFlag_ = UINT
ASSOC_FILTER = UINT
SCNRT_STATUS = UINT
DATAOBJ_GET_ITEM_FLAGS = DWORD
GPFIDL_FLAGS = UINT
SHSTOCKICONID = UINT
QUERY_USER_NOTIFICATION_STATE = UINT
QUERY_USER_NOTIFICATION_STATE_PTR = Ptr("<I", QUERY_USER_NOTIFICATION_STATE())
LIBRARYMANAGEDIALOGOPTIONS = UINT
_RunFileDlgFlags_ = UINT
_NUMBERFMT_FLAGS_ = DWORD
_SGUPP_FLAGS_ = DWORD
_SECL_FLAGS_ = DWORD

class CLASSPIDL(MemStruct):
    fields = [
        ("hwnd", HWND()),
        ("hData", HANDLE()),
        ("hPrinterIcon", HICON()),
    ]

CLASSPIDL_PTR = Ptr("<I", CLASSPIDL())
_SSF_FLAGS_ = DWORD
_SHGNLI_FLAGS_ = UINT
SHARD = UINT
_SHGFI_FLAGS_ = UINT
_SHGSI_FLAGS_ = UINT
_SHUpdateImage_FLAGS_ = UINT
_SHDefExtractIcon_FLAGS_ = UINT
_MERGE_MENU_FLAGS_ = ULONG
_PPCF_FLAGS_ = DWORD
_PRF_FLAGS_ = UINT
_SHERB_FLAGS_ = DWORD
_OFASI_FLAGS_ = DWORD
_SHPPFW_FLAGS_ = DWORD

###################

###### Functions ######

def shell32_DuplicateIcon(jitter):
    """
    HICON DuplicateIcon(
        HINSTANCE hInst,
        HICON hIcon
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInst", "hIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ExtractAssociatedIcon(jitter, get_str, set_str):
    """
    HICON ExtractAssociatedIcon(
        HINSTANCE hInst,
        LPTSTR lpIconPath,
        LPWORD lpiIcon
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInst", "lpIconPath", "lpiIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ExtractAssociatedIconA(jitter):
    shell32_ExtractAssociatedIcon(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_ExtractAssociatedIconW(jitter):
    shell32_ExtractAssociatedIcon(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_ExtractIcon(jitter, get_str, set_str):
    """
    HICON ExtractIcon(
        HINSTANCE hInst,
        LPCTSTR lpszExeFileName,
        UINT nIconIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInst", "lpszExeFileName", "nIconIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ExtractIconA(jitter):
    shell32_ExtractIcon(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_ExtractIconW(jitter):
    shell32_ExtractIcon(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_ExtractIconEx(jitter, get_str, set_str):
    """
    UINT ExtractIconEx(
        LPCTSTR lpszFile,
        int nIconIndex,
        HICON* phiconLarge,
        HICON* phiconSmall,
        UINT nIcons
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFile", "nIconIndex", "phiconLarge", "phiconSmall", "nIcons"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ExtractIconExA(jitter):
    shell32_ExtractIconEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_ExtractIconExW(jitter):
    shell32_ExtractIconEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_AssocCreateForClasses(jitter):
    """
    HRESULT AssocCreateForClasses(
        const ASSOCIATIONELEMENT* rgClasses,
        ULONG cClasses,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rgClasses", "cClasses", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_AssocGetDetailsOfPropKey(jitter):
    """
    HRESULT AssocGetDetailsOfPropKey(
        IShellFolder* psf,
        PCUITEMID_CHILD pidl,
        PROPERTYKEY* pkey,
        VARIANT* pv,
        BOOL* pfFoundPropKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psf", "pidl", "pkey", "pv", "pfFoundPropKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CallCPLEntry16(jitter):
    """
    int CallCPLEntry16(
        HINSTANCE hInst,
        FARPROC16 lpfnEntry,
        HWND hwndCPL,
        UINT msg,
        LPARAM lParam1,
        LPARAM lParam2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInst", "lpfnEntry", "hwndCPL", "msg", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CDefFolderMenu_Create2(jitter):
    """
    HRESULT CDefFolderMenu_Create2(
        PCIDLIST_ABSOLUTE pidlFolder,
        HWND hwnd,
        UINT cidl,
        PCUITEMID_CHILD_ARRAY* apidl,
        IShellFolder* psf,
        LPFNDFMCALLBACK lpfn,
        UINT nKeys,
        const HKEY* ahkeys,
        IContextMenu** ppcm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlFolder", "hwnd", "cidl", "apidl", "psf", "lpfn", "nKeys", "ahkeys", "ppcm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CIDLData_CreateFromIDArray(jitter):
    """
    HRESULT CIDLData_CreateFromIDArray(
        PCIDLIST_ABSOLUTE pidlFolder,
        UINT cidl,
        PCUIDLIST_RELATIVE_ARRAY apidl,
        IDataObject** ppdtobj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlFolder", "cidl", "apidl", "ppdtobj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CommandLineToArgvW(jitter):
    """
    LPWSTR* CommandLineToArgvW(
        LPCWSTR lpCmdLine,
        int* pNumArgs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpCmdLine", "pNumArgs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DAD_AutoScroll(jitter):
    """
    BOOL DAD_AutoScroll(
        HWND hwnd,
        AUTO_SCROLL_DATA* pad,
        const POINT* pptNow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pad", "pptNow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DAD_DragEnterEx(jitter):
    """
    BOOL DAD_DragEnterEx(
        HWND hwndTarget,
        const POINT ptStart
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndTarget", "ptStart"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DAD_DragLeave(jitter):
    """
    BOOL DAD_DragLeave()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DAD_DragMove(jitter):
    """
    BOOL DAD_DragMove(
        POINT pt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DAD_SetDragImage(jitter):
    """
    BOOL DAD_SetDragImage(
        HIMAGELIST him,
        POINT* pptOffset
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["him", "pptOffset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DAD_ShowDragImage(jitter):
    """
    BOOL DAD_ShowDragImage(
        BOOL fShow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DoEnvironmentSubst(jitter, get_str, set_str):
    """
    DWORD DoEnvironmentSubst(
        LPTSTR pszString,
        UINT cchString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszString", "cchString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DoEnvironmentSubstA(jitter):
    shell32_DoEnvironmentSubst(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_DoEnvironmentSubstW(jitter):
    shell32_DoEnvironmentSubst(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_DragAcceptFiles(jitter):
    """
    VOID DragAcceptFiles(
        HWND hWnd,
        BOOL fAccept
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "fAccept"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DragFinish(jitter):
    """
    VOID DragFinish(
        HDROP hDrop
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDrop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DragQueryFile(jitter, get_str, set_str):
    """
    UINT DragQueryFile(
        HDROP hDrop,
        UINT iFile,
        LPTSTR lpszFile,
        UINT cch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDrop", "iFile", "lpszFile", "cch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DragQueryFileA(jitter):
    shell32_DragQueryFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_DragQueryFileW(jitter):
    shell32_DragQueryFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_DragQueryPoint(jitter):
    """
    BOOL DragQueryPoint(
        HDROP hDrop,
        LPPOINT lppt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDrop", "lppt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DriveType(jitter):
    """
    int DriveType(
        int iDrive
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["iDrive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ExtractAssociatedIconEx(jitter, get_str, set_str):
    """
    HICON ExtractAssociatedIconEx(
        HINSTANCE hInst,
        LPTSTR lpIconPath,
        LPWORD lpiIconIndex,
        LPWORD lpiIconId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInst", "lpIconPath", "lpiIconIndex", "lpiIconId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ExtractAssociatedIconExA(jitter):
    shell32_ExtractAssociatedIconEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_ExtractAssociatedIconExW(jitter):
    shell32_ExtractAssociatedIconEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_FileIconInit(jitter):
    """
    BOOL FileIconInit(
        BOOL fRestoreCache
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fRestoreCache"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_FindExecutable(jitter, get_str, set_str):
    """
    HINSTANCE FindExecutable(
        LPCTSTR lpFile,
        LPCTSTR lpDirectory,
        LPTSTR lpResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpFile", "lpDirectory", "lpResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_FindExecutableA(jitter):
    shell32_FindExecutable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_FindExecutableW(jitter):
    shell32_FindExecutable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_GetCurrentProcessExplicitAppUserModelID(jitter):
    """
    HRESULT GetCurrentProcessExplicitAppUserModelID(
        PWSTR* AppID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AppID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_GetFileNameFromBrowse(jitter):
    """
    BOOL GetFileNameFromBrowse(
        HWND hwnd,
        LPWSTR pszFilePath,
        UINT cchFilePath,
        LPCWSTR pszWorkingDir,
        LPCWSTR pszDefExt,
        LPCWSTR pszFilters,
        LPCWSTR szTitle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszFilePath", "cchFilePath", "pszWorkingDir", "pszDefExt", "pszFilters", "szTitle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_GUIDFromString(jitter, get_str, set_str):
    """
    BOOL GUIDFromString(
        LPCTSTR psz,
        LPGUID pguid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "pguid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_GUIDFromStringA(jitter):
    shell32_GUIDFromString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_GUIDFromStringW(jitter):
    shell32_GUIDFromString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_ILAppendID(jitter):
    """
    PIDLIST_RELATIVE ILAppendID(
        PIDLIST_RELATIVE pidl,
        LPSHITEMID pmkid,
        BOOL fAppend
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "pmkid", "fAppend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILClone(jitter):
    """
    PIDLIST_RELATIVE ILClone(
        PCUIDLIST_RELATIVE pidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILCloneFirst(jitter):
    """
    PITEMID_CHILD ILCloneFirst(
        PCUIDLIST_RELATIVE pidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILCombine(jitter):
    """
    PIDLIST_ABSOLUTE ILCombine(
        PCIDLIST_ABSOLUTE pidl1,
        PCUIDLIST_RELATIVE pidl2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl1", "pidl2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILCreateFromPath(jitter):
    """
    PIDLIST_ABSOLUTE ILCreateFromPath(
        LPCWSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILCreateFromPath(jitter, get_str, set_str):
    """
    PIDLIST_ABSOLUTE ILCreateFromPath(
        LPCSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILCreateFromPathA(jitter):
    shell32_ILCreateFromPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_ILCreateFromPathW(jitter):
    shell32_ILCreateFromPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_ILFindChild(jitter):
    """
    PUIDLIST_RELATIVE ILFindChild(
        PCIDLIST_ABSOLUTE pidlParent,
        PCIDLIST_ABSOLUTE pidlChild
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlParent", "pidlChild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILFindLastID(jitter):
    """
    PUITEMID_CHILD ILFindLastID(
        PCUIDLIST_RELATIVE pidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILFree(jitter):
    """
    void ILFree(
        PIDLIST_RELATIVE pidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILGetNext(jitter):
    """
    PUIDLIST_RELATIVE ILGetNext(
        PCUIDLIST_RELATIVE pidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILGetSize(jitter):
    """
    UINT ILGetSize(
        PCUIDLIST_RELATIVE pidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILIsEqual(jitter):
    """
    BOOL ILIsEqual(
        PCIDLIST_ABSOLUTE pidl1,
        PCIDLIST_ABSOLUTE pidl2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl1", "pidl2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILIsParent(jitter):
    """
    BOOL ILIsParent(
        PCIDLIST_ABSOLUTE pidl1,
        PCIDLIST_ABSOLUTE pidl2,
        BOOL fImmediate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl1", "pidl2", "fImmediate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILLoadFromStream(jitter):
    """
    HRESULT ILLoadFromStream(
        IStream* pstm,
        PIDLIST_RELATIVE* pidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILRemoveLastID(jitter):
    """
    BOOL ILRemoveLastID(
        PUIDLIST_RELATIVE pidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILSaveToStream(jitter):
    """
    HRESULT ILSaveToStream(
        IStream* pstm,
        PCUIDLIST_RELATIVE pidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_InitNetworkAddressControl(jitter):
    """
    BOOL InitNetworkAddressControl()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_IsNetDrive(jitter):
    """
    int IsNetDrive(
        int iDrive
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["iDrive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_IsUserAnAdmin(jitter):
    """
    BOOL IsUserAnAdmin()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_LinkWindow_RegisterClass(jitter):
    """
    BOOL LinkWindow_RegisterClass()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_LinkWindow_UnregisterClass(jitter):
    """
    BOOL LinkWindow_UnregisterClass()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_NTSHChangeNotifyDeregister(jitter):
    """
    BOOL NTSHChangeNotifyDeregister(
        ULONG ulID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHChangeNotify(jitter):
    """
    void SHChangeNotify(
        [ShellChangeNotifyEvent] wEventId,
        [ShellChangeNotifyFlag] uFlags,
        LPCVOID dwItem1,
        LPCVOID dwItem2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wEventId", "uFlags", "dwItem1", "dwItem2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_NTSHChangeNotifyRegister(jitter):
    """
    ULONG NTSHChangeNotifyRegister(
        HWND hwnd,
        int fSources,
        LONG fEvents,
        UINT wMsg,
        int cEntries,
        SHChangeNotifyEntry* pfsne
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "fSources", "fEvents", "wMsg", "cEntries", "pfsne"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_OpenRegStream(jitter):
    """
    IStream* OpenRegStream(
        HKEY hkey,
        LPCWSTR pszSubkey,
        LPCWSTR pszValue,
        [STGM_FLAGS] grfMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubkey", "pszValue", "grfMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ParseField(jitter):
    """
    bool ParseField(
        LPCTSTR* szData,
        int n,
        LPTSTR* szBuf,
        int iBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szData", "n", "szBuf", "iBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathCleanupSpec(jitter):
    """
    int PathCleanupSpec(
        LPCWSTR pszDir,
        LPWSTR pszSpec
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDir", "pszSpec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathGetShortPath(jitter):
    """
    void PathGetShortPath(
        LPWSTR pszLongPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszLongPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathIsExe(jitter):
    """
    int PathIsExe(
        LPCWSTR szfile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szfile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathIsSlow(jitter, get_str, set_str):
    """
    BOOL PathIsSlow(
        LPCTSTR pszFile,
        DWORD dwFileAttr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFile", "dwFileAttr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathIsSlowA(jitter):
    shell32_PathIsSlow(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_PathIsSlowW(jitter):
    shell32_PathIsSlow(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_PathMakeUniqueName(jitter):
    """
    BOOL PathMakeUniqueName(
        LPWSTR pszUniqueName,
        UINT cchMax,
        LPCWSTR pszTemplate,
        LPCWSTR pszLongPlate,
        LPCWSTR pszDir
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUniqueName", "cchMax", "pszTemplate", "pszLongPlate", "pszDir"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathProcessCommand(jitter):
    """
    LONG PathProcessCommand(
        LPCWSTR lpSrc,
        LPWSTR lpDest,
        int iDestMax,
        [PPCF_FLAGS] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpSrc", "lpDest", "iDestMax", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathResolve(jitter):
    """
    BOOL PathResolve(
        LPWSTR pszPath,
        LPCWSTR* dirs,
        [PRF_FLAGS] fFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "dirs", "fFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathYetAnotherMakeUniqueName(jitter):
    """
    BOOL PathYetAnotherMakeUniqueName(
        LPWSTR pszUniqueName,
        LPCWSTR pszPath,
        LPCWSTR pszShort,
        LPCWSTR pszFileSpec
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUniqueName", "pszPath", "pszShort", "pszFileSpec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PickIconDlg(jitter):
    """
    int PickIconDlg(
        HWND hwnd,
        LPWSTR pszIconPath,
        UINT cchIconPath,
        int* piIconIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszIconPath", "cchIconPath", "piIconIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ReadCabinetState(jitter):
    """
    BOOL ReadCabinetState(
        CABINETSTATE* pcs,
        int cLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcs", "cLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_RealDriveType(jitter):
    """
    int RealDriveType(
        int iDrive,
        BOOL fOKToHitNet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["iDrive", "fOKToHitNet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_RestartDialog(jitter):
    """
    int RestartDialog(
        HWND hParent,
        LPCWSTR pszPrompt,
        [EWX_FLAGS] dwReturn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hParent", "pszPrompt", "dwReturn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_RestartDialogEx(jitter):
    """
    int RestartDialogEx(
        HWND hParent,
        LPCWSTR pszPrompt,
        [EWX_FLAGS] dwReturn,
        [SHTDN_REASON] dwReasonCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hParent", "pszPrompt", "dwReturn", "dwReasonCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SetCurrentProcessExplicitAppUserModelID(jitter):
    """
    HRESULT SetCurrentProcessExplicitAppUserModelID(
        PCWSTR AppID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AppID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAddFromPropSheetExtArray(jitter):
    """
    int SHAddFromPropSheetExtArray(
        HPSXA hpsxa,
        LPFNADDPROPSHEETPAGE lpfnAddPage,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hpsxa", "lpfnAddPage", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAddToRecentDocs(jitter):
    """
    void SHAddToRecentDocs(
        SHARD uFlags,
        LPCVOID pv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uFlags", "pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAlloc(jitter):
    """
    LPVOID SHAlloc(
        SIZE_T cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAppBarMessage(jitter):
    """
    UINT_PTR SHAppBarMessage(
        DWORD dwMessage,
        PAPPBARDATA pData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwMessage", "pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAssocEnumHandlers(jitter):
    """
    HRESULT SHAssocEnumHandlers(
        LPCWSTR pszExtra,
        ASSOC_FILTER afFilter,
        IEnumAssocHandlers** ppEnumHandler
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszExtra", "afFilter", "ppEnumHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAssocEnumHandlersForProtocolByApplication(jitter):
    """
    HRESULT SHAssocEnumHandlersForProtocolByApplication(
        PCWSTR protocol,
        REFIID riid,
        void** enumHandlers
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["protocol", "riid", "enumHandlers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHBindToFolderIDListParent(jitter):
    """
    HRESULT SHBindToFolderIDListParent(
        IShellFolder* psfRoot,
        PCUIDLIST_RELATIVE pidl,
        REFIID riid,
        void** ppv,
        PCUITEMID_CHILD* ppidlLast
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psfRoot", "pidl", "riid", "ppv", "ppidlLast"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHBindToObject(jitter):
    """
    HRESULT SHBindToObject(
        IShellFolder* psf,
        PCUIDLIST_RELATIVE pidl,
        IBindCtx* pbc,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psf", "pidl", "pbc", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHBindToParent(jitter):
    """
    HRESULT SHBindToParent(
        PCIDLIST_ABSOLUTE pidl,
        REFIID riid,
        VOID** ppv,
        PCUITEMID_CHILD* ppidlLast
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "riid", "ppv", "ppidlLast"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHBrowseForFolder(jitter, get_str, set_str):
    """
    PIDLIST_ABSOLUTE SHBrowseForFolder(
        LPBROWSEINFO lpbi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpbi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHBrowseForFolderA(jitter):
    shell32_SHBrowseForFolder(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHBrowseForFolderW(jitter):
    shell32_SHBrowseForFolder(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHChangeNotification_Lock(jitter):
    """
    HANDLE SHChangeNotification_Lock(
        HANDLE hChange,
        DWORD dwProcId,
        PIDLIST_ABSOLUTE** pppidl,
        LONG* plEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hChange", "dwProcId", "pppidl", "plEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHChangeNotification_Unlock(jitter):
    """
    BOOL SHChangeNotification_Unlock(
        HANDLE hLock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHChangeNotifyDeregister(jitter):
    """
    BOOL SHChangeNotifyDeregister(
        ULONG ulID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHChangeNotifyRegister(jitter):
    """
    ULONG SHChangeNotifyRegister(
        HWND hwnd,
        int fSources,
        LONG fEvents,
        UINT wMsg,
        int cEntries,
        const SHChangeNotifyEntry* pshcne
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "fSources", "fEvents", "wMsg", "cEntries", "pshcne"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHChangeNotifyRegisterThread(jitter):
    """
    void SHChangeNotifyRegisterThread(
        SCNRT_STATUS status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCloneSpecialIDList(jitter):
    """
    PIDLIST_ABSOLUTE SHCloneSpecialIDList(
        HWND hwndOwner,
        [CSIDL] csidl,
        BOOL fCreate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "csidl", "fCreate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCLSIDFromString(jitter):
    """
    HRESULT SHCLSIDFromString(
        LPCWSTR psz,
        CLSID* pclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCoCreateInstance(jitter):
    """
    HRESULT SHCoCreateInstance(
        LPCWSTR pszCLSID,
        const CLSID* pclsid,
        IUnknown* pUnkOuter,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszCLSID", "pclsid", "pUnkOuter", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateAssociationRegistration(jitter):
    """
    HRESULT SHCreateAssociationRegistration(
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateDataObject(jitter):
    """
    HRESULT SHCreateDataObject(
        PCIDLIST_ABSOLUTE pidlFolder,
        UINT cidl,
        PCUITEMID_CHILD_ARRAY apidl,
        IDataObject* pdtInner,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlFolder", "cidl", "apidl", "pdtInner", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateDefaultContextMenu(jitter):
    """
    HRESULT SHCreateDefaultContextMenu(
        const DEFCONTEXTMENU* pdcm,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdcm", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateDefaultExtractIcon(jitter):
    """
    HRESULT SHCreateDefaultExtractIcon(
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateDefaultPropertiesOp(jitter):
    """
    HRESULT SHCreateDefaultPropertiesOp(
        IShellItem* psi,
        IFileOperation** ppFileOp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psi", "ppFileOp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateDirectory(jitter):
    """
    int SHCreateDirectory(
        HWND hwnd,
        LPCWSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateDirectoryEx(jitter, get_str, set_str):
    """
    int SHCreateDirectoryEx(
        HWND hwnd,
        LPCTSTR pszPath,
        const SECURITY_ATTRIBUTES* psa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszPath", "psa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateDirectoryExA(jitter):
    shell32_SHCreateDirectoryEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHCreateDirectoryExW(jitter):
    shell32_SHCreateDirectoryEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHCreateFileExtractIconW(jitter):
    """
    HRESULT SHCreateFileExtractIconW(
        LPCWSTR pszFile,
        [FileAttributes] dwFileAttributes,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFile", "dwFileAttributes", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateItemFromParsingName(jitter):
    """
    HRESULT SHCreateItemFromParsingName(
        PCWSTR pszPath,
        IBindCtx* pbc,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pbc", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateItemFromRelativeName(jitter):
    """
    HRESULT SHCreateItemFromRelativeName(
        IShellItem* psiParent,
        PCWSTR pszName,
        IBindCtx* pbc,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psiParent", "pszName", "pbc", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateItemInKnownFolder(jitter):
    """
    HRESULT SHCreateItemInKnownFolder(
        REFKNOWNFOLDERID kfid,
        [KNOWN_FOLDER_FLAG|DWORD] dwKFFlags,
        PCWSTR pszItem,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["kfid", "dwKFFlags", "pszItem", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateProcessAsUserW(jitter):
    """
    BOOL SHCreateProcessAsUserW(
        PSHCREATEPROCESSINFOW pscpi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pscpi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreatePropSheetExtArray(jitter):
    """
    HPSXA SHCreatePropSheetExtArray(
        HKEY hkey,
        LPCWSTR pszSubkey,
        UINT max_iface
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubkey", "max_iface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateQueryCancelAutoPlayMoniker(jitter):
    """
    HRESULT SHCreateQueryCancelAutoPlayMoniker(
        IMoniker** ppmoniker
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppmoniker"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellFolderViewEx(jitter):
    """
    HRESULT SHCreateShellFolderViewEx(
        LPCSFV pcsfv,
        IShellView** ppsv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcsfv", "ppsv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellFolderView(jitter):
    """
    HRESULT SHCreateShellFolderView(
        const SFV_CREATE* pcsfv,
        IShellView** ppsv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcsfv", "ppsv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellItem(jitter):
    """
    HRESULT SHCreateShellItem(
        PCIDLIST_ABSOLUTE pidlParent,
        IShellFolder* psfParent,
        PCUITEMID_CHILD pidl,
        IShellItem** ppsi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlParent", "psfParent", "pidl", "ppsi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateItemWithParent(jitter):
    """
    HRESULT SHCreateItemWithParent(
        PCIDLIST_ABSOLUTE pidlParent,
        IShellFolder* psfParent,
        PCUITEMID_CHILD pidl,
        REFIID riid,
        void** ppvItem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlParent", "psfParent", "pidl", "riid", "ppvItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateItemFromIDList(jitter):
    """
    HRESULT SHCreateItemFromIDList(
        PCIDLIST_ABSOLUTE pidl,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellItemArray(jitter):
    """
    HRESULT SHCreateShellItemArray(
        PCIDLIST_ABSOLUTE pidlParent,
        IShellFolder* psf,
        UINT cidl,
        PCUITEMID_CHILD_ARRAY ppidl,
        IShellItemArray** ppsiItemArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlParent", "psf", "cidl", "ppidl", "ppsiItemArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellItemArrayFromDataObject(jitter):
    """
    HRESULT SHCreateShellItemArrayFromDataObject(
        IDataObject* pdo,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdo", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellItemArrayFromIDLists(jitter):
    """
    HRESULT SHCreateShellItemArrayFromIDLists(
        UINT cidl,
        PCIDLIST_ABSOLUTE_ARRAY rgpidl,
        IShellItemArray** ppsiItemArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cidl", "rgpidl", "ppsiItemArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellItemArrayFromShellItem(jitter):
    """
    HRESULT SHCreateShellItemArrayFromShellItem(
        IShellItem* psi,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psi", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateStdEnumFmtEtc(jitter):
    """
    HRESULT SHCreateStdEnumFmtEtc(
        UINT cfmt,
        const FORMATETC [] afmt,
        IEnumFORMATETC** ppenumFormatEtc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cfmt", "afmt", "ppenumFormatEtc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHDefExtractIcon(jitter, get_str, set_str):
    """
    HRESULT SHDefExtractIcon(
        LPCTSTR pszIconFile,
        int iIndex,
        [SHDefExtractIcon_FLAGS] uFlags,
        HICON* phiconLarge,
        HICON* phiconSmall,
        UINT nIconSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszIconFile", "iIndex", "uFlags", "phiconLarge", "phiconSmall", "nIconSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHDefExtractIconA(jitter):
    shell32_SHDefExtractIcon(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHDefExtractIconW(jitter):
    shell32_SHDefExtractIcon(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHDestroyPropSheetExtArray(jitter):
    """
    void SHDestroyPropSheetExtArray(
        HPSXA hpsxa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hpsxa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHDoDragDrop(jitter):
    """
    HRESULT SHDoDragDrop(
        HWND hwnd,
        IDataObject* pdtobj,
        IDropSource* pdsrc,
        DWORD dwEffect,
        DWORD* pdwEffect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pdtobj", "pdsrc", "dwEffect", "pdwEffect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Shell_GetCachedImageIndex(jitter):
    """
    int Shell_GetCachedImageIndex(
        LPCWSTR pwszIconPath,
        int iIconIndex,
        UINT uIconFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszIconPath", "iIconIndex", "uIconFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Shell_GetCachedImageIndex(jitter, get_str, set_str):
    """
    int Shell_GetCachedImageIndex(
        LPCTSTR pszIconPath,
        int iIconIndex,
        UINT uIconFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszIconPath", "iIconIndex", "uIconFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Shell_GetCachedImageIndexA(jitter):
    shell32_Shell_GetCachedImageIndex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_Shell_GetCachedImageIndexW(jitter):
    shell32_Shell_GetCachedImageIndex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_Shell_GetImageLists(jitter):
    """
    BOOL Shell_GetImageLists(
        HIMAGELIST* phiml,
        HIMAGELIST* phimlSmall
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phiml", "phimlSmall"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Shell_MergeMenus(jitter):
    """
    UINT Shell_MergeMenus(
        HMENU hmDst,
        HMENU hmSrc,
        UINT uInsert,
        UINT uIDAdjust,
        UINT uIDAdjustMax,
        [MERGE_MENU_FLAGS] uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmDst", "hmSrc", "uInsert", "uIDAdjust", "uIDAdjustMax", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Shell_NotifyIcon(jitter, get_str, set_str):
    """
    BOOL Shell_NotifyIcon(
        DWORD dwMessage,
        PNOTIFYICONDATA lpdata
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwMessage", "lpdata"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Shell_NotifyIconA(jitter):
    shell32_Shell_NotifyIcon(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_Shell_NotifyIconW(jitter):
    shell32_Shell_NotifyIcon(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_Shell_NotifyIconGetRect(jitter):
    """
    HRESULT Shell_NotifyIconGetRect(
        const NOTIFYICONIDENTIFIER* identifier,
        RECT* iconLocation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["identifier", "iconLocation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ShellAbout(jitter, get_str, set_str):
    """
    int ShellAbout(
        HWND hWnd,
        LPCTSTR szApp,
        LPCTSTR szOtherStuff,
        HICON hIcon
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "szApp", "szOtherStuff", "hIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ShellAboutA(jitter):
    shell32_ShellAbout(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_ShellAboutW(jitter):
    shell32_ShellAbout(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_ShellExecuteEx(jitter, get_str, set_str):
    """
    BOOL ShellExecuteEx(
        LPSHELLEXECUTEINFO lpExecInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpExecInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ShellExecuteExA(jitter):
    shell32_ShellExecuteEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_ShellExecuteExW(jitter):
    shell32_ShellExecuteEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHEmptyRecycleBin(jitter, get_str, set_str):
    """
    HRESULT SHEmptyRecycleBin(
        HWND hwnd,
        LPCTSTR pszRootPath,
        [SHERB_FLAGS] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszRootPath", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHEmptyRecycleBinA(jitter):
    shell32_SHEmptyRecycleBin(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHEmptyRecycleBinW(jitter):
    shell32_SHEmptyRecycleBin(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHEnumerateUnreadMailAccountsW(jitter):
    """
    HRESULT SHEnumerateUnreadMailAccountsW(
        HKEY hKeyUser,
        DWORD dwIndex,
        LPWSTR pszMailAddress,
        int cchMailAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKeyUser", "dwIndex", "pszMailAddress", "cchMailAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHEvaluateSystemCommandTemplate(jitter):
    """
    HRESULT SHEvaluateSystemCommandTemplate(
        PCWSTR pszCmdTemplate,
        PWSTR* ppszApplication,
        PWSTR* ppszCommandLine,
        PWSTR* ppszParameters
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszCmdTemplate", "ppszApplication", "ppszCommandLine", "ppszParameters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ShellExecute(jitter, get_str, set_str):
    """
    HINSTANCE ShellExecute(
        HWND hwnd,
        LPCTSTR lpOperation,
        LPCTSTR lpFile,
        LPCTSTR lpParameters,
        LPCTSTR lpDirectory,
        [ShowWindowCmd] nShowCmd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpOperation", "lpFile", "lpParameters", "lpDirectory", "nShowCmd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ShellExecuteA(jitter):
    shell32_ShellExecute(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_ShellExecuteW(jitter):
    shell32_ShellExecute(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHExtractIconsW(jitter):
    """
    UINT SHExtractIconsW(
        LPCWSTR pszFileName,
        int nIconIndex,
        int cxIcon,
        int cyIcon,
        HICON* phIcon,
        UINT* pIconId,
        UINT nIcons,
        [LRFlags] flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFileName", "nIconIndex", "cxIcon", "cyIcon", "phIcon", "pIconId", "nIcons", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFind_InitMenuPopup(jitter):
    """
    IContextMenu* SHFind_InitMenuPopup(
        HMENU hmenu,
        HWND hwnd,
        UINT idCmdFirst,
        UINT idCmdLast
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "hwnd", "idCmdFirst", "idCmdLast"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFindFiles(jitter):
    """
    BOOL SHFindFiles(
        PCIDLIST_ABSOLUTE pidlFolder,
        PCIDLIST_ABSOLUTE pidlSaveFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlFolder", "pidlSaveFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFlushClipboard(jitter):
    """
    HRESULT SHFlushClipboard()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFlushSFCache(jitter):
    """
    void SHFlushSFCache()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFormatDrive(jitter):
    """
    DWORD SHFormatDrive(
        HWND hwnd,
        UINT drive,
        UINT fmtID,
        UINT options
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "drive", "fmtID", "options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFree(jitter):
    """
    void SHFree(
        void* pv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFreeNameMappings(jitter):
    """
    void SHFreeNameMappings(
        HANDLE hNameMappings
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hNameMappings"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFileOperation(jitter, get_str, set_str):
    """
    int SHFileOperation(
        LPSHFILEOPSTRUCT lpFileOp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpFileOp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFileOperationA(jitter):
    shell32_SHFileOperation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHFileOperationW(jitter):
    shell32_SHFileOperation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHGetAttributesFromDataObject(jitter):
    """
    HRESULT SHGetAttributesFromDataObject(
        IDataObject* pdo,
        [SFGAOF_DWORD] dwAttributeMask,
        [SFGAOF_DWORD*] pdwAttributes,
        UINT* pcItems
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdo", "dwAttributeMask", "pdwAttributes", "pcItems"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetDataFromIDList(jitter, get_str, set_str):
    """
    HRESULT SHGetDataFromIDList(
        IShellFolder* psf,
        PCUITEMID_CHILD pidl,
        [SHGetDataFromIDListFormats] nFormat,
        PVOID pv,
        int cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psf", "pidl", "nFormat", "pv", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetDataFromIDListA(jitter):
    shell32_SHGetDataFromIDList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHGetDataFromIDListW(jitter):
    shell32_SHGetDataFromIDList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHGetDesktopFolder(jitter):
    """
    HRESULT SHGetDesktopFolder(
        IShellFolder** ppshf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppshf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetDiskFreeSpace(jitter, get_str, set_str):
    """
    BOOL SHGetDiskFreeSpace(
        LPCTSTR pszVolume,
        ULARGE_INTEGER* pqwFreeCaller,
        ULARGE_INTEGER* pqwTot,
        ULARGE_INTEGER* pqwFree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszVolume", "pqwFreeCaller", "pqwTot", "pqwFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetDiskFreeSpaceA(jitter):
    shell32_SHGetDiskFreeSpace(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHGetDiskFreeSpaceW(jitter):
    shell32_SHGetDiskFreeSpace(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHGetDiskFreeSpaceEx(jitter, get_str, set_str):
    """
    BOOL SHGetDiskFreeSpaceEx(
        LPCTSTR pszVolume,
        ULARGE_INTEGER* pqwFreeCaller,
        ULARGE_INTEGER* pqwTot,
        ULARGE_INTEGER* pqwFree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszVolume", "pqwFreeCaller", "pqwTot", "pqwFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetDiskFreeSpaceExA(jitter):
    shell32_SHGetDiskFreeSpaceEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHGetDiskFreeSpaceExW(jitter):
    shell32_SHGetDiskFreeSpaceEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHGetDriveMedia(jitter):
    """
    HRESULT SHGetDriveMedia(
        LPCWSTR pszDrive,
        DWORD* pdwMediaContent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDrive", "pdwMediaContent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetFileInfo(jitter, get_str, set_str):
    """
    DWORD_PTR SHGetFileInfo(
        LPCTSTR pszPath,
        [FileAttributes] dwFileAttributes,
        SHFILEINFO* psfi,
        UINT cbFileInfo,
        [SHGFI_FLAGS] uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "dwFileAttributes", "psfi", "cbFileInfo", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetFileInfoA(jitter):
    shell32_SHGetFileInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHGetFileInfoW(jitter):
    shell32_SHGetFileInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHGetFolderLocation(jitter):
    """
    HRESULT SHGetFolderLocation(
        HWND hwndOwner,
        [CSIDL] nFolder,
        HANDLE hToken,
        DWORD dwReserved,
        PIDLIST_ABSOLUTE* ppidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "nFolder", "hToken", "dwReserved", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetFolderPath(jitter, get_str, set_str):
    """
    HRESULT SHGetFolderPath(
        HWND hwndOwner,
        int nFolder,
        HANDLE hToken,
        [SHGetFolderPathFlags] dwFlags,
        LPTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "nFolder", "hToken", "dwFlags", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetFolderPathA(jitter):
    shell32_SHGetFolderPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHGetFolderPathW(jitter):
    shell32_SHGetFolderPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHGetFolderPathAndSubDir(jitter, get_str, set_str):
    """
    HRESULT SHGetFolderPathAndSubDir(
        HWND hwnd,
        [CSIDL] csidl,
        HANDLE hToken,
        [SHGetFolderPathFlags] dwFlags,
        LPCTSTR pszSubDir,
        LPTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "csidl", "hToken", "dwFlags", "pszSubDir", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetFolderPathAndSubDirA(jitter):
    shell32_SHGetFolderPathAndSubDir(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHGetFolderPathAndSubDirW(jitter):
    shell32_SHGetFolderPathAndSubDir(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHGetIconOverlayIndex(jitter, get_str, set_str):
    """
    int SHGetIconOverlayIndex(
        LPCTSTR pszIconPath,
        int iIconIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszIconPath", "iIconIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetIconOverlayIndexA(jitter):
    shell32_SHGetIconOverlayIndex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHGetIconOverlayIndexW(jitter):
    shell32_SHGetIconOverlayIndex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHGetIDListFromObject(jitter):
    """
    HRESULT SHGetIDListFromObject(
        IUnknown* punk,
        PIDLIST_ABSOLUTE* ppidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetImageList(jitter):
    """
    HRESULT SHGetImageList(
        int iImageList,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["iImageList", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetInstanceExplorer(jitter):
    """
    HRESULT SHGetInstanceExplorer(
        IUnknown** ppunk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppunk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetItemFromDataObject(jitter):
    """
    HRESULT SHGetItemFromDataObject(
        IDataObject* pdtobj,
        DATAOBJ_GET_ITEM_FLAGS dwFlags,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdtobj", "dwFlags", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetItemFromObject(jitter):
    """
    HRESULT SHGetItemFromObject(
        IUnknown* punk,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetKnownFolderIDList(jitter):
    """
    HRESULT SHGetKnownFolderIDList(
        REFKNOWNFOLDERID rfid,
        [KNOWN_FOLDER_FLAG|DWORD] dwFlags,
        HANDLE hToken,
        PIDLIST_ABSOLUTE* ppidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rfid", "dwFlags", "hToken", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetKnownFolderItem(jitter):
    """
    HRESULT SHGetKnownFolderItem(
        REFKNOWNFOLDERID rfid,
        KNOWN_FOLDER_FLAG dwFlags,
        HANDLE hToken,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rfid", "dwFlags", "hToken", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetKnownFolderPath(jitter):
    """
    HRESULT SHGetKnownFolderPath(
        REFKNOWNFOLDERID rfid,
        [KNOWN_FOLDER_FLAG|DWORD] dwFlags,
        HANDLE hToken,
        PWSTR* ppszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rfid", "dwFlags", "hToken", "ppszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetLocalizedName(jitter):
    """
    HRESULT SHGetLocalizedName(
        LPCWSTR pszPath,
        LPWSTR pszResModule,
        UINT cch,
        int* pidsRes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszResModule", "cch", "pidsRes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetMalloc(jitter):
    """
    HRESULT SHGetMalloc(
        LPMALLOC* ppMalloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppMalloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetNameFromIDList(jitter):
    """
    HRESULT SHGetNameFromIDList(
        PCIDLIST_ABSOLUTE pidl,
        SIGDN sigdnName,
        PWSTR* ppszName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "sigdnName", "ppszName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetNameFromPropertyKey(jitter):
    """
    HRESULT SHGetNameFromPropertyKey(
        REFPROPERTYKEY propkey,
        PWSTR* ppszCanonicalName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["propkey", "ppszCanonicalName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetNewLinkInfo(jitter, get_str, set_str):
    """
    BOOL SHGetNewLinkInfo(
        LPCTSTR pszLinkTo,
        LPCTSTR pszDir,
        LPTSTR pszName,
        BOOL* pfMustCopy,
        [SHGNLI_FLAGS] uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszLinkTo", "pszDir", "pszName", "pfMustCopy", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetNewLinkInfoA(jitter):
    shell32_SHGetNewLinkInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHGetNewLinkInfoW(jitter):
    shell32_SHGetNewLinkInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHGetPathFromIDListEx(jitter):
    """
    BOOL SHGetPathFromIDListEx(
        PCIDLIST_ABSOLUTE pidl,
        PWSTR pszPath,
        DWORD cchPath,
        GPFIDL_FLAGS uOpts
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "pszPath", "cchPath", "uOpts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetPathFromIDList(jitter, get_str, set_str):
    """
    BOOL SHGetPathFromIDList(
        PCIDLIST_ABSOLUTE pidl,
        LPTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetPathFromIDListA(jitter):
    shell32_SHGetPathFromIDList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHGetPathFromIDListW(jitter):
    shell32_SHGetPathFromIDList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHGetRealIDL(jitter):
    """
    HRESULT SHGetRealIDL(
        IShellFolder* psf,
        PCUITEMID_CHILD pidlSimple,
        PITEMID_CHILD* ppidlReal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psf", "pidlSimple", "ppidlReal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetSetFolderCustomSettings(jitter):
    """
    HRESULT SHGetSetFolderCustomSettings(
        LPSHFOLDERCUSTOMSETTINGS pfcs,
        LPCTSTR pszPath,
        DWORD dwReadWrite
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfcs", "pszPath", "dwReadWrite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetSetSettings(jitter):
    """
    void SHGetSetSettings(
        LPSHELLSTATE lpss,
        [SSF_FLAGS] dwMask,
        BOOL bSet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpss", "dwMask", "bSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetSettings(jitter):
    """
    void SHGetSettings(
        LPSHELLFLAGSTATE lpsfs,
        [SSF_FLAGS] dwMask
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpsfs", "dwMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetShellStyleHInstance(jitter):
    """
    HINSTANCE SHGetShellStyleHInstance()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetSpecialFolderLocation(jitter):
    """
    HRESULT SHGetSpecialFolderLocation(
        HWND hwndOwner,
        [CSIDL] nFolder,
        PIDLIST_ABSOLUTE* ppidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "nFolder", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetSpecialFolderPath(jitter):
    """
    BOOL SHGetSpecialFolderPath(
        HWND hwndOwner,
        LPWSTR lpwszPath,
        [CSIDL] csidl,
        BOOL fCreate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "lpwszPath", "csidl", "fCreate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetSpecialFolderPath(jitter, get_str, set_str):
    """
    BOOL SHGetSpecialFolderPath(
        HWND hwndOwner,
        LPTSTR lpszPath,
        [CSIDL] csidl,
        BOOL fCreate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "lpszPath", "csidl", "fCreate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetSpecialFolderPathA(jitter):
    shell32_SHGetSpecialFolderPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHGetSpecialFolderPathW(jitter):
    shell32_SHGetSpecialFolderPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHGetStockIconInfo(jitter):
    """
    HRESULT SHGetStockIconInfo(
        SHSTOCKICONID siid,
        [SHGSI_FLAGS] uFlags,
        SHSTOCKICONINFO* psii
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["siid", "uFlags", "psii"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetTemporaryPropertyForItem(jitter):
    """
    HRESULT SHGetTemporaryPropertyForItem(
        IShellItem* psi,
        REFPROPERTYKEY pk,
        PROPVARIANT* ppropvarInk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psi", "pk", "ppropvarInk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetUnreadMailCountW(jitter):
    """
    HRESULT SHGetUnreadMailCountW(
        HKEY hKeyUser,
        LPCWSTR pszMailAddress,
        DWORD* pdwCount,
        FILETIME* pFileTime,
        LPCWSTR pszShellExecuteCommand,
        int cchShellExecuteCommand
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKeyUser", "pszMailAddress", "pdwCount", "pFileTime", "pszShellExecuteCommand", "cchShellExecuteCommand"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHHandleUpdateImage(jitter):
    """
    int SHHandleUpdateImage(
        PCIDLIST_ABSOLUTE pidlExtra
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlExtra"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHILCreateFromPath(jitter):
    """
    HRESULT SHILCreateFromPath(
        LPCWSTR pszPath,
        PIDLIST_ABSOLUTE* ppidl,
        DWORD* rgflnOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "ppidl", "rgflnOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHInvokePrinterCommand(jitter, get_str, set_str):
    """
    BOOL SHInvokePrinterCommand(
        HWND hwnd,
        UINT uAction,
        LPCTSTR lpBuf1,
        LPCTSTR lpBuf2,
        BOOL fModal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "uAction", "lpBuf1", "lpBuf2", "fModal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHInvokePrinterCommandA(jitter):
    shell32_SHInvokePrinterCommand(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHInvokePrinterCommandW(jitter):
    shell32_SHInvokePrinterCommand(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHIsFileAvailableOffline(jitter):
    """
    HRESULT SHIsFileAvailableOffline(
        LPCWSTR pszPath,
        LPDWORD pdwStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pdwStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHLimitInputEdit(jitter):
    """
    HRESULT SHLimitInputEdit(
        HWND hwndEdit,
        IShellFolder* psf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndEdit", "psf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHLoadInProc(jitter):
    """
    HRESULT SHLoadInProc(
        REFCLSID rclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHLoadNonloadedIconOverlayIdentifiers(jitter):
    """
    HRESULT SHLoadNonloadedIconOverlayIdentifiers()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHLoadOLE(jitter):
    """
    HRESULT SHLoadOLE(
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHLocalStrDup(jitter, get_str, set_str):
    """
    HRESULT SHLocalStrDup(
        LPCWSTR psz,
        LPWSTR* ppsz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "ppsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHLocalStrDupA(jitter):
    shell32_SHLocalStrDup(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHLocalStrDupW(jitter):
    shell32_SHLocalStrDup(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHMapIDListToImageListIndexAsync(jitter):
    """
    HRESULT SHMapIDListToImageListIndexAsync(
        IShellTaskScheduler* pts,
        IShellFolder* psf,
        LPCITEMIDLIST pidl,
        [GIL_INPUT_FLAGS] flags,
        PFNASYNCICONTASKBALLBACK pfn,
        void* pvData,
        void* pvHint,
        int* piIndex,
        int* piIndexSel
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pts", "psf", "pidl", "flags", "pfn", "pvData", "pvHint", "piIndex", "piIndexSel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHMapPIDLToSystemImageListIndex(jitter):
    """
    int SHMapPIDLToSystemImageListIndex(
        IShellFolder* psf,
        PCUITEMID_CHILD pidl,
        int* piIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psf", "pidl", "piIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHMultiFileProperties(jitter):
    """
    HRESULT SHMultiFileProperties(
        IDataObject* pdtobj,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdtobj", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHObjectProperties(jitter):
    """
    BOOL SHObjectProperties(
        HWND hwnd,
        DWORD shopObjectType,
        PCWSTR pszObjectName,
        PCWSTR pszPropertyPage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "shopObjectType", "pszObjectName", "pszPropertyPage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHOpenFolderAndSelectItems(jitter):
    """
    HRESULT SHOpenFolderAndSelectItems(
        PCIDLIST_ABSOLUTE pidlFolder,
        UINT cidl,
        PCUITEMID_CHILD_ARRAY* apidl,
        [OFASI_FLAGS] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlFolder", "cidl", "apidl", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHOpenPropSheetW(jitter):
    """
    BOOL SHOpenPropSheetW(
        LPCWSTR pszCaption,
        HKEY [] ahkeys,
        UINT ckeys,
        const CLSID* pclsidDef,
        IDataObject* pdtobj,
        IShellBrowser* psb,
        LPCWSTR pStartPage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszCaption", "ahkeys", "ckeys", "pclsidDef", "pdtobj", "psb", "pStartPage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHOpenWithDialog(jitter):
    """
    HRESULT SHOpenWithDialog(
        HWND hwndParent,
        const OPENASINFO* poainfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "poainfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHParseDisplayName(jitter):
    """
    HRESULT SHParseDisplayName(
        LPCWSTR pszName,
        IBindCtx* pbc,
        PIDLIST_ABSOLUTE* ppidl,
        SFGAOF sfgaoIn,
        SFGAOF* psfgaoOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszName", "pbc", "ppidl", "sfgaoIn", "psfgaoOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHPathPrepareForWrite(jitter, get_str, set_str):
    """
    HRESULT SHPathPrepareForWrite(
        HWND hwnd,
        IUnknown* punkEnableModless,
        LPCTSTR pszPath,
        [SHPPFW_FLAGS] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "punkEnableModless", "pszPath", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHPathPrepareForWriteA(jitter):
    shell32_SHPathPrepareForWrite(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHPathPrepareForWriteW(jitter):
    shell32_SHPathPrepareForWrite(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHQueryRecycleBin(jitter, get_str, set_str):
    """
    HRESULT SHQueryRecycleBin(
        LPCTSTR pszRootPath,
        LPSHQUERYRBINFO pSHQueryRBInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszRootPath", "pSHQueryRBInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHQueryRecycleBinA(jitter):
    shell32_SHQueryRecycleBin(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHQueryRecycleBinW(jitter):
    shell32_SHQueryRecycleBin(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHQueryUserNotificationState(jitter):
    """
    HRESULT SHQueryUserNotificationState(
        QUERY_USER_NOTIFICATION_STATE* pquns
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pquns"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHRemoveLocalizedName(jitter):
    """
    HRESULT SHRemoveLocalizedName(
        LPCWSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHReplaceFromPropSheetExtArray(jitter):
    """
    UINT SHReplaceFromPropSheetExtArray(
        HPSXA hpsxa,
        UINT uPageID,
        LPFNADDPROPSHEETPAGE lpfnReplaceWith,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hpsxa", "uPageID", "lpfnReplaceWith", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHResolveLibrary(jitter):
    """
    HRESULT SHResolveLibrary(
        IShellItem* psiLibrary
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psiLibrary"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHRestricted(jitter):
    """
    DWORD SHRestricted(
        RESTRICTIONS rest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHRunControlPanel(jitter):
    """
    BOOL SHRunControlPanel(
        LPCWSTR lpcszCmdLine,
        HWND hwndMsgParent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpcszCmdLine", "hwndMsgParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSetDefaultProperties(jitter):
    """
    HRESULT SHSetDefaultProperties(
        HWND hwnd,
        IShellItem* psi,
        [FILEOP_FLAGS_DWORD] dwFileOpFlags,
        IFileOperationProgressSink* pfops
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "psi", "dwFileOpFlags", "pfops"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSetFolderPath(jitter, get_str, set_str):
    """
    HRESULT SHSetFolderPath(
        [CSIDL] csidl,
        HANDLE hToken,
        DWORD dwFlags,
        LPCTSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["csidl", "hToken", "dwFlags", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSetFolderPathA(jitter):
    shell32_SHSetFolderPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHSetFolderPathW(jitter):
    shell32_SHSetFolderPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHSetInstanceExplorer(jitter):
    """
    void SHSetInstanceExplorer(
        IUnknown* punk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSetKnownFolderPath(jitter):
    """
    HRESULT SHSetKnownFolderPath(
        REFKNOWNFOLDERID rfid,
        [KNOWN_FOLDER_FLAG|DWORD] dwFlags,
        HANDLE hToken,
        PCWSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rfid", "dwFlags", "hToken", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSetLocalizedName(jitter):
    """
    HRESULT SHSetLocalizedName(
        LPCWSTR pszPath,
        LPCWSTR pszResModule,
        int idsRes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszResModule", "idsRes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSetTemporaryPropertyForItem(jitter):
    """
    HRESULT SHSetTemporaryPropertyForItem(
        IShellItem* psi,
        REFPROPERTYKEY propkey,
        REFPROPVARIANT propvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psi", "propkey", "propvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSetUnreadMailCountW(jitter):
    """
    HRESULT SHSetUnreadMailCountW(
        LPCWSTR pszMailAddress,
        DWORD dwCount,
        LPCWSTR pszShellExecuteCommand
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszMailAddress", "dwCount", "pszShellExecuteCommand"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHShellFolderView_Message(jitter):
    """
    LRESULT SHShellFolderView_Message(
        HWND hwnd,
        UINT uMsg,
        LPARAM lparam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "uMsg", "lparam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHShowManageLibraryUI(jitter):
    """
    HRESULT SHShowManageLibraryUI(
        IShellItem* psiLibrary,
        HWND hwndOwner,
        LPCWSTR pszTitle,
        LPCWSTR pszInstruction,
        LIBRARYMANAGEDIALOGOPTIONS lmdOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psiLibrary", "hwndOwner", "pszTitle", "pszInstruction", "lmdOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSimpleIDListFromPath(jitter):
    """
    PIDLIST_ABSOLUTE SHSimpleIDListFromPath(
        LPCWSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHStartNetConnectionDialogW(jitter):
    """
    HRESULT SHStartNetConnectionDialogW(
        HWND hwnd,
        LPCWSTR pszRemoteName,
        DWORD dwType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszRemoteName", "dwType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHTestTokenMembership(jitter):
    """
    BOOL SHTestTokenMembership(
        HANDLE hToken,
        ULONG ulRID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hToken", "ulRID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHUpdateImage(jitter, get_str, set_str):
    """
    void SHUpdateImage(
        LPCTSTR pszHashItem,
        int iIndex,
        [SHUpdateImage_FLAGS] uFlags,
        int iImageIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszHashItem", "iIndex", "uFlags", "iImageIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHUpdateImageA(jitter):
    shell32_SHUpdateImage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHUpdateImageW(jitter):
    shell32_SHUpdateImage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHValidateUNC(jitter):
    """
    BOOL SHValidateUNC(
        HWND hwndOwner,
        LPWSTR pszFile,
        UINT fConnect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "pszFile", "fConnect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SignalFileOpen(jitter):
    """
    BOOL SignalFileOpen(
        PCIDLIST_ABSOLUTE pidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_StgMakeUniqueName(jitter):
    """
    HRESULT StgMakeUniqueName(
        IStorage* pstgParent,
        PCWSTR pszFileSpec,
        [STGM_FLAGS] grfMode,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstgParent", "pszFileSpec", "grfMode", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Win32DeleteFile(jitter):
    """
    BOOL Win32DeleteFile(
        LPCTSTR pszFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_WOWShellExecute(jitter):
    """
    HINSTANCE WOWShellExecute(
        HWND hwnd,
        LPCTSTR lpOperation,
        LPCTSTR lpFile,
        LPCTSTR lpParameters,
        LPCTSTR lpDirectory,
        [ShowWindowCmd] nShowCmd,
        void* lpfnCBWinExec
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpOperation", "lpFile", "lpParameters", "lpDirectory", "nShowCmd", "lpfnCBWinExec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_WriteCabinetState(jitter):
    """
    BOOL WriteCabinetState(
        CABINETSTATE* pcs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_RunFileDlg(jitter):
    """
    VOID RunFileDlg(
        HWND hwndOwner,
        HICON hIcon,
        LPCWSTR lpszDirectory,
        LPCWSTR lpszTitle,
        LPCWSTR lpszDescription,
        [RunFileDlgFlags] uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "hIcon", "lpszDirectory", "lpszTitle", "lpszDescription", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_StrRetToStrN(jitter):
    """
    BOOL StrRetToStrN(
        LPTSTR pszOut,
        UINT cchOut,
        LPSTRRET pStrRet,
        LPCITEMIDLIST pidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszOut", "cchOut", "pStrRet", "pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PifMgr_CloseProperties(jitter):
    """
    int PifMgr_CloseProperties(
        HANDLE hProps,
        UINT flOpt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProps", "flOpt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PifMgr_OpenProperties(jitter):
    """
    HANDLE PifMgr_OpenProperties(
        LPCWSTR pszApp,
        LPCWSTR lpszPIF,
        UINT hInf,
        UINT flOpt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszApp", "lpszPIF", "hInf", "flOpt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PifMgr_GetProperties(jitter):
    """
    int PifMgr_GetProperties(
        HANDLE hProps,
        LPCSTR pszGroup,
        VOID* lpProps,
        int cbProps,
        UINT flOpt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProps", "pszGroup", "lpProps", "cbProps", "flOpt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PifMgr_SetProperties(jitter):
    """
    int PifMgr_SetProperties(
        HANDLE hProps,
        LPCSTR pszGroup,
        VOID* lpProps,
        int cbProps,
        UINT flOpt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProps", "pszGroup", "lpProps", "cbProps", "flOpt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAddDefaultPropertiesByExt(jitter):
    """
    HRESULT SHAddDefaultPropertiesByExt(
        PCWSTR pszExt,
        IPropertyStore* pPropStore
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszExt", "pPropStore"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetPropertyStoreForWindow(jitter):
    """
    HRESULT SHGetPropertyStoreForWindow(
        HWND hwnd,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetPropertyStoreFromIDList(jitter):
    """
    HRESULT SHGetPropertyStoreFromIDList(
        PCIDLIST_ABSOLUTE pidl,
        GETPROPERTYSTOREFLAGS flags,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "flags", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetPropertyStoreFromParsingName(jitter):
    """
    HRESULT SHGetPropertyStoreFromParsingName(
        PCWSTR pszPath,
        IBindCtx* pbc,
        GETPROPERTYSTOREFLAGS flags,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pbc", "flags", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHPropStgCreate(jitter):
    """
    HRESULT SHPropStgCreate(
        IPropertySetStorage* psstg,
        REFFMTID fmtid,
        const CLSID* pclsid,
        [PROPSETFLAG] grfFlags,
        [STGM_FLAGS] grfMode,
        DWORD dwDisposition,
        IPropertyStorage** ppstg,
        UINT* puCodePage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psstg", "fmtid", "pclsid", "grfFlags", "grfMode", "dwDisposition", "ppstg", "puCodePage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHPropStgReadMultiple(jitter):
    """
    HRESULT SHPropStgReadMultiple(
        IPropertyStorage* pps,
        [CodePageEnum] uCodePage,
        ULONG cpspec,
        PROPSPEC const[] rgpspec,
        PROPVARIANT[] rgvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pps", "uCodePage", "cpspec", "rgpspec", "rgvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHPropStgWriteMultiple(jitter):
    """
    HRESULT SHPropStgWriteMultiple(
        IPropertyStorage* pps,
        UINT* uCodePage,
        ULONG cpspec,
        PROPSPEC const[] rgpspec,
        PROPVARIANT[] rgvar,
        PROPID propidNameFirst
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pps", "uCodePage", "cpspec", "rgpspec", "rgvar", "propidNameFirst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_AddCommasExportW(jitter):
    """
    LPWSTR AddCommasExportW(
        DWORD value,
        LPWSTR pwszBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["value", "pwszBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_AppCompat_RunDLLW(jitter):
    """
    void AppCompat_RunDLLW(
        HWND unusedHwnd,
        HINSTANCE unusedHinstance,
        LPWSTR commandLine,
        int unusedInt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["unusedHwnd", "unusedHinstance", "commandLine", "unusedInt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CheckStagingArea(jitter):
    """
    HRESULT CheckStagingArea()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CreateAutoListParser(jitter):
    """
    HRESULT CreateAutoListParser(
        REFIID riid,
        PVOID* ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CreateInfoTipFromItem(jitter):
    """
    HRESULT CreateInfoTipFromItem(
        IShellFolder2* psf,
        ITEMIDLIST* pidl,
        LPCWSTR pText,
        REFIID riid,
        PVOID* ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psf", "pidl", "pText", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CreateInfoTipFromItem2(jitter):
    """
    HRESULT CreateInfoTipFromItem2(
        IShellFolder2* psf,
        ITEMIDLIST* pidl,
        PROPERTYKEY* pPropKey,
        LPCWSTR pText,
        REFIID riid,
        PVOID* ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psf", "pidl", "pPropKey", "pText", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DisconnectWindowDialog(jitter):
    """
    void DisconnectWindowDialog(
        HWND hwndUnused
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndUnused"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_GetAppPathFromLink(jitter):
    """
    HRESULT GetAppPathFromLink(
        IShellItem* pItem,
        LPWSTR pwszPathBuffer,
        DWORD dwBufferLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pItem", "pwszPathBuffer", "dwBufferLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_GetSqmableFileName(jitter):
    """
    BOOL GetSqmableFileName(
        LPCWSTR pwszFileName,
        LPWSTR pwszSqmName,
        UINT sqmNameBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszFileName", "pwszSqmName", "sqmNameBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Int64ToString(jitter):
    """
    int Int64ToString(
        INT64 number,
        LPWSTR pwszBuf,
        UINT bufLen,
        BOOL useNumberFormat,
        NUMBERFMT* pFormatInfo,
        [NUMBERFMT_FLAGS] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["number", "pwszBuf", "bufLen", "useNumberFormat", "pFormatInfo", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_IsElevationRequired(jitter):
    """
    BOOL IsElevationRequired(
        LPCWSTR lpwszExeFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwszExeFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_IsSearchEnabled(jitter):
    """
    BOOL IsSearchEnabled()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_LargeIntegerToString(jitter):
    """
    int LargeIntegerToString(
        LARGE_INTEGER* pNumber,
        LPWSTR pwszBuf,
        UINT bufLen,
        BOOL useNumberFormat,
        NUMBERFMT* pFormatInfo,
        [NUMBERFMT_FLAGS] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pNumber", "pwszBuf", "bufLen", "useNumberFormat", "pFormatInfo", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathGetPathDisplayName(jitter):
    """
    HRESULT PathGetPathDisplayName(
        LPCWSTR pwszPath,
        LPWSTR pwszDisplayName,
        DWORD displayNameLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszPath", "pwszDisplayName", "displayNameLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathIsTemporary(jitter, get_str, set_str):
    """
    BOOL PathIsTemporary(
        LPCTSTR pszFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathIsTemporaryA(jitter):
    shell32_PathIsTemporary(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_PathIsTemporaryW(jitter):
    shell32_PathIsTemporary(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_Printer_AddPrinterPropPages(jitter):
    """
    void Printer_AddPrinterPropPages(
        LPCWSTR printer,
        PROPSHEETHEADER* pPropHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["printer", "pPropHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Printer_LoadIconsW(jitter):
    """
    void Printer_LoadIconsW(
        LPCWSTR printerName,
        HICON* phLargeIcon,
        HICON* phSmallIcon
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["printerName", "phLargeIcon", "phSmallIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Printers_RegisterWindowW(jitter):
    """
    BOOL Printers_RegisterWindowW(
        LPCWSTR pwszPrinter,
        DWORD pidlType,
        BOOL* pWinCreated,
        HWND* phwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszPrinter", "pidlType", "pWinCreated", "phwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Printers_UnregisterWindow(jitter):
    """
    void Printers_UnregisterWindow(
        CLASSPIDL* pClassPidl,
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pClassPidl", "hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_RefreshBrowserLayout(jitter):
    """
    HRESULT RefreshBrowserLayout(
        IShellItem* pItem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_RunAsNewUser_RunDLLW(jitter):
    """
    int RunAsNewUser_RunDLLW(
        HWND hWnd,
        HINSTANCE hIinstance,
        LPCWSTR lpszFileMapName,
        [ShowWindowCmd] nCmdShow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hIinstance", "lpszFileMapName", "nCmdShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetUserDisplayName(jitter):
    """
    HRESULT SHGetUserDisplayName(
        LPWSTR pwszName,
        UINT pBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszName", "pBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetUserPicturePathEx(jitter):
    """
    HRESULT SHGetUserPicturePathEx(
        LPCWSTR pwszUserOrPicName,
        [SGUPP_FLAGS] sguppFlags,
        LPCWSTR pwszDesiredSrcExt,
        LPWSTR pwszPicPath,
        UINT picPathLen,
        LPWSTR pwszSrcPath,
        UINT srcLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszUserOrPicName", "sguppFlags", "pwszDesiredSrcExt", "pwszPicPath", "picPathLen", "pwszSrcPath", "srcLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHHelpShortcuts_RunDLL(jitter, get_str, set_str):
    """
    void SHHelpShortcuts_RunDLL(
        HWND hwndParent,
        HINSTANCE unusedHinstance,
        LPCTSTR commandLine,
        int unusedInt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "unusedHinstance", "commandLine", "unusedInt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHHelpShortcuts_RunDLLA(jitter):
    shell32_SHHelpShortcuts_RunDLL(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def shell32_SHHelpShortcuts_RunDLLW(jitter):
    shell32_SHHelpShortcuts_RunDLL(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def shell32_SHResolveUserNames(jitter):
    """
    HRESULT SHResolveUserNames(
        LPCWSTR pwszSids,
        LPWSTR pwszNames,
        UINT nameLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszSids", "pwszNames", "nameLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSettingsChanged(jitter):
    """
    void SHSettingsChanged(
        WPARAM wParam,
        LPCWSTR lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHShouldShowWizards(jitter):
    """
    BOOL SHShouldShowWizards(
        IUnknown* pUnk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHTestTokenPrivilegeW(jitter):
    """
    BOOL SHTestTokenPrivilegeW(
        HANDLE hToken,
        LPCWSTR pwszPrivilege
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hToken", "pwszPrivilege"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHUserGetPasswordHint(jitter):
    """
    HRESULT SHUserGetPasswordHint(
        PCWSTR pwszUserName,
        PWSTR* ppwszHint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszUserName", "ppwszHint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHUserSetPasswordHint(jitter):
    """
    HRESULT SHUserSetPasswordHint(
        PCWSTR pwszUserName,
        PCWSTR pwszPasswordHint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszUserName", "pwszPasswordHint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ShellExecCmdLine(jitter):
    """
    HRESULT ShellExecCmdLine(
        HWND hwnd,
        LPCWSTR pwszCommand,
        LPCWSTR pwszStartDir,
        [ShowWindowCmd] nShow,
        LPVOID pUnused,
        [SECL_FLAGS] dwSeclFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pwszCommand", "pwszStartDir", "nShow", "pUnused", "dwSeclFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ShortSizeFormatExportW(jitter):
    """
    LPWSTR ShortSizeFormatExportW(
        DWORD value,
        LPWSTR pwszBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["value", "pwszBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
