
def msi_MsiSetInternalUI(jitter):
    """"
    [Msi.dll] INSTALLUILEVEL MsiSetInternalUI(INSTALLUILEVEL dwUILevel, HWND* phWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwUILevel", "phWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetExternalUI(jitter):
    """"
    [Msi.dll] INSTALLUI_HANDLER MsiSetExternalUI(INSTALLUI_HANDLER puiHandler, [MsiInstallLogMode] dwMessageFilter, LPVOID pvContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["puiHandler", "dwMessageFilter", "pvContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetExternalUIRecord(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSetExternalUIRecord(PINSTALLUI_HANDLER_RECORD puiHandler, [MsiInstallLogMode] dwMessageFilter, LPVOID pvContext, PINSTALLUI_HANDLER_RECORD ppuiPrevHandler)
    """"
    ret_ad, args = jitter.func_args_stdcall(["puiHandler", "dwMessageFilter", "pvContext", "ppuiPrevHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnableLog(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnableLog([MsiInstallLogMode] dwLogMode, LPCTSTR szLogFile, [MsiInstallLogAttributes] dwLogAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwLogMode", "szLogFile", "dwLogAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiCloseHandle(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiCloseHandle(MSIHANDLE hAny)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hAny"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiCloseAllHandles(jitter):
    """"
    [Msi.dll] UINT MsiCloseAllHandles()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiAdvertiseProduct(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiAdvertiseProduct(LPCTSTR szPackagePath, LPCTSTR szScriptfilePath, LPCTSTR szTransforms, LANGID lgidLanguage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szPackagePath", "szScriptfilePath", "szTransforms", "lgidLanguage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiAdvertiseProductEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiAdvertiseProductEx(LPCTSTR szPackagePath, LPCTSTR szScriptfilePath, LPCTSTR szTransforms, LANGID lgidLanguage, [MsiArchFlags] dwPlatform, [MsiAdOptions] dwOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szPackagePath", "szScriptfilePath", "szTransforms", "lgidLanguage", "dwPlatform", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiAdvertiseScript(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiAdvertiseScript(LPCTSTR szScriptFile, [MsiScriptFlags] dwFlags, PHKEY phRegData, BOOL fRemoveItems)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szScriptFile", "dwFlags", "phRegData", "fRemoveItems"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiInstallProduct(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiInstallProduct(LPCTSTR szPackagePath, LPCTSTR szCommandLine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szPackagePath", "szCommandLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiConfigureProduct(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiConfigureProduct(LPCTSTR szProduct, [MsiInstallLevel] iInstallLevel, INSTALLSTATE eInstallState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "iInstallLevel", "eInstallState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiConfigureProductEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiConfigureProductEx(LPCTSTR szProduct, [MsiInstallLevel] iInstallLevel, INSTALLSTATE eInstallState, LPCTSTR szCommandLine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "iInstallLevel", "eInstallState", "szCommandLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiReinstallProduct(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiReinstallProduct(LPCTSTR szProduct, [MsiReinstallMode] dwReinstallMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "dwReinstallMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiConfigureFeature(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiConfigureFeature(LPCTSTR szProduct, LPCTSTR szFeature, INSTALLSTATE eInstallState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature", "eInstallState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiReinstallFeature(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiReinstallFeature(LPCTSTR szProduct, LPCTSTR szFeature, [MsiReinstallMode] dwReinstallMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature", "dwReinstallMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiInstallMissingComponent(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiInstallMissingComponent(LPCTSTR szProduct, LPCTSTR szComponent, INSTALLSTATE eInstallState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szComponent", "eInstallState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiInstallMissingFile(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiInstallMissingFile(LPCTSTR szProduct, LPCTSTR szFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiNotifySidChange(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiNotifySidChange(LPCTSTR szOldSid, LPCTSTR szNewSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szOldSid", "szNewSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiProcessAdvertiseScript(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiProcessAdvertiseScript(LPCTSTR szScriptFile, LPCTSTR szIconFolder, HKEY hRegData, BOOL fShortcuts, BOOL fRemoveItems)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szScriptFile", "szIconFolder", "hRegData", "fShortcuts", "fRemoveItems"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListAddSource(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSourceListAddSource(LPCTSTR szProduct, LPCTSTR szUserName, DWORD dwReserved, LPCTSTR szSource)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szUserName", "dwReserved", "szSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListAddSourceEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSourceListAddSourceEx(LPCTSTR szProductCodeOrPatchCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, [MsiSourceType] dwOptions, LPCTSTR szSource, DWORD dwIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "szSource", "dwIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListClearSource(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSourceListClearSource(LPCTSTR szProductCodeOrPatchCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, [MsiSourceType] dwOptions, LPCTSTR szSource)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "szSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListClearAll(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSourceListClearAll(LPCTSTR szProduct, LPCTSTR szUserName, DWORD dwReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szUserName", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListClearAllEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSourceListClearAllEx(LPCTSTR szProductCodeOrPatchCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, [MsiSourceType] dwOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListForceResolution(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSourceListForceResolution(LPCTSTR szProduct, LPCTSTR szUserName, DWORD dwReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szUserName", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListForceResolutionEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSourceListForceResolutionEx(LPCTSTR szProductCodeOrPatchCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, [MsiCode] dwOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListGetInfo(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSourceListGetInfo(LPCTSTR szProductCodeOrPatchCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, [MsiCode] dwOptions, LPCTSTR szProperty, LPTSTR szValue, LPDWORD pcchValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "szProperty", "szValue", "pcchValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListSetInfo(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSourceListSetInfo(LPCTSTR szProductCodeOrPatchCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, [MsiSourceType] dwOptions, LPCTSTR szProperty, LPCTSTR szValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "szProperty", "szValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListEnumMediaDisks(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSourceListEnumMediaDisks(LPCTSTR szProductCodeOrPatchCode, LPCTSTR szUserSID, MSIINSTALLCONTEXT dwContext, [MsiCode] dwOptions, DWORD dwIndex, LPWORD pdwDiskId, LPTSTR szVolumeLabel, LPDWORD pcchVolumeLabel, LPTSTR szDiskPrompt, LPDWORD pcchDiskPrompt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSID", "dwContext", "dwOptions", "dwIndex", "pdwDiskId", "szVolumeLabel", "pcchVolumeLabel", "szDiskPrompt", "pcchDiskPrompt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListAddMediaDisk(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSourceListAddMediaDisk(LPCTSTR szProductCodeOrPatchCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, [MsiCode] dwOptions, DWORD dwDiskId, LPCTSTR szVolumeLabel, LPCTSTR szDiskPrompt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "dwDiskId", "szVolumeLabel", "szDiskPrompt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListClearMediaDisk(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSourceListClearMediaDisk(LPCTSTR szProductCodeOrPatchCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, [MsiCode] dwOptions, DWORD dwDiskID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "dwDiskID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSourceListEnumSources(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSourceListEnumSources(LPCTSTR szProductCodeOrPatchCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, [MsiSourceType] dwOptions, DWORD dwIndex, LPTSTR szSource, LPDWORD pcchSource)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCodeOrPatchCode", "szUserSid", "dwContext", "dwOptions", "dwIndex", "szSource", "pcchSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiProvideAssembly(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiProvideAssembly(LPCTSTR szAssemblyName, LPCTSTR szAppContext, [MsiInstallMode] dwInstallMode, [MsiAssemblyInfo] dwAssemblyInfo, LPTSTR lpPathBuf, DWORD* pcchPathBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szAssemblyName", "szAppContext", "dwInstallMode", "dwAssemblyInfo", "lpPathBuf", "pcchPathBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiProvideComponent(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiProvideComponent(LPCTSTR szProduct, LPCTSTR szFeature, LPCTSTR szComponent, [MsiInstallMode] dwInstallMode, LPTSTR lpPathBuf, DWORD* pcchPathBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature", "szComponent", "dwInstallMode", "lpPathBuf", "pcchPathBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiProvideQualifiedComponent(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiProvideQualifiedComponent(LPCTSTR szComponent, LPCTSTR szQualifier, [MsiInstallMode] dwInstallMode, LPTSTR lpPathBuf, DWORD* pcchPathBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "szQualifier", "dwInstallMode", "lpPathBuf", "pcchPathBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiProvideQualifiedComponentEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiProvideQualifiedComponentEx(LPCTSTR szComponent, LPCTSTR szQualifier, [MsiInstallMode] dwInstallMode, LPTSTR szProduct, DWORD dwUnused1, DWORD dwUnused2, LPTSTR lpPathBuf, DWORD* pcchPathBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "szQualifier", "dwInstallMode", "szProduct", "dwUnused1", "dwUnused2", "lpPathBuf", "pcchPathBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetComponentPath(jitter):
    """"
    [Msi.dll] INSTALLSTATE MsiGetComponentPath(LPCTSTR szProduct, LPCTSTR szComponent, LPTSTR lpPathBuf, DWORD* pcchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szComponent", "lpPathBuf", "pcchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetComponentPathEx(jitter):
    """"
    [Msi.dll] INSTALLSTATE MsiGetComponentPathEx(LPCTSTR szProductCode, LPCTSTR szComponentCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, LPTSTR szPathBuf, LPDWORD pcchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szComponentCode", "szUserSid", "dwContext", "szPathBuf", "pcchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiLocateComponent(jitter):
    """"
    [Msi.dll] INSTALLSTATE MsiLocateComponent(LPCTSTR szComponent, LPTSTR lpPathBuf, DWORD* pcchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "lpPathBuf", "pcchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiQueryComponentState(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiQueryComponentState(LPTSTR szProductCode, LPTSTR szUserSid, MSIINSTALLCONTEXT dwContext, LPCTSTR szComponent, INSTALLSTATE* pdwState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szUserSid", "dwContext", "szComponent", "pdwState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiCollectUserInfo(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiCollectUserInfo(LPCTSTR szProduct)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiUseFeature(jitter):
    """"
    [Msi.dll] INSTALLSTATE MsiUseFeature(LPCTSTR szProduct, LPCTSTR szFeature)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiUseFeatureEx(jitter):
    """"
    [Msi.dll] INSTALLSTATE MsiUseFeatureEx(LPCTSTR szProduct, LPCTSTR szFeature, [MsiInstallMode] dwInstallMode, DWORD dwReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature", "dwInstallMode", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetProductCode(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetProductCode(LPCTSTR szComponent, LPTSTR lpProductBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "lpProductBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumProducts(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnumProducts(DWORD iProductIndex, LPTSTR lpProductBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iProductIndex", "lpProductBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumProductsEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnumProductsEx(LPCTSTR szProductCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, DWORD dwIndex, TCHAR [39] szInstalledProductCode, MSIINSTALLCONTEXT* pdwInstalledContext, LPTSTR szSid, LPDWORD pcchSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szUserSid", "dwContext", "dwIndex", "szInstalledProductCode", "pdwInstalledContext", "szSid", "pcchSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumRelatedProducts(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnumRelatedProducts(LPCTSTR lpUpgradeCode, DWORD dwReserved, DWORD iProductIndex, LPTSTR lpProductBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpUpgradeCode", "dwReserved", "iProductIndex", "lpProductBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumFeatures(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnumFeatures(LPCTSTR szProduct, DWORD iFeatureIndex, LPTSTR lpFeatureBuf, LPTSTR lpParentBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "iFeatureIndex", "lpFeatureBuf", "lpParentBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumComponents(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnumComponents(DWORD iComponentIndex, LPTSTR lpComponentBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["iComponentIndex", "lpComponentBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumComponentsEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnumComponentsEx(LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, DWORD dwIndex, TCHAR [39] szInstalledComponentCode, MSIINSTALLCONTEXT* pdwInstalledContext, LPTSTR szSid, LPDWORD pcchSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szUserSid", "dwContext", "dwIndex", "szInstalledComponentCode", "pdwInstalledContext", "szSid", "pcchSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumClients(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnumClients(LPCTSTR szComponent, DWORD iProductIndex, LPTSTR lpProductBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "iProductIndex", "lpProductBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumClientsEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnumClientsEx(LPCTSTR szComponent, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, DWORD dwProductIndex, TCHAR [39] szProductBuf, MSIINSTALLCONTEXT* pdwInstalledContext, LPTSTR szSid, LPDWORD pcchSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "szUserSid", "dwContext", "dwProductIndex", "szProductBuf", "pdwInstalledContext", "szSid", "pcchSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumComponentQualifiers(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnumComponentQualifiers(LPTSTR szComponent, DWORD iIndex, LPTSTR lpQualifierBuf, DWORD* pcchQualifierBuf, LPTSTR lpApplicationDataBuf, DWORD* pcchApplicationDataBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szComponent", "iIndex", "lpQualifierBuf", "pcchQualifierBuf", "lpApplicationDataBuf", "pcchApplicationDataBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiQueryFeatureState(jitter):
    """"
    [Msi.dll] INSTALLSTATE MsiQueryFeatureState(LPCTSTR szProduct, LPCTSTR szFeature)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiQueryFeatureStateEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiQueryFeatureStateEx(LPTSTR szProductCode, LPTSTR szUserSid, MSIINSTALLCONTEXT dwContext, LPCTSTR szFeature, INSTALLSTATE* pdwState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szUserSid", "dwContext", "szFeature", "pdwState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiQueryProductState(jitter):
    """"
    [Msi.dll] INSTALLSTATE MsiQueryProductState(LPCTSTR szProduct)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFeatureUsage(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetFeatureUsage(LPCTSTR szProduct, LPCTSTR szFeature, DWORD* pdwUseCount, WORD* pwDateUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szFeature", "pdwUseCount", "pwDateUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetProductInfo(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetProductInfo(LPCTSTR szProduct, LPCTSTR szProperty, LPTSTR lpValueBuf, DWORD* pcchValueBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "szProperty", "lpValueBuf", "pcchValueBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetProductInfoEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetProductInfoEx(LPCTSTR szProductCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, LPCTSTR szProperty, LPTSTR lpValue, LPDWORD pcchValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szUserSid", "dwContext", "szProperty", "lpValue", "pcchValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetUserInfo(jitter):
    """"
    [Msi.dll] USERINFOSTATE MsiGetUserInfo(LPCTSTR szProduct, LPTSTR lpUserNameBuf, DWORD* pcchUserNameBuf, LPTSTR lpOrgNameBuf, DWORD* pcchOrgNameBuf, LPTSTR lpSerialBuf, DWORD* pcchSerialBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "lpUserNameBuf", "pcchUserNameBuf", "lpOrgNameBuf", "pcchOrgNameBuf", "lpSerialBuf", "pcchSerialBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiOpenProduct(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiOpenProduct(LPCTSTR szProduct, MSIHANDLE* hProduct)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "hProduct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiOpenPackage(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiOpenPackage(LPCTSTR szPackagePath, MSIHANDLE* hProduct)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szPackagePath", "hProduct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiOpenPackageEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiOpenPackageEx(LPCTSTR szPackagePath, [MsiOpenPackageFlags] dwOptions, MSIHANDLE* hProduct)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szPackagePath", "dwOptions", "hProduct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiIsProductElevated(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiIsProductElevated(LPCTSTR szProductCode, BOOL* pfElevated)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "pfElevated"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetProductInfoFromScript(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetProductInfoFromScript(LPCTSTR szScriptFile, LPTSTR lpProductBuf39, LANGID* plgidLanguage, DWORD* pdwVersion, LPTSTR lpNameBuf, DWORD* pcchNameBuf, LPTSTR lpPackageBuf, DWORD* pcchPackageBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szScriptFile", "lpProductBuf39", "plgidLanguage", "pdwVersion", "lpNameBuf", "pcchNameBuf", "lpPackageBuf", "pcchPackageBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetProductProperty(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetProductProperty(MSIHANDLE hProduct, LPCTSTR szProperty, LPTSTR lpValueBuf, DWORD* pcchValueBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProduct", "szProperty", "lpValueBuf", "pcchValueBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetShortcutTarget(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetShortcutTarget(LPCTSTR szShortcutTarget, LPTSTR szProductCode, LPTSTR szFeatureId, LPTSTR szComponentCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szShortcutTarget", "szProductCode", "szFeatureId", "szComponentCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFeatureInfo(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetFeatureInfo(MSIHANDLE hProduct, LPCTSTR szFeature, [MsiInstallFeatureAttr*] lpAttributes, LPTSTR lpTitleBuf, LPDWORD pcchTitleBuf, LPTSTR lpHelpBuf, LPDWORD pcchHelpBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProduct", "szFeature", "lpAttributes", "lpTitleBuf", "pcchTitleBuf", "lpHelpBuf", "pcchHelpBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiVerifyPackage(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiVerifyPackage(LPCTSTR szPackagePath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szPackagePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiApplyPatch(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiApplyPatch(LPCTSTR szPatchPackage, LPCTSTR szInstallPackage, INSTALLTYPE eInstallType, LPCTSTR szCommandLine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szPatchPackage", "szInstallPackage", "eInstallType", "szCommandLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumPatches(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnumPatches(LPCTSTR szProduct, DWORD iPatchIndex, LPTSTR lpPatchBuf, LPTSTR lpTransformsBuf, DWORD* pcchTransformsBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProduct", "iPatchIndex", "lpPatchBuf", "lpTransformsBuf", "pcchTransformsBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetPatchInfo(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetPatchInfo(LPCTSTR szPatch, LPCTSTR szAttribute, LPTSTR lpValueBuf, DWORD* pcchValueBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szPatch", "szAttribute", "lpValueBuf", "pcchValueBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRemovePatches(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiRemovePatches(LPCTSTR szPatchList, LPCTSTR szProductCode, INSTALLTYPE eUninstallType, LPCTSTR szPropertyList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szPatchList", "szProductCode", "eUninstallType", "szPropertyList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDeterminePatchSequence(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiDeterminePatchSequence(LPCTSTR szProductCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, DWORD cPatchInfo, PMSIPATCHSEQUENCEINFO pPatchInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szUserSid", "dwContext", "cPatchInfo", "pPatchInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiApplyMultiplePatches(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiApplyMultiplePatches(LPCTSTR szPatchPackages, LPCTSTR szProductCode, LPCTSTR szPropertiesList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szPatchPackages", "szProductCode", "szPropertiesList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumPatchesEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnumPatchesEx(LPCTSTR szProductCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, [MsiPatchState] dwFilter, DWORD dwIndex, TCHAR [39] szPatchCode, TCHAR [39] szTargetProductCode, MSIINSTALLCONTEXT* pdwTargetProductContext, LPTSTR szTargetUserSid, LPDWORD pcchTargetUserSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szUserSid", "dwContext", "dwFilter", "dwIndex", "szPatchCode", "szTargetProductCode", "pdwTargetProductContext", "szTargetUserSid", "pcchTargetUserSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetPatchFileList(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetPatchFileList(LPCTSTR szProductCode, LPCTSTR szPatchList, LPDWORD pcFiles, MSIHANDLE** pphFileRecords)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductCode", "szPatchList", "pcFiles", "pphFileRecords"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetPatchInfoEx(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetPatchInfoEx(LPCTSTR szPatchCode, LPCTSTR szProductCode, LPCTSTR szUserSid, MSIINSTALLCONTEXT dwContext, LPCTSTR szProperty, LPTSTR lpValue, DWORD* pcchValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szPatchCode", "szProductCode", "szUserSid", "dwContext", "szProperty", "lpValue", "pcchValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiExtractPatchXMLData(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiExtractPatchXMLData(LPCTSTR szPatchPath, DWORD dwReserved, LPTSTR szXMLData, DWORD* pcchXMLData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szPatchPath", "dwReserved", "szXMLData", "pcchXMLData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDetermineApplicablePatches(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiDetermineApplicablePatches(LPCTSTR szProductPackagePath, DWORD cPatchInfo, PMSIPATCHSEQUENCEINFO pPatchInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szProductPackagePath", "cPatchInfo", "pPatchInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFileHash(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetFileHash(LPCTSTR szFilePath, DWORD dwOptions, PMSIFILEHASHINFO pHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szFilePath", "dwOptions", "pHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFileSignatureInformation(jitter):
    """"
    [Msi.dll] HRESULT MsiGetFileSignatureInformation(LPCTSTR szSignedObjectPath, [MsiHashFlags] dwFlags, PCCERT_CONTEXT* ppcCertContext, BYTE* pbHashData, DWORD* pcbHashData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szSignedObjectPath", "dwFlags", "ppcCertContext", "pbHashData", "pcbHashData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFileVersion(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetFileVersion(LPCTSTR szFilePath, LPTSTR lpVersionBuf, DWORD* pcchVersionBuf, LPTSTR lpLangBuf, DWORD* pcchLangBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szFilePath", "lpVersionBuf", "pcchVersionBuf", "lpLangBuf", "pcchLangBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiBeginTransaction(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiBeginTransaction(LPCWSTR szTransactionName, [MsiTransactionAttributes] dwTransactionAttributes, MSIHANDLE* hTransactionID, HANDLE* phChangeOfOwnerEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szTransactionName", "dwTransactionAttributes", "hTransactionID", "phChangeOfOwnerEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiJoinTransaction(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiJoinTransaction(MSIHANDLE hTransactionID, [MsiTransactionAttributes] dwTransactionAttributes, HANDLE* phChangeOfOwnerEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTransactionID", "dwTransactionAttributes", "phChangeOfOwnerEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEndTransaction(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEndTransaction([MsiTransactionState] dwTransactionState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwTransactionState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseCommit(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiDatabaseCommit(MSIHANDLE hDatabase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDatabase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseGetPrimaryKeys(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiDatabaseGetPrimaryKeys(MSIHANDLE hDatabase, LPCTSTR szTableName, MSIHANDLE* phRecord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szTableName", "phRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseIsTablePersistent(jitter):
    """"
    [Msi.dll] MSICONDITION MsiDatabaseIsTablePersistent(MSIHANDLE hDatabase, LPCTSTR szTableName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szTableName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseOpenView(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiDatabaseOpenView(MSIHANDLE hDatabase, LPCTSTR szQuery, MSIHANDLE* phView)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szQuery", "phView"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetActiveDatabase(jitter):
    """"
    [Msi.dll] MSIHANDLE MsiGetActiveDatabase(MSIHANDLE hInstall)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiViewGetColumnInfo(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiViewGetColumnInfo(MSIHANDLE hView, MSICOLINFO eColumnInfo, MSIHANDLE* phRecord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hView", "eColumnInfo", "phRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiOpenDatabase(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiOpenDatabase(LPCTSTR szDatabasePath, LPCTSTR szPersist, MSIHANDLE* phDatabase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szDatabasePath", "szPersist", "phDatabase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiViewClose(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiViewClose(MSIHANDLE hView)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hView"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiViewExecute(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiViewExecute(MSIHANDLE hView, MSIHANDLE hRecord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hView", "hRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiViewFetch(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiViewFetch(MSIHANDLE hView, MSIHANDLE* phRecord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hView", "phRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiViewGetError(jitter):
    """"
    [Msi.dll] MSIDBERROR MsiViewGetError(MSIHANDLE hView, LPTSTR szColumnNameBuffer, DWORD* pcchBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hView", "szColumnNameBuffer", "pcchBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiViewModify(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiViewModify(MSIHANDLE hView, MSIMODIFY eModifyMode, MSIHANDLE hRecord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hView", "eModifyMode", "hRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiCreateTransformSummaryInfo(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiCreateTransformSummaryInfo(MSIHANDLE hDatabase, MSIHANDLE hDatabaseReference, LPCTSTR szTransformFile, MSITRANSFORM_ERROR iErrorConditions, MSITRANSFORM_VALIDATE iValidation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "hDatabaseReference", "szTransformFile", "iErrorConditions", "iValidation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseApplyTransform(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiDatabaseApplyTransform(MSIHANDLE hDatabase, LPCTSTR szTransformFile, MSITRANSFORM_ERROR iErrorConditions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szTransformFile", "iErrorConditions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseExport(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiDatabaseExport(MSIHANDLE hDatabase, LPCTSTR szTableName, LPCTSTR szFolderPath, LPCTSTR szFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szTableName", "szFolderPath", "szFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseGenerateTransform(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiDatabaseGenerateTransform(MSIHANDLE hDatabase, MSIHANDLE hDatabaseReference, LPCTSTR szTransformFile, int iReserved1, int iReserved2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "hDatabaseReference", "szTransformFile", "iReserved1", "iReserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseImport(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiDatabaseImport(MSIHANDLE hDatabase, LPCTSTR szFolderPath, LPCTSTR szFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szFolderPath", "szFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDatabaseMerge(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiDatabaseMerge(MSIHANDLE hDatabase, MSIHANDLE hDatabaseMerge, LPCTSTR szTableName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "hDatabaseMerge", "szTableName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetDatabaseState(jitter):
    """"
    [Msi.dll] MSIDBSTATE MsiGetDatabaseState(MSIHANDLE hDatabase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDatabase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiCreateRecord(jitter):
    """"
    [Msi.dll] MSIHANDLE MsiCreateRecord(unsigned int cParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiFormatRecord(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiFormatRecord(MSIHANDLE hInstall, MSIHANDLE hRecord, LPTSTR szResultBuf, DWORD* pcchResultBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "hRecord", "szResultBuf", "pcchResultBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordClearData(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiRecordClearData(MSIHANDLE hRecord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordDataSize(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiRecordDataSize(MSIHANDLE hRecord, unsigned int iField)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordGetFieldCount(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiRecordGetFieldCount(MSIHANDLE hRecord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordGetInteger(jitter):
    """"
    [Msi.dll] int MsiRecordGetInteger(MSIHANDLE hRecord, unsigned int iField)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordGetString(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiRecordGetString(MSIHANDLE hRecord, unsigned int iField, LPTSTR szValueBuf, DWORD* pcchValueBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField", "szValueBuf", "pcchValueBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordIsNull(jitter):
    """"
    [Msi.dll] BOOL MsiRecordIsNull(MSIHANDLE hRecord, unsigned int iField)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordReadStream(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiRecordReadStream(MSIHANDLE hRecord, UINT iField, char* szDataBuf, DWORD* pcbDataBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField", "szDataBuf", "pcbDataBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordSetInteger(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiRecordSetInteger(MSIHANDLE hRecord, unsigned int iField, int iValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField", "iValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordSetStream(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiRecordSetStream(MSIHANDLE hRecord, UINT iField, LPCTSTR szFilePath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField", "szFilePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiRecordSetString(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiRecordSetString(MSIHANDLE hRecord, unsigned int iField, LPCTSTR szValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRecord", "iField", "szValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetSummaryInformation(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetSummaryInformation(MSIHANDLE hDatabase, LPCTSTR szDatabasePath, UINT uiUpdateCount, MSIHANDLE* phSummaryInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "szDatabasePath", "uiUpdateCount", "phSummaryInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSummaryInfoGetProperty(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSummaryInfoGetProperty(MSIHANDLE hSummaryInfo, [MSI_PID] uiProperty, [MSI_DATA_TYPE*] puiDataType, INT* piValue, FILETIME* pftValue, LPTSTR szValueBuf, DWORD* pcchValueBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSummaryInfo", "uiProperty", "puiDataType", "piValue", "pftValue", "szValueBuf", "pcchValueBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSummaryInfoGetPropertyCount(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSummaryInfoGetPropertyCount(MSIHANDLE hSummaryInfo, UINT* puiPropertyCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSummaryInfo", "puiPropertyCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSummaryInfoPersist(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSummaryInfoPersist(MSIHANDLE hSummaryInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSummaryInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSummaryInfoSetProperty(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSummaryInfoSetProperty(MSIHANDLE hSummaryInfo, [MSI_PID] uiProperty, [MSI_DATA_TYPE] uiDataType, INT iValue, FILETIME* pftValue, LPTSTR szValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSummaryInfo", "uiProperty", "uiDataType", "iValue", "pftValue", "szValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetLanguage(jitter):
    """"
    [Msi.dll] LANGID MsiGetLanguage(MSIHANDLE hInstall)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetLastErrorRecord(jitter):
    """"
    [Msi.dll] MSIHANDLE MsiGetLastErrorRecord()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetMode(jitter):
    """"
    [Msi.dll] BOOL MsiGetMode(MSIHANDLE hInstall, MSIRUNMODE iRunMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "iRunMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetProperty(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetProperty(MSIHANDLE hInstall, LPCTSTR szName, LPTSTR szValueBuf, DWORD* pchValueBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szName", "szValueBuf", "pchValueBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetProperty(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSetProperty(MSIHANDLE hInstall, LPCTSTR szName, LPCTSTR szValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szName", "szValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetMode(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSetMode(MSIHANDLE hInstall, unsigned int iRunMode, BOOL fState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "iRunMode", "fState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiDoAction(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiDoAction(MSIHANDLE hInstall, LPCTSTR szAction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szAction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEvaluateCondition(jitter):
    """"
    [Msi.dll] MSICONDITION MsiEvaluateCondition(MSIHANDLE hInstall, LPCTSTR szCondition)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szCondition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiProcessMessage(jitter):
    """"
    [Msi.dll] int MsiProcessMessage(MSIHANDLE hInstall, INSTALLMESSAGE eMessageType, MSIHANDLE hRecord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "eMessageType", "hRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSequence(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSequence(MSIHANDLE hInstall, LPCTSTR szTable, INT iSequenceMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szTable", "iSequenceMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetSourcePath(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetSourcePath(MSIHANDLE hInstall, LPCTSTR szFolder, LPTSTR szPathBuf, DWORD* pcchPathBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFolder", "szPathBuf", "pcchPathBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetTargetPath(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetTargetPath(MSIHANDLE hInstall, LPCTSTR szFolder, LPTSTR szPathBuf, DWORD* pcchPathBuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFolder", "szPathBuf", "pcchPathBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetTargetPath(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSetTargetPath(MSIHANDLE hInstall, LPCTSTR szFolder, LPCTSTR szFolderPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFolder", "szFolderPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnumComponentCosts(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnumComponentCosts(MSIHANDLE hInstall, LPCTSTR szComponent, DWORD dwIndex, INSTALLSTATE iState, LPTSTR lpDriveBuf, DWORD* pcchDriveBuf, int* piCost, int* pTempCost)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szComponent", "dwIndex", "iState", "lpDriveBuf", "pcchDriveBuf", "piCost", "pTempCost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetComponentState(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetComponentState(MSIHANDLE hInstall, LPCTSTR szComponent, INSTALLSTATE* piInstalled, INSTALLSTATE* piAction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szComponent", "piInstalled", "piAction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFeatureCost(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetFeatureCost(MSIHANDLE hInstall, LPCTSTR szFeature, MSICOSTTREE iCostTree, INSTALLSTATE iState, INT* piCost)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFeature", "iCostTree", "iState", "piCost"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFeatureState(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetFeatureState(MSIHANDLE hInstall, LPCTSTR szFeature, INSTALLSTATE* piInstalled, INSTALLSTATE* piAction)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFeature", "piInstalled", "piAction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiGetFeatureValidStates(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiGetFeatureValidStates(MSIHANDLE hInstall, LPCTSTR szFeature, [INSTALLSTATE-DWORD*] pInstallState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFeature", "pInstallState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetComponentState(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSetComponentState(MSIHANDLE hInstall, LPCTSTR szComponent, INSTALLSTATE iState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szComponent", "iState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetFeatureAttributes(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSetFeatureAttributes(MSIHANDLE hInstall, LPCTSTR szFeature, [MsiInstallFeatureAttr] dwAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFeature", "dwAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetFeatureState(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSetFeatureState(MSIHANDLE hInstall, LPCTSTR szFeature, INSTALLSTATE iState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "szFeature", "iState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiSetInstallLevel(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiSetInstallLevel(MSIHANDLE hInstall, int iInstallLevel)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall", "iInstallLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiVerifyDiskSpace(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiVerifyDiskSpace(MSIHANDLE hInstall)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hInstall"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiEnableUIPreview(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiEnableUIPreview(MSIHANDLE hDatabase, MSIHANDLE* phPreview)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDatabase", "phPreview"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiPreviewBillboard(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiPreviewBillboard(MSIHANDLE hPreview, LPCTSTR szControlName, LPCTSTR szBillboard)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPreview", "szControlName", "szBillboard"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msi_MsiPreviewDialog(jitter):
    """"
    [Msi.dll] [MSI_ERROR] MsiPreviewDialog(MSIHANDLE hPreview, LPCTSTR szDialogName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPreview", "szDialogName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
