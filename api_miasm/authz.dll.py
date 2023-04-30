AUDIT_PARAM_TYPE = {
    "APT_None": 1,
    "APT_String": 2,
    "APT_Ulong": 3,
    "APT_Pointer": 4,
    "APT_Sid": 5,
    "APT_LogonId": 6,
    "APT_ObjectTypeList": 7,
    "APT_Luid": 8,
    "APT_Guid": 9,
    "APT_Time": 10,
    "APT_Int64": 11,
    "APT_IpAddress": 12,
    "APT_LogonIdWithSid": 13,
}
AUDIT_PARAM_TYPE_INV = {
    1: "APT_None",
    2: "APT_String",
    3: "APT_Ulong",
    4: "APT_Pointer",
    5: "APT_Sid",
    6: "APT_LogonId",
    7: "APT_ObjectTypeList",
    8: "APT_Luid",
    9: "APT_Guid",
    10: "APT_Time",
    11: "APT_Int64",
    12: "APT_IpAddress",
    13: "APT_LogonIdWithSid",
}
_APF_TYPE_ = {
    "APF_AuditFailure": 0x00000000,
    "APF_AuditSuccess": 0x00000001,
}
_APF_TYPE__INV = {
    0x00000000: "APF_AuditFailure",
    0x00000001: "APF_AuditSuccess",
}
AUTHZ_CONTEXT_INFORMATION_CLASS = {
    "AuthzContextInfoUserSid": 1,
    "AuthzContextInfoGroupsSids": 2,
    "AuthzContextInfoRestrictedSids": 3,
    "AuthzContextInfoPrivileges": 4,
    "AuthzContextInfoExpirationTime": 5,
    "AuthzContextInfoServerContext": 6,
    "AuthzContextInfoIdentifier": 7,
    "AuthzContextInfoSource": 8,
    "AuthzContextInfoAll": 9,
    "AuthzContextInfoAuthenticationId": 0,
}
AUTHZ_CONTEXT_INFORMATION_CLASS_INV = {
    1: "AuthzContextInfoUserSid",
    2: "AuthzContextInfoGroupsSids",
    3: "AuthzContextInfoRestrictedSids",
    4: "AuthzContextInfoPrivileges",
    5: "AuthzContextInfoExpirationTime",
    6: "AuthzContextInfoServerContext",
    7: "AuthzContextInfoIdentifier",
    8: "AuthzContextInfoSource",
    9: "AuthzContextInfoAll",
    0: "AuthzContextInfoAuthenticationId",
}
AUTHZ_SECURITY_ATTRIBUTE_OPERATION = {
    "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_NONE": 0,
    "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE_ALL": 1,
    "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_ADD": 2,
    "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_DELETE": 3,
    "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE": 4,
}
AUTHZ_SECURITY_ATTRIBUTE_OPERATION_INV = {
    0: "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_NONE",
    1: "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE_ALL",
    2: "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_ADD",
    3: "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_DELETE",
    4: "AUTHZ_SECURITY_ATTRIBUTE_OPERATION_REPLACE",
}
AUTHZ_SID_OPERATION = {
    "AUTHZ_SID_OPERATION_NONE": 0,
    "AUTHZ_SID_OPERATION_REPLACE_ALL": 1,
    "AUTHZ_SID_OPERATION_ADD": 2,
    "AUTHZ_SID_OPERATION_DELETE": 3,
    "AUTHZ_SID_OPERATION_REPLACE": 4,
}
AUTHZ_SID_OPERATION_INV = {
    0: "AUTHZ_SID_OPERATION_NONE",
    1: "AUTHZ_SID_OPERATION_REPLACE_ALL",
    2: "AUTHZ_SID_OPERATION_ADD",
    3: "AUTHZ_SID_OPERATION_DELETE",
    4: "AUTHZ_SID_OPERATION_REPLACE",
}

