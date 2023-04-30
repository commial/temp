###### Enums ######
MERGE_VIRTUAL_DISK_VERSION = {
    "MERGE_VIRTUAL_DISK_VERSION_UNSPECIFIED": 0,
    "MERGE_VIRTUAL_DISK_VERSION_1": 1,
}
MERGE_VIRTUAL_DISK_VERSION_INV = {
    0: "MERGE_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    1: "MERGE_VIRTUAL_DISK_VERSION_1",
}
SET_VIRTUAL_DISK_INFO_VERSION = {
    "SET_VIRTUAL_DISK_INFO_UNSPECIFIED": 0,
    "SET_VIRTUAL_DISK_INFO_PARENT_PATH": 1,
    "SET_VIRTUAL_DISK_INFO_IDENTIFIER": 2,
}
SET_VIRTUAL_DISK_INFO_VERSION_INV = {
    0: "SET_VIRTUAL_DISK_INFO_UNSPECIFIED",
    1: "SET_VIRTUAL_DISK_INFO_PARENT_PATH",
    2: "SET_VIRTUAL_DISK_INFO_IDENTIFIER",
}
CREATE_VIRTUAL_DISK_VERSION = {
    "CREATE_VIRTUAL_DISK_VERSION_UNSPECIFIED": 0,
    "CREATE_VIRTUAL_DISK_VERSION_1": 1,
}
CREATE_VIRTUAL_DISK_VERSION_INV = {
    0: "CREATE_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    1: "CREATE_VIRTUAL_DISK_VERSION_1",
}
OPEN_VIRTUAL_DISK_VERSION = {
    "OPEN_VIRTUAL_DISK_VERSION_UNSPECIFIED": 0,
    "OPEN_VIRTUAL_DISK_VERSION_1": 1,
}
OPEN_VIRTUAL_DISK_VERSION_INV = {
    0: "OPEN_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    1: "OPEN_VIRTUAL_DISK_VERSION_1",
}
EXPAND_VIRTUAL_DISK_VERSION = {
    "EXPAND_VIRTUAL_DISK_VERSION_UNSPECIFIED": 0,
    "EXPAND_VIRTUAL_DISK_VERSION_1": 1,
}
EXPAND_VIRTUAL_DISK_VERSION_INV = {
    0: "EXPAND_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    1: "EXPAND_VIRTUAL_DISK_VERSION_1",
}
COMPACT_VIRTUAL_DISK_VERSION = {
    "COMPACT_VIRTUAL_DISK_VERSION_UNSPECIFIED": 0,
    "COMPACT_VIRTUAL_DISK_VERSION_1": 1,
}
COMPACT_VIRTUAL_DISK_VERSION_INV = {
    0: "COMPACT_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    1: "COMPACT_VIRTUAL_DISK_VERSION_1",
}
ATTACH_VIRTUAL_DISK_VERSION = {
    "ATTACH_VIRTUAL_DISK_VERSION_UNSPECIFIED": 0,
    "ATTACH_VIRTUAL_DISK_VERSION_1": 1,
}
ATTACH_VIRTUAL_DISK_VERSION_INV = {
    0: "ATTACH_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    1: "ATTACH_VIRTUAL_DISK_VERSION_1",
}
MIRROR_VIRTUAL_DISK_VERSION = {
    "MIRROR_VIRTUAL_DISK_VERSION_UNSPECIFIED": 0,
    "MIRROR_VIRTUAL_DISK_VERSION_1": 1,
}
MIRROR_VIRTUAL_DISK_VERSION_INV = {
    0: "MIRROR_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    1: "MIRROR_VIRTUAL_DISK_VERSION_1",
}
RESIZE_VIRTUAL_DISK_VERSION = {
    "RESIZE_VIRTUAL_DISK_VERSION_UNSPECIFIED": 0,
    "RESIZE_VIRTUAL_DISK_VERSION_1": 1,
}
RESIZE_VIRTUAL_DISK_VERSION_INV = {
    0: "RESIZE_VIRTUAL_DISK_VERSION_UNSPECIFIED",
    1: "RESIZE_VIRTUAL_DISK_VERSION_1",
}

###################

###### Types ######
PSTORAGE_DEPENDENCY_INFO = LPVOID
PGET_VIRTUAL_DISK_INFO = LPVOID
MERGE_VIRTUAL_DISK_VERSION = UINT
_VirtMergeDepth_ = ULONG

class _MERGE_VIRTUAL_DISK_PARAMETERS_u_s1_(MemStruct):
    fields = [
        ("MergeDepth", _VirtMergeDepth_()),
    ]


class _MERGE_VIRTUAL_DISK_PARAMETERS_u_s2_(MemStruct):
    fields = [
        ("MergeSourceDepth", _VirtMergeDepth_()),
        ("MergeTargetDepth", _VirtMergeDepth_()),
    ]

_MERGE_VIRTUAL_DISK_PARAMETERS_u_ = Union([
    ("Version1", _MERGE_VIRTUAL_DISK_PARAMETERS_u_s1_),
    ("Version2", _MERGE_VIRTUAL_DISK_PARAMETERS_u_s2_),
])

