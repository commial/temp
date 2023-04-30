
def shlwapi_SHAllocShared(jitter):
    """"
    [ShLwApi.dll] HANDLE SHAllocShared(const void* pvData, DWORD dwSize, DWORD dwDestinationProcessId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvData", "dwSize", "dwDestinationProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ShellMessageBox(jitter):
    """"
    [ShLwApi.dll] [MessageBoxResult] ShellMessageBox(HINSTANCE hInst, HWND hWnd, LPCTSTR pszMsg, LPCTSTR pszTitle, [MessageBoxType] fuStyle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInst", "hWnd", "pszMsg", "pszTitle", "fuStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGetViewStatePropertyBag(jitter):
    """"
    [ShLwApi.dll] HRESULT SHGetViewStatePropertyBag(PCIDLIST_ABSOLUTE pidl, LPCWSTR pszBagName, DWORD dwFlags, REFIID riid, void** ppv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pidl", "pszBagName", "dwFlags", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHLockShared(jitter):
    """"
    [ShLwApi.dll] LPVOID SHLockShared(HANDLE* hData, DWORD dwOtherProcId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hData", "dwOtherProcId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHUnlockShared(jitter):
    """"
    [ShLwApi.dll] BOOL SHUnlockShared(void* pvData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHFreeShared(jitter):
    """"
    [ShLwApi.dll] BOOL SHFreeShared(HANDLE hData, DWORD dwSourceProcId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hData", "dwSourceProcId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrStrNW(jitter):
    """"
    [ShLwApi.dll] LPCWSTR StrStrNW(LPCWSTR lpFirst, LPCWSTR lpSrch, UINT cchMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFirst", "lpSrch", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrStrNIW(jitter):
    """"
    [ShLwApi.dll] LPCWSTR StrStrNIW(LPCWSTR lpFirst, LPCWSTR lpSrch, UINT cchMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFirst", "lpSrch", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ColorAdjustLuma(jitter):
    """"
    [ShLwApi.dll] COLORREF ColorAdjustLuma(COLORREF clrRGB, int n, BOOL fScale)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clrRGB", "n", "fScale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ColorHLSToRGB(jitter):
    """"
    [ShLwApi.dll] COLORREF ColorHLSToRGB(WORD wHue, WORD wLuminance, WORD wSaturation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["wHue", "wLuminance", "wSaturation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ColorRGBToHLS(jitter):
    """"
    [ShLwApi.dll] void ColorRGBToHLS(COLORREF clrRGB, WORD* pwHue, WORD* pwLuminance, WORD* pwSaturation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clrRGB", "pwHue", "pwLuminance", "pwSaturation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateShellPalette(jitter):
    """"
    [ShLwApi.dll] HPALETTE SHCreateShellPalette(HDC hdc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGetInverseCMAP(jitter):
    """"
    [ShLwApi.dll] HRESULT SHGetInverseCMAP(BYTE* pbMap, ULONG cbMap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pbMap", "cbMap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathAddBackslash(jitter):
    """"
    [ShLwApi.dll] LPTSTR PathAddBackslash(LPTSTR lpszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathAddExtension(jitter):
    """"
    [ShLwApi.dll] BOOL PathAddExtension(LPTSTR pszPath, LPCTSTR pszExtension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszExtension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathAppend(jitter):
    """"
    [ShLwApi.dll] BOOL PathAppend(LPTSTR pszPath, LPCTSTR pszMore)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszMore"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathBuildRoot(jitter):
    """"
    [ShLwApi.dll] LPTSTR PathBuildRoot(LPTSTR szRoot, int iDrive)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szRoot", "iDrive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathCanonicalize(jitter):
    """"
    [ShLwApi.dll] BOOL PathCanonicalize(LPTSTR lpszDst, LPCTSTR lpszSrc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDst", "lpszSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathCombine(jitter):
    """"
    [ShLwApi.dll] LPTSTR PathCombine(LPTSTR lpszDest, LPCTSTR lpszDir, LPCTSTR lpszFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDest", "lpszDir", "lpszFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathCommonPrefix(jitter):
    """"
    [ShLwApi.dll] int PathCommonPrefix(LPCTSTR pszFile1, LPCTSTR pszFile2, LPTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszFile1", "pszFile2", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathCompactPath(jitter):
    """"
    [ShLwApi.dll] BOOL PathCompactPath(HDC hDC, LPTSTR lpszPath, UINT dx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDC", "lpszPath", "dx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathCompactPathEx(jitter):
    """"
    [ShLwApi.dll] BOOL PathCompactPathEx(LPTSTR pszOut, LPCTSTR pszSrc, UINT cchMax, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszOut", "pszSrc", "cchMax", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathCreateFromUrl(jitter):
    """"
    [ShLwApi.dll] HRESULT PathCreateFromUrl(PCTSTR pszUrl, PTSTR pszPath, DWORD* pcchPath, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszUrl", "pszPath", "pcchPath", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathCreateFromUrlAlloc(jitter):
    """"
    [ShLwApi.dll] HRESULT PathCreateFromUrlAlloc(PCWSTR pszIn, PWSTR* ppszOut, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszIn", "ppszOut", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathFileExists(jitter):
    """"
    [ShLwApi.dll] BOOL PathFileExists(LPCTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathFindExtension(jitter):
    """"
    [ShLwApi.dll] PTSTR PathFindExtension(PTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathFindFileName(jitter):
    """"
    [ShLwApi.dll] PTSTR PathFindFileName(PTSTR pPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathFindNextComponent(jitter):
    """"
    [ShLwApi.dll] PTSTR PathFindNextComponent(PTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathFindOnPath(jitter):
    """"
    [ShLwApi.dll] BOOL PathFindOnPath(LPTSTR pszFile, LPCTSTR* ppszOtherDirs)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszFile", "ppszOtherDirs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathFindSuffixArray(jitter):
    """"
    [ShLwApi.dll] LPCTSTR PathFindSuffixArray(LPCTSTR pszPath, const LPCTSTR* apszSuffix, int iArraySize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "apszSuffix", "iArraySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathGetArgs(jitter):
    """"
    [ShLwApi.dll] PTSTR PathGetArgs(PTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathGetCharType(jitter):
    """"
    [ShLwApi.dll] UINT PathGetCharType(TCHAR ch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathGetDriveNumber(jitter):
    """"
    [ShLwApi.dll] int PathGetDriveNumber(LPCTSTR lpsz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsContentType(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsContentType(LPCTSTR pszPath, LPCTSTR pszContentType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszContentType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsDirectory(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsDirectory(LPCTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsDirectoryEmpty(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsDirectoryEmpty(LPCTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsFileSpec(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsFileSpec(LPCTSTR lpszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsHTMLFile(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsHTMLFile(LPCTSTR pszFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsLFNFileSpec(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsLFNFileSpec(LPCTSTR pszName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsNetworkPath(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsNetworkPath(LPCTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsPrefix(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsPrefix(LPCTSTR pszPrefix, LPCTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPrefix", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsRelative(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsRelative(LPCTSTR lpszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsRoot(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsRoot(LPCTSTR pPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsSameRoot(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsSameRoot(LPCTSTR pszPath1, LPCTSTR pszPath2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath1", "pszPath2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsSystemFolder(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsSystemFolder(LPCTSTR pszPath, DWORD dwAttrb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "dwAttrb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsUNC(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsUNC(LPCTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsUNCServer(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsUNCServer(LPCTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsUNCServerShare(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsUNCServerShare(LPCTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathIsURL(jitter):
    """"
    [ShLwApi.dll] BOOL PathIsURL(LPCTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathMakePretty(jitter):
    """"
    [ShLwApi.dll] BOOL PathMakePretty(LPTSTR lpPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathMakeSystemFolder(jitter):
    """"
    [ShLwApi.dll] BOOL PathMakeSystemFolder(LPTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathMatchSpec(jitter):
    """"
    [ShLwApi.dll] BOOL PathMatchSpec(LPCSTR pszFile, LPCSTR pszSpec)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszFile", "pszSpec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathMatchSpecEx(jitter):
    """"
    [ShLwApi.dll] HRESULT PathMatchSpecEx(LPCTSTR pszFile, LPCTSTR pszSpec, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszFile", "pszSpec", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathParseIconLocation(jitter):
    """"
    [ShLwApi.dll] int PathParseIconLocation(LPTSTR pszIconFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszIconFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathQuoteSpaces(jitter):
    """"
    [ShLwApi.dll] BOOL PathQuoteSpaces(LPTSTR lpsz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRelativePathTo(jitter):
    """"
    [ShLwApi.dll] BOOL PathRelativePathTo(LPTSTR pszPath, LPCTSTR pszFrom, DWORD dwAttrFrom, LPCTSTR pszTo, DWORD dwAttrTo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszFrom", "dwAttrFrom", "pszTo", "dwAttrTo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRemoveArgs(jitter):
    """"
    [ShLwApi.dll] void PathRemoveArgs(LPTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRemoveBackslash(jitter):
    """"
    [ShLwApi.dll] LPTSTR PathRemoveBackslash(LPTSTR lpszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRemoveBlanks(jitter):
    """"
    [ShLwApi.dll] void PathRemoveBlanks(LPTSTR lpszString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRemoveExtension(jitter):
    """"
    [ShLwApi.dll] void PathRemoveExtension(LPTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRemoveFileSpec(jitter):
    """"
    [ShLwApi.dll] BOOL PathRemoveFileSpec(LPTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathRenameExtension(jitter):
    """"
    [ShLwApi.dll] BOOL PathRenameExtension(LPTSTR pszPath, LPCTSTR pszExt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszExt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathSearchAndQualify(jitter):
    """"
    [ShLwApi.dll] BOOL PathSearchAndQualify(LPCTSTR pcszPath, LPTSTR pszFullyQualifiedPath, UINT cchFullyQualifiedPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pcszPath", "pszFullyQualifiedPath", "cchFullyQualifiedPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathSetDlgItemPath(jitter):
    """"
    [ShLwApi.dll] void PathSetDlgItemPath(HWND hDlg, int id, LPCSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "id", "pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathSkipRoot(jitter):
    """"
    [ShLwApi.dll] PTSTR PathSkipRoot(PTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathStripPath(jitter):
    """"
    [ShLwApi.dll] void PathStripPath(LPTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathStripToRoot(jitter):
    """"
    [ShLwApi.dll] BOOL PathStripToRoot(LPTSTR szRoot)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szRoot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathUndecorate(jitter):
    """"
    [ShLwApi.dll] void PathUndecorate(LPTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathUnExpandEnvStrings(jitter):
    """"
    [ShLwApi.dll] BOOL PathUnExpandEnvStrings(LPCTSTR pszPath, LPTSTR pszBuf, UINT cchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathUnmakeSystemFolder(jitter):
    """"
    [ShLwApi.dll] BOOL PathUnmakeSystemFolder(LPTSTR pszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathUnquoteSpaces(jitter):
    """"
    [ShLwApi.dll] void PathUnquoteSpaces(LPTSTR lpsz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHSkipJunction(jitter):
    """"
    [ShLwApi.dll] BOOL SHSkipJunction(IBindCtx* pbc, const CLSID* pclsid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pbc", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlApplyScheme(jitter):
    """"
    [ShLwApi.dll] HRESULT UrlApplyScheme(PCTSTR pszIn, PTSTR pszOut, DWORD* pcchOut, [URL_APPLY_FLAGS] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszIn", "pszOut", "pcchOut", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlCanonicalize(jitter):
    """"
    [ShLwApi.dll] HRESULT UrlCanonicalize(PCTSTR pszUrl, PTSTR pszCanonicalized, DWORD* pcchCanonicalized, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszUrl", "pszCanonicalized", "pcchCanonicalized", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlCombine(jitter):
    """"
    [ShLwApi.dll] HRESULT UrlCombine(PCTSTR pszBase, PCTSTR pszRelative, PTSTR pszCombined, DWORD* pcchCombined, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszBase", "pszRelative", "pszCombined", "pcchCombined", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlCompare(jitter):
    """"
    [ShLwApi.dll] int UrlCompare(PCTSTR psz1, PCTSTR psz2, BOOL fIgnoreSlash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2", "fIgnoreSlash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlCreateFromPath(jitter):
    """"
    [ShLwApi.dll] HRESULT UrlCreateFromPath(PCTSTR pszPath, PTSTR pszUrl, DWORD* pcchUrl, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "pszUrl", "pcchUrl", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlEscape(jitter):
    """"
    [ShLwApi.dll] HRESULT UrlEscape(PCTSTR pszURL, PTSTR pszEscaped, DWORD* pcchEscaped, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszURL", "pszEscaped", "pcchEscaped", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlEscapeSpaces(jitter):
    """"
    [ShLwApi.dll] HRESULT UrlEscapeSpaces(LPCTSTR pszURL, LPTSTR pszEscaped, LPDWORD pcchEscaped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszURL", "pszEscaped", "pcchEscaped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlFixupW(jitter):
    """"
    [ShLwApi.dll] HRESULT UrlFixupW(PCWSTR pcszUrl, PWSTR pszTranslatedUrl, DWORD cchMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pcszUrl", "pszTranslatedUrl", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlGetLocation(jitter):
    """"
    [ShLwApi.dll] LPCTSTR UrlGetLocation(PCTSTR pszURL)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszURL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlGetPart(jitter):
    """"
    [ShLwApi.dll] HRESULT UrlGetPart(PCTSTR pszIn, PTSTR pszOut, DWORD* pcchOut, DWORD dwPart, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszIn", "pszOut", "pcchOut", "dwPart", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlHash(jitter):
    """"
    [ShLwApi.dll] HRESULT UrlHash(PCTSTR pszURL, BYTE* pbHash, DWORD cbHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszURL", "pbHash", "cbHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlIs(jitter):
    """"
    [ShLwApi.dll] BOOL UrlIs(PCTSTR pszUrl, URLIS UrlIs)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszUrl", "UrlIs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlIsFileUrl(jitter):
    """"
    [ShLwApi.dll] BOOL UrlIsFileUrl(LPCTSTR pszUrl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszUrl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlIsNoHistory(jitter):
    """"
    [ShLwApi.dll] BOOL UrlIsNoHistory(PCTSTR pszURL)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszURL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlIsOpaque(jitter):
    """"
    [ShLwApi.dll] BOOL UrlIsOpaque(PCTSTR pszURL)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszURL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlUnescape(jitter):
    """"
    [ShLwApi.dll] HRESULT UrlUnescape(PTSTR pszURL, PTSTR pszUnescaped, DWORD* pcchUnescaped, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszURL", "pszUnescaped", "pcchUnescaped", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_UrlUnescapeInPlace(jitter):
    """"
    [ShLwApi.dll] HRESULT UrlUnescapeInPlace(LPTSTR pszURL, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszURL", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_AssocCreate(jitter):
    """"
    [ShLwApi.dll] HRESULT AssocCreate(CLSID clsid, REFIID riid, void** ppv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clsid", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_AssocGetPerceivedType(jitter):
    """"
    [ShLwApi.dll] HRESULT AssocGetPerceivedType(PCWSTR pszExt, PERCEIVED* ptype, PERCEIVEDFLAG* pflag, PWSTR* ppszType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszExt", "ptype", "pflag", "ppszType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_AssocIsDangerous(jitter):
    """"
    [ShLwApi.dll] BOOL AssocIsDangerous(PCWSTR pszAssoc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszAssoc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_AssocQueryKey(jitter):
    """"
    [ShLwApi.dll] HRESULT AssocQueryKey(ASSOCF flags, ASSOCKEY key, LPCTSTR pszAssoc, LPCTSTR pszExtra, HKEY* phkeyOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["flags", "key", "pszAssoc", "pszExtra", "phkeyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_AssocQueryString(jitter):
    """"
    [ShLwApi.dll] HRESULT AssocQueryString(ASSOCF flags, ASSOCSTR str, LPCTSTR pszAssoc, LPCTSTR pszExtra, LPTSTR pszOut, DWORD* pcchOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["flags", "str", "pszAssoc", "pszExtra", "pszOut", "pcchOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_AssocQueryStringByKey(jitter):
    """"
    [ShLwApi.dll] HRESULT AssocQueryStringByKey(ASSOCF flags, ASSOCSTR str, HKEY hkAssoc, LPCTSTR pszExtra, LPTSTR pszOut, DWORD* pcchOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["flags", "str", "hkAssoc", "pszExtra", "pszOut", "pcchOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCopyKey(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHCopyKey(HKEY hkeySrc, LPCTSTR pszSrcSubKey, HKEY hkeyDest, DWORD fReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkeySrc", "pszSrcSubKey", "hkeyDest", "fReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHDeleteEmptyKey(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHDeleteEmptyKey(HKEY hkey, LPCTSTR pszSubKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHDeleteKey(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHDeleteKey(HKEY hkey, LPCTSTR pszSubKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHDeleteValue(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHDeleteValue(HKEY hkey, LPCTSTR pszSubKey, LPCTSTR pszValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey", "pszValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHEnumKeyEx(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHEnumKeyEx(HKEY hkey, DWORD dwIndex, LPTSTR pszName, LPDWORD pcchName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "dwIndex", "pszName", "pcchName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHEnumValue(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHEnumValue(HKEY hkey, DWORD dwIndex, LPTSTR pszValueName, LPDWORD pcchValueName, [RegType*] pdwType, LPVOID pvData, LPDWORD pcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "dwIndex", "pszValueName", "pcchValueName", "pdwType", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGetValue(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHGetValue(HKEY hkey, LPCTSTR pszSubKey, LPCTSTR pszValue, [RegType*] pdwType, LPVOID pvData, LPDWORD pcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey", "pszValue", "pdwType", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHOpenRegStream(jitter):
    """"
    [ShLwApi.dll] IStream* SHOpenRegStream(HKEY hkey, LPCTSTR pszSubkey, LPCTSTR pszValue, [STGM_FLAGS] grfMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubkey", "pszValue", "grfMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHOpenRegStream2(jitter):
    """"
    [ShLwApi.dll] IStream* SHOpenRegStream2(HKEY hkey, LPCTSTR pszSubkey, LPCTSTR pszValue, [STGM_FLAGS] grfMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubkey", "pszValue", "grfMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHQueryInfoKey(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHQueryInfoKey(HKEY hkey, LPDWORD pcSubKeys, LPDWORD pcchMaxSubKeyLen, LPDWORD pcValues, LPDWORD pcchMaxValueNameLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pcSubKeys", "pcchMaxSubKeyLen", "pcValues", "pcchMaxValueNameLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHQueryValueEx(jitter):
    """"
    [ShLwApi.dll] [ERROR_CODE] SHQueryValueEx(HKEY hkey, LPCTSTR pszValue, LPDWORD pdwReserved, [RegType*] pdwType, LPVOID pvData, LPDWORD pcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszValue", "pdwReserved", "pdwType", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegCloseUSKey(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegCloseUSKey(HUSKEY hUSKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hUSKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegCreateUSKey(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegCreateUSKey(LPCTSTR pszPath, REGSAM samDesired, HUSKEY hRelativeUSKey, PHUSKEY phNewUSKey, [ShRegSetFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "samDesired", "hRelativeUSKey", "phNewUSKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegDeleteEmptyUSKey(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegDeleteEmptyUSKey(HUSKEY hUSKey, LPCSTR pszValue, SHREGDEL_FLAGS delRegFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "pszValue", "delRegFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegDeleteUSValue(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegDeleteUSValue(HUSKEY hUSKey, LPCTSTR pszValue, SHREGDEL_FLAGS delRegFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "pszValue", "delRegFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegDuplicateHKey(jitter):
    """"
    [ShLwApi.dll] HKEY SHRegDuplicateHKey(HKEY hkey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegEnumUSKey(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegEnumUSKey(HUSKEY hUSKey, DWORD dwIndex, LPTSTR pszName, LPDWORD pcchName, SHREGENUM_FLAGS enumRegFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "dwIndex", "pszName", "pcchName", "enumRegFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegEnumUSValue(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegEnumUSValue(HUSKEY hUSKey, DWORD dwIndex, LPTSTR pszValueName, LPDWORD pcchValueNameLen, [RegType*] pdwType, void* pvData, LPDWORD pcbData, SHREGENUM_FLAGS enumRegFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "dwIndex", "pszValueName", "pcchValueNameLen", "pdwType", "pvData", "pcbData", "enumRegFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegGetBoolUSValue(jitter):
    """"
    [ShLwApi.dll] BOOL SHRegGetBoolUSValue(LPCTSTR pszSubKey, LPCTSTR pszValue, BOOL fIgnoreHKCU, BOOL fDefault)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszSubKey", "pszValue", "fIgnoreHKCU", "fDefault"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegGetIntW(jitter):
    """"
    [ShLwApi.dll] int SHRegGetIntW(HKEY hk, LPCWSTR szKey, int nDefault)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hk", "szKey", "nDefault"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegGetPath(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegGetPath(HKEY hkey, LPCTSTR pszSubkey, LPCTSTR pszValue, LPTSTR pszPath, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubkey", "pszValue", "pszPath", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegGetUSValue(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegGetUSValue(LPCTSTR pszSubKey, LPCTSTR pszValue, DWORD* pdwType, void* pvData, DWORD* pcbData, BOOL fIgnoreHKCU, void* pvDefaultData, DWORD dwDefaultDataSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszSubKey", "pszValue", "pdwType", "pvData", "pcbData", "fIgnoreHKCU", "pvDefaultData", "dwDefaultDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegGetValue(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegGetValue(HKEY hkey, LPCTSTR pszSubKey, LPCTSTR pszValue, SRRF srrfFlags, LPDWORD pdwType, LPVOID pvData, LPDWORD pcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey", "pszValue", "srrfFlags", "pdwType", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegOpenUSKey(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegOpenUSKey(LPCTSTR pszPath, REGSAM samDesired, HUSKEY hRelativeUSKey, PHUSKEY phNewUSKey, BOOL fIgnoreHKCU)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPath", "samDesired", "hRelativeUSKey", "phNewUSKey", "fIgnoreHKCU"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegQueryInfoUSKey(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegQueryInfoUSKey(HUSKEY hUSKey, LPDWORD pcSubKeys, LPDWORD pcchMaxSubKeyLen, LPDWORD pcValues, LPDWORD pcchMaxValueNameLen, SHREGENUM_FLAGS enumRegFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "pcSubKeys", "pcchMaxSubKeyLen", "pcValues", "pcchMaxValueNameLen", "enumRegFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegQueryUSValue(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegQueryUSValue(HUSKEY hUSKey, LPCTSTR pszValue, [RegType*] pdwType, LPVOID pvData, LPDWORD pcbData, BOOL fIgnoreHKCU, LPVOID pvDefaultData, DWORD dwDefaultDataSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "pszValue", "pdwType", "pvData", "pcbData", "fIgnoreHKCU", "pvDefaultData", "dwDefaultDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegSetPath(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegSetPath(HKEY hkey, LPCTSTR pszSubkey, LPCTSTR pszValue, LPCTSTR pszPath, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubkey", "pszValue", "pszPath", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegSetUSValue(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegSetUSValue(LPCTSTR pszSubKey, LPCTSTR pszValue, DWORD dwType, LPVOID pvData, DWORD cbData, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszSubKey", "pszValue", "dwType", "pvData", "cbData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegSetValue(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegSetValue(HKEY hkey, LPCTSTR pszSubKey, LPCTSTR pszValue, SRRF srrfFlags, DWORD dwType, LPCVOID pvData, DWORD cbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey", "pszValue", "srrfFlags", "dwType", "pvData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegWriteUSValue(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegWriteUSValue(HUSKEY hUSKey, LPCTSTR pszValue, DWORD dwType, LPVOID pvData, DWORD cbData, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hUSKey", "pszValue", "dwType", "pvData", "cbData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHSetValue(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHSetValue(HKEY hkey, LPCTSTR pszSubKey, LPCTSTR pszValue, [RegType] dwType, LPCVOID pvData, DWORD cbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "pszSubKey", "pszValue", "dwType", "pvData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_CharLowerWrapW(jitter):
    """"
    [ShLwApi.dll] LPWSTR CharLowerWrapW(LPWSTR pch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_CharUpperBuffWrapW(jitter):
    """"
    [ShLwApi.dll] DWORD CharUpperBuffWrapW(LPWSTR pch, DWORD cchLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pch", "cchLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ChrCmpI(jitter):
    """"
    [ShLwApi.dll] BOOL ChrCmpI(TCHAR w1, TCHAR w2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["w1", "w2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_CompareStringWrapW(jitter):
    """"
    [ShLwApi.dll] int CompareStringWrapW(LCID Locale, DWORD dwCmpFlags, LPCWSTR lpString1, int cchCount1, LPCWSTR lpString2, int cchCount2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwCmpFlags", "lpString1", "cchCount1", "lpString2", "cchCount2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_GetAcceptLanguages(jitter):
    """"
    [ShLwApi.dll] HRESULT GetAcceptLanguages(LPTSTR pszLanguages, DWORD* pcchLanguages)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszLanguages", "pcchLanguages"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_GetDateFormatWrapW(jitter):
    """"
    [ShLwApi.dll] int GetDateFormatWrapW(LCID Locale, DWORD dwFlags, const SYSTEMTIME* lpDate, LPCWSTR pwzFormat, LPWSTR pwzDateStr, int cchDate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwFlags", "lpDate", "pwzFormat", "pwzDateStr", "cchDate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_GetTimeFormatWrapW(jitter):
    """"
    [ShLwApi.dll] int GetTimeFormatWrapW(LCID Locale, DWORD dwFlags, const SYSTEMTIME* lpTime, LPCWSTR pwzFormat, LPWSTR pwzTimeStr, int cchTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Locale", "dwFlags", "lpTime", "pwzFormat", "pwzTimeStr", "cchTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IntlStrEqN(jitter):
    """"
    [ShLwApi.dll] BOOL IntlStrEqN(LPCTSTR pszStr1, LPCTSTR pszStr2, int nChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszStr1", "pszStr2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IntlStrEqNI(jitter):
    """"
    [ShLwApi.dll] BOOL IntlStrEqNI(LPCTSTR pszStr1, LPCTSTR pszStr2, int nChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszStr1", "pszStr2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IntlStrEqWorker(jitter):
    """"
    [ShLwApi.dll] BOOL IntlStrEqWorker(BOOL fCaseSens, LPCTSTR pszStr1, LPCTSTR pszStr2, int nChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fCaseSens", "pszStr1", "pszStr2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IsCharAlphaNumericWrapW(jitter):
    """"
    [ShLwApi.dll] BOOL IsCharAlphaNumericWrapW(WCHAR ch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IsCharSpace(jitter):
    """"
    [ShLwApi.dll] BOOL IsCharSpace(TCHAR wch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["wch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_OutputDebugStringWrapW(jitter):
    """"
    [ShLwApi.dll] void OutputDebugStringWrapW(LPCWSTR lpOutputString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpOutputString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHLoadIndirectString(jitter):
    """"
    [ShLwApi.dll] HRESULT SHLoadIndirectString(PCWSTR pszSource, PWSTR pszOutBuf, UINT cchOutBuf, void** ppvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszSource", "pszOutBuf", "cchOutBuf", "ppvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHStrDup(jitter):
    """"
    [ShLwApi.dll] HRESULT SHStrDup(LPCTSTR pszSource, LPTSTR* ppwsz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszSource", "ppwsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCat(jitter):
    """"
    [ShLwApi.dll] PTSTR StrCat(PTSTR psz1, PCTSTR psz2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCatBuff(jitter):
    """"
    [ShLwApi.dll] PTSTR StrCatBuff(PTSTR pszDest, PCTSTR pszSrc, int cchDestBuffSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszDest", "pszSrc", "cchDestBuffSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCatChainW(jitter):
    """"
    [ShLwApi.dll] DWORD StrCatChainW(PWSTR pszDst, DWORD cchDst, DWORD ichAt, PCWSTR pszSrc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszDst", "cchDst", "ichAt", "pszSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrChr(jitter):
    """"
    [ShLwApi.dll] PTSTR StrChr(PTSTR pszStart, TCHAR wMatch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszStart", "wMatch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrChrI(jitter):
    """"
    [ShLwApi.dll] PTSTR StrChrI(PTSTR pszStart, TCHAR wMatch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszStart", "wMatch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrChrNIW(jitter):
    """"
    [ShLwApi.dll] PWSTR StrChrNIW(PCWSTR pszStart, WCHAR wMatch, UINT cchMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszStart", "wMatch", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrChrNW(jitter):
    """"
    [ShLwApi.dll] PWSTR StrChrNW(PWSTR pszStart, WCHAR wMatch, UINT cchMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszStart", "wMatch", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmp(jitter):
    """"
    [ShLwApi.dll] int StrCmp(PCTSTR psz1, PCTSTR psz2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpC(jitter):
    """"
    [ShLwApi.dll] int StrCmpC(LPCTSTR lpStr1, LPCTSTR lpStr2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpStr1", "lpStr2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpI(jitter):
    """"
    [ShLwApi.dll] int StrCmpI(PCTSTR psz1, PCTSTR psz2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpIC(jitter):
    """"
    [ShLwApi.dll] int StrCmpIC(LPCTSTR lpStr1, LPCTSTR lpStr2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpStr1", "lpStr2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpLogicalW(jitter):
    """"
    [ShLwApi.dll] int StrCmpLogicalW(PCWSTR psz1, PCWSTR psz2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpN(jitter):
    """"
    [ShLwApi.dll] int StrCmpN(PCTSTR psz1, PCTSTR psz2, int nChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpNC(jitter):
    """"
    [ShLwApi.dll] int StrCmpNC(LPCTSTR pszStr1, LPCTSTR pszStr2, int nChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszStr1", "pszStr2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpNI(jitter):
    """"
    [ShLwApi.dll] int StrCmpNI(PCTSTR psz1, PCTSTR psz2, int nChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCmpNIC(jitter):
    """"
    [ShLwApi.dll] int StrCmpNIC(LPCTSTR pszStr1, LPCTSTR pszStr2, int nChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszStr1", "pszStr2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCpy(jitter):
    """"
    [ShLwApi.dll] PTSTR StrCpy(PTSTR psz1, PCTSTR psz2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCpyN(jitter):
    """"
    [ShLwApi.dll] PTSTR StrCpyN(PTSTR pszDst, PCTSTR pszSrc, int cchMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszDst", "pszSrc", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCSpn(jitter):
    """"
    [ShLwApi.dll] int StrCSpn(PCTSTR pszStr, PCTSTR pszSet)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszStr", "pszSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrCSpnI(jitter):
    """"
    [ShLwApi.dll] int StrCSpnI(PCTSTR pszStr, PCTSTR pszSet)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszStr", "pszSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrDup(jitter):
    """"
    [ShLwApi.dll] PTSTR StrDup(PCTSTR pszSrch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszSrch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrFormatByteSize64(jitter):
    """"
    [ShLwApi.dll] PTSTR StrFormatByteSize64(LONGLONG qdw, PTSTR pszBuf, UINT cchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["qdw", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrFormatByteSizeA(jitter):
    """"
    [ShLwApi.dll] PSTR StrFormatByteSizeA(DWORD dw, PSTR pszBuf, UINT cchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dw", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrFormatByteSizeW(jitter):
    """"
    [ShLwApi.dll] PWSTR StrFormatByteSizeW(LONGLONG qdw, PWSTR pszBuf, UINT cchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["qdw", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrFormatByteSizeEx(jitter):
    """"
    [ShLwApi.dll] HRESULT StrFormatByteSizeEx(ULONGLONG ull, SFBS_FLAGS flags, LPWSTR pszBuf, UINT cchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ull", "flags", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrFormatKBSize(jitter):
    """"
    [ShLwApi.dll] PTSTR StrFormatKBSize(LONGLONG qdw, PTSTR pszBuf, UINT cchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["qdw", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrFromTimeInterval(jitter):
    """"
    [ShLwApi.dll] int StrFromTimeInterval(PTSTR pszOut, UINT cchMax, DWORD dwTimeMS, int digits)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszOut", "cchMax", "dwTimeMS", "digits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrIsIntlEqual(jitter):
    """"
    [ShLwApi.dll] BOOL StrIsIntlEqual(BOOL fCaseSens, PCTSTR pszString1, PCTSTR pszString2, int nChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fCaseSens", "pszString1", "pszString2", "nChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrNCat(jitter):
    """"
    [ShLwApi.dll] PTSTR StrNCat(PTSTR psz1, PCTSTR psz2, int cchMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psz1", "psz2", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrPBrk(jitter):
    """"
    [ShLwApi.dll] PTSTR StrPBrk(PTSTR psz, PCTSTR pszSet)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psz", "pszSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrRChr(jitter):
    """"
    [ShLwApi.dll] PTSTR StrRChr(PTSTR pszStart, PCTSTR pszEnd, TCHAR wMatch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszStart", "pszEnd", "wMatch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrRChrI(jitter):
    """"
    [ShLwApi.dll] PTSTR StrRChrI(PTSTR pszStart, PCTSTR pszEnd, TCHAR wMatch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszStart", "pszEnd", "wMatch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrRetToBSTR(jitter):
    """"
    [ShLwApi.dll] HRESULT StrRetToBSTR(STRRET* pstr, PCUITEMID_CHILD pidl, BSTR* pbstr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstr", "pidl", "pbstr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrRetToBuf(jitter):
    """"
    [ShLwApi.dll] HRESULT StrRetToBuf(STRRET* pstr, PCUITEMID_CHILD pidl, LPTSTR pszBuf, UINT cchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstr", "pidl", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrRetToStr(jitter):
    """"
    [ShLwApi.dll] HRESULT StrRetToStr(STRRET* pstr, PCUITEMID_CHILD pidl, LPTSTR* ppszName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstr", "pidl", "ppszName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrRStrI(jitter):
    """"
    [ShLwApi.dll] PTSTR StrRStrI(PTSTR pszSource, PCTSTR pszLast, PCTSTR pszSrch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszSource", "pszLast", "pszSrch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrSpn(jitter):
    """"
    [ShLwApi.dll] int StrSpn(PCTSTR psz, PCTSTR pszSet)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psz", "pszSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrStr(jitter):
    """"
    [ShLwApi.dll] PTSTR StrStr(PTSTR pszFirst, PCTSTR pszSrch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszFirst", "pszSrch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrStrI(jitter):
    """"
    [ShLwApi.dll] PTSTR StrStrI(PTSTR pszFirst, PCTSTR pszSrch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszFirst", "pszSrch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrToInt(jitter):
    """"
    [ShLwApi.dll] int StrToInt(PCTSTR pszSrc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrToInt64Ex(jitter):
    """"
    [ShLwApi.dll] BOOL StrToInt64Ex(PCTSTR pszString, STIF_FLAGS dwFlags, LONGLONG* pllRet)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszString", "dwFlags", "pllRet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrToIntEx(jitter):
    """"
    [ShLwApi.dll] BOOL StrToIntEx(PCTSTR pszString, STIF_FLAGS dwFlags, int* piRet)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszString", "dwFlags", "piRet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StrTrim(jitter):
    """"
    [ShLwApi.dll] BOOL StrTrim(PTSTR psz, PCTSTR pszTrimChars)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psz", "pszTrimChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_wnsprintf(jitter):
    """"
    [ShLwApi.dll] int wnsprintf(PTSTR pszDest, int cchDest, PCTSTR pszFmt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszDest", "cchDest", "pszFmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_wvnsprintf(jitter):
    """"
    [ShLwApi.dll] int wvnsprintf(PTSTR pszDest, int cchDest, PCTSTR pszFmt, va_list arglist)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszDest", "cchDest", "pszFmt", "arglist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ConnectToConnectionPoint(jitter):
    """"
    [ShLwApi.dll] HRESULT ConnectToConnectionPoint(IUnknown* punk, REFIID riidEvent, BOOL fConnect, IUnknown* punkTarget, DWORD* pdwCookie, IConnectionPoint** ppcpOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["punk", "riidEvent", "fConnect", "punkTarget", "pdwCookie", "ppcpOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_DllInstall(jitter):
    """"
    [ShLwApi.dll] HRESULT DllInstall(BOOL bInstall, PCWSTR pszCmdLine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bInstall", "pszCmdLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_FindResourceWrapW(jitter):
    """"
    [ShLwApi.dll] HRSRC FindResourceWrapW(HMODULE hModule, LPCWSTR lpName, LPCWSTR lpType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "lpName", "lpType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_GetMenuPosFromID(jitter):
    """"
    [ShLwApi.dll] int GetMenuPosFromID(HMENU hmenu, UINT id)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmenu", "id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_HashData(jitter):
    """"
    [ShLwApi.dll] HRESULT HashData(BYTE* pbData, DWORD cbData, BYTE* pbHash, DWORD cbHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pbData", "cbData", "pbHash", "cbHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_GUIDFromString(jitter):
    """"
    [ShLwApi.dll] BOOL GUIDFromString(LPCTSTR psz, LPGUID pguid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["psz", "pguid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IsInternetESCEnabled(jitter):
    """"
    [ShLwApi.dll] BOOL IsInternetESCEnabled()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IsOS(jitter):
    """"
    [ShLwApi.dll] BOOL IsOS(DWORD dwOS)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwOS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_Copy(jitter):
    """"
    [ShLwApi.dll] HRESULT IStream_Copy(IStream* pstmFrom, IStream* pstmTo, DWORD cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstmFrom", "pstmTo", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_Read(jitter):
    """"
    [ShLwApi.dll] HRESULT IStream_Read(IStream* pstm, VOID* pv, ULONG cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstm", "pv", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_ReadPidl(jitter):
    """"
    [ShLwApi.dll] HRESULT IStream_ReadPidl(IStream* pstm, PIDLIST_RELATIVE* ppidlOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstm", "ppidlOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_ReadStr(jitter):
    """"
    [ShLwApi.dll] HRESULT IStream_ReadStr(IStream* pstm, PWSTR* ppsz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstm", "ppsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_Reset(jitter):
    """"
    [ShLwApi.dll] HRESULT IStream_Reset(IStream* pstm)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_Size(jitter):
    """"
    [ShLwApi.dll] HRESULT IStream_Size(IStream* pstm, ULARGE_INTEGER* pui)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstm", "pui"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_Write(jitter):
    """"
    [ShLwApi.dll] HRESULT IStream_Write(IStream* pstm, const void* pv, ULONG cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstm", "pv", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_WritePidl(jitter):
    """"
    [ShLwApi.dll] HRESULT IStream_WritePidl(IStream* pstm, PCUIDLIST_RELATIVE pidlWrite)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstm", "pidlWrite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_WriteStr(jitter):
    """"
    [ShLwApi.dll] HRESULT IStream_WriteStr(IStream* pstm, PCWSTR psz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstm", "psz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_AtomicRelease(jitter):
    """"
    [ShLwApi.dll] void IUnknown_AtomicRelease(void** ppunk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ppunk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_GetSite(jitter):
    """"
    [ShLwApi.dll] HRESULT IUnknown_GetSite(IUnknown* punk, REFIID riid, VOID** ppvSite)
    """"
    ret_ad, args = jitter.func_args_stdcall(["punk", "riid", "ppvSite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_GetWindow(jitter):
    """"
    [ShLwApi.dll] HRESULT IUnknown_GetWindow(IUnknown* punk, HWND* phwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["punk", "phwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_QueryService(jitter):
    """"
    [ShLwApi.dll] HRESULT IUnknown_QueryService(IUnknown* punk, REFGUID guidService, REFIID riid, void** ppvOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["punk", "guidService", "riid", "ppvOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_Set(jitter):
    """"
    [ShLwApi.dll] void IUnknown_Set(IUnknown* ppunk, IUnknown* punk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ppunk", "punk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_SetSite(jitter):
    """"
    [ShLwApi.dll] HRESULT IUnknown_SetSite(IUnknown* punk, IUnknown* punkSite)
    """"
    ret_ad, args = jitter.func_args_stdcall(["punk", "punkSite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_MLFreeLibrary(jitter):
    """"
    [ShLwApi.dll] BOOL MLFreeLibrary(HMODULE hModule)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_MLLoadLibrary(jitter):
    """"
    [ShLwApi.dll] HINSTANCE MLLoadLibrary(LPCTSTR lpszLibFileName, HMODULE hModule, DWORD dwCrossCodePage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszLibFileName", "hModule", "dwCrossCodePage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_MLHtmlHelp(jitter):
    """"
    [ShLwApi.dll] HWND MLHtmlHelp(HWND hwndCaller, LPCTSTR pszFile, UINT uCommand, DWORD_PTR dwData, DWORD dwCrossCodePage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndCaller", "pszFile", "uCommand", "dwData", "dwCrossCodePage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_MLWinHelp(jitter):
    """"
    [ShLwApi.dll] BOOL MLWinHelp(HWND hWndMain, LPCTSTR lpszHelp, UINT uCommand, DWORD_PTR dwData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndMain", "lpszHelp", "uCommand", "dwData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ParseURL(jitter):
    """"
    [ShLwApi.dll] HRESULT ParseURL(LPCTSTR pcszUrl, PARSEDURL* ppu)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pcszUrl", "ppu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_QISearch(jitter):
    """"
    [ShLwApi.dll] HRESULT QISearch(void* that, LPCQITAB pqit, REFIID riid, void** ppv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["that", "pqit", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHAnsiToAnsi(jitter):
    """"
    [ShLwApi.dll] int SHAnsiToAnsi(LPCSTR pszSrc, LPWSTR pszDst, int cchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszSrc", "pszDst", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHAnsiToUnicode(jitter):
    """"
    [ShLwApi.dll] int SHAnsiToUnicode(PCSTR pszSrc, PWSTR pwszDst, int cwchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszSrc", "pwszDst", "cwchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHAutoComplete(jitter):
    """"
    [ShLwApi.dll] HRESULT SHAutoComplete(HWND hwndEdit, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndEdit", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateMemStream(jitter):
    """"
    [ShLwApi.dll] IStream* SHCreateMemStream(const BYTE* pInit, UINT cbInit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pInit", "cbInit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateStreamOnFile(jitter):
    """"
    [ShLwApi.dll] HRESULT SHCreateStreamOnFile(LPCTSTR pszFile, [STGM_FLAGS] grfMode, IStream** ppstm)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszFile", "grfMode", "ppstm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateStreamOnFileEx(jitter):
    """"
    [ShLwApi.dll] HRESULT SHCreateStreamOnFileEx(LPCWSTR pszFile, [STGM_FLAGS] grfMode, DWORD dwAttributes, BOOL fCreate, IStream* pstmTemplate, IStream** ppstm)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszFile", "grfMode", "dwAttributes", "fCreate", "pstmTemplate", "ppstm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateThread(jitter):
    """"
    [ShLwApi.dll] BOOL SHCreateThread(LPTHREAD_START_ROUTINE pfnThreadProc, void* pData, SHCT_FLAGS dwFlags, LPTHREAD_START_ROUTINE pfnCallback)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfnThreadProc", "pData", "dwFlags", "pfnCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateThreadRef(jitter):
    """"
    [ShLwApi.dll] HRESULT SHCreateThreadRef(LONG* pcRef, IUnknown** ppunk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pcRef", "ppunk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateThreadWithHandle(jitter):
    """"
    [ShLwApi.dll] BOOL SHCreateThreadWithHandle(LPTHREAD_START_ROUTINE pfnThreadProc, void* pData, SHCT_FLAGS flags, LPTHREAD_START_ROUTINE pfnCallback, HANDLE* pHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfnThreadProc", "pData", "flags", "pfnCallback", "pHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHFormatDateTime(jitter):
    """"
    [ShLwApi.dll] int SHFormatDateTime(const FILETIME* pft, DWORD* pdwFlags, LPTSTR pszBuf, UINT cchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pft", "pdwFlags", "pszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGetThreadRef(jitter):
    """"
    [ShLwApi.dll] HRESULT SHGetThreadRef(IUnknown** ppunk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ppunk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHSetThreadRef(jitter):
    """"
    [ShLwApi.dll] HRESULT SHSetThreadRef(IUnknown* punk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["punk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHReleaseThreadRef(jitter):
    """"
    [ShLwApi.dll] HRESULT SHReleaseThreadRef()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGlobalCounterDecrement(jitter):
    """"
    [ShLwApi.dll] long SHGlobalCounterDecrement(const SHGLOBALCOUNTER id)
    """"
    ret_ad, args = jitter.func_args_stdcall(["id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGlobalCounterGetValue(jitter):
    """"
    [ShLwApi.dll] long SHGlobalCounterGetValue(const SHGLOBALCOUNTER id)
    """"
    ret_ad, args = jitter.func_args_stdcall(["id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGlobalCounterIncrement(jitter):
    """"
    [ShLwApi.dll] long SHGlobalCounterIncrement(const SHGLOBALCOUNTER id)
    """"
    ret_ad, args = jitter.func_args_stdcall(["id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHIsChildOrSelf(jitter):
    """"
    [ShLwApi.dll] HRESULT SHIsChildOrSelf(HWND hwndParent, HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHIsLowMemoryMachine(jitter):
    """"
    [ShLwApi.dll] BOOL SHIsLowMemoryMachine(DWORD dwType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHMessageBoxCheck(jitter):
    """"
    [ShLwApi.dll] int SHMessageBoxCheck(HWND hwnd, LPCTSTR pszText, LPCTSTR pszCaption, UINT uType, int iDefault, LPCTSTR pszRegVal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszText", "pszCaption", "uType", "iDefault", "pszRegVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHSendMessageBroadcast(jitter):
    """"
    [ShLwApi.dll] LRESULT SHSendMessageBroadcast(UINT uMsg, WPARAM wParam, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uMsg", "wParam", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHStripMneumonic(jitter):
    """"
    [ShLwApi.dll] TCHAR SHStripMneumonic(LPTSTR* pszMenu)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszMenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHUnicodeToAnsi(jitter):
    """"
    [ShLwApi.dll] int SHUnicodeToAnsi(PCWSTR pwszSrc, PSTR pszDst, int cchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszSrc", "pszDst", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHUnicodeToUnicode(jitter):
    """"
    [ShLwApi.dll] int SHUnicodeToUnicode(PCWSTR pwzSrc, PWSTR pwzDst, int cwchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwzSrc", "pwzDst", "cwchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StopWatchFlush(jitter):
    """"
    [ShLwApi.dll] [ERROR_CODE] StopWatchFlush()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_StopWatchMode(jitter):
    """"
    [ShLwApi.dll] DWORD StopWatchMode()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_WhichPlatform(jitter):
    """"
    [ShLwApi.dll] UINT WhichPlatform()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_GetProcessReference(jitter):
    """"
    [ShLwApi.dll] HRESULT GetProcessReference(IUnknown** punk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["punk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SetProcessReference(jitter):
    """"
    [ShLwApi.dll] void SetProcessReference(IUnknown* punk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["punk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRunIndirectRegClientCommand(jitter):
    """"
    [ShLwApi.dll] HRESULT SHRunIndirectRegClientCommand(HWND hwnd, LPCWSTR pszClientType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszClientType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_DupWideToAnsi(jitter):
    """"
    [ShLwApi.dll] HRESULT DupWideToAnsi(LPCWSTR pwszString, LPSTR* ppszStr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszString", "ppszStr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_ReadStrLong(jitter):
    """"
    [ShLwApi.dll] HRESULT IStream_ReadStrLong(IStream* pStream, LPWSTR* ppwszString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStream", "ppwszString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IStream_WriteStrLong(jitter):
    """"
    [ShLwApi.dll] HRESULT IStream_WriteStrLong(IStream* pStream, LPCWSTR pwszString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStream", "pwszString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_RemoveBackReferences(jitter):
    """"
    [ShLwApi.dll] HRESULT IUnknown_RemoveBackReferences(IUnknown* pUnk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_TranslateAcceleratorGlobal(jitter):
    """"
    [ShLwApi.dll] HRESULT IUnknown_TranslateAcceleratorGlobal(IUnknown* pUnk, MSG* pMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "pMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_IUnknown_TranslateAcceleratorIO(jitter):
    """"
    [ShLwApi.dll] HRESULT IUnknown_TranslateAcceleratorIO(IUnknown* pUnk, MSG* pMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "pMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_MapWin32ErrorToSTG(jitter):
    """"
    [ShLwApi.dll] HRESULT MapWin32ErrorToSTG(HRESULT hrWin32)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hrWin32"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_ModeToCreateFileFlags(jitter):
    """"
    [ShLwApi.dll] HRESULT ModeToCreateFileFlags([STGM_FLAGS] grfFlags, BOOL bCreate, DWORD* pDesiredAccess, DWORD* pShareMode, DWORD* pDisposition)
    """"
    ret_ad, args = jitter.func_args_stdcall(["grfFlags", "bCreate", "pDesiredAccess", "pShareMode", "pDisposition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathUnExpandEnvStringsForUserW(jitter):
    """"
    [ShLwApi.dll] BOOL PathUnExpandEnvStringsForUserW(HANDLE hUserToken, LPCWSTR pwszPath, LPWSTR pwszBuf, UINT cchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hUserToken", "pwszPath", "pwszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_PathUnExpandSystemEnvStringsW(jitter):
    """"
    [ShLwApi.dll] BOOL PathUnExpandSystemEnvStringsW(LPCWSTR pwszPath, LPWSTR pwszBuf, UINT cchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszPath", "pwszBuf", "cchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_QuerySourceCreateFromKey(jitter):
    """"
    [ShLwApi.dll] HRESULT QuerySourceCreateFromKey(HKEY hKey, LPCWSTR pwszSubKey, BOOL shouldCreate, REFIID riid, LPVOID* ppInterface)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pwszSubKey", "shouldCreate", "riid", "ppInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_QuerySourceCreateFromKeyEx(jitter):
    """"
    [ShLwApi.dll] HRESULT QuerySourceCreateFromKeyEx(HKEY hKey, LPCWSTR pwszSubKey, BOOL shouldCreate, ACCESS_MASK amDesired, REFIID riid, LPVOID* ppInterface)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pwszSubKey", "shouldCreate", "amDesired", "riid", "ppInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHAnsiToUnicodeCPAlloc(jitter):
    """"
    [ShLwApi.dll] HRESULT SHAnsiToUnicodeCPAlloc(UINT codePage, LPCSTR pszString, LPWSTR* ppwszConverted)
    """"
    ret_ad, args = jitter.func_args_stdcall(["codePage", "pszString", "ppwszConverted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHAreIconsEqual(jitter):
    """"
    [ShLwApi.dll] BOOL SHAreIconsEqual(HICON hIcon1, HICON hIcon2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIcon1", "hIcon2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHBoolSystemParametersInfo(jitter):
    """"
    [ShLwApi.dll] BOOL SHBoolSystemParametersInfo([SystemParametersInfoEnum] uiAction, PVOID pData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uiAction", "pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreatePropertyBagOnMemory(jitter):
    """"
    [ShLwApi.dll] HRESULT SHCreatePropertyBagOnMemory(PVOID pUnused, REFIID riid, PVOID* ppv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnused", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreatePropertyStoreOnXML(jitter):
    """"
    [ShLwApi.dll] HRESULT SHCreatePropertyStoreOnXML(IXMLDOMNode* pXmlDomNode, [STGM_FLAGS] grfMode, IPropertyBag* pPropBagInit, REFIID riid, PVOID* ppv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pXmlDomNode", "grfMode", "pPropBagInit", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateStreamOnDllResourceW(jitter):
    """"
    [ShLwApi.dll] HRESULT SHCreateStreamOnDllResourceW(LPCWSTR pwszModule, LPCWSTR pwszName, LPCWSTR pwszType, IStream** ppStream)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszModule", "pwszName", "pwszType", "ppStream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHCreateStreamOnModuleResourceW(jitter):
    """"
    [ShLwApi.dll] HRESULT SHCreateStreamOnModuleResourceW(HMODULE hModule, LPCWSTR pwszName, LPCWSTR pwszType, IStream** ppStream)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hModule", "pwszName", "pwszType", "ppStream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHExpandEnvironmentStringsAlloc(jitter):
    """"
    [ShLwApi.dll] HRESULT SHExpandEnvironmentStringsAlloc(LPCWSTR pwszExpandableString, LPWSTR* ppwszExpanded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszExpandableString", "ppwszExpanded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHForwardContextMenuMsg(jitter):
    """"
    [ShLwApi.dll] HRESULT SHForwardContextMenuMsg(IUnknown* pUnk, UINT uMsg, WPARAM wParam, LPARAM lParam, LRESULT* pResult, BOOL useIContextMenu2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "uMsg", "wParam", "lParam", "pResult", "useIContextMenu2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHGetSizeShared(jitter):
    """"
    [ShLwApi.dll] DWORD SHGetSizeShared(PVOID pData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHInvokeCommandOnContextMenu(jitter):
    """"
    [ShLwApi.dll] HRESULT SHInvokeCommandOnContextMenu(HWND hwnd, IObjectWithSite* pSite, IContextMenu* pCtxMenu, [CMIC_Mask] fMask, LPCSTR pszVerb, LPCWSTR pwszDirectory)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pSite", "pCtxMenu", "fMask", "pszVerb", "pwszDirectory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHInvokeCommandOnContextMenuEx(jitter):
    """"
    [ShLwApi.dll] HRESULT SHInvokeCommandOnContextMenuEx(HWND hwnd, IObjectWithSite* pSite, IContextMenu* pCtxMenu, [CMIC_Mask] fMask, UINT queryFlags, LPCSTR pszVerb, LPCWSTR pwszDirectory)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pSite", "pCtxMenu", "fMask", "queryFlags", "pszVerb", "pwszDirectory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHInvokeCommandWithFlagsAndSite(jitter):
    """"
    [ShLwApi.dll] HRESULT SHInvokeCommandWithFlagsAndSite(HWND hwnd, IObjectWithSite* pSite, IShellFolder* pShellFolder, LPITEMIDLIST pidl, [CMIC_Mask] fMask, LPCSTR pszVerb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pSite", "pShellFolder", "pidl", "fMask", "pszVerb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHInvokeCommandsOnContextMenuEx(jitter):
    """"
    [ShLwApi.dll] HRESULT SHInvokeCommandsOnContextMenuEx(HWND hwnd, IObjectWithSite* pSite, IContextMenu* pCtxMenu, [CMIC_Mask] fMask, UINT queryFlags, LPCSTR* ppszVerbs, UINT numVerbs, LPCWSTR pwszDirectory)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pSite", "pCtxMenu", "fMask", "queryFlags", "ppszVerbs", "numVerbs", "pwszDirectory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHRegSetValue(jitter):
    """"
    [ShLwApi.dll] LSTATUS SHRegSetValue(HKEY hKey, LPCWSTR pwszSubKey, LPCWSTR pwszValue, SRRF srrfFlags, DWORD dwType, LPCVOID pvData, DWORD cbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pwszSubKey", "pwszValue", "srrfFlags", "dwType", "pvData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shlwapi_SHUnicodeToAnsiCPAlloc(jitter):
    """"
    [ShLwApi.dll] HRESULT SHUnicodeToAnsiCPAlloc(UINT codePage, LPCWSTR pwszString, LPSTR* ppszConverted)
    """"
    ret_ad, args = jitter.func_args_stdcall(["codePage", "pwszString", "ppszConverted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
