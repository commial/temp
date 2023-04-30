
def combase_CoEnterApplicationThreadLifetimeLoop(jitter):
    """
    void CoEnterApplicationThreadLifetimeLoop()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_CoGetApplicationThreadReference(jitter):
    """
    HRESULT CoGetApplicationThreadReference(
        IUnknown** ppThreadReference
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppThreadReference"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_CoWaitForMultipleObjects(jitter):
    """
    HRESULT CoWaitForMultipleObjects(
        DWORD dwFlags,
        DWORD dwTimeout,
        ULONG cHandles,
        LPHANDLE pHandles,
        LPDWORD lpdwIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "dwTimeout", "cHandles", "pHandles", "lpdwIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_GetRestrictedErrorInfo(jitter):
    """
    HRESULT GetRestrictedErrorInfo(
        IRestrictedErrorInfo** ppRestrictedErrorInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppRestrictedErrorInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_SetRestrictedErrorInfo(jitter):
    """
    HRESULT SetRestrictedErrorInfo(
        IRestrictedErrorInfo* pRestrictedErrorInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRestrictedErrorInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_CoDecodeProxy(jitter):
    """
    HRESULT CoDecodeProxy(
        DWORD dwClientPid,
        UINT64 ui64ProxyAddress,
        PServerInformation pServerInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwClientPid", "ui64ProxyAddress", "pServerInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserFree(jitter):
    """
    void HSTRING_UserFree(
        ULONG* pFlags,
        HSTRING* ppidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserFree64(jitter):
    """
    void HSTRING_UserFree64(
        ULONG* pFlags,
        HSTRING* ppidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserMarshal(jitter):
    """
    UCHAR* HSTRING_UserMarshal(
        ULONG* pFlags,
        UCHAR* pBuffer,
        HSTRING* ppidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserMarshal64(jitter):
    """
    UCHAR* HSTRING_UserMarshal64(
        ULONG* pFlags,
        UCHAR* pBuffer,
        HSTRING* ppidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserSize(jitter):
    """
    ULONG HSTRING_UserSize(
        ULONG* pFlags,
        ULONG StartingSize,
        HSTRING* ppidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "StartingSize", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserSize64(jitter):
    """
    ULONG HSTRING_UserSize64(
        ULONG* pFlags,
        ULONG StartingSize,
        HSTRING* ppidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "StartingSize", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserUnmarshal(jitter):
    """
    UCHAR* HSTRING_UserUnmarshal(
        ULONG* pFlags,
        UCHAR* pBuffer,
        HSTRING* ppidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserUnmarshal64(jitter):
    """
    UCHAR* HSTRING_UserUnmarshal64(
        ULONG* pFlags,
        UCHAR* pBuffer,
        HSTRING* ppidl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoActivateInstance(jitter):
    """
    HRESULT RoActivateInstance(
        HSTRING activatableClassId,
        IInspectable** instance
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["activatableClassId", "instance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoCaptureErrorContext(jitter):
    """
    HRESULT RoCaptureErrorContext(
        HRESULT hrError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoFailFastWithErrorContext(jitter):
    """
    void RoFailFastWithErrorContext(
        HRESULT hrError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hrError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoFreeParameterizedTypeExtra(jitter):
    """
    HRESULT RoFreeParameterizedTypeExtra(
        ROPARAMIIDHANDLE extra
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["extra"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoGetActivatableClassRegistration(jitter):
    """
    HRESULT RoGetActivatableClassRegistration(
        HSTRING activatableClassId,
        PActivatableClassRegistration* activatableClassRegistration
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["activatableClassId", "activatableClassRegistration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoGetActivationFactory(jitter):
    """
    HRESULT RoGetActivationFactory(
        HSTRING activatableClassId,
        REFIID iid,
        void** factory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["activatableClassId", "iid", "factory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoGetApartmentIdentifier(jitter):
    """
    HRESULT RoGetApartmentIdentifier(
        UINT64* apartmentIdentifier
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["apartmentIdentifier"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoGetErrorReportingFlags(jitter):
    """
    HRESULT RoGetErrorReportingFlags(
        RO_ERROR_REPORTING_FLAGS* pflags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pflags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoGetParameterizedTypeInstanceIID(jitter):
    """
    HRESULT RoGetParameterizedTypeInstanceIID(
        UINT32 nameElementCount,
        PCWSTR* nameElements,
        const IRoMetaDataLocator& metaDataLocator,
        GUID* iid,
        ROPARAMIIDHANDLE* pExtra
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nameElementCount", "nameElements", "metaDataLocator", "iid", "pExtra"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoGetServerActivatableClasses(jitter):
    """
    HRESULT RoGetServerActivatableClasses(
        HSTRING serverName,
        HSTRING** activatableClassIds,
        DWORD* count
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["serverName", "activatableClassIds", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoInitialize(jitter):
    """
    HRESULT RoInitialize(
        RO_INIT_TYPE initType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["initType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoOriginateError(jitter):
    """
    BOOL RoOriginateError(
        HRESULT error,
        HSTRING message
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["error", "message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoOriginateErrorW(jitter):
    """
    BOOL RoOriginateErrorW(
        HRESULT error,
        UINT cchMax,
        PCWSTR message
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["error", "cchMax", "message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoParameterizedTypeExtraGetTypeSignature(jitter):
    """
    HRESULT RoParameterizedTypeExtraGetTypeSignature(
        ROPARAMIIDHANDLE extra
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["extra"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoRegisterActivationFactories(jitter):
    """
    HRESULT RoRegisterActivationFactories(
        HSTRING* activatableClassIds,
        PFNGETACTIVATIONFACTORY* activationFactoryCallbacks,
        UINT32 count,
        RO_REGISTRATION_COOKIE* cookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["activatableClassIds", "activationFactoryCallbacks", "count", "cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoRegisterForApartmentShutdown(jitter):
    """
    HRESULT RoRegisterForApartmentShutdown(
        IApartmentShutdown* callbackObject,
        UINT64* apartmentIdentifier,
        APARTMENT_SHUTDOWN_REGISTRATION_COOKIE* regCookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["callbackObject", "apartmentIdentifier", "regCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoResolveRestrictedErrorInfoReference(jitter):
    """
    HRESULT RoResolveRestrictedErrorInfoReference(
        PCWSTR reference,
        IRestrictedErrorInfo** ppRestrictedErrorInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["reference", "ppRestrictedErrorInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoRevokeActivationFactories(jitter):
    """
    void RoRevokeActivationFactories(
        RO_REGISTRATION_COOKIE cookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoSetErrorReportingFlags(jitter):
    """
    HRESULT RoSetErrorReportingFlags(
        RO_ERROR_REPORTING_FLAGS flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoTransformError(jitter):
    """
    BOOL RoTransformError(
        HRESULT oldError,
        HRESULT newError,
        HSTRING message
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["oldError", "newError", "message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoTransformErrorW(jitter):
    """
    BOOL RoTransformErrorW(
        HRESULT oldError,
        HRESULT newError,
        UINT cchMax,
        PCWSTR message
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["oldError", "newError", "cchMax", "message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoUninitialize(jitter):
    """
    void RoUninitialize()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoUnregisterForApartmentShutdown(jitter):
    """
    HRESULT RoUnregisterForApartmentShutdown(
        APARTMENT_SHUTDOWN_REGISTRATION_COOKIE regCookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["regCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsCompareStringOrdinal(jitter):
    """
    HRESULT WindowsCompareStringOrdinal(
        HSTRING string1,
        HSTRING string2,
        INT32* result
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string1", "string2", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsConcatString(jitter):
    """
    HRESULT WindowsConcatString(
        HSTRING string1,
        HSTRING string2,
        HSTRING* newString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string1", "string2", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsCreateString(jitter):
    """
    HRESULT WindowsCreateString(
        LPCWSTR sourceString,
        UINT32 length,
        HSTRING* string
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sourceString", "length", "string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsCreateStringReference(jitter):
    """
    HRESULT WindowsCreateStringReference(
        PCWSTR sourceString,
        UINT32 length,
        HSTRING_HEADER* hstringHeader,
        HSTRING* string
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sourceString", "length", "hstringHeader", "string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsDeleteString(jitter):
    """
    HRESULT WindowsDeleteString(
        HSTRING string
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsDeleteStringBuffer(jitter):
    """
    HRESULT WindowsDeleteStringBuffer(
        HSTRING_BUFFER bufferHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bufferHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsDuplicateString(jitter):
    """
    HRESULT WindowsDuplicateString(
        HSTRING string,
        HSTRING* newString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsGetStringLen(jitter):
    """
    UINT32 WindowsGetStringLen(
        HSTRING string
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsGetStringRawBuffer(jitter):
    """
    PCWSTR WindowsGetStringRawBuffer(
        HSTRING string,
        UINT32* length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsInspectString(jitter):
    """
    HRESULT WindowsInspectString(
        UINT_PTR targetHString,
        USHORT machine,
        PINSPECT_HSTRING_CALLBACK callback,
        void* context,
        UINT32* length,
        UINT_PTR* targetStringAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["targetHString", "machine", "callback", "context", "length", "targetStringAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsIsStringEmpty(jitter):
    """
    BOOL WindowsIsStringEmpty(
        HSTRING string
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsPreallocateStringBuffer(jitter):
    """
    HRESULT WindowsPreallocateStringBuffer(
        UINT32 length,
        WCHAR** mutableBuffer,
        HSTRING_BUFFER* bufferHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["length", "mutableBuffer", "bufferHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsPromoteStringBuffer(jitter):
    """
    HRESULT WindowsPromoteStringBuffer(
        HSTRING_BUFFER bufferHandle,
        HSTRING* string
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bufferHandle", "string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsReplaceString(jitter):
    """
    HRESULT WindowsReplaceString(
        HSTRING string,
        HSTRING stringReplaced,
        HSTRING stringReplaceWith,
        HSTRING* newString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "stringReplaced", "stringReplaceWith", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsStringHasEmbeddedNull(jitter):
    """
    HRESULT WindowsStringHasEmbeddedNull(
        HSTRING string,
        BOOL* hasEmbedNull
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "hasEmbedNull"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsSubstring(jitter):
    """
    HRESULT WindowsSubstring(
        HSTRING string,
        UINT32 startIndex,
        HSTRING* newString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "startIndex", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsSubstringWithSpecifiedLength(jitter):
    """
    HRESULT WindowsSubstringWithSpecifiedLength(
        HSTRING string,
        UINT32 startIndex,
        UINT32 length,
        HSTRING* newString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "startIndex", "length", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsTrimStringEnd(jitter):
    """
    HRESULT WindowsTrimStringEnd(
        HSTRING string,
        HSTRING trimString,
        HSTRING* newString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "trimString", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsTrimStringStart(jitter):
    """
    HRESULT WindowsTrimStringStart(
        HSTRING string,
        HSTRING trimString,
        HSTRING* newString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "trimString", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_CoAllowUnmarshalerCLSID(jitter):
    """
    HRESULT CoAllowUnmarshalerCLSID(
        REFCLSID clsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
