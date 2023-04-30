MSIPATCHDATATYPE = {
    "MSIPATCH_DATATYPE_PATCHFILE": 0,
    "MSIPATCH_DATATYPE_XMLPATH": 1,
    "MSIPATCH_DATATYPE_XMLBLOB": 2,
}
MSIPATCHDATATYPE_INV = {
    0: "MSIPATCH_DATATYPE_PATCHFILE",
    1: "MSIPATCH_DATATYPE_XMLPATH",
    2: "MSIPATCH_DATATYPE_XMLBLOB",
}
USERINFOSTATE = {
    "USERINFOSTATE_MOREDATA": -3,
    "USERINFOSTATE_INVALIDARG": -2,
    "USERINFOSTATE_UNKNOWN": -1,
    "USERINFOSTATE_ABSENT": 0,
    "USERINFOSTATE_PRESENT": 1,
}
USERINFOSTATE_INV = {
    -3: "USERINFOSTATE_MOREDATA",
    -2: "USERINFOSTATE_INVALIDARG",
    -1: "USERINFOSTATE_UNKNOWN",
    0: "USERINFOSTATE_ABSENT",
    1: "USERINFOSTATE_PRESENT",
}
INSTALLSTATE = {
    "INSTALLSTATE_NOTUSED": -7,
    "INSTALLSTATE_BADCONFIG": -6,
    "INSTALLSTATE_INCOMPLETE": -5,
    "INSTALLSTATE_SOURCEABSENT": -4,
    "INSTALLSTATE_MOREDATA": -3,
    "INSTALLSTATE_INVALIDARG": -2,
    "INSTALLSTATE_UNKNOWN": -1,
    "INSTALLSTATE_BROKEN": 0,
    "INSTALLSTATE_ADVERTISED": 1,
    "INSTALLSTATE_ABSENT": 2,
    "INSTALLSTATE_LOCAL": 3,
    "INSTALLSTATE_SOURCE": 4,
    "INSTALLSTATE_DEFAULT": 5,
}
INSTALLSTATE_INV = {
    -7: "INSTALLSTATE_NOTUSED",
    -6: "INSTALLSTATE_BADCONFIG",
    -5: "INSTALLSTATE_INCOMPLETE",
    -4: "INSTALLSTATE_SOURCEABSENT",
    -3: "INSTALLSTATE_MOREDATA",
    -2: "INSTALLSTATE_INVALIDARG",
    -1: "INSTALLSTATE_UNKNOWN",
    0: "INSTALLSTATE_BROKEN",
    1: "INSTALLSTATE_ADVERTISED",
    2: "INSTALLSTATE_ABSENT",
    3: "INSTALLSTATE_LOCAL",
    4: "INSTALLSTATE_SOURCE",
    5: "INSTALLSTATE_DEFAULT",
}
_MsiInstallLevel_ = {
    "INSTALLLEVEL_DEFAULT": 0,
    "INSTALLLEVEL_MINIMUM": 1,
    "INSTALLLEVEL_MAXIMUM": 0xFFFF,
}
_MsiInstallLevel__INV = {
    0: "INSTALLLEVEL_DEFAULT",
    1: "INSTALLLEVEL_MINIMUM",
    0xFFFF: "INSTALLLEVEL_MAXIMUM",
}
_MsiInstallMode_ = {
    "INSTALLMODE_NODETECTION_ANY": -4,
    "INSTALLMODE_NOSOURCERESOLUTION": -3,
    "INSTALLMODE_NODETECTION": -2,
    "INSTALLMODE_EXISTING": -1,
    "INSTALLMODE_DEFAULT": 0,
}
_MsiInstallMode__INV = {
    -4: "INSTALLMODE_NODETECTION_ANY",
    -3: "INSTALLMODE_NOSOURCERESOLUTION",
    -2: "INSTALLMODE_NODETECTION",
    -1: "INSTALLMODE_EXISTING",
    0: "INSTALLMODE_DEFAULT",
}
_MsiTransactionState_ = {
    "MSITRANSACTIONSTATE_ROLLBACK": 0,
    "MSITRANSACTIONSTATE_COMMIT": 1,
}
_MsiTransactionState__INV = {
    0: "MSITRANSACTIONSTATE_ROLLBACK",
    1: "MSITRANSACTIONSTATE_COMMIT",
}
MSIMODIFY = {
    "MSIMODIFY_SEEK": -1,
    "MSIMODIFY_REFRESH": 0,
    "MSIMODIFY_INSERT": 1,
    "MSIMODIFY_UPDATE": 2,
    "MSIMODIFY_ASSIGN": 3,
    "MSIMODIFY_REPLACE": 4,
    "MSIMODIFY_MERGE": 5,
    "MSIMODIFY_DELETE": 6,
    "MSIMODIFY_INSERT_TEMPORARY": 7,
    "MSIMODIFY_VALIDATE": 8,
    "MSIMODIFY_VALIDATE_NEW": 9,
    "MSIMODIFY_VALIDATE_FIELD": 10,
    "MSIMODIFY_VALIDATE_DELETE": 11,
}
MSIMODIFY_INV = {
    -1: "MSIMODIFY_SEEK",
    0: "MSIMODIFY_REFRESH",
    1: "MSIMODIFY_INSERT",
    2: "MSIMODIFY_UPDATE",
    3: "MSIMODIFY_ASSIGN",
    4: "MSIMODIFY_REPLACE",
    5: "MSIMODIFY_MERGE",
    6: "MSIMODIFY_DELETE",
    7: "MSIMODIFY_INSERT_TEMPORARY",
    8: "MSIMODIFY_VALIDATE",
    9: "MSIMODIFY_VALIDATE_NEW",
    10: "MSIMODIFY_VALIDATE_FIELD",
    11: "MSIMODIFY_VALIDATE_DELETE",
}
MSICOLINFO = {
    "MSICOLINFO_NAMES": 0,
    "MSICOLINFO_TYPES": 1,
}
MSICOLINFO_INV = {
    0: "MSICOLINFO_NAMES",
    1: "MSICOLINFO_TYPES",
}
MSICONDITION = {
    "MSICONDITION_FALSE": 0,
    "MSICONDITION_TRUE": 1,
    "MSICONDITION_NONE": 2,
    "MSICONDITION_ERROR": 3,
}
MSICONDITION_INV = {
    0: "MSICONDITION_FALSE",
    1: "MSICONDITION_TRUE",
    2: "MSICONDITION_NONE",
    3: "MSICONDITION_ERROR",
}
MSIDBERROR = {
    "MSIDBERROR_INVALIDARG": -3,
    "MSIDBERROR_MOREDATA": -2,
    "MSIDBERROR_FUNCTIONERROR": -1,
    "MSIDBERROR_NOERROR": 0,
    "MSIDBERROR_DUPLICATEKEY": 1,
    "MSIDBERROR_REQUIRED": 2,
    "MSIDBERROR_BADLINK": 3,
    "MSIDBERROR_OVERFLOW": 4,
    "MSIDBERROR_UNDERFLOW": 5,
    "MSIDBERROR_NOTINSET": 6,
    "MSIDBERROR_BADVERSION": 7,
    "MSIDBERROR_BADCASE": 8,
    "MSIDBERROR_BADGUID": 9,
    "MSIDBERROR_BADWILDCARD": 10,
    "MSIDBERROR_BADIDENTIFIER": 11,
    "MSIDBERROR_BADLANGUAGE": 12,
    "MSIDBERROR_BADFILENAME": 13,
    "MSIDBERROR_BADPATH": 14,
    "MSIDBERROR_BADCONDITION": 15,
    "MSIDBERROR_BADFORMATTED": 16,
    "MSIDBERROR_BADTEMPLATE": 17,
    "MSIDBERROR_BADDEFAULTDIR": 18,
    "MSIDBERROR_BADREGPATH": 19,
    "MSIDBERROR_BADCUSTOMSOURCE": 20,
    "MSIDBERROR_BADPROPERTY": 21,
    "MSIDBERROR_MISSINGDATA": 22,
    "MSIDBERROR_BADCATEGORY": 23,
    "MSIDBERROR_BADKEYTABLE": 24,
    "MSIDBERROR_BADMAXMINVALUES": 25,
    "MSIDBERROR_BADCABINET": 26,
    "MSIDBERROR_BADSHORTCUT": 27,
    "MSIDBERROR_STRINGOVERFLOW": 28,
    "MSIDBERROR_BADLOCALIZEATTRIB": 29,
}
MSIDBERROR_INV = {
    -3: "MSIDBERROR_INVALIDARG",
    -2: "MSIDBERROR_MOREDATA",
    -1: "MSIDBERROR_FUNCTIONERROR",
    0: "MSIDBERROR_NOERROR",
    1: "MSIDBERROR_DUPLICATEKEY",
    2: "MSIDBERROR_REQUIRED",
    3: "MSIDBERROR_BADLINK",
    4: "MSIDBERROR_OVERFLOW",
    5: "MSIDBERROR_UNDERFLOW",
    6: "MSIDBERROR_NOTINSET",
    7: "MSIDBERROR_BADVERSION",
    8: "MSIDBERROR_BADCASE",
    9: "MSIDBERROR_BADGUID",
    10: "MSIDBERROR_BADWILDCARD",
    11: "MSIDBERROR_BADIDENTIFIER",
    12: "MSIDBERROR_BADLANGUAGE",
    13: "MSIDBERROR_BADFILENAME",
    14: "MSIDBERROR_BADPATH",
    15: "MSIDBERROR_BADCONDITION",
    16: "MSIDBERROR_BADFORMATTED",
    17: "MSIDBERROR_BADTEMPLATE",
    18: "MSIDBERROR_BADDEFAULTDIR",
    19: "MSIDBERROR_BADREGPATH",
    20: "MSIDBERROR_BADCUSTOMSOURCE",
    21: "MSIDBERROR_BADPROPERTY",
    22: "MSIDBERROR_MISSINGDATA",
    23: "MSIDBERROR_BADCATEGORY",
    24: "MSIDBERROR_BADKEYTABLE",
    25: "MSIDBERROR_BADMAXMINVALUES",
    26: "MSIDBERROR_BADCABINET",
    27: "MSIDBERROR_BADSHORTCUT",
    28: "MSIDBERROR_STRINGOVERFLOW",
    29: "MSIDBERROR_BADLOCALIZEATTRIB",
}
MSICOSTTREE = {
    "MSICOSTTREE_SELFONLY": 0,
    "MSICOSTTREE_CHILDREN": 1,
    "MSICOSTTREE_PARENTS": 2,
    "MSICOSTTREE_RESERVED": 3,
}
MSICOSTTREE_INV = {
    0: "MSICOSTTREE_SELFONLY",
    1: "MSICOSTTREE_CHILDREN",
    2: "MSICOSTTREE_PARENTS",
    3: "MSICOSTTREE_RESERVED",
}
INSTALLMESSAGE = {
    "INSTALLMESSAGE_FATALEXIT": 0x00000000,
    "INSTALLMESSAGE_ERROR": 0x01000000,
    "INSTALLMESSAGE_WARNING": 0x02000000,
    "INSTALLMESSAGE_USER": 0x03000000,
    "INSTALLMESSAGE_INFO": 0x04000000,
    "INSTALLMESSAGE_FILESINUSE": 0x05000000,
    "INSTALLMESSAGE_RESOLVESOURCE": 0x06000000,
    "INSTALLMESSAGE_OUTOFDISKSPACE": 0x07000000,
    "INSTALLMESSAGE_ACTIONSTART": 0x08000000,
    "INSTALLMESSAGE_ACTIONDATA": 0x09000000,
    "INSTALLMESSAGE_PROGRESS": 0x0A000000,
    "INSTALLMESSAGE_COMMONDATA": 0x0B000000,
    "INSTALLMESSAGE_INITIALIZE": 0x0C000000,
    "INSTALLMESSAGE_TERMINATE": 0x0D000000,
    "INSTALLMESSAGE_SHOWDIALOG": 0x0E000000,
    "INSTALLMESSAGE_PERFORMANCE": 0x0F000000,
    "INSTALLMESSAGE_RMFILESINUSE": 0x19000000,
    "INSTALLMESSAGE_INSTALLSTART": 0x1A000000,
    "INSTALLMESSAGE_INSTALLEND": 0x1B000000,
}
INSTALLMESSAGE_INV = {
    0x00000000: "INSTALLMESSAGE_FATALEXIT",
    0x01000000: "INSTALLMESSAGE_ERROR",
    0x02000000: "INSTALLMESSAGE_WARNING",
    0x03000000: "INSTALLMESSAGE_USER",
    0x04000000: "INSTALLMESSAGE_INFO",
    0x05000000: "INSTALLMESSAGE_FILESINUSE",
    0x06000000: "INSTALLMESSAGE_RESOLVESOURCE",
    0x07000000: "INSTALLMESSAGE_OUTOFDISKSPACE",
    0x08000000: "INSTALLMESSAGE_ACTIONSTART",
    0x09000000: "INSTALLMESSAGE_ACTIONDATA",
    0x0A000000: "INSTALLMESSAGE_PROGRESS",
    0x0B000000: "INSTALLMESSAGE_COMMONDATA",
    0x0C000000: "INSTALLMESSAGE_INITIALIZE",
    0x0D000000: "INSTALLMESSAGE_TERMINATE",
    0x0E000000: "INSTALLMESSAGE_SHOWDIALOG",
    0x0F000000: "INSTALLMESSAGE_PERFORMANCE",
    0x19000000: "INSTALLMESSAGE_RMFILESINUSE",
    0x1A000000: "INSTALLMESSAGE_INSTALLSTART",
    0x1B000000: "INSTALLMESSAGE_INSTALLEND",
}
MSIRUNMODE = {
    "MSIRUNMODE_ADMIN": 0,
    "MSIRUNMODE_ADVERTISE": 1,
    "MSIRUNMODE_MAINTENANCE": 2,
    "MSIRUNMODE_ROLLBACKENABLED": 3,
    "MSIRUNMODE_LOGENABLED": 4,
    "MSIRUNMODE_OPERATIONS": 5,
    "MSIRUNMODE_REBOOTATEND": 6,
    "MSIRUNMODE_REBOOTNOW": 7,
    "MSIRUNMODE_CABINET": 8,
    "MSIRUNMODE_SOURCESHORTNAMES": 9,
    "MSIRUNMODE_TARGETSHORTNAMES": 10,
    "MSIRUNMODE_RESERVED11": 11,
    "MSIRUNMODE_WINDOWS9X": 12,
    "MSIRUNMODE_ZAWENABLED": 13,
    "MSIRUNMODE_RESERVED14": 14,
    "MSIRUNMODE_RESERVED15": 15,
    "MSIRUNMODE_SCHEDULED": 16,
    "MSIRUNMODE_ROLLBACK": 17,
    "MSIRUNMODE_COMMIT": 18,
}
MSIRUNMODE_INV = {
    0: "MSIRUNMODE_ADMIN",
    1: "MSIRUNMODE_ADVERTISE",
    2: "MSIRUNMODE_MAINTENANCE",
    3: "MSIRUNMODE_ROLLBACKENABLED",
    4: "MSIRUNMODE_LOGENABLED",
    5: "MSIRUNMODE_OPERATIONS",
    6: "MSIRUNMODE_REBOOTATEND",
    7: "MSIRUNMODE_REBOOTNOW",
    8: "MSIRUNMODE_CABINET",
    9: "MSIRUNMODE_SOURCESHORTNAMES",
    10: "MSIRUNMODE_TARGETSHORTNAMES",
    11: "MSIRUNMODE_RESERVED11",
    12: "MSIRUNMODE_WINDOWS9X",
    13: "MSIRUNMODE_ZAWENABLED",
    14: "MSIRUNMODE_RESERVED14",
    15: "MSIRUNMODE_RESERVED15",
    16: "MSIRUNMODE_SCHEDULED",
    17: "MSIRUNMODE_ROLLBACK",
    18: "MSIRUNMODE_COMMIT",
}
MSIDBSTATE = {
    "MSIDBSTATE_ERROR": -1,
    "MSIDBSTATE_READ": 0,
    "MSIDBSTATE_WRITE": 1,
}
MSIDBSTATE_INV = {
    -1: "MSIDBSTATE_ERROR",
    0: "MSIDBSTATE_READ",
    1: "MSIDBSTATE_WRITE",
}
_MSI_PID_ = {
    "PID_DICTIONARY": 0,
    "PID_CODEPAGE": 1,
    "PID_TITLE": 2,
    "PID_SUBJECT": 3,
    "PID_AUTHOR": 4,
    "PID_KEYWORDS": 5,
    "PID_COMMENTS": 6,
    "PID_TEMPLATE": 7,
    "PID_LASTAUTHOR": 8,
    "PID_REVNUMBER": 9,
    "PID_EDITTIME": 10,
    "PID_LASTPRINTED": 11,
    "PID_CREATE_DTM": 12,
    "PID_LASTSAVE_DTM": 13,
    "PID_PAGECOUNT": 14,
    "PID_WORDCOUNT": 15,
    "PID_CHARCOUNT": 16,
    "PID_THUMBNAIL": 17,
    "PID_APPNAME": 18,
    "PID_SECURITY": 19,
}
_MSI_PID__INV = {
    0: "PID_DICTIONARY",
    1: "PID_CODEPAGE",
    2: "PID_TITLE",
    3: "PID_SUBJECT",
    4: "PID_AUTHOR",
    5: "PID_KEYWORDS",
    6: "PID_COMMENTS",
    7: "PID_TEMPLATE",
    8: "PID_LASTAUTHOR",
    9: "PID_REVNUMBER",
    10: "PID_EDITTIME",
    11: "PID_LASTPRINTED",
    12: "PID_CREATE_DTM",
    13: "PID_LASTSAVE_DTM",
    14: "PID_PAGECOUNT",
    15: "PID_WORDCOUNT",
    16: "PID_CHARCOUNT",
    17: "PID_THUMBNAIL",
    18: "PID_APPNAME",
    19: "PID_SECURITY",
}

