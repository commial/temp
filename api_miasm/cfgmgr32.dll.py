
def cfgmgr32_CM_Add_Empty_Log_Conf(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Add_Empty_Log_Conf(PLOG_CONF plcLogConf, DEVINST dnDevInst, PRIORITY Priority, [LogicalConfigFlags] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["plcLogConf", "dnDevInst", "Priority", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Add_Empty_Log_Conf_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Add_Empty_Log_Conf_Ex(PLOG_CONF plcLogConf, DEVINST dnDevInst, PRIORITY Priority, [LogicalConfigFlags] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["plcLogConf", "dnDevInst", "Priority", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Add_ID(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Add_ID(DEVINST dnDevInst, PTSTR pszID, [CM_ADD_ID_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "pszID", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Add_IDA(jitter):
    cfgmgr32_CM_Add_ID(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Add_IDW(jitter):
    cfgmgr32_CM_Add_ID(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Add_ID_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Add_ID_Ex(DEVINST dnDevInst, PTSTR pszID, [CM_ADD_ID_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "pszID", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Add_ID_ExA(jitter):
    cfgmgr32_CM_Add_ID_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Add_ID_ExW(jitter):
    cfgmgr32_CM_Add_ID_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Add_Res_Des(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Add_Res_Des(PRES_DES prdResDes, LOG_CONF lcLogConf, RESOURCEID ResourceID, PCVOID ResourceData, ULONG ResourceLen, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "lcLogConf", "ResourceID", "ResourceData", "ResourceLen", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Add_Res_Des_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Add_Res_Des_Ex(PRES_DES prdResDes, LOG_CONF lcLogConf, RESOURCEID ResourceID, PCVOID ResourceData, ULONG ResourceLen, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "lcLogConf", "ResourceID", "ResourceData", "ResourceLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Connect_Machine(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Connect_Machine(PCTSTR UNCServerName, PHMACHINE phMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["UNCServerName", "phMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Connect_MachineA(jitter):
    cfgmgr32_CM_Connect_Machine(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Connect_MachineW(jitter):
    cfgmgr32_CM_Connect_Machine(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Delete_Class_Key(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Delete_Class_Key(LPGUID ClassGuid, [CM_DELETE_CLASS_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_Device_Interface_Key(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Delete_Device_Interface_Key(LPCTSTR pszDeviceInterface, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_Device_Interface_KeyA(jitter):
    cfgmgr32_CM_Delete_Device_Interface_Key(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Delete_Device_Interface_KeyW(jitter):
    cfgmgr32_CM_Delete_Device_Interface_Key(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Delete_DevNode_Key(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Delete_DevNode_Key(DEVNODE dnDevNode, ULONG ulHardwareProfile, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevNode", "ulHardwareProfile", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Disable_DevNode(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Disable_DevNode(DEVINST dnDevInst, [CM_DISABLE_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Disconnect_Machine(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Disconnect_Machine(HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enable_DevNode(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Enable_DevNode(DEVINST dnDevInst, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enumerate_Classes(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Enumerate_Classes(ULONG ulClassIndex, LPGUID ClassGuid, [CM_ENUMERATE_CLASSES_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ulClassIndex", "ClassGuid", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enumerate_Classes_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Enumerate_Classes_Ex(ULONG ulClassIndex, LPGUID ClassGuid, [CM_ENUMERATE_CLASSES_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ulClassIndex", "ClassGuid", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enumerate_Enumerators(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Enumerate_Enumerators(ULONG ulEnumIndex, PTCHAR Buffer, PULONG pulLength, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ulEnumIndex", "Buffer", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enumerate_EnumeratorsA(jitter):
    cfgmgr32_CM_Enumerate_Enumerators(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Enumerate_EnumeratorsW(jitter):
    cfgmgr32_CM_Enumerate_Enumerators(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Enumerate_Enumerators_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Enumerate_Enumerators_Ex(ULONG ulEnumIndex, PTCHAR Buffer, PULONG pulLength, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ulEnumIndex", "Buffer", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enumerate_Enumerators_ExA(jitter):
    cfgmgr32_CM_Enumerate_Enumerators_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Enumerate_Enumerators_ExW(jitter):
    cfgmgr32_CM_Enumerate_Enumerators_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Free_Log_Conf(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Free_Log_Conf(LOG_CONF lcLogConfToBeFreed, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["lcLogConfToBeFreed", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Log_Conf_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Free_Log_Conf_Ex(LOG_CONF lcLogConfToBeFreed, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["lcLogConfToBeFreed", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Log_Conf_Handle(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Free_Log_Conf_Handle(LOG_CONF lcLogConf)
    """
    ret_ad, args = jitter.func_args_stdcall(["lcLogConf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Res_Des(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Free_Res_Des(PRES_DES prdResDes, RES_DES rdResDes, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "rdResDes", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Res_Des_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Free_Res_Des_Ex(PRES_DES prdResDes, RES_DES rdResDes, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "rdResDes", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Res_Des_Handle(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Free_Res_Des_Handle(RES_DES rdResDes)
    """
    ret_ad, args = jitter.func_args_stdcall(["rdResDes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Resource_Conflict_Handle(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Free_Resource_Conflict_Handle(CONFLICT_LIST clConflictList)
    """
    ret_ad, args = jitter.func_args_stdcall(["clConflictList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Child(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Child(PDEVINST pdnDevInst, DEVINST dnDevInst, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Child_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Child_Ex(PDEVINST pdnDevInst, DEVINST dnDevInst, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_PropertyW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Class_PropertyW(LPCGUID ClassGUID, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE* PropertyType, PBYTE PropertyBuffer, PULONG PropertyBufferSize, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGUID", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Property_Keys(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Class_Property_Keys(LPCGUID ClassGUID, DEVPROPKEY* PropertyKeyArray, PULONG PropertyKeyCount, [CM_CLASS_PROPERTY_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGUID", "PropertyKeyArray", "PropertyKeyCount", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Registry_Property(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Class_Registry_Property(LPGUID ClassGuid, [CM_CRP] ulProperty, PULONG pulRegDataType, PVOID Buffer, PULONG pulLength, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ulProperty", "pulRegDataType", "Buffer", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Registry_PropertyA(jitter):
    cfgmgr32_CM_Get_Class_Registry_Property(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Registry_PropertyW(jitter):
    cfgmgr32_CM_Get_Class_Registry_Property(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Depth(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Depth(PULONG pulDepth, DEVINST dnDevInst, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulDepth", "dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Depth_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Depth_Ex(PULONG pulDepth, DEVINST dnDevInst, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulDepth", "dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_ID(DEVINST dnDevInst, PTCHAR Buffer, ULONG BufferLen, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "Buffer", "BufferLen", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_IDA(jitter):
    cfgmgr32_CM_Get_Device_ID(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_IDW(jitter):
    cfgmgr32_CM_Get_Device_ID(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_ID_Ex(DEVINST dnDevInst, PTCHAR Buffer, ULONG BufferLen, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "Buffer", "BufferLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID_ExA(jitter):
    cfgmgr32_CM_Get_Device_ID_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_ExW(jitter):
    cfgmgr32_CM_Get_Device_ID_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_ID_List(PCTSTR pszFilter, PTCHAR Buffer, ULONG BufferLen, [CM_GETIDLIST_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFilter", "Buffer", "BufferLen", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID_ListA(jitter):
    cfgmgr32_CM_Get_Device_ID_List(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_ListW(jitter):
    cfgmgr32_CM_Get_Device_ID_List(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_ID_List_Ex(PCTSTR pszFilter, PTCHAR Buffer, ULONG BufferLen, [CM_GETIDLIST_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFilter", "Buffer", "BufferLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID_List_ExA(jitter):
    cfgmgr32_CM_Get_Device_ID_List_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List_ExW(jitter):
    cfgmgr32_CM_Get_Device_ID_List_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List_Size(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_ID_List_Size(PULONG pulLen, PCTSTR pszFilter, [CM_GETIDLIST_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulLen", "pszFilter", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID_List_SizeA(jitter):
    cfgmgr32_CM_Get_Device_ID_List_Size(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List_SizeW(jitter):
    cfgmgr32_CM_Get_Device_ID_List_Size(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List_Size_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_ID_List_Size_Ex(PULONG pulLen, PCTSTR pszFilter, [CM_GETIDLIST_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulLen", "pszFilter", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID_List_Size_ExA(jitter):
    cfgmgr32_CM_Get_Device_ID_List_Size_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_List_Size_ExW(jitter):
    cfgmgr32_CM_Get_Device_ID_List_Size_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_ID_Size(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_ID_Size(PULONG pulLen, DEVINST dnDevInst, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulLen", "dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_ID_Size_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_ID_Size_Ex(PULONG pulLen, DEVINST dnDevInst, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulLen", "dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_List(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_Interface_List(LPGUID InterfaceClassGuid, DEVINSTID pDeviceID, PTCHAR Buffer, ULONG BufferLen, [CM_GET_DEVICE_INTERFACE_LIST_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceClassGuid", "pDeviceID", "Buffer", "BufferLen", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_ListA(jitter):
    cfgmgr32_CM_Get_Device_Interface_List(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_ListW(jitter):
    cfgmgr32_CM_Get_Device_Interface_List(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_List_Size(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_Interface_List_Size(PULONG pulLen, LPGUID InterfaceClassGuid, DEVINSTID pDeviceID, [CM_GET_DEVICE_INTERFACE_LIST_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulLen", "InterfaceClassGuid", "pDeviceID", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_List_SizeA(jitter):
    cfgmgr32_CM_Get_Device_Interface_List_Size(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_List_SizeW(jitter):
    cfgmgr32_CM_Get_Device_Interface_List_Size(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_PropertyW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_Interface_PropertyW(LPCWSTR pszDeviceInterface, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE* PropertyType, PBYTE PropertyBuffer, PULONG PropertyBufferSize, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_Property_KeysW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_Interface_Property_KeysW(LPCWSTR pszDeviceInterface, DEVPROPKEY* PropertyKeyArray, PULONG PropertyKeyCount, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "PropertyKeyArray", "PropertyKeyCount", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_PropertyW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_DevNode_PropertyW(DEVINST dnDevInst, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE* PropertyType, PBYTE PropertyBuffer, PULONG PropertyBufferSize, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Property_Keys(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_DevNode_Property_Keys(DEVINST dnDevInst, DEVPROPKEY* PropertyKeyArray, PULONG PropertyKeyCount, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "PropertyKeyArray", "PropertyKeyCount", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Registry_Property(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_DevNode_Registry_Property(DEVINST dnDevInst, [CM_DRP] ulProperty, PULONG pulRegDataType, PVOID Buffer, PULONG pulLength, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulProperty", "pulRegDataType", "Buffer", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Registry_PropertyA(jitter):
    cfgmgr32_CM_Get_DevNode_Registry_Property(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_DevNode_Registry_PropertyW(jitter):
    cfgmgr32_CM_Get_DevNode_Registry_Property(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_DevNode_Status(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_DevNode_Status([DN_FLAGS*] pulStatus, [CmProblemNumber*] pulProblemNumber, DEVINST dnDevInst, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulStatus", "pulProblemNumber", "dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Status_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_DevNode_Status_Ex([DN_FLAGS*] pulStatus, [CmProblemNumber*] pulProblemNumber, DEVINST dnDevInst, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulStatus", "pulProblemNumber", "dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_First_Log_Conf(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_First_Log_Conf(PLOG_CONF plcLogConf, DEVINST dnDevInst, [LogicalConfigFlags] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["plcLogConf", "dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_First_Log_Conf_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_First_Log_Conf_Ex(PLOG_CONF plcLogConf, DEVINST dnDevInst, [LogicalConfigFlags] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["plcLogConf", "dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_HW_Prof_Flags(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_HW_Prof_Flags(DEVINSTID pDeviceID, [CsConfigFlags*] pulValue, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pDeviceID", "pulValue", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_HW_Prof_FlagsA(jitter):
    cfgmgr32_CM_Get_HW_Prof_Flags(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_HW_Prof_FlagsW(jitter):
    cfgmgr32_CM_Get_HW_Prof_Flags(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_HW_Prof_Flags_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_HW_Prof_Flags_Ex(DEVINSTID pDeviceID, ULONG ulHardwareProfile, [CsConfigFlags*] pulValue, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pDeviceID", "ulHardwareProfile", "pulValue", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_HW_Prof_Flags_ExA(jitter):
    cfgmgr32_CM_Get_HW_Prof_Flags_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_HW_Prof_Flags_ExW(jitter):
    cfgmgr32_CM_Get_HW_Prof_Flags_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Log_Conf_Priority(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Log_Conf_Priority(LOG_CONF lcLogConf, PPRIORITY pPriority, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["lcLogConf", "pPriority", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Log_Conf_Priority_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Log_Conf_Priority_Ex(LOG_CONF lcLogConf, PPRIORITY pPriority, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["lcLogConf", "pPriority", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Next_Log_Conf(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Next_Log_Conf(PLOG_CONF plcLogConf, LOG_CONF lcLogConf, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["plcLogConf", "lcLogConf", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Next_Log_Conf_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Next_Log_Conf_Ex(PLOG_CONF plcLogConf, LOG_CONF lcLogConf, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["plcLogConf", "lcLogConf", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Next_Res_Des(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Next_Res_Des(PRES_DES prdResDes, RES_DES rdResDes, RESOURCEID ForResource, PRESOURCEID pResourceID, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "rdResDes", "ForResource", "pResourceID", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Next_Res_Des_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Next_Res_Des_Ex(PRES_DES prdResDes, RES_DES rdResDes, RESOURCEID ForResource, PRESOURCEID pResourceID, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "rdResDes", "ForResource", "pResourceID", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Parent(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Parent(PDEVINST pdnDevInst, DEVINST dnDevInst, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Parent_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Parent_Ex(PDEVINST pdnDevInst, DEVINST dnDevInst, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Res_Des_Data(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Res_Des_Data(RES_DES rdResDes, PVOID Buffer, ULONG BufferLen, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["rdResDes", "Buffer", "BufferLen", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Res_Des_Data_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Res_Des_Data_Ex(RES_DES rdResDes, PVOID Buffer, ULONG BufferLen, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["rdResDes", "Buffer", "BufferLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Res_Des_Data_Size(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Res_Des_Data_Size(PULONG pulSize, RES_DES rdResDes, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulSize", "rdResDes", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Res_Des_Data_Size_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Res_Des_Data_Size_Ex(PULONG pulSize, RES_DES rdResDes, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulSize", "rdResDes", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Resource_Conflict_Count(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Resource_Conflict_Count(CONFLICT_LIST clConflictList, PULONG pulCount)
    """
    ret_ad, args = jitter.func_args_stdcall(["clConflictList", "pulCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Resource_Conflict_Details(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Resource_Conflict_Details(CONFLICT_LIST clConflictList, ULONG ulIndex, PCONFLICT_DETAILS pConflictDetails)
    """
    ret_ad, args = jitter.func_args_stdcall(["clConflictList", "ulIndex", "pConflictDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Resource_Conflict_DetailsA(jitter):
    cfgmgr32_CM_Get_Resource_Conflict_Details(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Resource_Conflict_DetailsW(jitter):
    cfgmgr32_CM_Get_Resource_Conflict_Details(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Sibling(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Sibling(PDEVINST pdnDevInst, DEVINST DevInst, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "DevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Sibling_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Sibling_Ex(PDEVINST pdnDevInst, DEVINST DevInst, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "DevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Version(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Version()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Version_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Version_Ex(HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Is_Dock_Station_Present(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Is_Dock_Station_Present(PBOOL pbPresent)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbPresent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Is_Dock_Station_Present_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Is_Dock_Station_Present_Ex(PBOOL pbPresent, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbPresent", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Is_Version_Available(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Is_Version_Available(WORD wVersion)
    """
    ret_ad, args = jitter.func_args_stdcall(["wVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Is_Version_Available_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Is_Version_Available_Ex(WORD wVersion, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["wVersion", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Locate_DevNode(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Locate_DevNode(PDEVINST pdnDevInst, DEVINSTID pDeviceID, [CM_Locate_DevNode_Flags] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "pDeviceID", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Locate_DevNodeA(jitter):
    cfgmgr32_CM_Locate_DevNode(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Locate_DevNodeW(jitter):
    cfgmgr32_CM_Locate_DevNode(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Locate_DevNode_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Locate_DevNode_Ex(PDEVINST pdnDevInst, DEVINSTID pDeviceID, [CM_Locate_DevNode_Flags] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "pDeviceID", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Locate_DevNode_ExA(jitter):
    cfgmgr32_CM_Locate_DevNode_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Locate_DevNode_ExW(jitter):
    cfgmgr32_CM_Locate_DevNode_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Modify_Res_Des(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Modify_Res_Des(PRES_DES prdResDes, RES_DES rdResDes, RESOURCEID ResourceID, PCVOID ResourceData, ULONG ResourceLen, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "rdResDes", "ResourceID", "ResourceData", "ResourceLen", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Modify_Res_Des_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Modify_Res_Des_Ex(PRES_DES prdResDes, RES_DES rdResDes, RESOURCEID ResourceID, PCVOID ResourceData, ULONG ResourceLen, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["prdResDes", "rdResDes", "ResourceID", "ResourceData", "ResourceLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Class_Key(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Open_Class_Key(LPGUID ClassGuid, LPCTSTR pszClassName, REGSAM samDesired, REGDISPOSITION Disposition, PHKEY phkClass, [CM_OPEN_CLASS_KEY_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "pszClassName", "samDesired", "Disposition", "phkClass", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Class_KeyA(jitter):
    cfgmgr32_CM_Open_Class_Key(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Open_Class_KeyW(jitter):
    cfgmgr32_CM_Open_Class_Key(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Open_Device_Interface_Key(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Open_Device_Interface_Key(LPCTSTR pszDeviceInterface, REGSAM samDesired, REGDISPOSITION Disposition, PHKEY phkDeviceInterface, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "samDesired", "Disposition", "phkDeviceInterface", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Device_Interface_KeyA(jitter):
    cfgmgr32_CM_Open_Device_Interface_Key(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Open_Device_Interface_KeyW(jitter):
    cfgmgr32_CM_Open_Device_Interface_Key(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Open_DevNode_Key(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Open_DevNode_Key(DEVINST dnDevNode, REGSAM samDesired, ULONG ulHardwareProfile, REGDISPOSITION Disposition, PHKEY phkDevice, [CM_REGISTRY_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevNode", "samDesired", "ulHardwareProfile", "Disposition", "phkDevice", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_And_Remove_SubTree(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Query_And_Remove_SubTree(DEVINST dnAncestor, PPNP_VETO_TYPE pVetoType, LPTSTR pszVetoName, ULONG ulNameLength, [CM_REMOVE_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnAncestor", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_And_Remove_SubTreeA(jitter):
    cfgmgr32_CM_Query_And_Remove_SubTree(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Query_And_Remove_SubTreeW(jitter):
    cfgmgr32_CM_Query_And_Remove_SubTree(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Query_And_Remove_SubTree_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Query_And_Remove_SubTree_Ex(DEVINST dnAncestor, PPNP_VETO_TYPE pVetoType, LPTSTR pszVetoName, ULONG ulNameLength, [CM_REMOVE_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnAncestor", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_And_Remove_SubTree_ExA(jitter):
    cfgmgr32_CM_Query_And_Remove_SubTree_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Query_And_Remove_SubTree_ExW(jitter):
    cfgmgr32_CM_Query_And_Remove_SubTree_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Query_Resource_Conflict_List(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Query_Resource_Conflict_List(PCONFLICT_LIST pclConflictList, DEVINST dnDevInst, RESOURCEID ResourceID, PCVOID ResourceData, ULONG ResourceLen, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pclConflictList", "dnDevInst", "ResourceID", "ResourceData", "ResourceLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Reenumerate_DevNode(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Reenumerate_DevNode(DEVINST dnDevInst, [CM_REENUMERATE_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Reenumerate_DevNode_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Reenumerate_DevNode_Ex(DEVINST dnDevInst, [CM_REENUMERATE_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Register_Notification(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Register_Notification(PCM_NOTIFY_FILTER pFilter, PVOID pContext, PCM_NOTIFY_CALLBACK pCallback, PHCMNOTIFICATION pNotifyContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["pFilter", "pContext", "pCallback", "pNotifyContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Request_Device_Eject(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Request_Device_Eject(DEVINST dnDevInst, PPNP_VETO_TYPE pVetoType, LPTSTR pszVetoName, ULONG ulNameLength, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Request_Device_EjectA(jitter):
    cfgmgr32_CM_Request_Device_Eject(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Request_Device_EjectW(jitter):
    cfgmgr32_CM_Request_Device_Eject(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Request_Device_Eject_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Request_Device_Eject_Ex(DEVINST dnDevInst, PPNP_VETO_TYPE pVetoType, LPTSTR pszVetoName, ULONG ulNameLength, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "pVetoType", "pszVetoName", "ulNameLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Request_Device_Eject_ExA(jitter):
    cfgmgr32_CM_Request_Device_Eject_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Request_Device_Eject_ExW(jitter):
    cfgmgr32_CM_Request_Device_Eject_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Request_Eject_PC(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Request_Eject_PC()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Request_Eject_PC_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Request_Eject_PC_Ex(HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_Class_PropertyW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_Class_PropertyW(LPCGUID ClassGUID, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE PropertyType, CONST PBYTE PropertyBuffer, ULONG PropertyBufferSize, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGUID", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_Class_Registry_Property(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_Class_Registry_Property(LPGUID ClassGuid, [CM_CRP] ulProperty, PCVOID Buffer, ULONG ulLength, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ulProperty", "Buffer", "ulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_Class_Registry_PropertyA(jitter):
    cfgmgr32_CM_Set_Class_Registry_Property(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Set_Class_Registry_PropertyW(jitter):
    cfgmgr32_CM_Set_Class_Registry_Property(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Set_Device_Interface_PropertyW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_Device_Interface_PropertyW(LPCWSTR pszDeviceInterface, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE PropertyType, CONST PBYTE PropertyBuffer, ULONG PropertyBufferSize, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Problem(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_DevNode_Problem(DEVINST dnDevInst, [CmProblemNumber] ulProblem, [CM_SET_DEVNODE_PROBLEM_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulProblem", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Problem_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_DevNode_Problem_Ex(DEVINST dnDevInst, [CmProblemNumber] ulProblem, [CM_SET_DEVNODE_PROBLEM_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulProblem", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_PropertyW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_DevNode_PropertyW(DEVINST dnDevInst, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE PropertyType, CONST PBYTE PropertyBuffer, ULONG PropertyBufferSize, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Registry_Property(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_DevNode_Registry_Property(DEVINST dnDevInst, [CM_DRP] ulProperty, PCVOID Buffer, ULONG ulLength, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulProperty", "Buffer", "ulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Registry_PropertyA(jitter):
    cfgmgr32_CM_Set_DevNode_Registry_Property(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Set_DevNode_Registry_PropertyW(jitter):
    cfgmgr32_CM_Set_DevNode_Registry_Property(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Setup_DevNode(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Setup_DevNode(DEVINST dnDevInst, [CM_SETUP_DEVNODE_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Uninstall_DevNode(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Uninstall_DevNode(DEVNODE dnDevInst, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Unregister_Notification(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Unregister_Notification(HCMNOTIFICATION NotifyContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["NotifyContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_WaitNoPendingInstallEvents(jitter):
    """
    [CfgMgr32.dll] [WAIT_RESULT] CM_WaitNoPendingInstallEvents(DWORD dwTimeout)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CMP_WaitNoPendingInstallEvents(jitter):
    """
    [CfgMgr32.dll] [WAIT_RESULT] CMP_WaitNoPendingInstallEvents(DWORD dwTimeout)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Add_Range(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Add_Range(DWORDLONG ullStartValue, DWORDLONG ullEndValue, RANGE_LIST rlh, [CM_ADD_RANGE_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ullStartValue", "ullEndValue", "rlh", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Create_DevNode(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Create_DevNode(PDEVINST pdnDevInst, DEVINSTID pDeviceID, DEVINST dnParent, [CM_CREATE_DEVNODE_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "pDeviceID", "dnParent", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Create_DevNodeA(jitter):
    cfgmgr32_CM_Create_DevNode(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Create_DevNodeW(jitter):
    cfgmgr32_CM_Create_DevNode(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Create_DevNode_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Create_DevNode_Ex(PDEVINST pdnDevInst, DEVINSTID pDeviceID, DEVINST dnParent, [CM_CREATE_DEVNODE_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdnDevInst", "pDeviceID", "dnParent", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Create_DevNode_ExA(jitter):
    cfgmgr32_CM_Create_DevNode_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Create_DevNode_ExW(jitter):
    cfgmgr32_CM_Create_DevNode_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Create_Range_List(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Create_Range_List(PRANGE_LIST prlh, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["prlh", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_Class_Key_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Delete_Class_Key_Ex(LPGUID ClassGuid, [CM_DELETE_CLASS_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_DevNode_Key_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Delete_DevNode_Key_Ex(DEVNODE dnDevNode, ULONG ulHardwareProfile, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevNode", "ulHardwareProfile", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_Range(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Delete_Range(DWORDLONG ullStartValue, DWORDLONG ullEndValue, RANGE_LIST rlh, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ullStartValue", "ullEndValue", "rlh", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Disable_DevNode_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Disable_DevNode_Ex(DEVINST dnDevInst, [CM_DISABLE_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Dup_Range_List(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Dup_Range_List(RANGE_LIST rlhOld, RANGE_LIST rlhNew, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["rlhOld", "rlhNew", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Enable_DevNode_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Enable_DevNode_Ex(DEVINST dnDevInst, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Find_Range(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Find_Range(PDWORDLONG pullStart, DWORDLONG ullStart, ULONG ulLength, DWORDLONG ullAlignment, DWORDLONG ullEnd, RANGE_LIST rlh, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pullStart", "ullStart", "ulLength", "ullAlignment", "ullEnd", "rlh", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_First_Range(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_First_Range(RANGE_LIST rlh, PDWORDLONG pullStart, PDWORDLONG pullEnd, PRANGE_ELEMENT preElement, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["rlh", "pullStart", "pullEnd", "preElement", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Free_Range_List(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Free_Range_List(RANGE_LIST rlh, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["rlh", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Key_Name(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Class_Key_Name(LPGUID ClassGuid, LPTSTR pszKeyName, PULONG pulLength, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "pszKeyName", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Key_NameA(jitter):
    cfgmgr32_CM_Get_Class_Key_Name(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Key_NameW(jitter):
    cfgmgr32_CM_Get_Class_Key_Name(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Key_Name_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Class_Key_Name_Ex(LPGUID ClassGuid, LPTSTR pszKeyName, PULONG pulLength, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "pszKeyName", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Key_Name_ExA(jitter):
    cfgmgr32_CM_Get_Class_Key_Name_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Key_Name_ExW(jitter):
    cfgmgr32_CM_Get_Class_Key_Name_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Name(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Class_Name(LPGUID ClassGuid, PTSTR Buffer, PULONG pulLength, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "Buffer", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_NameA(jitter):
    cfgmgr32_CM_Get_Class_Name(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Class_NameW(jitter):
    cfgmgr32_CM_Get_Class_Name(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Name_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Class_Name_Ex(LPGUID ClassGuid, PTSTR Buffer, PULONG pulLength, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "Buffer", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Name_ExA(jitter):
    cfgmgr32_CM_Get_Class_Name_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Name_ExW(jitter):
    cfgmgr32_CM_Get_Class_Name_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_Alias(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_Interface_Alias(LPCTSTR pszDeviceInterface, LPGUID AliasInterfaceGuid, LPTSTR pszAliasDeviceInterface, PULONG pulLength, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "AliasInterfaceGuid", "pszAliasDeviceInterface", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_AliasA(jitter):
    cfgmgr32_CM_Get_Device_Interface_Alias(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_AliasW(jitter):
    cfgmgr32_CM_Get_Device_Interface_Alias(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_Alias_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_Interface_Alias_Ex(LPCTSTR pszDeviceInterface, LPGUID AliasInterfaceGuid, LPTSTR pszAliasDeviceInterface, PULONG pulLength, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "AliasInterfaceGuid", "pszAliasDeviceInterface", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_Alias_ExA(jitter):
    cfgmgr32_CM_Get_Device_Interface_Alias_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_Alias_ExW(jitter):
    cfgmgr32_CM_Get_Device_Interface_Alias_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_List_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_Interface_List_Ex(LPGUID InterfaceClassGuid, DEVINSTID pDeviceID, PTCHAR Buffer, ULONG BufferLen, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceClassGuid", "pDeviceID", "Buffer", "BufferLen", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_List_ExA(jitter):
    cfgmgr32_CM_Get_Device_Interface_List_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_List_ExW(jitter):
    cfgmgr32_CM_Get_Device_Interface_List_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_List_Size_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_Interface_List_Size_Ex(PULONG pulLen, LPGUID InterfaceClassGuid, DEVINSTID pDeviceID, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulLen", "InterfaceClassGuid", "pDeviceID", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_List_Size_ExA(jitter):
    cfgmgr32_CM_Get_Device_Interface_List_Size_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Device_Interface_List_Size_ExW(jitter):
    cfgmgr32_CM_Get_Device_Interface_List_Size_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_DevNode_Custom_Property(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_DevNode_Custom_Property(DEVINST dnDevInst, PCTSTR pszCustomPropertyName, PULONG pulRegDataType, PVOID Buffer, PULONG pulLength, [CM_CUSTOMDEVPROP_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "pszCustomPropertyName", "pulRegDataType", "Buffer", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Custom_PropertyA(jitter):
    cfgmgr32_CM_Get_DevNode_Custom_Property(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_DevNode_Custom_PropertyW(jitter):
    cfgmgr32_CM_Get_DevNode_Custom_Property(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_DevNode_Custom_Property_ExW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_DevNode_Custom_Property_ExW(DEVINST dnDevInst, PCTSTR pszCustomPropertyName, PULONG pulRegDataType, PVOID Buffer, PULONG pulLength, [CM_CUSTOMDEVPROP_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "pszCustomPropertyName", "pulRegDataType", "Buffer", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Registry_Property_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_DevNode_Registry_Property_Ex(DEVINST dnDevInst, [CM_DRP] ulProperty, PULONG pulRegDataType, PVOID Buffer, PULONG pulLength, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulProperty", "pulRegDataType", "Buffer", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Registry_Property_ExA(jitter):
    cfgmgr32_CM_Get_DevNode_Registry_Property_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_DevNode_Registry_Property_ExW(jitter):
    cfgmgr32_CM_Get_DevNode_Registry_Property_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Global_State(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Global_State(PULONG pulState, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulState", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Global_State_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Global_State_Ex(PULONG pulState, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulState", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Hardware_Profile_Info(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Hardware_Profile_Info(ULONG ulIndex, PHWPROFILEINFO pHWProfileInfo, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIndex", "pHWProfileInfo", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Hardware_Profile_InfoA(jitter):
    cfgmgr32_CM_Get_Hardware_Profile_Info(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Hardware_Profile_InfoW(jitter):
    cfgmgr32_CM_Get_Hardware_Profile_Info(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Hardware_Profile_Info_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Hardware_Profile_Info_Ex(ULONG ulIndex, PHWPROFILEINFO pHWProfileInfo, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIndex", "pHWProfileInfo", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Hardware_Profile_Info_ExA(jitter):
    cfgmgr32_CM_Get_Hardware_Profile_Info_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Get_Hardware_Profile_Info_ExW(jitter):
    cfgmgr32_CM_Get_Hardware_Profile_Info_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Intersect_Range_List(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Intersect_Range_List(RANGE_LIST rlhOld1, RANGE_LIST rlhOld2, RANGE_LIST rlhNew, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["rlhOld1", "rlhOld2", "rlhNew", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Invert_Range_List(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Invert_Range_List(RANGE_LIST rlhOld, RANGE_LIST rlhNew, DWORDLONG ullMaxValue, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["rlhOld", "rlhNew", "ullMaxValue", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Merge_Range_List(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Merge_Range_List(RANGE_LIST rlhOld1, RANGE_LIST rlhOld2, RANGE_LIST rlhNew, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["rlhOld1", "rlhOld2", "rlhNew", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Move_DevNode(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Move_DevNode(DEVINST dnFromDevInst, DEVINST dnToDevInst, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnFromDevInst", "dnToDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Move_DevNode_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Move_DevNode_Ex(DEVINST dnFromDevInst, DEVINST dnToDevInst, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnFromDevInst", "dnToDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Next_Range(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Next_Range(PRANGE_ELEMENT preElement, PDWORDLONG pullStart, PDWORDLONG pullEnd, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["preElement", "pullStart", "pullEnd", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Class_Key_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Open_Class_Key_Ex(LPGUID ClassGuid, LPCTSTR pszClassName, REGSAM samDesired, REGDISPOSITION Disposition, PHKEY phkClass, [CM_OPEN_CLASS_KEY_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "pszClassName", "samDesired", "Disposition", "phkClass", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Class_Key_ExA(jitter):
    cfgmgr32_CM_Open_Class_Key_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Open_Class_Key_ExW(jitter):
    cfgmgr32_CM_Open_Class_Key_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Open_DevNode_Key_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Open_DevNode_Key_Ex(DEVINST dnDevNode, REGSAM samDesired, ULONG ulHardwareProfile, REGDISPOSITION Disposition, PHKEY phkDevice, [CM_REGISTRY_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevNode", "samDesired", "ulHardwareProfile", "Disposition", "phkDevice", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_Arbitrator_Free_Data(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Query_Arbitrator_Free_Data(PVOID pData, ULONG DataLen, DEVINST dnDevInst, RESOURCEID ResourceID, [CM_QUERY_ARBITRATOR_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pData", "DataLen", "dnDevInst", "ResourceID", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_Arbitrator_Free_Data_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Query_Arbitrator_Free_Data_Ex(PVOID pData, ULONG DataLen, DEVINST dnDevInst, RESOURCEID ResourceID, [CM_QUERY_ARBITRATOR_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pData", "DataLen", "dnDevInst", "ResourceID", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_Arbitrator_Free_Size(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Query_Arbitrator_Free_Size(PULONG pulSize, DEVINST dnDevInst, RESOURCEID ResourceID, [CM_QUERY_ARBITRATOR_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulSize", "dnDevInst", "ResourceID", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_Arbitrator_Free_Size_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Query_Arbitrator_Free_Size_Ex(PULONG pulSize, DEVINST dnDevInst, RESOURCEID ResourceID, [CM_QUERY_ARBITRATOR_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pulSize", "dnDevInst", "ResourceID", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_Remove_SubTree(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Query_Remove_SubTree(DEVINST dnAncestor, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnAncestor", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Query_Remove_SubTree_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Query_Remove_SubTree_Ex(DEVINST dnAncestor, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnAncestor", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Register_Device_Driver(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Register_Device_Driver(DEVINST dnDevInst, [CM_REGISTER_DEVICE_DRIVER_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Register_Device_Driver_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Register_Device_Driver_Ex(DEVINST dnDevInst, [CM_REGISTER_DEVICE_DRIVER_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Register_Device_Interface(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Register_Device_Interface(DEVINST dnDevInst, LPGUID InterfaceClassGuid, LPCTSTR pszReference, LPTSTR pszDeviceInterface, PULONG pulLength, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "InterfaceClassGuid", "pszReference", "pszDeviceInterface", "pulLength", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Register_Device_InterfaceA(jitter):
    cfgmgr32_CM_Register_Device_Interface(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Register_Device_InterfaceW(jitter):
    cfgmgr32_CM_Register_Device_Interface(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Register_Device_Interface_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Register_Device_Interface_Ex(DEVINST dnDevInst, LPGUID InterfaceClassGuid, LPCTSTR pszReference, LPTSTR pszDeviceInterface, PULONG pulLength, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "InterfaceClassGuid", "pszReference", "pszDeviceInterface", "pulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Register_Device_Interface_ExA(jitter):
    cfgmgr32_CM_Register_Device_Interface_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Register_Device_Interface_ExW(jitter):
    cfgmgr32_CM_Register_Device_Interface_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Run_Detection(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Run_Detection([CM_DETECT_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Run_Detection_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Run_Detection_Ex([CM_DETECT_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Registry_Property_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_DevNode_Registry_Property_Ex(DEVINST dnDevInst, [CM_DRP] ulProperty, PCVOID Buffer, ULONG ulLength, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulProperty", "Buffer", "ulLength", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Registry_Property_ExA(jitter):
    cfgmgr32_CM_Set_DevNode_Registry_Property_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Set_DevNode_Registry_Property_ExW(jitter):
    cfgmgr32_CM_Set_DevNode_Registry_Property_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Set_HW_Prof(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_HW_Prof(ULONG ulHardwareProfile, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ulHardwareProfile", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_HW_Prof_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_HW_Prof_Ex(ULONG ulHardwareProfile, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ulHardwareProfile", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_HW_Prof_Flags(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_HW_Prof_Flags(DEVINSTID pDeviceID, ULONG ulConfig, ULONG ulValue, [CM_SET_HW_PROF_FLAGS] ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pDeviceID", "ulConfig", "ulValue", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_HW_Prof_FlagsA(jitter):
    cfgmgr32_CM_Set_HW_Prof_Flags(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Set_HW_Prof_FlagsW(jitter):
    cfgmgr32_CM_Set_HW_Prof_Flags(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Set_HW_Prof_Flags_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_HW_Prof_Flags_Ex(DEVINSTID pDeviceID, ULONG ulConfig, ULONG ulValue, [CM_SET_HW_PROF_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pDeviceID", "ulConfig", "ulValue", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_HW_Prof_Flags_ExA(jitter):
    cfgmgr32_CM_Set_HW_Prof_Flags_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Set_HW_Prof_Flags_ExW(jitter):
    cfgmgr32_CM_Set_HW_Prof_Flags_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Setup_DevNode_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Setup_DevNode_Ex(DEVINST dnDevInst, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Test_Range_Available(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Test_Range_Available(DWORDLONG ullStartValue, DWORDLONG ullEndValue, RANGE_LIST rlh, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["ullStartValue", "ullEndValue", "rlh", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Uninstall_DevNode_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Uninstall_DevNode_Ex(DEVNODE dnDevInst, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Unregister_Device_Interface(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Unregister_Device_Interface(LPCTSTR pszDeviceInterface, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Unregister_Device_InterfaceA(jitter):
    cfgmgr32_CM_Unregister_Device_Interface(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Unregister_Device_InterfaceW(jitter):
    cfgmgr32_CM_Unregister_Device_Interface(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Unregister_Device_Interface_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Unregister_Device_Interface_Ex(LPCTSTR pszDeviceInterface, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Unregister_Device_Interface_ExA(jitter):
    cfgmgr32_CM_Unregister_Device_Interface_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Unregister_Device_Interface_ExW(jitter):
    cfgmgr32_CM_Unregister_Device_Interface_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Detect_Resource_Conflict(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Detect_Resource_Conflict(DEVINST dnDevInst, RESOURCEID ResourceID, PCVOID ResourceData, ULONG ResourceLen, PBOOL pbConflictDetected, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ResourceID", "ResourceData", "ResourceLen", "pbConflictDetected", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Detect_Resource_Conflict_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Detect_Resource_Conflict_Ex(DEVINST dnDevInst, RESOURCEID ResourceID, PCVOID ResourceData, ULONG ResourceLen, PBOOL pbConflictDetected, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "ResourceID", "ResourceData", "ResourceLen", "pbConflictDetected", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Remove_SubTree(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Remove_SubTree(DEVINST dnAncestor, ULONG ulFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnAncestor", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Remove_SubTree_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Remove_SubTree_Ex(DEVINST dnAncestor, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnAncestor", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_RestoreAll_DefaultPowerSchemes(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_RestoreAll_DefaultPowerSchemes(PDWORD Error)
    """
    ret_ad, args = jitter.func_args_stdcall(["Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Restore_DefaultPowerScheme(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Restore_DefaultPowerScheme(CONST GUID* SchemeGuid, PDWORD Error)
    """
    ret_ad, args = jitter.func_args_stdcall(["SchemeGuid", "Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_ActiveScheme(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_ActiveScheme(CONST GUID* SchemeGuid, PDWORD Error)
    """
    ret_ad, args = jitter.func_args_stdcall(["SchemeGuid", "Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Apply_PowerScheme(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Apply_PowerScheme()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_PowerScheme(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Delete_PowerScheme(CONST GUID* SchemeGuid, PDWORD Error)
    """
    ret_ad, args = jitter.func_args_stdcall(["SchemeGuid", "Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Duplicate_PowerScheme(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Duplicate_PowerScheme(CONST GUID* SourceSchemeGuid, GUID** DestinationSchemeGuid, PDWORD Error)
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceSchemeGuid", "DestinationSchemeGuid", "Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Import_PowerScheme(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Import_PowerScheme(LPCWSTR ImportFileNamePath, GUID** DestinationSchemeGuid, PDWORD Error)
    """
    ret_ad, args = jitter.func_args_stdcall(["ImportFileNamePath", "DestinationSchemeGuid", "Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Write_UserPowerKey(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Write_UserPowerKey(CONST GUID* SchemeGuid, CONST GUID* SubGroupOfPowerSettingsGuid, CONST GUID* PowerSettingGuid, ULONG AccessFlags, ULONG Type, UCHAR* Buffer, DWORD BufferSize, PDWORD Error)
    """
    ret_ad, args = jitter.func_args_stdcall(["SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "AccessFlags", "Type", "Buffer", "BufferSize", "Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_Class_Property_ExW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_Class_Property_ExW(LPCGUID ClassGUID, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE PropertyType, CONST PBYTE PropertyBuffer, ULONG PropertyBufferSize, [CM_CLASS_PROPERTY_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGUID", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_DevNode_Property_ExW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_DevNode_Property_ExW(DEVINST dnDevInst, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE PropertyType, CONST PBYTE PropertyBuffer, ULONG PropertyBufferSize, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Set_Device_Interface_Property_ExW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Set_Device_Interface_Property_ExW(LPCWSTR pszDeviceInterface, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE PropertyType, CONST PBYTE PropertyBuffer, ULONG PropertyBufferSize, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_Device_Interface_Key_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Delete_Device_Interface_Key_Ex(LPCTSTR pszDeviceInterface, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Delete_Device_Interface_Key_ExA(jitter):
    cfgmgr32_CM_Delete_Device_Interface_Key_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Delete_Device_Interface_Key_ExW(jitter):
    cfgmgr32_CM_Delete_Device_Interface_Key_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cfgmgr32_CM_Get_Class_Property_ExW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Class_Property_ExW(LPCGUID ClassGUID, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE* PropertyType, PBYTE PropertyBuffer, PULONG PropertyBufferSize, [CM_CLASS_PROPERTY_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGUID", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Class_Property_Keys_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Class_Property_Keys_Ex(LPCGUID ClassGUID, DEVPROPKEY* PropertyKeyArray, PULONG PropertyKeyCount, [CM_CLASS_PROPERTY_FLAGS] ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGUID", "PropertyKeyArray", "PropertyKeyCount", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Property_ExW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_DevNode_Property_ExW(DEVINST dnDevInst, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE* PropertyType, PBYTE PropertyBuffer, PULONG PropertyBufferSize, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_DevNode_Property_Keys_Ex(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_DevNode_Property_Keys_Ex(DEVINST dnDevInst, DEVPROPKEY* PropertyKeyArray, PULONG PropertyKeyCount, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["dnDevInst", "PropertyKeyArray", "PropertyKeyCount", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_Property_ExW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_Interface_Property_ExW(LPCWSTR pszDeviceInterface, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE* PropertyType, PBYTE PropertyBuffer, PULONG PropertyBufferSize, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Get_Device_Interface_Property_Keys_ExW(jitter):
    """
    [CfgMgr32.dll] CONFIGRET CM_Get_Device_Interface_Property_Keys_ExW(LPCWSTR pszDeviceInterface, DEVPROPKEY* PropertyKeyArray, PULONG PropertyKeyCount, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "PropertyKeyArray", "PropertyKeyCount", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Device_Interface_Key_Ex(jitter, get_str, set_str):
    """
    [CfgMgr32.dll] CONFIGRET CM_Open_Device_Interface_Key_Ex(LPCTSTR pszDeviceInterface, REGSAM samDesired, REGDISPOSITION Disposition, PHKEY phkDeviceInterface, ULONG ulFlags, HMACHINE hMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDeviceInterface", "samDesired", "Disposition", "phkDeviceInterface", "ulFlags", "hMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cfgmgr32_CM_Open_Device_Interface_Key_ExA(jitter):
    cfgmgr32_CM_Open_Device_Interface_Key_Ex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cfgmgr32_CM_Open_Device_Interface_Key_ExW(jitter):
    cfgmgr32_CM_Open_Device_Interface_Key_Ex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
