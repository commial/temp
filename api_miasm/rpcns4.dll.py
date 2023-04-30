
def rpcns4_RpcNsBindingExport(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsBindingExport(unsigned long EntryNameSyntax, unsigned char* EntryName, RPC_IF_HANDLE IfSpec, RPC_BINDING_VECTOR* BindingVec, UUID_VECTOR* ObjectUuidVec)
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName", "IfSpec", "BindingVec", "ObjectUuidVec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsBindingExportA(jitter):
    rpcns4_RpcNsBindingExport(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsBindingExportW(jitter):
    rpcns4_RpcNsBindingExport(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsBindingExportPnP(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsBindingExportPnP(unsigned long EntryNameSyntax, unsigned char* EntryName, RPC_IF_HANDLE IfSpec, UUID_VECTOR* ObjectUuidVec)
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName", "IfSpec", "ObjectUuidVec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsBindingExportPnPA(jitter):
    rpcns4_RpcNsBindingExportPnP(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsBindingExportPnPW(jitter):
    rpcns4_RpcNsBindingExportPnP(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsBindingImportBegin(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsBindingImportBegin(unsigned long EntryNameSyntax, unsigned char* EntryName, RPC_IF_HANDLE IfSpec, UUID* ObjUuid, RPC_NS_HANDLE* ImportContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName", "IfSpec", "ObjUuid", "ImportContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsBindingImportBeginA(jitter):
    rpcns4_RpcNsBindingImportBegin(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsBindingImportBeginW(jitter):
    rpcns4_RpcNsBindingImportBegin(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsBindingImportDone(jitter):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsBindingImportDone(RPC_NS_HANDLE* ImportContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["ImportContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsBindingImportNext(jitter):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsBindingImportNext(RPC_NS_HANDLE ImportContext, RPC_BINDING_HANDLE* Binding)
    """
    ret_ad, args = jitter.func_args_stdcall(["ImportContext", "Binding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsBindingLookupBegin(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsBindingLookupBegin(unsigned long EntryNameSyntax, unsigned char* EntryName, RPC_IF_HANDLE IfSpec, UUID* ObjUuid, unsigned long BindingMaxCount, RPC_NS_HANDLE* LookupContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName", "IfSpec", "ObjUuid", "BindingMaxCount", "LookupContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsBindingLookupBeginA(jitter):
    rpcns4_RpcNsBindingLookupBegin(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsBindingLookupBeginW(jitter):
    rpcns4_RpcNsBindingLookupBegin(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsBindingLookupDone(jitter):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsBindingLookupDone(RPC_NS_HANDLE* LookupContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["LookupContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsBindingLookupNext(jitter):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsBindingLookupNext(RPC_NS_HANDLE LookupContext, RPC_BINDING_VECTOR** BindingVec)
    """
    ret_ad, args = jitter.func_args_stdcall(["LookupContext", "BindingVec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsBindingSelect(jitter):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsBindingSelect(RPC_BINDING_VECTOR* BindingVec, RPC_BINDING_HANDLE* Binding)
    """
    ret_ad, args = jitter.func_args_stdcall(["BindingVec", "Binding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsBindingUnexport(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsBindingUnexport(unsigned long EntryNameSyntax, unsigned char* EntryName, RPC_IF_HANDLE IfSpec, UUID_VECTOR* ObjectUuidVec)
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName", "IfSpec", "ObjectUuidVec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsBindingUnexportA(jitter):
    rpcns4_RpcNsBindingUnexport(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsBindingUnexportW(jitter):
    rpcns4_RpcNsBindingUnexport(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsBindingUnexportPnP(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsBindingUnexportPnP(unsigned long EntryNameSyntax, unsigned char* EntryName, RPC_IF_HANDLE IfSpec, UUID_VECTOR* ObjectUuidVec)
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName", "IfSpec", "ObjectUuidVec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsBindingUnexportPnPA(jitter):
    rpcns4_RpcNsBindingUnexportPnP(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsBindingUnexportPnPW(jitter):
    rpcns4_RpcNsBindingUnexportPnP(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsEntryExpandName(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsEntryExpandName(unsigned long EntryNameSyntax, unsigned char* EntryName, unsigned char** ExpandedName)
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName", "ExpandedName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsEntryExpandNameA(jitter):
    rpcns4_RpcNsEntryExpandName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsEntryExpandNameW(jitter):
    rpcns4_RpcNsEntryExpandName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsEntryObjectInqBegin(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsEntryObjectInqBegin(unsigned long EntryNameSyntax, unsigned char* EntryName, RPC_NS_HANDLE* InquiryContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName", "InquiryContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsEntryObjectInqBeginA(jitter):
    rpcns4_RpcNsEntryObjectInqBegin(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsEntryObjectInqBeginW(jitter):
    rpcns4_RpcNsEntryObjectInqBegin(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsEntryObjectInqDone(jitter):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsEntryObjectInqDone(RPC_NS_HANDLE* InquiryContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["InquiryContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsEntryObjectInqNext(jitter):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsEntryObjectInqNext(RPC_NS_HANDLE InquiryContext, UUID* ObjUuid)
    """
    ret_ad, args = jitter.func_args_stdcall(["InquiryContext", "ObjUuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsGroupDelete(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsGroupDelete(unsigned long GroupNameSyntax, unsigned char* GroupName)
    """
    ret_ad, args = jitter.func_args_stdcall(["GroupNameSyntax", "GroupName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsGroupDeleteA(jitter):
    rpcns4_RpcNsGroupDelete(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsGroupDeleteW(jitter):
    rpcns4_RpcNsGroupDelete(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsGroupMbrAdd(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsGroupMbrAdd(unsigned long GroupNameSyntax, unsigned char* GroupName, unsigned long MemberNameSyntax, unsigned char* MemberName)
    """
    ret_ad, args = jitter.func_args_stdcall(["GroupNameSyntax", "GroupName", "MemberNameSyntax", "MemberName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsGroupMbrAddA(jitter):
    rpcns4_RpcNsGroupMbrAdd(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsGroupMbrAddW(jitter):
    rpcns4_RpcNsGroupMbrAdd(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsGroupMbrInqBegin(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsGroupMbrInqBegin(unsigned long GroupNameSyntax, unsigned char* GroupName, unsigned long MemberNameSyntax, RPC_NS_HANDLE* InquiryContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["GroupNameSyntax", "GroupName", "MemberNameSyntax", "InquiryContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsGroupMbrInqBeginA(jitter):
    rpcns4_RpcNsGroupMbrInqBegin(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsGroupMbrInqBeginW(jitter):
    rpcns4_RpcNsGroupMbrInqBegin(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsGroupMbrInqDone(jitter):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsGroupMbrInqDone(RPC_NS_HANDLE* InquiryContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["InquiryContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsGroupMbrInqNext(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsGroupMbrInqNext(RPC_NS_HANDLE InquiryContext, unsigned char** MemberName)
    """
    ret_ad, args = jitter.func_args_stdcall(["InquiryContext", "MemberName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsGroupMbrInqNextA(jitter):
    rpcns4_RpcNsGroupMbrInqNext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsGroupMbrInqNextW(jitter):
    rpcns4_RpcNsGroupMbrInqNext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsGroupMbrRemove(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsGroupMbrRemove(unsigned long GroupNameSyntax, unsigned char* GroupName, unsigned long MemberNameSyntax, unsigned char* MemberName)
    """
    ret_ad, args = jitter.func_args_stdcall(["GroupNameSyntax", "GroupName", "MemberNameSyntax", "MemberName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsGroupMbrRemoveA(jitter):
    rpcns4_RpcNsGroupMbrRemove(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsGroupMbrRemoveW(jitter):
    rpcns4_RpcNsGroupMbrRemove(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsMgmtBindingUnexport(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsMgmtBindingUnexport(unsigned long EntryNameSyntax, unsigned char* EntryName, RPC_IF_ID* IfId, unsigned long VersOption, UUID_VECTOR* ObjectUuidVec)
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName", "IfId", "VersOption", "ObjectUuidVec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsMgmtBindingUnexportA(jitter):
    rpcns4_RpcNsMgmtBindingUnexport(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsMgmtBindingUnexportW(jitter):
    rpcns4_RpcNsMgmtBindingUnexport(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsMgmtEntryCreate(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsMgmtEntryCreate(unsigned long EntryNameSyntax, unsigned char* EntryName)
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsMgmtEntryCreateA(jitter):
    rpcns4_RpcNsMgmtEntryCreate(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsMgmtEntryCreateW(jitter):
    rpcns4_RpcNsMgmtEntryCreate(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsMgmtEntryDelete(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsMgmtEntryDelete(unsigned long EntryNameSyntax, unsigned char* EntryName)
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsMgmtEntryDeleteA(jitter):
    rpcns4_RpcNsMgmtEntryDelete(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsMgmtEntryDeleteW(jitter):
    rpcns4_RpcNsMgmtEntryDelete(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsMgmtEntryInqIfIds(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsMgmtEntryInqIfIds(unsigned long EntryNameSyntax, unsigned char* EntryName, RPC_IF_ID_VECTOR** IfIdVec)
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName", "IfIdVec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsMgmtEntryInqIfIdsA(jitter):
    rpcns4_RpcNsMgmtEntryInqIfIds(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsMgmtEntryInqIfIdsW(jitter):
    rpcns4_RpcNsMgmtEntryInqIfIds(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsMgmtHandleSetExpAge(jitter):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsMgmtHandleSetExpAge(RPC_NS_HANDLE NsHandle, unsigned long ExpirationAge)
    """
    ret_ad, args = jitter.func_args_stdcall(["NsHandle", "ExpirationAge"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsMgmtInqExpAge(jitter):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsMgmtInqExpAge(unsigned long* ExpirationAge)
    """
    ret_ad, args = jitter.func_args_stdcall(["ExpirationAge"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsMgmtSetExpAge(jitter):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsMgmtSetExpAge(unsigned long ExpirationAge)
    """
    ret_ad, args = jitter.func_args_stdcall(["ExpirationAge"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsProfileDelete(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsProfileDelete(unsigned long ProfileNameSyntax, unsigned char* ProfileName)
    """
    ret_ad, args = jitter.func_args_stdcall(["ProfileNameSyntax", "ProfileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsProfileDeleteA(jitter):
    rpcns4_RpcNsProfileDelete(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsProfileDeleteW(jitter):
    rpcns4_RpcNsProfileDelete(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsProfileEltAdd(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsProfileEltAdd(unsigned long ProfileNameSyntax, unsigned char* ProfileName, RPC_IF_ID* IfId, unsigned long MemberNameSyntax, unsigned char* MemberName, unsigned long Priority, unsigned char* Annotation)
    """
    ret_ad, args = jitter.func_args_stdcall(["ProfileNameSyntax", "ProfileName", "IfId", "MemberNameSyntax", "MemberName", "Priority", "Annotation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsProfileEltAddA(jitter):
    rpcns4_RpcNsProfileEltAdd(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsProfileEltAddW(jitter):
    rpcns4_RpcNsProfileEltAdd(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsProfileEltInqBegin(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsProfileEltInqBegin(unsigned long ProfileNameSyntax, unsigned char* ProfileName, unsigned long InquiryType, RPC_IF_ID* IfId, unsigned long VersOption, unsigned long MemberNameSyntax, unsigned char* MemberName, RPC_NS_HANDLE* InquiryContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["ProfileNameSyntax", "ProfileName", "InquiryType", "IfId", "VersOption", "MemberNameSyntax", "MemberName", "InquiryContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsProfileEltInqBeginA(jitter):
    rpcns4_RpcNsProfileEltInqBegin(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsProfileEltInqBeginW(jitter):
    rpcns4_RpcNsProfileEltInqBegin(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsProfileEltInqDone(jitter):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsProfileEltInqDone(RPC_NS_HANDLE* InquiryContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["InquiryContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsProfileEltInqNext(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsProfileEltInqNext(RPC_NS_HANDLE InquiryContext, RPC_IF_ID* IfId, unsigned char** MemberName, unsigned long* Priority, unsigned char** Annotation)
    """
    ret_ad, args = jitter.func_args_stdcall(["InquiryContext", "IfId", "MemberName", "Priority", "Annotation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsProfileEltInqNextA(jitter):
    rpcns4_RpcNsProfileEltInqNext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsProfileEltInqNextW(jitter):
    rpcns4_RpcNsProfileEltInqNext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcns4_RpcNsProfileEltRemove(jitter, get_str, set_str):
    """
    [RpcNS4.dll] RPC_STATUS RpcNsProfileEltRemove(unsigned long ProfileNameSyntax, unsigned char* ProfileName, RPC_IF_ID* IfId, unsigned long MemberNameSyntax, unsigned char* MemberName)
    """
    ret_ad, args = jitter.func_args_stdcall(["ProfileNameSyntax", "ProfileName", "IfId", "MemberNameSyntax", "MemberName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcns4_RpcNsProfileEltRemoveA(jitter):
    rpcns4_RpcNsProfileEltRemove(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcns4_RpcNsProfileEltRemoveW(jitter):
    rpcns4_RpcNsProfileEltRemove(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
