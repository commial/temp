
def urlmon_CreateFormatEnumerator(jitter):
    """
    [urlmon.dll] HRESULT CreateFormatEnumerator(UINT cfmtetc, FORMATETC* rgfmtetc, IEnumFORMATETC** ppenumfmtetc)
    """
    ret_ad, args = jitter.func_args_stdcall(["cfmtetc", "rgfmtetc", "ppenumfmtetc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetCreateSecurityManager(jitter):
    """
    [urlmon.dll] HRESULT CoInternetCreateSecurityManager(IServiceProvider* pSP, IInternetSecurityManager** ppSM, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pSP", "ppSM", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetCreateZoneManager(jitter):
    """
    [urlmon.dll] HRESULT CoInternetCreateZoneManager(IServiceProvider* pSP, IInternetZoneManager** ppZM, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pSP", "ppZM", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetGetSecurityUrl(jitter):
    """
    [urlmon.dll] HRESULT CoInternetGetSecurityUrl(LPCWSTR pwzUrl, LPWSTR* ppwzSecUrl, PSUACTION psuAction, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzUrl", "ppwzSecUrl", "psuAction", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetGetSecurityUrlEx(jitter):
    """
    [urlmon.dll] HRESULT CoInternetGetSecurityUrlEx(IUri* pUri, IUri** ppSecUri, PSUACTION psuAction, DWORD_PTR dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pUri", "ppSecUri", "psuAction", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetIsFeatureEnabled(jitter):
    """
    [urlmon.dll] HRESULT CoInternetIsFeatureEnabled(INTERNETFEATURELIST FeatureEntry, [GetFeatureFlag] dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["FeatureEntry", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetIsFeatureEnabledForIUri(jitter):
    """
    [urlmon.dll] STDAPI CoInternetIsFeatureEnabledForIUri(INTERNETFEATURELIST FeatureEntry, [GetFeatureFlag] dwFlags, IUri* pIUri, IInternetSecurityManagerEx2* pSecMgr)
    """
    ret_ad, args = jitter.func_args_stdcall(["FeatureEntry", "dwFlags", "pIUri", "pSecMgr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetIsFeatureEnabledForUrl(jitter):
    """
    [urlmon.dll] HRESULT CoInternetIsFeatureEnabledForUrl(INTERNETFEATURELIST FeatureEntry, [GetFeatureFlag] dwFlags, LPCWSTR szURL, IInternetSecurityManager* pSecMgr)
    """
    ret_ad, args = jitter.func_args_stdcall(["FeatureEntry", "dwFlags", "szURL", "pSecMgr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetIsFeatureZoneElevationEnabled(jitter):
    """
    [urlmon.dll] HRESULT CoInternetIsFeatureZoneElevationEnabled(LPCWSTR szFromURL, LPCWSTR szToURL, IInternetSecurityManager* pSecMgr, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["szFromURL", "szToURL", "pSecMgr", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetSetFeatureEnabled(jitter):
    """
    [urlmon.dll] HRESULT CoInternetSetFeatureEnabled(INTERNETFEATURELIST FeatureEntry, DWORD dwFlags, BOOL fEnable)
    """
    ret_ad, args = jitter.func_args_stdcall(["FeatureEntry", "dwFlags", "fEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_AsyncInstallDistributionUnit(jitter):
    """
    [urlmon.dll] HRESULT AsyncInstallDistributionUnit(LPCWSTR szDistUnit, LPCWSTR szTYPE, LPCWSTR szExt, DWORD dwFileVersionMS, DWORD dwFileVersionLS, LPCWSTR szURL, IBindCtx* pbc, LPVOID pvReserved, DWORD flags)
    """
    ret_ad, args = jitter.func_args_stdcall(["szDistUnit", "szTYPE", "szExt", "dwFileVersionMS", "dwFileVersionLS", "szURL", "pbc", "pvReserved", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoGetClassObjectFromURL(jitter):
    """
    [urlmon.dll] HRESULT CoGetClassObjectFromURL(REFCLSID rclsid, LPCWSTR szCodeURL, DWORD dwFileVersionMS, DWORD dwFileVersionLS, LPCWSTR szContentType, LPBINDCTX pBindCtx, DWORD dwClsContext, LPVOID pvReserved, REFIID riid, VOID** ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "szCodeURL", "dwFileVersionMS", "dwFileVersionLS", "szContentType", "pBindCtx", "dwClsContext", "pvReserved", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetCombineIUri(jitter):
    """
    [urlmon.dll] HRESULT CoInternetCombineIUri(IUri* pBaseUri, IUri* pRelativeUri, [UrlFlags] dwCombineFlags, IUri** ppCombinedUri, DWORD_PTR dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pBaseUri", "pRelativeUri", "dwCombineFlags", "ppCombinedUri", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetCombineUrl(jitter):
    """
    [urlmon.dll] HRESULT CoInternetCombineUrl(LPCWSTR pwzBaseUrl, LPCWSTR pwzRelativeUrl, [UrlFlags] dwCombineFlags, LPWSTR pwzResult, DWORD cchResult, DWORD* pcchResult, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzBaseUrl", "pwzRelativeUrl", "dwCombineFlags", "pwzResult", "cchResult", "pcchResult", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetCombineUrlEx(jitter):
    """
    [urlmon.dll] HRESULT CoInternetCombineUrlEx(IUri* pBaseUri, LPCWSTR pwzRelativeUrl, [UrlFlags] dwCombineFlags, IUri** ppCombinedUri, DWORD_PTR dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pBaseUri", "pwzRelativeUrl", "dwCombineFlags", "ppCombinedUri", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetCompareUrl(jitter):
    """
    [urlmon.dll] HRESULT CoInternetCompareUrl(LPCWSTR pwzUrl1, LPCWSTR pwzUrl2, DWORD dwCompareFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzUrl1", "pwzUrl2", "dwCompareFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetGetProtocolFlags(jitter):
    """
    [urlmon.dll] HRESULT CoInternetGetProtocolFlags(LPCWSTR pwzUrl, DWORD* pdwFlags, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzUrl", "pdwFlags", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetGetSession(jitter):
    """
    [urlmon.dll] HRESULT CoInternetGetSession(DWORD dwSessionMode, IInternetSession** ppIInternetSession, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwSessionMode", "ppIInternetSession", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetParseIUri(jitter):
    """
    [urlmon.dll] STDAPI CoInternetParseIUri(IUri* pIUri, PARSEACTION ParseAction, DWORD dwFlags, LPWSTR pwzResult, DWORD cchResult, DWORD* pcchResult, DWORD_PTR dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pIUri", "ParseAction", "dwFlags", "pwzResult", "cchResult", "pcchResult", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetParseUrl(jitter):
    """
    [urlmon.dll] STDAPI CoInternetParseUrl(LPCWSTR pwzUrl, PARSEACTION ParseAction, DWORD dwFlags, LPWSTR pszResult, DWORD cchResult, DWORD* pcchResult, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzUrl", "ParseAction", "dwFlags", "pszResult", "cchResult", "pcchResult", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CoInternetQueryInfo(jitter):
    """
    [urlmon.dll] HRESULT CoInternetQueryInfo(LPCWSTR pwzUrl, QUERYOPTION QueryOption, DWORD dwQueryFlags, LPVOID pvBuffer, DWORD cbBuffer, DWORD* pcbBuffer, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzUrl", "QueryOption", "dwQueryFlags", "pvBuffer", "cbBuffer", "pcbBuffer", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CompareSecurityIds(jitter):
    """
    [urlmon.dll] HRESULT CompareSecurityIds(BYTE* pbSecurityId1, DWORD dwLen1, BYTE* pbSecurityId2, DWORD dwLen2, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbSecurityId1", "dwLen1", "pbSecurityId2", "dwLen2", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CopyBindInfo(jitter):
    """
    [urlmon.dll] HRESULT CopyBindInfo(const BINDINFO* pcbiSrc, BINDINFO* pcbiDest)
    """
    ret_ad, args = jitter.func_args_stdcall(["pcbiSrc", "pcbiDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CopyStgMedium(jitter):
    """
    [urlmon.dll] HRESULT CopyStgMedium(const STGMEDIUM* pcstgmedSrc, STGMEDIUM* pstgmedDest)
    """
    ret_ad, args = jitter.func_args_stdcall(["pcstgmedSrc", "pstgmedDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CreateAsyncBindCtx(jitter):
    """
    [urlmon.dll] HRESULT CreateAsyncBindCtx(DWORD dwReserved, IBindStatusCallback* pbsc, IEnumFORMATETC* penumfmtetc, IBindCtx** ppbc)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwReserved", "pbsc", "penumfmtetc", "ppbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CreateAsyncBindCtxEx(jitter):
    """
    [urlmon.dll] HRESULT CreateAsyncBindCtxEx(IBindCtx* pbc, DWORD dwOptions, IBindStatusCallback* pBSCb, IEnumFORMATETC* pEnum, IBindCtx** ppBC, DWORD reserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbc", "dwOptions", "pBSCb", "pEnum", "ppBC", "reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CreateIUriBuilder(jitter):
    """
    [urlmon.dll] STDAPI CreateIUriBuilder(IUri* pIUri, DWORD dwFlags, DWORD_PTR dwReserved, IUriBuilder** ppIUriBuilder)
    """
    ret_ad, args = jitter.func_args_stdcall(["pIUri", "dwFlags", "dwReserved", "ppIUriBuilder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CreateUri(jitter):
    """
    [urlmon.dll] STDAPI CreateUri(LPCWSTR pwzURI, [Uri_CREATE_FLAGS] dwFlags, DWORD_PTR dwReserved, IUri** ppURI)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzURI", "dwFlags", "dwReserved", "ppURI"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CreateUriFromMultiByteString(jitter):
    """
    [urlmon.dll] HRESULT CreateUriFromMultiByteString(LPCSTR pszANSIInputUri, [Uri_ENCODING_FLAGS] dwEncodingFlags, DWORD dwCodePage, [Uri_CREATE_FLAGS] dwCreateFlags, DWORD_PTR dwReserved, IUri** ppURI)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszANSIInputUri", "dwEncodingFlags", "dwCodePage", "dwCreateFlags", "dwReserved", "ppURI"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CreateUriWithFragment(jitter):
    """
    [urlmon.dll] STDAPI CreateUriWithFragment(LPCWSTR pwzURI, LPCWSTR pwzFragment, [Uri_CREATE_FLAGS] dwFlags, DWORD_PTR dwReserved, IUri** ppURI)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzURI", "pwzFragment", "dwFlags", "dwReserved", "ppURI"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CreateURLBinding(jitter):
    """
    [urlmon.dll] STDAPI CreateURLBinding(LPCWSTR lpszUrl, IBindCtx* pbc, IBinding** ppBdg)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszUrl", "pbc", "ppBdg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CreateURLMoniker(jitter):
    """
    [urlmon.dll] HRESULT CreateURLMoniker(IMoniker* pMkCtx, LPCWSTR szURL, IMoniker** ppmk)
    """
    ret_ad, args = jitter.func_args_stdcall(["pMkCtx", "szURL", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CreateURLMonikerEx(jitter):
    """
    [urlmon.dll] HRESULT CreateURLMonikerEx(IMoniker* pMkCtx, LPCWSTR szURL, IMoniker** ppmk, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pMkCtx", "szURL", "ppmk", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_CreateURLMonikerEx2(jitter):
    """
    [urlmon.dll] HRESULT CreateURLMonikerEx2(IMoniker* pMkCtx, IUri* pUri, IMoniker** ppmk, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pMkCtx", "pUri", "ppmk", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_FaultInIEFeature(jitter):
    """
    [urlmon.dll] HRESULT FaultInIEFeature(HWND hWnd, uCLSSPEC* pClassSpec, QUERYCONTEXT* pQuery, [FIEF_FLAGS] dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pClassSpec", "pQuery", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_FindMediaType(jitter):
    """
    [urlmon.dll] HRESULT FindMediaType(LPCSTR rgszTypes, CLIPFORMAT* rgcfTypes)
    """
    ret_ad, args = jitter.func_args_stdcall(["rgszTypes", "rgcfTypes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_FindMediaTypeClass(jitter):
    """
    [urlmon.dll] HRESULT FindMediaTypeClass(LPBC pbc, LPCSTR szType, CLSID* pclsID, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbc", "szType", "pclsID", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_FindMimeFromData(jitter):
    """
    [urlmon.dll] HRESULT FindMimeFromData(LPBC pBC, LPCWSTR pwzUrl, LPVOID pBuffer, DWORD cbSize, LPCWSTR pwzMimeProposed, DWORD dwMimeFlags, LPWSTR* ppwzMimeOut, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pBC", "pwzUrl", "pBuffer", "cbSize", "pwzMimeProposed", "dwMimeFlags", "ppwzMimeOut", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_GetClassFileOrMime(jitter):
    """
    [urlmon.dll] HRESULT GetClassFileOrMime(LPBC pBC, LPCWSTR szFilename, LPVOID pBuffer, DWORD cbSize, LPCWSTR szMime, DWORD dwReserved, CLSID* pclsid)
    """
    ret_ad, args = jitter.func_args_stdcall(["pBC", "szFilename", "pBuffer", "cbSize", "szMime", "dwReserved", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_GetClassURL(jitter):
    """
    [urlmon.dll] HRESULT GetClassURL(LPCWSTR szURL, CLSID* pClsID)
    """
    ret_ad, args = jitter.func_args_stdcall(["szURL", "pClsID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_GetComponentIDFromCLSSPEC(jitter):
    """
    [urlmon.dll] HRESULT GetComponentIDFromCLSSPEC(uCLSSPEC* pClassSpec, LPSTR* ppszComponentID)
    """
    ret_ad, args = jitter.func_args_stdcall(["pClassSpec", "ppszComponentID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_IEInstallScope(jitter):
    """
    [urlmon.dll] HRESULT IEInstallScope(LPDWORD* pdwScope)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwScope"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_IsAsyncMoniker(jitter):
    """
    [urlmon.dll] HRESULT IsAsyncMoniker(IMoniker* pmk)
    """
    ret_ad, args = jitter.func_args_stdcall(["pmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_IsValidURL(jitter):
    """
    [urlmon.dll] HRESULT IsValidURL(LPBC pBC, LPCWSTR szURL, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pBC", "szURL", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_MkParseDisplayNameEx(jitter):
    """
    [urlmon.dll] HRESULT MkParseDisplayNameEx(IBindCtx* pbc, LPWSTR szDisplayName, ULONG* pcchEaten, IMoniker** ppmk)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbc", "szDisplayName", "pcchEaten", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_ObtainUserAgentString(jitter):
    """
    [urlmon.dll] HRESULT ObtainUserAgentString(DWORD dwOption, LPCSTR* pcszUAOut, DWORD* cbSize)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwOption", "pcszUAOut", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_RegisterBindStatusCallback(jitter):
    """
    [urlmon.dll] HRESULT RegisterBindStatusCallback(IBindCtx* pbc, IBindStatusCallback* pbsc, IBindStatusCallback** ppbscPrevious, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbc", "pbsc", "ppbscPrevious", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_RegisterFormatEnumerator(jitter):
    """
    [urlmon.dll] HRESULT RegisterFormatEnumerator(LPBC pBC, IEnumFORMATETC* pEFetc, DWORD reserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pBC", "pEFetc", "reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_RegisterMediaTypeClass(jitter):
    """
    [urlmon.dll] HRESULT RegisterMediaTypeClass(LPBC pbc, UINT ctypes, LPCSTR* rgszTypes, CLSID* rgclsID, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbc", "ctypes", "rgszTypes", "rgclsID", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_RegisterMediaTypes(jitter):
    """
    [urlmon.dll] HRESULT RegisterMediaTypes(UINT ctypes, LPCSTR* rgszTypes, CLIPFORMAT* rgcfTypes)
    """
    ret_ad, args = jitter.func_args_stdcall(["ctypes", "rgszTypes", "rgcfTypes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_ReleaseBindInfo(jitter):
    """
    [urlmon.dll] void ReleaseBindInfo(BINDINFO* pbindinfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbindinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_RevokeBindStatusCallback(jitter):
    """
    [urlmon.dll] HRESULT RevokeBindStatusCallback(IBindCtx* pbc, IBindStatusCallback* pbsc)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbc", "pbsc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_RevokeFormatEnumerator(jitter):
    """
    [urlmon.dll] HRESULT RevokeFormatEnumerator(LPBC pbc, IEnumFORMATETC* pEFetc)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbc", "pEFetc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_URLDownloadToCacheFile(jitter, get_str, set_str):
    """
    [urlmon.dll] HRESULT URLDownloadToCacheFile(LPUNKNOWN lpUnkcaller, LPCSTR szURL, LPTSTR szFileName, DWORD cchFileName, DWORD dwReserved, IBindStatusCallback* pBSC)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpUnkcaller", "szURL", "szFileName", "cchFileName", "dwReserved", "pBSC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_URLDownloadToCacheFileA(jitter):
    urlmon_URLDownloadToCacheFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def urlmon_URLDownloadToCacheFileW(jitter):
    urlmon_URLDownloadToCacheFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def urlmon_URLDownloadToFile(jitter, get_str, set_str):
    """
    [urlmon.dll] HRESULT URLDownloadToFile(LPUNKNOWN pCaller, LPCTSTR szURL, LPCTSTR szFileName, DWORD dwReserved, LPBINDSTATUSCALLBACK lpfnCB)
    """
    ret_ad, args = jitter.func_args_stdcall(["pCaller", "szURL", "szFileName", "dwReserved", "lpfnCB"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_URLDownloadToFileA(jitter):
    urlmon_URLDownloadToFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def urlmon_URLDownloadToFileW(jitter):
    urlmon_URLDownloadToFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def urlmon_UrlMkGetSessionOption(jitter):
    """
    [urlmon.dll] HRESULT UrlMkGetSessionOption([UrlMkSessionOption] dwOption, LPVOID pBuffer, DWORD dwBufferLength, DWORD* pdwBufferLengthOut, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwOption", "pBuffer", "dwBufferLength", "pdwBufferLengthOut", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_UrlMkSetSessionOption(jitter):
    """
    [urlmon.dll] HRESULT UrlMkSetSessionOption([UrlMkSessionOption] dwOption, LPVOID pBuffer, DWORD dwBufferLength, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwOption", "pBuffer", "dwBufferLength", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_URLOpenBlockingStream(jitter, get_str, set_str):
    """
    [urlmon.dll] HRESULT URLOpenBlockingStream(LPUNKNOWN pCaller, LPCSTR szURL, LPSTREAM* ppStream, DWORD dwReserved, LPBINDSTATUSCALLBACK lpfnCB)
    """
    ret_ad, args = jitter.func_args_stdcall(["pCaller", "szURL", "ppStream", "dwReserved", "lpfnCB"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_URLOpenBlockingStreamA(jitter):
    urlmon_URLOpenBlockingStream(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def urlmon_URLOpenBlockingStreamW(jitter):
    urlmon_URLOpenBlockingStream(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def urlmon_URLOpenPullStream(jitter, get_str, set_str):
    """
    [urlmon.dll] HRESULT URLOpenPullStream(LPUNKNOWN pCaller, LPCSTR szURL, DWORD dwReserved, LPBINDSTATUSCALLBACK lpfnCB)
    """
    ret_ad, args = jitter.func_args_stdcall(["pCaller", "szURL", "dwReserved", "lpfnCB"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_URLOpenPullStreamA(jitter):
    urlmon_URLOpenPullStream(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def urlmon_URLOpenPullStreamW(jitter):
    urlmon_URLOpenPullStream(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def urlmon_URLOpenStream(jitter, get_str, set_str):
    """
    [urlmon.dll] HRESULT URLOpenStream(LPUNKNOWN pCaller, LPCSTR szURL, DWORD dwReserved, LPBINDSTATUSCALLBACK lpfnCB)
    """
    ret_ad, args = jitter.func_args_stdcall(["pCaller", "szURL", "dwReserved", "lpfnCB"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def urlmon_URLOpenStreamA(jitter):
    urlmon_URLOpenStream(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def urlmon_URLOpenStreamW(jitter):
    urlmon_URLOpenStream(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def urlmon_CompatFlagsFromClsid(jitter):
    """
    [urlmon.dll] HRESULT CompatFlagsFromClsid(CLSID* pclsid, LPDWORD pdwCompatFlags, LPDWORD pdwMiscStatusFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pclsid", "pdwCompatFlags", "pdwMiscStatusFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
