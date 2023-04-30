
def dnsapi_DnsAcquireContextHandle_(jitter):
    """"
    [Dnsapi.dll] DNS_STATUS DnsAcquireContextHandle_(BOOL CredentialFlags, PVOID Credentials, PHANDLE pContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CredentialFlags", "Credentials", "pContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsExtractRecordsFromMessage_W(jitter):
    """"
    [Dnsapi.dll] DNS_STATUS DnsExtractRecordsFromMessage_W(PDNS_MESSAGE_BUFFER pDnsBuffer, WORD wMessageLength, PDNS_RECORD* ppRecord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pDnsBuffer", "wMessageLength", "ppRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsFree(jitter):
    """"
    [Dnsapi.dll] void DnsFree(PVOID pData, DNS_FREE_TYPE FreeType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pData", "FreeType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsFreeProxyName(jitter):
    """"
    [Dnsapi.dll] void DnsFreeProxyName(PWSTR proxyName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["proxyName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsGetProxyInformation(jitter):
    """"
    [Dnsapi.dll] DNS_STATUS DnsGetProxyInformation(PCWSTR hostName, DNS_PROXY_INFORMATION* proxyInformation, DNS_PROXY_INFORMATION* defaultProxyInformation, DNS_PROXY_COMPLETION_ROUTINE completionRoutine, void* completionContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hostName", "proxyInformation", "defaultProxyInformation", "completionRoutine", "completionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsModifyRecordsInSet_(jitter):
    """"
    [Dnsapi.dll] DNS_STATUS DnsModifyRecordsInSet_(PDNS_RECORD pAddRecords, PDNS_RECORD pDeleteRecords, DWORD Options, HANDLE hContext, PVOID pExtraList, PVOID pReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pAddRecords", "pDeleteRecords", "Options", "hContext", "pExtraList", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsNameCompare_(jitter):
    """"
    [Dnsapi.dll] BOOL DnsNameCompare_(PCTSTR pName1, PCTSTR pName2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName1", "pName2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsQuery_(jitter):
    """"
    [Dnsapi.dll] DNS_STATUS DnsQuery_(PCTSTR lpstrName, [DnsRecordType] wType, [DnsQueryOptions] Options, PVOID pExtra, PDNS_RECORD* ppQueryResultsSet, PVOID* pReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpstrName", "wType", "Options", "pExtra", "ppQueryResultsSet", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsQueryConfig(jitter):
    """"
    [Dnsapi.dll] DNS_STATUS DnsQueryConfig(DNS_CONFIG_TYPE Config, [DnsConfigFlags] Flag, PCWSTR pwsAdapterName, PVOID pReserved, PVOID pBuffer, PDWORD pBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Config", "Flag", "pwsAdapterName", "pReserved", "pBuffer", "pBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsRecordCompare(jitter):
    """"
    [Dnsapi.dll] BOOL DnsRecordCompare(PDNS_RECORD pRecord1, PDNS_RECORD pRecord2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRecord1", "pRecord2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsRecordCopyEx(jitter):
    """"
    [Dnsapi.dll] PDNS_RECORD DnsRecordCopyEx(PDNS_RECORD pRecord, DNS_CHARSET CharSetIn, DNS_CHARSET CharSetOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRecord", "CharSetIn", "CharSetOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsRecordListFree(jitter):
    """"
    [Dnsapi.dll] void DnsRecordListFree(PDNS_RECORD pRecordList, DNS_FREE_TYPE FreeType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRecordList", "FreeType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsRecordSetCompare(jitter):
    """"
    [Dnsapi.dll] BOOL DnsRecordSetCompare(PDNS_RECORD pRR1, PDNS_RECORD pRR2, PDNS_RECORD* ppDiff1, PDNS_RECORD* ppDiff2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRR1", "pRR2", "ppDiff1", "ppDiff2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsRecordSetCopyEx(jitter):
    """"
    [Dnsapi.dll] PDNS_RECORD DnsRecordSetCopyEx(PDNS_RECORD pRecordSet, DNS_CHARSET CharSetIn, DNS_CHARSET CharSetOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRecordSet", "CharSetIn", "CharSetOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsRecordSetDetach(jitter):
    """"
    [Dnsapi.dll] PDNS_RECORD DnsRecordSetDetach(PDNS_RECORD pRR)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRR"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsReleaseContextHandle(jitter):
    """"
    [Dnsapi.dll] void DnsReleaseContextHandle(HANDLE ContextHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsReplaceRecordSet(jitter):
    """"
    [Dnsapi.dll] DNS_STATUS DnsReplaceRecordSet(PDNS_RECORD pNewSet, [DnsUpdateFlags] Options, HANDLE hContext, PVOID pExtraInfo, PVOID pReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pNewSet", "Options", "hContext", "pExtraInfo", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsValidateName_(jitter):
    """"
    [Dnsapi.dll] DNS_STATUS DnsValidateName_(PCTSTR pszName, DNS_NAME_FORMAT Format)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszName", "Format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsWriteQuestionToBuffer_W(jitter):
    """"
    [Dnsapi.dll] BOOL DnsWriteQuestionToBuffer_W(PDNS_MESSAGE_BUFFER pDnsBuffer, PDWORD pdwBufferSize, PCWSTR pszName, [DnsRecordType] wType, WORD Xid, BOOL fRecursionDesired)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pDnsBuffer", "pdwBufferSize", "pszName", "wType", "Xid", "fRecursionDesired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsCancelQuery(jitter):
    """"
    [Dnsapi.dll] DNS_STATUS DnsCancelQuery(PDNS_QUERY_CANCEL pCancelHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCancelHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsQueryEx(jitter):
    """"
    [Dnsapi.dll] DNS_STATUS DnsQueryEx(PDNS_QUERY_REQUEST pQueryRequest, PDNS_QUERY_RESULT pQueryResults, PDNS_QUERY_CANCEL pCancelHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pQueryRequest", "pQueryResults", "pCancelHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