class MERGE_VIRTUAL_DISK_PARAMETERS(MemStruct):
    fields = [
        ("Version", MERGE_VIRTUAL_DISK_VERSION()),
        (None, _MERGE_VIRTUAL_DISK_PARAMETERS_u_()),
    ]

PMERGE_VIRTUAL_DISK_PARAMETERS = Ptr("<I", MERGE_VIRTUAL_DISK_PARAMETERS())
SET_VIRTUAL_DISK_INFO_VERSION = UINT
_SET_VIRTUAL_DISK_INFO_u_ = Union([
    ("ParentFilePath", PCWSTR),
    ("UniqueIdentifier", GUID),
])

class SET_VIRTUAL_DISK_INFO(MemStruct):
    fields = [
        ("Version", SET_VIRTUAL_DISK_INFO_VERSION()),
        (None, _SET_VIRTUAL_DISK_INFO_u_()),
    ]

PSET_VIRTUAL_DISK_INFO = Ptr("<I", SET_VIRTUAL_DISK_INFO())
CREATE_VIRTUAL_DISK_VERSION = UINT
OPEN_VIRTUAL_DISK_FLAG = UINT

class VIRTUAL_STORAGE_TYPE(MemStruct):
    fields = [
        ("DeviceId", ULONG()),
        ("VendorId", GUID()),
    ]

PVIRTUAL_STORAGE_TYPE = Ptr("<I", VIRTUAL_STORAGE_TYPE())

class _CREATE_VIRTUAL_DISK_PARAMETERS_u_s1_(MemStruct):
    fields = [
        ("UniqueId", GUID()),
        ("MaximumSize", ULONGLONG()),
        ("BlockSizeInBytes", ULONG()),
        ("SectorSizeInBytes", ULONG()),
        ("ParentPath", PCWSTR()),
        ("SourcePath", PCWSTR()),
    ]


class _CREATE_VIRTUAL_DISK_PARAMETERS_u_s2_(MemStruct):
    fields = [
        ("UniqueId", GUID()),
        ("MaximumSize", ULONGLONG()),
        ("BlockSizeInBytes", ULONG()),
        ("SectorSizeInBytes", ULONG()),
        ("PhysicalSectorSizeInBytes", ULONG()),
        ("ParentPath", PCWSTR()),
        ("SourcePath", PCWSTR()),
        ("OpenFlags", OPEN_VIRTUAL_DISK_FLAG()),
        ("ParentVirtualStorageType", VIRTUAL_STORAGE_TYPE()),
        ("SourceVirtualStorageType", VIRTUAL_STORAGE_TYPE()),
        ("ResiliencyGuid", GUID()),
    ]

_CREATE_VIRTUAL_DISK_PARAMETERS_u_ = Union([
    ("Version1", _CREATE_VIRTUAL_DISK_PARAMETERS_u_s1_),
    ("Version2", _CREATE_VIRTUAL_DISK_PARAMETERS_u_s2_),
])

class CREATE_VIRTUAL_DISK_PARAMETERS(MemStruct):
    fields = [
        ("Version", CREATE_VIRTUAL_DISK_VERSION()),
        (None, _CREATE_VIRTUAL_DISK_PARAMETERS_u_()),
    ]

PCREATE_VIRTUAL_DISK_PARAMETERS = Ptr("<I", CREATE_VIRTUAL_DISK_PARAMETERS())
OPEN_VIRTUAL_DISK_VERSION = UINT

class _OPEN_VIRTUAL_DISK_PARAMETERS_u_s1_(MemStruct):
    fields = [
        ("RWDepth", ULONG()),
    ]


class _OPEN_VIRTUAL_DISK_PARAMETERS_u_s2_(MemStruct):
    fields = [
        ("GetInfoOnly", BOOL()),
        ("ReadOnly", BOOL()),
        ("ResiliencyGuid", GUID()),
    ]

_OPEN_VIRTUAL_DISK_PARAMETERS_u_ = Union([
    ("Version1", _OPEN_VIRTUAL_DISK_PARAMETERS_u_s1_),
    ("Version2", _OPEN_VIRTUAL_DISK_PARAMETERS_u_s2_),
])

class OPEN_VIRTUAL_DISK_PARAMETERS(MemStruct):
    fields = [
        ("Version", OPEN_VIRTUAL_DISK_VERSION()),
        (None, _OPEN_VIRTUAL_DISK_PARAMETERS_u_()),
    ]

POPEN_VIRTUAL_DISK_PARAMETERS = Ptr("<I", OPEN_VIRTUAL_DISK_PARAMETERS())
EXPAND_VIRTUAL_DISK_VERSION = UINT

class _EXPAND_VIRTUAL_DISK_PARAMETERS_u_s_(MemStruct):
    fields = [
        ("NewSize", ULONGLONG()),
    ]

_EXPAND_VIRTUAL_DISK_PARAMETERS_u_ = Union([
    ("Version1", _EXPAND_VIRTUAL_DISK_PARAMETERS_u_s_),
])

