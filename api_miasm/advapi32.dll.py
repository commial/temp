
def advapi32_RegCloseKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegCloseKey(HKEY hKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegConnectRegistry(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegConnectRegistry(LPCTSTR lpMachineName, HKEY hKey, PHKEY phkResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMachineName", "hKey", "phkResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegCopyTree(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegCopyTree(HKEY hKeySrc, LPCTSTR lpSubKey, HKEY hKeyDest)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKeySrc", "lpSubKey", "hKeyDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegCreateKeyEx(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegCreateKeyEx(HKEY hKey, LPCTSTR lpSubKey, DWORD Reserved, LPTSTR lpClass, [RegOptions] dwOptions, REGSAM samDesired, LPSECURITY_ATTRIBUTES lpSecurityAttributes, PHKEY phkResult, [RegDisposition*] lpdwDisposition)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "Reserved", "lpClass", "dwOptions", "samDesired", "lpSecurityAttributes", "phkResult", "lpdwDisposition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegCreateKeyTransacted(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegCreateKeyTransacted(HKEY hKey, LPCTSTR lpSubKey, DWORD Reserved, LPTSTR lpClass, [RegOptions] dwOptions, REGSAM samDesired, const LPSECURITY_ATTRIBUTES lpSecurityAttributes, PHKEY phkResult, [RegDisposition*] lpdwDisposition, HANDLE hTransaction, PVOID pExtendedParemeter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "Reserved", "lpClass", "dwOptions", "samDesired", "lpSecurityAttributes", "phkResult", "lpdwDisposition", "hTransaction", "pExtendedParemeter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegDeleteKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegDeleteKey(HKEY hKey, LPCTSTR lpSubKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegDeleteKeyEx(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegDeleteKeyEx(HKEY hKey, LPCTSTR lpSubKey, REGSAM samDesired, DWORD Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "samDesired", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegDeleteKeyTransacted(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegDeleteKeyTransacted(HKEY hKey, LPCTSTR lpSubKey, REGSAM samDesired, DWORD Reserved, HANDLE hTransaction, PVOID pExtendedParameter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "samDesired", "Reserved", "hTransaction", "pExtendedParameter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegDeleteKeyValue(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegDeleteKeyValue(HKEY hKey, LPCTSTR lpSubKey, LPCTSTR lpValueName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "lpValueName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegDeleteTree(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegDeleteTree(HKEY hKey, LPCTSTR lpSubKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegDeleteValue(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegDeleteValue(HKEY hKey, LPCTSTR lpValueName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpValueName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegDisablePredefinedCache(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegDisablePredefinedCache()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegDisablePredefinedCacheEx(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegDisablePredefinedCacheEx()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegDisableReflectionKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegDisableReflectionKey(HKEY hBase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegEnableReflectionKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegEnableReflectionKey(HKEY hBase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegEnumKeyEx(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegEnumKeyEx(HKEY hKey, DWORD dwIndex, LPTSTR lpName, LPDWORD lpcName, LPDWORD lpReserved, LPTSTR lpClass, LPDWORD lpcClass, PFILETIME lpftLastWriteTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "dwIndex", "lpName", "lpcName", "lpReserved", "lpClass", "lpcClass", "lpftLastWriteTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegEnumValue(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegEnumValue(HKEY hKey, DWORD dwIndex, LPTSTR lpValueName, LPDWORD lpcchValueName, LPDWORD lpReserved, [RegType*] lpType, LPBYTE lpData, LPDWORD lpcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "dwIndex", "lpValueName", "lpcchValueName", "lpReserved", "lpType", "lpData", "lpcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegFlushKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegFlushKey(HKEY hKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegGetValue(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegGetValue(HKEY hkey, LPCTSTR lpSubKey, LPCTSTR lpValue, DWORD dwFlags, [RegType*] pdwType, PVOID pvData, LPDWORD pcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hkey", "lpSubKey", "lpValue", "dwFlags", "pdwType", "pvData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegLoadAppKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegLoadAppKey(LPCTSTR lpFile, PHKEY phkResult, REGSAM samDesired, [RegLoadAppKey_Options] dwOptions, DWORD Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFile", "phkResult", "samDesired", "dwOptions", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegLoadKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegLoadKey(HKEY hKey, LPCTSTR lpSubKey, LPCTSTR lpFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "lpFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegLoadMUIString(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegLoadMUIString(HKEY hKey, LPCTSTR pszValue, LPTSTR pszOutBuf, DWORD cbOutBuf, LPDWORD pcbData, [RegMuiFlags] Flags, LPCTSTR pszDirectory)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pszValue", "pszOutBuf", "cbOutBuf", "pcbData", "Flags", "pszDirectory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegNotifyChangeKeyValue(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegNotifyChangeKeyValue(HKEY hKey, BOOL bWatchSubtree, [RegNotifyFlags] dwNotifyFilter, HANDLE hEvent, BOOL fAsynchronous)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "bWatchSubtree", "dwNotifyFilter", "hEvent", "fAsynchronous"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegOpenCurrentUser(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegOpenCurrentUser(REGSAM samDesired, PHKEY phkResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["samDesired", "phkResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegOpenKeyEx(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegOpenKeyEx(HKEY hKey, LPCTSTR lpSubKey, DWORD ulOptions, REGSAM samDesired, PHKEY phkResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "ulOptions", "samDesired", "phkResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegOpenKeyTransacted(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegOpenKeyTransacted(HKEY hKey, LPCTSTR lpSubKey, DWORD ulOptions, REGSAM samDesired, PHKEY phkResult, HANDLE hTransaction, PVOID pExtendedParameter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "ulOptions", "samDesired", "phkResult", "hTransaction", "pExtendedParameter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegOpenUserClassesRoot(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegOpenUserClassesRoot(HANDLE hToken, DWORD dwOptions, REGSAM samDesired, PHKEY phkResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hToken", "dwOptions", "samDesired", "phkResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegOverridePredefKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegOverridePredefKey(HKEY hKey, HKEY hNewHKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "hNewHKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegQueryInfoKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegQueryInfoKey(HKEY hKey, LPTSTR lpClass, LPDWORD lpcClass, LPDWORD lpReserved, LPDWORD lpcSubKeys, LPDWORD lpcMaxSubKeyLen, LPDWORD lpcMaxClassLen, LPDWORD lpcValues, LPDWORD lpcMaxValueNameLen, LPDWORD lpcMaxValueLen, LPDWORD lpcbSecurityDescriptor, PFILETIME lpftLastWriteTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpClass", "lpcClass", "lpReserved", "lpcSubKeys", "lpcMaxSubKeyLen", "lpcMaxClassLen", "lpcValues", "lpcMaxValueNameLen", "lpcMaxValueLen", "lpcbSecurityDescriptor", "lpftLastWriteTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegQueryMultipleValues(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegQueryMultipleValues(HKEY hKey, PVALENT val_list, DWORD num_vals, LPVOID lpValueBuf, LPDWORD ldwTotsize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "val_list", "num_vals", "lpValueBuf", "ldwTotsize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegQueryReflectionKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegQueryReflectionKey(HKEY hBase, BOOL* bIsReflectionDisabled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hBase", "bIsReflectionDisabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegQueryValueEx(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegQueryValueEx(HKEY hKey, LPCTSTR lpValueName, LPDWORD lpReserved, [RegType*] lpType, LPBYTE lpData, LPDWORD lpcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpValueName", "lpReserved", "lpType", "lpData", "lpcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegReplaceKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegReplaceKey(HKEY hKey, LPCTSTR lpSubKey, LPCTSTR lpNewFile, LPCTSTR lpOldFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "lpNewFile", "lpOldFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegRestoreKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegRestoreKey(HKEY hKey, LPCTSTR lpFile, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpFile", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegSaveKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegSaveKey(HKEY hKey, LPCTSTR lpFile, LPSECURITY_ATTRIBUTES lpSecurityAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpFile", "lpSecurityAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegSaveKeyEx(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegSaveKeyEx(HKEY hKey, LPCTSTR lpFile, LPSECURITY_ATTRIBUTES lpSecurityAttributes, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpFile", "lpSecurityAttributes", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegSetKeyValue(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegSetKeyValue(HKEY hKey, LPCTSTR lpSubKey, LPCTSTR lpValueName, [RegType] dwType, LPCVOID lpData, DWORD cbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "lpValueName", "dwType", "lpData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegSetValueEx(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegSetValueEx(HKEY hKey, LPCTSTR lpValueName, DWORD Reserved, [RegType] dwType, const BYTE* lpData, DWORD cbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpValueName", "Reserved", "dwType", "lpData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegUnLoadKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegUnLoadKey(HKEY hKey, LPCTSTR lpSubKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegCreateKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegCreateKey(HKEY hKey, LPCTSTR lpSubKey, PHKEY phkResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "phkResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegEnumKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegEnumKey(HKEY hKey, DWORD dwIndex, LPTSTR lpName, DWORD cchName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "dwIndex", "lpName", "cchName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegOpenKey(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegOpenKey(HKEY hKey, LPCTSTR lpSubKey, PHKEY phkResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "phkResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegQueryValue(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegQueryValue(HKEY hKey, LPCTSTR lpSubKey, LPTSTR lpValue, PLONG lpcbValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "lpValue", "lpcbValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegSetValue(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegSetValue(HKEY hKey, LPCTSTR lpSubKey, [RegType] dwType, LPCTSTR lpData, DWORD cbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "dwType", "lpData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AddUsersToEncryptedFile(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] AddUsersToEncryptedFile(LPCWSTR lpFileName, PENCRYPTION_CERTIFICATE_LIST pUsers)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "pUsers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CloseEncryptedFileRaw(jitter):
    """"
    [Advapi32.dll] void CloseEncryptedFileRaw(PVOID pvContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_DecryptFile(jitter):
    """"
    [Advapi32.dll] BOOL DecryptFile(LPCTSTR lpFileName, DWORD dwReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_DuplicateEncryptionInfoFile(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] DuplicateEncryptionInfoFile(LPCTSTR SrcFileName, LPCTSTR DstFileName, DWORD dwCreationDistribution, DWORD dwAttributes, const LPSECURITY_ATTRIBUTES lpSecurityAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SrcFileName", "DstFileName", "dwCreationDistribution", "dwAttributes", "lpSecurityAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EncryptFile(jitter):
    """"
    [Advapi32.dll] BOOL EncryptFile(LPCTSTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EncryptionDisable(jitter):
    """"
    [Advapi32.dll] BOOL EncryptionDisable(LPCWSTR DirPath, BOOL Disable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DirPath", "Disable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_FileEncryptionStatus(jitter):
    """"
    [Advapi32.dll] BOOL FileEncryptionStatus(LPCTSTR lpFileName, LPDWORD lpStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "lpStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_FreeEncryptionCertificateHashList(jitter):
    """"
    [Advapi32.dll] void FreeEncryptionCertificateHashList(PENCRYPTION_CERTIFICATE_HASH_LIST pHashes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pHashes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_OpenEncryptedFileRaw(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] OpenEncryptedFileRaw(LPCTSTR lpFileName, ULONG ulFlags, PVOID* pvContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "ulFlags", "pvContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_QueryRecoveryAgentsOnEncryptedFile(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] QueryRecoveryAgentsOnEncryptedFile(LPCWSTR lpFileName, PENCRYPTION_CERTIFICATE_HASH_LIST* pRecoveryAgents)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "pRecoveryAgents"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_QueryUsersOnEncryptedFile(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] QueryUsersOnEncryptedFile(LPCWSTR lpFileName, PENCRYPTION_CERTIFICATE_HASH_LIST* pUsers)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "pUsers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ReadEncryptedFileRaw(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] ReadEncryptedFileRaw(PFE_EXPORT_FUNC pfExportCallback, PVOID pvCallbackContext, PVOID pvContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfExportCallback", "pvCallbackContext", "pvContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RemoveUsersFromEncryptedFile(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] RemoveUsersFromEncryptedFile(LPCWSTR lpFileName, PENCRYPTION_CERTIFICATE_HASH_LIST pHashes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "pHashes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetUserFileEncryptionKey(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] SetUserFileEncryptionKey(PENCRYPTION_CERTIFICATE pEncryptionCertificate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pEncryptionCertificate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_WriteEncryptedFileRaw(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] WriteEncryptedFileRaw(PFE_IMPORT_FUNC pfImportCallback, PVOID pvCallbackContext, PVOID pvContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfImportCallback", "pvCallbackContext", "pvContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CreateProcessAsUser(jitter):
    """"
    [Advapi32.dll] BOOL CreateProcessAsUser(HANDLE hToken, LPCTSTR lpApplicationName, LPTSTR lpCommandLine, LPSECURITY_ATTRIBUTES lpProcessAttributes, LPSECURITY_ATTRIBUTES lpThreadAttributes, BOOL bInheritHandles, [CreateProcessFlags] dwCreationFlags, LPVOID lpEnvironment, LPCTSTR lpCurrentDirectory, LPSTARTUPINFO lpStartupInfo, LPPROCESS_INFORMATION lpProcessInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hToken", "lpApplicationName", "lpCommandLine", "lpProcessAttributes", "lpThreadAttributes", "bInheritHandles", "dwCreationFlags", "lpEnvironment", "lpCurrentDirectory", "lpStartupInfo", "lpProcessInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CreateProcessWithLogonW(jitter):
    """"
    [Advapi32.dll] BOOL CreateProcessWithLogonW(LPCWSTR lpUsername, LPCWSTR lpDomain, LPCWSTR lpPassword, [LogonFlags] dwLogonFlags, LPCWSTR lpApplicationName, LPWSTR lpCommandLine, [CreateProcessFlags] dwCreationFlags, LPVOID lpEnvironment, LPCWSTR lpCurrentDirectory, LPSTARTUPINFOW lpStartupInfo, LPPROCESS_INFORMATION lpProcessInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpUsername", "lpDomain", "lpPassword", "dwLogonFlags", "lpApplicationName", "lpCommandLine", "dwCreationFlags", "lpEnvironment", "lpCurrentDirectory", "lpStartupInfo", "lpProcessInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CreateProcessWithTokenW(jitter):
    """"
    [Advapi32.dll] BOOL CreateProcessWithTokenW(HANDLE hToken, [LogonFlags] dwLogonFlags, LPCWSTR lpApplicationName, LPWSTR lpCommandLine, [CreateProcessFlags] dwCreationFlags, LPVOID lpEnvironment, LPCWSTR lpCurrentDirectory, LPSTARTUPINFOW lpStartupInfo, LPPROCESS_INFORMATION lpProcessInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hToken", "dwLogonFlags", "lpApplicationName", "lpCommandLine", "dwCreationFlags", "lpEnvironment", "lpCurrentDirectory", "lpStartupInfo", "lpProcessInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetLocalManagedApplications(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] GetLocalManagedApplications(BOOL bUserApps, LPDWORD pdwApps, PLOCALMANAGEDAPPLICATION* prgLocalApps)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bUserApps", "pdwApps", "prgLocalApps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetManagedApplications(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] GetManagedApplications(GUID* pCategory, DWORD dwQueryFlags, DWORD dwInfoLevel, LPDWORD pdwApps, PMANAGEDAPPLICATION* prgManagedApps)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCategory", "dwQueryFlags", "dwInfoLevel", "pdwApps", "prgManagedApps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetManagedApplicationCategories(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] GetManagedApplicationCategories(DWORD dwReserved, APPCATEGORYINFOLIST* pAppCategory)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwReserved", "pAppCategory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_InstallApplication(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] InstallApplication(PINSTALLDATA* pInstallInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pInstallInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_UninstallApplication(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] UninstallApplication(WCHAR* ProductCode, DWORD dwStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProductCode", "dwStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AbortSystemShutdown(jitter):
    """"
    [Advapi32.dll] BOOL AbortSystemShutdown(LPTSTR lpMachineName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMachineName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_InitiateShutdown(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] InitiateShutdown(LPTSTR lpMachineName, LPTSTR lpMessage, DWORD dwGracePeriod, [SHUTDOWN_FLAGS] dwShutdownFlags, [SHTDN_REASON] dwReason)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMachineName", "lpMessage", "dwGracePeriod", "dwShutdownFlags", "dwReason"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_InitiateSystemShutdown(jitter):
    """"
    [Advapi32.dll] BOOL InitiateSystemShutdown(LPTSTR lpMachineName, LPTSTR lpMessage, DWORD dwTimeout, BOOL bForceAppsClosed, BOOL bRebootAfterShutdown)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMachineName", "lpMessage", "dwTimeout", "bForceAppsClosed", "bRebootAfterShutdown"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_InitiateSystemShutdownEx(jitter):
    """"
    [Advapi32.dll] BOOL InitiateSystemShutdownEx(LPTSTR lpMachineName, LPTSTR lpMessage, DWORD dwTimeout, BOOL bForceAppsClosed, BOOL bRebootAfterShutdown, [SHTDN_REASON] dwReason)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMachineName", "lpMessage", "dwTimeout", "bForceAppsClosed", "bRebootAfterShutdown", "dwReason"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_BackupEventLog(jitter):
    """"
    [Advapi32.dll] BOOL BackupEventLog(HANDLE hEventLog, LPCTSTR lpBackupFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEventLog", "lpBackupFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ClearEventLog(jitter):
    """"
    [Advapi32.dll] BOOL ClearEventLog(HANDLE hEventLog, LPCTSTR lpBackupFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEventLog", "lpBackupFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CloseEventLog(jitter):
    """"
    [Advapi32.dll] BOOL CloseEventLog(HANDLE hEventLog)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEventLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_DeregisterEventSource(jitter):
    """"
    [Advapi32.dll] BOOL DeregisterEventSource(HANDLE hEventLog)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEventLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetEventLogInformation(jitter):
    """"
    [Advapi32.dll] BOOL GetEventLogInformation(HANDLE hEventLog, DWORD dwInfoLevel, LPVOID lpBuffer, DWORD cbBufSize, LPDWORD pcbBytesNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEventLog", "dwInfoLevel", "lpBuffer", "cbBufSize", "pcbBytesNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetNumberOfEventLogRecords(jitter):
    """"
    [Advapi32.dll] BOOL GetNumberOfEventLogRecords(HANDLE hEventLog, PDWORD NumberOfRecords)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEventLog", "NumberOfRecords"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetOldestEventLogRecord(jitter):
    """"
    [Advapi32.dll] BOOL GetOldestEventLogRecord(HANDLE hEventLog, PDWORD OldestRecord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEventLog", "OldestRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_NotifyChangeEventLog(jitter):
    """"
    [Advapi32.dll] BOOL NotifyChangeEventLog(HANDLE hEventLog, HANDLE hEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEventLog", "hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_OpenBackupEventLog(jitter):
    """"
    [Advapi32.dll] HANDLE OpenBackupEventLog(LPCTSTR lpUNCServerName, LPCTSTR lpFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpUNCServerName", "lpFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_OpenEventLog(jitter):
    """"
    [Advapi32.dll] HANDLE OpenEventLog(LPCTSTR lpUNCServerName, LPCTSTR lpSourceName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpUNCServerName", "lpSourceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ReadEventLog(jitter):
    """"
    [Advapi32.dll] BOOL ReadEventLog(HANDLE hEventLog, DWORD dwReadFlags, DWORD dwRecordOffset, LPVOID lpBuffer, DWORD nNumberOfBytesToRead, DWORD* pnBytesRead, DWORD* pnMinNumberOfBytesNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEventLog", "dwReadFlags", "dwRecordOffset", "lpBuffer", "nNumberOfBytesToRead", "pnBytesRead", "pnMinNumberOfBytesNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegisterEventSource(jitter):
    """"
    [Advapi32.dll] HANDLE RegisterEventSource(LPCTSTR lpUNCServerName, LPCTSTR lpSourceName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpUNCServerName", "lpSourceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ReportEvent(jitter):
    """"
    [Advapi32.dll] BOOL ReportEvent(HANDLE hEventLog, [EventLogType] wType, WORD wCategory, DWORD dwEventID, PSID lpUserSid, WORD wNumStrings, DWORD dwDataSize, LPCTSTR* lpStrings, LPVOID lpRawData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEventLog", "wType", "wCategory", "dwEventID", "lpUserSid", "wNumStrings", "dwDataSize", "lpStrings", "lpRawData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfCreateInstance(jitter):
    """"
    [Advapi32.dll] PPERF_COUNTERSET_INSTANCE PerfCreateInstance(HANDLE hProvider, LPCGUID CounterSetGuid, LPCWSTR szInstanceName, ULONG dwInstance)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "CounterSetGuid", "szInstanceName", "dwInstance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfDecrementULongCounterValue(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] PerfDecrementULongCounterValue(HANDLE hProvider, PPERF_COUNTERSET_INSTANCE pInstance, ULONG CounterId, ULONG lValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pInstance", "CounterId", "lValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfDecrementULongLongCounterValue(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] PerfDecrementULongLongCounterValue(HANDLE hProvider, PPERF_COUNTERSET_INSTANCE pInstance, ULONG CounterId, ULONGLONG llValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pInstance", "CounterId", "llValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfDeleteInstance(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] PerfDeleteInstance(HANDLE hProvider, PPERF_COUNTERSET_INSTANCE InstanceBlock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "InstanceBlock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfIncrementULongCounterValue(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] PerfIncrementULongCounterValue(HANDLE hProvider, PPERF_COUNTERSET_INSTANCE pInstance, ULONG CounterId, ULONG lValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pInstance", "CounterId", "lValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfIncrementULongLongCounterValue(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] PerfIncrementULongLongCounterValue(HANDLE hProvider, PPERF_COUNTERSET_INSTANCE pInstance, ULONG CounterId, ULONGLONG llValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pInstance", "CounterId", "llValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfQueryInstance(jitter):
    """"
    [Advapi32.dll] PPERF_COUNTERSET_INSTANCE PerfQueryInstance(HANDLE hProvider, LPCGUID CounterSetGuid, LPCWSTR szInstance, ULONG dwInstance)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "CounterSetGuid", "szInstance", "dwInstance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfSetCounterSetInfo(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] PerfSetCounterSetInfo(HANDLE hProvider, PPERF_COUNTERSET_INFO pTemplate, ULONG dwTemplateSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pTemplate", "dwTemplateSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfSetULongCounterValue(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] PerfSetULongCounterValue(HANDLE hProvider, PPERF_COUNTERSET_INSTANCE pInstance, ULONG CounterId, ULONG lValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pInstance", "CounterId", "lValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfSetULongLongCounterValue(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] PerfSetULongLongCounterValue(HANDLE hProvider, PPERF_COUNTERSET_INSTANCE pInstance, ULONG CounterId, ULONGLONG llValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pInstance", "CounterId", "llValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfSetCounterRefValue(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] PerfSetCounterRefValue(HANDLE hProvider, PPERF_COUNTERSET_INSTANCE pInstance, ULONG CounterId, PVOID lpAddr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pInstance", "CounterId", "lpAddr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfStartProvider(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] PerfStartProvider(LPGUID ProviderGuid, PERFLIBREQUEST ControlCallback, HANDLE* phProvider)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProviderGuid", "ControlCallback", "phProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfStartProviderEx(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] PerfStartProviderEx(LPGUID ProviderGuid, PPERF_PROVIDER_CONTEXT ProviderContext, HANDLE* phProvider)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProviderGuid", "ProviderContext", "phProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PerfStopProvider(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] PerfStopProvider(HANDLE hProvider)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegisterServiceCtrlHandler(jitter):
    """"
    [Advapi32.dll] SERVICE_STATUS_HANDLE RegisterServiceCtrlHandler(LPCTSTR lpServiceName, LPHANDLER_FUNCTION lpHandlerProc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpServiceName", "lpHandlerProc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegisterServiceCtrlHandlerEx(jitter):
    """"
    [Advapi32.dll] SERVICE_STATUS_HANDLE RegisterServiceCtrlHandlerEx(LPCTSTR lpServiceName, LPHANDLER_FUNCTION_EX lpHandlerProc, LPVOID lpContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpServiceName", "lpHandlerProc", "lpContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetServiceBits(jitter):
    """"
    [Advapi32.dll] BOOL SetServiceBits(SERVICE_STATUS_HANDLE hServiceStatus, DWORD dwServiceBits, BOOL bSetBitsOn, BOOL bUpdateImmediately)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServiceStatus", "dwServiceBits", "bSetBitsOn", "bUpdateImmediately"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetServiceStatus(jitter):
    """"
    [Advapi32.dll] BOOL SetServiceStatus(SERVICE_STATUS_HANDLE hServiceStatus, LPSERVICE_STATUS lpServiceStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServiceStatus", "lpServiceStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_StartServiceCtrlDispatcher(jitter):
    """"
    [Advapi32.dll] BOOL StartServiceCtrlDispatcher(const SERVICE_TABLE_ENTRY* lpServiceTable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpServiceTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ChangeServiceConfig(jitter):
    """"
    [Advapi32.dll] BOOL ChangeServiceConfig(SC_HANDLE hService, [ServiceType] dwServiceType, [ServiceStartType] dwStartType, [ServiceErrorControl] dwErrorControl, LPCTSTR lpBinaryPathName, LPCTSTR lpLoadOrderGroup, LPDWORD lpdwTagId, LPCTSTR lpDependencies, LPCTSTR lpServiceStartName, LPCTSTR lpPassword, LPCTSTR lpDisplayName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "dwServiceType", "dwStartType", "dwErrorControl", "lpBinaryPathName", "lpLoadOrderGroup", "lpdwTagId", "lpDependencies", "lpServiceStartName", "lpPassword", "lpDisplayName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ChangeServiceConfig2(jitter):
    """"
    [Advapi32.dll] BOOL ChangeServiceConfig2(SC_HANDLE hService, [ServiceInfoLevel] dwInfoLevel, LPVOID lpInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "dwInfoLevel", "lpInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CloseServiceHandle(jitter):
    """"
    [Advapi32.dll] BOOL CloseServiceHandle(SC_HANDLE hSCObject)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSCObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ControlService(jitter):
    """"
    [Advapi32.dll] BOOL ControlService(SC_HANDLE hService, [ServiceControl] dwControl, LPSERVICE_STATUS lpServiceStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "dwControl", "lpServiceStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ControlServiceEx(jitter):
    """"
    [Advapi32.dll] BOOL ControlServiceEx(SC_HANDLE hService, DWORD dwControl, DWORD dwInfoLevel, PVOID pControlParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "dwControl", "dwInfoLevel", "pControlParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CreateService(jitter):
    """"
    [Advapi32.dll] SC_HANDLE CreateService(SC_HANDLE hSCManager, LPCTSTR lpServiceName, LPCTSTR lpDisplayName, [ServiceAccess] dwDesiredAccess, [ServiceType] dwServiceType, [ServiceStartType] dwStartType, [ServiceErrorControl] dwErrorControl, LPCTSTR lpBinaryPathName, LPCTSTR lpLoadOrderGroup, LPDWORD lpdwTagId, LPCTSTR lpDependencies, LPCTSTR lpServiceStartName, LPCTSTR lpPassword)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSCManager", "lpServiceName", "lpDisplayName", "dwDesiredAccess", "dwServiceType", "dwStartType", "dwErrorControl", "lpBinaryPathName", "lpLoadOrderGroup", "lpdwTagId", "lpDependencies", "lpServiceStartName", "lpPassword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_DeleteService(jitter):
    """"
    [Advapi32.dll] BOOL DeleteService(SC_HANDLE hService)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EnumDependentServices(jitter):
    """"
    [Advapi32.dll] BOOL EnumDependentServices(SC_HANDLE hService, [ServiceState] dwServiceState, LPENUM_SERVICE_STATUS lpServices, DWORD cbBufSize, LPDWORD pcbBytesNeeded, LPDWORD lpServicesReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "dwServiceState", "lpServices", "cbBufSize", "pcbBytesNeeded", "lpServicesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EnumServicesStatusEx(jitter):
    """"
    [Advapi32.dll] BOOL EnumServicesStatusEx(SC_HANDLE hSCManager, SC_ENUM_TYPE InfoLevel, [ServiceType] dwServiceType, [ServiceState] dwServiceState, LPBYTE lpServices, DWORD cbBufSize, LPDWORD pcbBytesNeeded, LPDWORD lpServicesReturned, LPDWORD lpResumeHandle, LPCTSTR pszGroupName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSCManager", "InfoLevel", "dwServiceType", "dwServiceState", "lpServices", "cbBufSize", "pcbBytesNeeded", "lpServicesReturned", "lpResumeHandle", "pszGroupName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetServiceDisplayName(jitter):
    """"
    [Advapi32.dll] BOOL GetServiceDisplayName(SC_HANDLE hSCManager, LPCTSTR lpServiceName, LPTSTR lpDisplayName, LPDWORD lpcchBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSCManager", "lpServiceName", "lpDisplayName", "lpcchBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetServiceKeyName(jitter):
    """"
    [Advapi32.dll] BOOL GetServiceKeyName(SC_HANDLE hSCManager, LPCTSTR lpDisplayName, LPTSTR lpServiceName, LPDWORD lpcchBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSCManager", "lpDisplayName", "lpServiceName", "lpcchBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_NotifyBootConfigStatus(jitter):
    """"
    [Advapi32.dll] BOOL NotifyBootConfigStatus(BOOL BootAcceptable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BootAcceptable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_NotifyServiceStatusChange(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] NotifyServiceStatusChange(SC_HANDLE hService, [ServiceNotifyMask] dwNotifyMask, PSERVICE_NOTIFYA pNotifyBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "dwNotifyMask", "pNotifyBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_NotifyServiceStatusChange(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] NotifyServiceStatusChange(SC_HANDLE hService, [ServiceNotifyMask] dwNotifyMask, PSERVICE_NOTIFY pNotifyBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "dwNotifyMask", "pNotifyBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_OpenSCManager(jitter):
    """"
    [Advapi32.dll] SC_HANDLE OpenSCManager(LPCTSTR lpMachineName, LPCTSTR lpDatabaseName, [SCManagerAccess] dwDesiredAccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpMachineName", "lpDatabaseName", "dwDesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_OpenService(jitter):
    """"
    [Advapi32.dll] SC_HANDLE OpenService(SC_HANDLE hSCManager, LPCTSTR lpServiceName, [ServiceAccess] dwDesiredAccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSCManager", "lpServiceName", "dwDesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_QueryServiceConfig(jitter):
    """"
    [Advapi32.dll] BOOL QueryServiceConfig(SC_HANDLE hService, LPQUERY_SERVICE_CONFIG lpServiceConfig, DWORD cbBufSize, LPDWORD pcbBytesNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "lpServiceConfig", "cbBufSize", "pcbBytesNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_QueryServiceConfig2(jitter):
    """"
    [Advapi32.dll] BOOL QueryServiceConfig2(SC_HANDLE hService, [ServiceInfoLevel] dwInfoLevel, LPBYTE lpBuffer, DWORD cbBufSize, LPDWORD pcbBytesNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "dwInfoLevel", "lpBuffer", "cbBufSize", "pcbBytesNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_QueryServiceDynamicInformation(jitter):
    """"
    [Advapi32.dll] BOOL QueryServiceDynamicInformation(SERVICE_STATUS_HANDLE hServiceStatus, DWORD dwInfoLevel, PVOID* ppDynamicInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServiceStatus", "dwInfoLevel", "ppDynamicInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_QueryServiceStatus(jitter):
    """"
    [Advapi32.dll] BOOL QueryServiceStatus(SC_HANDLE hService, LPSERVICE_STATUS lpServiceStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "lpServiceStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_QueryServiceStatusEx(jitter):
    """"
    [Advapi32.dll] BOOL QueryServiceStatusEx(SC_HANDLE hService, SC_STATUS_TYPE InfoLevel, LPBYTE lpBuffer, DWORD cbBufSize, LPDWORD pcbBytesNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "InfoLevel", "lpBuffer", "cbBufSize", "pcbBytesNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_StartService(jitter):
    """"
    [Advapi32.dll] BOOL StartService(SC_HANDLE hService, DWORD dwNumServiceArgs, LPCTSTR* lpServiceArgVectors)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "dwNumServiceArgs", "lpServiceArgVectors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EnumServicesStatus(jitter):
    """"
    [Advapi32.dll] BOOL EnumServicesStatus(SC_HANDLE hSCManager, [ServiceType] dwServiceType, [ServiceState] dwServiceState, LPENUM_SERVICE_STATUS lpServices, DWORD cbBufSize, LPDWORD pcbBytesNeeded, LPDWORD lpServicesReturned, LPDWORD lpResumeHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSCManager", "dwServiceType", "dwServiceState", "lpServices", "cbBufSize", "pcbBytesNeeded", "lpServicesReturned", "lpResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LockServiceDatabase(jitter):
    """"
    [Advapi32.dll] SC_LOCK LockServiceDatabase(SC_HANDLE hSCManager)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSCManager"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_QueryServiceLockStatus(jitter):
    """"
    [Advapi32.dll] BOOL QueryServiceLockStatus(SC_HANDLE hSCManager, LPQUERY_SERVICE_LOCK_STATUS lpLockStatus, DWORD cbBufSize, LPDWORD pcbBytesNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSCManager", "lpLockStatus", "cbBufSize", "pcbBytesNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_UnlockServiceDatabase(jitter):
    """"
    [Advapi32.dll] BOOL UnlockServiceDatabase(SC_LOCK ScLock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ScLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetCurrentHwProfile(jitter):
    """"
    [Advapi32.dll] BOOL GetCurrentHwProfile(LPHW_PROFILE_INFO lpHwProfileInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpHwProfileInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetUserName(jitter):
    """"
    [Advapi32.dll] BOOL GetUserName(LPTSTR lpBuffer, LPDWORD lpnSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpBuffer", "lpnSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_IsTextUnicode(jitter):
    """"
    [Advapi32.dll] BOOL IsTextUnicode(const VOID* lpv, int iSize, [IsTextUnicodeFlags*] lpiResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpv", "iSize", "lpiResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptAcquireContext(jitter):
    """"
    [Advapi32.dll] BOOL CryptAcquireContext(HCRYPTPROV* phProv, LPCTSTR pszContainer, LPCTSTR pszProvider, [CryptProv] dwProvType, [CryptAcquireContextFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phProv", "pszContainer", "pszProvider", "dwProvType", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptContextAddRef(jitter):
    """"
    [Advapi32.dll] BOOL CryptContextAddRef(HCRYPTPROV hProv, DWORD* pdwReserved, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProv", "pdwReserved", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptEnumProviders(jitter):
    """"
    [Advapi32.dll] BOOL CryptEnumProviders(DWORD dwIndex, DWORD* pdwReserved, DWORD dwFlags, [CryptProv*] pdwProvType, LPTSTR pszProvName, DWORD* pcbProvName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwIndex", "pdwReserved", "dwFlags", "pdwProvType", "pszProvName", "pcbProvName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptEnumProviderTypes(jitter):
    """"
    [Advapi32.dll] BOOL CryptEnumProviderTypes(DWORD dwIndex, DWORD* pdwReserved, DWORD dwFlags, [CryptProv*] pdwProvType, LPTSTR pszTypeName, DWORD* pcbTypeName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwIndex", "pdwReserved", "dwFlags", "pdwProvType", "pszTypeName", "pcbTypeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptGetDefaultProvider(jitter):
    """"
    [Advapi32.dll] BOOL CryptGetDefaultProvider([CryptProv] dwProvType, DWORD* pdwReserved, DWORD dwFlags, LPTSTR pszProvName, DWORD* pcbProvName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwProvType", "pdwReserved", "dwFlags", "pszProvName", "pcbProvName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptGetProvParam(jitter):
    """"
    [Advapi32.dll] BOOL CryptGetProvParam(HCRYPTPROV hProv, [CryptGetProvParam] dwParam, BYTE* pbData, DWORD* pdwDataLen, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProv", "dwParam", "pbData", "pdwDataLen", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptReleaseContext(jitter):
    """"
    [Advapi32.dll] BOOL CryptReleaseContext(HCRYPTPROV hProv, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProv", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptSetProvider(jitter):
    """"
    [Advapi32.dll] BOOL CryptSetProvider(LPCTSTR pszProvName, [CryptProv] dwProvType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszProvName", "dwProvType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptSetProviderEx(jitter):
    """"
    [Advapi32.dll] BOOL CryptSetProviderEx(LPCTSTR pszProvName, [CryptProv] dwProvType, DWORD* pdwReserved, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszProvName", "dwProvType", "pdwReserved", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptSetProvParam(jitter):
    """"
    [Advapi32.dll] BOOL CryptSetProvParam(HCRYPTPROV hProv, [CryptSetProvParam] dwParam, const BYTE* pbData, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProv", "dwParam", "pbData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptDeriveKey(jitter):
    """"
    [Advapi32.dll] BOOL CryptDeriveKey(HCRYPTPROV hProv, ALG_ID Algid, HCRYPTHASH hBaseData, DWORD dwFlags, HCRYPTKEY* phKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProv", "Algid", "hBaseData", "dwFlags", "phKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptDestroyKey(jitter):
    """"
    [Advapi32.dll] BOOL CryptDestroyKey(HCRYPTKEY hKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptDuplicateKey(jitter):
    """"
    [Advapi32.dll] BOOL CryptDuplicateKey(HCRYPTKEY hKey, DWORD* pdwReserved, DWORD dwFlags, HCRYPTKEY* phKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "pdwReserved", "dwFlags", "phKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptExportKey(jitter):
    """"
    [Advapi32.dll] BOOL CryptExportKey(HCRYPTKEY hKey, HCRYPTKEY hExpKey, [CryptBlobType] dwBlobType, [CryptExportKeyFlags] dwFlags, BYTE* pbData, DWORD* pdwDataLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "hExpKey", "dwBlobType", "dwFlags", "pbData", "pdwDataLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptGenKey(jitter):
    """"
    [Advapi32.dll] BOOL CryptGenKey(HCRYPTPROV hProv, ALG_ID Algid, DWORD dwFlags, HCRYPTKEY* phKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProv", "Algid", "dwFlags", "phKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptGenRandom(jitter):
    """"
    [Advapi32.dll] BOOL CryptGenRandom(HCRYPTPROV hProv, DWORD dwLen, BYTE* pbBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProv", "dwLen", "pbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptGetKeyParam(jitter):
    """"
    [Advapi32.dll] BOOL CryptGetKeyParam(HCRYPTKEY hKey, [CryptKeyParam] dwParam, BYTE* pbData, DWORD* pdwDataLen, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "dwParam", "pbData", "pdwDataLen", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptGetUserKey(jitter):
    """"
    [Advapi32.dll] BOOL CryptGetUserKey(HCRYPTPROV hProv, [CryptKeySpec] dwKeySpec, HCRYPTKEY* phUserKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProv", "dwKeySpec", "phUserKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptImportKey(jitter):
    """"
    [Advapi32.dll] BOOL CryptImportKey(HCRYPTPROV hProv, BYTE* pbData, DWORD dwDataLen, HCRYPTKEY hPubKey, [CryptImportKeyFlags] dwFlags, HCRYPTKEY* phKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProv", "pbData", "dwDataLen", "hPubKey", "dwFlags", "phKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptSetKeyParam(jitter):
    """"
    [Advapi32.dll] BOOL CryptSetKeyParam(HCRYPTKEY hKey, [CryptKeyParam] dwParam, const BYTE* pbData, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "dwParam", "pbData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptDecrypt(jitter):
    """"
    [Advapi32.dll] BOOL CryptDecrypt(HCRYPTKEY hKey, HCRYPTHASH hHash, BOOL Final, DWORD dwFlags, BYTE* pbData, DWORD* pdwDataLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "hHash", "Final", "dwFlags", "pbData", "pdwDataLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptEncrypt(jitter):
    """"
    [Advapi32.dll] BOOL CryptEncrypt(HCRYPTKEY hKey, HCRYPTHASH hHash, BOOL Final, DWORD dwFlags, BYTE* pbData, DWORD* pdwDataLen, DWORD dwBufLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "hHash", "Final", "dwFlags", "pbData", "pdwDataLen", "dwBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptCreateHash(jitter):
    """"
    [Advapi32.dll] BOOL CryptCreateHash(HCRYPTPROV hProv, ALG_ID Algid, HCRYPTKEY hKey, [CryptCreateHashFlags] dwFlags, HCRYPTHASH* phHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProv", "Algid", "hKey", "dwFlags", "phHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptDestroyHash(jitter):
    """"
    [Advapi32.dll] BOOL CryptDestroyHash(HCRYPTHASH hHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptDuplicateHash(jitter):
    """"
    [Advapi32.dll] BOOL CryptDuplicateHash(HCRYPTHASH hHash, DWORD* pdwReserved, DWORD dwFlags, HCRYPTHASH* phHash)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHash", "pdwReserved", "dwFlags", "phHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptGetHashParam(jitter):
    """"
    [Advapi32.dll] BOOL CryptGetHashParam(HCRYPTHASH hHash, [CryptHashParam] dwParam, BYTE* pbData, DWORD* pdwDataLen, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHash", "dwParam", "pbData", "pdwDataLen", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptHashData(jitter):
    """"
    [Advapi32.dll] BOOL CryptHashData(HCRYPTHASH hHash, BYTE* pbData, DWORD dwDataLen, [CryptHashDataFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHash", "pbData", "dwDataLen", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptHashSessionKey(jitter):
    """"
    [Advapi32.dll] BOOL CryptHashSessionKey(HCRYPTHASH hHash, HCRYPTKEY hKey, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHash", "hKey", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptSetHashParam(jitter):
    """"
    [Advapi32.dll] BOOL CryptSetHashParam(HCRYPTHASH hHash, [CryptHashParam] dwParam, const BYTE* pbData, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHash", "dwParam", "pbData", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptSignHash(jitter):
    """"
    [Advapi32.dll] BOOL CryptSignHash(HCRYPTHASH hHash, [CryptKeySpec] dwKeySpec, LPCTSTR sDescription, [CryptSignFlags] dwFlags, BYTE* pbSignature, DWORD* pdwSigLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHash", "dwKeySpec", "sDescription", "dwFlags", "pbSignature", "pdwSigLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CryptVerifySignature(jitter):
    """"
    [Advapi32.dll] BOOL CryptVerifySignature(HCRYPTHASH hHash, BYTE* pbSignature, DWORD dwSigLen, HCRYPTKEY hPubKey, LPCTSTR sDescription, [CryptSignFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hHash", "pbSignature", "dwSigLen", "hPubKey", "sDescription", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ControlTrace(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] ControlTrace(TRACEHANDLE SessionHandle, LPCTSTR SessionName, PEVENT_TRACE_PROPERTIES Properties, ULONG ControlCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "SessionName", "Properties", "ControlCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EnableTrace(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EnableTrace(ULONG Enable, ULONG EnableFlag, ULONG EnableLevel, LPCGUID ControlGuid, TRACEHANDLE SessionHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Enable", "EnableFlag", "EnableLevel", "ControlGuid", "SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EnableTraceEx(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EnableTraceEx(LPCGUID ProviderId, LPCGUID SourceId, TRACEHANDLE TraceHandle, ULONG IsEnabled, UCHAR Level, ULONGLONG MatchAnyKeyword, ULONGLONG MatchAllKeyword, ULONG EnableProperty, PEVENT_FILTER_DESCRIPTOR EnableFilterDesc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProviderId", "SourceId", "TraceHandle", "IsEnabled", "Level", "MatchAnyKeyword", "MatchAllKeyword", "EnableProperty", "EnableFilterDesc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EnableTraceEx2(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EnableTraceEx2(TRACEHANDLE TraceHandle, LPCGUID ProviderId, ULONG ControlCode, UCHAR Level, ULONGLONG MatchAnyKeyword, ULONGLONG MatchAllKeyword, ULONG Timeout, PENABLE_TRACE_PARAMETERS EnableParameters)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TraceHandle", "ProviderId", "ControlCode", "Level", "MatchAnyKeyword", "MatchAllKeyword", "Timeout", "EnableParameters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EnumerateTraceGuids(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EnumerateTraceGuids(PTRACE_GUID_PROPERTIES* GuidPropertiesArray, ULONG PropertyArrayCount, PULONG GuidCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["GuidPropertiesArray", "PropertyArrayCount", "GuidCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EnumerateTraceGuidsEx(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EnumerateTraceGuidsEx(TRACE_QUERY_INFO_CLASS TraceQueryInfoClass, PVOID InBuffer, ULONG InBufferSize, PVOID OutBuffer, ULONG OutBufferSize, PULONG ReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TraceQueryInfoClass", "InBuffer", "InBufferSize", "OutBuffer", "OutBufferSize", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_FlushTrace(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] FlushTrace(TRACEHANDLE SessionHandle, LPCTSTR SessionName, PEVENT_TRACE_PROPERTIES Properties)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "SessionName", "Properties"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_QueryAllTraces(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] QueryAllTraces(PEVENT_TRACE_PROPERTIES* PropertyArray, ULONG PropertyArrayCount, PULONG SessionCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PropertyArray", "PropertyArrayCount", "SessionCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_QueryTrace(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] QueryTrace(TRACEHANDLE SessionHandle, LPCTSTR SessionName, PEVENT_TRACE_PROPERTIES Properties)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "SessionName", "Properties"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_StartTrace(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] StartTrace(PTRACEHANDLE SessionHandle, LPCTSTR SessionName, PEVENT_TRACE_PROPERTIES Properties)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "SessionName", "Properties"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_StopTrace(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] StopTrace(TRACEHANDLE SessionHandle, LPCTSTR SessionName, PEVENT_TRACE_PROPERTIES Properties)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "SessionName", "Properties"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_TraceQueryInformation(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] TraceQueryInformation(TRACEHANDLE SessionHandle, TRACE_QUERY_INFO_CLASS InformationClass, PVOID TraceInformation, ULONG InformationLength, PULONG ReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "InformationClass", "TraceInformation", "InformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_TraceSetInformation(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] TraceSetInformation(TRACEHANDLE SessionHandle, TRACE_INFO_CLASS InformationClass, PVOID TraceInformation, ULONG InformationLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "InformationClass", "TraceInformation", "InformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_UpdateTrace(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] UpdateTrace(TRACEHANDLE SessionHandle, LPCTSTR SessionName, PEVENT_TRACE_PROPERTIES Properties)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "SessionName", "Properties"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CreateTraceInstanceId(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] CreateTraceInstanceId(HANDLE RegHandle, PEVENT_INSTANCE_INFO pInstInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegHandle", "pInstInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetTraceEnableFlags(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] GetTraceEnableFlags(TRACEHANDLE SessionHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetTraceEnableLevel(jitter):
    """"
    [Advapi32.dll] UCHAR GetTraceEnableLevel(TRACEHANDLE SessionHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetTraceLoggerHandle(jitter):
    """"
    [Advapi32.dll] TRACEHANDLE GetTraceLoggerHandle(PVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegisterTraceGuids(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] RegisterTraceGuids(WMIDPREQUEST RequestAddress, PVOID RequestContext, LPCGUID ControlGuid, ULONG GuidCount, PTRACE_GUID_REGISTRATION TraceGuidReg, LPCTSTR MofImagePath, LPCTSTR MofResourceName, PTRACEHANDLE RegistrationHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RequestAddress", "RequestContext", "ControlGuid", "GuidCount", "TraceGuidReg", "MofImagePath", "MofResourceName", "RegistrationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_TraceEvent(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] TraceEvent(TRACEHANDLE SessionHandle, PEVENT_TRACE_HEADER EventTrace)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "EventTrace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_TraceEventInstance(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] TraceEventInstance(TRACEHANDLE SessionHandle, PEVENT_INSTANCE_HEADER EventTrace, PEVENT_INSTANCE_INFO pInstInfo, PEVENT_INSTANCE_INFO pParentInstInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "EventTrace", "pInstInfo", "pParentInstInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_TraceMessage(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] TraceMessage(TRACEHANDLE SessionHandle, [TRACE_MESSAGE_FLAGS] MessageFlags, LPGUID MessageGuid, USHORT MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "MessageFlags", "MessageGuid", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_TraceMessageVa(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] TraceMessageVa(TRACEHANDLE SessionHandle, ULONG MessageFlags, LPGUID MessageGuid, USHORT MessageNumber, va_list MessageArgList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "MessageFlags", "MessageGuid", "MessageNumber", "MessageArgList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_UnregisterTraceGuids(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] UnregisterTraceGuids(TRACEHANDLE RegistrationHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegistrationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EventActivityIdControl(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EventActivityIdControl([EventActivity] ControlCode, LPGUID ActivityId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ControlCode", "ActivityId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EventEnabled(jitter):
    """"
    [Advapi32.dll] BOOLEAN EventEnabled(REGHANDLE RegHandle, PCEVENT_DESCRIPTOR EventDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegHandle", "EventDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EventProviderEnabled(jitter):
    """"
    [Advapi32.dll] BOOLEAN EventProviderEnabled(REGHANDLE RegHandle, UCHAR Level, ULONGLONG Keyword)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegHandle", "Level", "Keyword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EventRegister(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EventRegister(LPCGUID ProviderId, ENABLECALLBACK EnableCallback, PVOID CallbackContext, PREGHANDLE RegHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProviderId", "EnableCallback", "CallbackContext", "RegHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EventSetInformation(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EventSetInformation(REGHANDLE RegHandle, EVENT_INFO_CLASS InformationClass, PVOID EventInformation, ULONG InformationLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegHandle", "InformationClass", "EventInformation", "InformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EventUnregister(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EventUnregister(REGHANDLE RegHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EventWrite(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EventWrite(REGHANDLE RegHandle, PCEVENT_DESCRIPTOR EventDescriptor, ULONG UserDataCount, PEVENT_DATA_DESCRIPTOR UserData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegHandle", "EventDescriptor", "UserDataCount", "UserData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EventWriteEx(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EventWriteEx(REGHANDLE RegHandle, PCEVENT_DESCRIPTOR EventDescriptor, ULONG64 Filter, ULONG Flags, LPCGUID ActivityId, LPCGUID RelatedActivityId, ULONG UserDataCount, PEVENT_DATA_DESCRIPTOR UserData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegHandle", "EventDescriptor", "Filter", "Flags", "ActivityId", "RelatedActivityId", "UserDataCount", "UserData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EventWriteString(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EventWriteString(REGHANDLE RegHandle, UCHAR Level, ULONGLONG Keyword, PCWSTR String)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegHandle", "Level", "Keyword", "String"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EventWriteTransfer(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EventWriteTransfer(REGHANDLE RegHandle, PCEVENT_DESCRIPTOR EventDescriptor, LPCGUID ActivityId, LPCGUID RelatedActivityId, ULONG UserDataCount, PEVENT_DATA_DESCRIPTOR UserData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegHandle", "EventDescriptor", "ActivityId", "RelatedActivityId", "UserDataCount", "UserData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CloseTrace(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] CloseTrace(TRACEHANDLE TraceHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TraceHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_OpenTrace(jitter):
    """"
    [Advapi32.dll] TRACEHANDLE OpenTrace(PEVENT_TRACE_LOGFILE Logfile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Logfile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ProcessTrace(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] ProcessTrace(PTRACEHANDLE HandleArray, ULONG HandleCount, LPFILETIME StartTime, LPFILETIME EndTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HandleArray", "HandleCount", "StartTime", "EndTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RemoveTraceCallback(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] RemoveTraceCallback(LPCGUID pGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetTraceCallback(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] SetTraceCallback(LPCGUID pGuid, PEVENT_CALLBACK EventCallback)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pGuid", "EventCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EventAccessControl(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EventAccessControl(LPGUID Guid, ULONG Operation, PSID Sid, ULONG Rights, BOOLEAN AllowOrDeny)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Guid", "Operation", "Sid", "Rights", "AllowOrDeny"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EventAccessQuery(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EventAccessQuery(LPGUID Guid, PSECURITY_DESCRIPTOR Buffer, PULONG BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Guid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EventAccessRemove(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] EventAccessRemove(LPGUID Guid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Guid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AccessCheck(jitter):
    """"
    [Advapi32.dll] BOOL AccessCheck(PSECURITY_DESCRIPTOR pSecurityDescriptor, HANDLE ClientToken, DWORD DesiredAccess, PGENERIC_MAPPING GenericMapping, PPRIVILEGE_SET PrivilegeSet, LPDWORD PrivilegeSetLength, LPDWORD GrantedAccess, LPBOOL AccessStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "ClientToken", "DesiredAccess", "GenericMapping", "PrivilegeSet", "PrivilegeSetLength", "GrantedAccess", "AccessStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AccessCheckByType(jitter):
    """"
    [Advapi32.dll] BOOL AccessCheckByType(PSECURITY_DESCRIPTOR pSecurityDescriptor, PSID PrincipalSelfSid, HANDLE ClientToken, DWORD DesiredAccess, POBJECT_TYPE_LIST ObjectTypeList, DWORD ObjectTypeListLength, PGENERIC_MAPPING GenericMapping, PPRIVILEGE_SET PrivilegeSet, LPDWORD PrivilegeSetLength, LPDWORD GrantedAccess, LPBOOL AccessStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "PrincipalSelfSid", "ClientToken", "DesiredAccess", "ObjectTypeList", "ObjectTypeListLength", "GenericMapping", "PrivilegeSet", "PrivilegeSetLength", "GrantedAccess", "AccessStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AccessCheckByTypeResultList(jitter):
    """"
    [Advapi32.dll] BOOL AccessCheckByTypeResultList(PSECURITY_DESCRIPTOR pSecurityDescriptor, PSID PrincipalSelfSid, HANDLE ClientToken, DWORD DesiredAccess, POBJECT_TYPE_LIST ObjectTypeList, DWORD ObjectTypeListLength, PGENERIC_MAPPING GenericMapping, PPRIVILEGE_SET PrivilegeSet, LPDWORD PrivilegeSetLength, LPDWORD GrantedAccessList, LPDWORD AccessStatusList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "PrincipalSelfSid", "ClientToken", "DesiredAccess", "ObjectTypeList", "ObjectTypeListLength", "GenericMapping", "PrivilegeSet", "PrivilegeSetLength", "GrantedAccessList", "AccessStatusList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AdjustTokenGroups(jitter):
    """"
    [Advapi32.dll] BOOL AdjustTokenGroups(HANDLE TokenHandle, BOOL ResetToDefault, PTOKEN_GROUPS NewState, DWORD BufferLength, PTOKEN_GROUPS PreviousState, PDWORD ReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TokenHandle", "ResetToDefault", "NewState", "BufferLength", "PreviousState", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AdjustTokenPrivileges(jitter):
    """"
    [Advapi32.dll] BOOL AdjustTokenPrivileges(HANDLE TokenHandle, BOOL DisableAllPrivileges, PTOKEN_PRIVILEGES NewState, DWORD BufferLength, PTOKEN_PRIVILEGES PreviousState, PDWORD ReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TokenHandle", "DisableAllPrivileges", "NewState", "BufferLength", "PreviousState", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AllocateAndInitializeSid(jitter):
    """"
    [Advapi32.dll] BOOL AllocateAndInitializeSid(PSID_IDENTIFIER_AUTHORITY pIdentifierAuthority, BYTE nSubAuthorityCount, DWORD dwSubAuthority0, DWORD dwSubAuthority1, DWORD dwSubAuthority2, DWORD dwSubAuthority3, DWORD dwSubAuthority4, DWORD dwSubAuthority5, DWORD dwSubAuthority6, DWORD dwSubAuthority7, PSID* pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pIdentifierAuthority", "nSubAuthorityCount", "dwSubAuthority0", "dwSubAuthority1", "dwSubAuthority2", "dwSubAuthority3", "dwSubAuthority4", "dwSubAuthority5", "dwSubAuthority6", "dwSubAuthority7", "pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AllocateLocallyUniqueId(jitter):
    """"
    [Advapi32.dll] BOOL AllocateLocallyUniqueId(PLUID Luid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Luid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_BuildExplicitAccessWithName(jitter):
    """"
    [Advapi32.dll] VOID BuildExplicitAccessWithName(PEXPLICIT_ACCESS pExplicitAccess, LPTSTR pTrusteeName, DWORD AccessPermissions, ACCESS_MODE AccessMode, [AceFlags] Inheritance)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pExplicitAccess", "pTrusteeName", "AccessPermissions", "AccessMode", "Inheritance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_BuildImpersonateExplicitAccessWithName(jitter):
    """"
    [Advapi32.dll] VOID BuildImpersonateExplicitAccessWithName(PEXPLICIT_ACCESS pExplicitAccess, LPTSTR pTrusteeName, PTRUSTEE pTrustee, DWORD AccessPermissions, ACCESS_MODE AccessMode, [AceFlags] Inheritance)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pExplicitAccess", "pTrusteeName", "pTrustee", "AccessPermissions", "AccessMode", "Inheritance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_BuildImpersonateTrustee(jitter):
    """"
    [Advapi32.dll] VOID BuildImpersonateTrustee(PTRUSTEE pTrustee, PTRUSTEE pImpersonateTrustee)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTrustee", "pImpersonateTrustee"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_BuildTrusteeWithName(jitter):
    """"
    [Advapi32.dll] VOID BuildTrusteeWithName(PTRUSTEE pTrustee, LPTSTR pName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTrustee", "pName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_BuildTrusteeWithObjectsAndName(jitter):
    """"
    [Advapi32.dll] void BuildTrusteeWithObjectsAndName(PTRUSTEE pTrustee, POBJECTS_AND_NAME pObjName, SE_OBJECT_TYPE ObjectType, LPTSTR ObjectTypeName, LPTSTR InheritedObjectTypeName, LPTSTR Name)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTrustee", "pObjName", "ObjectType", "ObjectTypeName", "InheritedObjectTypeName", "Name"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_BuildTrusteeWithObjectsAndSid(jitter):
    """"
    [Advapi32.dll] void BuildTrusteeWithObjectsAndSid(PTRUSTEE pTrustee, POBJECTS_AND_SID pObjSid, GUID* pObjectGuid, GUID* pInheritedObjectGuid, PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTrustee", "pObjSid", "pObjectGuid", "pInheritedObjectGuid", "pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_BuildTrusteeWithSid(jitter):
    """"
    [Advapi32.dll] VOID BuildTrusteeWithSid(PTRUSTEE pTrustee, PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTrustee", "pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CheckTokenMembership(jitter):
    """"
    [Advapi32.dll] BOOL CheckTokenMembership(HANDLE TokenHandle, PSID SidToCheck, PBOOL IsMember)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TokenHandle", "SidToCheck", "IsMember"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ConvertSecurityDescriptorToStringSecurityDescriptor(jitter):
    """"
    [Advapi32.dll] BOOL ConvertSecurityDescriptorToStringSecurityDescriptor(PSECURITY_DESCRIPTOR SecurityDescriptor, DWORD RequestedStringSDRevision, SECURITY_INFORMATION SecurityInformation, LPTSTR* StringSecurityDescriptor, PULONG StringSecurityDescriptorLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "RequestedStringSDRevision", "SecurityInformation", "StringSecurityDescriptor", "StringSecurityDescriptorLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ConvertSidToStringSid(jitter):
    """"
    [Advapi32.dll] BOOL ConvertSidToStringSid(PSID Sid, LPTSTR* StringSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Sid", "StringSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ConvertStringSecurityDescriptorToSecurityDescriptor(jitter):
    """"
    [Advapi32.dll] BOOL ConvertStringSecurityDescriptorToSecurityDescriptor(LPCTSTR StringSecurityDescriptor, DWORD StringSDRevision, PSECURITY_DESCRIPTOR* SecurityDescriptor, PULONG SecurityDescriptorSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["StringSecurityDescriptor", "StringSDRevision", "SecurityDescriptor", "SecurityDescriptorSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ConvertStringSidToSid(jitter):
    """"
    [Advapi32.dll] BOOL ConvertStringSidToSid(LPCTSTR StringSid, PSID* Sid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["StringSid", "Sid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CopySid(jitter):
    """"
    [Advapi32.dll] BOOL CopySid(DWORD nDestinationSidLength, PSID pDestinationSid, PSID pSourceSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nDestinationSidLength", "pDestinationSid", "pSourceSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CreateRestrictedToken(jitter):
    """"
    [Advapi32.dll] BOOL CreateRestrictedToken(HANDLE ExistingTokenHandle, [CreateRestrictedTokenFlags] Flags, DWORD DisableSidCount, PSID_AND_ATTRIBUTES SidsToDisable, DWORD DeletePrivilegeCount, PLUID_AND_ATTRIBUTES PrivilegesToDelete, DWORD RestrictedSidCount, PSID_AND_ATTRIBUTES SidsToRestrict, PHANDLE NewTokenHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExistingTokenHandle", "Flags", "DisableSidCount", "SidsToDisable", "DeletePrivilegeCount", "PrivilegesToDelete", "RestrictedSidCount", "SidsToRestrict", "NewTokenHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CreateWellKnownSid(jitter):
    """"
    [Advapi32.dll] BOOL CreateWellKnownSid(WELL_KNOWN_SID_TYPE WellKnownSidType, PSID DomainSid, PSID pSid, DWORD* cbSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["WellKnownSidType", "DomainSid", "pSid", "cbSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_DuplicateToken(jitter):
    """"
    [Advapi32.dll] BOOL DuplicateToken(HANDLE ExistingTokenHandle, SECURITY_IMPERSONATION_LEVEL ImpersonationLevel, PHANDLE DuplicateTokenHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExistingTokenHandle", "ImpersonationLevel", "DuplicateTokenHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_DuplicateTokenEx(jitter):
    """"
    [Advapi32.dll] BOOL DuplicateTokenEx(HANDLE hExistingToken, [TOKEN_ACCESS_MASK_DWORD] dwDesiredAccess, LPSECURITY_ATTRIBUTES lpTokenAttributes, SECURITY_IMPERSONATION_LEVEL ImpersonationLevel, TOKEN_TYPE TokenType, PHANDLE phNewToken)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hExistingToken", "dwDesiredAccess", "lpTokenAttributes", "ImpersonationLevel", "TokenType", "phNewToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EqualDomainSid(jitter):
    """"
    [Advapi32.dll] BOOL EqualDomainSid(PSID pSid1, PSID pSid2, BOOL* pfEqual)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid1", "pSid2", "pfEqual"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EqualPrefixSid(jitter):
    """"
    [Advapi32.dll] BOOL EqualPrefixSid(PSID pSid1, PSID pSid2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid1", "pSid2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_EqualSid(jitter):
    """"
    [Advapi32.dll] BOOL EqualSid(PSID pSid1, PSID pSid2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid1", "pSid2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_FreeSid(jitter):
    """"
    [Advapi32.dll] PVOID FreeSid(PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetAuditedPermissionsFromAcl(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] GetAuditedPermissionsFromAcl(PACL pacl, PTRUSTEE pTrustee, PACCESS_MASK pSuccessfulAuditedRights, PACCESS_MASK pFailedAuditRights)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pacl", "pTrustee", "pSuccessfulAuditedRights", "pFailedAuditRights"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetEffectiveRightsFromAcl(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] GetEffectiveRightsFromAcl(PACL pacl, PTRUSTEE pTrustee, PACCESS_MASK pAccessRights)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pacl", "pTrustee", "pAccessRights"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetExplicitEntriesFromAcl(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] GetExplicitEntriesFromAcl(PACL pacl, PULONG pcCountOfExplicitEntries, PEXPLICIT_ACCESS* pListOfExplicitEntries)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pacl", "pcCountOfExplicitEntries", "pListOfExplicitEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetLengthSid(jitter):
    """"
    [Advapi32.dll] DWORD GetLengthSid(PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetMultipleTrustee(jitter):
    """"
    [Advapi32.dll] PTRUSTEE GetMultipleTrustee(PTRUSTEE pTrustee)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTrustee"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetMultipleTrusteeOperation(jitter):
    """"
    [Advapi32.dll] MULTIPLE_TRUSTEE_OPERATION GetMultipleTrusteeOperation(PTRUSTEE pTrustee)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTrustee"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetNamedSecurityInfo(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] GetNamedSecurityInfo(LPTSTR pObjectName, SE_OBJECT_TYPE ObjectType, SECURITY_INFORMATION SecurityInfo, PSID* ppsidOwner, PSID* ppsidGroup, PACL* ppDacl, PACL* ppSacl, PSECURITY_DESCRIPTOR_RELATIVE* ppSecurityDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pObjectName", "ObjectType", "SecurityInfo", "ppsidOwner", "ppsidGroup", "ppDacl", "ppSacl", "ppSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetSecurityDescriptorControl(jitter):
    """"
    [Advapi32.dll] BOOL GetSecurityDescriptorControl(PSECURITY_DESCRIPTOR pSecurityDescriptor, PSECURITY_DESCRIPTOR_CONTROL pControl, LPDWORD lpdwRevision)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "pControl", "lpdwRevision"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetSecurityInfo(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] GetSecurityInfo(HANDLE handle, SE_OBJECT_TYPE ObjectType, SECURITY_INFORMATION SecurityInfo, PSID* ppsidOwner, PSID* ppsidGroup, PACL* ppDacl, PACL* ppSacl, PSECURITY_DESCRIPTOR* ppSecurityDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["handle", "ObjectType", "SecurityInfo", "ppsidOwner", "ppsidGroup", "ppDacl", "ppSacl", "ppSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetSidIdentifierAuthority(jitter):
    """"
    [Advapi32.dll] PSID_IDENTIFIER_AUTHORITY GetSidIdentifierAuthority(PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetSidLengthRequired(jitter):
    """"
    [Advapi32.dll] DWORD GetSidLengthRequired(UCHAR nSubAuthorityCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nSubAuthorityCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetSidSubAuthority(jitter):
    """"
    [Advapi32.dll] PDWORD GetSidSubAuthority(PSID pSid, DWORD nSubAuthority)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid", "nSubAuthority"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetSidSubAuthorityCount(jitter):
    """"
    [Advapi32.dll] PUCHAR GetSidSubAuthorityCount(PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetTokenInformation(jitter):
    """"
    [Advapi32.dll] BOOL GetTokenInformation(HANDLE TokenHandle, TOKEN_INFORMATION_CLASS TokenInformationClass, LPVOID TokenInformation, DWORD TokenInformationLength, PDWORD ReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TokenHandle", "TokenInformationClass", "TokenInformation", "TokenInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetTrusteeForm(jitter):
    """"
    [Advapi32.dll] TRUSTEE_FORM GetTrusteeForm(PTRUSTEE pTrustee)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTrustee"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetTrusteeName(jitter):
    """"
    [Advapi32.dll] LPTSTR GetTrusteeName(PTRUSTEE pTrustee)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTrustee"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetTrusteeType(jitter):
    """"
    [Advapi32.dll] TRUSTEE_TYPE GetTrusteeType(PTRUSTEE pTrustee)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTrustee"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetWindowsAccountDomainSid(jitter):
    """"
    [Advapi32.dll] BOOL GetWindowsAccountDomainSid(PSID pSid, PSID ppDomainSid, DWORD* cbSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid", "ppDomainSid", "cbSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_InitializeSid(jitter):
    """"
    [Advapi32.dll] BOOL InitializeSid(PSID Sid, PSID_IDENTIFIER_AUTHORITY pIdentifierAuthority, BYTE nSubAuthorityCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Sid", "pIdentifierAuthority", "nSubAuthorityCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_IsTokenRestricted(jitter):
    """"
    [Advapi32.dll] BOOL IsTokenRestricted(HANDLE TokenHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TokenHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_IsValidSid(jitter):
    """"
    [Advapi32.dll] BOOL IsValidSid(PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_IsWellKnownSid(jitter):
    """"
    [Advapi32.dll] BOOL IsWellKnownSid(PSID pSid, WELL_KNOWN_SID_TYPE WellKnownSidType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid", "WellKnownSidType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LookupAccountName(jitter):
    """"
    [Advapi32.dll] BOOL LookupAccountName(LPCTSTR lpSystemName, LPCTSTR lpAccountName, PSID Sid, LPDWORD cbSid, LPTSTR ReferencedDomainName, LPDWORD cchReferencedDomainName, PSID_NAME_USE peUse)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemName", "lpAccountName", "Sid", "cbSid", "ReferencedDomainName", "cchReferencedDomainName", "peUse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LookupAccountSid(jitter):
    """"
    [Advapi32.dll] BOOL LookupAccountSid(LPCTSTR lpSystemName, PSID lpSid, LPTSTR lpName, LPDWORD cchName, LPTSTR lpReferencedDomainName, LPDWORD cchReferencedDomainName, PSID_NAME_USE peUse)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemName", "lpSid", "lpName", "cchName", "lpReferencedDomainName", "cchReferencedDomainName", "peUse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LookupPrivilegeDisplayName(jitter):
    """"
    [Advapi32.dll] BOOL LookupPrivilegeDisplayName(LPCTSTR lpSystemName, LPCTSTR lpName, LPTSTR lpDisplayName, LPDWORD cchDisplayName, LPDWORD lpLanguageId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemName", "lpName", "lpDisplayName", "cchDisplayName", "lpLanguageId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LookupPrivilegeName(jitter):
    """"
    [Advapi32.dll] BOOL LookupPrivilegeName(LPCTSTR lpSystemName, PLUID lpLuid, LPTSTR lpName, LPDWORD cchName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemName", "lpLuid", "lpName", "cchName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LookupPrivilegeValue(jitter):
    """"
    [Advapi32.dll] BOOL LookupPrivilegeValue(LPCTSTR lpSystemName, LPCTSTR lpName, PLUID lpLuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemName", "lpName", "lpLuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_OpenProcessToken(jitter):
    """"
    [Advapi32.dll] BOOL OpenProcessToken([ProcessHandle] ProcessHandle, [TOKEN_ACCESS_MASK_DWORD] DesiredAccess, PHANDLE TokenHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "DesiredAccess", "TokenHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_OpenThreadToken(jitter):
    """"
    [Advapi32.dll] BOOL OpenThreadToken([ThreadHandle] ThreadHandle, [TOKEN_ACCESS_MASK_DWORD] DesiredAccess, BOOL OpenAsSelf, PHANDLE TokenHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "DesiredAccess", "OpenAsSelf", "TokenHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_QuerySecurityAccessMask(jitter):
    """"
    [Advapi32.dll] VOID QuerySecurityAccessMask(SECURITY_INFORMATION SecurityInformation, LPDWORD DesiredAccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SecurityInformation", "DesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetEntriesInAcl(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] SetEntriesInAcl(ULONG cCountOfExplicitEntries, PEXPLICIT_ACCESS pListOfExplicitEntries, PACL OldAcl, PACL* NewAcl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cCountOfExplicitEntries", "pListOfExplicitEntries", "OldAcl", "NewAcl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetNamedSecurityInfo(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] SetNamedSecurityInfo(LPTSTR pObjectName, SE_OBJECT_TYPE ObjectType, SECURITY_INFORMATION SecurityInfo, PSID psidOwner, PSID psidGroup, PACL pDacl, PACL pSacl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pObjectName", "ObjectType", "SecurityInfo", "psidOwner", "psidGroup", "pDacl", "pSacl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetSecurityAccessMask(jitter):
    """"
    [Advapi32.dll] VOID SetSecurityAccessMask(SECURITY_INFORMATION SecurityInformation, LPDWORD DesiredAccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SecurityInformation", "DesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetSecurityDescriptorControl(jitter):
    """"
    [Advapi32.dll] BOOL SetSecurityDescriptorControl(PSECURITY_DESCRIPTOR pSecurityDescriptor, SECURITY_DESCRIPTOR_CONTROL ControlBitsOfInterest, SECURITY_DESCRIPTOR_CONTROL ControlBitsToSet)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "ControlBitsOfInterest", "ControlBitsToSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetSecurityInfo(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] SetSecurityInfo(HANDLE handle, SE_OBJECT_TYPE ObjectType, SECURITY_INFORMATION SecurityInfo, PSID psidOwner, PSID psidGroup, PACL pDacl, PACL pSacl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["handle", "ObjectType", "SecurityInfo", "psidOwner", "psidGroup", "pDacl", "pSacl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetThreadToken(jitter):
    """"
    [Advapi32.dll] BOOL SetThreadToken(PHANDLE Thread, HANDLE Token)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Thread", "Token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetTokenInformation(jitter):
    """"
    [Advapi32.dll] BOOL SetTokenInformation(HANDLE TokenHandle, TOKEN_INFORMATION_CLASS TokenInformationClass, LPVOID TokenInformation, DWORD TokenInformationLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TokenHandle", "TokenInformationClass", "TokenInformation", "TokenInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_TreeResetNamedSecurityInfo(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] TreeResetNamedSecurityInfo(LPTSTR pObjectName, SE_OBJECT_TYPE ObjectType, SECURITY_INFORMATION SecurityInfo, PSID pOwner, PSID pGroup, PACL pDacl, PACL pSacl, BOOL KeepExplicit, FN_PROGRESS fnProgress, PROG_INVOKE_SETTING ProgressInvokeSetting, PVOID Args)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pObjectName", "ObjectType", "SecurityInfo", "pOwner", "pGroup", "pDacl", "pSacl", "KeepExplicit", "fnProgress", "ProgressInvokeSetting", "Args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_TreeSetNamedSecurityInfo(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] TreeSetNamedSecurityInfo(LPTSTR pObjectName, SE_OBJECT_TYPE ObjectType, SECURITY_INFORMATION SecurityInfo, PSID pOwner, PSID pGroup, PACL pDacl, PACL pSacl, [TreeSecAction] dwAction, FN_PROGRESS fnProgress, PROG_INVOKE_SETTING ProgressInvokeSetting, PVOID Args)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pObjectName", "ObjectType", "SecurityInfo", "pOwner", "pGroup", "pDacl", "pSacl", "dwAction", "fnProgress", "ProgressInvokeSetting", "Args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AreAllAccessesGranted(jitter):
    """"
    [Advapi32.dll] BOOL AreAllAccessesGranted(DWORD GrantedAccess, DWORD DesiredAccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["GrantedAccess", "DesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AreAnyAccessesGranted(jitter):
    """"
    [Advapi32.dll] BOOL AreAnyAccessesGranted(DWORD GrantedAccess, DWORD DesiredAccess)
    """"
    ret_ad, args = jitter.func_args_stdcall(["GrantedAccess", "DesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_BuildSecurityDescriptor(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] BuildSecurityDescriptor(PTRUSTEE pOwner, PTRUSTEE pGroup, ULONG cCountOfAccessEntries, PEXPLICIT_ACCESS pListOfAccessEntries, ULONG cCountOfAuditEntries, PEXPLICIT_ACCESS pListOfAuditEntries, PSECURITY_DESCRIPTOR pOldSD, PULONG pSizeNewSD, PSECURITY_DESCRIPTOR* pNewSD)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pOwner", "pGroup", "cCountOfAccessEntries", "pListOfAccessEntries", "cCountOfAuditEntries", "pListOfAuditEntries", "pOldSD", "pSizeNewSD", "pNewSD"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ConvertToAutoInheritPrivateObjectSecurity(jitter):
    """"
    [Advapi32.dll] BOOL ConvertToAutoInheritPrivateObjectSecurity(PSECURITY_DESCRIPTOR ParentDescriptor, PSECURITY_DESCRIPTOR CurrentSecurityDescriptor, PSECURITY_DESCRIPTOR* NewSecurityDescriptor, GUID* ObjectType, BOOLEAN IsDirectoryObject, PGENERIC_MAPPING GenericMapping)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ParentDescriptor", "CurrentSecurityDescriptor", "NewSecurityDescriptor", "ObjectType", "IsDirectoryObject", "GenericMapping"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CreatePrivateObjectSecurity(jitter):
    """"
    [Advapi32.dll] BOOL CreatePrivateObjectSecurity(PSECURITY_DESCRIPTOR ParentDescriptor, PSECURITY_DESCRIPTOR CreatorDescriptor, PSECURITY_DESCRIPTOR* NewDescriptor, BOOL IsDirectoryObject, HANDLE Token, PGENERIC_MAPPING GenericMapping)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ParentDescriptor", "CreatorDescriptor", "NewDescriptor", "IsDirectoryObject", "Token", "GenericMapping"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CreatePrivateObjectSecurityEx(jitter):
    """"
    [Advapi32.dll] BOOL CreatePrivateObjectSecurityEx(PSECURITY_DESCRIPTOR ParentDescriptor, PSECURITY_DESCRIPTOR CreatorDescriptor, PSECURITY_DESCRIPTOR* NewDescriptor, GUID* ObjectType, BOOL IsContainerObject, [SEF_Flags] AutoInheritFlags, HANDLE Token, PGENERIC_MAPPING GenericMapping)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ParentDescriptor", "CreatorDescriptor", "NewDescriptor", "ObjectType", "IsContainerObject", "AutoInheritFlags", "Token", "GenericMapping"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CreatePrivateObjectSecurityWithMultipleInheritance(jitter):
    """"
    [Advapi32.dll] BOOL CreatePrivateObjectSecurityWithMultipleInheritance(PSECURITY_DESCRIPTOR ParentDescriptor, PSECURITY_DESCRIPTOR CreatorDescriptor, PSECURITY_DESCRIPTOR* NewDescriptor, GUID** ObjectTypes, ULONG GuidCount, BOOL IsContainerObject, [SEF_Flags] AutoInheritFlags, HANDLE Token, PGENERIC_MAPPING GenericMapping)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ParentDescriptor", "CreatorDescriptor", "NewDescriptor", "ObjectTypes", "GuidCount", "IsContainerObject", "AutoInheritFlags", "Token", "GenericMapping"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_DestroyPrivateObjectSecurity(jitter):
    """"
    [Advapi32.dll] BOOL DestroyPrivateObjectSecurity(PSECURITY_DESCRIPTOR* ObjectDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ObjectDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetPrivateObjectSecurity(jitter):
    """"
    [Advapi32.dll] BOOL GetPrivateObjectSecurity(PSECURITY_DESCRIPTOR ObjectDescriptor, SECURITY_INFORMATION SecurityInformation, PSECURITY_DESCRIPTOR ResultantDescriptor, DWORD DescriptorLength, PDWORD ReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ObjectDescriptor", "SecurityInformation", "ResultantDescriptor", "DescriptorLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ImpersonateAnonymousToken(jitter):
    """"
    [Advapi32.dll] BOOL ImpersonateAnonymousToken([ThreadHandle] ThreadHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ImpersonateLoggedOnUser(jitter):
    """"
    [Advapi32.dll] BOOL ImpersonateLoggedOnUser(HANDLE hToken)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ImpersonateNamedPipeClient(jitter):
    """"
    [Advapi32.dll] BOOL ImpersonateNamedPipeClient(HANDLE hNamedPipe)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hNamedPipe"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ImpersonateSelf(jitter):
    """"
    [Advapi32.dll] BOOL ImpersonateSelf(SECURITY_IMPERSONATION_LEVEL ImpersonationLevel)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ImpersonationLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LookupSecurityDescriptorParts(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] LookupSecurityDescriptorParts(PTRUSTEE* pOwner, PTRUSTEE* pGroup, PULONG cCountOfAccessEntries, PEXPLICIT_ACCESS* pListOfAccessEntries, PULONG cCountOfAuditEntries, PEXPLICIT_ACCESS* pListOfAuditEntries, PSECURITY_DESCRIPTOR pSD)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pOwner", "pGroup", "cCountOfAccessEntries", "pListOfAccessEntries", "cCountOfAuditEntries", "pListOfAuditEntries", "pSD"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_MapGenericMask(jitter):
    """"
    [Advapi32.dll] VOID MapGenericMask(PDWORD AccessMask, PGENERIC_MAPPING GenericMapping)
    """"
    ret_ad, args = jitter.func_args_stdcall(["AccessMask", "GenericMapping"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ObjectCloseAuditAlarm(jitter):
    """"
    [Advapi32.dll] BOOL ObjectCloseAuditAlarm(LPCTSTR SubsystemName, LPVOID HandleId, BOOL GenerateOnClose)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "GenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ObjectDeleteAuditAlarm(jitter):
    """"
    [Advapi32.dll] BOOL ObjectDeleteAuditAlarm(LPCTSTR SubsystemName, LPVOID HandleId, BOOL GenerateOnClose)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "GenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ObjectOpenAuditAlarm(jitter):
    """"
    [Advapi32.dll] BOOL ObjectOpenAuditAlarm(LPCTSTR SubsystemName, LPVOID HandleId, LPTSTR ObjectTypeName, LPTSTR ObjectName, PSECURITY_DESCRIPTOR pSecurityDescriptor, HANDLE ClientToken, DWORD DesiredAccess, DWORD GrantedAccess, PPRIVILEGE_SET Privileges, BOOL ObjectCreation, BOOL AccessGranted, LPBOOL GenerateOnClose)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "ObjectTypeName", "ObjectName", "pSecurityDescriptor", "ClientToken", "DesiredAccess", "GrantedAccess", "Privileges", "ObjectCreation", "AccessGranted", "GenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_ObjectPrivilegeAuditAlarm(jitter):
    """"
    [Advapi32.dll] BOOL ObjectPrivilegeAuditAlarm(LPCTSTR SubsystemName, LPVOID HandleId, HANDLE ClientToken, DWORD DesiredAccess, PPRIVILEGE_SET Privileges, BOOL AccessGranted)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "ClientToken", "DesiredAccess", "Privileges", "AccessGranted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PrivilegeCheck(jitter):
    """"
    [Advapi32.dll] BOOL PrivilegeCheck(HANDLE ClientToken, PPRIVILEGE_SET RequiredPrivileges, LPBOOL pfResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClientToken", "RequiredPrivileges", "pfResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_PrivilegedServiceAuditAlarm(jitter):
    """"
    [Advapi32.dll] BOOL PrivilegedServiceAuditAlarm(LPCTSTR SubsystemName, LPCTSTR ServiceName, HANDLE ClientToken, PPRIVILEGE_SET Privileges, BOOL AccessGranted)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "ServiceName", "ClientToken", "Privileges", "AccessGranted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RevertToSelf(jitter):
    """"
    [Advapi32.dll] BOOL RevertToSelf()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetPrivateObjectSecurity(jitter):
    """"
    [Advapi32.dll] BOOL SetPrivateObjectSecurity(SECURITY_INFORMATION SecurityInformation, PSECURITY_DESCRIPTOR ModificationDescriptor, PSECURITY_DESCRIPTOR* ObjectsSecurityDescriptor, PGENERIC_MAPPING GenericMapping, HANDLE Token)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SecurityInformation", "ModificationDescriptor", "ObjectsSecurityDescriptor", "GenericMapping", "Token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetPrivateObjectSecurityEx(jitter):
    """"
    [Advapi32.dll] BOOL SetPrivateObjectSecurityEx(SECURITY_INFORMATION SecurityInformation, PSECURITY_DESCRIPTOR ModificationDescriptor, PSECURITY_DESCRIPTOR* ObjectsSecurityDescriptor, [SEF_Flags] AutoInheritFlags, PGENERIC_MAPPING GenericMapping, HANDLE Token)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SecurityInformation", "ModificationDescriptor", "ObjectsSecurityDescriptor", "AutoInheritFlags", "GenericMapping", "Token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetSecurityDescriptorRMControl(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] GetSecurityDescriptorRMControl(PSECURITY_DESCRIPTOR SecurityDescriptor, PUCHAR RMControl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "RMControl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetSecurityDescriptorRMControl(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] SetSecurityDescriptorRMControl(PSECURITY_DESCRIPTOR SecurityDescriptor, PUCHAR RMControl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "RMControl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AccessCheckAndAuditAlarm(jitter):
    """"
    [Advapi32.dll] BOOL AccessCheckAndAuditAlarm(LPCTSTR SubsystemName, LPVOID HandleId, LPTSTR ObjectTypeName, LPTSTR ObjectName, PSECURITY_DESCRIPTOR SecurityDescriptor, DWORD DesiredAccess, PGENERIC_MAPPING GenericMapping, BOOL ObjectCreation, LPDWORD GrantedAccess, LPBOOL AccessStatus, LPBOOL pfGenerateOnClose)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "ObjectTypeName", "ObjectName", "SecurityDescriptor", "DesiredAccess", "GenericMapping", "ObjectCreation", "GrantedAccess", "AccessStatus", "pfGenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AccessCheckByTypeAndAuditAlarm(jitter):
    """"
    [Advapi32.dll] BOOL AccessCheckByTypeAndAuditAlarm(LPCTSTR SubsystemName, LPVOID HandleId, LPCTSTR ObjectTypeName, LPCTSTR ObjectName, PSECURITY_DESCRIPTOR pSecurityDescriptor, PSID PrincipalSelfSid, DWORD DesiredAccess, AUDIT_EVENT_TYPE AuditType, DWORD Flags, POBJECT_TYPE_LIST ObjectTypeList, DWORD ObjectTypeListLength, PGENERIC_MAPPING GenericMapping, BOOL ObjectCreation, LPDWORD GrantedAccess, LPBOOL AccessStatus, LPBOOL pfGenerateOnClose)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "ObjectTypeName", "ObjectName", "pSecurityDescriptor", "PrincipalSelfSid", "DesiredAccess", "AuditType", "Flags", "ObjectTypeList", "ObjectTypeListLength", "GenericMapping", "ObjectCreation", "GrantedAccess", "AccessStatus", "pfGenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AccessCheckByTypeResultListAndAuditAlarm(jitter):
    """"
    [Advapi32.dll] BOOL AccessCheckByTypeResultListAndAuditAlarm(LPCTSTR SubsystemName, LPVOID HandleId, LPCTSTR ObjectTypeName, LPCTSTR ObjectName, PSECURITY_DESCRIPTOR pSecurityDescriptor, PSID PrincipalSelfSid, DWORD DesiredAccess, AUDIT_EVENT_TYPE AuditType, DWORD Flags, POBJECT_TYPE_LIST ObjectTypeList, DWORD ObjectTypeListLength, PGENERIC_MAPPING GenericMapping, BOOL ObjectCreation, LPDWORD GrantedAccess, LPDWORD AccessStatusList, LPBOOL pfGenerateOnClose)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "ObjectTypeName", "ObjectName", "pSecurityDescriptor", "PrincipalSelfSid", "DesiredAccess", "AuditType", "Flags", "ObjectTypeList", "ObjectTypeListLength", "GenericMapping", "ObjectCreation", "GrantedAccess", "AccessStatusList", "pfGenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AccessCheckByTypeResultListAndAuditAlarmByHandle(jitter):
    """"
    [Advapi32.dll] BOOL AccessCheckByTypeResultListAndAuditAlarmByHandle(LPCTSTR SubsystemName, LPVOID HandleId, HANDLE ClientToken, LPCTSTR ObjectTypeName, LPCTSTR ObjectName, PSECURITY_DESCRIPTOR pSecurityDescriptor, PSID PrincipalSelfSid, DWORD DesiredAccess, AUDIT_EVENT_TYPE AuditType, DWORD Flags, POBJECT_TYPE_LIST ObjectTypeList, DWORD ObjectTypeListLength, PGENERIC_MAPPING GenericMapping, BOOL ObjectCreation, LPDWORD GrantedAccess, LPDWORD AccessStatusList, LPBOOL pfGenerateOnClose)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "ClientToken", "ObjectTypeName", "ObjectName", "pSecurityDescriptor", "PrincipalSelfSid", "DesiredAccess", "AuditType", "Flags", "ObjectTypeList", "ObjectTypeListLength", "GenericMapping", "ObjectCreation", "GrantedAccess", "AccessStatusList", "pfGenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AddAccessAllowedAce(jitter):
    """"
    [Advapi32.dll] BOOL AddAccessAllowedAce(PACL pAcl, DWORD dwAceRevision, [ACCESS_MASK_DWORD] AccessMask, PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AccessMask", "pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AddAccessAllowedAceEx(jitter):
    """"
    [Advapi32.dll] BOOL AddAccessAllowedAceEx(PACL pAcl, DWORD dwAceRevision, [AceFlags] AceFlags, [ACCESS_MASK_DWORD] AccessMask, PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AceFlags", "AccessMask", "pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AddAccessAllowedObjectAce(jitter):
    """"
    [Advapi32.dll] BOOL AddAccessAllowedObjectAce(PACL pAcl, DWORD dwAceRevision, [AceFlags] AceFlags, [ACCESS_MASK_DWORD] AccessMask, GUID* ObjectTypeGuid, GUID* InheritedObjectTypeGuid, PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AceFlags", "AccessMask", "ObjectTypeGuid", "InheritedObjectTypeGuid", "pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AddAccessDeniedAce(jitter):
    """"
    [Advapi32.dll] BOOL AddAccessDeniedAce(PACL pAcl, DWORD dwAceRevision, [ACCESS_MASK_DWORD] AccessMask, PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AccessMask", "pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AddAccessDeniedAceEx(jitter):
    """"
    [Advapi32.dll] BOOL AddAccessDeniedAceEx(PACL pAcl, DWORD dwAceRevision, [AceFlags] AceFlags, [ACCESS_MASK_DWORD] AccessMask, PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AceFlags", "AccessMask", "pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AddAccessDeniedObjectAce(jitter):
    """"
    [Advapi32.dll] BOOL AddAccessDeniedObjectAce(PACL pAcl, DWORD dwAceRevision, [AceFlags] AceFlags, [ACCESS_MASK_DWORD] AccessMask, GUID* ObjectTypeGuid, GUID* InheritedObjectTypeGuid, PSID pSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AceFlags", "AccessMask", "ObjectTypeGuid", "InheritedObjectTypeGuid", "pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AddAce(jitter):
    """"
    [Advapi32.dll] BOOL AddAce(PACL pAcl, DWORD dwAceRevision, DWORD dwStartingAceIndex, LPVOID pAceList, DWORD nAceListLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "dwStartingAceIndex", "pAceList", "nAceListLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AddAuditAccessAce(jitter):
    """"
    [Advapi32.dll] BOOL AddAuditAccessAce(PACL pAcl, DWORD dwAceRevision, [ACCESS_MASK_DWORD] dwAccessMask, PSID pSid, BOOL bAuditSuccess, BOOL bAuditFailure)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "dwAccessMask", "pSid", "bAuditSuccess", "bAuditFailure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AddAuditAccessAceEx(jitter):
    """"
    [Advapi32.dll] BOOL AddAuditAccessAceEx(PACL pAcl, DWORD dwAceRevision, [AceFlags] AceFlags, [ACCESS_MASK_DWORD] dwAccessMask, PSID pSid, BOOL bAuditSuccess, BOOL bAuditFailure)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AceFlags", "dwAccessMask", "pSid", "bAuditSuccess", "bAuditFailure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AddAuditAccessObjectAce(jitter):
    """"
    [Advapi32.dll] BOOL AddAuditAccessObjectAce(PACL pAcl, DWORD dwAceRevision, [AceFlags] AceFlags, [ACCESS_MASK_DWORD] AccessMask, GUID* ObjectTypeGuid, GUID* InheritedObjectTypeGuid, PSID pSid, BOOL bAuditSuccess, BOOL bAuditFailure)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AceFlags", "AccessMask", "ObjectTypeGuid", "InheritedObjectTypeGuid", "pSid", "bAuditSuccess", "bAuditFailure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AddMandatoryAce(jitter):
    """"
    [Advapi32.dll] BOOL AddMandatoryAce(PACL pAcl, DWORD dwAceRevision, [AceFlags] AceFlags, [MandatoryPolicyFlags] MandatoryPolicy, PSID pLabelSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AceFlags", "MandatoryPolicy", "pLabelSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_DeleteAce(jitter):
    """"
    [Advapi32.dll] BOOL DeleteAce(PACL pAcl, DWORD dwAceIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_FindFirstFreeAce(jitter):
    """"
    [Advapi32.dll] BOOL FindFirstFreeAce(PACL pAcl, PACE* pAce)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "pAce"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_FreeInheritedFromArray(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] FreeInheritedFromArray(PINHERITED_FROM pInheritArray, USHORT AceCnt, PFN_OBJECT_MGR_FUNCTS pfnArray)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pInheritArray", "AceCnt", "pfnArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetAce(jitter):
    """"
    [Advapi32.dll] BOOL GetAce(PACL pAcl, DWORD dwAceIndex, PACE* pAce)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceIndex", "pAce"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetAclInformation(jitter):
    """"
    [Advapi32.dll] BOOL GetAclInformation(PACL pAcl, LPVOID pAclInformation, DWORD nAclInformationLength, ACL_INFORMATION_CLASS dwAclInformationClass)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "pAclInformation", "nAclInformationLength", "dwAclInformationClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetFileSecurity(jitter):
    """"
    [Advapi32.dll] BOOL GetFileSecurity(LPCTSTR lpFileName, SECURITY_INFORMATION RequestedInformation, PSECURITY_DESCRIPTOR pSecurityDescriptor, DWORD nLength, LPDWORD lpnLengthNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "RequestedInformation", "pSecurityDescriptor", "nLength", "lpnLengthNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetInheritanceSource(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE] GetInheritanceSource(LPTSTR pObjectName, SE_OBJECT_TYPE ObjectType, SECURITY_INFORMATION SecurityInfo, BOOL Container, GUID** pObjectClassGuids, DWORD GuidCount, PACL pAcl, PFN_OBJECT_MGR_FUNCTS pfnArray, PGENERIC_MAPPING pGenericMapping, PINHERITED_FROM pInheritArray)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pObjectName", "ObjectType", "SecurityInfo", "Container", "pObjectClassGuids", "GuidCount", "pAcl", "pfnArray", "pGenericMapping", "pInheritArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetKernelObjectSecurity(jitter):
    """"
    [Advapi32.dll] BOOL GetKernelObjectSecurity(HANDLE Handle, SECURITY_INFORMATION RequestedInformation, PISECURITY_DESCRIPTOR_RELATIVE pSecurityDescriptor, DWORD nLength, LPDWORD lpnLengthNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Handle", "RequestedInformation", "pSecurityDescriptor", "nLength", "lpnLengthNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetSecurityDescriptorDacl(jitter):
    """"
    [Advapi32.dll] BOOL GetSecurityDescriptorDacl(PSECURITY_DESCRIPTOR pSecurityDescriptor, LPBOOL lpbDaclPresent, PACL* pDacl, LPBOOL lpbDaclDefaulted)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "lpbDaclPresent", "pDacl", "lpbDaclDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetSecurityDescriptorGroup(jitter):
    """"
    [Advapi32.dll] BOOL GetSecurityDescriptorGroup(PSECURITY_DESCRIPTOR pSecurityDescriptor, PSID* pGroup, LPBOOL lpbGroupDefaulted)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "pGroup", "lpbGroupDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetSecurityDescriptorLength(jitter):
    """"
    [Advapi32.dll] DWORD GetSecurityDescriptorLength(PSECURITY_DESCRIPTOR pSecurityDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetSecurityDescriptorOwner(jitter):
    """"
    [Advapi32.dll] BOOL GetSecurityDescriptorOwner(PSECURITY_DESCRIPTOR pSecurityDescriptor, PSID* pOwner, LPBOOL lpbOwnerDefaulted)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "pOwner", "lpbOwnerDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetSecurityDescriptorSacl(jitter):
    """"
    [Advapi32.dll] BOOL GetSecurityDescriptorSacl(PSECURITY_DESCRIPTOR pSecurityDescriptor, LPBOOL lpbSaclPresent, PACL* pSacl, LPBOOL lpbSaclDefaulted)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "lpbSaclPresent", "pSacl", "lpbSaclDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_InitializeAcl(jitter):
    """"
    [Advapi32.dll] BOOL InitializeAcl(PACL pAcl, DWORD nAclLength, DWORD dwAclRevision)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "nAclLength", "dwAclRevision"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_InitializeSecurityDescriptor(jitter):
    """"
    [Advapi32.dll] BOOL InitializeSecurityDescriptor(PSECURITY_DESCRIPTOR pSecurityDescriptor, DWORD dwRevision)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "dwRevision"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_IsValidAcl(jitter):
    """"
    [Advapi32.dll] BOOL IsValidAcl(PACL pAcl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_IsValidSecurityDescriptor(jitter):
    """"
    [Advapi32.dll] BOOL IsValidSecurityDescriptor(PSECURITY_DESCRIPTOR pSecurityDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_MakeAbsoluteSD(jitter):
    """"
    [Advapi32.dll] BOOL MakeAbsoluteSD(PSECURITY_DESCRIPTOR_RELATIVE pSelfRelativeSD, PSECURITY_DESCRIPTOR pAbsoluteSD, LPDWORD lpdwAbsoluteSDSize, PACL pDacl, LPDWORD lpdwDaclSize, PACL pSacl, LPDWORD lpdwSaclSize, PSID pOwner, LPDWORD lpdwOwnerSize, PSID pPrimaryGroup, LPDWORD lpdwPrimaryGroupSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSelfRelativeSD", "pAbsoluteSD", "lpdwAbsoluteSDSize", "pDacl", "lpdwDaclSize", "pSacl", "lpdwSaclSize", "pOwner", "lpdwOwnerSize", "pPrimaryGroup", "lpdwPrimaryGroupSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_MakeSelfRelativeSD(jitter):
    """"
    [Advapi32.dll] BOOL MakeSelfRelativeSD(PSECURITY_DESCRIPTOR pAbsoluteSD, PSECURITY_DESCRIPTOR pSelfRelativeSD, LPDWORD lpdwBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAbsoluteSD", "pSelfRelativeSD", "lpdwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_QueryServiceObjectSecurity(jitter):
    """"
    [Advapi32.dll] BOOL QueryServiceObjectSecurity(SC_HANDLE hService, SECURITY_INFORMATION dwSecurityInformation, PSECURITY_DESCRIPTOR lpSecurityDescriptor, DWORD cbBufSize, LPDWORD pcbBytesNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "dwSecurityInformation", "lpSecurityDescriptor", "cbBufSize", "pcbBytesNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegGetKeySecurity(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegGetKeySecurity(HKEY hKey, SECURITY_INFORMATION SecurityInformation, PSECURITY_DESCRIPTOR pSecurityDescriptor, LPDWORD lpcbSecurityDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "SecurityInformation", "pSecurityDescriptor", "lpcbSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegSetKeySecurity(jitter):
    """"
    [Advapi32.dll] [REG_ERROR] RegSetKeySecurity(HKEY hKey, SECURITY_INFORMATION SecurityInformation, PSECURITY_DESCRIPTOR pSecurityDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hKey", "SecurityInformation", "pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetAclInformation(jitter):
    """"
    [Advapi32.dll] BOOL SetAclInformation(PACL pAcl, LPVOID pAclInformation, DWORD nAclInformationLength, ACL_INFORMATION_CLASS dwAclInformationClass)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "pAclInformation", "nAclInformationLength", "dwAclInformationClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetFileSecurity(jitter):
    """"
    [Advapi32.dll] BOOL SetFileSecurity(LPCTSTR lpFileName, SECURITY_INFORMATION SecurityInformation, PSECURITY_DESCRIPTOR pSecurityDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpFileName", "SecurityInformation", "pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetKernelObjectSecurity(jitter):
    """"
    [Advapi32.dll] BOOL SetKernelObjectSecurity(HANDLE Handle, SECURITY_INFORMATION SecurityInformation, PSECURITY_DESCRIPTOR SecurityDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Handle", "SecurityInformation", "SecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetSecurityDescriptorDacl(jitter):
    """"
    [Advapi32.dll] BOOL SetSecurityDescriptorDacl(PSECURITY_DESCRIPTOR pSecurityDescriptor, BOOL bDaclPresent, PACL pDacl, BOOL bDaclDefaulted)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "bDaclPresent", "pDacl", "bDaclDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetSecurityDescriptorGroup(jitter):
    """"
    [Advapi32.dll] BOOL SetSecurityDescriptorGroup(PSECURITY_DESCRIPTOR pSecurityDescriptor, PSID pGroup, BOOL bGroupDefaulted)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "pGroup", "bGroupDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetSecurityDescriptorOwner(jitter):
    """"
    [Advapi32.dll] BOOL SetSecurityDescriptorOwner(PSECURITY_DESCRIPTOR pSecurityDescriptor, PSID pOwner, BOOL bOwnerDefaulted)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "pOwner", "bOwnerDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetSecurityDescriptorSacl(jitter):
    """"
    [Advapi32.dll] BOOL SetSecurityDescriptorSacl(PSECURITY_DESCRIPTOR pSecurityDescriptor, BOOL bSaclPresent, PACL pSacl, BOOL bSaclDefaulted)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "bSaclPresent", "pSacl", "bSaclDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SetServiceObjectSecurity(jitter):
    """"
    [Advapi32.dll] BOOL SetServiceObjectSecurity(SC_HANDLE hService, SECURITY_INFORMATION dwSecurityInformation, PSECURITY_DESCRIPTOR lpSecurityDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hService", "dwSecurityInformation", "lpSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditComputeEffectivePolicyBySid(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditComputeEffectivePolicyBySid(const PSID pSid, const GUID* pSubCategoryGuids, ULONG PolicyCount, PAUDIT_POLICY_INFORMATION* ppAuditPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid", "pSubCategoryGuids", "PolicyCount", "ppAuditPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditComputeEffectivePolicyByToken(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditComputeEffectivePolicyByToken(HANDLE hTokenHandle, const GUID* pSubCategoryGuids, ULONG PolicyCount, PAUDIT_POLICY_INFORMATION* ppAuditPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hTokenHandle", "pSubCategoryGuids", "PolicyCount", "ppAuditPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditEnumerateCategories(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditEnumerateCategories(GUID** ppAuditCategoriesArray, PULONG pCountReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ppAuditCategoriesArray", "pCountReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditEnumeratePerUserPolicy(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditEnumeratePerUserPolicy(PPOLICY_AUDIT_SID_ARRAY* ppAuditSidArray)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ppAuditSidArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditEnumerateSubCategories(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditEnumerateSubCategories(const GUID* pAuditCategoryGuid, BOOLEAN bRetrieveAllSubCategories, GUID** ppAuditSubCategoriesArray, PULONG pCountReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAuditCategoryGuid", "bRetrieveAllSubCategories", "ppAuditSubCategoriesArray", "pCountReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditFree(jitter):
    """"
    [Advapi32.dll] VOID AuditFree(PVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditLookupCategoryGuidFromCategoryId(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditLookupCategoryGuidFromCategoryId(POLICY_AUDIT_EVENT_TYPE AuditCategoryId, GUID* pAuditCategoryGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["AuditCategoryId", "pAuditCategoryGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditLookupCategoryIdFromCategoryGuid(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditLookupCategoryIdFromCategoryGuid(const GUID* pAuditCategoryGuid, PPOLICY_AUDIT_EVENT_TYPE pAuditCategoryId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAuditCategoryGuid", "pAuditCategoryId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditLookupCategoryName(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditLookupCategoryName(const GUID* pAuditCategoryGuid, PTSTR* ppszCategoryName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAuditCategoryGuid", "ppszCategoryName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditLookupSubCategoryName(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditLookupSubCategoryName(const GUID* pAuditSubCategoryGuid, PTSTR* ppszSubCategoryName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAuditSubCategoryGuid", "ppszSubCategoryName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditQueryPerUserPolicy(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditQueryPerUserPolicy(const PSID pSid, const GUID* pSubCategoryGuids, ULONG PolicyCount, PAUDIT_POLICY_INFORMATION* ppAuditPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid", "pSubCategoryGuids", "PolicyCount", "ppAuditPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditQuerySystemPolicy(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditQuerySystemPolicy(const GUID* pSubCategoryGuids, ULONG PolicyCount, PAUDIT_POLICY_INFORMATION* ppAuditPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSubCategoryGuids", "PolicyCount", "ppAuditPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditSetPerUserPolicy(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditSetPerUserPolicy(const PSID pSid, PCAUDIT_POLICY_INFORMATION pAuditPolicy, ULONG PolicyCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid", "pAuditPolicy", "PolicyCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditSetSystemPolicy(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditSetSystemPolicy(PCAUDIT_POLICY_INFORMATION pAuditPolicy, ULONG PolicyCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAuditPolicy", "PolicyCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditQueryGlobalSacl(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditQueryGlobalSacl(PCTSTR ObjectTypeName, PACL* Acl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ObjectTypeName", "Acl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditSetGlobalSacl(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditSetGlobalSacl(PCTSTR ObjectTypeName, PACL Acl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ObjectTypeName", "Acl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditQuerySecurity(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditQuerySecurity(SECURITY_INFORMATION SecurityInformation, PSECURITY_DESCRIPTOR* ppSecurityDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SecurityInformation", "ppSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AuditSetSecurity(jitter):
    """"
    [Advapi32.dll] BOOLEAN AuditSetSecurity(SECURITY_INFORMATION SecurityInformation, PSECURITY_DESCRIPTOR pSecurityDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SecurityInformation", "pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_AddConditionalAce(jitter):
    """"
    [Advapi32.dll] BOOL AddConditionalAce(PACL pAcl, DWORD dwAceRevision, [AceFlags] AceFlags, [ACE_TYPE|UCHAR] AceType, [ACCESS_MASK_DWORD] AccessMask, PSID pSid, PWCHAR ConditionStr, DWORD* ReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AceFlags", "AceType", "AccessMask", "pSid", "ConditionStr", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetAppContainerNamedObjectPath(jitter):
    """"
    [Advapi32.dll] BOOL GetAppContainerNamedObjectPath(HANDLE Token, PSID AppContainerSid, ULONG ObjectPathLength, LPWSTR ObjectPath, PULONG ReturnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Token", "AppContainerSid", "ObjectPathLength", "ObjectPath", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LogonUser(jitter):
    """"
    [Advapi32.dll] BOOL LogonUser(LPTSTR lpszUsername, LPTSTR lpszDomain, LPTSTR lpszPassword, [LogonType] dwLogonType, [LogonProvider] dwLogonProvider, PHANDLE phToken)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszUsername", "lpszDomain", "lpszPassword", "dwLogonType", "dwLogonProvider", "phToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LogonUserEx(jitter):
    """"
    [Advapi32.dll] BOOL LogonUserEx(LPTSTR lpszUsername, LPTSTR lpszDomain, LPTSTR lpszPassword, [LogonType] dwLogonType, [LogonProvider] dwLogonProvider, PHANDLE phToken, PSID* ppLogonSid, PVOID* ppProfileBuffer, LPDWORD pdwProfileLength, PQUOTA_LIMITS pQuotaLimits)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszUsername", "lpszDomain", "lpszPassword", "dwLogonType", "dwLogonProvider", "phToken", "ppLogonSid", "ppProfileBuffer", "pdwProfileLength", "pQuotaLimits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LogonUserExExW(jitter):
    """"
    [Advapi32.dll] BOOL LogonUserExExW(LPWSTR lpszUsername, LPWSTR lpszDomain, LPWSTR lpszPassword, [LogonType] dwLogonType, PTOKEN_GROUPS pTokenGroups, [LogonProvider] dwLogonProvider, PHANDLE phToken, PSID* ppLogonSid, PVOID* ppProfileBuffer, LPDWORD pdwProfileLength, PQUOTA_LIMITS pQuotaLimits)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszUsername", "lpszDomain", "lpszPassword", "dwLogonType", "pTokenGroups", "dwLogonProvider", "phToken", "ppLogonSid", "ppProfileBuffer", "pdwProfileLength", "pQuotaLimits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredDelete(jitter):
    """"
    [Advapi32.dll] BOOL CredDelete(LPCTSTR TargetName, DWORD Type, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TargetName", "Type", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredEnumerate(jitter):
    """"
    [Advapi32.dll] BOOL CredEnumerate(LPCTSTR Filter, [CredEnumerateFlags] Flags, DWORD* Count, PCREDENTIAL** Credentials)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Filter", "Flags", "Count", "Credentials"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredFindBestCredential(jitter):
    """"
    [Advapi32.dll] BOOL CredFindBestCredential(LPCTSTR TargetName, DWORD Type, DWORD Flags, PCREDENTIAL* Credential)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TargetName", "Type", "Flags", "Credential"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredFree(jitter):
    """"
    [Advapi32.dll] VOID CredFree(PVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredGetSessionTypes(jitter):
    """"
    [Advapi32.dll] BOOL CredGetSessionTypes(DWORD MaximumPersistCount, LPDWORD MaximumPersist)
    """"
    ret_ad, args = jitter.func_args_stdcall(["MaximumPersistCount", "MaximumPersist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredGetTargetInfo(jitter):
    """"
    [Advapi32.dll] BOOL CredGetTargetInfo(LPCTSTR TargetName, [CredGetTargetInfoFlags] Flags, PCREDENTIAL_TARGET_INFORMATION* TargetInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TargetName", "Flags", "TargetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredIsProtected(jitter):
    """"
    [Advapi32.dll] BOOL CredIsProtected(LPTSTR pszProtectedCredentials, CRED_PROTECTION_TYPE* pProtectionType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszProtectedCredentials", "pProtectionType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredProtect(jitter):
    """"
    [Advapi32.dll] BOOL CredProtect(BOOL fAsSelf, LPTSTR pszCredentials, DWORD cchCredentials, LPTSTR pszProtectedCredentials, DWORD* pcchMaxChars, CRED_PROTECTION_TYPE* ProtectionType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fAsSelf", "pszCredentials", "cchCredentials", "pszProtectedCredentials", "pcchMaxChars", "ProtectionType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredMarshalCredential(jitter):
    """"
    [Advapi32.dll] BOOL CredMarshalCredential(CRED_MARSHAL_TYPE CredType, PVOID Credential, LPTSTR* MarshaledCredential)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CredType", "Credential", "MarshaledCredential"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredRead(jitter):
    """"
    [Advapi32.dll] BOOL CredRead(LPCTSTR TargetName, [CredType] Type, DWORD Flags, PCREDENTIAL* Credential)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TargetName", "Type", "Flags", "Credential"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredReadDomainCredentials(jitter):
    """"
    [Advapi32.dll] BOOL CredReadDomainCredentials(PCREDENTIAL_TARGET_INFORMATION TargetInfo, DWORD Flags, DWORD* Count, PCREDENTIAL** Credentials)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TargetInfo", "Flags", "Count", "Credentials"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredRename(jitter):
    """"
    [Advapi32.dll] BOOL CredRename(LPCTSTR OldTargetName, LPCTSTR NewTargetName, DWORD Type, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["OldTargetName", "NewTargetName", "Type", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredUnmarshalCredential(jitter):
    """"
    [Advapi32.dll] BOOL CredUnmarshalCredential(LPCTSTR MarshaledCredential, PCRED_MARSHAL_TYPE CredType, PVOID* Credential)
    """"
    ret_ad, args = jitter.func_args_stdcall(["MarshaledCredential", "CredType", "Credential"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredUnprotect(jitter):
    """"
    [Advapi32.dll] BOOL CredUnprotect(BOOL fAsSelf, LPTSTR pszProtectedCredentials, DWORD cchCredentials, LPTSTR pszCredentials, DWORD* pcchMaxChars)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fAsSelf", "pszProtectedCredentials", "cchCredentials", "pszCredentials", "pcchMaxChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredWrite(jitter):
    """"
    [Advapi32.dll] BOOL CredWrite(PCREDENTIAL Credential, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Credential", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredWriteDomainCredentials(jitter):
    """"
    [Advapi32.dll] BOOL CredWriteDomainCredentials(PCREDENTIAL_TARGET_INFORMATION TargetInfo, PCREDENTIAL Credential, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TargetInfo", "Credential", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CredIsMarshaledCredential(jitter):
    """"
    [Advapi32.dll] BOOL CredIsMarshaledCredential(LPTSTR MarshaledCredential)
    """"
    ret_ad, args = jitter.func_args_stdcall(["MarshaledCredential"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaEnumerateAccountsWithUserRight(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaEnumerateAccountsWithUserRight(LSA_HANDLE PolicyHandle, PLSA_UNICODE_STRING UserRights, PVOID* EnumerationBuffer, PULONG CountReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "UserRights", "EnumerationBuffer", "CountReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaEnumerateTrustedDomainsEx(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaEnumerateTrustedDomainsEx(LSA_HANDLE PolicyHandle, PLSA_ENUMERATION_HANDLE EnumerationContext, PVOID* Buffer, ULONG PreferredMaximumLength, PULONG CountReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "EnumerationContext", "Buffer", "PreferredMaximumLength", "CountReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaLookupNames(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaLookupNames(LSA_HANDLE PolicyHandle, ULONG Count, PLSA_UNICODE_STRING Names, PLSA_REFERENCED_DOMAIN_LIST* ReferencedDomains, PLSA_TRANSLATED_SID* Sids)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "Count", "Names", "ReferencedDomains", "Sids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaLookupNames2(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaLookupNames2(LSA_HANDLE PolicyHandle, [LSA_LOOKUP_FLAGS] Flags, ULONG Count, PLSA_UNICODE_STRING Names, PLSA_REFERENCED_DOMAIN_LIST* ReferencedDomains, PLSA_TRANSLATED_SID2* Sids)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "Flags", "Count", "Names", "ReferencedDomains", "Sids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaLookupPrivilegeValue(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaLookupPrivilegeValue(LSA_HANDLE PolicyHandle, PUNICODE_STRING Name, PLUID Value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "Name", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaLookupSids(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaLookupSids(LSA_HANDLE PolicyHandle, ULONG Count, PSID* Sids, PLSA_REFERENCED_DOMAIN_LIST* ReferencedDomains, PLSA_TRANSLATED_NAME* Names)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "Count", "Sids", "ReferencedDomains", "Names"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaLookupSids2(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaLookupSids2(LSA_HANDLE PolicyHandle, ULONG LookupOptions, ULONG Count, PSID* Sids, PLSA_REFERENCED_DOMAIN_LIST* ReferencedDomains, PLSA_TRANSLATED_NAME* Names)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "LookupOptions", "Count", "Sids", "ReferencedDomains", "Names"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaAddAccountRights(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaAddAccountRights(LSA_HANDLE PolicyHandle, PSID AccountSid, PLSA_UNICODE_STRING UserRights, ULONG CountOfRights)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "AccountSid", "UserRights", "CountOfRights"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaEnumerateAccountRights(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaEnumerateAccountRights(LSA_HANDLE PolicyHandle, PSID AccountSid, PLSA_UNICODE_STRING* UserRights, PULONG CountOfRights)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "AccountSid", "UserRights", "CountOfRights"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaRemoveAccountRights(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaRemoveAccountRights(LSA_HANDLE PolicyHandle, PSID AccountSid, BOOLEAN AllRights, PLSA_UNICODE_STRING UserRights, ULONG CountOfRights)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "AccountSid", "AllRights", "UserRights", "CountOfRights"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaCreateTrustedDomainEx(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaCreateTrustedDomainEx(LSA_HANDLE PolicyHandle, PTRUSTED_DOMAIN_INFORMATION_EX TrustedDomainInformation, PTRUSTED_DOMAIN_AUTH_INFORMATION AuthenticationInformation, ACCESS_MASK DesiredAccess, PLSA_HANDLE TrustedDomainHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "TrustedDomainInformation", "AuthenticationInformation", "DesiredAccess", "TrustedDomainHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaDeleteTrustedDomain(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaDeleteTrustedDomain(LSA_HANDLE PolicyHandle, PSID TrustedDomainSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "TrustedDomainSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaEnumerateTrustedDomains(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaEnumerateTrustedDomains(LSA_HANDLE PolicyHandle, PLSA_ENUMERATION_HANDLE EnumerationContext, PVOID* Buffer, ULONG PreferedMaximumLength, PULONG CountReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "EnumerationContext", "Buffer", "PreferedMaximumLength", "CountReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaOpenTrustedDomainByName(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaOpenTrustedDomainByName(LSA_HANDLE PolicyHandle, PLSA_UNICODE_STRING TrustedDomainName, ACCESS_MASK DesiredAccess, PLSA_HANDLE TrustedDomainHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "TrustedDomainName", "DesiredAccess", "TrustedDomainHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaQueryTrustedDomainInfo(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaQueryTrustedDomainInfo(LSA_HANDLE PolicyHandle, PSID TrustedDomainSid, TRUSTED_INFORMATION_CLASS InformationClass, PVOID* Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "TrustedDomainSid", "InformationClass", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaQueryTrustedDomainInfoByName(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaQueryTrustedDomainInfoByName(LSA_HANDLE PolicyHandle, PLSA_UNICODE_STRING TrustedDomainName, TRUSTED_INFORMATION_CLASS InformationClass, PVOID* Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "TrustedDomainName", "InformationClass", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaSetTrustedDomainInfoByName(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaSetTrustedDomainInfoByName(LSA_HANDLE PolicyHandle, PLSA_UNICODE_STRING TrustedDomainName, TRUSTED_INFORMATION_CLASS InformationClass, PVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "TrustedDomainName", "InformationClass", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaSetTrustedDomainInformation(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaSetTrustedDomainInformation(LSA_HANDLE PolicyHandle, PSID TrustedDomainSid, TRUSTED_INFORMATION_CLASS InformationClass, PVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "TrustedDomainSid", "InformationClass", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaRetrievePrivateData(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaRetrievePrivateData(LSA_HANDLE PolicyHandle, PLSA_UNICODE_STRING KeyName, PLSA_UNICODE_STRING* PrivateData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "KeyName", "PrivateData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaStorePrivateData(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaStorePrivateData(LSA_HANDLE PolicyHandle, PLSA_UNICODE_STRING KeyName, PLSA_UNICODE_STRING PrivateData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "KeyName", "PrivateData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaClose(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaClose(LSA_HANDLE ObjectHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ObjectHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaFreeMemory(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaFreeMemory(PVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaNtStatusToWinError(jitter):
    """"
    [Advapi32.dll] [ERROR_CODE_ULONG] LsaNtStatusToWinError(NTSTATUS Status)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SaferCloseLevel(jitter):
    """"
    [Advapi32.dll] BOOL SaferCloseLevel(SAFER_LEVEL_HANDLE hLevelHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLevelHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SaferIdentifyLevel(jitter):
    """"
    [Advapi32.dll] BOOL SaferIdentifyLevel(DWORD dwNumProperties, PSAFER_CODE_PROPERTIES pCodeProperties, SAFER_LEVEL_HANDLE* pLevelHandle, LPVOID lpReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwNumProperties", "pCodeProperties", "pLevelHandle", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SaferComputeTokenFromLevel(jitter):
    """"
    [Advapi32.dll] BOOL SaferComputeTokenFromLevel(SAFER_LEVEL_HANDLE LevelHandle, HANDLE InAccessToken, PHANDLE OutAccessToken, DWORD dwFlags, LPVOID lpReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LevelHandle", "InAccessToken", "OutAccessToken", "dwFlags", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SaferCreateLevel(jitter):
    """"
    [Advapi32.dll] BOOL SaferCreateLevel([SaferScopeId] dwScopeId, DWORD dwLevelId, DWORD OpenFlags, SAFER_LEVEL_HANDLE* pLevelHandle, LPVOID lpReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwScopeId", "dwLevelId", "OpenFlags", "pLevelHandle", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SaferGetLevelInformation(jitter):
    """"
    [Advapi32.dll] BOOL SaferGetLevelInformation(SAFER_LEVEL_HANDLE LevelHandle, SAFER_OBJECT_INFO_CLASS dwInfoType, LPVOID lpQueryBuffer, DWORD dwInBufferSize, LPDWORD lpdwOutBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LevelHandle", "dwInfoType", "lpQueryBuffer", "dwInBufferSize", "lpdwOutBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SaferGetPolicyInformation(jitter):
    """"
    [Advapi32.dll] BOOL SaferGetPolicyInformation([SaferScopeId] dwScopeId, SAFER_POLICY_INFO_CLASS SaferPolicyInfoClass, DWORD InfoBufferSize, PVOID InfoBuffer, PDWORD InfoBufferRetSize, LPVOID lpReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwScopeId", "SaferPolicyInfoClass", "InfoBufferSize", "InfoBuffer", "InfoBufferRetSize", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SaferiIsExecutableFileType(jitter):
    """"
    [Advapi32.dll] BOOL SaferiIsExecutableFileType(LPCWSTR szFullPath, BOOLEAN bFromShellExecute)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szFullPath", "bFromShellExecute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SaferRecordEventLogEntry(jitter):
    """"
    [Advapi32.dll] BOOL SaferRecordEventLogEntry(SAFER_LEVEL_HANDLE hLevel, LPCWSTR szTargetPath, LPVOID lpReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLevel", "szTargetPath", "lpReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_CloseThreadWaitChainSession(jitter):
    """"
    [Advapi32.dll] VOID CloseThreadWaitChainSession(HWCT WctHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["WctHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_GetThreadWaitChain(jitter):
    """"
    [Advapi32.dll] BOOL GetThreadWaitChain(HWCT WctHandle, DWORD_PTR Context, DWORD Flags, DWORD ThreadId, LPDWORD NodeCount, PWAITCHAIN_NODE_INFO NodeInfoArray, LPBOOL IsCycle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["WctHandle", "Context", "Flags", "ThreadId", "NodeCount", "NodeInfoArray", "IsCycle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_OpenThreadWaitChainSession(jitter):
    """"
    [Advapi32.dll] HWCT OpenThreadWaitChainSession(DWORD Flags, PWAITCHAINCALLBACK callback)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "callback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_RegisterWaitChainCOMCallback(jitter):
    """"
    [Advapi32.dll] VOID RegisterWaitChainCOMCallback(PCOGETCALLSTATE CallStateCallback, PCOGETACTIVATIONSTATE ActivationStateCallback)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CallStateCallback", "ActivationStateCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaOpenPolicy(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaOpenPolicy(PLSA_UNICODE_STRING SystemName, PLSA_OBJECT_ATTRIBUTES ObjectAttributes, ACCESS_MASK DesiredAccess, PLSA_HANDLE PolicyHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SystemName", "ObjectAttributes", "DesiredAccess", "PolicyHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaQueryInformationPolicy(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaQueryInformationPolicy(LSA_HANDLE PolicyHandle, POLICY_INFORMATION_CLASS InformationClass, PVOID* Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "InformationClass", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaSetInformationPolicy(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaSetInformationPolicy(LSA_HANDLE PolicyHandle, POLICY_INFORMATION_CLASS InformationClass, PVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "InformationClass", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaGetAppliedCAPIDs(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaGetAppliedCAPIDs(PLSA_UNICODE_STRING SystemName, PSID** CAPIDs, PULONG CAPIDCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SystemName", "CAPIDs", "CAPIDCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaQueryCAPs(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaQueryCAPs(PSID* CAPIDs, ULONG CAPIDCount, PCENTRAL_ACCESS_POLICY* CAPs, PULONG CAPCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CAPIDs", "CAPIDCount", "CAPs", "CAPCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaSetCAPs(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaSetCAPs(PLSA_UNICODE_STRING CAPDNs, ULONG CAPDNCount, ULONG Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CAPDNs", "CAPDNCount", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaQueryDomainInformationPolicy(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaQueryDomainInformationPolicy(LSA_HANDLE PolicyHandle, POLICY_DOMAIN_INFORMATION_CLASS InformationClass, PVOID* Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "InformationClass", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaQueryForestTrustInformation(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaQueryForestTrustInformation(LSA_HANDLE PolicyHandle, PLSA_UNICODE_STRING TrustedDomainName, PLSA_FOREST_TRUST_INFORMATION* ForestTrustInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "TrustedDomainName", "ForestTrustInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaSetDomainInformationPolicy(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaSetDomainInformationPolicy(LSA_HANDLE PolicyHandle, POLICY_DOMAIN_INFORMATION_CLASS InformationClass, PVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "InformationClass", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaSetForestTrustInformation(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaSetForestTrustInformation(LSA_HANDLE PolicyHandle, PLSA_UNICODE_STRING TrustedDomainName, PLSA_FOREST_TRUST_INFORMATION ForestTrustInfo, BOOLEAN CheckOnly, PLSA_FOREST_TRUST_COLLISION_INFORMATION* CollisionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "TrustedDomainName", "ForestTrustInfo", "CheckOnly", "CollisionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaOpenSecret(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaOpenSecret(LSA_HANDLE PolicyHandle, PLSA_UNICODE_STRING SecretName, ACCESS_MASK DesiredAccess, PLSA_HANDLE SecretHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "SecretName", "DesiredAccess", "SecretHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaSetSecret(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaSetSecret(LSA_HANDLE SecretHandle, PLSA_UNICODE_STRING CurrentValue, PLSA_UNICODE_STRING OldValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SecretHandle", "CurrentValue", "OldValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_LsaQuerySecret(jitter):
    """"
    [Advapi32.dll] NTSTATUS LsaQuerySecret(LSA_HANDLE SecretHandle, PLSA_UNICODE_STRING* CurrentValue, PLARGE_INTEGER CurrentValueSetTime, PLSA_UNICODE_STRING* OldValue, PLARGE_INTEGER OldValueSetTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SecretHandle", "CurrentValue", "CurrentValueSetTime", "OldValue", "OldValueSetTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SystemFunction036(jitter):
    """"
    [Advapi32.dll] BOOLEAN SystemFunction036(PVOID RandomBuffer, ULONG RandomBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RandomBuffer", "RandomBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SystemFunction040(jitter):
    """"
    [Advapi32.dll] NTSTATUS SystemFunction040(PVOID Memory, ULONG MemorySize, [RTL_ENCRYPT_OPTION_FLAGS] OptionFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Memory", "MemorySize", "OptionFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def advapi32_SystemFunction041(jitter):
    """"
    [Advapi32.dll] NTSTATUS SystemFunction041(PVOID Memory, ULONG MemorySize, [RTL_ENCRYPT_OPTION_FLAGS] OptionFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Memory", "MemorySize", "OptionFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
