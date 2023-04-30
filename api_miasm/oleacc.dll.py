
def oleacc_AccessibleChildren(jitter):
    """"
    [Oleacc.dll] STDAPI AccessibleChildren(IAccessible* paccContainer, LONG iChildStart, LONG cChildren, VARIANT* rgvarChildren, LONG* pcObtained)
    """"
    ret_ad, args = jitter.func_args_stdcall(["paccContainer", "iChildStart", "cChildren", "rgvarChildren", "pcObtained"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_AccessibleObjectFromEvent(jitter):
    """"
    [Oleacc.dll] STDAPI AccessibleObjectFromEvent(HWND hwnd, DWORD dwObjectID, DWORD dwChildID, IAccessible** ppacc, VARIANT* pvarChild)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwObjectID", "dwChildID", "ppacc", "pvarChild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_AccessibleObjectFromPoint(jitter):
    """"
    [Oleacc.dll] STDAPI AccessibleObjectFromPoint(POINT ptScreen, IAccessible** ppacc, VARIANT* pvarChild)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ptScreen", "ppacc", "pvarChild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_AccessibleObjectFromWindow(jitter):
    """"
    [Oleacc.dll] STDAPI AccessibleObjectFromWindow(HWND hwnd, DWORD dwObjectID, REFIID riid, void** ppvObject)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwObjectID", "riid", "ppvObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_GetOleaccVersionInfo(jitter):
    """"
    [Oleacc.dll] void GetOleaccVersionInfo(DWORD* pdwVer, DWORD* pdwBuild)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pdwVer", "pdwBuild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_GetProcessHandleFromHwnd(jitter):
    """"
    [Oleacc.dll] HANDLE GetProcessHandleFromHwnd(HWND hwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_GetRoleText(jitter):
    """"
    [Oleacc.dll] UINT GetRoleText(DWORD dwRole, LPTSTR lpszRole, UINT cchRoleMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwRole", "lpszRole", "cchRoleMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_GetStateText(jitter):
    """"
    [Oleacc.dll] UINT GetStateText(DWORD dwStateBit, LPTSTR lpszStateBit, UINT cchStateBitMax)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwStateBit", "lpszStateBit", "cchStateBitMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_WindowFromAccessibleObject(jitter):
    """"
    [Oleacc.dll] STDAPI WindowFromAccessibleObject(IAccessible* pacc, HWND* phwnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pacc", "phwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_CreateStdAccessibleObject(jitter):
    """"
    [Oleacc.dll] STDAPI CreateStdAccessibleObject(HWND hwnd, LONG idObject, REFIID riidInterface, void** ppvObject)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "idObject", "riidInterface", "ppvObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_CreateStdAccessibleProxy(jitter):
    """"
    [Oleacc.dll] STDAPI CreateStdAccessibleProxy(HWND hwnd, LPCTSTR pszClassName, LONG idObject, REFIID riidInterface, void** ppvObject)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszClassName", "idObject", "riidInterface", "ppvObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_LresultFromObject(jitter):
    """"
    [Oleacc.dll] LRESULT LresultFromObject(REFIID riid, WPARAM wParam, LPUNKNOWN pAcc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["riid", "wParam", "pAcc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_ObjectFromLresult(jitter):
    """"
    [Oleacc.dll] STDAPI ObjectFromLresult(LRESULT lResult, REFIID riid, WPARAM wParam, void** ppvObject)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lResult", "riid", "wParam", "ppvObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_AccSetRunningUtilityState(jitter):
    """"
    [Oleacc.dll] STDAPI AccSetRunningUtilityState(HWND hwndApp, DWORD dwUtilityStateMask, DWORD dwUtilityState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndApp", "dwUtilityStateMask", "dwUtilityState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
