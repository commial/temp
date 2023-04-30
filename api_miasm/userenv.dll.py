GPO_LINK = {
    "GPLinkUnknown": 0,
    "GPLinkMachine": 1,
    "GPLinkSite": 2,
    "GPLinkDomain": 3,
    "GPLinkOrganizationalUnit": 4,
}
SETTINGSTATUS = {
    "RSOPUnspecified": 0,
    "RSOPApplied": 1,
    "RSOPIgnored": 2,
    "RSOPFailed": 3,
    "RSOPSubsettingFailed": 4,
}

def userenv_EnterCriticalPolicySection(jitter):
    """
    HANDLE EnterCriticalPolicySection(
        BOOL bMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_FreeGPOList(jitter, get_str, set_str):
    """
    BOOL FreeGPOList(
        PGROUP_POLICY_OBJECT pGPOList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pGPOList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_FreeGPOListA(jitter):
    userenv_FreeGPOList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def userenv_FreeGPOListW(jitter):
    userenv_FreeGPOList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def userenv_GetAppliedGPOList(jitter, get_str, set_str):
    """
    [ERROR_CODE] GetAppliedGPOList(
        DWORD dwFlags,
        LPCTSTR pMachineName,
        PSID pSidUser,
        GUID* pGuidExtension,
        PGROUP_POLICY_OBJECT* ppGPOList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pMachineName", "pSidUser", "pGuidExtension", "ppGPOList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetAppliedGPOListA(jitter):
    userenv_GetAppliedGPOList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def userenv_GetAppliedGPOListW(jitter):
    userenv_GetAppliedGPOList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def userenv_GetGPOList(jitter, get_str, set_str):
    """
    BOOL GetGPOList(
        HANDLE hToken,
        LPCTSTR lpName,
        LPCTSTR lpHostName,
        LPCTSTR lpComputerName,
        DWORD dwFlags,
        PGROUP_POLICY_OBJECT* pGPOList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hToken", "lpName", "lpHostName", "lpComputerName", "dwFlags", "pGPOList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetGPOListA(jitter):
    userenv_GetGPOList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def userenv_GetGPOListW(jitter):
    userenv_GetGPOList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def userenv_LeaveCriticalPolicySection(jitter):
    """
    BOOL LeaveCriticalPolicySection(
        HANDLE hSection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_ProcessGroupPolicyCompleted(jitter):
    """
    [ERROR_CODE] ProcessGroupPolicyCompleted(
        REFGPEXTENSIONID extensionId,
        ASYNCCOMPLETIONHANDLE pAsyncHandle,
        DWORD dwStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["extensionId", "pAsyncHandle", "dwStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_ProcessGroupPolicyCompletedEx(jitter):
    """
    [ERROR_CODE] ProcessGroupPolicyCompletedEx(
        REFGPEXTENSIONID extensionId,
        ASYNCCOMPLETIONHANDLE pAsyncHandle,
        DWORD dwStatus,
        HRESULT RsopStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["extensionId", "pAsyncHandle", "dwStatus", "RsopStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RefreshPolicy(jitter):
    """
    BOOL RefreshPolicy(
        BOOL bMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RefreshPolicyEx(jitter):
    """
    BOOL RefreshPolicyEx(
        BOOL bMachine,
        DWORD dwOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bMachine", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RegisterGPNotification(jitter):
    """
    BOOL RegisterGPNotification(
        HANDLE hEvent,
        BOOL bMachine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEvent", "bMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RsopAccessCheckByType(jitter):
    """
    HRESULT RsopAccessCheckByType(
        PSECURITY_DESCRIPTOR pSecurityDescriptor,
        PSID pPrincipalSelfSid,
        PRSOPTOKEN pRsopToken,
        [ACCESS_MASK_DWORD] dwDesiredAccessMask,
        POBJECT_TYPE_LIST pObjectTypeList,
        DWORD ObjectTypeListLength,
        PGENERIC_MAPPING pGenericMapping,
        PPRIVILEGE_SET pPrivilegeSet,
        LPDWORD pdwPrivilegeSetLength,
        [ACCESS_MASK_LPDWORD] pdwGrantedAccessMask,
        LPBOOL pbAccessStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSecurityDescriptor", "pPrincipalSelfSid", "pRsopToken", "dwDesiredAccessMask", "pObjectTypeList", "ObjectTypeListLength", "pGenericMapping", "pPrivilegeSet", "pdwPrivilegeSetLength", "pdwGrantedAccessMask", "pbAccessStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RsopFileAccessCheck(jitter):
    """
    HRESULT RsopFileAccessCheck(
        LPWSTR pszFileName,
        PRSOPTOKEN pRsopToken,
        [ACCESS_MASK_DWORD] dwDesiredAccessMask,
        [ACCESS_MASK_LPDWORD] pdwGrantedAccessMask,
        LPBOOL pbAccessStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFileName", "pRsopToken", "dwDesiredAccessMask", "pdwGrantedAccessMask", "pbAccessStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RsopResetPolicySettingStatus(jitter):
    """
    HRESULT RsopResetPolicySettingStatus(
        DWORD dwFlags,
        IWbemServices* pServices,
        IWbemClassObject* pSettingInstance
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pServices", "pSettingInstance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_RsopSetPolicySettingStatus(jitter):
    """
    HRESULT RsopSetPolicySettingStatus(
        DWORD dwFlags,
        IWbemServices* pServices,
        IWbemClassObject* pSettingInstance,
        DWORD nInfo,
        POLICYSETTINGSTATUSINFO* pStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pServices", "pSettingInstance", "nInfo", "pStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_UnregisterGPNotification(jitter):
    """
    BOOL UnregisterGPNotification(
        HANDLE hEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_CreateEnvironmentBlock(jitter):
    """
    BOOL CreateEnvironmentBlock(
        LPVOID* lpEnvironment,
        HANDLE hToken,
        BOOL bInherit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpEnvironment", "hToken", "bInherit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_CreateProfile(jitter):
    """
    HRESULT CreateProfile(
        LPCWSTR pszUserSid,
        LPCWSTR pszUserName,
        LPWSTR pszProfilePath,
        DWORD cchProfilePath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUserSid", "pszUserName", "pszProfilePath", "cchProfilePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_CreateUserProfileEx(jitter, get_str, set_str):
    """
    BOOL CreateUserProfileEx(
        PSID pSid,
        LPCTSTR lpUserName,
        LPCTSTR lpUserHive,
        LPTSTR lpProfileDir,
        DWORD dwDirSize,
        BOOL bWin9xUpg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSid", "lpUserName", "lpUserHive", "lpProfileDir", "dwDirSize", "bWin9xUpg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_CreateUserProfileExA(jitter):
    userenv_CreateUserProfileEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def userenv_CreateUserProfileExW(jitter):
    userenv_CreateUserProfileEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def userenv_DeleteProfile(jitter, get_str, set_str):
    """
    BOOL DeleteProfile(
        LPCTSTR lpSidString,
        LPCTSTR lpProfilePath,
        LPCTSTR lpComputerName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpSidString", "lpProfilePath", "lpComputerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_DeleteProfileA(jitter):
    userenv_DeleteProfile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def userenv_DeleteProfileW(jitter):
    userenv_DeleteProfile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def userenv_DestroyEnvironmentBlock(jitter):
    """
    BOOL DestroyEnvironmentBlock(
        LPVOID lpEnvironment
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpEnvironment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_ExpandEnvironmentStringsForUser(jitter, get_str, set_str):
    """
    BOOL ExpandEnvironmentStringsForUser(
        HANDLE hToken,
        LPCTSTR lpSrc,
        LPTSTR lpDest,
        DWORD dwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hToken", "lpSrc", "lpDest", "dwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_ExpandEnvironmentStringsForUserA(jitter):
    userenv_ExpandEnvironmentStringsForUser(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def userenv_ExpandEnvironmentStringsForUserW(jitter):
    userenv_ExpandEnvironmentStringsForUser(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def userenv_GetAllUsersProfileDirectory(jitter, get_str, set_str):
    """
    BOOL GetAllUsersProfileDirectory(
        LPTSTR lpProfileDir,
        LPDWORD lpcchSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpProfileDir", "lpcchSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetAllUsersProfileDirectoryA(jitter):
    userenv_GetAllUsersProfileDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def userenv_GetAllUsersProfileDirectoryW(jitter):
    userenv_GetAllUsersProfileDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def userenv_GetDefaultUserProfileDirectory(jitter, get_str, set_str):
    """
    BOOL GetDefaultUserProfileDirectory(
        LPTSTR lpProfileDir,
        LPDWORD lpcchSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpProfileDir", "lpcchSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetDefaultUserProfileDirectoryA(jitter):
    userenv_GetDefaultUserProfileDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def userenv_GetDefaultUserProfileDirectoryW(jitter):
    userenv_GetDefaultUserProfileDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def userenv_GetProfilesDirectory(jitter, get_str, set_str):
    """
    BOOL GetProfilesDirectory(
        LPTSTR lpProfilesDir,
        LPDWORD lpcchSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpProfilesDir", "lpcchSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetProfilesDirectoryA(jitter):
    userenv_GetProfilesDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def userenv_GetProfilesDirectoryW(jitter):
    userenv_GetProfilesDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def userenv_GetProfileType(jitter):
    """
    BOOL GetProfileType(
        [ProfileType*] pdwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetUserProfileDirectory(jitter, get_str, set_str):
    """
    BOOL GetUserProfileDirectory(
        HANDLE hToken,
        LPTSTR lpProfileDir,
        LPDWORD lpcchSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hToken", "lpProfileDir", "lpcchSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetUserProfileDirectoryA(jitter):
    userenv_GetUserProfileDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def userenv_GetUserProfileDirectoryW(jitter):
    userenv_GetUserProfileDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def userenv_LoadUserProfile(jitter, get_str, set_str):
    """
    BOOL LoadUserProfile(
        HANDLE hToken,
        LPPROFILEINFO lpProfileInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hToken", "lpProfileInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_LoadUserProfileA(jitter):
    userenv_LoadUserProfile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def userenv_LoadUserProfileW(jitter):
    userenv_LoadUserProfile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def userenv_UnloadUserProfile(jitter):
    """
    BOOL UnloadUserProfile(
        HANDLE hToken,
        HANDLE hProfile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hToken", "hProfile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_CreateAppContainerProfile(jitter):
    """
    HRESULT CreateAppContainerProfile(
        PCWSTR pszAppContainerName,
        PCWSTR pszDisplayName,
        PCWSTR pszDescription,
        PSID_AND_ATTRIBUTES pCapabilities,
        DWORD dwCapabilityCount,
        PSID* ppSidAppContainerSid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszAppContainerName", "pszDisplayName", "pszDescription", "pCapabilities", "dwCapabilityCount", "ppSidAppContainerSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_DeleteAppContainerProfile(jitter):
    """
    HRESULT DeleteAppContainerProfile(
        PCWSTR pszAppContainerName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszAppContainerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_DeriveAppContainerSidFromAppContainerName(jitter):
    """
    HRESULT DeriveAppContainerSidFromAppContainerName(
        PCWSTR pszAppContainerName,
        PSID* ppsidAppContainerSid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszAppContainerName", "ppsidAppContainerSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetAppContainerFolderPath(jitter):
    """
    HRESULT GetAppContainerFolderPath(
        PCWSTR pszAppContainerSid,
        PWSTR* ppszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszAppContainerSid", "ppszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def userenv_GetAppContainerRegistryLocation(jitter):
    """
    HRESULT GetAppContainerRegistryLocation(
        REGSAM desiredAccess,
        PHKEY phAppContainerKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["desiredAccess", "phAppContainerKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
