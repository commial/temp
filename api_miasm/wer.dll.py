
def wer_WerAddExcludedApplication(jitter):
    """
    HRESULT WerAddExcludedApplication(
        PCWSTR pwzExeName,
        BOOL bAllUsers
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzExeName", "bAllUsers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerRemoveExcludedApplication(jitter):
    """
    HRESULT WerRemoveExcludedApplication(
        PCWSTR pwzExeName,
        BOOL bAllUsers
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzExeName", "bAllUsers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportAddDump(jitter):
    """
    HRESULT WerReportAddDump(
        HREPORT hReportHandle,
        [ProcessHandle] hProcess,
        [ThreadHandle] hThread,
        WER_DUMP_TYPE dumpType,
        PWER_EXCEPTION_INFORMATION pExceptionParam,
        PWER_DUMP_CUSTOM_OPTIONS pDumpCustomOptions,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hReportHandle", "hProcess", "hThread", "dumpType", "pExceptionParam", "pDumpCustomOptions", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportAddFile(jitter):
    """
    HRESULT WerReportAddFile(
        HREPORT hReportHandle,
        PCWSTR pwzPath,
        WER_FILE_TYPE repFileType,
        DWORD dwFileFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hReportHandle", "pwzPath", "repFileType", "dwFileFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportCloseHandle(jitter):
    """
    HRESULT WerReportCloseHandle(
        HREPORT hReportHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hReportHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportCreate(jitter):
    """
    HRESULT WerReportCreate(
        PCWSTR pwzEventType,
        WER_REPORT_TYPE repType,
        PWER_REPORT_INFORMATION pReportInformation,
        HREPORT* phReportHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzEventType", "repType", "pReportInformation", "phReportHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportSetParameter(jitter):
    """
    HRESULT WerReportSetParameter(
        HREPORT hReportHandle,
        DWORD dwparamID,
        PCWSTR pwzName,
        PCWSTR pwzValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hReportHandle", "dwparamID", "pwzName", "pwzValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportSetUIOption(jitter):
    """
    HRESULT WerReportSetUIOption(
        HREPORT hReportHandle,
        WER_REPORT_UI repUITypeID,
        PCWSTR pwzValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hReportHandle", "repUITypeID", "pwzValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wer_WerReportSubmit(jitter):
    """
    HRESULT WerReportSubmit(
        HREPORT hReportHandle,
        WER_CONSENT consent,
        DWORD dwFlags,
        PWER_SUBMIT_RESULT pSubmitResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hReportHandle", "consent", "dwFlags", "pSubmitResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
