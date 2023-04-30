
def winbio_WinBioAcquireFocus(jitter):
    """
    HRESULT WinBioAcquireFocus()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioAsyncEnumBiometricUnits(jitter):
    """
    HRESULT WinBioAsyncEnumBiometricUnits(
        WINBIO_FRAMEWORK_HANDLE FrameworkHandle,
        WINBIO_BIOMETRIC_TYPE Factor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FrameworkHandle", "Factor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioAsyncEnumDatabases(jitter):
    """
    HRESULT WinBioAsyncEnumDatabases(
        WINBIO_FRAMEWORK_HANDLE FrameworkHandle,
        WINBIO_BIOMETRIC_TYPE Factor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FrameworkHandle", "Factor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioAsyncEnumServiceProviders(jitter):
    """
    HRESULT WinBioAsyncEnumServiceProviders(
        WINBIO_FRAMEWORK_HANDLE FrameworkHandle,
        WINBIO_BIOMETRIC_TYPE Factor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FrameworkHandle", "Factor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioAsyncMonitorFrameworkChanges(jitter):
    """
    HRESULT WinBioAsyncMonitorFrameworkChanges(
        WINBIO_FRAMEWORK_HANDLE FrameworkHandle,
        WINBIO_FRAMEWORK_CHANGE_TYPE ChangeTypes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FrameworkHandle", "ChangeTypes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioAsyncOpenFramework(jitter):
    """
    HRESULT WinBioAsyncOpenFramework(
        WINBIO_ASYNC_NOTIFICATION_METHOD NotificationMethod,
        HWND TargetWindow,
        UINT MessageCode,
        PWINBIO_ASYNC_COMPLETION_CALLBACK CallbackRoutine,
        PVOID UserData,
        BOOL AsynchronousOpen,
        WINBIO_FRAMEWORK_HANDLE* FrameworkHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NotificationMethod", "TargetWindow", "MessageCode", "CallbackRoutine", "UserData", "AsynchronousOpen", "FrameworkHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioAsyncOpenSession(jitter):
    """
    HRESULT WinBioAsyncOpenSession(
        WINBIO_BIOMETRIC_TYPE Factor,
        WINBIO_POOL_TYPE PoolType,
        WINBIO_SESSION_FLAGS Flags,
        WINBIO_UNIT_ID* UnitArray,
        SIZE_T UnitCount,
        GUID* DatabaseId,
        WINBIO_ASYNC_NOTIFICATION_METHOD NotificationMethod,
        HWND TargetWindow,
        UINT MessageCode,
        PWINBIO_ASYNC_COMPLETION_CALLBACK CallbackRoutine,
        PVOID UserData,
        BOOL AsynchronousOpen,
        WINBIO_SESSION_HANDLE* SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Factor", "PoolType", "Flags", "UnitArray", "UnitCount", "DatabaseId", "NotificationMethod", "TargetWindow", "MessageCode", "CallbackRoutine", "UserData", "AsynchronousOpen", "SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioCancel(jitter):
    """
    HRESULT WinBioCancel(
        WINBIO_SESSION_HANDLE SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioCaptureSample(jitter):
    """
    HRESULT WinBioCaptureSample(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_BIR_PURPOSE Purpose,
        WINBIO_BIR_DATA_FLAGS Flags,
        WINBIO_UNIT_ID* UnitId,
        PWINBIO_BIR* Sample,
        SIZE_T* SampleSize,
        WINBIO_REJECT_DETAIL* RejectDetail
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "Purpose", "Flags", "UnitId", "Sample", "SampleSize", "RejectDetail"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioCaptureSampleWithCallback(jitter):
    """
    HRESULT WinBioCaptureSampleWithCallback(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_BIR_PURPOSE Purpose,
        WINBIO_BIR_DATA_FLAGS Flags,
        PWINBIO_CAPTURE_CALLBACK CaptureCallback,
        PVOID CaptureCallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "Purpose", "Flags", "CaptureCallback", "CaptureCallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioCloseFramework(jitter):
    """
    HRESULT WinBioCloseFramework(
        WINBIO_FRAMEWORK_HANDLE FrameworkHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FrameworkHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioCloseSession(jitter):
    """
    HRESULT WinBioCloseSession(
        WINBIO_SESSION_HANDLE SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioControlUnit(jitter):
    """
    HRESULT WinBioControlUnit(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID UnitId,
        WINBIO_COMPONENT Component,
        ULONG ControlCode,
        PUCHAR SendBuffer,
        SIZE_T SendBufferSize,
        PUCHAR ReceiveBuffer,
        SIZE_T ReceiveBufferSize,
        SIZE_T* ReceiveDataSize,
        ULONG* OperationStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId", "Component", "ControlCode", "SendBuffer", "SendBufferSize", "ReceiveBuffer", "ReceiveBufferSize", "ReceiveDataSize", "OperationStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioControlUnitPrivileged(jitter):
    """
    HRESULT WinBioControlUnitPrivileged(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID UnitId,
        WINBIO_COMPONENT Component,
        ULONG ControlCode,
        PUCHAR SendBuffer,
        SIZE_T SendBufferSize,
        PUCHAR ReceiveBuffer,
        SIZE_T ReceiveBufferSize,
        SIZE_T* ReceiveDataSize,
        ULONG* OperationStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId", "Component", "ControlCode", "SendBuffer", "SendBufferSize", "ReceiveBuffer", "ReceiveBufferSize", "ReceiveDataSize", "OperationStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioDeleteTemplate(jitter):
    """
    HRESULT WinBioDeleteTemplate(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID UnitId,
        WINBIO_IDENTITY* Identity,
        WINBIO_BIOMETRIC_SUBTYPE SubFactor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId", "Identity", "SubFactor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnrollBegin(jitter):
    """
    HRESULT WinBioEnrollBegin(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_BIOMETRIC_SUBTYPE SubFactor,
        WINBIO_UNIT_ID UnitId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "SubFactor", "UnitId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnrollCapture(jitter):
    """
    HRESULT WinBioEnrollCapture(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_REJECT_DETAIL* RejectDetail
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "RejectDetail"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnrollCaptureWithCallback(jitter):
    """
    HRESULT WinBioEnrollCaptureWithCallback(
        WINBIO_SESSION_HANDLE SessionHandle,
        PWINBIO_ENROLL_CAPTURE_CALLBACK EnrollCallback,
        PVOID EnrollCallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "EnrollCallback", "EnrollCallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnrollCommit(jitter):
    """
    HRESULT WinBioEnrollCommit(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_IDENTITY* Identity,
        BOOLEAN* IsNewTemplate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "Identity", "IsNewTemplate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnrollDiscard(jitter):
    """
    HRESULT WinBioEnrollDiscard(
        WINBIO_SESSION_HANDLE SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnumBiometricUnits(jitter):
    """
    HRESULT WinBioEnumBiometricUnits(
        WINBIO_BIOMETRIC_TYPE Factor,
        WINBIO_UNIT_SCHEMA** UnitSchemaArray,
        SIZE_T* UnitCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Factor", "UnitSchemaArray", "UnitCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnumDatabases(jitter):
    """
    HRESULT WinBioEnumDatabases(
        WINBIO_BIOMETRIC_TYPE Factor,
        WINBIO_STORAGE_SCHEMA** StorageSchemaArray,
        SIZE_T* StorageCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Factor", "StorageSchemaArray", "StorageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnumEnrollments(jitter):
    """
    HRESULT WinBioEnumEnrollments(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID UnitId,
        WINBIO_IDENTITY* Identity,
        WINBIO_BIOMETRIC_SUBTYPE** SubFactorArray,
        SIZE_T* SubFactorCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId", "Identity", "SubFactorArray", "SubFactorCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnumServiceProviders(jitter):
    """
    HRESULT WinBioEnumServiceProviders(
        WINBIO_BIOMETRIC_TYPE Factor,
        WINBIO_BSP_SCHEMA** BspSchemaArray,
        SIZE_T* BspCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Factor", "BspSchemaArray", "BspCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioFree(jitter):
    """
    HRESULT WinBioFree(
        PVOID Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioGetCredentialState(jitter):
    """
    HRESULT WinBioGetCredentialState(
        WINBIO_IDENTITY Identity,
        WINBIO_CREDENTIAL_TYPE Type,
        WINBIO_CREDENTIAL_STATE* CredentialState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Identity", "Type", "CredentialState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioGetDomainLogonSetting(jitter):
    """
    HRESULT WinBioGetDomainLogonSetting(
        BOOLEAN* Value,
        PWINBIO_SETTING_SOURCE_TYPE Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Value", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioGetEnabledSetting(jitter):
    """
    HRESULT WinBioGetEnabledSetting(
        BOOLEAN* Value,
        PWINBIO_SETTING_SOURCE_TYPE Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Value", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioGetLogonSetting(jitter):
    """
    HRESULT WinBioGetLogonSetting(
        BOOLEAN* Value,
        PWINBIO_SETTING_SOURCE_TYPE Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Value", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioGetProperty(jitter):
    """
    HRESULT WinBioGetProperty(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_PROPERTY_TYPE PropertyType,
        WINBIO_PROPERTY_ID PropertyId,
        WINBIO_UNIT_ID UnitId,
        WINBIO_IDENTITY* Identity,
        WINBIO_BIOMETRIC_SUBTYPE SubFactor,
        PVOID* PropertyBuffer,
        SIZE_T* PropertyBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "PropertyType", "PropertyId", "UnitId", "Identity", "SubFactor", "PropertyBuffer", "PropertyBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioIdentify(jitter):
    """
    HRESULT WinBioIdentify(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID* UnitId,
        WINBIO_IDENTITY* Identity,
        WINBIO_BIOMETRIC_SUBTYPE* SubFactor,
        WINBIO_REJECT_DETAIL* RejectDetail
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId", "Identity", "SubFactor", "RejectDetail"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioIdentifyWithCallback(jitter):
    """
    HRESULT WinBioIdentifyWithCallback(
        WINBIO_SESSION_HANDLE SessionHandle,
        PWINBIO_IDENTIFY_CALLBACK IdentifyCallback,
        PVOID IdentifyCallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "IdentifyCallback", "IdentifyCallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioLocateSensor(jitter):
    """
    HRESULT WinBioLocateSensor(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID* UnitId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioLocateSensorWithCallback(jitter):
    """
    HRESULT WinBioLocateSensorWithCallback(
        WINBIO_SESSION_HANDLE SessionHandle,
        PWINBIO_LOCATE_SENSOR_CALLBACK LocateCallback,
        PVOID LocateCallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "LocateCallback", "LocateCallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioLockUnit(jitter):
    """
    HRESULT WinBioLockUnit(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID UnitId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioLogonIdentifiedUser(jitter):
    """
    HRESULT WinBioLogonIdentifiedUser(
        WINBIO_SESSION_HANDLE SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioOpenSession(jitter):
    """
    HRESULT WinBioOpenSession(
        WINBIO_BIOMETRIC_TYPE Factor,
        WINBIO_POOL_TYPE PoolType,
        WINBIO_SESSION_FLAGS Flags,
        WINBIO_UNIT_ID* UnitArray,
        SIZE_T UnitCount,
        GUID* DatabaseId,
        WINBIO_SESSION_HANDLE* SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Factor", "PoolType", "Flags", "UnitArray", "UnitCount", "DatabaseId", "SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioRegisterEventMonitor(jitter):
    """
    HRESULT WinBioRegisterEventMonitor(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_EVENT_TYPE EventMask,
        PWINBIO_EVENT_CALLBACK EventCallback,
        PVOID EventCallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "EventMask", "EventCallback", "EventCallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioReleaseFocus(jitter):
    """
    HRESULT WinBioReleaseFocus()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioRemoveAllCredentials(jitter):
    """
    HRESULT WinBioRemoveAllCredentials()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioRemoveAllDomainCredentials(jitter):
    """
    HRESULT WinBioRemoveAllDomainCredentials()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioRemoveCredential(jitter):
    """
    HRESULT WinBioRemoveCredential(
        WINBIO_IDENTITY Identity,
        WINBIO_CREDENTIAL_TYPE Type
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Identity", "Type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioSetCredential(jitter):
    """
    HRESULT WinBioSetCredential(
        WINBIO_CREDENTIAL_TYPE Type,
        PUCHAR Credential,
        SIZE_T CredentialSize,
        WINBIO_CREDENTIAL_FORMAT Format
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Type", "Credential", "CredentialSize", "Format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioUnlockUnit(jitter):
    """
    HRESULT WinBioUnlockUnit(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID UnitId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioUnregisterEventMonitor(jitter):
    """
    HRESULT WinBioUnregisterEventMonitor(
        WINBIO_SESSION_HANDLE SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioVerify(jitter):
    """
    HRESULT WinBioVerify(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_IDENTITY* Identity,
        WINBIO_BIOMETRIC_SUBTYPE SubFactor,
        WINBIO_UNIT_ID* UnitId,
        BOOLEAN* Match,
        WINBIO_REJECT_DETAIL* RejectDetail
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "Identity", "SubFactor", "UnitId", "Match", "RejectDetail"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioVerifyWithCallback(jitter):
    """
    HRESULT WinBioVerifyWithCallback(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_IDENTITY* Identity,
        WINBIO_BIOMETRIC_SUBTYPE SubFactor,
        PWINBIO_VERIFY_CALLBACK VerifyCallback,
        PVOID VerifyCallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "Identity", "SubFactor", "VerifyCallback", "VerifyCallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioWait(jitter):
    """
    HRESULT WinBioWait(
        WINBIO_SESSION_HANDLE SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
