###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def oleacc_AccessibleChildren(jitter):
    """
    STDAPI AccessibleChildren(
        IAccessible* paccContainer,
        LONG iChildStart,
        LONG cChildren,
        VARIANT* rgvarChildren,
        LONG* pcObtained
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["paccContainer", "iChildStart", "cChildren", "rgvarChildren", "pcObtained"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_AccessibleObjectFromEvent(jitter):
    """
    STDAPI AccessibleObjectFromEvent(
        HWND hwnd,
        DWORD dwObjectID,
        DWORD dwChildID,
        IAccessible** ppacc,
        VARIANT* pvarChild
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwObjectID", "dwChildID", "ppacc", "pvarChild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_AccessibleObjectFromPoint(jitter):
    """
    STDAPI AccessibleObjectFromPoint(
        POINT ptScreen,
        IAccessible** ppacc,
        VARIANT* pvarChild
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ptScreen", "ppacc", "pvarChild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_AccessibleObjectFromWindow(jitter):
    """
    STDAPI AccessibleObjectFromWindow(
        HWND hwnd,
        DWORD dwObjectID,
        REFIID riid,
        void** ppvObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwObjectID", "riid", "ppvObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_GetOleaccVersionInfo(jitter):
    """
    void GetOleaccVersionInfo(
        DWORD* pdwVer,
        DWORD* pdwBuild
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwVer", "pdwBuild"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_GetProcessHandleFromHwnd(jitter):
    """
    HANDLE GetProcessHandleFromHwnd(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_GetRoleText(jitter, get_str, set_str):
    """
    UINT GetRoleText(
        DWORD dwRole,
        LPTSTR lpszRole,
        UINT cchRoleMax
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwRole", "lpszRole", "cchRoleMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_GetRoleTextA(jitter):
    oleacc_GetRoleText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oleacc_GetRoleTextW(jitter):
    oleacc_GetRoleText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oleacc_GetStateText(jitter, get_str, set_str):
    """
    UINT GetStateText(
        DWORD dwStateBit,
        LPTSTR lpszStateBit,
        UINT cchStateBitMax
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwStateBit", "lpszStateBit", "cchStateBitMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_GetStateTextA(jitter):
    oleacc_GetStateText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def oleacc_GetStateTextW(jitter):
    oleacc_GetStateText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def oleacc_WindowFromAccessibleObject(jitter):
    """
    STDAPI WindowFromAccessibleObject(
        IAccessible* pacc,
        HWND* phwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pacc", "phwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_CreateStdAccessibleObject(jitter):
    """
    STDAPI CreateStdAccessibleObject(
        HWND hwnd,
        LONG idObject,
        REFIID riidInterface,
        void** ppvObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "idObject", "riidInterface", "ppvObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_CreateStdAccessibleProxy(jitter):
    """
    STDAPI CreateStdAccessibleProxy(
        HWND hwnd,
        LPCTSTR pszClassName,
        LONG idObject,
        REFIID riidInterface,
        void** ppvObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pszClassName", "idObject", "riidInterface", "ppvObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_LresultFromObject(jitter):
    """
    LRESULT LresultFromObject(
        REFIID riid,
        WPARAM wParam,
        LPUNKNOWN pAcc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "wParam", "pAcc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_ObjectFromLresult(jitter):
    """
    STDAPI ObjectFromLresult(
        LRESULT lResult,
        REFIID riid,
        WPARAM wParam,
        void** ppvObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lResult", "riid", "wParam", "ppvObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleacc_AccSetRunningUtilityState(jitter):
    """
    STDAPI AccSetRunningUtilityState(
        HWND hwndApp,
        DWORD dwUtilityStateMask,
        DWORD dwUtilityState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndApp", "dwUtilityStateMask", "dwUtilityState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
