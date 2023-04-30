STGFMT = {
    "STGFMT_STORAGE": 0,
    "STGFMT_NATIVE": 1,
    "STGFMT_FILE": 3,
    "STGFMT_ANY": 4,
    "STGFMT_DOCFILE": 5,
}
OLERENDER = {
    "OLERENDER_NONE": 0,
    "OLERENDER_DRAW": 1,
    "OLERENDER_FORMAT": 2,
    "OLERENDER_ASIS": 3,
}

def ole32_BindMoniker(jitter):
    """
    HRESULT BindMoniker(
        LPMONIKER pmk,
        DWORD grfOpt,
        REFIID iidResult,
        LPVOID* ppvResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pmk", "grfOpt", "iidResult", "ppvResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CLSIDFromProgID(jitter):
    """
    HRESULT CLSIDFromProgID(
        LPCOLESTR lpszProgID,
        LPCLSID lpclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszProgID", "lpclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CLSIDFromProgIDEx(jitter):
    """
    HRESULT CLSIDFromProgIDEx(
        LPCOLESTR lpszProgID,
        LPCLSID lpclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszProgID", "lpclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CLSIDFromString(jitter):
    """
    HRESULT CLSIDFromString(
        LPCOLESTR lpsz,
        LPCLSID pclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpsz", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoAddRefServerProcess(jitter):
    """
    ULONG CoAddRefServerProcess()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoAllowSetForegroundWindow(jitter):
    """
    HRESULT CoAllowSetForegroundWindow(
        IUnknown* pUnk,
        LPVOID lpvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "lpvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCancelCall(jitter):
    """
    HRESULT CoCancelCall(
        DWORD dwThreadId,
        ULONG ulTimeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwThreadId", "ulTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCopyProxy(jitter):
    """
    HRESULT CoCopyProxy(
        IUnknown* pProxy,
        IUnknown** ppCopy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxy", "ppCopy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCreateFreeThreadedMarshaler(jitter):
    """
    HRESULT CoCreateFreeThreadedMarshaler(
        LPUNKNOWN punkOuter,
        LPUNKNOWN* ppunkMarshal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punkOuter", "ppunkMarshal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCreateGuid(jitter):
    """
    HRESULT CoCreateGuid(
        GUID* pguid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pguid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCreateInstance(jitter):
    """
    HRESULT CoCreateInstance(
        REFCLSID rclsid,
        LPUNKNOWN pUnkOuter,
        [CLSCTX] dwClsContext,
        REFIID riid,
        LPVOID* ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "pUnkOuter", "dwClsContext", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCreateInstanceEx(jitter):
    """
    HRESULT CoCreateInstanceEx(
        REFCLSID rclsid,
        IUnknown* punkOuter,
        [CLSCTX] dwClsCtx,
        COSERVERINFO* pServerInfo,
        DWORD dwCount,
        MULTI_QI* pResults
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "punkOuter", "dwClsCtx", "pServerInfo", "dwCount", "pResults"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoDisableCallCancellation(jitter):
    """
    HRESULT CoDisableCallCancellation(
        LPVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoDisconnectContext(jitter):
    """
    HRESULT CoDisconnectContext(
        DWORD dwTimeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoDisconnectObject(jitter):
    """
    HRESULT CoDisconnectObject(
        LPUNKNOWN pUnk,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoDosDateTimeToFileTime(jitter):
    """
    BOOL CoDosDateTimeToFileTime(
        WORD nDosDate,
        WORD nDosTime,
        FILETIME* lpFileTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nDosDate", "nDosTime", "lpFileTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoEnableCallCancellation(jitter):
    """
    HRESULT CoEnableCallCancellation(
        LPVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoFileTimeNow(jitter):
    """
    HRESULT CoFileTimeNow(
        FILETIME* lpFileTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpFileTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoFileTimeToDosDateTime(jitter):
    """
    BOOL CoFileTimeToDosDateTime(
        FILETIME* lpFileTime,
        LPWORD lpDosDate,
        LPWORD lpDosTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpFileTime", "lpDosDate", "lpDosTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoFreeAllLibraries(jitter):
    """
    void CoFreeAllLibraries()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoFreeLibrary(jitter):
    """
    void CoFreeLibrary(
        HINSTANCE hInst
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoFreeUnusedLibraries(jitter):
    """
    void CoFreeUnusedLibraries()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoFreeUnusedLibrariesEx(jitter):
    """
    void CoFreeUnusedLibrariesEx(
        DWORD dwUnloadDelay,
        DWORD dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwUnloadDelay", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetApartmentType(jitter):
    """
    HRESULT CoGetApartmentType(
        APTTYPE* pAptType,
        APTTYPEQUALIFIER* pAptQualifier
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAptType", "pAptQualifier"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetCallContext(jitter):
    """
    HRESULT CoGetCallContext(
        REFIID riid,
        void** ppInterface
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "ppInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetCallerTID(jitter):
    """
    HRESULT CoGetCallerTID(
        LPDWORD lpdwTID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpdwTID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetCancelObject(jitter):
    """
    HRESULT CoGetCancelObject(
        DWORD dwThreadId,
        REFIID iid,
        void** ppUnk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwThreadId", "iid", "ppUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetClassObject(jitter):
    """
    HRESULT CoGetClassObject(
        REFCLSID rclsid,
        [CLSCTX] dwClsContext,
        COSERVERINFO* pServerInfo,
        REFIID riid,
        LPVOID* ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "dwClsContext", "pServerInfo", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetContextToken(jitter):
    """
    HRESULT CoGetContextToken(
        ULONG_PTR* pToken
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetCurrentLogicalThreadId(jitter):
    """
    HRESULT CoGetCurrentLogicalThreadId(
        GUID* pguid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pguid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetCurrentProcess(jitter):
    """
    DWORD CoGetCurrentProcess()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetInstanceFromFile(jitter):
    """
    HRESULT CoGetInstanceFromFile(
        COSERVERINFO* pServerInfo,
        CLSID* pClsid,
        IUnknown* punkOuter,
        [CLSCTX] dwClsCtx,
        [STGM_FLAGS] grfMode,
        OLECHAR* pwszName,
        DWORD dwCount,
        MULTI_QI* pResults
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pServerInfo", "pClsid", "punkOuter", "dwClsCtx", "grfMode", "pwszName", "dwCount", "pResults"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetInstanceFromIStorage(jitter):
    """
    HRESULT CoGetInstanceFromIStorage(
        COSERVERINFO* pServerInfo,
        CLSID* pClsid,
        IUnknown* punkOuter,
        [CLSCTX] dwClsCtx,
        struct IStorage* pstg,
        DWORD dwCount,
        MULTI_QI* pResults
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pServerInfo", "pClsid", "punkOuter", "dwClsCtx", "pstg", "dwCount", "pResults"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetInterceptor(jitter):
    """
    HRESULT CoGetInterceptor(
        REFIID iidIntercepted,
        IUnknown* punkOuter,
        REFIID iid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["iidIntercepted", "punkOuter", "iid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetInterfaceAndReleaseStream(jitter):
    """
    HRESULT CoGetInterfaceAndReleaseStream(
        LPSTREAM pStm,
        REFIID iid,
        LPVOID* ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStm", "iid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetMalloc(jitter):
    """
    HRESULT CoGetMalloc(
        DWORD dwMemContext,
        LPMALLOC* ppMalloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwMemContext", "ppMalloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetMarshalSizeMax(jitter):
    """
    HRESULT CoGetMarshalSizeMax(
        ULONG* pulSize,
        REFIID riid,
        LPUNKNOWN pUnk,
        DWORD dwDestContext,
        LPVOID pvDestContext,
        MSHLFLAGS mshlflags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pulSize", "riid", "pUnk", "dwDestContext", "pvDestContext", "mshlflags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetObject(jitter):
    """
    HRESULT CoGetObject(
        LPCWSTR pszName,
        BIND_OPTS* pBindOptions,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszName", "pBindOptions", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetObjectContext(jitter):
    """
    HRESULT CoGetObjectContext(
        REFIID riid,
        LPVOID* ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetPSClsid(jitter):
    """
    HRESULT CoGetPSClsid(
        REFIID riid,
        CLSID* pClsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "pClsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetStandardMarshal(jitter):
    """
    HRESULT CoGetStandardMarshal(
        REFIID riid,
        LPUNKNOWN pUnk,
        DWORD dwDestContext,
        LPVOID pvDestContext,
        MSHLFLAGS mshlflags,
        LPMARSHAL* ppMarshal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "pUnk", "dwDestContext", "pvDestContext", "mshlflags", "ppMarshal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetStdMarshalEx(jitter):
    """
    HRESULT CoGetStdMarshalEx(
        LPUNKNOWN pUnkOuter,
        DWORD smexflags,
        LPUNKNOWN* ppUnkInner
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnkOuter", "smexflags", "ppUnkInner"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetTreatAsClass(jitter):
    """
    HRESULT CoGetTreatAsClass(
        REFCLSID clsidOld,
        LPCLSID pClsidNew
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsidOld", "pClsidNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoImpersonateClient(jitter):
    """
    HRESULT CoImpersonateClient()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoInitialize(jitter):
    """
    HRESULT CoInitialize(
        LPVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoInitializeEx(jitter):
    """
    HRESULT CoInitializeEx(
        LPVOID pvReserved,
        [COINIT_FLAG] dwCoInit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvReserved", "dwCoInit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoInitializeSecurity(jitter):
    """
    HRESULT CoInitializeSecurity(
        PSECURITY_DESCRIPTOR pSecDesc,
        LONG cAuthSvc,
        SOLE_AUTHENTICATION_SERVICE* asAuthSvc,
        void* pReserved1,
        [RPC_C_AUTHN_LEVEL] dwAuthnLevel,
        [RPC_C_IMP_LEVEL] dwImpLevel,
        void* pAuthList,
        EOLE_AUTHENTICATION_CAPABILITIES dwCapabilities,
        void* pReserved3
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSecDesc", "cAuthSvc", "asAuthSvc", "pReserved1", "dwAuthnLevel", "dwImpLevel", "pAuthList", "dwCapabilities", "pReserved3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoInstall(jitter):
    """
    HRESULT CoInstall(
        IBindCtx* pbc,
        DWORD dwFlags,
        uCLSSPEC* pClassSpec,
        QUERYCONTEXT* pQuery,
        LPWSTR pszCodeBase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbc", "dwFlags", "pClassSpec", "pQuery", "pszCodeBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoInvalidateRemoteMachineBindings(jitter):
    """
    HRESULT CoInvalidateRemoteMachineBindings(
        LPOLESTR pszMachineName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszMachineName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoIsHandlerConnected(jitter):
    """
    BOOL CoIsHandlerConnected(
        LPUNKNOWN pUnk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoIsOle1Class(jitter):
    """
    BOOL CoIsOle1Class(
        REFCLSID rclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoLoadLibrary(jitter):
    """
    HINSTANCE CoLoadLibrary(
        LPOLESTR lpszLibName,
        BOOL bAutoFree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszLibName", "bAutoFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoLockObjectExternal(jitter):
    """
    HRESULT CoLockObjectExternal(
        LPUNKNOWN pUnk,
        BOOL fLock,
        BOOL fLastUnlockReleases
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "fLock", "fLastUnlockReleases"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoMarshalHresult(jitter):
    """
    HRESULT CoMarshalHresult(
        LPSTREAM pstm,
        HRESULT hresult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "hresult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoMarshalInterface(jitter):
    """
    HRESULT CoMarshalInterface(
        LPSTREAM pStm,
        REFIID riid,
        LPUNKNOWN pUnk,
        DWORD dwDestContext,
        LPVOID pvDestContext,
        MSHLFLAGS mshlflags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStm", "riid", "pUnk", "dwDestContext", "pvDestContext", "mshlflags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoMarshalInterThreadInterfaceInStream(jitter):
    """
    HRESULT CoMarshalInterThreadInterfaceInStream(
        REFIID riid,
        LPUNKNOWN pUnk,
        LPSTREAM* ppStm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "pUnk", "ppStm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoQueryAuthenticationServices(jitter):
    """
    HRESULT CoQueryAuthenticationServices(
        DWORD* pcAuthSvc,
        SOLE_AUTHENTICATION_SERVICE** asAuthSvc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcAuthSvc", "asAuthSvc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoQueryClientBlanket(jitter):
    """
    HRESULT CoQueryClientBlanket(
        DWORD* pAuthnSvc,
        DWORD* pAuthzSvc,
        OLECHAR** pServerPrincName,
        DWORD* pAuthnLevel,
        DWORD* pImpLevel,
        RPC_AUTHZ_HANDLE* pPrivs,
        DWORD* pCapabilities
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAuthnSvc", "pAuthzSvc", "pServerPrincName", "pAuthnLevel", "pImpLevel", "pPrivs", "pCapabilities"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoQueryProxyBlanket(jitter):
    """
    HRESULT CoQueryProxyBlanket(
        IUnknown* pProxy,
        DWORD* pwAuthnSvc,
        DWORD* pAuthzSvc,
        OLECHAR** pServerPrincName,
        DWORD* pAuthnLevel,
        DWORD* pImpLevel,
        RPC_AUTH_IDENTITY_HANDLE* pAuthInfo,
        DWORD* pCapabilites
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxy", "pwAuthnSvc", "pAuthzSvc", "pServerPrincName", "pAuthnLevel", "pImpLevel", "pAuthInfo", "pCapabilites"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterClassObject(jitter):
    """
    HRESULT CoRegisterClassObject(
        REFCLSID rclsid,
        LPUNKNOWN pUnk,
        [CLSCTX] dwClsContext,
        REGCLS flags,
        LPDWORD lpdwRegister
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "pUnk", "dwClsContext", "flags", "lpdwRegister"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterInitializeSpy(jitter):
    """
    HRESULT CoRegisterInitializeSpy(
        LPINITIALIZESPY pSpy,
        ULARGE_INTEGER* puliCookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSpy", "puliCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterMallocSpy(jitter):
    """
    HRESULT CoRegisterMallocSpy(
        LPMALLOCSPY pMallocSpy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMallocSpy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterMessageFilter(jitter):
    """
    HRESULT CoRegisterMessageFilter(
        LPMESSAGEFILTER lpMessageFilter,
        LPMESSAGEFILTER* lplpMessageFilter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpMessageFilter", "lplpMessageFilter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterPSClsid(jitter):
    """
    HRESULT CoRegisterPSClsid(
        REFIID riid,
        REFCLSID rclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "rclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterSurrogate(jitter):
    """
    HRESULT CoRegisterSurrogate(
        LPSURROGATE pSurrogate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSurrogate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoReleaseMarshalData(jitter):
    """
    HRESULT CoReleaseMarshalData(
        LPSTREAM pStm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoReleaseServerProcess(jitter):
    """
    ULONG CoReleaseServerProcess()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoResumeClassObjects(jitter):
    """
    HRESULT CoResumeClassObjects()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRevertToSelf(jitter):
    """
    HRESULT CoRevertToSelf()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRevokeClassObject(jitter):
    """
    HRESULT CoRevokeClassObject(
        DWORD dwRegister
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwRegister"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRevokeInitializeSpy(jitter):
    """
    HRESULT CoRevokeInitializeSpy(
        ULARGE_INTEGER uliCookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uliCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRevokeMallocSpy(jitter):
    """
    HRESULT CoRevokeMallocSpy()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoSetCancelObject(jitter):
    """
    HRESULT CoSetCancelObject(
        IUnknown* pUnk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoSetProxyBlanket(jitter):
    """
    HRESULT CoSetProxyBlanket(
        IUnknown* pProxy,
        [RPC_C_AUTHN_SVC] dwAuthnSvc,
        [RPC_C_AUTHZ] dwAuthzSvc,
        OLECHAR* pServerPrincName,
        [RPC_C_AUTHN_LEVEL] dwAuthnLevel,
        [RPC_C_IMP_LEVEL] dwImpLevel,
        RPC_AUTH_IDENTITY_HANDLE pAuthInfo,
        EOLE_AUTHENTICATION_CAPABILITIES dwCapabilities
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxy", "dwAuthnSvc", "dwAuthzSvc", "pServerPrincName", "dwAuthnLevel", "dwImpLevel", "pAuthInfo", "dwCapabilities"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoSuspendClassObjects(jitter):
    """
    HRESULT CoSuspendClassObjects()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoSwitchCallContext(jitter):
    """
    HRESULT CoSwitchCallContext(
        IUnknown* pNewObject,
        IUnknown** ppOldObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pNewObject", "ppOldObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoTaskMemAlloc(jitter):
    """
    LPVOID CoTaskMemAlloc(
        SIZE_T cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoTaskMemFree(jitter):
    """
    void CoTaskMemFree(
        LPVOID pv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoTaskMemRealloc(jitter):
    """
    LPVOID CoTaskMemRealloc(
        LPVOID pv,
        SIZE_T cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pv", "cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoTestCancel(jitter):
    """
    HRESULT CoTestCancel()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoTreatAsClass(jitter):
    """
    HRESULT CoTreatAsClass(
        REFCLSID clsidOld,
        REFCLSID clsidNew
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsidOld", "clsidNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoUninitialize(jitter):
    """
    void CoUninitialize()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoUnmarshalHresult(jitter):
    """
    HRESULT CoUnmarshalHresult(
        LPSTREAM pstm,
        HRESULT* phresult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "phresult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoUnmarshalInterface(jitter):
    """
    HRESULT CoUnmarshalInterface(
        LPSTREAM pStm,
        REFIID riid,
        LPVOID* ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStm", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoWaitForMultipleHandles(jitter):
    """
    HRESULT CoWaitForMultipleHandles(
        DWORD dwFlags,
        DWORD dwTimeout,
        ULONG cHandles,
        LPHANDLE pHandles,
        LPDWORD lpdwindex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "dwTimeout", "cHandles", "pHandles", "lpdwindex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateAntiMoniker(jitter):
    """
    HRESULT CreateAntiMoniker(
        LPMONIKER* ppmk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateBindCtx(jitter):
    """
    HRESULT CreateBindCtx(
        DWORD reserved,
        LPBC* ppbc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["reserved", "ppbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateClassMoniker(jitter):
    """
    HRESULT CreateClassMoniker(
        REFCLSID rclsid,
        LPMONIKER* ppmk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateFileMoniker(jitter):
    """
    HRESULT CreateFileMoniker(
        LPCOLESTR lpszPathName,
        LPMONIKER* ppmk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPathName", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateGenericComposite(jitter):
    """
    HRESULT CreateGenericComposite(
        LPMONIKER pmkFirst,
        LPMONIKER pmkRest,
        LPMONIKER* ppmkComposite
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pmkFirst", "pmkRest", "ppmkComposite"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateItemMoniker(jitter):
    """
    HRESULT CreateItemMoniker(
        LPCOLESTR lpszDelim,
        LPCOLESTR lpszItem,
        LPMONIKER* ppmk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDelim", "lpszItem", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateObjrefMoniker(jitter):
    """
    HRESULT CreateObjrefMoniker(
        LPUNKNOWN punk,
        LPMONIKER* ppmk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreatePointerMoniker(jitter):
    """
    HRESULT CreatePointerMoniker(
        LPUNKNOWN punk,
        LPMONIKER* ppmk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_GetClassFile(jitter):
    """
    HRESULT GetClassFile(
        LPCOLESTR szFilename,
        CLSID* pclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szFilename", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_GetRunningObjectTable(jitter):
    """
    HRESULT GetRunningObjectTable(
        DWORD reserved,
        LPRUNNINGOBJECTTABLE* pprot
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["reserved", "pprot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_IIDFromString(jitter):
    """
    HRESULT IIDFromString(
        LPCOLESTR lpsz,
        LPIID lpiid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpsz", "lpiid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_IsAccelerator(jitter):
    """
    BOOL IsAccelerator(
        HACCEL hAccel,
        int cAccelEntries,
        LPMSG lpMsg,
        WORD* lpwCmd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAccel", "cAccelEntries", "lpMsg", "lpwCmd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_IsEqualGUID(jitter):
    """
    BOOL IsEqualGUID(
        REFGUID rguid1,
        REFGUID rguid2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rguid1", "rguid2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_MkParseDisplayName(jitter):
    """
    HRESULT MkParseDisplayName(
        LPBC pbc,
        LPCOLESTR szUserName,
        ULONG* pchEaten,
        LPMONIKER* ppmk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbc", "szUserName", "pchEaten", "ppmk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_MonikerCommonPrefixWith(jitter):
    """
    HRESULT MonikerCommonPrefixWith(
        LPMONIKER pmkThis,
        LPMONIKER pmkOther,
        LPMONIKER* ppmkCommon
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pmkThis", "pmkOther", "ppmkCommon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_MonikerRelativePathTo(jitter):
    """
    HRESULT MonikerRelativePathTo(
        LPMONIKER pmkSrc,
        LPMONIKER pmkDest,
        LPMONIKER* ppmkRelPath,
        BOOL dwReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pmkSrc", "pmkDest", "ppmkRelPath", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleDoAutoConvert(jitter):
    """
    HRESULT OleDoAutoConvert(
        LPSTORAGE pStg,
        LPCLSID pClsidNew
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStg", "pClsidNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleGetAutoConvert(jitter):
    """
    HRESULT OleGetAutoConvert(
        REFCLSID clsidOld,
        LPCLSID pClsidNew
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsidOld", "pClsidNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleGetIconOfClass(jitter):
    """
    HGLOBAL OleGetIconOfClass(
        REFCLSID rclsid,
        LPOLESTR lpszLabel,
        BOOL fUseTypeAsLabel
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "lpszLabel", "fUseTypeAsLabel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleGetIconOfFile(jitter):
    """
    HGLOBAL OleGetIconOfFile(
        LPOLESTR lpszPath,
        BOOL fUseFileAsLabel
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPath", "fUseFileAsLabel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleRegGetMiscStatus(jitter):
    """
    HRESULT OleRegGetMiscStatus(
        REFCLSID clsid,
        DVASPECT dwAspect,
        DWORD* pdwStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsid", "dwAspect", "pdwStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleRegGetUserType(jitter):
    """
    HRESULT OleRegGetUserType(
        REFCLSID clsid,
        DWORD dwFormOfType,
        LPOLESTR* pszUserType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsid", "dwFormOfType", "pszUserType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleSetAutoConvert(jitter):
    """
    HRESULT OleSetAutoConvert(
        REFCLSID clsidOld,
        REFCLSID clsidNew
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsidOld", "clsidNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_ProgIDFromCLSID(jitter):
    """
    HRESULT ProgIDFromCLSID(
        REFCLSID clsid,
        LPOLESTR* lplpszProgID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsid", "lplpszProgID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StringFromCLSID(jitter):
    """
    HRESULT StringFromCLSID(
        REFCLSID rclsid,
        LPOLESTR* lplpsz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "lplpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StringFromGUID2(jitter):
    """
    int StringFromGUID2(
        REFGUID rguid,
        LPOLESTR lpsz,
        int cchMax
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rguid", "lpsz", "cchMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StringFromIID(jitter):
    """
    HRESULT StringFromIID(
        REFIID rclsid,
        LPOLESTR* lplpsz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "lplpsz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoRegisterChannelHook(jitter):
    """
    HRESULT CoRegisterChannelHook(
        REFGUID ExtensionUuid,
        IChannelHook* pChannelHook
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExtensionUuid", "pChannelHook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoCreateInstanceFromApp(jitter):
    """
    HRESULT CoCreateInstanceFromApp(
        REFCLSID rclsid,
        IUnknown* punkOuter,
        DWORD dwClsCtx,
        PVOID reserved,
        DWORD dwCount,
        MULTI_QI* pResults
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "punkOuter", "dwClsCtx", "reserved", "dwCount", "pResults"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoDecrementMTAUsage(jitter):
    """
    HRESULT CoDecrementMTAUsage(
        CO_MTA_USAGE_COOKIE Cookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoHandlePriorityEventsFromMessagePump(jitter):
    """
    void CoHandlePriorityEventsFromMessagePump()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoIncrementMTAUsage(jitter):
    """
    HRESULT CoIncrementMTAUsage(
        CO_MTA_USAGE_COOKIE* pCookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoSetMessageDispatcher(jitter):
    """
    HRESULT CoSetMessageDispatcher(
        PMessageDispatcher pMessageDispatcher
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMessageDispatcher"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateDataAdviseHolder(jitter):
    """
    HRESULT CreateDataAdviseHolder(
        LPDATAADVISEHOLDER* ppDAHolder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppDAHolder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateDataCache(jitter):
    """
    HRESULT CreateDataCache(
        LPUNKNOWN pUnkOuter,
        REFCLSID rclsid,
        REFIID iid,
        LPVOID* ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnkOuter", "rclsid", "iid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateOleAdviseHolder(jitter):
    """
    HRESULT CreateOleAdviseHolder(
        LPOLEADVISEHOLDER* ppOAHolder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppOAHolder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_DoDragDrop(jitter):
    """
    HRESULT DoDragDrop(
        LPDATAOBJECT pDataObj,
        LPDROPSOURCE pDropSource,
        DWORD dwOKEffects,
        LPDWORD pdwEffect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDataObj", "pDropSource", "dwOKEffects", "pdwEffect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreate(jitter):
    """
    HRESULT OleCreate(
        REFCLSID rclsid,
        REFIID riid,
        OLERENDER renderopt,
        LPFORMATETC pFormatEtc,
        LPOLECLIENTSITE pClientSite,
        LPSTORAGE pStg,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "riid", "renderopt", "pFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateDefaultHandler(jitter):
    """
    HRESULT OleCreateDefaultHandler(
        REFCLSID clsid,
        LPUNKNOWN pUnkOuter,
        REFIID riid,
        LPVOID* lplpObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsid", "pUnkOuter", "riid", "lplpObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateEmbeddingHelper(jitter):
    """
    HRESULT OleCreateEmbeddingHelper(
        REFCLSID clsid,
        LPUNKNOWN pUnkOuter,
        DWORD flags,
        LPCLASSFACTORY pCF,
        REFIID riid,
        LPVOID* lplpObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsid", "pUnkOuter", "flags", "pCF", "riid", "lplpObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateEx(jitter):
    """
    HRESULT OleCreateEx(
        REFCLSID rclsid,
        REFIID riid,
        DWORD dwFlags,
        OLERENDER renderopt,
        ULONG cFormats,
        DWORD* rgAdvf,
        LPFORMATETC rgFormatEtc,
        IAdviseSink* lpAdviseSink,
        DWORD* rgdwConnection,
        LPOLECLIENTSITE pClientSite,
        LPSTORAGE pStg,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "riid", "dwFlags", "renderopt", "cFormats", "rgAdvf", "rgFormatEtc", "lpAdviseSink", "rgdwConnection", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateFromData(jitter):
    """
    HRESULT OleCreateFromData(
        LPDATAOBJECT pSrcDataObj,
        REFIID riid,
        OLERENDER renderopt,
        LPFORMATETC pFormatEtc,
        LPOLECLIENTSITE pClientSite,
        LPSTORAGE pStg,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObj", "riid", "renderopt", "pFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateFromDataEx(jitter):
    """
    HRESULT OleCreateFromDataEx(
        LPDATAOBJECT pSrcDataObj,
        REFIID riid,
        DWORD dwFlags,
        OLERENDER renderopt,
        ULONG cFormats,
        DWORD* rgAdvf,
        LPFORMATETC rgFormatEtc,
        IAdviseSink* lpAdviseSink,
        DWORD* rgdwConnection,
        LPOLECLIENTSITE pClientSite,
        LPSTORAGE pStg,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObj", "riid", "dwFlags", "renderopt", "cFormats", "rgAdvf", "rgFormatEtc", "lpAdviseSink", "rgdwConnection", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateFromFile(jitter):
    """
    HRESULT OleCreateFromFile(
        REFCLSID rclsid,
        LPCOLESTR lpszFileName,
        REFIID riid,
        OLERENDER renderopt,
        LPFORMATETC lpFormatEtc,
        LPOLECLIENTSITE pClientSite,
        LPSTORAGE pStg,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "lpszFileName", "riid", "renderopt", "lpFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateFromFileEx(jitter):
    """
    HRESULT OleCreateFromFileEx(
        REFCLSID rclsid,
        LPCOLESTR lpszFileName,
        REFIID riid,
        DWORD dwFlags,
        OLERENDER renderopt,
        ULONG cFormats,
        DWORD* rgAdvf,
        LPFORMATETC rgFormatEtc,
        IAdviseSink* lpAdviseSink,
        DWORD* rgdwConnection,
        LPOLECLIENTSITE pClientSite,
        LPSTORAGE pStg,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "lpszFileName", "riid", "dwFlags", "renderopt", "cFormats", "rgAdvf", "rgFormatEtc", "lpAdviseSink", "rgdwConnection", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateLink(jitter):
    """
    HRESULT OleCreateLink(
        LPMONIKER pmkLinkSrc,
        REFIID riid,
        OLERENDER renderopt,
        LPFORMATETC lpFormatEtc,
        LPOLECLIENTSITE pClientSite,
        LPSTORAGE pStg,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pmkLinkSrc", "riid", "renderopt", "lpFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateLinkEx(jitter):
    """
    HRESULT OleCreateLinkEx(
        LPMONIKER pmkLinkSrc,
        REFIID riid,
        DWORD dwFlags,
        OLERENDER renderopt,
        ULONG cFormats,
        DWORD* rgAdvf,
        LPFORMATETC rgFormatEtc,
        IAdviseSink* lpAdviseSink,
        DWORD* rgdwConnection,
        LPOLECLIENTSITE pClientSite,
        LPSTORAGE pStg,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pmkLinkSrc", "riid", "dwFlags", "renderopt", "cFormats", "rgAdvf", "rgFormatEtc", "lpAdviseSink", "rgdwConnection", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateLinkFromData(jitter):
    """
    HRESULT OleCreateLinkFromData(
        LPDATAOBJECT pSrcDataObj,
        REFIID riid,
        OLERENDER renderopt,
        LPFORMATETC pFormatEtc,
        LPOLECLIENTSITE pClientSite,
        LPSTORAGE pStg,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObj", "riid", "renderopt", "pFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateLinkFromDataEx(jitter):
    """
    HRESULT OleCreateLinkFromDataEx(
        LPDATAOBJECT pSrcDataObj,
        REFIID riid,
        DWORD dwFlags,
        OLERENDER renderopt,
        ULONG cFormats,
        DWORD* rgAdvf,
        LPFORMATETC rgFormatEtc,
        IAdviseSink* lpAdviseSink,
        DWORD* rgdwConnection,
        LPOLECLIENTSITE pClientSite,
        LPSTORAGE pStg,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObj", "riid", "dwFlags", "renderopt", "cFormats", "rgAdvf", "rgFormatEtc", "lpAdviseSink", "rgdwConnection", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateLinkToFile(jitter):
    """
    HRESULT OleCreateLinkToFile(
        LPCOLESTR lpszFileName,
        REFIID riid,
        OLERENDER renderopt,
        LPFORMATETC lpFormatEtc,
        LPOLECLIENTSITE pClientSite,
        LPSTORAGE pStg,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFileName", "riid", "renderopt", "lpFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateLinkToFileEx(jitter):
    """
    HRESULT OleCreateLinkToFileEx(
        LPCOLESTR lpszFileName,
        REFIID riid,
        DWORD dwFlags,
        OLERENDER renderopt,
        ULONG cFormats,
        DWORD* rgAdvf,
        LPFORMATETC rgFormatEtc,
        IAdviseSink* lpAdviseSink,
        DWORD* rgdwConnection,
        LPOLECLIENTSITE pClientSite,
        LPSTORAGE pStg,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFileName", "riid", "dwFlags", "renderopt", "cFormats", "rgAdvf", "rgFormatEtc", "lpAdviseSink", "rgdwConnection", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateMenuDescriptor(jitter):
    """
    HOLEMENU OleCreateMenuDescriptor(
        HMENU hmenuCombined,
        LPOLEMENUGROUPWIDTHS lpMenuWidths
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmenuCombined", "lpMenuWidths"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleCreateStaticFromData(jitter):
    """
    HRESULT OleCreateStaticFromData(
        LPDATAOBJECT pSrcDataObj,
        REFIID iid,
        OLERENDER renderopt,
        LPFORMATETC pFormatEtc,
        LPOLECLIENTSITE pClientSite,
        LPSTORAGE pStg,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObj", "iid", "renderopt", "pFormatEtc", "pClientSite", "pStg", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleDestroyMenuDescriptor(jitter):
    """
    VOID OleDestroyMenuDescriptor(
        HOLEMENU holemenu
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["holemenu"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleDraw(jitter):
    """
    HRESULT OleDraw(
        LPUNKNOWN pUnknown,
        DVASPECT dwAspect,
        HDC hdcDraw,
        LPCRECT lprcBounds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnknown", "dwAspect", "hdcDraw", "lprcBounds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleDuplicateData(jitter):
    """
    HANDLE OleDuplicateData(
        HANDLE hSrc,
        CLIPFORMAT cfFormat,
        UINT uiFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSrc", "cfFormat", "uiFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleFlushClipboard(jitter):
    """
    HRESULT OleFlushClipboard()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleGetClipboard(jitter):
    """
    HRESULT OleGetClipboard(
        LPDATAOBJECT* ppDataObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppDataObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleInitialize(jitter):
    """
    HRESULT OleInitialize(
        LPVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleIsCurrentClipboard(jitter):
    """
    HRESULT OleIsCurrentClipboard(
        LPDATAOBJECT pDataObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDataObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleIsRunning(jitter):
    """
    BOOL OleIsRunning(
        LPOLEOBJECT pObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleLoad(jitter):
    """
    HRESULT OleLoad(
        LPSTORAGE pStg,
        REFIID riid,
        REFCLSID rclsid,
        LPOLECLIENTSITE pClientSite,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStg", "riid", "rclsid", "pClientSite", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleLoadFromStream(jitter):
    """
    HRESULT OleLoadFromStream(
        LPSTREAM pStm,
        REFIID iidInterface,
        LPVOID* ppvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStm", "iidInterface", "ppvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleLockRunning(jitter):
    """
    HRESULT OleLockRunning(
        LPUNKNOWN pUnknown,
        BOOL fLock,
        BOOL fLastUnlockCloses
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnknown", "fLock", "fLastUnlockCloses"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleMetafilePictFromIconAndLabel(jitter):
    """
    HGLOBAL OleMetafilePictFromIconAndLabel(
        HICON hIcon,
        LPOLESTR lpszLabel,
        LPOLESTR lpszSourceFile,
        UINT iIconIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hIcon", "lpszLabel", "lpszSourceFile", "iIconIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleNoteObjectVisible(jitter):
    """
    HRESULT OleNoteObjectVisible(
        LPUNKNOWN pUnknown,
        BOOL fVisible
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnknown", "fVisible"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleQueryCreateFromData(jitter):
    """
    HRESULT OleQueryCreateFromData(
        LPDATAOBJECT pSrcDataObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleQueryLinkFromData(jitter):
    """
    HRESULT OleQueryLinkFromData(
        LPDATAOBJECT pSrcDataObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSrcDataObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleRegEnumFormatEtc(jitter):
    """
    HRESULT OleRegEnumFormatEtc(
        REFCLSID clsid,
        DWORD dwDirection,
        LPENUMFORMATETC* ppenum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsid", "dwDirection", "ppenum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleRegEnumVerbs(jitter):
    """
    HRESULT OleRegEnumVerbs(
        REFCLSID clsid,
        LPENUMOLEVERB* ppenum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsid", "ppenum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleRun(jitter):
    """
    HRESULT OleRun(
        LPUNKNOWN pUnknown
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnknown"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleSave(jitter):
    """
    HRESULT OleSave(
        LPPERSISTSTORAGE pPS,
        LPSTORAGE pStg,
        BOOL fSameAsLoad
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPS", "pStg", "fSameAsLoad"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleSaveToStream(jitter):
    """
    HRESULT OleSaveToStream(
        LPPERSISTSTREAM pPStm,
        LPSTREAM pStm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPStm", "pStm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleSetClipboard(jitter):
    """
    HRESULT OleSetClipboard(
        LPDATAOBJECT pDataObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDataObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleSetContainedObject(jitter):
    """
    HRESULT OleSetContainedObject(
        LPUNKNOWN pUnknown,
        BOOL fContained
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnknown", "fContained"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleSetMenuDescriptor(jitter):
    """
    HRESULT OleSetMenuDescriptor(
        HOLEMENU holemenu,
        HWND hwndFrame,
        HWND hwndActiveObject,
        LPOLEINPLACEFRAME lpFrame,
        LPOLEINPLACEACTIVEOBJECT lpActiveObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["holemenu", "hwndFrame", "hwndActiveObject", "lpFrame", "lpActiveObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleTranslateAccelerator(jitter):
    """
    HRESULT OleTranslateAccelerator(
        LPOLEINPLACEFRAME lpFrame,
        LPOLEINPLACEFRAMEINFO lpFrameInfo,
        LPMSG lpmsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpFrame", "lpFrameInfo", "lpmsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleUninitialize(jitter):
    """
    void OleUninitialize()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_RegisterDragDrop(jitter):
    """
    HRESULT RegisterDragDrop(
        HWND hwnd,
        LPDROPTARGET pDropTarget
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pDropTarget"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_ReleaseStgMedium(jitter):
    """
    void ReleaseStgMedium(
        LPSTGMEDIUM pMedium
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMedium"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_RevokeDragDrop(jitter):
    """
    HRESULT RevokeDragDrop(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateILockBytesOnHGlobal(jitter):
    """
    WINOLEAPI CreateILockBytesOnHGlobal(
        HGLOBAL hGlobal,
        BOOL fDeleteOnRelease,
        ILockBytes** ppLkbyt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hGlobal", "fDeleteOnRelease", "ppLkbyt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CreateStreamOnHGlobal(jitter):
    """
    WINOLEAPI CreateStreamOnHGlobal(
        HGLOBAL hGlobal,
        BOOL fDeleteOnRelease,
        LPSTREAM* ppstm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hGlobal", "fDeleteOnRelease", "ppstm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_FmtIdToPropStgName(jitter):
    """
    HRESULT FmtIdToPropStgName(
        const FMTID* pfmtid,
        LPOLESTR oszName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfmtid", "oszName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_FreePropVariantArray(jitter):
    """
    WINOLEAPI FreePropVariantArray(
        ULONG cVariants,
        PROPVARIANT* rgvars
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cVariants", "rgvars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_GetConvertStg(jitter):
    """
    WINOLEAPI GetConvertStg(
        IStorage* pStg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_GetHGlobalFromILockBytes(jitter):
    """
    WINOLEAPI GetHGlobalFromILockBytes(
        ILockBytes* pLkbyt,
        HGLOBAL* phglobal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pLkbyt", "phglobal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_GetHGlobalFromStream(jitter):
    """
    WINOLEAPI GetHGlobalFromStream(
        IStream* pstm,
        HGLOBAL* phglobal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm", "phglobal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleConvertIStorageToOLESTREAM(jitter):
    """
    WINOLEAPI OleConvertIStorageToOLESTREAM(
        IStorage* pStg,
        LPOLESTREAM lpolestream
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStg", "lpolestream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleConvertIStorageToOLESTREAMEx(jitter):
    """
    WINOLEAPI OleConvertIStorageToOLESTREAMEx(
        IStorage* pStg,
        CLIPFORMAT cfFormat,
        LONG lWidth,
        LONG lHeight,
        DWORD dwSize,
        LPSTGMEDIUM pmedium,
        LPOLESTREAM lpolestm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStg", "cfFormat", "lWidth", "lHeight", "dwSize", "pmedium", "lpolestm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleConvertOLESTREAMToIStorage(jitter):
    """
    WINOLEAPI OleConvertOLESTREAMToIStorage(
        LPOLESTREAM lpolestream,
        IStorage* pstg,
        const DVTARGETDEVICE* ptd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpolestream", "pstg", "ptd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_OleConvertOLESTREAMToIStorageEx(jitter):
    """
    WINOLEAPI OleConvertOLESTREAMToIStorageEx(
        LPOLESTREAM lpolestm,
        IStorage* pstg,
        CLIPFORMAT* pcfFormat,
        LONG* plWidth,
        LONG* plHeight,
        DWORD* pdwSize,
        LPSTGMEDIUM pmedium
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpolestm", "pstg", "pcfFormat", "plWidth", "plHeight", "pdwSize", "pmedium"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_PropStgNameToFmtId(jitter):
    """
    HRESULT PropStgNameToFmtId(
        const LPOLESTR oszName,
        FMTID* pfmtid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["oszName", "pfmtid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_PropVariantClear(jitter):
    """
    WINOLEAPI PropVariantClear(
        PROPVARIANT* pvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_PropVariantCopy(jitter):
    """
    WINOLEAPI PropVariantCopy(
        PROPVARIANT* pvarDest,
        const PROPVARIANT* pvarSrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarDest", "pvarSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_ReadClassStg(jitter):
    """
    WINOLEAPI ReadClassStg(
        IStorage* pStg,
        CLSID* pclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStg", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_ReadClassStm(jitter):
    """
    WINOLEAPI ReadClassStm(
        IStream* pStm,
        CLSID* pclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStm", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_ReadFmtUserTypeStg(jitter):
    """
    WINOLEAPI ReadFmtUserTypeStg(
        IStorage* pStg,
        CLIPFORMAT* pcf,
        LPWSTR* lplpszUserType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStg", "pcf", "lplpszUserType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgConvertPropertyToVariant(jitter):
    """
    BOOLEAN StgConvertPropertyToVariant(
        SERIALIZEDPROPERTYVALUE* prop,
        USHORT CodePage,
        PROPVARIANT* pvar,
        IMemoryAllocator* pma
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["prop", "CodePage", "pvar", "pma"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_SetConvertStg(jitter):
    """
    WINOLEAPI SetConvertStg(
        IStorage* pStg,
        BOOL fConvert
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStg", "fConvert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgConvertVariantToProperty(jitter):
    """
    SERIALIZEDPROPERTYVALUE* StgConvertVariantToProperty(
        PROPVARIANT* pvar,
        USHORT CodePage,
        SERIALIZEDPROPERTYVALUE* pprop,
        ULONG* pcb,
        PROPID pid,
        BOOLEAN fReserved,
        ULONG* pcIndirect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvar", "CodePage", "pprop", "pcb", "pid", "fReserved", "pcIndirect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgCreateDocfile(jitter):
    """
    HRESULT StgCreateDocfile(
        const WCHAR* pwcsName,
        [STGM_FLAGS] grfMode,
        DWORD reserved,
        IStorage** ppstgOpen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwcsName", "grfMode", "reserved", "ppstgOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgCreateDocfileOnILockBytes(jitter):
    """
    WINOLEAPI StgCreateDocfileOnILockBytes(
        ILockBytes* plkbyt,
        [STGM_FLAGS] grfMode,
        DWORD reserved,
        IStorage** ppstgOpen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plkbyt", "grfMode", "reserved", "ppstgOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgCreatePropSetStg(jitter):
    """
    HRESULT StgCreatePropSetStg(
        IStorage* pStorage,
        DWORD dwReserved,
        IPropertySetStorage** ppPropSetStg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStorage", "dwReserved", "ppPropSetStg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgCreatePropStg(jitter):
    """
    HRESULT StgCreatePropStg(
        IUnknown* pUnk,
        REFFMTID fmtid,
        const CLSID* pclsid,
        [PROPSETFLAG] grfFlags,
        DWORD dwReserved,
        IPropertyStorage** ppPropStg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "fmtid", "pclsid", "grfFlags", "dwReserved", "ppPropStg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgCreateStorageEx(jitter):
    """
    WINOLEAPI StgCreateStorageEx(
        const WCHAR* pwcsName,
        [STGM_FLAGS] grfMode,
        STGFMT stgfmt,
        DWORD grfAttrs,
        STGOPTIONS* pStgOptions,
        PSECURITY_DESCRIPTOR* pSecurityDescriptor,
        REFIID riid,
        void** ppObjectOpen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwcsName", "grfMode", "stgfmt", "grfAttrs", "pStgOptions", "pSecurityDescriptor", "riid", "ppObjectOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgGetIFillLockBytesOnFile(jitter):
    """
    WINOLEAPI StgGetIFillLockBytesOnFile(
        OLECHAR* pwcsName,
        IFillLockBytes** ppflb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwcsName", "ppflb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgGetIFillLockBytesOnILockBytes(jitter):
    """
    WINOLEAPI StgGetIFillLockBytesOnILockBytes(
        ILockBytes* pilb,
        IFillLockBytes** ppflb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pilb", "ppflb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgIsStorageFile(jitter):
    """
    WINOLEAPI StgIsStorageFile(
        const WCHAR* pwcsName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwcsName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgIsStorageILockBytes(jitter):
    """
    WINOLEAPI StgIsStorageILockBytes(
        ILockBytes* plkbyt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plkbyt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgOpenAsyncDocfileOnIFillLockBytes(jitter):
    """
    WINOLEAPI StgOpenAsyncDocfileOnIFillLockBytes(
        IFillLockBytes* ppflb,
        [STGM_FLAGS] grfmode,
        [ASYNC_MODE_FLAGS] asyncFlags,
        IStorage** ppstgOpen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppflb", "grfmode", "asyncFlags", "ppstgOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgOpenPropStg(jitter):
    """
    HRESULT StgOpenPropStg(
        IUnknown* pUnk,
        REFFMTID fmtid,
        [PROPSETFLAG] grfFlags,
        DWORD dwReserved,
        IPropertyStorage** ppPropStg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnk", "fmtid", "grfFlags", "dwReserved", "ppPropStg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgOpenStorage(jitter):
    """
    HRESULT StgOpenStorage(
        const WCHAR* pwcsName,
        IStorage* pstgPriority,
        [STGM_FLAGS] grfMode,
        SNB snbExclude,
        DWORD reserved,
        IStorage** ppstgOpen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwcsName", "pstgPriority", "grfMode", "snbExclude", "reserved", "ppstgOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgOpenStorageEx(jitter):
    """
    HRESULT StgOpenStorageEx(
        const WCHAR* pwcsName,
        [STGM_FLAGS] grfMode,
        STGFMT stgfmt,
        DWORD grfAttrs,
        STGOPTIONS* pStgOptions,
        void* reserved2,
        REFIID riid,
        void** ppObjectOpen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwcsName", "grfMode", "stgfmt", "grfAttrs", "pStgOptions", "reserved2", "riid", "ppObjectOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgOpenStorageOnILockBytes(jitter):
    """
    WINOLEAPI StgOpenStorageOnILockBytes(
        ILockBytes* plkbyt,
        IStorage* pStgPriority,
        [STGM_FLAGS] grfMode,
        SNB snbExclude,
        DWORD reserved,
        IStorage** ppstgOpen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plkbyt", "pStgPriority", "grfMode", "snbExclude", "reserved", "ppstgOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgPropertyLengthAsVariant(jitter):
    """
    ULONG StgPropertyLengthAsVariant(
        SERIALIZEDPROPERTYVALUE* pProp,
        ULONG cbProp,
        USHORT CodePage,
        BYTE bReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProp", "cbProp", "CodePage", "bReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_StgSetTimes(jitter):
    """
    WINOLEAPI StgSetTimes(
        WCHAR const* lpszName,
        FILETIME const* pctime,
        FILETIME const* patime,
        FILETIME const* pmtime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszName", "pctime", "patime", "pmtime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_WriteClassStg(jitter):
    """
    WINOLEAPI WriteClassStg(
        IStorage* pStg,
        REFCLSID rclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStg", "rclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_WriteClassStm(jitter):
    """
    WINOLEAPI WriteClassStm(
        IStream* pStm,
        REFCLSID rclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStm", "rclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_WriteFmtUserTypeStg(jitter):
    """
    WINOLEAPI WriteFmtUserTypeStg(
        IStorage* pStg,
        CLIPFORMAT cf,
        LPWSTR* lpszUserType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStg", "cf", "lpszUserType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ole32_CoGetModuleType(jitter):
    """
    HRESULT CoGetModuleType(
        LPCWSTR pwszFile,
        int* pModuleType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszFile", "pModuleType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