def msi_MsiSetInternalUI(jitter):
    """
    INSTALLUILEVEL MsiSetInternalUI(
        INSTALLUILEVEL dwUILevel,
        HWND* phWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwUILevel", "phWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetExternalUI(jitter, get_str, set_str):
    """
    INSTALLUI_HANDLER MsiSetExternalUI(
        INSTALLUI_HANDLER puiHandler,
        [MsiInstallLogMode] dwMessageFilter,
        LPVOID pvContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["puiHandler", "dwMessageFilter", "pvContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetExternalUIA(jitter):
    msi_MsiSetExternalUI(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSetExternalUIW(jitter):
    msi_MsiSetExternalUI(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSetExternalUIRecord(jitter):
    """
    [MSI_ERROR] MsiSetExternalUIRecord(
        PINSTALLUI_HANDLER_RECORD puiHandler,
        [MsiInstallLogMode] dwMessageFilter,
        LPVOID pvContext,
        PINSTALLUI_HANDLER_RECORD ppuiPrevHandler
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["puiHandler", "dwMessageFilter", "pvContext", "ppuiPrevHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnableLog(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiEnableLog(
        [MsiInstallLogMode] dwLogMode,
        LPCTSTR szLogFile,
        [MsiInstallLogAttributes] dwLogAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwLogMode", "szLogFile", "dwLogAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnableLogA(jitter):
    msi_MsiEnableLog(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEnableLogW(jitter):
    msi_MsiEnableLog(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiCloseHandle(jitter):
    """
    [MSI_ERROR] MsiCloseHandle(
        MSIHANDLE hAny
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAny"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiCloseAllHandles(jitter):
    """
    UINT MsiCloseAllHandles()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiAdvertiseProduct(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiAdvertiseProduct(
        LPCTSTR szPackagePath,
        LPCTSTR szScriptfilePath,
        LPCTSTR szTransforms,
        LANGID lgidLanguage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szPackagePath", "szScriptfilePath", "szTransforms", "lgidLanguage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiAdvertiseProductA(jitter):
    msi_MsiAdvertiseProduct(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiAdvertiseProductW(jitter):
    msi_MsiAdvertiseProduct(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiAdvertiseProductEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiAdvertiseProductEx(
        LPCTSTR szPackagePath,
        LPCTSTR szScriptfilePath,
        LPCTSTR szTransforms,
        LANGID lgidLanguage,
        [MsiArchFlags] dwPlatform,
        [MsiAdOptions] dwOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szPackagePath", "szScriptfilePath", "szTransforms", "lgidLanguage", "dwPlatform", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiAdvertiseProductExA(jitter):
    msi_MsiAdvertiseProductEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiAdvertiseProductExW(jitter):
    msi_MsiAdvertiseProductEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiAdvertiseScript(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiAdvertiseScript(
        LPCTSTR szScriptFile,
        [MsiScriptFlags] dwFlags,
        PHKEY phRegData,
        BOOL fRemoveItems
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szScriptFile", "dwFlags", "phRegData", "fRemoveItems"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiAdvertiseScriptA(jitter):
    msi_MsiAdvertiseScript(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiAdvertiseScriptW(jitter):
    msi_MsiAdvertiseScript(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiInstallProduct(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiInstallProduct(
        LPCTSTR szPackagePath,
        LPCTSTR szCommandLine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szPackagePath", "szCommandLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiInstallProductA(jitter):
    msi_MsiInstallProduct(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiInstallProductW(jitter):
    msi_MsiInstallProduct(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiConfigureProduct(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiConfigureProduct(
        LPCTSTR szProduct,
        [MsiInstallLevel] iInstallLevel,
        INSTALLSTATE eInstallState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "iInstallLevel", "eInstallState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiConfigureProductA(jitter):
    msi_MsiConfigureProduct(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiConfigureProductW(jitter):
    msi_MsiConfigureProduct(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiConfigureProductEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiConfigureProductEx(
        LPCTSTR szProduct,
        [MsiInstallLevel] iInstallLevel,
        INSTALLSTATE eInstallState,
        LPCTSTR szCommandLine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "iInstallLevel", "eInstallState", "szCommandLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiConfigureProductExA(jitter):
    msi_MsiConfigureProductEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiConfigureProductExW(jitter):
    msi_MsiConfigureProductEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiReinstallProduct(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiReinstallProduct(
        LPCTSTR szProduct,
        [MsiReinstallMode] dwReinstallMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "dwReinstallMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiReinstallProductA(jitter):
    msi_MsiReinstallProduct(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiReinstallProductW(jitter):
    msi_MsiReinstallProduct(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiConfigureFeature(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiConfigureFeature(
        LPCTSTR szProduct,
        LPCTSTR szFeature,
        INSTALLSTATE eInstallState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature", "eInstallState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiConfigureFeatureA(jitter):
    msi_MsiConfigureFeature(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiConfigureFeatureW(jitter):
    msi_MsiConfigureFeature(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiReinstallFeature(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiReinstallFeature(
        LPCTSTR szProduct,
        LPCTSTR szFeature,
        [MsiReinstallMode] dwReinstallMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature", "dwReinstallMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiReinstallFeatureA(jitter):
    msi_MsiReinstallFeature(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiReinstallFeatureW(jitter):
    msi_MsiReinstallFeature(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiInstallMissingComponent(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiInstallMissingComponent(
        LPCTSTR szProduct,
        LPCTSTR szComponent,
        INSTALLSTATE eInstallState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szComponent", "eInstallState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiInstallMissingComponentA(jitter):
    msi_MsiInstallMissingComponent(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiInstallMissingComponentW(jitter):
    msi_MsiInstallMissingComponent(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiInstallMissingFile(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiInstallMissingFile(
        LPCTSTR szProduct,
        LPCTSTR szFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiInstallMissingFileA(jitter):
    msi_MsiInstallMissingFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiInstallMissingFileW(jitter):
    msi_MsiInstallMissingFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiNotifySidChange(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiNotifySidChange(
        LPCTSTR szOldSid,
        LPCTSTR szNewSid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szOldSid", "szNewSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiNotifySidChangeA(jitter):
    msi_MsiNotifySidChange(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiNotifySidChangeW(jitter):
    msi_MsiNotifySidChange(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiProcessAdvertiseScript(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiProcessAdvertiseScript(
        LPCTSTR szScriptFile,
        LPCTSTR szIconFolder,
        HKEY hRegData,
        BOOL fShortcuts,
        BOOL fRemoveItems
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szScriptFile", "szIconFolder", "hRegData", "fShortcuts", "fRemoveItems"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiProcessAdvertiseScriptA(jitter):
    msi_MsiProcessAdvertiseScript(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiProcessAdvertiseScriptW(jitter):
    msi_MsiProcessAdvertiseScript(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSourceListAddSource(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSourceListAddSource(
        LPCTSTR szProduct,
        LPCTSTR szUserName,
        DWORD dwReserved,
        LPCTSTR szSource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szUserName", "dwReserved", "szSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListAddSourceA(jitter):
    msi_MsiSourceListAddSource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSourceListAddSourceW(jitter):
    msi_MsiSourceListAddSource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSourceListAddSourceEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSourceListAddSourceEx(
        LPCTSTR szProductCodeOrPatchCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        [MsiSourceType] dwOptions,
        LPCTSTR szSource,
        DWORD dwIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "szSource", "dwIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListAddSourceExA(jitter):
    msi_MsiSourceListAddSourceEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSourceListAddSourceExW(jitter):
    msi_MsiSourceListAddSourceEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSourceListClearSource(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSourceListClearSource(
        LPCTSTR szProductCodeOrPatchCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        [MsiSourceType] dwOptions,
        LPCTSTR szSource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "szSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListClearSourceA(jitter):
    msi_MsiSourceListClearSource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSourceListClearSourceW(jitter):
    msi_MsiSourceListClearSource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSourceListClearAll(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSourceListClearAll(
        LPCTSTR szProduct,
        LPCTSTR szUserName,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szUserName", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListClearAllA(jitter):
    msi_MsiSourceListClearAll(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSourceListClearAllW(jitter):
    msi_MsiSourceListClearAll(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSourceListClearAllEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSourceListClearAllEx(
        LPCTSTR szProductCodeOrPatchCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        [MsiSourceType] dwOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListClearAllExA(jitter):
    msi_MsiSourceListClearAllEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSourceListClearAllExW(jitter):
    msi_MsiSourceListClearAllEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSourceListForceResolution(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSourceListForceResolution(
        LPCTSTR szProduct,
        LPCTSTR szUserName,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szUserName", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListForceResolutionA(jitter):
    msi_MsiSourceListForceResolution(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSourceListForceResolutionW(jitter):
    msi_MsiSourceListForceResolution(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSourceListForceResolutionEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSourceListForceResolutionEx(
        LPCTSTR szProductCodeOrPatchCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        [MsiCode] dwOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListForceResolutionExA(jitter):
    msi_MsiSourceListForceResolutionEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSourceListForceResolutionExW(jitter):
    msi_MsiSourceListForceResolutionEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSourceListGetInfo(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSourceListGetInfo(
        LPCTSTR szProductCodeOrPatchCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        [MsiCode] dwOptions,
        LPCTSTR szProperty,
        LPTSTR szValue,
        LPDWORD pcchValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "szProperty", "szValue", "pcchValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListGetInfoA(jitter):
    msi_MsiSourceListGetInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSourceListGetInfoW(jitter):
    msi_MsiSourceListGetInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSourceListSetInfo(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSourceListSetInfo(
        LPCTSTR szProductCodeOrPatchCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        [MsiSourceType] dwOptions,
        LPCTSTR szProperty,
        LPCTSTR szValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "szProperty", "szValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListSetInfoA(jitter):
    msi_MsiSourceListSetInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSourceListSetInfoW(jitter):
    msi_MsiSourceListSetInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSourceListEnumMediaDisks(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSourceListEnumMediaDisks(
        LPCTSTR szProductCodeOrPatchCode,
        LPCTSTR szUserSID,
        MSIINSTALLCONTEXT dwContext,
        [MsiCode] dwOptions,
        DWORD dwIndex,
        LPWORD pdwDiskId,
        LPTSTR szVolumeLabel,
        LPDWORD pcchVolumeLabel,
        LPTSTR szDiskPrompt,
        LPDWORD pcchDiskPrompt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSID", "dwContext", "dwOptions", "dwIndex", "pdwDiskId", "szVolumeLabel", "pcchVolumeLabel", "szDiskPrompt", "pcchDiskPrompt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListEnumMediaDisksA(jitter):
    msi_MsiSourceListEnumMediaDisks(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSourceListEnumMediaDisksW(jitter):
    msi_MsiSourceListEnumMediaDisks(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSourceListAddMediaDisk(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSourceListAddMediaDisk(
        LPCTSTR szProductCodeOrPatchCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        [MsiCode] dwOptions,
        DWORD dwDiskId,
        LPCTSTR szVolumeLabel,
        LPCTSTR szDiskPrompt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "dwDiskId", "szVolumeLabel", "szDiskPrompt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListAddMediaDiskA(jitter):
    msi_MsiSourceListAddMediaDisk(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSourceListAddMediaDiskW(jitter):
    msi_MsiSourceListAddMediaDisk(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSourceListClearMediaDisk(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSourceListClearMediaDisk(
        LPCTSTR szProductCodeOrPatchCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        [MsiCode] dwOptions,
        DWORD dwDiskID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "dwDiskID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListClearMediaDiskA(jitter):
    msi_MsiSourceListClearMediaDisk(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSourceListClearMediaDiskW(jitter):
    msi_MsiSourceListClearMediaDisk(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSourceListEnumSources(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSourceListEnumSources(
        LPCTSTR szProductCodeOrPatchCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        [MsiSourceType] dwOptions,
        DWORD dwIndex,
        LPTSTR szSource,
        LPDWORD pcchSource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "dwIndex", "szSource", "pcchSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListEnumSourcesA(jitter):
    msi_MsiSourceListEnumSources(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSourceListEnumSourcesW(jitter):
    msi_MsiSourceListEnumSources(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiProvideAssembly(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiProvideAssembly(
        LPCTSTR szAssemblyName,
        LPCTSTR szAppContext,
        [MsiInstallMode] dwInstallMode,
        [MsiAssemblyInfo] dwAssemblyInfo,
        LPTSTR lpPathBuf,
        DWORD* pcchPathBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szAssemblyName", "szAppContext", "dwInstallMode", "dwAssemblyInfo", "lpPathBuf", "pcchPathBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiProvideAssemblyA(jitter):
    msi_MsiProvideAssembly(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiProvideAssemblyW(jitter):
    msi_MsiProvideAssembly(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiProvideComponent(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiProvideComponent(
        LPCTSTR szProduct,
        LPCTSTR szFeature,
        LPCTSTR szComponent,
        [MsiInstallMode] dwInstallMode,
        LPTSTR lpPathBuf,
        DWORD* pcchPathBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature", "szComponent", "dwInstallMode", "lpPathBuf", "pcchPathBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiProvideComponentA(jitter):
    msi_MsiProvideComponent(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiProvideComponentW(jitter):
    msi_MsiProvideComponent(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiProvideQualifiedComponent(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiProvideQualifiedComponent(
        LPCTSTR szComponent,
        LPCTSTR szQualifier,
        [MsiInstallMode] dwInstallMode,
        LPTSTR lpPathBuf,
        DWORD* pcchPathBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "szQualifier", "dwInstallMode", "lpPathBuf", "pcchPathBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiProvideQualifiedComponentA(jitter):
    msi_MsiProvideQualifiedComponent(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiProvideQualifiedComponentW(jitter):
    msi_MsiProvideQualifiedComponent(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiProvideQualifiedComponentEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiProvideQualifiedComponentEx(
        LPCTSTR szComponent,
        LPCTSTR szQualifier,
        [MsiInstallMode] dwInstallMode,
        LPTSTR szProduct,
        DWORD dwUnused1,
        DWORD dwUnused2,
        LPTSTR lpPathBuf,
        DWORD* pcchPathBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "szQualifier", "dwInstallMode", "szProduct", "dwUnused1", "dwUnused2", "lpPathBuf", "pcchPathBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiProvideQualifiedComponentExA(jitter):
    msi_MsiProvideQualifiedComponentEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiProvideQualifiedComponentExW(jitter):
    msi_MsiProvideQualifiedComponentEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetComponentPath(jitter, get_str, set_str):
    """
    INSTALLSTATE MsiGetComponentPath(
        LPCTSTR szProduct,
        LPCTSTR szComponent,
        LPTSTR lpPathBuf,
        DWORD* pcchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szComponent", "lpPathBuf", "pcchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetComponentPathA(jitter):
    msi_MsiGetComponentPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetComponentPathW(jitter):
    msi_MsiGetComponentPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetComponentPathEx(jitter, get_str, set_str):
    """
    INSTALLSTATE MsiGetComponentPathEx(
        LPCTSTR szProductCode,
        LPCTSTR szComponentCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        LPTSTR szPathBuf,
        LPDWORD pcchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szComponentCode", "szUserSid", "dwContext", "szPathBuf", "pcchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetComponentPathExA(jitter):
    msi_MsiGetComponentPathEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetComponentPathExW(jitter):
    msi_MsiGetComponentPathEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiLocateComponent(jitter, get_str, set_str):
    """
    INSTALLSTATE MsiLocateComponent(
        LPCTSTR szComponent,
        LPTSTR lpPathBuf,
        DWORD* pcchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "lpPathBuf", "pcchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiLocateComponentA(jitter):
    msi_MsiLocateComponent(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiLocateComponentW(jitter):
    msi_MsiLocateComponent(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiQueryComponentState(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiQueryComponentState(
        LPTSTR szProductCode,
        LPTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        LPCTSTR szComponent,
        INSTALLSTATE* pdwState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szUserSid", "dwContext", "szComponent", "pdwState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiQueryComponentStateA(jitter):
    msi_MsiQueryComponentState(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiQueryComponentStateW(jitter):
    msi_MsiQueryComponentState(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiCollectUserInfo(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiCollectUserInfo(
        LPCTSTR szProduct
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiCollectUserInfoA(jitter):
    msi_MsiCollectUserInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiCollectUserInfoW(jitter):
    msi_MsiCollectUserInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiUseFeature(jitter, get_str, set_str):
    """
    INSTALLSTATE MsiUseFeature(
        LPCTSTR szProduct,
        LPCTSTR szFeature
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiUseFeatureA(jitter):
    msi_MsiUseFeature(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiUseFeatureW(jitter):
    msi_MsiUseFeature(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiUseFeatureEx(jitter, get_str, set_str):
    """
    INSTALLSTATE MsiUseFeatureEx(
        LPCTSTR szProduct,
        LPCTSTR szFeature,
        [MsiInstallMode] dwInstallMode,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature", "dwInstallMode", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiUseFeatureExA(jitter):
    msi_MsiUseFeatureEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiUseFeatureExW(jitter):
    msi_MsiUseFeatureEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetProductCode(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetProductCode(
        LPCTSTR szComponent,
        LPTSTR lpProductBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "lpProductBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetProductCodeA(jitter):
    msi_MsiGetProductCode(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetProductCodeW(jitter):
    msi_MsiGetProductCode(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiEnumProducts(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiEnumProducts(
        DWORD iProductIndex,
        LPTSTR lpProductBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["iProductIndex", "lpProductBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumProductsA(jitter):
    msi_MsiEnumProducts(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEnumProductsW(jitter):
    msi_MsiEnumProducts(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiEnumProductsEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiEnumProductsEx(
        LPCTSTR szProductCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        DWORD dwIndex,
        TCHAR [39] szInstalledProductCode,
        MSIINSTALLCONTEXT* pdwInstalledContext,
        LPTSTR szSid,
        LPDWORD pcchSid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szUserSid", "dwContext", "dwIndex", "szInstalledProductCode", "pdwInstalledContext", "szSid", "pcchSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumProductsExA(jitter):
    msi_MsiEnumProductsEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEnumProductsExW(jitter):
    msi_MsiEnumProductsEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiEnumRelatedProducts(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiEnumRelatedProducts(
        LPCTSTR lpUpgradeCode,
        DWORD dwReserved,
        DWORD iProductIndex,
        LPTSTR lpProductBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpUpgradeCode", "dwReserved", "iProductIndex", "lpProductBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumRelatedProductsA(jitter):
    msi_MsiEnumRelatedProducts(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEnumRelatedProductsW(jitter):
    msi_MsiEnumRelatedProducts(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiEnumFeatures(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiEnumFeatures(
        LPCTSTR szProduct,
        DWORD iFeatureIndex,
        LPTSTR lpFeatureBuf,
        LPTSTR lpParentBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "iFeatureIndex", "lpFeatureBuf", "lpParentBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumFeaturesA(jitter):
    msi_MsiEnumFeatures(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEnumFeaturesW(jitter):
    msi_MsiEnumFeatures(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiEnumComponents(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiEnumComponents(
        DWORD iComponentIndex,
        LPTSTR lpComponentBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["iComponentIndex", "lpComponentBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumComponentsA(jitter):
    msi_MsiEnumComponents(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEnumComponentsW(jitter):
    msi_MsiEnumComponents(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiEnumComponentsEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiEnumComponentsEx(
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        DWORD dwIndex,
        TCHAR [39] szInstalledComponentCode,
        MSIINSTALLCONTEXT* pdwInstalledContext,
        LPTSTR szSid,
        LPDWORD pcchSid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szUserSid", "dwContext", "dwIndex", "szInstalledComponentCode", "pdwInstalledContext", "szSid", "pcchSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumComponentsExA(jitter):
    msi_MsiEnumComponentsEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEnumComponentsExW(jitter):
    msi_MsiEnumComponentsEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiEnumClients(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiEnumClients(
        LPCTSTR szComponent,
        DWORD iProductIndex,
        LPTSTR lpProductBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "iProductIndex", "lpProductBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumClientsA(jitter):
    msi_MsiEnumClients(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEnumClientsW(jitter):
    msi_MsiEnumClients(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiEnumClientsEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiEnumClientsEx(
        LPCTSTR szComponent,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        DWORD dwProductIndex,
        TCHAR [39] szProductBuf,
        MSIINSTALLCONTEXT* pdwInstalledContext,
        LPTSTR szSid,
        LPDWORD pcchSid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "szUserSid", "dwContext", "dwProductIndex", "szProductBuf", "pdwInstalledContext", "szSid", "pcchSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumClientsExA(jitter):
    msi_MsiEnumClientsEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEnumClientsExW(jitter):
    msi_MsiEnumClientsEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiEnumComponentQualifiers(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiEnumComponentQualifiers(
        LPTSTR szComponent,
        DWORD iIndex,
        LPTSTR lpQualifierBuf,
        DWORD* pcchQualifierBuf,
        LPTSTR lpApplicationDataBuf,
        DWORD* pcchApplicationDataBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "iIndex", "lpQualifierBuf", "pcchQualifierBuf", "lpApplicationDataBuf", "pcchApplicationDataBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumComponentQualifiersA(jitter):
    msi_MsiEnumComponentQualifiers(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEnumComponentQualifiersW(jitter):
    msi_MsiEnumComponentQualifiers(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiQueryFeatureState(jitter, get_str, set_str):
    """
    INSTALLSTATE MsiQueryFeatureState(
        LPCTSTR szProduct,
        LPCTSTR szFeature
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiQueryFeatureStateA(jitter):
    msi_MsiQueryFeatureState(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiQueryFeatureStateW(jitter):
    msi_MsiQueryFeatureState(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiQueryFeatureStateEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiQueryFeatureStateEx(
        LPTSTR szProductCode,
        LPTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        LPCTSTR szFeature,
        INSTALLSTATE* pdwState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szUserSid", "dwContext", "szFeature", "pdwState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiQueryFeatureStateExA(jitter):
    msi_MsiQueryFeatureStateEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiQueryFeatureStateExW(jitter):
    msi_MsiQueryFeatureStateEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiQueryProductState(jitter, get_str, set_str):
    """
    INSTALLSTATE MsiQueryProductState(
        LPCTSTR szProduct
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiQueryProductStateA(jitter):
    msi_MsiQueryProductState(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiQueryProductStateW(jitter):
    msi_MsiQueryProductState(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetFeatureUsage(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetFeatureUsage(
        LPCTSTR szProduct,
        LPCTSTR szFeature,
        DWORD* pdwUseCount,
        WORD* pwDateUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature", "pdwUseCount", "pwDateUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFeatureUsageA(jitter):
    msi_MsiGetFeatureUsage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetFeatureUsageW(jitter):
    msi_MsiGetFeatureUsage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetProductInfo(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetProductInfo(
        LPCTSTR szProduct,
        LPCTSTR szProperty,
        LPTSTR lpValueBuf,
        DWORD* pcchValueBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szProperty", "lpValueBuf", "pcchValueBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetProductInfoA(jitter):
    msi_MsiGetProductInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetProductInfoW(jitter):
    msi_MsiGetProductInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetProductInfoEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetProductInfoEx(
        LPCTSTR szProductCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        LPCTSTR szProperty,
        LPTSTR lpValue,
        LPDWORD pcchValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szUserSid", "dwContext", "szProperty", "lpValue", "pcchValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetProductInfoExA(jitter):
    msi_MsiGetProductInfoEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetProductInfoExW(jitter):
    msi_MsiGetProductInfoEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetUserInfo(jitter, get_str, set_str):
    """
    USERINFOSTATE MsiGetUserInfo(
        LPCTSTR szProduct,
        LPTSTR lpUserNameBuf,
        DWORD* pcchUserNameBuf,
        LPTSTR lpOrgNameBuf,
        DWORD* pcchOrgNameBuf,
        LPTSTR lpSerialBuf,
        DWORD* pcchSerialBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "lpUserNameBuf", "pcchUserNameBuf", "lpOrgNameBuf", "pcchOrgNameBuf", "lpSerialBuf", "pcchSerialBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetUserInfoA(jitter):
    msi_MsiGetUserInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetUserInfoW(jitter):
    msi_MsiGetUserInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiOpenProduct(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiOpenProduct(
        LPCTSTR szProduct,
        MSIHANDLE* hProduct
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "hProduct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiOpenProductA(jitter):
    msi_MsiOpenProduct(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiOpenProductW(jitter):
    msi_MsiOpenProduct(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiOpenPackage(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiOpenPackage(
        LPCTSTR szPackagePath,
        MSIHANDLE* hProduct
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szPackagePath", "hProduct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiOpenPackageA(jitter):
    msi_MsiOpenPackage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiOpenPackageW(jitter):
    msi_MsiOpenPackage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiOpenPackageEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiOpenPackageEx(
        LPCTSTR szPackagePath,
        [MsiOpenPackageFlags] dwOptions,
        MSIHANDLE* hProduct
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szPackagePath", "dwOptions", "hProduct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiOpenPackageExA(jitter):
    msi_MsiOpenPackageEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiOpenPackageExW(jitter):
    msi_MsiOpenPackageEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiIsProductElevated(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiIsProductElevated(
        LPCTSTR szProductCode,
        BOOL* pfElevated
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "pfElevated"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiIsProductElevatedA(jitter):
    msi_MsiIsProductElevated(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiIsProductElevatedW(jitter):
    msi_MsiIsProductElevated(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetProductInfoFromScript(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetProductInfoFromScript(
        LPCTSTR szScriptFile,
        LPTSTR lpProductBuf39,
        LANGID* plgidLanguage,
        DWORD* pdwVersion,
        LPTSTR lpNameBuf,
        DWORD* pcchNameBuf,
        LPTSTR lpPackageBuf,
        DWORD* pcchPackageBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szScriptFile", "lpProductBuf39", "plgidLanguage", "pdwVersion", "lpNameBuf", "pcchNameBuf", "lpPackageBuf", "pcchPackageBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetProductInfoFromScriptA(jitter):
    msi_MsiGetProductInfoFromScript(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetProductInfoFromScriptW(jitter):
    msi_MsiGetProductInfoFromScript(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetProductProperty(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetProductProperty(
        MSIHANDLE hProduct,
        LPCTSTR szProperty,
        LPTSTR lpValueBuf,
        DWORD* pcchValueBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProduct", "szProperty", "lpValueBuf", "pcchValueBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetProductPropertyA(jitter):
    msi_MsiGetProductProperty(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetProductPropertyW(jitter):
    msi_MsiGetProductProperty(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetShortcutTarget(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetShortcutTarget(
        LPCTSTR szShortcutTarget,
        LPTSTR szProductCode,
        LPTSTR szFeatureId,
        LPTSTR szComponentCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szShortcutTarget", "szProductCode", "szFeatureId", "szComponentCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetShortcutTargetA(jitter):
    msi_MsiGetShortcutTarget(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetShortcutTargetW(jitter):
    msi_MsiGetShortcutTarget(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetFeatureInfo(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetFeatureInfo(
        MSIHANDLE hProduct,
        LPCTSTR szFeature,
        [MsiInstallFeatureAttr*] lpAttributes,
        LPTSTR lpTitleBuf,
        LPDWORD pcchTitleBuf,
        LPTSTR lpHelpBuf,
        LPDWORD pcchHelpBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProduct", "szFeature", "lpAttributes", "lpTitleBuf", "pcchTitleBuf", "lpHelpBuf", "pcchHelpBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFeatureInfoA(jitter):
    msi_MsiGetFeatureInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetFeatureInfoW(jitter):
    msi_MsiGetFeatureInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiVerifyPackage(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiVerifyPackage(
        LPCTSTR szPackagePath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szPackagePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiVerifyPackageA(jitter):
    msi_MsiVerifyPackage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiVerifyPackageW(jitter):
    msi_MsiVerifyPackage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiApplyPatch(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiApplyPatch(
        LPCTSTR szPatchPackage,
        LPCTSTR szInstallPackage,
        INSTALLTYPE eInstallType,
        LPCTSTR szCommandLine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szPatchPackage", "szInstallPackage", "eInstallType", "szCommandLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiApplyPatchA(jitter):
    msi_MsiApplyPatch(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiApplyPatchW(jitter):
    msi_MsiApplyPatch(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiEnumPatches(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiEnumPatches(
        LPCTSTR szProduct,
        DWORD iPatchIndex,
        LPTSTR lpPatchBuf,
        LPTSTR lpTransformsBuf,
        DWORD* pcchTransformsBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "iPatchIndex", "lpPatchBuf", "lpTransformsBuf", "pcchTransformsBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumPatchesA(jitter):
    msi_MsiEnumPatches(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEnumPatchesW(jitter):
    msi_MsiEnumPatches(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetPatchInfo(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetPatchInfo(
        LPCTSTR szPatch,
        LPCTSTR szAttribute,
        LPTSTR lpValueBuf,
        DWORD* pcchValueBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szPatch", "szAttribute", "lpValueBuf", "pcchValueBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetPatchInfoA(jitter):
    msi_MsiGetPatchInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetPatchInfoW(jitter):
    msi_MsiGetPatchInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiRemovePatches(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiRemovePatches(
        LPCTSTR szPatchList,
        LPCTSTR szProductCode,
        INSTALLTYPE eUninstallType,
        LPCTSTR szPropertyList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szPatchList", "szProductCode", "eUninstallType", "szPropertyList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRemovePatchesA(jitter):
    msi_MsiRemovePatches(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiRemovePatchesW(jitter):
    msi_MsiRemovePatches(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiDeterminePatchSequence(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiDeterminePatchSequence(
        LPCTSTR szProductCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        DWORD cPatchInfo,
        PMSIPATCHSEQUENCEINFO pPatchInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szUserSid", "dwContext", "cPatchInfo", "pPatchInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDeterminePatchSequenceA(jitter):
    msi_MsiDeterminePatchSequence(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiDeterminePatchSequenceW(jitter):
    msi_MsiDeterminePatchSequence(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiApplyMultiplePatches(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiApplyMultiplePatches(
        LPCTSTR szPatchPackages,
        LPCTSTR szProductCode,
        LPCTSTR szPropertiesList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szPatchPackages", "szProductCode", "szPropertiesList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiApplyMultiplePatchesA(jitter):
    msi_MsiApplyMultiplePatches(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiApplyMultiplePatchesW(jitter):
    msi_MsiApplyMultiplePatches(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiEnumPatchesEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiEnumPatchesEx(
        LPCTSTR szProductCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        [MsiPatchState] dwFilter,
        DWORD dwIndex,
        TCHAR [39] szPatchCode,
        TCHAR [39] szTargetProductCode,
        MSIINSTALLCONTEXT* pdwTargetProductContext,
        LPTSTR szTargetUserSid,
        LPDWORD pcchTargetUserSid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szUserSid", "dwContext", "dwFilter", "dwIndex", "szPatchCode", "szTargetProductCode", "pdwTargetProductContext", "szTargetUserSid", "pcchTargetUserSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumPatchesExA(jitter):
    msi_MsiEnumPatchesEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEnumPatchesExW(jitter):
    msi_MsiEnumPatchesEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetPatchFileList(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetPatchFileList(
        LPCTSTR szProductCode,
        LPCTSTR szPatchList,
        LPDWORD pcFiles,
        MSIHANDLE** pphFileRecords
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szPatchList", "pcFiles", "pphFileRecords"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetPatchFileListA(jitter):
    msi_MsiGetPatchFileList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetPatchFileListW(jitter):
    msi_MsiGetPatchFileList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetPatchInfoEx(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetPatchInfoEx(
        LPCTSTR szPatchCode,
        LPCTSTR szProductCode,
        LPCTSTR szUserSid,
        MSIINSTALLCONTEXT dwContext,
        LPCTSTR szProperty,
        LPTSTR lpValue,
        DWORD* pcchValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szPatchCode", "szProductCode", "szUserSid", "dwContext", "szProperty", "lpValue", "pcchValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetPatchInfoExA(jitter):
    msi_MsiGetPatchInfoEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetPatchInfoExW(jitter):
    msi_MsiGetPatchInfoEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiExtractPatchXMLData(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiExtractPatchXMLData(
        LPCTSTR szPatchPath,
        DWORD dwReserved,
        LPTSTR szXMLData,
        DWORD* pcchXMLData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szPatchPath", "dwReserved", "szXMLData", "pcchXMLData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiExtractPatchXMLDataA(jitter):
    msi_MsiExtractPatchXMLData(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiExtractPatchXMLDataW(jitter):
    msi_MsiExtractPatchXMLData(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiDetermineApplicablePatches(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiDetermineApplicablePatches(
        LPCTSTR szProductPackagePath,
        DWORD cPatchInfo,
        PMSIPATCHSEQUENCEINFO pPatchInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szProductPackagePath", "cPatchInfo", "pPatchInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDetermineApplicablePatchesA(jitter):
    msi_MsiDetermineApplicablePatches(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiDetermineApplicablePatchesW(jitter):
    msi_MsiDetermineApplicablePatches(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetFileHash(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetFileHash(
        LPCTSTR szFilePath,
        DWORD dwOptions,
        PMSIFILEHASHINFO pHash
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szFilePath", "dwOptions", "pHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFileHashA(jitter):
    msi_MsiGetFileHash(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetFileHashW(jitter):
    msi_MsiGetFileHash(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetFileSignatureInformation(jitter, get_str, set_str):
    """
    HRESULT MsiGetFileSignatureInformation(
        LPCTSTR szSignedObjectPath,
        [MsiHashFlags] dwFlags,
        PCCERT_CONTEXT* ppcCertContext,
        BYTE* pbHashData,
        DWORD* pcbHashData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szSignedObjectPath", "dwFlags", "ppcCertContext", "pbHashData", "pcbHashData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFileSignatureInformationA(jitter):
    msi_MsiGetFileSignatureInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetFileSignatureInformationW(jitter):
    msi_MsiGetFileSignatureInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetFileVersion(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetFileVersion(
        LPCTSTR szFilePath,
        LPTSTR lpVersionBuf,
        DWORD* pcchVersionBuf,
        LPTSTR lpLangBuf,
        DWORD* pcchLangBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szFilePath", "lpVersionBuf", "pcchVersionBuf", "lpLangBuf", "pcchLangBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFileVersionA(jitter):
    msi_MsiGetFileVersion(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetFileVersionW(jitter):
    msi_MsiGetFileVersion(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiBeginTransaction(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiBeginTransaction(
        LPCWSTR szTransactionName,
        [MsiTransactionAttributes] dwTransactionAttributes,
        MSIHANDLE* hTransactionID,
        HANDLE* phChangeOfOwnerEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szTransactionName", "dwTransactionAttributes", "hTransactionID", "phChangeOfOwnerEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiBeginTransactionA(jitter):
    msi_MsiBeginTransaction(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiBeginTransactionW(jitter):
    msi_MsiBeginTransaction(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiJoinTransaction(jitter):
    """
    [MSI_ERROR] MsiJoinTransaction(
        MSIHANDLE hTransactionID,
        [MsiTransactionAttributes] dwTransactionAttributes,
        HANDLE* phChangeOfOwnerEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hTransactionID", "dwTransactionAttributes", "phChangeOfOwnerEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEndTransaction(jitter):
    """
    [MSI_ERROR] MsiEndTransaction(
        [MsiTransactionState] dwTransactionState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTransactionState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseCommit(jitter):
    """
    [MSI_ERROR] MsiDatabaseCommit(
        MSIHANDLE hDatabase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDatabase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseGetPrimaryKeys(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiDatabaseGetPrimaryKeys(
        MSIHANDLE hDatabase,
        LPCTSTR szTableName,
        MSIHANDLE* phRecord
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szTableName", "phRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseGetPrimaryKeysA(jitter):
    msi_MsiDatabaseGetPrimaryKeys(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiDatabaseGetPrimaryKeysW(jitter):
    msi_MsiDatabaseGetPrimaryKeys(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiDatabaseIsTablePersistent(jitter, get_str, set_str):
    """
    MSICONDITION MsiDatabaseIsTablePersistent(
        MSIHANDLE hDatabase,
        LPCTSTR szTableName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szTableName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseIsTablePersistentA(jitter):
    msi_MsiDatabaseIsTablePersistent(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiDatabaseIsTablePersistentW(jitter):
    msi_MsiDatabaseIsTablePersistent(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiDatabaseOpenView(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiDatabaseOpenView(
        MSIHANDLE hDatabase,
        LPCTSTR szQuery,
        MSIHANDLE* phView
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szQuery", "phView"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseOpenViewA(jitter):
    msi_MsiDatabaseOpenView(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiDatabaseOpenViewW(jitter):
    msi_MsiDatabaseOpenView(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetActiveDatabase(jitter):
    """
    MSIHANDLE MsiGetActiveDatabase(
        MSIHANDLE hInstall
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiViewGetColumnInfo(jitter):
    """
    [MSI_ERROR] MsiViewGetColumnInfo(
        MSIHANDLE hView,
        MSICOLINFO eColumnInfo,
        MSIHANDLE* phRecord
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hView", "eColumnInfo", "phRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiOpenDatabase(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiOpenDatabase(
        LPCTSTR szDatabasePath,
        LPCTSTR szPersist,
        MSIHANDLE* phDatabase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szDatabasePath", "szPersist", "phDatabase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiOpenDatabaseA(jitter):
    msi_MsiOpenDatabase(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiOpenDatabaseW(jitter):
    msi_MsiOpenDatabase(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiViewClose(jitter):
    """
    [MSI_ERROR] MsiViewClose(
        MSIHANDLE hView
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hView"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiViewExecute(jitter):
    """
    [MSI_ERROR] MsiViewExecute(
        MSIHANDLE hView,
        MSIHANDLE hRecord
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hView", "hRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiViewFetch(jitter):
    """
    [MSI_ERROR] MsiViewFetch(
        MSIHANDLE hView,
        MSIHANDLE* phRecord
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hView", "phRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiViewGetError(jitter, get_str, set_str):
    """
    MSIDBERROR MsiViewGetError(
        MSIHANDLE hView,
        LPTSTR szColumnNameBuffer,
        DWORD* pcchBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hView", "szColumnNameBuffer", "pcchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiViewGetErrorA(jitter):
    msi_MsiViewGetError(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiViewGetErrorW(jitter):
    msi_MsiViewGetError(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiViewModify(jitter):
    """
    [MSI_ERROR] MsiViewModify(
        MSIHANDLE hView,
        MSIMODIFY eModifyMode,
        MSIHANDLE hRecord
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hView", "eModifyMode", "hRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiCreateTransformSummaryInfo(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiCreateTransformSummaryInfo(
        MSIHANDLE hDatabase,
        MSIHANDLE hDatabaseReference,
        LPCTSTR szTransformFile,
        MSITRANSFORM_ERROR iErrorConditions,
        MSITRANSFORM_VALIDATE iValidation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "hDatabaseReference", "szTransformFile", "iErrorConditions", "iValidation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiCreateTransformSummaryInfoA(jitter):
    msi_MsiCreateTransformSummaryInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiCreateTransformSummaryInfoW(jitter):
    msi_MsiCreateTransformSummaryInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiDatabaseApplyTransform(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiDatabaseApplyTransform(
        MSIHANDLE hDatabase,
        LPCTSTR szTransformFile,
        MSITRANSFORM_ERROR iErrorConditions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szTransformFile", "iErrorConditions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseApplyTransformA(jitter):
    msi_MsiDatabaseApplyTransform(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiDatabaseApplyTransformW(jitter):
    msi_MsiDatabaseApplyTransform(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiDatabaseExport(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiDatabaseExport(
        MSIHANDLE hDatabase,
        LPCTSTR szTableName,
        LPCTSTR szFolderPath,
        LPCTSTR szFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szTableName", "szFolderPath", "szFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseExportA(jitter):
    msi_MsiDatabaseExport(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiDatabaseExportW(jitter):
    msi_MsiDatabaseExport(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiDatabaseGenerateTransform(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiDatabaseGenerateTransform(
        MSIHANDLE hDatabase,
        MSIHANDLE hDatabaseReference,
        LPCTSTR szTransformFile,
        int iReserved1,
        int iReserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "hDatabaseReference", "szTransformFile", "iReserved1", "iReserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseGenerateTransformA(jitter):
    msi_MsiDatabaseGenerateTransform(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiDatabaseGenerateTransformW(jitter):
    msi_MsiDatabaseGenerateTransform(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiDatabaseImport(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiDatabaseImport(
        MSIHANDLE hDatabase,
        LPCTSTR szFolderPath,
        LPCTSTR szFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szFolderPath", "szFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseImportA(jitter):
    msi_MsiDatabaseImport(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiDatabaseImportW(jitter):
    msi_MsiDatabaseImport(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiDatabaseMerge(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiDatabaseMerge(
        MSIHANDLE hDatabase,
        MSIHANDLE hDatabaseMerge,
        LPCTSTR szTableName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "hDatabaseMerge", "szTableName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseMergeA(jitter):
    msi_MsiDatabaseMerge(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiDatabaseMergeW(jitter):
    msi_MsiDatabaseMerge(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetDatabaseState(jitter):
    """
    MSIDBSTATE MsiGetDatabaseState(
        MSIHANDLE hDatabase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDatabase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiCreateRecord(jitter):
    """
    MSIHANDLE MsiCreateRecord(
        unsigned int cParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiFormatRecord(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiFormatRecord(
        MSIHANDLE hInstall,
        MSIHANDLE hRecord,
        LPTSTR szResultBuf,
        DWORD* pcchResultBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "hRecord", "szResultBuf", "pcchResultBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiFormatRecordA(jitter):
    msi_MsiFormatRecord(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiFormatRecordW(jitter):
    msi_MsiFormatRecord(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiRecordClearData(jitter):
    """
    [MSI_ERROR] MsiRecordClearData(
        MSIHANDLE hRecord
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordDataSize(jitter):
    """
    [MSI_ERROR] MsiRecordDataSize(
        MSIHANDLE hRecord,
        unsigned int iField
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordGetFieldCount(jitter):
    """
    [MSI_ERROR] MsiRecordGetFieldCount(
        MSIHANDLE hRecord
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordGetInteger(jitter):
    """
    int MsiRecordGetInteger(
        MSIHANDLE hRecord,
        unsigned int iField
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordGetString(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiRecordGetString(
        MSIHANDLE hRecord,
        unsigned int iField,
        LPTSTR szValueBuf,
        DWORD* pcchValueBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField", "szValueBuf", "pcchValueBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordGetStringA(jitter):
    msi_MsiRecordGetString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiRecordGetStringW(jitter):
    msi_MsiRecordGetString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiRecordIsNull(jitter):
    """
    BOOL MsiRecordIsNull(
        MSIHANDLE hRecord,
        unsigned int iField
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordReadStream(jitter):
    """
    [MSI_ERROR] MsiRecordReadStream(
        MSIHANDLE hRecord,
        UINT iField,
        char* szDataBuf,
        DWORD* pcbDataBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField", "szDataBuf", "pcbDataBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordSetInteger(jitter):
    """
    [MSI_ERROR] MsiRecordSetInteger(
        MSIHANDLE hRecord,
        unsigned int iField,
        int iValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField", "iValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordSetStream(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiRecordSetStream(
        MSIHANDLE hRecord,
        UINT iField,
        LPCTSTR szFilePath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField", "szFilePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordSetStreamA(jitter):
    msi_MsiRecordSetStream(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiRecordSetStreamW(jitter):
    msi_MsiRecordSetStream(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiRecordSetString(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiRecordSetString(
        MSIHANDLE hRecord,
        unsigned int iField,
        LPCTSTR szValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField", "szValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordSetStringA(jitter):
    msi_MsiRecordSetString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiRecordSetStringW(jitter):
    msi_MsiRecordSetString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetSummaryInformation(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetSummaryInformation(
        MSIHANDLE hDatabase,
        LPCTSTR szDatabasePath,
        UINT uiUpdateCount,
        MSIHANDLE* phSummaryInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szDatabasePath", "uiUpdateCount", "phSummaryInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetSummaryInformationA(jitter):
    msi_MsiGetSummaryInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetSummaryInformationW(jitter):
    msi_MsiGetSummaryInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSummaryInfoGetProperty(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSummaryInfoGetProperty(
        MSIHANDLE hSummaryInfo,
        [MSI_PID] uiProperty,
        [MSI_DATA_TYPE*] puiDataType,
        INT* piValue,
        FILETIME* pftValue,
        LPTSTR szValueBuf,
        DWORD* pcchValueBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSummaryInfo", "uiProperty", "puiDataType", "piValue", "pftValue", "szValueBuf", "pcchValueBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSummaryInfoGetPropertyA(jitter):
    msi_MsiSummaryInfoGetProperty(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSummaryInfoGetPropertyW(jitter):
    msi_MsiSummaryInfoGetProperty(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSummaryInfoGetPropertyCount(jitter):
    """
    [MSI_ERROR] MsiSummaryInfoGetPropertyCount(
        MSIHANDLE hSummaryInfo,
        UINT* puiPropertyCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSummaryInfo", "puiPropertyCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSummaryInfoPersist(jitter):
    """
    [MSI_ERROR] MsiSummaryInfoPersist(
        MSIHANDLE hSummaryInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSummaryInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSummaryInfoSetProperty(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSummaryInfoSetProperty(
        MSIHANDLE hSummaryInfo,
        [MSI_PID] uiProperty,
        [MSI_DATA_TYPE] uiDataType,
        INT iValue,
        FILETIME* pftValue,
        LPTSTR szValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSummaryInfo", "uiProperty", "uiDataType", "iValue", "pftValue", "szValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSummaryInfoSetPropertyA(jitter):
    msi_MsiSummaryInfoSetProperty(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSummaryInfoSetPropertyW(jitter):
    msi_MsiSummaryInfoSetProperty(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetLanguage(jitter):
    """
    LANGID MsiGetLanguage(
        MSIHANDLE hInstall
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetLastErrorRecord(jitter):
    """
    MSIHANDLE MsiGetLastErrorRecord()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetMode(jitter):
    """
    BOOL MsiGetMode(
        MSIHANDLE hInstall,
        MSIRUNMODE iRunMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "iRunMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetProperty(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetProperty(
        MSIHANDLE hInstall,
        LPCTSTR szName,
        LPTSTR szValueBuf,
        DWORD* pchValueBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szName", "szValueBuf", "pchValueBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetPropertyA(jitter):
    msi_MsiGetProperty(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetPropertyW(jitter):
    msi_MsiGetProperty(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSetProperty(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSetProperty(
        MSIHANDLE hInstall,
        LPCTSTR szName,
        LPCTSTR szValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szName", "szValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetPropertyA(jitter):
    msi_MsiSetProperty(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSetPropertyW(jitter):
    msi_MsiSetProperty(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSetMode(jitter):
    """
    [MSI_ERROR] MsiSetMode(
        MSIHANDLE hInstall,
        unsigned int iRunMode,
        BOOL fState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "iRunMode", "fState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDoAction(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiDoAction(
        MSIHANDLE hInstall,
        LPCTSTR szAction
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szAction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDoActionA(jitter):
    msi_MsiDoAction(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiDoActionW(jitter):
    msi_MsiDoAction(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiEvaluateCondition(jitter, get_str, set_str):
    """
    MSICONDITION MsiEvaluateCondition(
        MSIHANDLE hInstall,
        LPCTSTR szCondition
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szCondition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEvaluateConditionA(jitter):
    msi_MsiEvaluateCondition(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEvaluateConditionW(jitter):
    msi_MsiEvaluateCondition(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiProcessMessage(jitter):
    """
    int MsiProcessMessage(
        MSIHANDLE hInstall,
        INSTALLMESSAGE eMessageType,
        MSIHANDLE hRecord
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "eMessageType", "hRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSequence(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSequence(
        MSIHANDLE hInstall,
        LPCTSTR szTable,
        INT iSequenceMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szTable", "iSequenceMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSequenceA(jitter):
    msi_MsiSequence(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSequenceW(jitter):
    msi_MsiSequence(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetSourcePath(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetSourcePath(
        MSIHANDLE hInstall,
        LPCTSTR szFolder,
        LPTSTR szPathBuf,
        DWORD* pcchPathBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFolder", "szPathBuf", "pcchPathBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetSourcePathA(jitter):
    msi_MsiGetSourcePath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetSourcePathW(jitter):
    msi_MsiGetSourcePath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetTargetPath(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetTargetPath(
        MSIHANDLE hInstall,
        LPCTSTR szFolder,
        LPTSTR szPathBuf,
        DWORD* pcchPathBuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFolder", "szPathBuf", "pcchPathBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetTargetPathA(jitter):
    msi_MsiGetTargetPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetTargetPathW(jitter):
    msi_MsiGetTargetPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSetTargetPath(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSetTargetPath(
        MSIHANDLE hInstall,
        LPCTSTR szFolder,
        LPCTSTR szFolderPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFolder", "szFolderPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetTargetPathA(jitter):
    msi_MsiSetTargetPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSetTargetPathW(jitter):
    msi_MsiSetTargetPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiEnumComponentCosts(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiEnumComponentCosts(
        MSIHANDLE hInstall,
        LPCTSTR szComponent,
        DWORD dwIndex,
        INSTALLSTATE iState,
        LPTSTR lpDriveBuf,
        DWORD* pcchDriveBuf,
        int* piCost,
        int* pTempCost
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szComponent", "dwIndex", "iState", "lpDriveBuf", "pcchDriveBuf", "piCost", "pTempCost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumComponentCostsA(jitter):
    msi_MsiEnumComponentCosts(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiEnumComponentCostsW(jitter):
    msi_MsiEnumComponentCosts(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetComponentState(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetComponentState(
        MSIHANDLE hInstall,
        LPCTSTR szComponent,
        INSTALLSTATE* piInstalled,
        INSTALLSTATE* piAction
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szComponent", "piInstalled", "piAction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetComponentStateA(jitter):
    msi_MsiGetComponentState(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetComponentStateW(jitter):
    msi_MsiGetComponentState(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetFeatureCost(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetFeatureCost(
        MSIHANDLE hInstall,
        LPCTSTR szFeature,
        MSICOSTTREE iCostTree,
        INSTALLSTATE iState,
        INT* piCost
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFeature", "iCostTree", "iState", "piCost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFeatureCostA(jitter):
    msi_MsiGetFeatureCost(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetFeatureCostW(jitter):
    msi_MsiGetFeatureCost(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetFeatureState(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetFeatureState(
        MSIHANDLE hInstall,
        LPCTSTR szFeature,
        INSTALLSTATE* piInstalled,
        INSTALLSTATE* piAction
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFeature", "piInstalled", "piAction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFeatureStateA(jitter):
    msi_MsiGetFeatureState(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetFeatureStateW(jitter):
    msi_MsiGetFeatureState(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiGetFeatureValidStates(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiGetFeatureValidStates(
        MSIHANDLE hInstall,
        LPCTSTR szFeature,
        [INSTALLSTATE-DWORD*] pInstallState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFeature", "pInstallState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFeatureValidStatesA(jitter):
    msi_MsiGetFeatureValidStates(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiGetFeatureValidStatesW(jitter):
    msi_MsiGetFeatureValidStates(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSetComponentState(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSetComponentState(
        MSIHANDLE hInstall,
        LPCTSTR szComponent,
        INSTALLSTATE iState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szComponent", "iState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetComponentStateA(jitter):
    msi_MsiSetComponentState(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSetComponentStateW(jitter):
    msi_MsiSetComponentState(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSetFeatureAttributes(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSetFeatureAttributes(
        MSIHANDLE hInstall,
        LPCTSTR szFeature,
        [MsiInstallFeatureAttr] dwAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFeature", "dwAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetFeatureAttributesA(jitter):
    msi_MsiSetFeatureAttributes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSetFeatureAttributesW(jitter):
    msi_MsiSetFeatureAttributes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSetFeatureState(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiSetFeatureState(
        MSIHANDLE hInstall,
        LPCTSTR szFeature,
        INSTALLSTATE iState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFeature", "iState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetFeatureStateA(jitter):
    msi_MsiSetFeatureState(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiSetFeatureStateW(jitter):
    msi_MsiSetFeatureState(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiSetInstallLevel(jitter):
    """
    [MSI_ERROR] MsiSetInstallLevel(
        MSIHANDLE hInstall,
        int iInstallLevel
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "iInstallLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiVerifyDiskSpace(jitter):
    """
    [MSI_ERROR] MsiVerifyDiskSpace(
        MSIHANDLE hInstall
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstall"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnableUIPreview(jitter):
    """
    [MSI_ERROR] MsiEnableUIPreview(
        MSIHANDLE hDatabase,
        MSIHANDLE* phPreview
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "phPreview"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiPreviewBillboard(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiPreviewBillboard(
        MSIHANDLE hPreview,
        LPCTSTR szControlName,
        LPCTSTR szBillboard
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPreview", "szControlName", "szBillboard"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiPreviewBillboardA(jitter):
    msi_MsiPreviewBillboard(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiPreviewBillboardW(jitter):
    msi_MsiPreviewBillboard(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msi_MsiPreviewDialog(jitter, get_str, set_str):
    """
    [MSI_ERROR] MsiPreviewDialog(
        MSIHANDLE hPreview,
        LPCTSTR szDialogName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPreview", "szDialogName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiPreviewDialogA(jitter):
    msi_MsiPreviewDialog(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msi_MsiPreviewDialogW(jitter):
    msi_MsiPreviewDialog(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
