
def ole32_BindMoniker(jitter):
    """"
    [Ole32.dll] HRESULT BindMoniker(LPMONIKER pmk, DWORD grfOpt, REFIID iidResult, LPVOID* ppvResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pmk", "grfOpt", "iidResult", "ppvResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CLSIDFromProgID(jitter):
    """"
    [Ole32.dll] HRESULT CLSIDFromProgID(LPCOLESTR lpszProgID, LPCLSID lpclsid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszProgID", "lpclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CLSIDFromProgIDEx(jitter):
    """"
    [Ole32.dll] HRESULT CLSIDFromProgIDEx(LPCOLESTR lpszProgID, LPCLSID lpclsid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszProgID", "lpclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CLSIDFromString(jitter):
    """"
    [Ole32.dll] HRESULT CLSIDFromString(LPCOLESTR lpsz, LPCLSID pclsid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpsz", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoAddRefServerProcess(jitter):
    """"
    [Ole32.dll] ULONG CoAddRefServerProcess()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoAllowSetForegroundWindow(jitter):
    """"
    [Ole32.dll] HRESULT CoAllowSetForegroundWindow(IUnknown* pUnk, LPVOID lpvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "lpvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCancelCall(jitter):
    """"
    [Ole32.dll] HRESULT CoCancelCall(DWORD dwThreadId, ULONG ulTimeout)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwThreadId", "ulTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCopyProxy(jitter):
    """"
    [Ole32.dll] HRESULT CoCopyProxy(IUnknown* pProxy, IUnknown** ppCopy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pProxy", "ppCopy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCreateFreeThreadedMarshaler(jitter):
    """"
    [Ole32.dll] HRESULT CoCreateFreeThreadedMarshaler(LPUNKNOWN punkOuter, LPUNKNOWN* ppunkMarshal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["punkOuter", "ppunkMarshal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCreateGuid(jitter):
    """"
    [Ole32.dll] HRESULT CoCreateGuid(GUID* pguid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pguid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCreateInstance(jitter):
    """"
    [Ole32.dll] HRESULT CoCreateInstance(REFCLSID rclsid, LPUNKNOWN pUnkOuter, [CLSCTX] dwClsContext, REFIID riid, LPVOID* ppv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "pUnkOuter", "dwClsContext", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCreateInstanceEx(jitter):
    """"
    [Ole32.dll] HRESULT CoCreateInstanceEx(REFCLSID rclsid, IUnknown* punkOuter, [CLSCTX] dwClsCtx, COSERVERINFO* pServerInfo, DWORD dwCount, MULTI_QI* pResults)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "punkOuter", "dwClsCtx", "pServerInfo", "dwCount", "pResults"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoDisableCallCancellation(jitter):
    """"
    [Ole32.dll] HRESULT CoDisableCallCancellation(LPVOID pReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoDisconnectContext(jitter):
    """"
    [Ole32.dll] HRESULT CoDisconnectContext(DWORD dwTimeout)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoDisconnectObject(jitter):
    """"
    [Ole32.dll] HRESULT CoDisconnectObject(LPUNKNOWN pUnk, DWORD dwReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoDosDateTimeToFileTime(jitter):
    """"
    [Ole32.dll] BOOL CoDosDateTimeToFileTime(WORD nDosDate, WORD nDosTime, FILETIME* lpFileTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nDosDate", "nDosTime", "lpFileTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoEnableCallCancellation(jitter):
    """"
    [Ole32.dll] HRESULT CoEnableCallCancellation(LPVOID pReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoFileTimeNow(jitter):
    """"
    [Ole32.dll] HRESULT CoFileTimeNow(FILETIME* lpFileTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoFileTimeToDosDateTime(jitter):
    """"
    [Ole32.dll] BOOL CoFileTimeToDosDateTime(FILETIME* lpFileTime, LPWORD lpDosDate, LPWORD lpDosTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileTime", "lpDosDate", "lpDosTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoFreeAllLibraries(jitter):
    """"
    [Ole32.dll] void CoFreeAllLibraries()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoFreeLibrary(jitter):
    """"
    [Ole32.dll] void CoFreeLibrary(HINSTANCE hInst)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoFreeUnusedLibraries(jitter):
    """"
    [Ole32.dll] void CoFreeUnusedLibraries()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoFreeUnusedLibrariesEx(jitter):
    """"
    [Ole32.dll] void CoFreeUnusedLibrariesEx(DWORD dwUnloadDelay, DWORD dwReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwUnloadDelay", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetApartmentType(jitter):
    """"
    [Ole32.dll] HRESULT CoGetApartmentType(APTTYPE* pAptType, APTTYPEQUALIFIER* pAptQualifier)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAptType", "pAptQualifier"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetCallContext(jitter):
    """"
    [Ole32.dll] HRESULT CoGetCallContext(REFIID riid, void** ppInterface)
    """"
    ret_ad, args = jitter.func_args_stdcall(["riid", "ppInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetCallerTID(jitter):
    """"
    [Ole32.dll] HRESULT CoGetCallerTID(LPDWORD lpdwTID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpdwTID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetCancelObject(jitter):
    """"
    [Ole32.dll] HRESULT CoGetCancelObject(DWORD dwThreadId, REFIID iid, void** ppUnk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwThreadId", "iid", "ppUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetClassObject(jitter):
    """"
    [Ole32.dll] HRESULT CoGetClassObject(REFCLSID rclsid, [CLSCTX] dwClsContext, COSERVERINFO* pServerInfo, REFIID riid, LPVOID* ppv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "dwClsContext", "pServerInfo", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetContextToken(jitter):
    """"
    [Ole32.dll] HRESULT CoGetContextToken(ULONG_PTR* pToken)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetCurrentLogicalThreadId(jitter):
    """"
    [Ole32.dll] HRESULT CoGetCurrentLogicalThreadId(GUID* pguid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pguid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetCurrentProcess(jitter):
    """"
    [Ole32.dll] DWORD CoGetCurrentProcess()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetInstanceFromFile(jitter):
    """"
    [Ole32.dll] HRESULT CoGetInstanceFromFile(COSERVERINFO* pServerInfo, CLSID* pClsid, IUnknown* punkOuter, [CLSCTX] dwClsCtx, [STGM_FLAGS] grfMode, OLECHAR* pwszName, DWORD dwCount, MULTI_QI* pResults)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pServerInfo", "pClsid", "punkOuter", "dwClsCtx", "grfMode", "pwszName", "dwCount", "pResults"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetInstanceFromIStorage(jitter):
    """"
    [Ole32.dll] HRESULT CoGetInstanceFromIStorage(COSERVERINFO* pServerInfo, CLSID* pClsid, IUnknown* punkOuter, [CLSCTX] dwClsCtx, struct IStorage* pstg, DWORD dwCount, MULTI_QI* pResults)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pServerInfo", "pClsid", "punkOuter", "dwClsCtx", "pstg", "dwCount", "pResults"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetInterceptor(jitter):
    """"
    [Ole32.dll] HRESULT CoGetInterceptor(REFIID iidIntercepted, IUnknown* punkOuter, REFIID iid, void** ppv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iidIntercepted", "punkOuter", "iid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetInterfaceAndReleaseStream(jitter):
    """"
    [Ole32.dll] HRESULT CoGetInterfaceAndReleaseStream(LPSTREAM pStm, REFIID iid, LPVOID* ppv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStm", "iid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetMalloc(jitter):
    """"
    [Ole32.dll] HRESULT CoGetMalloc(DWORD dwMemContext, LPMALLOC* ppMalloc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwMemContext", "ppMalloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetMarshalSizeMax(jitter):
    """"
    [Ole32.dll] HRESULT CoGetMarshalSizeMax(ULONG* pulSize, REFIID riid, LPUNKNOWN pUnk, DWORD dwDestContext, LPVOID pvDestContext, MSHLFLAGS mshlflags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pulSize", "riid", "pUnk", "dwDestContext", "pvDestContext", "mshlflags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetObject(jitter):
    """"
    [Ole32.dll] HRESULT CoGetObject(LPCWSTR pszName, BIND_OPTS* pBindOptions, REFIID riid, void** ppv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszName", "pBindOptions", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetObjectContext(jitter):
    """"
    [Ole32.dll] HRESULT CoGetObjectContext(REFIID riid, LPVOID* ppv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetPSClsid(jitter):
    """"
    [Ole32.dll] HRESULT CoGetPSClsid(REFIID riid, CLSID* pClsid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["riid", "pClsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetStandardMarshal(jitter):
    """"
    [Ole32.dll] HRESULT CoGetStandardMarshal(REFIID riid, LPUNKNOWN pUnk, DWORD dwDestContext, LPVOID pvDestContext, MSHLFLAGS mshlflags, LPMARSHAL* ppMarshal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["riid", "pUnk", "dwDestContext", "pvDestContext", "mshlflags", "ppMarshal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetStdMarshalEx(jitter):
    """"
    [Ole32.dll] HRESULT CoGetStdMarshalEx(LPUNKNOWN pUnkOuter, DWORD smexflags, LPUNKNOWN* ppUnkInner)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnkOuter", "smexflags", "ppUnkInner"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetTreatAsClass(jitter):
    """"
    [Ole32.dll] HRESULT CoGetTreatAsClass(REFCLSID clsidOld, LPCLSID pClsidNew)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clsidOld", "pClsidNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoImpersonateClient(jitter):
    """"
    [Ole32.dll] HRESULT CoImpersonateClient()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoInitialize(jitter):
    """"
    [Ole32.dll] HRESULT CoInitialize(LPVOID pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoInitializeEx(jitter):
    """"
    [Ole32.dll] HRESULT CoInitializeEx(LPVOID pvReserved, [COINIT_FLAG] dwCoInit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvReserved", "dwCoInit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoInitializeSecurity(jitter):
    """"
    [Ole32.dll] HRESULT CoInitializeSecurity(PSECURITY_DESCRIPTOR pSecDesc, LONG cAuthSvc, SOLE_AUTHENTICATION_SERVICE* asAuthSvc, void* pReserved1, [RPC_C_AUTHN_LEVEL] dwAuthnLevel, [RPC_C_IMP_LEVEL] dwImpLevel, void* pAuthList, EOLE_AUTHENTICATION_CAPABILITIES dwCapabilities, void* pReserved3)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecDesc", "cAuthSvc", "asAuthSvc", "pReserved1", "dwAuthnLevel", "dwImpLevel", "pAuthList", "dwCapabilities", "pReserved3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoInstall(jitter):
    """"
    [Ole32.dll] HRESULT CoInstall(IBindCtx* pbc, DWORD dwFlags, uCLSSPEC* pClassSpec, QUERYCONTEXT* pQuery, LPWSTR pszCodeBase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pbc", "dwFlags", "pClassSpec", "pQuery", "pszCodeBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoInvalidateRemoteMachineBindings(jitter):
    """"
    [Ole32.dll] HRESULT CoInvalidateRemoteMachineBindings(LPOLESTR pszMachineName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszMachineName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoIsHandlerConnected(jitter):
    """"
    [Ole32.dll] BOOL CoIsHandlerConnected(LPUNKNOWN pUnk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoIsOle1Class(jitter):
    """"
    [Ole32.dll] BOOL CoIsOle1Class(REFCLSID rclsid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoLoadLibrary(jitter):
    """"
    [Ole32.dll] HINSTANCE CoLoadLibrary(LPOLESTR lpszLibName, BOOL bAutoFree)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszLibName", "bAutoFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoLockObjectExternal(jitter):
    """"
    [Ole32.dll] HRESULT CoLockObjectExternal(LPUNKNOWN pUnk, BOOL fLock, BOOL fLastUnlockReleases)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "fLock", "fLastUnlockReleases"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoMarshalHresult(jitter):
    """"
    [Ole32.dll] HRESULT CoMarshalHresult(LPSTREAM pstm, HRESULT hresult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstm", "hresult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoMarshalInterface(jitter):
    """"
    [Ole32.dll] HRESULT CoMarshalInterface(LPSTREAM pStm, REFIID riid, LPUNKNOWN pUnk, DWORD dwDestContext, LPVOID pvDestContext, MSHLFLAGS mshlflags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStm", "riid", "pUnk", "dwDestContext", "pvDestContext", "mshlflags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoMarshalInterThreadInterfaceInStream(jitter):
    """"
    [Ole32.dll] HRESULT CoMarshalInterThreadInterfaceInStream(REFIID riid, LPUNKNOWN pUnk, LPSTREAM* ppStm)
    """"
    ret_ad, args = jitter.func_args_stdcall(["riid", "pUnk", "ppStm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoQueryAuthenticationServices(jitter):
    """"
    [Ole32.dll] HRESULT CoQueryAuthenticationServices(DWORD* pcAuthSvc, SOLE_AUTHENTICATION_SERVICE** asAuthSvc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pcAuthSvc", "asAuthSvc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoQueryClientBlanket(jitter):
    """"
    [Ole32.dll] HRESULT CoQueryClientBlanket(DWORD* pAuthnSvc, DWORD* pAuthzSvc, OLECHAR** pServerPrincName, DWORD* pAuthnLevel, DWORD* pImpLevel, RPC_AUTHZ_HANDLE* pPrivs, DWORD* pCapabilities)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAuthnSvc", "pAuthzSvc", "pServerPrincName", "pAuthnLevel", "pImpLevel", "pPrivs", "pCapabilities"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoQueryProxyBlanket(jitter):
    """"
    [Ole32.dll] HRESULT CoQueryProxyBlanket(IUnknown* pProxy, DWORD* pwAuthnSvc, DWORD* pAuthzSvc, OLECHAR** pServerPrincName, DWORD* pAuthnLevel, DWORD* pImpLevel, RPC_AUTH_IDENTITY_HANDLE* pAuthInfo, DWORD* pCapabilites)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pProxy", "pwAuthnSvc", "pAuthzSvc", "pServerPrincName", "pAuthnLevel", "pImpLevel", "pAuthInfo", "pCapabilites"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterClassObject(jitter):
    """"
    [Ole32.dll] HRESULT CoRegisterClassObject(REFCLSID rclsid, LPUNKNOWN pUnk, [CLSCTX] dwClsContext, REGCLS flags, LPDWORD lpdwRegister)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "pUnk", "dwClsContext", "flags", "lpdwRegister"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterInitializeSpy(jitter):
    """"
    [Ole32.dll] HRESULT CoRegisterInitializeSpy(LPINITIALIZESPY pSpy, ULARGE_INTEGER* puliCookie)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSpy", "puliCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterMallocSpy(jitter):
    """"
    [Ole32.dll] HRESULT CoRegisterMallocSpy(LPMALLOCSPY pMallocSpy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pMallocSpy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterMessageFilter(jitter):
    """"
    [Ole32.dll] HRESULT CoRegisterMessageFilter(LPMESSAGEFILTER lpMessageFilter, LPMESSAGEFILTER* lplpMessageFilter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMessageFilter", "lplpMessageFilter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterPSClsid(jitter):
    """"
    [Ole32.dll] HRESULT CoRegisterPSClsid(REFIID riid, REFCLSID rclsid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["riid", "rclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterSurrogate(jitter):
    """"
    [Ole32.dll] HRESULT CoRegisterSurrogate(LPSURROGATE pSurrogate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSurrogate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoReleaseMarshalData(jitter):
    """"
    [Ole32.dll] HRESULT CoReleaseMarshalData(LPSTREAM pStm)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoReleaseServerProcess(jitter):
    """"
    [Ole32.dll] ULONG CoReleaseServerProcess()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoResumeClassObjects(jitter):
    """"
    [Ole32.dll] HRESULT CoResumeClassObjects()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRevertToSelf(jitter):
    """"
    [Ole32.dll] HRESULT CoRevertToSelf()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRevokeClassObject(jitter):
    """"
    [Ole32.dll] HRESULT CoRevokeClassObject(DWORD dwRegister)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwRegister"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRevokeInitializeSpy(jitter):
    """"
    [Ole32.dll] HRESULT CoRevokeInitializeSpy(ULARGE_INTEGER uliCookie)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uliCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRevokeMallocSpy(jitter):
    """"
    [Ole32.dll] HRESULT CoRevokeMallocSpy()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoSetCancelObject(jitter):
    """"
    [Ole32.dll] HRESULT CoSetCancelObject(IUnknown* pUnk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoSetProxyBlanket(jitter):
    """"
    [Ole32.dll] HRESULT CoSetProxyBlanket(IUnknown* pProxy, [RPC_C_AUTHN_SVC] dwAuthnSvc, [RPC_C_AUTHZ] dwAuthzSvc, OLECHAR* pServerPrincName, [RPC_C_AUTHN_LEVEL] dwAuthnLevel, [RPC_C_IMP_LEVEL] dwImpLevel, RPC_AUTH_IDENTITY_HANDLE pAuthInfo, EOLE_AUTHENTICATION_CAPABILITIES dwCapabilities)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pProxy", "dwAuthnSvc", "dwAuthzSvc", "pServerPrincName", "dwAuthnLevel", "dwImpLevel", "pAuthInfo", "dwCapabilities"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoSuspendClassObjects(jitter):
    """"
    [Ole32.dll] HRESULT CoSuspendClassObjects()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoSwitchCallContext(jitter):
    """"
    [Ole32.dll] HRESULT CoSwitchCallContext(IUnknown* pNewObject, IUnknown** ppOldObject)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pNewObject", "ppOldObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoTaskMemAlloc(jitter):
    """"
    [Ole32.dll] LPVOID CoTaskMemAlloc(SIZE_T cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoTaskMemFree(jitter):
    """"
    [Ole32.dll] void CoTaskMemFree(LPVOID pv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoTaskMemRealloc(jitter):
    """"
    [Ole32.dll] LPVOID CoTaskMemRealloc(LPVOID pv, SIZE_T cb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pv", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoTestCancel(jitter):
    """"
    [Ole32.dll] HRESULT CoTestCancel()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoTreatAsClass(jitter):
    """"
    [Ole32.dll] HRESULT CoTreatAsClass(REFCLSID clsidOld, REFCLSID clsidNew)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clsidOld", "clsidNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoUninitialize(jitter):
    """"
    [Ole32.dll] void CoUninitialize()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoUnmarshalHresult(jitter):
    """"
    [Ole32.dll] HRESULT CoUnmarshalHresult(LPSTREAM pstm, HRESULT* phresult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstm", "phresult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoUnmarshalInterface(jitter):
    """"
    [Ole32.dll] HRESULT CoUnmarshalInterface(LPSTREAM pStm, REFIID riid, LPVOID* ppv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStm", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoWaitForMultipleHandles(jitter):
    """"
    [Ole32.dll] HRESULT CoWaitForMultipleHandles(DWORD dwFlags, DWORD dwTimeout, ULONG cHandles, LPHANDLE pHandles, LPDWORD lpdwindex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "dwTimeout", "cHandles", "pHandles", "lpdwindex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateAntiMoniker(jitter):
    """"
    [Ole32.dll] HRESULT CreateAntiMoniker(LPMONIKER* ppmk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateBindCtx(jitter):
    """"
    [Ole32.dll] HRESULT CreateBindCtx(DWORD reserved, LPBC* ppbc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["reserved", "ppbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateClassMoniker(jitter):
    """"
    [Ole32.dll] HRESULT CreateClassMoniker(REFCLSID rclsid, LPMONIKER* ppmk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateFileMoniker(jitter):
    """"
    [Ole32.dll] HRESULT CreateFileMoniker(LPCOLESTR lpszPathName, LPMONIKER* ppmk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPathName", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateGenericComposite(jitter):
    """"
    [Ole32.dll] HRESULT CreateGenericComposite(LPMONIKER pmkFirst, LPMONIKER pmkRest, LPMONIKER* ppmkComposite)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pmkFirst", "pmkRest", "ppmkComposite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateItemMoniker(jitter):
    """"
    [Ole32.dll] HRESULT CreateItemMoniker(LPCOLESTR lpszDelim, LPCOLESTR lpszItem, LPMONIKER* ppmk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDelim", "lpszItem", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateObjrefMoniker(jitter):
    """"
    [Ole32.dll] HRESULT CreateObjrefMoniker(LPUNKNOWN punk, LPMONIKER* ppmk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["punk", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreatePointerMoniker(jitter):
    """"
    [Ole32.dll] HRESULT CreatePointerMoniker(LPUNKNOWN punk, LPMONIKER* ppmk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["punk", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_GetClassFile(jitter):
    """"
    [Ole32.dll] HRESULT GetClassFile(LPCOLESTR szFilename, CLSID* pclsid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szFilename", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_GetRunningObjectTable(jitter):
    """"
    [Ole32.dll] HRESULT GetRunningObjectTable(DWORD reserved, LPRUNNINGOBJECTTABLE* pprot)
    """"
    ret_ad, args = jitter.func_args_stdcall(["reserved", "pprot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_IIDFromString(jitter):
    """"
    [Ole32.dll] HRESULT IIDFromString(LPCOLESTR lpsz, LPIID lpiid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpsz", "lpiid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_IsAccelerator(jitter):
    """"
    [Ole32.dll] BOOL IsAccelerator(HACCEL hAccel, int cAccelEntries, LPMSG lpMsg, WORD* lpwCmd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hAccel", "cAccelEntries", "lpMsg", "lpwCmd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_IsEqualGUID(jitter):
    """"
    [Ole32.dll] BOOL IsEqualGUID(REFGUID rguid1, REFGUID rguid2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rguid1", "rguid2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_MkParseDisplayName(jitter):
    """"
    [Ole32.dll] HRESULT MkParseDisplayName(LPBC pbc, LPCOLESTR szUserName, ULONG* pchEaten, LPMONIKER* ppmk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pbc", "szUserName", "pchEaten", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_MonikerCommonPrefixWith(jitter):
    """"
    [Ole32.dll] HRESULT MonikerCommonPrefixWith(LPMONIKER pmkThis, LPMONIKER pmkOther, LPMONIKER* ppmkCommon)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pmkThis", "pmkOther", "ppmkCommon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_MonikerRelativePathTo(jitter):
    """"
    [Ole32.dll] HRESULT MonikerRelativePathTo(LPMONIKER pmkSrc, LPMONIKER pmkDest, LPMONIKER* ppmkRelPath, BOOL dwReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pmkSrc", "pmkDest", "ppmkRelPath", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleDoAutoConvert(jitter):
    """"
    [Ole32.dll] HRESULT OleDoAutoConvert(LPSTORAGE pStg, LPCLSID pClsidNew)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStg", "pClsidNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleGetAutoConvert(jitter):
    """"
    [Ole32.dll] HRESULT OleGetAutoConvert(REFCLSID clsidOld, LPCLSID pClsidNew)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clsidOld", "pClsidNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleGetIconOfClass(jitter):
    """"
    [Ole32.dll] HGLOBAL OleGetIconOfClass(REFCLSID rclsid, LPOLESTR lpszLabel, BOOL fUseTypeAsLabel)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "lpszLabel", "fUseTypeAsLabel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleGetIconOfFile(jitter):
    """"
    [Ole32.dll] HGLOBAL OleGetIconOfFile(LPOLESTR lpszPath, BOOL fUseFileAsLabel)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPath", "fUseFileAsLabel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleRegGetMiscStatus(jitter):
    """"
    [Ole32.dll] HRESULT OleRegGetMiscStatus(REFCLSID clsid, DVASPECT dwAspect, DWORD* pdwStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clsid", "dwAspect", "pdwStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleRegGetUserType(jitter):
    """"
    [Ole32.dll] HRESULT OleRegGetUserType(REFCLSID clsid, DWORD dwFormOfType, LPOLESTR* pszUserType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clsid", "dwFormOfType", "pszUserType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleSetAutoConvert(jitter):
    """"
    [Ole32.dll] HRESULT OleSetAutoConvert(REFCLSID clsidOld, REFCLSID clsidNew)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clsidOld", "clsidNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_ProgIDFromCLSID(jitter):
    """"
    [Ole32.dll] HRESULT ProgIDFromCLSID(REFCLSID clsid, LPOLESTR* lplpszProgID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clsid", "lplpszProgID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StringFromCLSID(jitter):
    """"
    [Ole32.dll] HRESULT StringFromCLSID(REFCLSID rclsid, LPOLESTR* lplpsz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "lplpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StringFromGUID2(jitter):
    """"
    [Ole32.dll] int StringFromGUID2(REFGUID rguid, LPOLESTR lpsz, int cchMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rguid", "lpsz", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StringFromIID(jitter):
    """"
    [Ole32.dll] HRESULT StringFromIID(REFIID rclsid, LPOLESTR* lplpsz)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "lplpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterChannelHook(jitter):
    """"
    [Ole32.dll] HRESULT CoRegisterChannelHook(REFGUID ExtensionUuid, IChannelHook* pChannelHook)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExtensionUuid", "pChannelHook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCreateInstanceFromApp(jitter):
    """"
    [Ole32.dll] HRESULT CoCreateInstanceFromApp(REFCLSID rclsid, IUnknown* punkOuter, DWORD dwClsCtx, PVOID reserved, DWORD dwCount, MULTI_QI* pResults)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "punkOuter", "dwClsCtx", "reserved", "dwCount", "pResults"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoDecrementMTAUsage(jitter):
    """"
    [Ole32.dll] HRESULT CoDecrementMTAUsage(CO_MTA_USAGE_COOKIE Cookie)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoHandlePriorityEventsFromMessagePump(jitter):
    """"
    [Ole32.dll] void CoHandlePriorityEventsFromMessagePump()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoIncrementMTAUsage(jitter):
    """"
    [Ole32.dll] HRESULT CoIncrementMTAUsage(CO_MTA_USAGE_COOKIE* pCookie)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoSetMessageDispatcher(jitter):
    """"
    [Ole32.dll] HRESULT CoSetMessageDispatcher(PMessageDispatcher pMessageDispatcher)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pMessageDispatcher"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateDataAdviseHolder(jitter):
    """"
    [Ole32.dll] HRESULT CreateDataAdviseHolder(LPDATAADVISEHOLDER* ppDAHolder)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ppDAHolder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateDataCache(jitter):
    """"
    [Ole32.dll] HRESULT CreateDataCache(LPUNKNOWN pUnkOuter, REFCLSID rclsid, REFIID iid, LPVOID* ppv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnkOuter", "rclsid", "iid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateOleAdviseHolder(jitter):
    """"
    [Ole32.dll] HRESULT CreateOleAdviseHolder(LPOLEADVISEHOLDER* ppOAHolder)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ppOAHolder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_DoDragDrop(jitter):
    """"
    [Ole32.dll] HRESULT DoDragDrop(LPDATAOBJECT pDataObj, LPDROPSOURCE pDropSource, DWORD dwOKEffects, LPDWORD pdwEffect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pDataObj", "pDropSource", "dwOKEffects", "pdwEffect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreate(jitter):
    """"
    [Ole32.dll] HRESULT OleCreate(REFCLSID rclsid, REFIID riid, OLERENDER renderopt, LPFORMATETC pFormatEtc, LPOLECLIENTSITE pClientSite, LPSTORAGE pStg, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "riid", "renderopt", "pFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateDefaultHandler(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateDefaultHandler(REFCLSID clsid, LPUNKNOWN pUnkOuter, REFIID riid, LPVOID* lplpObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clsid", "pUnkOuter", "riid", "lplpObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateEmbeddingHelper(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateEmbeddingHelper(REFCLSID clsid, LPUNKNOWN pUnkOuter, DWORD flags, LPCLASSFACTORY pCF, REFIID riid, LPVOID* lplpObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clsid", "pUnkOuter", "flags", "pCF", "riid", "lplpObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateEx(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateEx(REFCLSID rclsid, REFIID riid, DWORD dwFlags, OLERENDER renderopt, ULONG cFormats, DWORD* rgAdvf, LPFORMATETC rgFormatEtc, IAdviseSink* lpAdviseSink, DWORD* rgdwConnection, LPOLECLIENTSITE pClientSite, LPSTORAGE pStg, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "riid", "dwFlags", "renderopt", "cFormats", "rgAdvf", "rgFormatEtc", "lpAdviseSink", "rgdwConnection", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateFromData(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateFromData(LPDATAOBJECT pSrcDataObj, REFIID riid, OLERENDER renderopt, LPFORMATETC pFormatEtc, LPOLECLIENTSITE pClientSite, LPSTORAGE pStg, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObj", "riid", "renderopt", "pFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateFromDataEx(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateFromDataEx(LPDATAOBJECT pSrcDataObj, REFIID riid, DWORD dwFlags, OLERENDER renderopt, ULONG cFormats, DWORD* rgAdvf, LPFORMATETC rgFormatEtc, IAdviseSink* lpAdviseSink, DWORD* rgdwConnection, LPOLECLIENTSITE pClientSite, LPSTORAGE pStg, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObj", "riid", "dwFlags", "renderopt", "cFormats", "rgAdvf", "rgFormatEtc", "lpAdviseSink", "rgdwConnection", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateFromFile(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateFromFile(REFCLSID rclsid, LPCOLESTR lpszFileName, REFIID riid, OLERENDER renderopt, LPFORMATETC lpFormatEtc, LPOLECLIENTSITE pClientSite, LPSTORAGE pStg, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "lpszFileName", "riid", "renderopt", "lpFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateFromFileEx(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateFromFileEx(REFCLSID rclsid, LPCOLESTR lpszFileName, REFIID riid, DWORD dwFlags, OLERENDER renderopt, ULONG cFormats, DWORD* rgAdvf, LPFORMATETC rgFormatEtc, IAdviseSink* lpAdviseSink, DWORD* rgdwConnection, LPOLECLIENTSITE pClientSite, LPSTORAGE pStg, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "lpszFileName", "riid", "dwFlags", "renderopt", "cFormats", "rgAdvf", "rgFormatEtc", "lpAdviseSink", "rgdwConnection", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateLink(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateLink(LPMONIKER pmkLinkSrc, REFIID riid, OLERENDER renderopt, LPFORMATETC lpFormatEtc, LPOLECLIENTSITE pClientSite, LPSTORAGE pStg, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pmkLinkSrc", "riid", "renderopt", "lpFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateLinkEx(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateLinkEx(LPMONIKER pmkLinkSrc, REFIID riid, DWORD dwFlags, OLERENDER renderopt, ULONG cFormats, DWORD* rgAdvf, LPFORMATETC rgFormatEtc, IAdviseSink* lpAdviseSink, DWORD* rgdwConnection, LPOLECLIENTSITE pClientSite, LPSTORAGE pStg, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pmkLinkSrc", "riid", "dwFlags", "renderopt", "cFormats", "rgAdvf", "rgFormatEtc", "lpAdviseSink", "rgdwConnection", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateLinkFromData(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateLinkFromData(LPDATAOBJECT pSrcDataObj, REFIID riid, OLERENDER renderopt, LPFORMATETC pFormatEtc, LPOLECLIENTSITE pClientSite, LPSTORAGE pStg, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObj", "riid", "renderopt", "pFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateLinkFromDataEx(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateLinkFromDataEx(LPDATAOBJECT pSrcDataObj, REFIID riid, DWORD dwFlags, OLERENDER renderopt, ULONG cFormats, DWORD* rgAdvf, LPFORMATETC rgFormatEtc, IAdviseSink* lpAdviseSink, DWORD* rgdwConnection, LPOLECLIENTSITE pClientSite, LPSTORAGE pStg, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObj", "riid", "dwFlags", "renderopt", "cFormats", "rgAdvf", "rgFormatEtc", "lpAdviseSink", "rgdwConnection", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateLinkToFile(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateLinkToFile(LPCOLESTR lpszFileName, REFIID riid, OLERENDER renderopt, LPFORMATETC lpFormatEtc, LPOLECLIENTSITE pClientSite, LPSTORAGE pStg, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszFileName", "riid", "renderopt", "lpFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateLinkToFileEx(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateLinkToFileEx(LPCOLESTR lpszFileName, REFIID riid, DWORD dwFlags, OLERENDER renderopt, ULONG cFormats, DWORD* rgAdvf, LPFORMATETC rgFormatEtc, IAdviseSink* lpAdviseSink, DWORD* rgdwConnection, LPOLECLIENTSITE pClientSite, LPSTORAGE pStg, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszFileName", "riid", "dwFlags", "renderopt", "cFormats", "rgAdvf", "rgFormatEtc", "lpAdviseSink", "rgdwConnection", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateMenuDescriptor(jitter):
    """"
    [Ole32.dll] HOLEMENU OleCreateMenuDescriptor(HMENU hmenuCombined, LPOLEMENUGROUPWIDTHS lpMenuWidths)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmenuCombined", "lpMenuWidths"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateStaticFromData(jitter):
    """"
    [Ole32.dll] HRESULT OleCreateStaticFromData(LPDATAOBJECT pSrcDataObj, REFIID iid, OLERENDER renderopt, LPFORMATETC pFormatEtc, LPOLECLIENTSITE pClientSite, LPSTORAGE pStg, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObj", "iid", "renderopt", "pFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleDestroyMenuDescriptor(jitter):
    """"
    [Ole32.dll] VOID OleDestroyMenuDescriptor(HOLEMENU holemenu)
    """"
    ret_ad, args = jitter.func_args_stdcall(["holemenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleDraw(jitter):
    """"
    [Ole32.dll] HRESULT OleDraw(LPUNKNOWN pUnknown, DVASPECT dwAspect, HDC hdcDraw, LPCRECT lprcBounds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnknown", "dwAspect", "hdcDraw", "lprcBounds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleDuplicateData(jitter):
    """"
    [Ole32.dll] HANDLE OleDuplicateData(HANDLE hSrc, CLIPFORMAT cfFormat, UINT uiFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSrc", "cfFormat", "uiFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleFlushClipboard(jitter):
    """"
    [Ole32.dll] HRESULT OleFlushClipboard()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleGetClipboard(jitter):
    """"
    [Ole32.dll] HRESULT OleGetClipboard(LPDATAOBJECT* ppDataObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ppDataObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleInitialize(jitter):
    """"
    [Ole32.dll] HRESULT OleInitialize(LPVOID pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleIsCurrentClipboard(jitter):
    """"
    [Ole32.dll] HRESULT OleIsCurrentClipboard(LPDATAOBJECT pDataObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pDataObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleIsRunning(jitter):
    """"
    [Ole32.dll] BOOL OleIsRunning(LPOLEOBJECT pObject)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleLoad(jitter):
    """"
    [Ole32.dll] HRESULT OleLoad(LPSTORAGE pStg, REFIID riid, REFCLSID rclsid, LPOLECLIENTSITE pClientSite, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStg", "riid", "rclsid", "pClientSite", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleLoadFromStream(jitter):
    """"
    [Ole32.dll] HRESULT OleLoadFromStream(LPSTREAM pStm, REFIID iidInterface, LPVOID* ppvObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStm", "iidInterface", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleLockRunning(jitter):
    """"
    [Ole32.dll] HRESULT OleLockRunning(LPUNKNOWN pUnknown, BOOL fLock, BOOL fLastUnlockCloses)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnknown", "fLock", "fLastUnlockCloses"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleMetafilePictFromIconAndLabel(jitter):
    """"
    [Ole32.dll] HGLOBAL OleMetafilePictFromIconAndLabel(HICON hIcon, LPOLESTR lpszLabel, LPOLESTR lpszSourceFile, UINT iIconIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIcon", "lpszLabel", "lpszSourceFile", "iIconIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleNoteObjectVisible(jitter):
    """"
    [Ole32.dll] HRESULT OleNoteObjectVisible(LPUNKNOWN pUnknown, BOOL fVisible)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnknown", "fVisible"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleQueryCreateFromData(jitter):
    """"
    [Ole32.dll] HRESULT OleQueryCreateFromData(LPDATAOBJECT pSrcDataObject)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleQueryLinkFromData(jitter):
    """"
    [Ole32.dll] HRESULT OleQueryLinkFromData(LPDATAOBJECT pSrcDataObject)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleRegEnumFormatEtc(jitter):
    """"
    [Ole32.dll] HRESULT OleRegEnumFormatEtc(REFCLSID clsid, DWORD dwDirection, LPENUMFORMATETC* ppenum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clsid", "dwDirection", "ppenum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleRegEnumVerbs(jitter):
    """"
    [Ole32.dll] HRESULT OleRegEnumVerbs(REFCLSID clsid, LPENUMOLEVERB* ppenum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["clsid", "ppenum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleRun(jitter):
    """"
    [Ole32.dll] HRESULT OleRun(LPUNKNOWN pUnknown)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnknown"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleSave(jitter):
    """"
    [Ole32.dll] HRESULT OleSave(LPPERSISTSTORAGE pPS, LPSTORAGE pStg, BOOL fSameAsLoad)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPS", "pStg", "fSameAsLoad"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleSaveToStream(jitter):
    """"
    [Ole32.dll] HRESULT OleSaveToStream(LPPERSISTSTREAM pPStm, LPSTREAM pStm)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPStm", "pStm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleSetClipboard(jitter):
    """"
    [Ole32.dll] HRESULT OleSetClipboard(LPDATAOBJECT pDataObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pDataObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleSetContainedObject(jitter):
    """"
    [Ole32.dll] HRESULT OleSetContainedObject(LPUNKNOWN pUnknown, BOOL fContained)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnknown", "fContained"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleSetMenuDescriptor(jitter):
    """"
    [Ole32.dll] HRESULT OleSetMenuDescriptor(HOLEMENU holemenu, HWND hwndFrame, HWND hwndActiveObject, LPOLEINPLACEFRAME lpFrame, LPOLEINPLACEACTIVEOBJECT lpActiveObj)
    """"
    ret_ad, args = jitter.func_args_stdcall(["holemenu", "hwndFrame", "hwndActiveObject", "lpFrame", "lpActiveObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleTranslateAccelerator(jitter):
    """"
    [Ole32.dll] HRESULT OleTranslateAccelerator(LPOLEINPLACEFRAME lpFrame, LPOLEINPLACEFRAMEINFO lpFrameInfo, LPMSG lpmsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFrame", "lpFrameInfo", "lpmsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleUninitialize(jitter):
    """"
    [Ole32.dll] void OleUninitialize()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_RegisterDragDrop(jitter):
    """"
    [Ole32.dll] HRESULT RegisterDragDrop(HWND hwnd, LPDROPTARGET pDropTarget)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pDropTarget"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_ReleaseStgMedium(jitter):
    """"
    [Ole32.dll] void ReleaseStgMedium(LPSTGMEDIUM pMedium)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pMedium"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_RevokeDragDrop(jitter):
    """"
    [Ole32.dll] HRESULT RevokeDragDrop(HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateILockBytesOnHGlobal(jitter):
    """"
    [Ole32.dll] WINOLEAPI CreateILockBytesOnHGlobal(HGLOBAL hGlobal, BOOL fDeleteOnRelease, ILockBytes** ppLkbyt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hGlobal", "fDeleteOnRelease", "ppLkbyt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateStreamOnHGlobal(jitter):
    """"
    [Ole32.dll] WINOLEAPI CreateStreamOnHGlobal(HGLOBAL hGlobal, BOOL fDeleteOnRelease, LPSTREAM* ppstm)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hGlobal", "fDeleteOnRelease", "ppstm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_FmtIdToPropStgName(jitter):
    """"
    [Ole32.dll] HRESULT FmtIdToPropStgName(const FMTID* pfmtid, LPOLESTR oszName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfmtid", "oszName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_FreePropVariantArray(jitter):
    """"
    [Ole32.dll] WINOLEAPI FreePropVariantArray(ULONG cVariants, PROPVARIANT* rgvars)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cVariants", "rgvars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_GetConvertStg(jitter):
    """"
    [Ole32.dll] WINOLEAPI GetConvertStg(IStorage* pStg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_GetHGlobalFromILockBytes(jitter):
    """"
    [Ole32.dll] WINOLEAPI GetHGlobalFromILockBytes(ILockBytes* pLkbyt, HGLOBAL* phglobal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pLkbyt", "phglobal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_GetHGlobalFromStream(jitter):
    """"
    [Ole32.dll] WINOLEAPI GetHGlobalFromStream(IStream* pstm, HGLOBAL* phglobal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pstm", "phglobal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleConvertIStorageToOLESTREAM(jitter):
    """"
    [Ole32.dll] WINOLEAPI OleConvertIStorageToOLESTREAM(IStorage* pStg, LPOLESTREAM lpolestream)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStg", "lpolestream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleConvertIStorageToOLESTREAMEx(jitter):
    """"
    [Ole32.dll] WINOLEAPI OleConvertIStorageToOLESTREAMEx(IStorage* pStg, CLIPFORMAT cfFormat, LONG lWidth, LONG lHeight, DWORD dwSize, LPSTGMEDIUM pmedium, LPOLESTREAM lpolestm)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStg", "cfFormat", "lWidth", "lHeight", "dwSize", "pmedium", "lpolestm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleConvertOLESTREAMToIStorage(jitter):
    """"
    [Ole32.dll] WINOLEAPI OleConvertOLESTREAMToIStorage(LPOLESTREAM lpolestream, IStorage* pstg, const DVTARGETDEVICE* ptd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpolestream", "pstg", "ptd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleConvertOLESTREAMToIStorageEx(jitter):
    """"
    [Ole32.dll] WINOLEAPI OleConvertOLESTREAMToIStorageEx(LPOLESTREAM lpolestm, IStorage* pstg, CLIPFORMAT* pcfFormat, LONG* plWidth, LONG* plHeight, DWORD* pdwSize, LPSTGMEDIUM pmedium)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpolestm", "pstg", "pcfFormat", "plWidth", "plHeight", "pdwSize", "pmedium"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_PropStgNameToFmtId(jitter):
    """"
    [Ole32.dll] HRESULT PropStgNameToFmtId(const LPOLESTR oszName, FMTID* pfmtid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["oszName", "pfmtid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_PropVariantClear(jitter):
    """"
    [Ole32.dll] WINOLEAPI PropVariantClear(PROPVARIANT* pvar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_PropVariantCopy(jitter):
    """"
    [Ole32.dll] WINOLEAPI PropVariantCopy(PROPVARIANT* pvarDest, const PROPVARIANT* pvarSrc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvarDest", "pvarSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_ReadClassStg(jitter):
    """"
    [Ole32.dll] WINOLEAPI ReadClassStg(IStorage* pStg, CLSID* pclsid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStg", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_ReadClassStm(jitter):
    """"
    [Ole32.dll] WINOLEAPI ReadClassStm(IStream* pStm, CLSID* pclsid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStm", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_ReadFmtUserTypeStg(jitter):
    """"
    [Ole32.dll] WINOLEAPI ReadFmtUserTypeStg(IStorage* pStg, CLIPFORMAT* pcf, LPWSTR* lplpszUserType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStg", "pcf", "lplpszUserType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgConvertPropertyToVariant(jitter):
    """"
    [Ole32.dll] BOOLEAN StgConvertPropertyToVariant(SERIALIZEDPROPERTYVALUE* prop, USHORT CodePage, PROPVARIANT* pvar, IMemoryAllocator* pma)
    """"
    ret_ad, args = jitter.func_args_stdcall(["prop", "CodePage", "pvar", "pma"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_SetConvertStg(jitter):
    """"
    [Ole32.dll] WINOLEAPI SetConvertStg(IStorage* pStg, BOOL fConvert)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStg", "fConvert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgConvertVariantToProperty(jitter):
    """"
    [Ole32.dll] SERIALIZEDPROPERTYVALUE* StgConvertVariantToProperty(PROPVARIANT* pvar, USHORT CodePage, SERIALIZEDPROPERTYVALUE* pprop, ULONG* pcb, PROPID pid, BOOLEAN fReserved, ULONG* pcIndirect)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvar", "CodePage", "pprop", "pcb", "pid", "fReserved", "pcIndirect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgCreateDocfile(jitter):
    """"
    [Ole32.dll] HRESULT StgCreateDocfile(const WCHAR* pwcsName, [STGM_FLAGS] grfMode, DWORD reserved, IStorage** ppstgOpen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwcsName", "grfMode", "reserved", "ppstgOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgCreateDocfileOnILockBytes(jitter):
    """"
    [Ole32.dll] WINOLEAPI StgCreateDocfileOnILockBytes(ILockBytes* plkbyt, [STGM_FLAGS] grfMode, DWORD reserved, IStorage** ppstgOpen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plkbyt", "grfMode", "reserved", "ppstgOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgCreatePropSetStg(jitter):
    """"
    [Ole32.dll] HRESULT StgCreatePropSetStg(IStorage* pStorage, DWORD dwReserved, IPropertySetStorage** ppPropSetStg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStorage", "dwReserved", "ppPropSetStg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgCreatePropStg(jitter):
    """"
    [Ole32.dll] HRESULT StgCreatePropStg(IUnknown* pUnk, REFFMTID fmtid, const CLSID* pclsid, [PROPSETFLAG] grfFlags, DWORD dwReserved, IPropertyStorage** ppPropStg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "fmtid", "pclsid", "grfFlags", "dwReserved", "ppPropStg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgCreateStorageEx(jitter):
    """"
    [Ole32.dll] WINOLEAPI StgCreateStorageEx(const WCHAR* pwcsName, [STGM_FLAGS] grfMode, STGFMT stgfmt, DWORD grfAttrs, STGOPTIONS* pStgOptions, PSECURITY_DESCRIPTOR* pSecurityDescriptor, REFIID riid, void** ppObjectOpen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwcsName", "grfMode", "stgfmt", "grfAttrs", "pStgOptions", "pSecurityDescriptor", "riid", "ppObjectOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgGetIFillLockBytesOnFile(jitter):
    """"
    [Ole32.dll] WINOLEAPI StgGetIFillLockBytesOnFile(OLECHAR* pwcsName, IFillLockBytes** ppflb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwcsName", "ppflb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgGetIFillLockBytesOnILockBytes(jitter):
    """"
    [Ole32.dll] WINOLEAPI StgGetIFillLockBytesOnILockBytes(ILockBytes* pilb, IFillLockBytes** ppflb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pilb", "ppflb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgIsStorageFile(jitter):
    """"
    [Ole32.dll] WINOLEAPI StgIsStorageFile(const WCHAR* pwcsName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwcsName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgIsStorageILockBytes(jitter):
    """"
    [Ole32.dll] WINOLEAPI StgIsStorageILockBytes(ILockBytes* plkbyt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plkbyt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgOpenAsyncDocfileOnIFillLockBytes(jitter):
    """"
    [Ole32.dll] WINOLEAPI StgOpenAsyncDocfileOnIFillLockBytes(IFillLockBytes* ppflb, [STGM_FLAGS] grfmode, [ASYNC_MODE_FLAGS] asyncFlags, IStorage** ppstgOpen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ppflb", "grfmode", "asyncFlags", "ppstgOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgOpenPropStg(jitter):
    """"
    [Ole32.dll] HRESULT StgOpenPropStg(IUnknown* pUnk, REFFMTID fmtid, [PROPSETFLAG] grfFlags, DWORD dwReserved, IPropertyStorage** ppPropStg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "fmtid", "grfFlags", "dwReserved", "ppPropStg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgOpenStorage(jitter):
    """"
    [Ole32.dll] HRESULT StgOpenStorage(const WCHAR* pwcsName, IStorage* pstgPriority, [STGM_FLAGS] grfMode, SNB snbExclude, DWORD reserved, IStorage** ppstgOpen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwcsName", "pstgPriority", "grfMode", "snbExclude", "reserved", "ppstgOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgOpenStorageEx(jitter):
    """"
    [Ole32.dll] HRESULT StgOpenStorageEx(const WCHAR* pwcsName, [STGM_FLAGS] grfMode, STGFMT stgfmt, DWORD grfAttrs, STGOPTIONS* pStgOptions, void* reserved2, REFIID riid, void** ppObjectOpen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwcsName", "grfMode", "stgfmt", "grfAttrs", "pStgOptions", "reserved2", "riid", "ppObjectOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgOpenStorageOnILockBytes(jitter):
    """"
    [Ole32.dll] WINOLEAPI StgOpenStorageOnILockBytes(ILockBytes* plkbyt, IStorage* pStgPriority, [STGM_FLAGS] grfMode, SNB snbExclude, DWORD reserved, IStorage** ppstgOpen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plkbyt", "pStgPriority", "grfMode", "snbExclude", "reserved", "ppstgOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgPropertyLengthAsVariant(jitter):
    """"
    [Ole32.dll] ULONG StgPropertyLengthAsVariant(SERIALIZEDPROPERTYVALUE* pProp, ULONG cbProp, USHORT CodePage, BYTE bReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pProp", "cbProp", "CodePage", "bReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgSetTimes(jitter):
    """"
    [Ole32.dll] WINOLEAPI StgSetTimes(WCHAR const* lpszName, FILETIME const* pctime, FILETIME const* patime, FILETIME const* pmtime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszName", "pctime", "patime", "pmtime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_WriteClassStg(jitter):
    """"
    [Ole32.dll] WINOLEAPI WriteClassStg(IStorage* pStg, REFCLSID rclsid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStg", "rclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_WriteClassStm(jitter):
    """"
    [Ole32.dll] WINOLEAPI WriteClassStm(IStream* pStm, REFCLSID rclsid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStm", "rclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_WriteFmtUserTypeStg(jitter):
    """"
    [Ole32.dll] WINOLEAPI WriteFmtUserTypeStg(IStorage* pStg, CLIPFORMAT cf, LPWSTR* lpszUserType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pStg", "cf", "lpszUserType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetModuleType(jitter):
    """"
    [Ole32.dll] HRESULT CoGetModuleType(LPCWSTR pwszFile, int* pModuleType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszFile", "pModuleType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