class EXPAND_VIRTUAL_DISK_PARAMETERS(MemStruct):
    fields = [
        ("Version", EXPAND_VIRTUAL_DISK_VERSION()),
        (None, _EXPAND_VIRTUAL_DISK_PARAMETERS_u_()),
    ]

PEXPAND_VIRTUAL_DISK_PARAMETERS = Ptr("<I", EXPAND_VIRTUAL_DISK_PARAMETERS())
COMPACT_VIRTUAL_DISK_VERSION = UINT

class _COMPACT_VIRTUAL_DISK_PARAMETERS_u_s_(MemStruct):
    fields = [
        ("Reserved", ULONG()),
    ]

_COMPACT_VIRTUAL_DISK_PARAMETERS_u_ = Union([
    ("Version1", _COMPACT_VIRTUAL_DISK_PARAMETERS_u_s_),
])

class COMPACT_VIRTUAL_DISK_PARAMETERS(MemStruct):
    fields = [
        ("Version", COMPACT_VIRTUAL_DISK_VERSION()),
        (None, _COMPACT_VIRTUAL_DISK_PARAMETERS_u_()),
    ]

PCOMPACT_VIRTUAL_DISK_PARAMETERS = Ptr("<I", COMPACT_VIRTUAL_DISK_PARAMETERS())
ATTACH_VIRTUAL_DISK_VERSION = UINT

class _ATTACH_VIRTUAL_DISK_PARAMETERS_u_s_(MemStruct):
    fields = [
        ("Reserved", ULONG()),
    ]

_ATTACH_VIRTUAL_DISK_PARAMETERS_u_ = Union([
    ("Version1", _ATTACH_VIRTUAL_DISK_PARAMETERS_u_s_),
])

class ATTACH_VIRTUAL_DISK_PARAMETERS(MemStruct):
    fields = [
        ("Version", ATTACH_VIRTUAL_DISK_VERSION()),
        (None, _ATTACH_VIRTUAL_DISK_PARAMETERS_u_()),
    ]

PATTACH_VIRTUAL_DISK_PARAMETERS = Ptr("<I", ATTACH_VIRTUAL_DISK_PARAMETERS())

class VIRTUAL_DISK_PROGRESS(MemStruct):
    fields = [
        ("OperationStatus", DWORD()),
        ("CurrentValue", ULONGLONG()),
        ("CompletionValue", ULONGLONG()),
    ]

PVIRTUAL_DISK_PROGRESS = Ptr("<I", VIRTUAL_DISK_PROGRESS())
ATTACH_VIRTUAL_DISK_FLAG = UINT
COMPACT_VIRTUAL_DISK_FLAG = UINT
DETACH_VIRTUAL_DISK_FLAG = UINT
EXPAND_VIRTUAL_DISK_FLAG = UINT
GET_STORAGE_DEPENDENCY_FLAG = UINT
MERGE_VIRTUAL_DISK_FLAG = UINT
CREATE_VIRTUAL_DISK_FLAG = UINT
VIRTUAL_DISK_ACCESS_MASK = UINT
MIRROR_VIRTUAL_DISK_FLAG = UINT
RESIZE_VIRTUAL_DISK_FLAG = UINT
MIRROR_VIRTUAL_DISK_VERSION = UINT
RESIZE_VIRTUAL_DISK_VERSION = UINT

class _MIRROR_VIRTUAL_DISK_PARAMETERS_s_(MemStruct):
    fields = [
        ("MirrorVirtualDiskPath", PCWSTR()),
    ]

_MIRROR_VIRTUAL_DISK_PARAMETERS_u_ = Union([
    ("Version1", _MIRROR_VIRTUAL_DISK_PARAMETERS_s_),
])

class MIRROR_VIRTUAL_DISK_PARAMETERS(MemStruct):
    fields = [
        ("Version", MIRROR_VIRTUAL_DISK_VERSION()),
        (None, _MIRROR_VIRTUAL_DISK_PARAMETERS_u_()),
    ]

PMIRROR_VIRTUAL_DISK_PARAMETERS = Ptr("<I", MIRROR_VIRTUAL_DISK_PARAMETERS())

class _RESIZE_VIRTUAL_DISK_PARAMETERS_s_(MemStruct):
    fields = [
        ("NewSize", ULONGLONG()),
    ]

_RESIZE_VIRTUAL_DISK_PARAMETERS_u_ = Union([
    ("Version1", _RESIZE_VIRTUAL_DISK_PARAMETERS_s_),
])

class RESIZE_VIRTUAL_DISK_PARAMETERS(MemStruct):
    fields = [
        ("Version", RESIZE_VIRTUAL_DISK_VERSION()),
        (None, _RESIZE_VIRTUAL_DISK_PARAMETERS_u_()),
    ]

PRESIZE_VIRTUAL_DISK_PARAMETERS = Ptr("<I", RESIZE_VIRTUAL_DISK_PARAMETERS())

###################

###### Functions ######

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