def authz_AuthzAccessCheck(jitter):
    """
    BOOL AuthzAccessCheck(
        [AuthzAccessCheckFlags] flags,
        AUTHZ_CLIENT_CONTEXT_HANDLE AuthzClientContext,
        PAUTHZ_ACCESS_REQUEST pRequest,
        AUTHZ_AUDIT_EVENT_HANDLE AuditInfo,
        PSECURITY_DESCRIPTOR pSecurityDescriptor,
        PSECURITY_DESCRIPTOR* OptionalSecurityDescriptorArray,
        DWORD OptionalSecurityDescriptorCount,
        PAUTHZ_ACCESS_REPLY pReply,
        PAUTHZ_ACCESS_CHECK_RESULTS_HANDLE pAuthzHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "AuthzClientContext", "pRequest", "AuditInfo", "pSecurityDescriptor", "OptionalSecurityDescriptorArray", "OptionalSecurityDescriptorCount", "pReply", "pAuthzHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzAddSidsToContext(jitter):
    """
    BOOL AuthzAddSidsToContext(
        AUTHZ_CLIENT_CONTEXT_HANDLE OrigClientContext,
        PSID_AND_ATTRIBUTES Sids,
        DWORD SidCount,
        PSID_AND_ATTRIBUTES RestrictedSids,
        DWORD RestrictedSidCount,
        PAUTHZ_CLIENT_CONTEXT_HANDLE pNewClientContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OrigClientContext", "Sids", "SidCount", "RestrictedSids", "RestrictedSidCount", "pNewClientContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzCachedAccessCheck(jitter):
    """
    BOOL AuthzCachedAccessCheck(
        DWORD Flags,
        AUTHZ_ACCESS_CHECK_RESULTS_HANDLE AuthzHandle,
        PAUTHZ_ACCESS_REQUEST pRequest,
        AUTHZ_AUDIT_EVENT_HANDLE AuditInfo,
        PAUTHZ_ACCESS_REPLY pReply
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "AuthzHandle", "pRequest", "AuditInfo", "pReply"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzEnumerateSecurityEventSources(jitter):
    """
    BOOL AuthzEnumerateSecurityEventSources(
        DWORD dwFlags,
        PAUTHZ_SOURCE_SCHEMA_REGISTRATION Buffer,
        PDWORD pdwCount,
        PDWORD pdwLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "Buffer", "pdwCount", "pdwLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzFreeAuditEvent(jitter):
    """
    BOOL AuthzFreeAuditEvent(
        AUTHZ_AUDIT_EVENT_HANDLE pAuditEventInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAuditEventInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzFreeContext(jitter):
    """
    BOOL AuthzFreeContext(
        AUTHZ_CLIENT_CONTEXT_HANDLE AuthzClientContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthzClientContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzFreeHandle(jitter):
    """
    BOOL AuthzFreeHandle(
        AUTHZ_ACCESS_CHECK_RESULTS_HANDLE AuthzHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthzHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzFreeResourceManager(jitter):
    """
    BOOL AuthzFreeResourceManager(
        AUTHZ_RESOURCE_MANAGER_HANDLE AuthzResourceManager
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthzResourceManager"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzGetInformationFromContext(jitter):
    """
    BOOL AuthzGetInformationFromContext(
        AUTHZ_CLIENT_CONTEXT_HANDLE hAuthzClientContext,
        AUTHZ_CONTEXT_INFORMATION_CLASS InfoClass,
        DWORD BufferSize,
        PDWORD pSizeRequired,
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAuthzClientContext", "InfoClass", "BufferSize", "pSizeRequired", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzInitializeContextFromAuthzContext(jitter):
    """
    BOOL AuthzInitializeContextFromAuthzContext(
        DWORD flags,
        AUTHZ_CLIENT_CONTEXT_HANDLE AuthzHandle,
        PLARGE_INTEGER ExpirationTime,
        LUID Identifier,
        PVOID DynamicGroupArgs,
        PAUTHZ_CLIENT_CONTEXT_HANDLE phNewAuthzHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "AuthzHandle", "ExpirationTime", "Identifier", "DynamicGroupArgs", "phNewAuthzHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzInitializeContextFromSid(jitter):
    """
    BOOL AuthzInitializeContextFromSid(
        [AuthzInitContextFlags] Flags,
        PSID UserSid,
        AUTHZ_RESOURCE_MANAGER_HANDLE hAuthzResourceManager,
        PLARGE_INTEGER pExpirationTime,
        LUID Identifier,
        PVOID DynamicGroupArgs,
        PAUTHZ_CLIENT_CONTEXT_HANDLE pAuthzClientContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "UserSid", "hAuthzResourceManager", "pExpirationTime", "Identifier", "DynamicGroupArgs", "pAuthzClientContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzInitializeContextFromToken(jitter):
    """
    BOOL AuthzInitializeContextFromToken(
        DWORD Flags,
        HANDLE TokenHandle,
        AUTHZ_RESOURCE_MANAGER_HANDLE AuthzResourceManager,
        PLARGE_INTEGER pExpirationTime,
        LUID Identifier,
        PVOID DynamicGroupArgs,
        PAUTHZ_CLIENT_CONTEXT_HANDLE pAuthzClientContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "TokenHandle", "AuthzResourceManager", "pExpirationTime", "Identifier", "DynamicGroupArgs", "pAuthzClientContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzInitializeObjectAccessAuditEvent(jitter):
    """
    BOOL AuthzInitializeObjectAccessAuditEvent(
        DWORD Flags,
        AUTHZ_AUDIT_EVENT_TYPE_HANDLE hAuditEventType,
        PWSTR szOperationType,
        PWSTR szObjectType,
        PWSTR szObjectName,
        PWSTR szAdditionalInfo,
        PAUTHZ_AUDIT_EVENT_HANDLE phAuditEvent,
        DWORD dwAdditionalParamCount,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "hAuditEventType", "szOperationType", "szObjectType", "szObjectName", "szAdditionalInfo", "phAuditEvent", "dwAdditionalParamCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzInitializeObjectAccessAuditEvent2(jitter):
    """
    BOOL AuthzInitializeObjectAccessAuditEvent2(
        [AUTHZ_INITOBJAUDITEVENT_FLAGS] Flags,
        AUTHZ_AUDIT_EVENT_TYPE_HANDLE hAuditEventType,
        PWSTR szOperationType,
        PWSTR szObjectType,
        PWSTR szObjectName,
        PWSTR szAdditionalInfo,
        PWSTR szAdditionalInfo2,
        PAUTHZ_AUDIT_EVENT_HANDLE phAuditEvent,
        DWORD dwAdditionalParameterCount,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "hAuditEventType", "szOperationType", "szObjectType", "szObjectName", "szAdditionalInfo", "szAdditionalInfo2", "phAuditEvent", "dwAdditionalParameterCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzInitializeRemoteResourceManager(jitter):
    """
    BOOL AuthzInitializeRemoteResourceManager(
        PAUTHZ_RPC_INIT_INFO_CLIENT pRpcInitInfo,
        PAUTHZ_RESOURCE_MANAGER_HANDLE phAuthzResourceManager
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcInitInfo", "phAuthzResourceManager"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzInitializeResourceManager(jitter):
    """
    BOOL AuthzInitializeResourceManager(
        [AuthzInitRMFlags] flags,
        PFN_AUTHZ_DYNAMIC_ACCESS_CHECK pfnAccessCheck,
        PFN_AUTHZ_COMPUTE_DYNAMIC_GROUPS pfnComputeDynamicGroups,
        PFN_AUTHZ_FREE_DYNAMIC_GROUPS pfnFreeDynamicGroups,
        PCWSTR ResourceManagerName,
        PAUTHZ_RESOURCE_MANAGER_HANDLE pAuthzResourceManager
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "pfnAccessCheck", "pfnComputeDynamicGroups", "pfnFreeDynamicGroups", "ResourceManagerName", "pAuthzResourceManager"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzInitializeResourceManagerEx(jitter):
    """
    BOOL AuthzInitializeResourceManagerEx(
        DWORD Flags,
        PVOID pAuthzInitInfo,
        PAUTHZ_RESOURCE_MANAGER_HANDLE phAuthzResourceManager
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "pAuthzInitInfo", "phAuthzResourceManager"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzOpenObjectAudit(jitter):
    """
    BOOL AuthzOpenObjectAudit(
        DWORD Flags,
        AUTHZ_CLIENT_CONTEXT_HANDLE hAuthzClientContext,
        PAUTHZ_ACCESS_REQUEST pRequest,
        AUTHZ_AUDIT_EVENT_HANDLE hAuditEvent,
        PSECURITY_DESCRIPTOR pSecurityDescriptor,
        PSECURITY_DESCRIPTOR* SecurityDescriptorArray,
        DWORD SecurityDescriptorCount,
        PAUTHZ_ACCESS_REPLY pReply
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "hAuthzClientContext", "pRequest", "hAuditEvent", "pSecurityDescriptor", "SecurityDescriptorArray", "SecurityDescriptorCount", "pReply"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzRegisterSecurityEventSource(jitter):
    """
    BOOL AuthzRegisterSecurityEventSource(
        DWORD dwFlags,
        PCWSTR szEventSourceName,
        PAUTHZ_SECURITY_EVENT_PROVIDER_HANDLE phEventProvider
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "szEventSourceName", "phEventProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzReportSecurityEvent(jitter):
    """
    BOOL AuthzReportSecurityEvent(
        [APF_TYPE] dwFlags,
        AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE hEventProvider,
        DWORD dwAuditId,
        PSID pUserSid,
        DWORD dwCount,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "hEventProvider", "dwAuditId", "pUserSid", "dwCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzReportSecurityEventFromParams(jitter):
    """
    BOOL AuthzReportSecurityEventFromParams(
        DWORD dwFlags,
        AUTHZ_SECURITY_EVENT_PROVIDER_HANDLE hEventProvider,
        DWORD dwAuditId,
        PSID pUserSid,
        PAUDIT_PARAMS pParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "hEventProvider", "dwAuditId", "pUserSid", "pParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzInstallSecurityEventSource(jitter):
    """
    BOOL AuthzInstallSecurityEventSource(
        DWORD dwFlags,
        PAUTHZ_SOURCE_SCHEMA_REGISTRATION pRegistration
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pRegistration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzUninstallSecurityEventSource(jitter):
    """
    BOOL AuthzUninstallSecurityEventSource(
        DWORD dwFlags,
        PCWSTR szEventSourceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "szEventSourceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzUnregisterSecurityEventSource(jitter):
    """
    BOOL AuthzUnregisterSecurityEventSource(
        DWORD dwFlags,
        PAUTHZ_SECURITY_EVENT_PROVIDER_HANDLE phEventProvider
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "phEventProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzModifySecurityAttributes(jitter):
    """
    BOOL AuthzModifySecurityAttributes(
        AUTHZ_CLIENT_CONTEXT_HANDLE AuthzClientContext,
        PAUTHZ_SECURITY_ATTRIBUTE_OPERATION pOperations,
        PAUTHZ_SECURITY_ATTRIBUTES_INFORMATION pAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthzClientContext", "pOperations", "pAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzFreeCentralAccessPolicyCache(jitter):
    """
    BOOL AuthzFreeCentralAccessPolicyCache()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzInitializeCompoundContext(jitter):
    """
    BOOL AuthzInitializeCompoundContext(
        AUTHZ_CLIENT_CONTEXT_HANDLE UserContext,
        AUTHZ_CLIENT_CONTEXT_HANDLE DeviceContext,
        PAUTHZ_CLIENT_CONTEXT_HANDLE phCompoundContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UserContext", "DeviceContext", "phCompoundContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzModifyClaims(jitter):
    """
    BOOL AuthzModifyClaims(
        AUTHZ_CLIENT_CONTEXT_HANDLE hAuthzClientContext,
        AUTHZ_CONTEXT_INFORMATION_CLASS ClaimClass,
        PAUTHZ_SECURITY_ATTRIBUTE_OPERATION pClaimOperations,
        PAUTHZ_SECURITY_ATTRIBUTES_INFORMATION pClaims
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAuthzClientContext", "ClaimClass", "pClaimOperations", "pClaims"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzModifySids(jitter):
    """
    BOOL AuthzModifySids(
        AUTHZ_CLIENT_CONTEXT_HANDLE hAuthzClientContext,
        AUTHZ_CONTEXT_INFORMATION_CLASS SidClass,
        PAUTHZ_SID_OPERATION pSidOperations,
        PTOKEN_GROUPS pSids
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAuthzClientContext", "SidClass", "pSidOperations", "pSids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzRegisterCapChangeNotification(jitter):
    """
    BOOL AuthzRegisterCapChangeNotification(
        PAUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE phCapChangeSubscription,
        LPTHREAD_START_ROUTINE pfnCapChangeCallback,
        PVOID pCallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phCapChangeSubscription", "pfnCapChangeCallback", "pCallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzSetAppContainerInformation(jitter):
    """
    BOOL AuthzSetAppContainerInformation(
        AUTHZ_CLIENT_CONTEXT_HANDLE hAuthzClientContext,
        PSID pAppContainerSid,
        DWORD CapabilityCount,
        PSID_AND_ATTRIBUTES pCapabilitySids
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hAuthzClientContext", "pAppContainerSid", "CapabilityCount", "pCapabilitySids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def authz_AuthzUnregisterCapChangeNotification(jitter):
    """
    BOOL AuthzUnregisterCapChangeNotification(
        AUTHZ_CAP_CHANGE_SUBSCRIPTION_HANDLE hCapChangeSubscription
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCapChangeSubscription"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
