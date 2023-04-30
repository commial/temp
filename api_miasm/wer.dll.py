WER_DUMP_TYPE = {
    "WerDumpTypeMicroDump": 1,
    "WerDumpTypeMiniDump": 2,
    "WerDumpTypeHeapDump": 3,
    "WerDumpTypeMax": 4,
}
WER_DUMP_TYPE_INV = {
    1: "WerDumpTypeMicroDump",
    2: "WerDumpTypeMiniDump",
    3: "WerDumpTypeHeapDump",
    4: "WerDumpTypeMax",
}
WER_FILE_TYPE = {
    "WerFileTypeMicrodump": 1,
    "WerFileTypeMinidump": 2,
    "WerFileTypeHeapdump": 3,
    "WerFileTypeUserDocument": 4,
    "WerFileTypeOther": 5,
}
WER_FILE_TYPE_INV = {
    1: "WerFileTypeMicrodump",
    2: "WerFileTypeMinidump",
    3: "WerFileTypeHeapdump",
    4: "WerFileTypeUserDocument",
    5: "WerFileTypeOther",
}
WER_REPORT_TYPE = {
    "WerReportNonCritical": 0,
    "WerReportCritical": 1,
    "WerReportApplicationCrash": 2,
    "WerReportApplicationHang": 3,
    "WerReportKernel": 4,
}
WER_REPORT_TYPE_INV = {
    0: "WerReportNonCritical",
    1: "WerReportCritical",
    2: "WerReportApplicationCrash",
    3: "WerReportApplicationHang",
    4: "WerReportKernel",
}
WER_REPORT_UI = {
    "WerUIAdditionalDataDlgHeader": 1,
    "WerUIIconFilePath": 2,
    "WerUIConsentDlgHeader": 3,
    "WerUIConsentDlgBody": 4,
    "WerUIOnlineSolutionCheckText": 5,
    "WerUIOfflineSolutionCheckText": 6,
    "WerUICloseText": 7,
    "WerUICloseDlgHeader": 8,
    "WerUICloseDlgBody": 9,
    "WerUICloseDlgButtonText": 10,
}
WER_REPORT_UI_INV = {
    1: "WerUIAdditionalDataDlgHeader",
    2: "WerUIIconFilePath",
    3: "WerUIConsentDlgHeader",
    4: "WerUIConsentDlgBody",
    5: "WerUIOnlineSolutionCheckText",
    6: "WerUIOfflineSolutionCheckText",
    7: "WerUICloseText",
    8: "WerUICloseDlgHeader",
    9: "WerUICloseDlgBody",
    10: "WerUICloseDlgButtonText",
}
WER_CONSENT = {
    "WerConsentNotAsked": 1,
    "WerConsentApproved": 2,
    "WerConsentDenied": 3,
}
WER_CONSENT_INV = {
    1: "WerConsentNotAsked",
    2: "WerConsentApproved",
    3: "WerConsentDenied",
}
WER_SUBMIT_RESULT = {
    "WerReportQueued": 1,
    "WerReportUploaded": 2,
    "WerReportDebug": 3,
    "WerReportFailed": 4,
    "WerDisabled": 5,
    "WerReportCancelled": 6,
    "WerDisabledQueue": 7,
    "WerReportAsync": 8,
    "WerCustomAction": 9,
    "WerThrottled": 10,
}
WER_SUBMIT_RESULT_INV = {
    1: "WerReportQueued",
    2: "WerReportUploaded",
    3: "WerReportDebug",
    4: "WerReportFailed",
    5: "WerDisabled",
    6: "WerReportCancelled",
    7: "WerDisabledQueue",
    8: "WerReportAsync",
    9: "WerCustomAction",
    10: "WerThrottled",
}

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
