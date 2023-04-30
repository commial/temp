###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def propsys_StgDeserializePropVariant(jitter):
    """
    WINOLEAPI StgDeserializePropVariant(
        SERIALIZEDPROPERTYVALUE* pprop,
        SERIALIZEDPROPERTYVALUE* cbMax,
        PROPVARIANT* pvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pprop", "cbMax", "pvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_StgSerializePropVariant(jitter):
    """
    WINOLEAPI StgSerializePropVariant(
        PROPVARIANT* pVar,
        SERIALIZEDPROPERTYVALUE** ppProp,
        SERIALIZEDPROPERTYVALUE* pcb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pVar", "ppProp", "pcb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSCoerceToCanonicalValue(jitter):
    """
    HRESULT PSCoerceToCanonicalValue(
        REFPROPERTYKEY key,
        PROPVARIANT* ppropvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["key", "ppropvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSCreateAdapterFromPropertyStore(jitter):
    """
    HRESULT PSCreateAdapterFromPropertyStore(
        IPropertyStore* pps,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pps", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSCreateDelayedMultiplexPropertyStore(jitter):
    """
    HRESULT PSCreateDelayedMultiplexPropertyStore(
        GETPROPERTYSTOREFLAGS flags,
        IDelayedPropertyStoreFactory* pdpsf,
        const DWORD* rgStoreIds,
        DWORD cStores,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "pdpsf", "rgStoreIds", "cStores", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSCreateMemoryPropertyStore(jitter):
    """
    HRESULT PSCreateMemoryPropertyStore(
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSCreateMultiplexPropertyStore(jitter):
    """
    HRESULT PSCreateMultiplexPropertyStore(
        IUnknown** prgpunkStores,
        DWORD cStores,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["prgpunkStores", "cStores", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSCreatePropertyChangeArray(jitter):
    """
    HRESULT PSCreatePropertyChangeArray(
        const PROPERTYKEY* rgpropkey,
        const PKA_FLAGS* rgflags,
        const PROPVARIANT* rgpropvar,
        UINT cChanges,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rgpropkey", "rgflags", "rgpropvar", "cChanges", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSCreatePropertyStoreFromObject(jitter):
    """
    HRESULT PSCreatePropertyStoreFromObject(
        IUnknown* punk,
        [STGM_FLAGS] grfMode,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk", "grfMode", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSCreatePropertyStoreFromPropertySetStorage(jitter):
    """
    HRESULT PSCreatePropertyStoreFromPropertySetStorage(
        IPropertySetStorage* ppss,
        [STGM_FLAGS] grfMode,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppss", "grfMode", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSCreateSimplePropertyChange(jitter):
    """
    HRESULT PSCreateSimplePropertyChange(
        PKA_FLAGS flags,
        REFPROPERTYKEY key,
        REFPROPVARIANT propvar,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "key", "propvar", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSEnumeratePropertyDescriptions(jitter):
    """
    PSSTDAPI PSEnumeratePropertyDescriptions(
        PROPDESC_ENUMFILTER filterOn,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["filterOn", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSFormatForDisplay(jitter):
    """
    HRESULT PSFormatForDisplay(
        REFPROPERTYKEY propkey,
        REFPROPVARIANT propvar,
        PROPDESC_FORMAT_FLAGS pdfFlags,
        LPWSTR pwszText,
        DWORD cchText
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["propkey", "propvar", "pdfFlags", "pwszText", "cchText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSFormatForDisplayAlloc(jitter):
    """
    HRESULT PSFormatForDisplayAlloc(
        REFPROPERTYKEY key,
        REFPROPVARIANT propvar,
        PROPDESC_FORMAT_FLAGS pdfFlags,
        PWSTR* ppszDisplay
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["key", "propvar", "pdfFlags", "ppszDisplay"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSFormatPropertyValue(jitter):
    """
    HRESULT PSFormatPropertyValue(
        IPropertyStore* pps,
        IPropertyDescription* ppd,
        PROPDESC_FORMAT_FLAGS pdff,
        LPWSTR* ppszDisplay
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pps", "ppd", "pdff", "ppszDisplay"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSGetItemPropertyHandler(jitter):
    """
    PSSTDAPI PSGetItemPropertyHandler(
        IUnknown* punkItem,
        BOOL fReadWrite,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punkItem", "fReadWrite", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSGetItemPropertyHandlerWithCreateObject(jitter):
    """
    PSSTDAPI PSGetItemPropertyHandlerWithCreateObject(
        IUnknown* punkItem,
        BOOL fReadWrite,
        IUnknown* punkCreateObject,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punkItem", "fReadWrite", "punkCreateObject", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSGetNamedPropertyFromPropertyStorage(jitter):
    """
    PSSTDAPI PSGetNamedPropertyFromPropertyStorage(
        PCUSERIALIZEDPROPSTORAGE psps,
        DWORD cb,
        LPCWSTR pszName,
        PROPVARIANT* ppropvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psps", "cb", "pszName", "ppropvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSGetNameFromPropertyKey(jitter):
    """
    HRESULT PSGetNameFromPropertyKey(
        REFPROPERTYKEY propkey,
        PWSTR* ppszCanonicalName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["propkey", "ppszCanonicalName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSGetPropertyDescription(jitter):
    """
    PSSTDAPI PSGetPropertyDescription(
        REFPROPERTYKEY propkey,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["propkey", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSGetPropertyDescriptionByName(jitter):
    """
    PSSTDAPI PSGetPropertyDescriptionByName(
        LPCWSTR pszCanonicalName,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszCanonicalName", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSGetPropertyDescriptionListFromString(jitter):
    """
    PSSTDAPI PSGetPropertyDescriptionListFromString(
        LPCWSTR pszPropList,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPropList", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSGetPropertyFromPropertyStorage(jitter):
    """
    PSSTDAPI PSGetPropertyFromPropertyStorage(
        PCUSERIALIZEDPROPSTORAGE psps,
        DWORD cb,
        REFPROPERTYKEY rpkey,
        PROPVARIANT** ppropvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psps", "cb", "rpkey", "ppropvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSGetPropertyKeyFromName(jitter):
    """
    HRESULT PSGetPropertyKeyFromName(
        PCWSTR pszName,
        PROPERTYKEY* ppropkey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszName", "ppropkey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSGetPropertySystem(jitter):
    """
    PSSTDAPI PSGetPropertySystem(
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSGetPropertyValue(jitter):
    """
    HRESULT PSGetPropertyValue(
        IPropertyStore* pps,
        IPropertyDescription* ppd,
        PROPVARIANT* ppropvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pps", "ppd", "ppropvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSLookupPropertyHandlerCLSID(jitter):
    """
    PSSTDAPI PSLookupPropertyHandlerCLSID(
        PCWSTR pszFilePath,
        CLSID* pclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFilePath", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSPropertyKeyFromString(jitter):
    """
    HRESULT PSPropertyKeyFromString(
        LPCWSTR pszString,
        PROPERTYKEY* pkey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszString", "pkey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSRegisterPropertySchema(jitter):
    """
    HRESULT PSRegisterPropertySchema(
        PCWSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSSetPropertyValue(jitter):
    """
    HRESULT PSSetPropertyValue(
        IPropertyStore* pps,
        IPropertyDescription* ppd,
        REFPROPVARIANT propvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pps", "ppd", "propvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSStringFromPropertyKey(jitter):
    """
    HRESULT PSStringFromPropertyKey(
        REFPROPERTYKEY pkey,
        LPWSTR psz,
        UINT cch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pkey", "psz", "cch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_PSUnregisterPropertySchema(jitter):
    """
    HRESULT PSUnregisterPropertySchema(
        PCWSTR pszPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_InitPropVariantFromGUIDAsBuffer(jitter):
    """
    HRESULT InitPropVariantFromGUIDAsBuffer(
        REFGUID guid,
        PROPVARIANT* ppropvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["guid", "ppropvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_InitPropVariantFromGUIDAsString(jitter):
    """
    HRESULT InitPropVariantFromGUIDAsString(
        REFGUID guid,
        PROPVARIANT* ppropvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["guid", "ppropvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_InitVariantFromGUIDAsBuffer(jitter):
    """
    HRESULT InitVariantFromGUIDAsBuffer(
        REFGUID guid,
        VARIANT* pvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["guid", "pvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def propsys_InitVariantFromGUIDAsString(jitter):
    """
    HRESULT InitVariantFromGUIDAsString(
        REFGUID guid,
        VARIANT* pvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["guid", "pvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
