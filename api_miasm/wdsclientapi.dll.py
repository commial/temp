
def wdsclientapi_WdsCliAuthorizeSession(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliAuthorizeSession(HANDLE hSession, PWDS_CLI_CRED pCred)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSession", "pCred"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliCancelTransfer(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliCancelTransfer(HANDLE hTransfer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTransfer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliClose(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliClose(HANDLE Handle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliCreateSession(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliCreateSession(PWSTR pwszServer, PWDS_CLI_CRED pCred, PHANDLE phSession)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszServer", "pCred", "phSession"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliFindFirstImage(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliFindFirstImage(HANDLE hSession, PHANDLE phFindHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSession", "phFindHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliFindNextImage(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliFindNextImage(HANDLE Handle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliFreeStringArray(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliFreeStringArray(PWSTR* ppwszArray, ULONG ulCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ppwszArray", "ulCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliObtainDriverPackages(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliObtainDriverPackages(HANDLE hImage, PWSTR* ppwszServerName, PWSTR** pppwszDriverPackages, ULONG* pulCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hImage", "ppwszServerName", "pppwszDriverPackages", "pulCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetEnumerationFlags(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetEnumerationFlags(HANDLE Handle, PDWORD pdwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Handle", "pdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageArchitecture(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageArchitecture(HANDLE hIfh, PDWORD pdwValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "pdwValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageDescription(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageDescription(HANDLE hIfh, PWSTR* ppwszValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "ppwszValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageGroup(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageGroup(HANDLE hIfh, PWSTR* ppwszValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "ppwszValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageHalName(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageHalName(HANDLE hIfh, PWSTR* ppwszValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "ppwszValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageHandleFromFindHandle(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageHandleFromFindHandle(HANDLE FindHandle, PHANDLE phImageHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FindHandle", "phImageHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageHandleFromTransferHandle(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageHandleFromTransferHandle(HANDLE hTransfer, PHANDLE phImageHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTransfer", "phImageHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageIndex(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageIndex(HANDLE hIfh, PDWORD pdwValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "pdwValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageLanguage(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageLanguage(HANDLE hIfh, PWSTR* ppwszValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "ppwszValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageLanguages(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageLanguages(HANDLE hIfh, PTSTR** pppszValues, PDWORD pdwNumValues)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "pppszValues", "pdwNumValues"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageLastModifiedTime(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageLastModifiedTime(HANDLE hIfh, PSYSTEMTIME* ppSysTimeValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "ppSysTimeValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageName(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageName(HANDLE hIfh, PWSTR* ppwszValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "ppwszValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageNamespace(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageNamespace(HANDLE hIfh, PWSTR* ppwszValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "ppwszValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImagePath(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImagePath(HANDLE hIfh, PWSTR* ppwszValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "ppwszValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageSize(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageSize(HANDLE hIfh, PULONGLONG pullValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "pullValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetImageVersion(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetImageVersion(HANDLE hIfh, PWSTR* ppwszValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "ppwszValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetTransferSize(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetTransferSize(HANDLE hIfh, PULONGLONG pullValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hIfh", "pullValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliInitializeLog(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliInitializeLog(HANDLE hSession, ULONG ulClientArchitecture, PWSTR pwszClientId, PWSTR pwszClientAddress)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSession", "ulClientArchitecture", "pwszClientId", "pwszClientAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliLog(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliLog(HANDLE hSession, ULONG ulLogLevel, ULONG ulMessageCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSession", "ulLogLevel", "ulMessageCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliRegisterTrace(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliRegisterTrace(PFN_WdsCliTraceFunction pfn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliTransferFile(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliTransferFile(PCWSTR pwszServer, PCWSTR pwszNamespace, PCWSTR pwszRemoteFilePath, PCWSTR pwszLocalFilePath, DWORD dwFlags, DWORD dwReserved, PFN_WdsCliCallback pfnWdsCliCallback, PVOID pvUserData, PHANDLE phTransfer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszServer", "pwszNamespace", "pwszRemoteFilePath", "pwszLocalFilePath", "dwFlags", "dwReserved", "pfnWdsCliCallback", "pvUserData", "phTransfer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliTransferImage(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliTransferImage(HANDLE hImage, PWSTR pwszLocalPath, DWORD dwFlags, DWORD dwReserved, PFN_WdsCliCallback pfnWdsCliCallback, PVOID pvUserData, PHANDLE phTransfer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hImage", "pwszLocalPath", "dwFlags", "dwReserved", "pfnWdsCliCallback", "pvUserData", "phTransfer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliWaitForTransfer(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliWaitForTransfer(HANDLE hTransfer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTransfer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliGetDriverQueryXml(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliGetDriverQueryXml(PWSTR pwszWinDirPath, PWSTR* ppwszDriverQuery)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszWinDirPath", "ppwszDriverQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsclientapi_WdsCliObtainDriverPackagesEx(jitter):
    """"
    [WdsClientAPI.dll] HRESULT WdsCliObtainDriverPackagesEx(HANDLE hSession, PWSTR pwszDriverQuery, PWSTR* ppwszServerName, PWSTR** pppwszDriverPackages, ULONG* pulCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSession", "pwszDriverQuery", "ppwszServerName", "pppwszDriverPackages", "pulCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
