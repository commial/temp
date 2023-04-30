
def msrating_RatingAccessDeniedDialog(jitter, get_str, set_str):
    """"
    [msrating.dll] HRESULT RatingAccessDeniedDialog(HWND hDlg, LPCTSTR pszUsername, LPCTSTR pszContentDescription, VOID* pRatingDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "pszUsername", "pszContentDescription", "pRatingDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msrating_RatingAccessDeniedDialogA(jitter):
    msrating_RatingAccessDeniedDialog(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msrating_RatingAccessDeniedDialogW(jitter):
    msrating_RatingAccessDeniedDialog(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msrating_RatingAccessDeniedDialog2(jitter, get_str, set_str):
    """"
    [msrating.dll] HRESULT RatingAccessDeniedDialog2(HWND hDlg, LPCSTR pszUsername, VOID* pRatingDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "pszUsername", "pRatingDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msrating_RatingAccessDeniedDialog2A(jitter):
    msrating_RatingAccessDeniedDialog2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msrating_RatingAccessDeniedDialog2W(jitter):
    msrating_RatingAccessDeniedDialog2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msrating_RatingCheckUserAccess(jitter, get_str, set_str):
    """"
    [msrating.dll] HRESULT RatingCheckUserAccess(LPCTSTR pszUsername, LPCTSTR pszURL, LPCTSTR pszRatingInfo, LPBYTE pData, DWORD cbData, VOID** ppRatingDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszUsername", "pszURL", "pszRatingInfo", "pData", "cbData", "ppRatingDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msrating_RatingCheckUserAccessA(jitter):
    msrating_RatingCheckUserAccess(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msrating_RatingCheckUserAccessW(jitter):
    msrating_RatingCheckUserAccess(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msrating_RatingEnable(jitter, get_str, set_str):
    """"
    [msrating.dll] HRESULT RatingEnable(HWND hwndParent, LPCSTR pszUsername, BOOL fEnable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "pszUsername", "fEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msrating_RatingEnableA(jitter):
    msrating_RatingEnable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msrating_RatingEnableW(jitter):
    msrating_RatingEnable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msrating_RatingEnabledQuery(jitter):
    """"
    [msrating.dll] HRESULT RatingEnabledQuery()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msrating_RatingFreeDetails(jitter):
    """"
    [msrating.dll] HRESULT RatingFreeDetails(VOID* pRatingDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRatingDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msrating_RatingObtainCancel(jitter):
    """"
    [msrating.dll] HRESULT RatingObtainCancel(HANDLE hRatingObtainQuery)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRatingObtainQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msrating_RatingObtainQuery(jitter, get_str, set_str):
    """"
    [msrating.dll] HRESULT RatingObtainQuery(LPCTSTR pszTargetUrl, DWORD dwUserData, DWORD dwUserData, HRESULT hr, LPCTSTR pszRating, HANDLE* phRatingObtainQuery)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszTargetUrl", "dwUserData", "dwUserData", "hr", "pszRating", "phRatingObtainQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msrating_RatingObtainQueryA(jitter):
    msrating_RatingObtainQuery(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msrating_RatingObtainQueryW(jitter):
    msrating_RatingObtainQuery(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msrating_RatingSetupUI(jitter, get_str, set_str):
    """"
    [msrating.dll] HRESULT RatingSetupUI(HWND hDlg, LPCSTR pszUsername)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "pszUsername"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msrating_RatingSetupUIA(jitter):
    msrating_RatingSetupUI(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msrating_RatingSetupUIW(jitter):
    msrating_RatingSetupUI(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
