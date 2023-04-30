
def virtdisk_AddVirtualDiskParent(jitter):
    """
    [ERROR_CODE] AddVirtualDiskParent(
        HANDLE VirtualDiskHandle,
        PCWSTR ParentPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "ParentPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_AttachVirtualDisk(jitter):
    """
    [ERROR_CODE] AttachVirtualDisk(
        HANDLE VirtualDiskHandle,
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        ATTACH_VIRTUAL_DISK_FLAG Flags,
        ULONG ProviderSpecificFlags,
        PATTACH_VIRTUAL_DISK_PARAMETERS Parameters,
        LPOVERLAPPED Overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "SecurityDescriptor", "Flags", "ProviderSpecificFlags", "Parameters", "Overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_BreakMirrorVirtualDisk(jitter):
    """
    [ERROR_CODE] BreakMirrorVirtualDisk(
        HANDLE VirtualDiskHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_CompactVirtualDisk(jitter):
    """
    [ERROR_CODE] CompactVirtualDisk(
        HANDLE VirtualDiskHandle,
        COMPACT_VIRTUAL_DISK_FLAG Flags,
        PCOMPACT_VIRTUAL_DISK_PARAMETERS Parameters,
        LPOVERLAPPED Overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "Flags", "Parameters", "Overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_CreateVirtualDisk(jitter):
    """
    [ERROR_CODE] CreateVirtualDisk(
        PVIRTUAL_STORAGE_TYPE VirtualStorageType,
        PCWSTR Path,
        VIRTUAL_DISK_ACCESS_MASK VirtualDiskAccessMask,
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        CREATE_VIRTUAL_DISK_FLAG Flags,
        ULONG ProviderSpecificFlags,
        PCREATE_VIRTUAL_DISK_PARAMETERS Parameters,
        LPOVERLAPPED Overlapped,
        PHANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualStorageType", "Path", "VirtualDiskAccessMask", "SecurityDescriptor", "Flags", "ProviderSpecificFlags", "Parameters", "Overlapped", "Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_DeleteVirtualDiskMetadata(jitter):
    """
    [ERROR_CODE] DeleteVirtualDiskMetadata(
        HANDLE VirtualDiskHandle,
        LPGUID Item
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "Item"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_DetachVirtualDisk(jitter):
    """
    [ERROR_CODE] DetachVirtualDisk(
        HANDLE VirtualDiskHandle,
        DETACH_VIRTUAL_DISK_FLAG Flags,
        ULONG ProviderSpecificFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "Flags", "ProviderSpecificFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_EnumerateVirtualDiskMetadata(jitter):
    """
    [ERROR_CODE] EnumerateVirtualDiskMetadata(
        HANDLE VirtualDiskHandle,
        PULONG NumberOfItems,
        GUID* Items
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "NumberOfItems", "Items"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_ExpandVirtualDisk(jitter):
    """
    [ERROR_CODE] ExpandVirtualDisk(
        HANDLE VirtualDiskHandle,
        EXPAND_VIRTUAL_DISK_FLAG Flags,
        PEXPAND_VIRTUAL_DISK_PARAMETERS Parameters,
        LPOVERLAPPED Overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "Flags", "Parameters", "Overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_GetStorageDependencyInformation(jitter):
    """
    [ERROR_CODE] GetStorageDependencyInformation(
        HANDLE ObjectHandle,
        GET_STORAGE_DEPENDENCY_FLAG Flags,
        ULONG StorageDependencyInfoSize,
        PSTORAGE_DEPENDENCY_INFO StorageDependencyInfo,
        PULONG SizeUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectHandle", "Flags", "StorageDependencyInfoSize", "StorageDependencyInfo", "SizeUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_GetVirtualDiskInformation(jitter):
    """
    [ERROR_CODE] GetVirtualDiskInformation(
        HANDLE VirtualDiskHandle,
        PULONG VirtualDiskInfoSize,
        PGET_VIRTUAL_DISK_INFO VirtualDiskInfo,
        PULONG SizeUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "VirtualDiskInfoSize", "VirtualDiskInfo", "SizeUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_GetVirtualDiskMetadata(jitter):
    """
    [ERROR_CODE] GetVirtualDiskMetadata(
        HANDLE VirtualDiskHandle,
        LPGUID Item,
        PULONG MetaDataSize,
        PVOID MetaData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "Item", "MetaDataSize", "MetaData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_GetVirtualDiskOperationProgress(jitter):
    """
    [ERROR_CODE] GetVirtualDiskOperationProgress(
        HANDLE VirtualDiskHandle,
        LPOVERLAPPED Overlapped,
        PVIRTUAL_DISK_PROGRESS Progress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "Overlapped", "Progress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_GetVirtualDiskPhysicalPath(jitter):
    """
    [ERROR_CODE] GetVirtualDiskPhysicalPath(
        HANDLE VirtualDiskHandle,
        PULONG DiskPathSizeInBytes,
        PWSTR DiskPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "DiskPathSizeInBytes", "DiskPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_MergeVirtualDisk(jitter):
    """
    [ERROR_CODE] MergeVirtualDisk(
        HANDLE VirtualDiskHandle,
        MERGE_VIRTUAL_DISK_FLAG Flags,
        PMERGE_VIRTUAL_DISK_PARAMETERS Parameters,
        LPOVERLAPPED Overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "Flags", "Parameters", "Overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_MirrorVirtualDisk(jitter):
    """
    [ERROR_CODE] MirrorVirtualDisk(
        HANDLE VirtualDiskHandle,
        MIRROR_VIRTUAL_DISK_FLAG Flags,
        PMIRROR_VIRTUAL_DISK_PARAMETERS Parameters,
        LPOVERLAPPED Overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "Flags", "Parameters", "Overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_OpenVirtualDisk(jitter):
    """
    [ERROR_CODE] OpenVirtualDisk(
        PVIRTUAL_STORAGE_TYPE VirtualStorageType,
        PCWSTR Path,
        VIRTUAL_DISK_ACCESS_MASK VirtualDiskAccessMask,
        OPEN_VIRTUAL_DISK_FLAG Flags,
        POPEN_VIRTUAL_DISK_PARAMETERS Parameters,
        PHANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualStorageType", "Path", "VirtualDiskAccessMask", "Flags", "Parameters", "Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_ResizeVirtualDisk(jitter):
    """
    [ERROR_CODE] ResizeVirtualDisk(
        HANDLE VirtualDiskHandle,
        RESIZE_VIRTUAL_DISK_FLAG Flags,
        PRESIZE_VIRTUAL_DISK_PARAMETERS Parameters,
        LPOVERLAPPED Overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "Flags", "Parameters", "Overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_SetVirtualDiskInformation(jitter):
    """
    [ERROR_CODE] SetVirtualDiskInformation(
        HANDLE VirtualDiskHandle,
        PSET_VIRTUAL_DISK_INFO VirtualDiskInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "VirtualDiskInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def virtdisk_SetVirtualDiskMetadata(jitter):
    """
    [ERROR_CODE] SetVirtualDiskMetadata(
        HANDLE VirtualDiskHandle,
        LPGUID Item,
        ULONG MetaDataSize,
        PVOID MetaData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualDiskHandle", "Item", "MetaDataSize", "MetaData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
