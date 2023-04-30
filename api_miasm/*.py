_DLLMAIN_REASON_ = {
    "DLL_PROCESS_ATTACH": 1,
    "DLL_THREAD_ATTACH": 2,
    "DLL_THREAD_DETACH": 3,
    "DLL_PROCESS_DETACH": 0,
}
_DLLMAIN_REASON__INV = {
    1: "DLL_PROCESS_ATTACH",
    2: "DLL_THREAD_ATTACH",
    3: "DLL_THREAD_DETACH",
    0: "DLL_PROCESS_DETACH",
}
_DLLVER_PLATFORM_ = {
    "DLLVER_PLATFORM_WINDOWS": 0x00000001,
    "DLLVER_PLATFORM_NT": 0x00000002,
}
_DLLVER_PLATFORM__INV = {
    0x00000001: "DLLVER_PLATFORM_WINDOWS",
    0x00000002: "DLLVER_PLATFORM_NT",
}
_CPL_MSG_ = {
    "CPL_INIT": 1,
    "CPL_GETCOUNT": 2,
    "CPL_INQUIRE": 3,
    "CPL_SELECT": 4,
    "CPL_DBLCLK": 5,
    "CPL_STOP": 6,
    "CPL_EXIT": 7,
    "CPL_NEWINQUIRE": 8,
    "CPL_STARTWPARMSA": 9,
    "CPL_STARTWPARMSW": 10,
    "CPL_SETUP": 200,
}
_CPL_MSG__INV = {
    1: "CPL_INIT",
    2: "CPL_GETCOUNT",
    3: "CPL_INQUIRE",
    4: "CPL_SELECT",
    5: "CPL_DBLCLK",
    6: "CPL_STOP",
    7: "CPL_EXIT",
    8: "CPL_NEWINQUIRE",
    9: "CPL_STARTWPARMSA",
    10: "CPL_STARTWPARMSW",
    200: "CPL_SETUP",
}

def *_DllMain(jitter):
    """
    BOOL DllMain(
        HINSTANCE hinstDLL,
        [DLLMAIN_REASON] fdwReason,
        LPVOID lpvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hinstDLL", "fdwReason", "lpvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllGetClassObject(jitter):
    """
    HRESULT DllGetClassObject(
        REFCLSID rclsid,
        REFIID riid,
        LPVOID* ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllCanUnloadNow(jitter):
    """
    HRESULT DllCanUnloadNow()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllRegisterServer(jitter):
    """
    HRESULT DllRegisterServer()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllUnregisterServer(jitter):
    """
    HRESULT DllUnregisterServer()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllDebugObjectRPCHook(jitter):
    """
    BOOL DllDebugObjectRPCHook(
        BOOL fTrace,
        LPORPC_INIT_ARGS lpOrpcInitArgs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fTrace", "lpOrpcInitArgs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_CPlApplet(jitter):
    """
    LONG CPlApplet(
        HWND hwndCPl,
        [CPL_MSG] uMsg,
        LPARAM lParam1,
        LPARAM lParam2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndCPl", "uMsg", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllGetVersion(jitter):
    """
    HRESULT DllGetVersion(
        DLLVERSIONINFO* pdvi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdvi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllInstall(jitter):
    """
    HRESULT DllInstall(
        BOOL bInstall,
        PCWSTR pszCmdLine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bInstall", "pszCmdLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *_DllGetActivationFactory(jitter):
    """
    HRESULT DllGetActivationFactory(
        HSTRING activatableClassId,
        IActivationFactory** factory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["activatableClassId", "factory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *__CorDllMain(jitter):
    """
    BOOL _CorDllMain(
        HINSTANCE hInst,
        DWORD dwReason,
        LPVOID lpReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInst", "dwReason", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *__CorExeMain(jitter):
    """
    __int32 _CorExeMain()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *__CorExeMain2(jitter):
    """
    __int32 _CorExeMain2(
        PBYTE pUnmappedPE,
        DWORD cUnmappedPE,
        LPWSTR pImageNameIn,
        LPWSTR pLoadersFileName,
        LPWSTR pCmdLine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUnmappedPE", "cUnmappedPE", "pImageNameIn", "pLoadersFileName", "pCmdLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *__CorImageUnloading(jitter):
    """
    STDAPI_(VOID) _CorImageUnloading(
        PVOID* ImageBase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def *__CorValidateImage(jitter):
    """
    STDAPI _CorValidateImage(
        PVOID* ImageBase,
        LPCWSTR FileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageBase", "FileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
