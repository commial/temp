
def userenv_EnterCriticalPolicySection(jitter):
    """"
    [Userenv.dll] HANDLE EnterCriticalPolicySection(BOOL bMachine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_FreeGPOList(jitter):
    """"
    [Userenv.dll] BOOL FreeGPOList(PGROUP_POLICY_OBJECT pGPOList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pGPOList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetAppliedGPOList(jitter):
    """"
    [Userenv.dll] [ERROR_CODE] GetAppliedGPOList(DWORD dwFlags, LPCTSTR pMachineName, PSID pSidUser, GUID* pGuidExtension, PGROUP_POLICY_OBJECT* ppGPOList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pMachineName", "pSidUser", "pGuidExtension", "ppGPOList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetGPOList(jitter):
    """"
    [Userenv.dll] BOOL GetGPOList(HANDLE hToken, LPCTSTR lpName, LPCTSTR lpHostName, LPCTSTR lpComputerName, DWORD dwFlags, PGROUP_POLICY_OBJECT* pGPOList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hToken", "lpName", "lpHostName", "lpComputerName", "dwFlags", "pGPOList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_LeaveCriticalPolicySection(jitter):
    """"
    [Userenv.dll] BOOL LeaveCriticalPolicySection(HANDLE hSection)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_ProcessGroupPolicyCompleted(jitter):
    """"
    [Userenv.dll] [ERROR_CODE] ProcessGroupPolicyCompleted(REFGPEXTENSIONID extensionId, ASYNCCOMPLETIONHANDLE pAsyncHandle, DWORD dwStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["extensionId", "pAsyncHandle", "dwStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_ProcessGroupPolicyCompletedEx(jitter):
    """"
    [Userenv.dll] [ERROR_CODE] ProcessGroupPolicyCompletedEx(REFGPEXTENSIONID extensionId, ASYNCCOMPLETIONHANDLE pAsyncHandle, DWORD dwStatus, HRESULT RsopStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["extensionId", "pAsyncHandle", "dwStatus", "RsopStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RefreshPolicy(jitter):
    """"
    [Userenv.dll] BOOL RefreshPolicy(BOOL bMachine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RefreshPolicyEx(jitter):
    """"
    [Userenv.dll] BOOL RefreshPolicyEx(BOOL bMachine, DWORD dwOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bMachine", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RegisterGPNotification(jitter):
    """"
    [Userenv.dll] BOOL RegisterGPNotification(HANDLE hEvent, BOOL bMachine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEvent", "bMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RsopAccessCheckByType(jitter):
    """"
    [Userenv.dll] HRESULT RsopAccessCheckByType(PSECURITY_DESCRIPTOR pSecurityDescriptor, PSID pPrincipalSelfSid, PRSOPTOKEN pRsopToken, [ACCESS_MASK_DWORD] dwDesiredAccessMask, POBJECT_TYPE_LIST pObjectTypeList, DWORD ObjectTypeListLength, PGENERIC_MAPPING pGenericMapping, PPRIVILEGE_SET pPrivilegeSet, LPDWORD pdwPrivilegeSetLength, [ACCESS_MASK_LPDWORD] pdwGrantedAccessMask, LPBOOL pbAccessStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "pPrincipalSelfSid", "pRsopToken", "dwDesiredAccessMask", "pObjectTypeList", "ObjectTypeListLength", "pGenericMapping", "pPrivilegeSet", "pdwPrivilegeSetLength", "pdwGrantedAccessMask", "pbAccessStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RsopFileAccessCheck(jitter):
    """"
    [Userenv.dll] HRESULT RsopFileAccessCheck(LPWSTR pszFileName, PRSOPTOKEN pRsopToken, [ACCESS_MASK_DWORD] dwDesiredAccessMask, [ACCESS_MASK_LPDWORD] pdwGrantedAccessMask, LPBOOL pbAccessStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszFileName", "pRsopToken", "dwDesiredAccessMask", "pdwGrantedAccessMask", "pbAccessStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RsopResetPolicySettingStatus(jitter):
    """"
    [Userenv.dll] HRESULT RsopResetPolicySettingStatus(DWORD dwFlags, IWbemServices* pServices, IWbemClassObject* pSettingInstance)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pServices", "pSettingInstance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RsopSetPolicySettingStatus(jitter):
    """"
    [Userenv.dll] HRESULT RsopSetPolicySettingStatus(DWORD dwFlags, IWbemServices* pServices, IWbemClassObject* pSettingInstance, DWORD nInfo, POLICYSETTINGSTATUSINFO* pStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pServices", "pSettingInstance", "nInfo", "pStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_UnregisterGPNotification(jitter):
    """"
    [Userenv.dll] BOOL UnregisterGPNotification(HANDLE hEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_CreateEnvironmentBlock(jitter):
    """"
    [Userenv.dll] BOOL CreateEnvironmentBlock(LPVOID* lpEnvironment, HANDLE hToken, BOOL bInherit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpEnvironment", "hToken", "bInherit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_CreateProfile(jitter):
    """"
    [Userenv.dll] HRESULT CreateProfile(LPCWSTR pszUserSid, LPCWSTR pszUserName, LPWSTR pszProfilePath, DWORD cchProfilePath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszUserSid", "pszUserName", "pszProfilePath", "cchProfilePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_CreateUserProfileEx(jitter):
    """"
    [Userenv.dll] BOOL CreateUserProfileEx(PSID pSid, LPCTSTR lpUserName, LPCTSTR lpUserHive, LPTSTR lpProfileDir, DWORD dwDirSize, BOOL bWin9xUpg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSid", "lpUserName", "lpUserHive", "lpProfileDir", "dwDirSize", "bWin9xUpg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_DeleteProfile(jitter):
    """"
    [Userenv.dll] BOOL DeleteProfile(LPCTSTR lpSidString, LPCTSTR lpProfilePath, LPCTSTR lpComputerName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSidString", "lpProfilePath", "lpComputerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_DestroyEnvironmentBlock(jitter):
    """"
    [Userenv.dll] BOOL DestroyEnvironmentBlock(LPVOID lpEnvironment)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpEnvironment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_ExpandEnvironmentStringsForUser(jitter):
    """"
    [Userenv.dll] BOOL ExpandEnvironmentStringsForUser(HANDLE hToken, LPCTSTR lpSrc, LPTSTR lpDest, DWORD dwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hToken", "lpSrc", "lpDest", "dwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetAllUsersProfileDirectory(jitter):
    """"
    [Userenv.dll] BOOL GetAllUsersProfileDirectory(LPTSTR lpProfileDir, LPDWORD lpcchSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpProfileDir", "lpcchSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetDefaultUserProfileDirectory(jitter):
    """"
    [Userenv.dll] BOOL GetDefaultUserProfileDirectory(LPTSTR lpProfileDir, LPDWORD lpcchSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpProfileDir", "lpcchSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetProfilesDirectory(jitter):
    """"
    [Userenv.dll] BOOL GetProfilesDirectory(LPTSTR lpProfilesDir, LPDWORD lpcchSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpProfilesDir", "lpcchSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetProfileType(jitter):
    """"
    [Userenv.dll] BOOL GetProfileType([ProfileType*] pdwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetUserProfileDirectory(jitter):
    """"
    [Userenv.dll] BOOL GetUserProfileDirectory(HANDLE hToken, LPTSTR lpProfileDir, LPDWORD lpcchSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hToken", "lpProfileDir", "lpcchSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_LoadUserProfile(jitter):
    """"
    [Userenv.dll] BOOL LoadUserProfile(HANDLE hToken, LPPROFILEINFO lpProfileInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hToken", "lpProfileInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_UnloadUserProfile(jitter):
    """"
    [Userenv.dll] BOOL UnloadUserProfile(HANDLE hToken, HANDLE hProfile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hToken", "hProfile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_CreateAppContainerProfile(jitter):
    """"
    [Userenv.dll] HRESULT CreateAppContainerProfile(PCWSTR pszAppContainerName, PCWSTR pszDisplayName, PCWSTR pszDescription, PSID_AND_ATTRIBUTES pCapabilities, DWORD dwCapabilityCount, PSID* ppSidAppContainerSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszAppContainerName", "pszDisplayName", "pszDescription", "pCapabilities", "dwCapabilityCount", "ppSidAppContainerSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_DeleteAppContainerProfile(jitter):
    """"
    [Userenv.dll] HRESULT DeleteAppContainerProfile(PCWSTR pszAppContainerName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszAppContainerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_DeriveAppContainerSidFromAppContainerName(jitter):
    """"
    [Userenv.dll] HRESULT DeriveAppContainerSidFromAppContainerName(PCWSTR pszAppContainerName, PSID* ppsidAppContainerSid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszAppContainerName", "ppsidAppContainerSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetAppContainerFolderPath(jitter):
    """"
    [Userenv.dll] HRESULT GetAppContainerFolderPath(PCWSTR pszAppContainerSid, PWSTR* ppszPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszAppContainerSid", "ppszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetAppContainerRegistryLocation(jitter):
    """"
    [Userenv.dll] HRESULT GetAppContainerRegistryLocation(REGSAM desiredAccess, PHKEY phAppContainerKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["desiredAccess", "phAppContainerKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
