
def *_DllMain(jitter):
    """
    [*] BOOL DllMain(HINSTANCE hinstDLL, [DLLMAIN_REASON] fdwReason, LPVOID lpvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hinstDLL", "fdwReason", "lpvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllGetClassObject(jitter):
    """
    [*] HRESULT DllGetClassObject(REFCLSID rclsid, REFIID riid, LPVOID* ppv)
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllCanUnloadNow(jitter):
    """
    [*] HRESULT DllCanUnloadNow()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllRegisterServer(jitter):
    """
    [*] HRESULT DllRegisterServer()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllUnregisterServer(jitter):
    """
    [*] HRESULT DllUnregisterServer()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllDebugObjectRPCHook(jitter):
    """
    [*] BOOL DllDebugObjectRPCHook(BOOL fTrace, LPORPC_INIT_ARGS lpOrpcInitArgs)
    """
    ret_ad, args = jitter.func_args_stdcall(["fTrace", "lpOrpcInitArgs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_CPlApplet(jitter):
    """
    [*] LONG CPlApplet(HWND hwndCPl, [CPL_MSG] uMsg, LPARAM lParam1, LPARAM lParam2)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndCPl", "uMsg", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllGetVersion(jitter):
    """
    [*] HRESULT DllGetVersion(DLLVERSIONINFO* pdvi)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdvi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllInstall(jitter):
    """
    [*] HRESULT DllInstall(BOOL bInstall, PCWSTR pszCmdLine)
    """
    ret_ad, args = jitter.func_args_stdcall(["bInstall", "pszCmdLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllGetActivationFactory(jitter):
    """
    [*] HRESULT DllGetActivationFactory(HSTRING activatableClassId, IActivationFactory** factory)
    """
    ret_ad, args = jitter.func_args_stdcall(["activatableClassId", "factory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *__CorDllMain(jitter):
    """
    [*] BOOL _CorDllMain(HINSTANCE hInst, DWORD dwReason, LPVOID lpReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["hInst", "dwReason", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *__CorExeMain(jitter):
    """
    [*] __int32 _CorExeMain()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *__CorExeMain2(jitter):
    """
    [*] __int32 _CorExeMain2(PBYTE pUnmappedPE, DWORD cUnmappedPE, LPWSTR pImageNameIn, LPWSTR pLoadersFileName, LPWSTR pCmdLine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnmappedPE", "cUnmappedPE", "pImageNameIn", "pLoadersFileName", "pCmdLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *__CorImageUnloading(jitter):
    """
    [*] STDAPI_(VOID) _CorImageUnloading(PVOID* ImageBase)
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *__CorValidateImage(jitter):
    """
    [*] STDAPI _CorValidateImage(PVOID* ImageBase, LPCWSTR FileName)
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageBase", "FileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
