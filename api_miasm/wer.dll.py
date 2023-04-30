
def wer_WerAddExcludedApplication(jitter):
    """
    [Wer.dll] HRESULT WerAddExcludedApplication(PCWSTR pwzExeName, BOOL bAllUsers)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzExeName", "bAllUsers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerRemoveExcludedApplication(jitter):
    """
    [Wer.dll] HRESULT WerRemoveExcludedApplication(PCWSTR pwzExeName, BOOL bAllUsers)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzExeName", "bAllUsers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportAddDump(jitter):
    """
    [Wer.dll] HRESULT WerReportAddDump(HREPORT hReportHandle, [ProcessHandle] hProcess, [ThreadHandle] hThread, WER_DUMP_TYPE dumpType, PWER_EXCEPTION_INFORMATION pExceptionParam, PWER_DUMP_CUSTOM_OPTIONS pDumpCustomOptions, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hReportHandle", "hProcess", "hThread", "dumpType", "pExceptionParam", "pDumpCustomOptions", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportAddFile(jitter):
    """
    [Wer.dll] HRESULT WerReportAddFile(HREPORT hReportHandle, PCWSTR pwzPath, WER_FILE_TYPE repFileType, DWORD dwFileFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hReportHandle", "pwzPath", "repFileType", "dwFileFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportCloseHandle(jitter):
    """
    [Wer.dll] HRESULT WerReportCloseHandle(HREPORT hReportHandle)
    """
    ret_ad, args = jitter.func_args_stdcall(["hReportHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportCreate(jitter):
    """
    [Wer.dll] HRESULT WerReportCreate(PCWSTR pwzEventType, WER_REPORT_TYPE repType, PWER_REPORT_INFORMATION pReportInformation, HREPORT* phReportHandle)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzEventType", "repType", "pReportInformation", "phReportHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportSetParameter(jitter):
    """
    [Wer.dll] HRESULT WerReportSetParameter(HREPORT hReportHandle, DWORD dwparamID, PCWSTR pwzName, PCWSTR pwzValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hReportHandle", "dwparamID", "pwzName", "pwzValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportSetUIOption(jitter):
    """
    [Wer.dll] HRESULT WerReportSetUIOption(HREPORT hReportHandle, WER_REPORT_UI repUITypeID, PCWSTR pwzValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hReportHandle", "repUITypeID", "pwzValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportSubmit(jitter):
    """
    [Wer.dll] HRESULT WerReportSubmit(HREPORT hReportHandle, WER_CONSENT consent, DWORD dwFlags, PWER_SUBMIT_RESULT pSubmitResult)
    """
    ret_ad, args = jitter.func_args_stdcall(["hReportHandle", "consent", "dwFlags", "pSubmitResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
