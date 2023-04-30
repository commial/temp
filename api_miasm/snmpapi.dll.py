
def snmpapi_SnmpSvcGetUptime(jitter):
    """"
    [Snmpapi.dll] DWORD SnmpSvcGetUptime()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpSvcSetLogLevel(jitter):
    """"
    [Snmpapi.dll] void SnmpSvcSetLogLevel(INT nLogLevel)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nLogLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpSvcSetLogType(jitter):
    """"
    [Snmpapi.dll] void SnmpSvcSetLogType(INT nLogType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nLogType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilAsnAnyCpy(jitter):
    """"
    [Snmpapi.dll] SNMPAPI SnmpUtilAsnAnyCpy(AsnAny* pAnyDst, AsnAny* pAnySrc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAnyDst", "pAnySrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilAsnAnyFree(jitter):
    """"
    [Snmpapi.dll] void SnmpUtilAsnAnyFree(AsnAny* pAny)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAny"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilDbgPrint(jitter):
    """"
    [Snmpapi.dll] void SnmpUtilDbgPrint(INT nLogLevel, LPSTR szFormat)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nLogLevel", "szFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilIdsToA(jitter):
    """"
    [Snmpapi.dll] LPSTR SnmpUtilIdsToA(UINT* Ids, UINT IdLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Ids", "IdLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilMemAlloc(jitter):
    """"
    [Snmpapi.dll] LPVOID SnmpUtilMemAlloc(UINT nBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["nBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilMemFree(jitter):
    """"
    [Snmpapi.dll] void SnmpUtilMemFree(LPVOID pMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilMemReAlloc(jitter):
    """"
    [Snmpapi.dll] LPVOID SnmpUtilMemReAlloc(LPVOID pMem, UINT nBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pMem", "nBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOctetsCmp(jitter):
    """"
    [Snmpapi.dll] SNMPAPI SnmpUtilOctetsCmp(AsnOctetString* pOctets1, AsnOctetString* pOctets2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pOctets1", "pOctets2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOctetsCpy(jitter):
    """"
    [Snmpapi.dll] SNMPAPI SnmpUtilOctetsCpy(AsnOctetString* pOctetsDst, AsnOctetString* pOctetsSrc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pOctetsDst", "pOctetsSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOctetsFree(jitter):
    """"
    [Snmpapi.dll] void SnmpUtilOctetsFree(AsnOctetString* pOctets)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pOctets"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOctetsNCmp(jitter):
    """"
    [Snmpapi.dll] SNMPAPI SnmpUtilOctetsNCmp(AsnOctetString* pOctets1, AsnOctetString* pOctets2, UINT nChars)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pOctets1", "pOctets2", "nChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOidAppend(jitter):
    """"
    [Snmpapi.dll] SNMPAPI SnmpUtilOidAppend(AsnObjectIdentifier* pOidDst, AsnObjectIdentifier* pOidSrc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pOidDst", "pOidSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOidCmp(jitter):
    """"
    [Snmpapi.dll] SNMPAPI SnmpUtilOidCmp(AsnObjectIdentifier* pOid1, AsnObjectIdentifier* pOid2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pOid1", "pOid2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOidCpy(jitter):
    """"
    [Snmpapi.dll] SNMPAPI SnmpUtilOidCpy(AsnObjectIdentifier* pOidDst, AsnObjectIdentifier* pOidSrc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pOidDst", "pOidSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOidFree(jitter):
    """"
    [Snmpapi.dll] void SnmpUtilOidFree(AsnObjectIdentifier* pOid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pOid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOidNCmp(jitter):
    """"
    [Snmpapi.dll] SNMPAPI SnmpUtilOidNCmp(AsnObjectIdentifier* pOid1, AsnObjectIdentifier* pOid2, UINT nSubIds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pOid1", "pOid2", "nSubIds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOidToA(jitter):
    """"
    [Snmpapi.dll] LPSTR SnmpUtilOidToA(AsnObjectIdentifier* Oid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Oid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilPrintAsnAny(jitter):
    """"
    [Snmpapi.dll] void SnmpUtilPrintAsnAny(AsnAny* pAny)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAny"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilPrintOid(jitter):
    """"
    [Snmpapi.dll] void SnmpUtilPrintOid(AsnObjectIdentifier* Oid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Oid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilVarBindCpy(jitter):
    """"
    [Snmpapi.dll] SNMPAPI SnmpUtilVarBindCpy(SnmpVarBind* pVbDst, SnmpVarBind* pVbSrc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pVbDst", "pVbSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilVarBindListCpy(jitter):
    """"
    [Snmpapi.dll] SNMPAPI SnmpUtilVarBindListCpy(SnmpVarBindList* pVblDst, SnmpVarBindList* pVblSrc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pVblDst", "pVblSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilVarBindFree(jitter):
    """"
    [Snmpapi.dll] void SnmpUtilVarBindFree(SnmpVarBind* pVb)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pVb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilVarBindListFree(jitter):
    """"
    [Snmpapi.dll] void SnmpUtilVarBindListFree(SnmpVarBindList* pVbl)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pVbl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
