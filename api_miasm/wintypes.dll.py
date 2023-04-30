###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def wintypes_RoGetBufferMarshaler(jitter):
    """
    HRESULT RoGetBufferMarshaler(
        IMarshal** bufferMarshaler
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bufferMarshaler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintypes_RoGetMetaDataFile(jitter):
    """
    HRESULT RoGetMetaDataFile(
        const HSTRING name,
        IMetaDataDispenserEx* metaDataDispenser,
        HSTRING* metaDataFilePath,
        IMetaDataImport2** metaDataImport,
        mdTypeDef* typeDefToken
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["name", "metaDataDispenser", "metaDataFilePath", "metaDataImport", "typeDefToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintypes_RoParseTypeName(jitter):
    """
    HRESULT RoParseTypeName(
        HSTRING typename,
        DWORD* partsCount,
        HSTRING** typeNameParts
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["typename", "partsCount", "typeNameParts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wintypes_RoResolveNamespace(jitter):
    """
    HRESULT RoResolveNamespace(
        const HSTRING name,
        const HSTRING windowsMetaDataDir,
        const DWORD packageGraphDirsCount,
        const HSTRING* packageGraphDirs,
        DWORD* metaDataFilePathsCount,
        HSTRING** metaDataFilePaths,
        DWORD* subNamespacesCount,
        HSTRING** subNamespaces
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["name", "windowsMetaDataDir", "packageGraphDirsCount", "packageGraphDirs", "metaDataFilePathsCount", "metaDataFilePaths", "subNamespacesCount", "subNamespaces"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
