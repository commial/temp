
def combase_CoEnterApplicationThreadLifetimeLoop(jitter):
    """
    [Combase.dll] void CoEnterApplicationThreadLifetimeLoop()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_CoGetApplicationThreadReference(jitter):
    """
    [Combase.dll] HRESULT CoGetApplicationThreadReference(IUnknown** ppThreadReference)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppThreadReference"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_CoWaitForMultipleObjects(jitter):
    """
    [Combase.dll] HRESULT CoWaitForMultipleObjects(DWORD dwFlags, DWORD dwTimeout, ULONG cHandles, LPHANDLE pHandles, LPDWORD lpdwIndex)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "dwTimeout", "cHandles", "pHandles", "lpdwIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_GetRestrictedErrorInfo(jitter):
    """
    [Combase.dll] HRESULT GetRestrictedErrorInfo(IRestrictedErrorInfo** ppRestrictedErrorInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppRestrictedErrorInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_SetRestrictedErrorInfo(jitter):
    """
    [Combase.dll] HRESULT SetRestrictedErrorInfo(IRestrictedErrorInfo* pRestrictedErrorInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["pRestrictedErrorInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_CoDecodeProxy(jitter):
    """
    [Combase.dll] HRESULT CoDecodeProxy(DWORD dwClientPid, UINT64 ui64ProxyAddress, PServerInformation pServerInformation)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwClientPid", "ui64ProxyAddress", "pServerInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserFree(jitter):
    """
    [Combase.dll] void HSTRING_UserFree(ULONG* pFlags, HSTRING* ppidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserFree64(jitter):
    """
    [Combase.dll] void HSTRING_UserFree64(ULONG* pFlags, HSTRING* ppidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserMarshal(jitter):
    """
    [Combase.dll] UCHAR* HSTRING_UserMarshal(ULONG* pFlags, UCHAR* pBuffer, HSTRING* ppidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserMarshal64(jitter):
    """
    [Combase.dll] UCHAR* HSTRING_UserMarshal64(ULONG* pFlags, UCHAR* pBuffer, HSTRING* ppidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserSize(jitter):
    """
    [Combase.dll] ULONG HSTRING_UserSize(ULONG* pFlags, ULONG StartingSize, HSTRING* ppidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "StartingSize", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserSize64(jitter):
    """
    [Combase.dll] ULONG HSTRING_UserSize64(ULONG* pFlags, ULONG StartingSize, HSTRING* ppidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "StartingSize", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserUnmarshal(jitter):
    """
    [Combase.dll] UCHAR* HSTRING_UserUnmarshal(ULONG* pFlags, UCHAR* pBuffer, HSTRING* ppidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_HSTRING_UserUnmarshal64(jitter):
    """
    [Combase.dll] UCHAR* HSTRING_UserUnmarshal64(ULONG* pFlags, UCHAR* pBuffer, HSTRING* ppidl)
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "ppidl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoActivateInstance(jitter):
    """
    [Combase.dll] HRESULT RoActivateInstance(HSTRING activatableClassId, IInspectable** instance)
    """
    ret_ad, args = jitter.func_args_stdcall(["activatableClassId", "instance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoCaptureErrorContext(jitter):
    """
    [Combase.dll] HRESULT RoCaptureErrorContext(HRESULT hrError)
    """
    ret_ad, args = jitter.func_args_stdcall(["hrError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoFailFastWithErrorContext(jitter):
    """
    [Combase.dll] void RoFailFastWithErrorContext(HRESULT hrError)
    """
    ret_ad, args = jitter.func_args_stdcall(["hrError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoFreeParameterizedTypeExtra(jitter):
    """
    [Combase.dll] HRESULT RoFreeParameterizedTypeExtra(ROPARAMIIDHANDLE extra)
    """
    ret_ad, args = jitter.func_args_stdcall(["extra"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoGetActivatableClassRegistration(jitter):
    """
    [Combase.dll] HRESULT RoGetActivatableClassRegistration(HSTRING activatableClassId, PActivatableClassRegistration* activatableClassRegistration)
    """
    ret_ad, args = jitter.func_args_stdcall(["activatableClassId", "activatableClassRegistration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoGetActivationFactory(jitter):
    """
    [Combase.dll] HRESULT RoGetActivationFactory(HSTRING activatableClassId, REFIID iid, void** factory)
    """
    ret_ad, args = jitter.func_args_stdcall(["activatableClassId", "iid", "factory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoGetApartmentIdentifier(jitter):
    """
    [Combase.dll] HRESULT RoGetApartmentIdentifier(UINT64* apartmentIdentifier)
    """
    ret_ad, args = jitter.func_args_stdcall(["apartmentIdentifier"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoGetErrorReportingFlags(jitter):
    """
    [Combase.dll] HRESULT RoGetErrorReportingFlags(RO_ERROR_REPORTING_FLAGS* pflags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pflags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoGetParameterizedTypeInstanceIID(jitter):
    """
    [Combase.dll] HRESULT RoGetParameterizedTypeInstanceIID(UINT32 nameElementCount, PCWSTR* nameElements, const IRoMetaDataLocator& metaDataLocator, GUID* iid, ROPARAMIIDHANDLE* pExtra)
    """
    ret_ad, args = jitter.func_args_stdcall(["nameElementCount", "nameElements", "metaDataLocator", "iid", "pExtra"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoGetServerActivatableClasses(jitter):
    """
    [Combase.dll] HRESULT RoGetServerActivatableClasses(HSTRING serverName, HSTRING** activatableClassIds, DWORD* count)
    """
    ret_ad, args = jitter.func_args_stdcall(["serverName", "activatableClassIds", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoInitialize(jitter):
    """
    [Combase.dll] HRESULT RoInitialize(RO_INIT_TYPE initType)
    """
    ret_ad, args = jitter.func_args_stdcall(["initType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoOriginateError(jitter):
    """
    [Combase.dll] BOOL RoOriginateError(HRESULT error, HSTRING message)
    """
    ret_ad, args = jitter.func_args_stdcall(["error", "message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoOriginateErrorW(jitter):
    """
    [Combase.dll] BOOL RoOriginateErrorW(HRESULT error, UINT cchMax, PCWSTR message)
    """
    ret_ad, args = jitter.func_args_stdcall(["error", "cchMax", "message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoParameterizedTypeExtraGetTypeSignature(jitter):
    """
    [Combase.dll] HRESULT RoParameterizedTypeExtraGetTypeSignature(ROPARAMIIDHANDLE extra)
    """
    ret_ad, args = jitter.func_args_stdcall(["extra"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoRegisterActivationFactories(jitter):
    """
    [Combase.dll] HRESULT RoRegisterActivationFactories(HSTRING* activatableClassIds, PFNGETACTIVATIONFACTORY* activationFactoryCallbacks, UINT32 count, RO_REGISTRATION_COOKIE* cookie)
    """
    ret_ad, args = jitter.func_args_stdcall(["activatableClassIds", "activationFactoryCallbacks", "count", "cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoRegisterForApartmentShutdown(jitter):
    """
    [Combase.dll] HRESULT RoRegisterForApartmentShutdown(IApartmentShutdown* callbackObject, UINT64* apartmentIdentifier, APARTMENT_SHUTDOWN_REGISTRATION_COOKIE* regCookie)
    """
    ret_ad, args = jitter.func_args_stdcall(["callbackObject", "apartmentIdentifier", "regCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoResolveRestrictedErrorInfoReference(jitter):
    """
    [Combase.dll] HRESULT RoResolveRestrictedErrorInfoReference(PCWSTR reference, IRestrictedErrorInfo** ppRestrictedErrorInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["reference", "ppRestrictedErrorInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoRevokeActivationFactories(jitter):
    """
    [Combase.dll] void RoRevokeActivationFactories(RO_REGISTRATION_COOKIE cookie)
    """
    ret_ad, args = jitter.func_args_stdcall(["cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoSetErrorReportingFlags(jitter):
    """
    [Combase.dll] HRESULT RoSetErrorReportingFlags(RO_ERROR_REPORTING_FLAGS flags)
    """
    ret_ad, args = jitter.func_args_stdcall(["flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoTransformError(jitter):
    """
    [Combase.dll] BOOL RoTransformError(HRESULT oldError, HRESULT newError, HSTRING message)
    """
    ret_ad, args = jitter.func_args_stdcall(["oldError", "newError", "message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoTransformErrorW(jitter):
    """
    [Combase.dll] BOOL RoTransformErrorW(HRESULT oldError, HRESULT newError, UINT cchMax, PCWSTR message)
    """
    ret_ad, args = jitter.func_args_stdcall(["oldError", "newError", "cchMax", "message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoUninitialize(jitter):
    """
    [Combase.dll] void RoUninitialize()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_RoUnregisterForApartmentShutdown(jitter):
    """
    [Combase.dll] HRESULT RoUnregisterForApartmentShutdown(APARTMENT_SHUTDOWN_REGISTRATION_COOKIE regCookie)
    """
    ret_ad, args = jitter.func_args_stdcall(["regCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsCompareStringOrdinal(jitter):
    """
    [Combase.dll] HRESULT WindowsCompareStringOrdinal(HSTRING string1, HSTRING string2, INT32* result)
    """
    ret_ad, args = jitter.func_args_stdcall(["string1", "string2", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsConcatString(jitter):
    """
    [Combase.dll] HRESULT WindowsConcatString(HSTRING string1, HSTRING string2, HSTRING* newString)
    """
    ret_ad, args = jitter.func_args_stdcall(["string1", "string2", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsCreateString(jitter):
    """
    [Combase.dll] HRESULT WindowsCreateString(LPCWSTR sourceString, UINT32 length, HSTRING* string)
    """
    ret_ad, args = jitter.func_args_stdcall(["sourceString", "length", "string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsCreateStringReference(jitter):
    """
    [Combase.dll] HRESULT WindowsCreateStringReference(PCWSTR sourceString, UINT32 length, HSTRING_HEADER* hstringHeader, HSTRING* string)
    """
    ret_ad, args = jitter.func_args_stdcall(["sourceString", "length", "hstringHeader", "string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsDeleteString(jitter):
    """
    [Combase.dll] HRESULT WindowsDeleteString(HSTRING string)
    """
    ret_ad, args = jitter.func_args_stdcall(["string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsDeleteStringBuffer(jitter):
    """
    [Combase.dll] HRESULT WindowsDeleteStringBuffer(HSTRING_BUFFER bufferHandle)
    """
    ret_ad, args = jitter.func_args_stdcall(["bufferHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsDuplicateString(jitter):
    """
    [Combase.dll] HRESULT WindowsDuplicateString(HSTRING string, HSTRING* newString)
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsGetStringLen(jitter):
    """
    [Combase.dll] UINT32 WindowsGetStringLen(HSTRING string)
    """
    ret_ad, args = jitter.func_args_stdcall(["string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsGetStringRawBuffer(jitter):
    """
    [Combase.dll] PCWSTR WindowsGetStringRawBuffer(HSTRING string, UINT32* length)
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsInspectString(jitter):
    """
    [Combase.dll] HRESULT WindowsInspectString(UINT_PTR targetHString, USHORT machine, PINSPECT_HSTRING_CALLBACK callback, void* context, UINT32* length, UINT_PTR* targetStringAddress)
    """
    ret_ad, args = jitter.func_args_stdcall(["targetHString", "machine", "callback", "context", "length", "targetStringAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsIsStringEmpty(jitter):
    """
    [Combase.dll] BOOL WindowsIsStringEmpty(HSTRING string)
    """
    ret_ad, args = jitter.func_args_stdcall(["string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsPreallocateStringBuffer(jitter):
    """
    [Combase.dll] HRESULT WindowsPreallocateStringBuffer(UINT32 length, WCHAR** mutableBuffer, HSTRING_BUFFER* bufferHandle)
    """
    ret_ad, args = jitter.func_args_stdcall(["length", "mutableBuffer", "bufferHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsPromoteStringBuffer(jitter):
    """
    [Combase.dll] HRESULT WindowsPromoteStringBuffer(HSTRING_BUFFER bufferHandle, HSTRING* string)
    """
    ret_ad, args = jitter.func_args_stdcall(["bufferHandle", "string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsReplaceString(jitter):
    """
    [Combase.dll] HRESULT WindowsReplaceString(HSTRING string, HSTRING stringReplaced, HSTRING stringReplaceWith, HSTRING* newString)
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "stringReplaced", "stringReplaceWith", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsStringHasEmbeddedNull(jitter):
    """
    [Combase.dll] HRESULT WindowsStringHasEmbeddedNull(HSTRING string, BOOL* hasEmbedNull)
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "hasEmbedNull"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsSubstring(jitter):
    """
    [Combase.dll] HRESULT WindowsSubstring(HSTRING string, UINT32 startIndex, HSTRING* newString)
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "startIndex", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsSubstringWithSpecifiedLength(jitter):
    """
    [Combase.dll] HRESULT WindowsSubstringWithSpecifiedLength(HSTRING string, UINT32 startIndex, UINT32 length, HSTRING* newString)
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "startIndex", "length", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsTrimStringEnd(jitter):
    """
    [Combase.dll] HRESULT WindowsTrimStringEnd(HSTRING string, HSTRING trimString, HSTRING* newString)
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "trimString", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_WindowsTrimStringStart(jitter):
    """
    [Combase.dll] HRESULT WindowsTrimStringStart(HSTRING string, HSTRING trimString, HSTRING* newString)
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "trimString", "newString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def combase_CoAllowUnmarshalerCLSID(jitter):
    """
    [Combase.dll] HRESULT CoAllowUnmarshalerCLSID(REFCLSID clsid)
    """
    ret_ad, args = jitter.func_args_stdcall(["clsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
