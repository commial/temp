
def msrating_RatingAccessDeniedDialog(jitter):
    """"
    [msrating.dll] HRESULT RatingAccessDeniedDialog(HWND hDlg, LPCTSTR pszUsername, LPCTSTR pszContentDescription, VOID* pRatingDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "pszUsername", "pszContentDescription", "pRatingDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msrating_RatingAccessDeniedDialog2(jitter):
    """"
    [msrating.dll] HRESULT RatingAccessDeniedDialog2(HWND hDlg, LPCSTR pszUsername, VOID* pRatingDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "pszUsername", "pRatingDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msrating_RatingCheckUserAccess(jitter):
    """"
    [msrating.dll] HRESULT RatingCheckUserAccess(LPCTSTR pszUsername, LPCTSTR pszURL, LPCTSTR pszRatingInfo, LPBYTE pData, DWORD cbData, VOID** ppRatingDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszUsername", "pszURL", "pszRatingInfo", "pData", "cbData", "ppRatingDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msrating_RatingEnable(jitter):
    """"
    [msrating.dll] HRESULT RatingEnable(HWND hwndParent, LPCSTR pszUsername, BOOL fEnable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "pszUsername", "fEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

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

def msrating_RatingObtainQuery(jitter):
    """"
    [msrating.dll] HRESULT RatingObtainQuery(LPCTSTR pszTargetUrl, DWORD dwUserData, DWORD dwUserData, HRESULT hr, LPCTSTR pszRating, HANDLE* phRatingObtainQuery)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszTargetUrl", "dwUserData", "dwUserData", "hr", "pszRating", "phRatingObtainQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msrating_RatingSetupUI(jitter):
    """"
    [msrating.dll] HRESULT RatingSetupUI(HWND hDlg, LPCSTR pszUsername)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDlg", "pszUsername"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
