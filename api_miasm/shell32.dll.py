
def shell32_DuplicateIcon(jitter):
    """
    [Shell32.dll] HICON DuplicateIcon(HINSTANCE hInst, HICON hIcon)
    """
    ret_ad, args = jitter.func_args_stdcall(["hInst", "hIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ExtractAssociatedIcon(jitter, get_str, set_str):
    """
    [Shell32.dll] HICON ExtractAssociatedIcon(HINSTANCE hInst, LPTSTR lpIconPath, LPWORD lpiIcon)
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
    [Shell32.dll] HICON ExtractIcon(HINSTANCE hInst, LPCTSTR lpszExeFileName, UINT nIconIndex)
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
    [Shell32.dll] UINT ExtractIconEx(LPCTSTR lpszFile, int nIconIndex, HICON* phiconLarge, HICON* phiconSmall, UINT nIcons)
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
    [Shell32.dll] HRESULT AssocCreateForClasses(const ASSOCIATIONELEMENT* rgClasses, ULONG cClasses, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["rgClasses", "cClasses", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_AssocGetDetailsOfPropKey(jitter):
    """
    [Shell32.dll] HRESULT AssocGetDetailsOfPropKey(IShellFolder* psf, PCUITEMID_CHILD pidl, PROPERTYKEY* pkey, VARIANT* pv, BOOL* pfFoundPropKey)
    """
    ret_ad, args = jitter.func_args_stdcall(["psf", "pidl", "pkey", "pv", "pfFoundPropKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CallCPLEntry16(jitter):
    """
    [Shell32.dll] int CallCPLEntry16(HINSTANCE hInst, FARPROC16 lpfnEntry, HWND hwndCPL, UINT msg, LPARAM lParam1, LPARAM lParam2)
    """
    ret_ad, args = jitter.func_args_stdcall(["hInst", "lpfnEntry", "hwndCPL", "msg", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CDefFolderMenu_Create2(jitter):
    """
    [Shell32.dll] HRESULT CDefFolderMenu_Create2(PCIDLIST_ABSOLUTE pidlFolder, HWND hwnd, UINT cidl, PCUITEMID_CHILD_ARRAY* apidl, IShellFolder* psf, LPFNDFMCALLBACK lpfn, UINT nKeys, const HKEY* ahkeys, IContextMenu** ppcm)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlFolder", "hwnd", "cidl", "apidl", "psf", "lpfn", "nKeys", "ahkeys", "ppcm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CIDLData_CreateFromIDArray(jitter):
    """
    [Shell32.dll] HRESULT CIDLData_CreateFromIDArray(PCIDLIST_ABSOLUTE pidlFolder, UINT cidl, PCUIDLIST_RELATIVE_ARRAY apidl, IDataObject** ppdtobj)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlFolder", "cidl", "apidl", "ppdtobj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CommandLineToArgvW(jitter):
    """
    [Shell32.dll] LPWSTR* CommandLineToArgvW(LPCWSTR lpCmdLine, int* pNumArgs)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpCmdLine", "pNumArgs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DAD_AutoScroll(jitter):
    """
    [Shell32.dll] BOOL DAD_AutoScroll(HWND hwnd, AUTO_SCROLL_DATA* pad, const POINT* pptNow)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pad", "pptNow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DAD_DragEnterEx(jitter):
    """
    [Shell32.dll] BOOL DAD_DragEnterEx(HWND hwndTarget, const POINT ptStart)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndTarget", "ptStart"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DAD_DragLeave(jitter):
    """
    [Shell32.dll] BOOL DAD_DragLeave()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DAD_DragMove(jitter):
    """
    [Shell32.dll] BOOL DAD_DragMove(POINT pt)
    """
    ret_ad, args = jitter.func_args_stdcall(["pt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DAD_SetDragImage(jitter):
    """
    [Shell32.dll] BOOL DAD_SetDragImage(HIMAGELIST him, POINT* pptOffset)
    """
    ret_ad, args = jitter.func_args_stdcall(["him", "pptOffset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DAD_ShowDragImage(jitter):
    """
    [Shell32.dll] BOOL DAD_ShowDragImage(BOOL fShow)
    """
    ret_ad, args = jitter.func_args_stdcall(["fShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DoEnvironmentSubst(jitter, get_str, set_str):
    """
    [Shell32.dll] DWORD DoEnvironmentSubst(LPTSTR pszString, UINT cchString)
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
    [Shell32.dll] VOID DragAcceptFiles(HWND hWnd, BOOL fAccept)
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "fAccept"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DragFinish(jitter):
    """
    [Shell32.dll] VOID DragFinish(HDROP hDrop)
    """
    ret_ad, args = jitter.func_args_stdcall(["hDrop"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DragQueryFile(jitter, get_str, set_str):
    """
    [Shell32.dll] UINT DragQueryFile(HDROP hDrop, UINT iFile, LPTSTR lpszFile, UINT cch)
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
    [Shell32.dll] BOOL DragQueryPoint(HDROP hDrop, LPPOINT lppt)
    """
    ret_ad, args = jitter.func_args_stdcall(["hDrop", "lppt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DriveType(jitter):
    """
    [Shell32.dll] int DriveType(int iDrive)
    """
    ret_ad, args = jitter.func_args_stdcall(["iDrive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ExtractAssociatedIconEx(jitter, get_str, set_str):
    """
    [Shell32.dll] HICON ExtractAssociatedIconEx(HINSTANCE hInst, LPTSTR lpIconPath, LPWORD lpiIconIndex, LPWORD lpiIconId)
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
    [Shell32.dll] BOOL FileIconInit(BOOL fRestoreCache)
    """
    ret_ad, args = jitter.func_args_stdcall(["fRestoreCache"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_FindExecutable(jitter, get_str, set_str):
    """
    [Shell32.dll] HINSTANCE FindExecutable(LPCTSTR lpFile, LPCTSTR lpDirectory, LPTSTR lpResult)
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
    [Shell32.dll] HRESULT GetCurrentProcessExplicitAppUserModelID(PWSTR* AppID)
    """
    ret_ad, args = jitter.func_args_stdcall(["AppID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_GetFileNameFromBrowse(jitter):
    """
    [Shell32.dll] BOOL GetFileNameFromBrowse(HWND hwnd, LPWSTR pszFilePath, UINT cchFilePath, LPCWSTR pszWorkingDir, LPCWSTR pszDefExt, LPCWSTR pszFilters, LPCWSTR szTitle)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszFilePath", "cchFilePath", "pszWorkingDir", "pszDefExt", "pszFilters", "szTitle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_GUIDFromString(jitter, get_str, set_str):
    """
    [Shell32.dll] BOOL GUIDFromString(LPCTSTR psz, LPGUID pguid)
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
    [Shell32.dll] PIDLIST_RELATIVE ILAppendID(PIDLIST_RELATIVE pidl, LPSHITEMID pmkid, BOOL fAppend)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "pmkid", "fAppend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILClone(jitter):
    """
    [Shell32.dll] PIDLIST_RELATIVE ILClone(PCUIDLIST_RELATIVE pidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILCloneFirst(jitter):
    """
    [Shell32.dll] PITEMID_CHILD ILCloneFirst(PCUIDLIST_RELATIVE pidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILCombine(jitter):
    """
    [Shell32.dll] PIDLIST_ABSOLUTE ILCombine(PCIDLIST_ABSOLUTE pidl1, PCUIDLIST_RELATIVE pidl2)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl1", "pidl2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILCreateFromPath(jitter):
    """
    [Shell32.dll] PIDLIST_ABSOLUTE ILCreateFromPath(LPCWSTR pszPath)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILCreateFromPath(jitter, get_str, set_str):
    """
    [Shell32.dll] PIDLIST_ABSOLUTE ILCreateFromPath(LPCSTR pszPath)
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
    [Shell32.dll] PUIDLIST_RELATIVE ILFindChild(PCIDLIST_ABSOLUTE pidlParent, PCIDLIST_ABSOLUTE pidlChild)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlParent", "pidlChild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILFindLastID(jitter):
    """
    [Shell32.dll] PUITEMID_CHILD ILFindLastID(PCUIDLIST_RELATIVE pidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILFree(jitter):
    """
    [Shell32.dll] void ILFree(PIDLIST_RELATIVE pidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILGetNext(jitter):
    """
    [Shell32.dll] PUIDLIST_RELATIVE ILGetNext(PCUIDLIST_RELATIVE pidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILGetSize(jitter):
    """
    [Shell32.dll] UINT ILGetSize(PCUIDLIST_RELATIVE pidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILIsEqual(jitter):
    """
    [Shell32.dll] BOOL ILIsEqual(PCIDLIST_ABSOLUTE pidl1, PCIDLIST_ABSOLUTE pidl2)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl1", "pidl2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILIsParent(jitter):
    """
    [Shell32.dll] BOOL ILIsParent(PCIDLIST_ABSOLUTE pidl1, PCIDLIST_ABSOLUTE pidl2, BOOL fImmediate)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl1", "pidl2", "fImmediate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILLoadFromStream(jitter):
    """
    [Shell32.dll] HRESULT ILLoadFromStream(IStream* pstm, PIDLIST_RELATIVE* pidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILRemoveLastID(jitter):
    """
    [Shell32.dll] BOOL ILRemoveLastID(PUIDLIST_RELATIVE pidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ILSaveToStream(jitter):
    """
    [Shell32.dll] HRESULT ILSaveToStream(IStream* pstm, PCUIDLIST_RELATIVE pidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_InitNetworkAddressControl(jitter):
    """
    [Shell32.dll] BOOL InitNetworkAddressControl()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_IsNetDrive(jitter):
    """
    [Shell32.dll] int IsNetDrive(int iDrive)
    """
    ret_ad, args = jitter.func_args_stdcall(["iDrive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_IsUserAnAdmin(jitter):
    """
    [Shell32.dll] BOOL IsUserAnAdmin()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_LinkWindow_RegisterClass(jitter):
    """
    [Shell32.dll] BOOL LinkWindow_RegisterClass()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_LinkWindow_UnregisterClass(jitter):
    """
    [Shell32.dll] BOOL LinkWindow_UnregisterClass()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_NTSHChangeNotifyDeregister(jitter):
    """
    [Shell32.dll] BOOL NTSHChangeNotifyDeregister(ULONG ulID)
    """
    ret_ad, args = jitter.func_args_stdcall(["ulID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHChangeNotify(jitter):
    """
    [Shell32.dll] void SHChangeNotify([ShellChangeNotifyEvent] wEventId, [ShellChangeNotifyFlag] uFlags, LPCVOID dwItem1, LPCVOID dwItem2)
    """
    ret_ad, args = jitter.func_args_stdcall(["wEventId", "uFlags", "dwItem1", "dwItem2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_NTSHChangeNotifyRegister(jitter):
    """
    [Shell32.dll] ULONG NTSHChangeNotifyRegister(HWND hwnd, int fSources, LONG fEvents, UINT wMsg, int cEntries, SHChangeNotifyEntry* pfsne)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "fSources", "fEvents", "wMsg", "cEntries", "pfsne"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_OpenRegStream(jitter):
    """
    [Shell32.dll] IStream* OpenRegStream(HKEY hkey, LPCWSTR pszSubkey, LPCWSTR pszValue, [STGM_FLAGS] grfMode)
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubkey", "pszValue", "grfMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ParseField(jitter):
    """
    [Shell32.dll] bool ParseField(LPCTSTR* szData, int n, LPTSTR* szBuf, int iBufLen)
    """
    ret_ad, args = jitter.func_args_stdcall(["szData", "n", "szBuf", "iBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathCleanupSpec(jitter):
    """
    [Shell32.dll] int PathCleanupSpec(LPCWSTR pszDir, LPWSTR pszSpec)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDir", "pszSpec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathGetShortPath(jitter):
    """
    [Shell32.dll] void PathGetShortPath(LPWSTR pszLongPath)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszLongPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathIsExe(jitter):
    """
    [Shell32.dll] int PathIsExe(LPCWSTR szfile)
    """
    ret_ad, args = jitter.func_args_stdcall(["szfile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathIsSlow(jitter, get_str, set_str):
    """
    [Shell32.dll] BOOL PathIsSlow(LPCTSTR pszFile, DWORD dwFileAttr)
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
    [Shell32.dll] BOOL PathMakeUniqueName(LPWSTR pszUniqueName, UINT cchMax, LPCWSTR pszTemplate, LPCWSTR pszLongPlate, LPCWSTR pszDir)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUniqueName", "cchMax", "pszTemplate", "pszLongPlate", "pszDir"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathProcessCommand(jitter):
    """
    [Shell32.dll] LONG PathProcessCommand(LPCWSTR lpSrc, LPWSTR lpDest, int iDestMax, [PPCF_FLAGS] dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpSrc", "lpDest", "iDestMax", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathResolve(jitter):
    """
    [Shell32.dll] BOOL PathResolve(LPWSTR pszPath, LPCWSTR* dirs, [PRF_FLAGS] fFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "dirs", "fFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathYetAnotherMakeUniqueName(jitter):
    """
    [Shell32.dll] BOOL PathYetAnotherMakeUniqueName(LPWSTR pszUniqueName, LPCWSTR pszPath, LPCWSTR pszShort, LPCWSTR pszFileSpec)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUniqueName", "pszPath", "pszShort", "pszFileSpec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PickIconDlg(jitter):
    """
    [Shell32.dll] int PickIconDlg(HWND hwnd, LPWSTR pszIconPath, UINT cchIconPath, int* piIconIndex)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszIconPath", "cchIconPath", "piIconIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ReadCabinetState(jitter):
    """
    [Shell32.dll] BOOL ReadCabinetState(CABINETSTATE* pcs, int cLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["pcs", "cLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_RealDriveType(jitter):
    """
    [Shell32.dll] int RealDriveType(int iDrive, BOOL fOKToHitNet)
    """
    ret_ad, args = jitter.func_args_stdcall(["iDrive", "fOKToHitNet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_RestartDialog(jitter):
    """
    [Shell32.dll] int RestartDialog(HWND hParent, LPCWSTR pszPrompt, [EWX_FLAGS] dwReturn)
    """
    ret_ad, args = jitter.func_args_stdcall(["hParent", "pszPrompt", "dwReturn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_RestartDialogEx(jitter):
    """
    [Shell32.dll] int RestartDialogEx(HWND hParent, LPCWSTR pszPrompt, [EWX_FLAGS] dwReturn, [SHTDN_REASON] dwReasonCode)
    """
    ret_ad, args = jitter.func_args_stdcall(["hParent", "pszPrompt", "dwReturn", "dwReasonCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SetCurrentProcessExplicitAppUserModelID(jitter):
    """
    [Shell32.dll] HRESULT SetCurrentProcessExplicitAppUserModelID(PCWSTR AppID)
    """
    ret_ad, args = jitter.func_args_stdcall(["AppID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAddFromPropSheetExtArray(jitter):
    """
    [Shell32.dll] int SHAddFromPropSheetExtArray(HPSXA hpsxa, LPFNADDPROPSHEETPAGE lpfnAddPage, LPARAM lParam)
    """
    ret_ad, args = jitter.func_args_stdcall(["hpsxa", "lpfnAddPage", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAddToRecentDocs(jitter):
    """
    [Shell32.dll] void SHAddToRecentDocs(SHARD uFlags, LPCVOID pv)
    """
    ret_ad, args = jitter.func_args_stdcall(["uFlags", "pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAlloc(jitter):
    """
    [Shell32.dll] LPVOID SHAlloc(SIZE_T cb)
    """
    ret_ad, args = jitter.func_args_stdcall(["cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAppBarMessage(jitter):
    """
    [Shell32.dll] UINT_PTR SHAppBarMessage(DWORD dwMessage, PAPPBARDATA pData)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwMessage", "pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAssocEnumHandlers(jitter):
    """
    [Shell32.dll] HRESULT SHAssocEnumHandlers(LPCWSTR pszExtra, ASSOC_FILTER afFilter, IEnumAssocHandlers** ppEnumHandler)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszExtra", "afFilter", "ppEnumHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAssocEnumHandlersForProtocolByApplication(jitter):
    """
    [Shell32.dll] HRESULT SHAssocEnumHandlersForProtocolByApplication(PCWSTR protocol, REFIID riid, void** enumHandlers)
    """
    ret_ad, args = jitter.func_args_stdcall(["protocol", "riid", "enumHandlers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHBindToFolderIDListParent(jitter):
    """
    [Shell32.dll] HRESULT SHBindToFolderIDListParent(IShellFolder* psfRoot, PCUIDLIST_RELATIVE pidl, REFIID riid, void** ppv, PCUITEMID_CHILD* ppidlLast)
    """
    ret_ad, args = jitter.func_args_stdcall(["psfRoot", "pidl", "riid", "ppv", "ppidlLast"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHBindToObject(jitter):
    """
    [Shell32.dll] HRESULT SHBindToObject(IShellFolder* psf, PCUIDLIST_RELATIVE pidl, IBindCtx* pbc, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["psf", "pidl", "pbc", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHBindToParent(jitter):
    """
    [Shell32.dll] HRESULT SHBindToParent(PCIDLIST_ABSOLUTE pidl, REFIID riid, VOID** ppv, PCUITEMID_CHILD* ppidlLast)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "riid", "ppv", "ppidlLast"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHBrowseForFolder(jitter, get_str, set_str):
    """
    [Shell32.dll] PIDLIST_ABSOLUTE SHBrowseForFolder(LPBROWSEINFO lpbi)
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
    [Shell32.dll] HANDLE SHChangeNotification_Lock(HANDLE hChange, DWORD dwProcId, PIDLIST_ABSOLUTE** pppidl, LONG* plEvent)
    """
    ret_ad, args = jitter.func_args_stdcall(["hChange", "dwProcId", "pppidl", "plEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHChangeNotification_Unlock(jitter):
    """
    [Shell32.dll] BOOL SHChangeNotification_Unlock(HANDLE hLock)
    """
    ret_ad, args = jitter.func_args_stdcall(["hLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHChangeNotifyDeregister(jitter):
    """
    [Shell32.dll] BOOL SHChangeNotifyDeregister(ULONG ulID)
    """
    ret_ad, args = jitter.func_args_stdcall(["ulID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHChangeNotifyRegister(jitter):
    """
    [Shell32.dll] ULONG SHChangeNotifyRegister(HWND hwnd, int fSources, LONG fEvents, UINT wMsg, int cEntries, const SHChangeNotifyEntry* pshcne)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "fSources", "fEvents", "wMsg", "cEntries", "pshcne"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHChangeNotifyRegisterThread(jitter):
    """
    [Shell32.dll] void SHChangeNotifyRegisterThread(SCNRT_STATUS status)
    """
    ret_ad, args = jitter.func_args_stdcall(["status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCloneSpecialIDList(jitter):
    """
    [Shell32.dll] PIDLIST_ABSOLUTE SHCloneSpecialIDList(HWND hwndOwner, [CSIDL] csidl, BOOL fCreate)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "csidl", "fCreate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCLSIDFromString(jitter):
    """
    [Shell32.dll] HRESULT SHCLSIDFromString(LPCWSTR psz, CLSID* pclsid)
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCoCreateInstance(jitter):
    """
    [Shell32.dll] HRESULT SHCoCreateInstance(LPCWSTR pszCLSID, const CLSID* pclsid, IUnknown* pUnkOuter, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszCLSID", "pclsid", "pUnkOuter", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateAssociationRegistration(jitter):
    """
    [Shell32.dll] HRESULT SHCreateAssociationRegistration(REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateDataObject(jitter):
    """
    [Shell32.dll] HRESULT SHCreateDataObject(PCIDLIST_ABSOLUTE pidlFolder, UINT cidl, PCUITEMID_CHILD_ARRAY apidl, IDataObject* pdtInner, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlFolder", "cidl", "apidl", "pdtInner", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateDefaultContextMenu(jitter):
    """
    [Shell32.dll] HRESULT SHCreateDefaultContextMenu(const DEFCONTEXTMENU* pdcm, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdcm", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateDefaultExtractIcon(jitter):
    """
    [Shell32.dll] HRESULT SHCreateDefaultExtractIcon(REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateDefaultPropertiesOp(jitter):
    """
    [Shell32.dll] HRESULT SHCreateDefaultPropertiesOp(IShellItem* psi, IFileOperation** ppFileOp)
    """
    ret_ad, args = jitter.func_args_stdcall(["psi", "ppFileOp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateDirectory(jitter):
    """
    [Shell32.dll] int SHCreateDirectory(HWND hwnd, LPCWSTR pszPath)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateDirectoryEx(jitter, get_str, set_str):
    """
    [Shell32.dll] int SHCreateDirectoryEx(HWND hwnd, LPCTSTR pszPath, const SECURITY_ATTRIBUTES* psa)
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
    [Shell32.dll] HRESULT SHCreateFileExtractIconW(LPCWSTR pszFile, [FileAttributes] dwFileAttributes, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFile", "dwFileAttributes", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateItemFromParsingName(jitter):
    """
    [Shell32.dll] HRESULT SHCreateItemFromParsingName(PCWSTR pszPath, IBindCtx* pbc, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pbc", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateItemFromRelativeName(jitter):
    """
    [Shell32.dll] HRESULT SHCreateItemFromRelativeName(IShellItem* psiParent, PCWSTR pszName, IBindCtx* pbc, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["psiParent", "pszName", "pbc", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateItemInKnownFolder(jitter):
    """
    [Shell32.dll] HRESULT SHCreateItemInKnownFolder(REFKNOWNFOLDERID kfid, [KNOWN_FOLDER_FLAG|DWORD] dwKFFlags, PCWSTR pszItem, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["kfid", "dwKFFlags", "pszItem", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateProcessAsUserW(jitter):
    """
    [Shell32.dll] BOOL SHCreateProcessAsUserW(PSHCREATEPROCESSINFOW pscpi)
    """
    ret_ad, args = jitter.func_args_stdcall(["pscpi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreatePropSheetExtArray(jitter):
    """
    [Shell32.dll] HPSXA SHCreatePropSheetExtArray(HKEY hkey, LPCWSTR pszSubkey, UINT max_iface)
    """
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubkey", "max_iface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateQueryCancelAutoPlayMoniker(jitter):
    """
    [Shell32.dll] HRESULT SHCreateQueryCancelAutoPlayMoniker(IMoniker** ppmoniker)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppmoniker"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellFolderViewEx(jitter):
    """
    [Shell32.dll] HRESULT SHCreateShellFolderViewEx(LPCSFV pcsfv, IShellView** ppsv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pcsfv", "ppsv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellFolderView(jitter):
    """
    [Shell32.dll] HRESULT SHCreateShellFolderView(const SFV_CREATE* pcsfv, IShellView** ppsv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pcsfv", "ppsv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellItem(jitter):
    """
    [Shell32.dll] HRESULT SHCreateShellItem(PCIDLIST_ABSOLUTE pidlParent, IShellFolder* psfParent, PCUITEMID_CHILD pidl, IShellItem** ppsi)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlParent", "psfParent", "pidl", "ppsi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateItemWithParent(jitter):
    """
    [Shell32.dll] HRESULT SHCreateItemWithParent(PCIDLIST_ABSOLUTE pidlParent, IShellFolder* psfParent, PCUITEMID_CHILD pidl, REFIID riid, void** ppvItem)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlParent", "psfParent", "pidl", "riid", "ppvItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateItemFromIDList(jitter):
    """
    [Shell32.dll] HRESULT SHCreateItemFromIDList(PCIDLIST_ABSOLUTE pidl, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellItemArray(jitter):
    """
    [Shell32.dll] HRESULT SHCreateShellItemArray(PCIDLIST_ABSOLUTE pidlParent, IShellFolder* psf, UINT cidl, PCUITEMID_CHILD_ARRAY ppidl, IShellItemArray** ppsiItemArray)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlParent", "psf", "cidl", "ppidl", "ppsiItemArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellItemArrayFromDataObject(jitter):
    """
    [Shell32.dll] HRESULT SHCreateShellItemArrayFromDataObject(IDataObject* pdo, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdo", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellItemArrayFromIDLists(jitter):
    """
    [Shell32.dll] HRESULT SHCreateShellItemArrayFromIDLists(UINT cidl, PCIDLIST_ABSOLUTE_ARRAY rgpidl, IShellItemArray** ppsiItemArray)
    """
    ret_ad, args = jitter.func_args_stdcall(["cidl", "rgpidl", "ppsiItemArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateShellItemArrayFromShellItem(jitter):
    """
    [Shell32.dll] HRESULT SHCreateShellItemArrayFromShellItem(IShellItem* psi, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["psi", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHCreateStdEnumFmtEtc(jitter):
    """
    [Shell32.dll] HRESULT SHCreateStdEnumFmtEtc(UINT cfmt, const FORMATETC [] afmt, IEnumFORMATETC** ppenumFormatEtc)
    """
    ret_ad, args = jitter.func_args_stdcall(["cfmt", "afmt", "ppenumFormatEtc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHDefExtractIcon(jitter, get_str, set_str):
    """
    [Shell32.dll] HRESULT SHDefExtractIcon(LPCTSTR pszIconFile, int iIndex, [SHDefExtractIcon_FLAGS] uFlags, HICON* phiconLarge, HICON* phiconSmall, UINT nIconSize)
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
    [Shell32.dll] void SHDestroyPropSheetExtArray(HPSXA hpsxa)
    """
    ret_ad, args = jitter.func_args_stdcall(["hpsxa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHDoDragDrop(jitter):
    """
    [Shell32.dll] HRESULT SHDoDragDrop(HWND hwnd, IDataObject* pdtobj, IDropSource* pdsrc, DWORD dwEffect, DWORD* pdwEffect)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pdtobj", "pdsrc", "dwEffect", "pdwEffect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Shell_GetCachedImageIndex(jitter):
    """
    [Shell32.dll] int Shell_GetCachedImageIndex(LPCWSTR pwszIconPath, int iIconIndex, UINT uIconFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszIconPath", "iIconIndex", "uIconFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Shell_GetCachedImageIndex(jitter, get_str, set_str):
    """
    [Shell32.dll] int Shell_GetCachedImageIndex(LPCTSTR pszIconPath, int iIconIndex, UINT uIconFlags)
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
    [Shell32.dll] BOOL Shell_GetImageLists(HIMAGELIST* phiml, HIMAGELIST* phimlSmall)
    """
    ret_ad, args = jitter.func_args_stdcall(["phiml", "phimlSmall"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Shell_MergeMenus(jitter):
    """
    [Shell32.dll] UINT Shell_MergeMenus(HMENU hmDst, HMENU hmSrc, UINT uInsert, UINT uIDAdjust, UINT uIDAdjustMax, [MERGE_MENU_FLAGS] uFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hmDst", "hmSrc", "uInsert", "uIDAdjust", "uIDAdjustMax", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Shell_NotifyIcon(jitter, get_str, set_str):
    """
    [Shell32.dll] BOOL Shell_NotifyIcon(DWORD dwMessage, PNOTIFYICONDATA lpdata)
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
    [Shell32.dll] HRESULT Shell_NotifyIconGetRect(const NOTIFYICONIDENTIFIER* identifier, RECT* iconLocation)
    """
    ret_ad, args = jitter.func_args_stdcall(["identifier", "iconLocation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ShellAbout(jitter, get_str, set_str):
    """
    [Shell32.dll] int ShellAbout(HWND hWnd, LPCTSTR szApp, LPCTSTR szOtherStuff, HICON hIcon)
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
    [Shell32.dll] BOOL ShellExecuteEx(LPSHELLEXECUTEINFO lpExecInfo)
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
    [Shell32.dll] HRESULT SHEmptyRecycleBin(HWND hwnd, LPCTSTR pszRootPath, [SHERB_FLAGS] dwFlags)
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
    [Shell32.dll] HRESULT SHEnumerateUnreadMailAccountsW(HKEY hKeyUser, DWORD dwIndex, LPWSTR pszMailAddress, int cchMailAddress)
    """
    ret_ad, args = jitter.func_args_stdcall(["hKeyUser", "dwIndex", "pszMailAddress", "cchMailAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHEvaluateSystemCommandTemplate(jitter):
    """
    [Shell32.dll] HRESULT SHEvaluateSystemCommandTemplate(PCWSTR pszCmdTemplate, PWSTR* ppszApplication, PWSTR* ppszCommandLine, PWSTR* ppszParameters)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszCmdTemplate", "ppszApplication", "ppszCommandLine", "ppszParameters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ShellExecute(jitter, get_str, set_str):
    """
    [Shell32.dll] HINSTANCE ShellExecute(HWND hwnd, LPCTSTR lpOperation, LPCTSTR lpFile, LPCTSTR lpParameters, LPCTSTR lpDirectory, [ShowWindowCmd] nShowCmd)
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
    [Shell32.dll] UINT SHExtractIconsW(LPCWSTR pszFileName, int nIconIndex, int cxIcon, int cyIcon, HICON* phIcon, UINT* pIconId, UINT nIcons, [LRFlags] flags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFileName", "nIconIndex", "cxIcon", "cyIcon", "phIcon", "pIconId", "nIcons", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFind_InitMenuPopup(jitter):
    """
    [Shell32.dll] IContextMenu* SHFind_InitMenuPopup(HMENU hmenu, HWND hwnd, UINT idCmdFirst, UINT idCmdLast)
    """
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "hwnd", "idCmdFirst", "idCmdLast"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFindFiles(jitter):
    """
    [Shell32.dll] BOOL SHFindFiles(PCIDLIST_ABSOLUTE pidlFolder, PCIDLIST_ABSOLUTE pidlSaveFile)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlFolder", "pidlSaveFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFlushClipboard(jitter):
    """
    [Shell32.dll] HRESULT SHFlushClipboard()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFlushSFCache(jitter):
    """
    [Shell32.dll] void SHFlushSFCache()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFormatDrive(jitter):
    """
    [Shell32.dll] DWORD SHFormatDrive(HWND hwnd, UINT drive, UINT fmtID, UINT options)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "drive", "fmtID", "options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFree(jitter):
    """
    [Shell32.dll] void SHFree(void* pv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFreeNameMappings(jitter):
    """
    [Shell32.dll] void SHFreeNameMappings(HANDLE hNameMappings)
    """
    ret_ad, args = jitter.func_args_stdcall(["hNameMappings"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHFileOperation(jitter, get_str, set_str):
    """
    [Shell32.dll] int SHFileOperation(LPSHFILEOPSTRUCT lpFileOp)
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
    [Shell32.dll] HRESULT SHGetAttributesFromDataObject(IDataObject* pdo, [SFGAOF_DWORD] dwAttributeMask, [SFGAOF_DWORD*] pdwAttributes, UINT* pcItems)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdo", "dwAttributeMask", "pdwAttributes", "pcItems"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetDataFromIDList(jitter, get_str, set_str):
    """
    [Shell32.dll] HRESULT SHGetDataFromIDList(IShellFolder* psf, PCUITEMID_CHILD pidl, [SHGetDataFromIDListFormats] nFormat, PVOID pv, int cb)
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
    [Shell32.dll] HRESULT SHGetDesktopFolder(IShellFolder** ppshf)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppshf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetDiskFreeSpace(jitter, get_str, set_str):
    """
    [Shell32.dll] BOOL SHGetDiskFreeSpace(LPCTSTR pszVolume, ULARGE_INTEGER* pqwFreeCaller, ULARGE_INTEGER* pqwTot, ULARGE_INTEGER* pqwFree)
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
    [Shell32.dll] BOOL SHGetDiskFreeSpaceEx(LPCTSTR pszVolume, ULARGE_INTEGER* pqwFreeCaller, ULARGE_INTEGER* pqwTot, ULARGE_INTEGER* pqwFree)
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
    [Shell32.dll] HRESULT SHGetDriveMedia(LPCWSTR pszDrive, DWORD* pdwMediaContent)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDrive", "pdwMediaContent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetFileInfo(jitter, get_str, set_str):
    """
    [Shell32.dll] DWORD_PTR SHGetFileInfo(LPCTSTR pszPath, [FileAttributes] dwFileAttributes, SHFILEINFO* psfi, UINT cbFileInfo, [SHGFI_FLAGS] uFlags)
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
    [Shell32.dll] HRESULT SHGetFolderLocation(HWND hwndOwner, [CSIDL] nFolder, HANDLE hToken, DWORD dwReserved, PIDLIST_ABSOLUTE* ppidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "nFolder", "hToken", "dwReserved", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetFolderPath(jitter, get_str, set_str):
    """
    [Shell32.dll] HRESULT SHGetFolderPath(HWND hwndOwner, int nFolder, HANDLE hToken, [SHGetFolderPathFlags] dwFlags, LPTSTR pszPath)
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
    [Shell32.dll] HRESULT SHGetFolderPathAndSubDir(HWND hwnd, [CSIDL] csidl, HANDLE hToken, [SHGetFolderPathFlags] dwFlags, LPCTSTR pszSubDir, LPTSTR pszPath)
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
    [Shell32.dll] int SHGetIconOverlayIndex(LPCTSTR pszIconPath, int iIconIndex)
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
    [Shell32.dll] HRESULT SHGetIDListFromObject(IUnknown* punk, PIDLIST_ABSOLUTE* ppidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["punk", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetImageList(jitter):
    """
    [Shell32.dll] HRESULT SHGetImageList(int iImageList, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["iImageList", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetInstanceExplorer(jitter):
    """
    [Shell32.dll] HRESULT SHGetInstanceExplorer(IUnknown** ppunk)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppunk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetItemFromDataObject(jitter):
    """
    [Shell32.dll] HRESULT SHGetItemFromDataObject(IDataObject* pdtobj, DATAOBJ_GET_ITEM_FLAGS dwFlags, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdtobj", "dwFlags", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetItemFromObject(jitter):
    """
    [Shell32.dll] HRESULT SHGetItemFromObject(IUnknown* punk, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["punk", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetKnownFolderIDList(jitter):
    """
    [Shell32.dll] HRESULT SHGetKnownFolderIDList(REFKNOWNFOLDERID rfid, [KNOWN_FOLDER_FLAG|DWORD] dwFlags, HANDLE hToken, PIDLIST_ABSOLUTE* ppidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["rfid", "dwFlags", "hToken", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetKnownFolderItem(jitter):
    """
    [Shell32.dll] HRESULT SHGetKnownFolderItem(REFKNOWNFOLDERID rfid, KNOWN_FOLDER_FLAG dwFlags, HANDLE hToken, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["rfid", "dwFlags", "hToken", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetKnownFolderPath(jitter):
    """
    [Shell32.dll] HRESULT SHGetKnownFolderPath(REFKNOWNFOLDERID rfid, [KNOWN_FOLDER_FLAG|DWORD] dwFlags, HANDLE hToken, PWSTR* ppszPath)
    """
    ret_ad, args = jitter.func_args_stdcall(["rfid", "dwFlags", "hToken", "ppszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetLocalizedName(jitter):
    """
    [Shell32.dll] HRESULT SHGetLocalizedName(LPCWSTR pszPath, LPWSTR pszResModule, UINT cch, int* pidsRes)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszResModule", "cch", "pidsRes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetMalloc(jitter):
    """
    [Shell32.dll] HRESULT SHGetMalloc(LPMALLOC* ppMalloc)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppMalloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetNameFromIDList(jitter):
    """
    [Shell32.dll] HRESULT SHGetNameFromIDList(PCIDLIST_ABSOLUTE pidl, SIGDN sigdnName, PWSTR* ppszName)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "sigdnName", "ppszName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetNameFromPropertyKey(jitter):
    """
    [Shell32.dll] HRESULT SHGetNameFromPropertyKey(REFPROPERTYKEY propkey, PWSTR* ppszCanonicalName)
    """
    ret_ad, args = jitter.func_args_stdcall(["propkey", "ppszCanonicalName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetNewLinkInfo(jitter, get_str, set_str):
    """
    [Shell32.dll] BOOL SHGetNewLinkInfo(LPCTSTR pszLinkTo, LPCTSTR pszDir, LPTSTR pszName, BOOL* pfMustCopy, [SHGNLI_FLAGS] uFlags)
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
    [Shell32.dll] BOOL SHGetPathFromIDListEx(PCIDLIST_ABSOLUTE pidl, PWSTR pszPath, DWORD cchPath, GPFIDL_FLAGS uOpts)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "pszPath", "cchPath", "uOpts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetPathFromIDList(jitter, get_str, set_str):
    """
    [Shell32.dll] BOOL SHGetPathFromIDList(PCIDLIST_ABSOLUTE pidl, LPTSTR pszPath)
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
    [Shell32.dll] HRESULT SHGetRealIDL(IShellFolder* psf, PCUITEMID_CHILD pidlSimple, PITEMID_CHILD* ppidlReal)
    """
    ret_ad, args = jitter.func_args_stdcall(["psf", "pidlSimple", "ppidlReal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetSetFolderCustomSettings(jitter):
    """
    [Shell32.dll] HRESULT SHGetSetFolderCustomSettings(LPSHFOLDERCUSTOMSETTINGS pfcs, LPCTSTR pszPath, DWORD dwReadWrite)
    """
    ret_ad, args = jitter.func_args_stdcall(["pfcs", "pszPath", "dwReadWrite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetSetSettings(jitter):
    """
    [Shell32.dll] void SHGetSetSettings(LPSHELLSTATE lpss, [SSF_FLAGS] dwMask, BOOL bSet)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpss", "dwMask", "bSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetSettings(jitter):
    """
    [Shell32.dll] void SHGetSettings(LPSHELLFLAGSTATE lpsfs, [SSF_FLAGS] dwMask)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpsfs", "dwMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetShellStyleHInstance(jitter):
    """
    [Shell32.dll] HINSTANCE SHGetShellStyleHInstance()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetSpecialFolderLocation(jitter):
    """
    [Shell32.dll] HRESULT SHGetSpecialFolderLocation(HWND hwndOwner, [CSIDL] nFolder, PIDLIST_ABSOLUTE* ppidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "nFolder", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetSpecialFolderPath(jitter):
    """
    [Shell32.dll] BOOL SHGetSpecialFolderPath(HWND hwndOwner, LPWSTR lpwszPath, [CSIDL] csidl, BOOL fCreate)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "lpwszPath", "csidl", "fCreate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetSpecialFolderPath(jitter, get_str, set_str):
    """
    [Shell32.dll] BOOL SHGetSpecialFolderPath(HWND hwndOwner, LPTSTR lpszPath, [CSIDL] csidl, BOOL fCreate)
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
    [Shell32.dll] HRESULT SHGetStockIconInfo(SHSTOCKICONID siid, [SHGSI_FLAGS] uFlags, SHSTOCKICONINFO* psii)
    """
    ret_ad, args = jitter.func_args_stdcall(["siid", "uFlags", "psii"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetTemporaryPropertyForItem(jitter):
    """
    [Shell32.dll] HRESULT SHGetTemporaryPropertyForItem(IShellItem* psi, REFPROPERTYKEY pk, PROPVARIANT* ppropvarInk)
    """
    ret_ad, args = jitter.func_args_stdcall(["psi", "pk", "ppropvarInk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetUnreadMailCountW(jitter):
    """
    [Shell32.dll] HRESULT SHGetUnreadMailCountW(HKEY hKeyUser, LPCWSTR pszMailAddress, DWORD* pdwCount, FILETIME* pFileTime, LPCWSTR pszShellExecuteCommand, int cchShellExecuteCommand)
    """
    ret_ad, args = jitter.func_args_stdcall(["hKeyUser", "pszMailAddress", "pdwCount", "pFileTime", "pszShellExecuteCommand", "cchShellExecuteCommand"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHHandleUpdateImage(jitter):
    """
    [Shell32.dll] int SHHandleUpdateImage(PCIDLIST_ABSOLUTE pidlExtra)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlExtra"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHILCreateFromPath(jitter):
    """
    [Shell32.dll] HRESULT SHILCreateFromPath(LPCWSTR pszPath, PIDLIST_ABSOLUTE* ppidl, DWORD* rgflnOut)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "ppidl", "rgflnOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHInvokePrinterCommand(jitter, get_str, set_str):
    """
    [Shell32.dll] BOOL SHInvokePrinterCommand(HWND hwnd, UINT uAction, LPCTSTR lpBuf1, LPCTSTR lpBuf2, BOOL fModal)
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
    [Shell32.dll] HRESULT SHIsFileAvailableOffline(LPCWSTR pszPath, LPDWORD pdwStatus)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pdwStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHLimitInputEdit(jitter):
    """
    [Shell32.dll] HRESULT SHLimitInputEdit(HWND hwndEdit, IShellFolder* psf)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndEdit", "psf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHLoadInProc(jitter):
    """
    [Shell32.dll] HRESULT SHLoadInProc(REFCLSID rclsid)
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHLoadNonloadedIconOverlayIdentifiers(jitter):
    """
    [Shell32.dll] HRESULT SHLoadNonloadedIconOverlayIdentifiers()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHLoadOLE(jitter):
    """
    [Shell32.dll] HRESULT SHLoadOLE(LPARAM lParam)
    """
    ret_ad, args = jitter.func_args_stdcall(["lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHLocalStrDup(jitter, get_str, set_str):
    """
    [Shell32.dll] HRESULT SHLocalStrDup(LPCWSTR psz, LPWSTR* ppsz)
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
    [Shell32.dll] HRESULT SHMapIDListToImageListIndexAsync(IShellTaskScheduler* pts, IShellFolder* psf, LPCITEMIDLIST pidl, [GIL_INPUT_FLAGS] flags, PFNASYNCICONTASKBALLBACK pfn, void* pvData, void* pvHint, int* piIndex, int* piIndexSel)
    """
    ret_ad, args = jitter.func_args_stdcall(["pts", "psf", "pidl", "flags", "pfn", "pvData", "pvHint", "piIndex", "piIndexSel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHMapPIDLToSystemImageListIndex(jitter):
    """
    [Shell32.dll] int SHMapPIDLToSystemImageListIndex(IShellFolder* psf, PCUITEMID_CHILD pidl, int* piIndex)
    """
    ret_ad, args = jitter.func_args_stdcall(["psf", "pidl", "piIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHMultiFileProperties(jitter):
    """
    [Shell32.dll] HRESULT SHMultiFileProperties(IDataObject* pdtobj, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdtobj", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHObjectProperties(jitter):
    """
    [Shell32.dll] BOOL SHObjectProperties(HWND hwnd, DWORD shopObjectType, PCWSTR pszObjectName, PCWSTR pszPropertyPage)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "shopObjectType", "pszObjectName", "pszPropertyPage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHOpenFolderAndSelectItems(jitter):
    """
    [Shell32.dll] HRESULT SHOpenFolderAndSelectItems(PCIDLIST_ABSOLUTE pidlFolder, UINT cidl, PCUITEMID_CHILD_ARRAY* apidl, [OFASI_FLAGS] dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidlFolder", "cidl", "apidl", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHOpenPropSheetW(jitter):
    """
    [Shell32.dll] BOOL SHOpenPropSheetW(LPCWSTR pszCaption, HKEY [] ahkeys, UINT ckeys, const CLSID* pclsidDef, IDataObject* pdtobj, IShellBrowser* psb, LPCWSTR pStartPage)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszCaption", "ahkeys", "ckeys", "pclsidDef", "pdtobj", "psb", "pStartPage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHOpenWithDialog(jitter):
    """
    [Shell32.dll] HRESULT SHOpenWithDialog(HWND hwndParent, const OPENASINFO* poainfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "poainfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHParseDisplayName(jitter):
    """
    [Shell32.dll] HRESULT SHParseDisplayName(LPCWSTR pszName, IBindCtx* pbc, PIDLIST_ABSOLUTE* ppidl, SFGAOF sfgaoIn, SFGAOF* psfgaoOut)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszName", "pbc", "ppidl", "sfgaoIn", "psfgaoOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHPathPrepareForWrite(jitter, get_str, set_str):
    """
    [Shell32.dll] HRESULT SHPathPrepareForWrite(HWND hwnd, IUnknown* punkEnableModless, LPCTSTR pszPath, [SHPPFW_FLAGS] dwFlags)
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
    [Shell32.dll] HRESULT SHQueryRecycleBin(LPCTSTR pszRootPath, LPSHQUERYRBINFO pSHQueryRBInfo)
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
    [Shell32.dll] HRESULT SHQueryUserNotificationState(QUERY_USER_NOTIFICATION_STATE* pquns)
    """
    ret_ad, args = jitter.func_args_stdcall(["pquns"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHRemoveLocalizedName(jitter):
    """
    [Shell32.dll] HRESULT SHRemoveLocalizedName(LPCWSTR pszPath)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHReplaceFromPropSheetExtArray(jitter):
    """
    [Shell32.dll] UINT SHReplaceFromPropSheetExtArray(HPSXA hpsxa, UINT uPageID, LPFNADDPROPSHEETPAGE lpfnReplaceWith, LPARAM lParam)
    """
    ret_ad, args = jitter.func_args_stdcall(["hpsxa", "uPageID", "lpfnReplaceWith", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHResolveLibrary(jitter):
    """
    [Shell32.dll] HRESULT SHResolveLibrary(IShellItem* psiLibrary)
    """
    ret_ad, args = jitter.func_args_stdcall(["psiLibrary"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHRestricted(jitter):
    """
    [Shell32.dll] DWORD SHRestricted(RESTRICTIONS rest)
    """
    ret_ad, args = jitter.func_args_stdcall(["rest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHRunControlPanel(jitter):
    """
    [Shell32.dll] BOOL SHRunControlPanel(LPCWSTR lpcszCmdLine, HWND hwndMsgParent)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpcszCmdLine", "hwndMsgParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSetDefaultProperties(jitter):
    """
    [Shell32.dll] HRESULT SHSetDefaultProperties(HWND hwnd, IShellItem* psi, [FILEOP_FLAGS_DWORD] dwFileOpFlags, IFileOperationProgressSink* pfops)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "psi", "dwFileOpFlags", "pfops"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSetFolderPath(jitter, get_str, set_str):
    """
    [Shell32.dll] HRESULT SHSetFolderPath([CSIDL] csidl, HANDLE hToken, DWORD dwFlags, LPCTSTR pszPath)
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
    [Shell32.dll] void SHSetInstanceExplorer(IUnknown* punk)
    """
    ret_ad, args = jitter.func_args_stdcall(["punk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSetKnownFolderPath(jitter):
    """
    [Shell32.dll] HRESULT SHSetKnownFolderPath(REFKNOWNFOLDERID rfid, [KNOWN_FOLDER_FLAG|DWORD] dwFlags, HANDLE hToken, PCWSTR pszPath)
    """
    ret_ad, args = jitter.func_args_stdcall(["rfid", "dwFlags", "hToken", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSetLocalizedName(jitter):
    """
    [Shell32.dll] HRESULT SHSetLocalizedName(LPCWSTR pszPath, LPCWSTR pszResModule, int idsRes)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszResModule", "idsRes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSetTemporaryPropertyForItem(jitter):
    """
    [Shell32.dll] HRESULT SHSetTemporaryPropertyForItem(IShellItem* psi, REFPROPERTYKEY propkey, REFPROPVARIANT propvar)
    """
    ret_ad, args = jitter.func_args_stdcall(["psi", "propkey", "propvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSetUnreadMailCountW(jitter):
    """
    [Shell32.dll] HRESULT SHSetUnreadMailCountW(LPCWSTR pszMailAddress, DWORD dwCount, LPCWSTR pszShellExecuteCommand)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszMailAddress", "dwCount", "pszShellExecuteCommand"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHShellFolderView_Message(jitter):
    """
    [Shell32.dll] LRESULT SHShellFolderView_Message(HWND hwnd, UINT uMsg, LPARAM lparam)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "uMsg", "lparam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHShowManageLibraryUI(jitter):
    """
    [Shell32.dll] HRESULT SHShowManageLibraryUI(IShellItem* psiLibrary, HWND hwndOwner, LPCWSTR pszTitle, LPCWSTR pszInstruction, LIBRARYMANAGEDIALOGOPTIONS lmdOptions)
    """
    ret_ad, args = jitter.func_args_stdcall(["psiLibrary", "hwndOwner", "pszTitle", "pszInstruction", "lmdOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSimpleIDListFromPath(jitter):
    """
    [Shell32.dll] PIDLIST_ABSOLUTE SHSimpleIDListFromPath(LPCWSTR pszPath)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHStartNetConnectionDialogW(jitter):
    """
    [Shell32.dll] HRESULT SHStartNetConnectionDialogW(HWND hwnd, LPCWSTR pszRemoteName, DWORD dwType)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszRemoteName", "dwType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHTestTokenMembership(jitter):
    """
    [Shell32.dll] BOOL SHTestTokenMembership(HANDLE hToken, ULONG ulRID)
    """
    ret_ad, args = jitter.func_args_stdcall(["hToken", "ulRID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHUpdateImage(jitter, get_str, set_str):
    """
    [Shell32.dll] void SHUpdateImage(LPCTSTR pszHashItem, int iIndex, [SHUpdateImage_FLAGS] uFlags, int iImageIndex)
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
    [Shell32.dll] BOOL SHValidateUNC(HWND hwndOwner, LPWSTR pszFile, UINT fConnect)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "pszFile", "fConnect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SignalFileOpen(jitter):
    """
    [Shell32.dll] BOOL SignalFileOpen(PCIDLIST_ABSOLUTE pidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_StgMakeUniqueName(jitter):
    """
    [Shell32.dll] HRESULT StgMakeUniqueName(IStorage* pstgParent, PCWSTR pszFileSpec, [STGM_FLAGS] grfMode, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pstgParent", "pszFileSpec", "grfMode", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Win32DeleteFile(jitter):
    """
    [Shell32.dll] BOOL Win32DeleteFile(LPCTSTR pszFileName)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_WOWShellExecute(jitter):
    """
    [Shell32.dll] HINSTANCE WOWShellExecute(HWND hwnd, LPCTSTR lpOperation, LPCTSTR lpFile, LPCTSTR lpParameters, LPCTSTR lpDirectory, [ShowWindowCmd] nShowCmd, void* lpfnCBWinExec)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "lpOperation", "lpFile", "lpParameters", "lpDirectory", "nShowCmd", "lpfnCBWinExec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_WriteCabinetState(jitter):
    """
    [Shell32.dll] BOOL WriteCabinetState(CABINETSTATE* pcs)
    """
    ret_ad, args = jitter.func_args_stdcall(["pcs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_RunFileDlg(jitter):
    """
    [Shell32.dll] VOID RunFileDlg(HWND hwndOwner, HICON hIcon, LPCWSTR lpszDirectory, LPCWSTR lpszTitle, LPCWSTR lpszDescription, [RunFileDlgFlags] uFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "hIcon", "lpszDirectory", "lpszTitle", "lpszDescription", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_StrRetToStrN(jitter):
    """
    [Shell32.dll] BOOL StrRetToStrN(LPTSTR pszOut, UINT cchOut, LPSTRRET pStrRet, LPCITEMIDLIST pidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszOut", "cchOut", "pStrRet", "pidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PifMgr_CloseProperties(jitter):
    """
    [Shell32.dll] int PifMgr_CloseProperties(HANDLE hProps, UINT flOpt)
    """
    ret_ad, args = jitter.func_args_stdcall(["hProps", "flOpt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PifMgr_OpenProperties(jitter):
    """
    [Shell32.dll] HANDLE PifMgr_OpenProperties(LPCWSTR pszApp, LPCWSTR lpszPIF, UINT hInf, UINT flOpt)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszApp", "lpszPIF", "hInf", "flOpt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PifMgr_GetProperties(jitter):
    """
    [Shell32.dll] int PifMgr_GetProperties(HANDLE hProps, LPCSTR pszGroup, VOID* lpProps, int cbProps, UINT flOpt)
    """
    ret_ad, args = jitter.func_args_stdcall(["hProps", "pszGroup", "lpProps", "cbProps", "flOpt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PifMgr_SetProperties(jitter):
    """
    [Shell32.dll] int PifMgr_SetProperties(HANDLE hProps, LPCSTR pszGroup, VOID* lpProps, int cbProps, UINT flOpt)
    """
    ret_ad, args = jitter.func_args_stdcall(["hProps", "pszGroup", "lpProps", "cbProps", "flOpt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHAddDefaultPropertiesByExt(jitter):
    """
    [Shell32.dll] HRESULT SHAddDefaultPropertiesByExt(PCWSTR pszExt, IPropertyStore* pPropStore)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszExt", "pPropStore"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetPropertyStoreForWindow(jitter):
    """
    [Shell32.dll] HRESULT SHGetPropertyStoreForWindow(HWND hwnd, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetPropertyStoreFromIDList(jitter):
    """
    [Shell32.dll] HRESULT SHGetPropertyStoreFromIDList(PCIDLIST_ABSOLUTE pidl, GETPROPERTYSTOREFLAGS flags, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pidl", "flags", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetPropertyStoreFromParsingName(jitter):
    """
    [Shell32.dll] HRESULT SHGetPropertyStoreFromParsingName(PCWSTR pszPath, IBindCtx* pbc, GETPROPERTYSTOREFLAGS flags, REFIID riid, void** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pbc", "flags", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHPropStgCreate(jitter):
    """
    [Shell32.dll] HRESULT SHPropStgCreate(IPropertySetStorage* psstg, REFFMTID fmtid, const CLSID* pclsid, [PROPSETFLAG] grfFlags, [STGM_FLAGS] grfMode, DWORD dwDisposition, IPropertyStorage** ppstg, UINT* puCodePage)
    """
    ret_ad, args = jitter.func_args_stdcall(["psstg", "fmtid", "pclsid", "grfFlags", "grfMode", "dwDisposition", "ppstg", "puCodePage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHPropStgReadMultiple(jitter):
    """
    [Shell32.dll] HRESULT SHPropStgReadMultiple(IPropertyStorage* pps, [CodePageEnum] uCodePage, ULONG cpspec, PROPSPEC const[] rgpspec, PROPVARIANT[] rgvar)
    """
    ret_ad, args = jitter.func_args_stdcall(["pps", "uCodePage", "cpspec", "rgpspec", "rgvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHPropStgWriteMultiple(jitter):
    """
    [Shell32.dll] HRESULT SHPropStgWriteMultiple(IPropertyStorage* pps, UINT* uCodePage, ULONG cpspec, PROPSPEC const[] rgpspec, PROPVARIANT[] rgvar, PROPID propidNameFirst)
    """
    ret_ad, args = jitter.func_args_stdcall(["pps", "uCodePage", "cpspec", "rgpspec", "rgvar", "propidNameFirst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_AddCommasExportW(jitter):
    """
    [Shell32.dll] LPWSTR AddCommasExportW(DWORD value, LPWSTR pwszBuf)
    """
    ret_ad, args = jitter.func_args_stdcall(["value", "pwszBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_AppCompat_RunDLLW(jitter):
    """
    [Shell32.dll] void AppCompat_RunDLLW(HWND unusedHwnd, HINSTANCE unusedHinstance, LPWSTR commandLine, int unusedInt)
    """
    ret_ad, args = jitter.func_args_stdcall(["unusedHwnd", "unusedHinstance", "commandLine", "unusedInt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CheckStagingArea(jitter):
    """
    [Shell32.dll] HRESULT CheckStagingArea()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CreateAutoListParser(jitter):
    """
    [Shell32.dll] HRESULT CreateAutoListParser(REFIID riid, PVOID* ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CreateInfoTipFromItem(jitter):
    """
    [Shell32.dll] HRESULT CreateInfoTipFromItem(IShellFolder2* psf, ITEMIDLIST* pidl, LPCWSTR pText, REFIID riid, PVOID* ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["psf", "pidl", "pText", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_CreateInfoTipFromItem2(jitter):
    """
    [Shell32.dll] HRESULT CreateInfoTipFromItem2(IShellFolder2* psf, ITEMIDLIST* pidl, PROPERTYKEY* pPropKey, LPCWSTR pText, REFIID riid, PVOID* ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["psf", "pidl", "pPropKey", "pText", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_DisconnectWindowDialog(jitter):
    """
    [Shell32.dll] void DisconnectWindowDialog(HWND hwndUnused)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndUnused"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_GetAppPathFromLink(jitter):
    """
    [Shell32.dll] HRESULT GetAppPathFromLink(IShellItem* pItem, LPWSTR pwszPathBuffer, DWORD dwBufferLen)
    """
    ret_ad, args = jitter.func_args_stdcall(["pItem", "pwszPathBuffer", "dwBufferLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_GetSqmableFileName(jitter):
    """
    [Shell32.dll] BOOL GetSqmableFileName(LPCWSTR pwszFileName, LPWSTR pwszSqmName, UINT sqmNameBufLen)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszFileName", "pwszSqmName", "sqmNameBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Int64ToString(jitter):
    """
    [Shell32.dll] int Int64ToString(INT64 number, LPWSTR pwszBuf, UINT bufLen, BOOL useNumberFormat, NUMBERFMT* pFormatInfo, [NUMBERFMT_FLAGS] dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["number", "pwszBuf", "bufLen", "useNumberFormat", "pFormatInfo", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_IsElevationRequired(jitter):
    """
    [Shell32.dll] BOOL IsElevationRequired(LPCWSTR lpwszExeFile)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwszExeFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_IsSearchEnabled(jitter):
    """
    [Shell32.dll] BOOL IsSearchEnabled()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_LargeIntegerToString(jitter):
    """
    [Shell32.dll] int LargeIntegerToString(LARGE_INTEGER* pNumber, LPWSTR pwszBuf, UINT bufLen, BOOL useNumberFormat, NUMBERFMT* pFormatInfo, [NUMBERFMT_FLAGS] dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pNumber", "pwszBuf", "bufLen", "useNumberFormat", "pFormatInfo", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathGetPathDisplayName(jitter):
    """
    [Shell32.dll] HRESULT PathGetPathDisplayName(LPCWSTR pwszPath, LPWSTR pwszDisplayName, DWORD displayNameLen)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszPath", "pwszDisplayName", "displayNameLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_PathIsTemporary(jitter, get_str, set_str):
    """
    [Shell32.dll] BOOL PathIsTemporary(LPCTSTR pszFile)
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
    [Shell32.dll] void Printer_AddPrinterPropPages(LPCWSTR printer, PROPSHEETHEADER* pPropHeader)
    """
    ret_ad, args = jitter.func_args_stdcall(["printer", "pPropHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Printer_LoadIconsW(jitter):
    """
    [Shell32.dll] void Printer_LoadIconsW(LPCWSTR printerName, HICON* phLargeIcon, HICON* phSmallIcon)
    """
    ret_ad, args = jitter.func_args_stdcall(["printerName", "phLargeIcon", "phSmallIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Printers_RegisterWindowW(jitter):
    """
    [Shell32.dll] BOOL Printers_RegisterWindowW(LPCWSTR pwszPrinter, DWORD pidlType, BOOL* pWinCreated, HWND* phwnd)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszPrinter", "pidlType", "pWinCreated", "phwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_Printers_UnregisterWindow(jitter):
    """
    [Shell32.dll] void Printers_UnregisterWindow(CLASSPIDL* pClassPidl, HWND hwnd)
    """
    ret_ad, args = jitter.func_args_stdcall(["pClassPidl", "hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_RefreshBrowserLayout(jitter):
    """
    [Shell32.dll] HRESULT RefreshBrowserLayout(IShellItem* pItem)
    """
    ret_ad, args = jitter.func_args_stdcall(["pItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_RunAsNewUser_RunDLLW(jitter):
    """
    [Shell32.dll] int RunAsNewUser_RunDLLW(HWND hWnd, HINSTANCE hIinstance, LPCWSTR lpszFileMapName, [ShowWindowCmd] nCmdShow)
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hIinstance", "lpszFileMapName", "nCmdShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetUserDisplayName(jitter):
    """
    [Shell32.dll] HRESULT SHGetUserDisplayName(LPWSTR pwszName, UINT pBufLen)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszName", "pBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHGetUserPicturePathEx(jitter):
    """
    [Shell32.dll] HRESULT SHGetUserPicturePathEx(LPCWSTR pwszUserOrPicName, [SGUPP_FLAGS] sguppFlags, LPCWSTR pwszDesiredSrcExt, LPWSTR pwszPicPath, UINT picPathLen, LPWSTR pwszSrcPath, UINT srcLen)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszUserOrPicName", "sguppFlags", "pwszDesiredSrcExt", "pwszPicPath", "picPathLen", "pwszSrcPath", "srcLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHHelpShortcuts_RunDLL(jitter, get_str, set_str):
    """
    [Shell32.dll] void SHHelpShortcuts_RunDLL(HWND hwndParent, HINSTANCE unusedHinstance, LPCTSTR commandLine, int unusedInt)
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
    [Shell32.dll] HRESULT SHResolveUserNames(LPCWSTR pwszSids, LPWSTR pwszNames, UINT nameLen)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszSids", "pwszNames", "nameLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHSettingsChanged(jitter):
    """
    [Shell32.dll] void SHSettingsChanged(WPARAM wParam, LPCWSTR lParam)
    """
    ret_ad, args = jitter.func_args_stdcall(["wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHShouldShowWizards(jitter):
    """
    [Shell32.dll] BOOL SHShouldShowWizards(IUnknown* pUnk)
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHTestTokenPrivilegeW(jitter):
    """
    [Shell32.dll] BOOL SHTestTokenPrivilegeW(HANDLE hToken, LPCWSTR pwszPrivilege)
    """
    ret_ad, args = jitter.func_args_stdcall(["hToken", "pwszPrivilege"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHUserGetPasswordHint(jitter):
    """
    [Shell32.dll] HRESULT SHUserGetPasswordHint(PCWSTR pwszUserName, PWSTR* ppwszHint)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszUserName", "ppwszHint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_SHUserSetPasswordHint(jitter):
    """
    [Shell32.dll] HRESULT SHUserSetPasswordHint(PCWSTR pwszUserName, PCWSTR pwszPasswordHint)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszUserName", "pwszPasswordHint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ShellExecCmdLine(jitter):
    """
    [Shell32.dll] HRESULT ShellExecCmdLine(HWND hwnd, LPCWSTR pwszCommand, LPCWSTR pwszStartDir, [ShowWindowCmd] nShow, LPVOID pUnused, [SECL_FLAGS] dwSeclFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pwszCommand", "pwszStartDir", "nShow", "pUnused", "dwSeclFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shell32_ShortSizeFormatExportW(jitter):
    """
    [Shell32.dll] LPWSTR ShortSizeFormatExportW(DWORD value, LPWSTR pwszBuf)
    """
    ret_ad, args = jitter.func_args_stdcall(["value", "pwszBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
