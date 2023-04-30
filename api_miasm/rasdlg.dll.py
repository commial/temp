
def rasdlg_RasDialDlg(jitter):
    """"
    [Rasdlg.dll] BOOL RasDialDlg(LPTSTR lpszPhonebook, LPTSTR lpszEntry, LPTSTR lpszPhoneNumber, LPRASDIALDLG lpInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpszPhoneNumber", "lpInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasdlg_RasEntryDlg(jitter):
    """"
    [Rasdlg.dll] BOOL RasEntryDlg(LPTSTR lpszPhonebook, LPTSTR lpszEntry, LPRASENTRYDLG lpInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasdlg_RasMonitorDlg(jitter):
    """"
    [Rasdlg.dll] BOOL RasMonitorDlg(LPTSTR lpszDeviceName, LPRASMONITORDLG lpInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDeviceName", "lpInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rasdlg_RasPhonebookDlg(jitter):
    """"
    [Rasdlg.dll] BOOL RasPhonebookDlg(LPTSTR lpszPhonebook, LPTSTR lpszEntry, LPRASPBDLG lpInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszPhonebook", "lpszEntry", "lpInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
