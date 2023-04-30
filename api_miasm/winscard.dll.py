
def winscard_SCardAccessStartedEvent(jitter):
    """"
    [WinSCard.dll] HANDLE SCardAccessStartedEvent()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardAddReaderToGroup(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardAddReaderToGroup(SCARDCONTEXT hContext, LPCTSTR szReaderName, LPCTSTR szGroupName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szReaderName", "szGroupName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardAudit(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardAudit(SCARDCONTEXT hContext, [SCARD_AUDIT_CHV] dwEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "dwEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardBeginTransaction(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardBeginTransaction(SCARDHANDLE hCard)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCard"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardCancel(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardCancel(SCARDCONTEXT hContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardConnect(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardConnect(SCARDCONTEXT hContext, LPCTSTR szReader, DWORD dwShareMode, DWORD dwPreferredProtocols, LPSCARDHANDLE phCard, LPDWORD pdwActiveProtocol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szReader", "dwShareMode", "dwPreferredProtocols", "phCard", "pdwActiveProtocol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardControl(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardControl(SCARDHANDLE hCard, DWORD dwControlCode, LPCVOID lpInBuffer, DWORD nInBufferSize, LPVOID lpOutBuffer, DWORD nOutBufferSize, LPDWORD lpBytesReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCard", "dwControlCode", "lpInBuffer", "nInBufferSize", "lpOutBuffer", "nOutBufferSize", "lpBytesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardDisconnect(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardDisconnect(SCARDHANDLE hCard, DWORD dwDisposition)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCard", "dwDisposition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardEndTransaction(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardEndTransaction(SCARDHANDLE hCard, DWORD dwDisposition)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCard", "dwDisposition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardEstablishContext(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardEstablishContext([SCardScope] dwScope, LPCVOID pvReserved1, LPCVOID pvReserved2, LPSCARDCONTEXT phContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwScope", "pvReserved1", "pvReserved2", "phContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardForgetCardType(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardForgetCardType(SCARDCONTEXT hContext, LPCTSTR szCardName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szCardName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardForgetReader(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardForgetReader(SCARDCONTEXT hContext, LPCTSTR szReaderName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szReaderName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardForgetReaderGroup(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardForgetReaderGroup(SCARDCONTEXT hContext, LPCTSTR szGroupName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szGroupName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardFreeMemory(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardFreeMemory(SCARDCONTEXT hContext, LPCVOID pvMem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "pvMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardGetAttrib(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardGetAttrib(SCARDHANDLE hCard, DWORD dwAttrId, LPBYTE pbAttr, LPDWORD pcbAttrLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCard", "dwAttrId", "pbAttr", "pcbAttrLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardGetCardTypeProviderName(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardGetCardTypeProviderName(SCARDCONTEXT hContext, LPCTSTR szCardName, DWORD dwProviderId, LPTSTR szProvider, LPDWORD* pcchProvider)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szCardName", "dwProviderId", "szProvider", "pcchProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardGetDeviceTypeId(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardGetDeviceTypeId(SCARDCONTEXT hContext, LPCTSTR szReaderName, LPDWORD pdwDeviceTypeId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szReaderName", "pdwDeviceTypeId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardGetProviderId(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardGetProviderId(SCARDCONTEXT hContext, LPCTSTR szCard, LPGUID pguidProviderId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szCard", "pguidProviderId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardGetReaderDeviceInstanceId(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardGetReaderDeviceInstanceId(SCARDCONTEXT hContext, LPCTSTR szReaderName, LPTSTR szDeviceInstanceId, LPDWORD cchDeviceInstanceId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szReaderName", "szDeviceInstanceId", "cchDeviceInstanceId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardGetReaderIcon(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardGetReaderIcon(SCARDCONTEXT hContext, LPCTSTR szReaderName, LPBYTE pbIcon, LPDWORD pcbIcon)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szReaderName", "pbIcon", "pcbIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardGetStatusChange(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardGetStatusChange(SCARDCONTEXT hContext, DWORD dwTimeout, LPSCARD_READERSTATE rgReaderStates, DWORD cReaders)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "dwTimeout", "rgReaderStates", "cReaders"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardGetTransmitCount(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardGetTransmitCount(SCARDHANDLE hCard, LPDWORD pcTransmitCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCard", "pcTransmitCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardIntroduceCardType(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardIntroduceCardType(SCARDCONTEXT hContext, LPCTSTR szCardName, LPCGUID pguidPrimaryProvider, LPCGUID rgguidInterfaces, DWORD dwInterfaceCount, LPCBYTE pbAtr, LPCBYTE pbAtrMask, DWORD cbAtrLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szCardName", "pguidPrimaryProvider", "rgguidInterfaces", "dwInterfaceCount", "pbAtr", "pbAtrMask", "cbAtrLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardIntroduceReader(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardIntroduceReader(SCARDCONTEXT hContext, LPCTSTR szReaderName, LPCTSTR szDeviceName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szReaderName", "szDeviceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardIntroduceReaderGroup(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardIntroduceReaderGroup(SCARDCONTEXT hContext, LPCTSTR szGroupName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szGroupName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardIsValidContext(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardIsValidContext(SCARDCONTEXT hContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardListCards(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardListCards(SCARDCONTEXT hContext, LPCBYTE pbAtr, LPCGUID rgguidInterfaces, DWORD cguidInterfaceCount, LPTSTR mszCards, LPDWORD pcchCards)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "pbAtr", "rgguidInterfaces", "cguidInterfaceCount", "mszCards", "pcchCards"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardListInterfaces(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardListInterfaces(SCARDCONTEXT hContext, LPCTSTR szCard, LPGUID pguidInterfaces, LPDWORD pcguidInterfaces)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szCard", "pguidInterfaces", "pcguidInterfaces"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardListReaderGroups(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardListReaderGroups(SCARDCONTEXT hContext, LPTSTR mszGroups, LPDWORD pcchGroups)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "mszGroups", "pcchGroups"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardListReaders(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardListReaders(SCARDCONTEXT hContext, LPCTSTR mszGroups, LPTSTR mszReaders, LPDWORD pcchReaders)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "mszGroups", "mszReaders", "pcchReaders"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardListReadersWithDeviceInstanceId(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardListReadersWithDeviceInstanceId(SCARDCONTEXT hContext, LPCTSTR szDeviceInstanceId, LPTSTR mszReaders, LPDWORD pcchReaders)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szDeviceInstanceId", "mszReaders", "pcchReaders"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardLocateCards(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardLocateCards(SCARDCONTEXT hContext, LPCTSTR mszCards, LPSCARD_READERSTATE rgReaderStates, DWORD cReaders)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "mszCards", "rgReaderStates", "cReaders"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardLocateCardsByATR(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardLocateCardsByATR(SCARDCONTEXT hContext, LPSCARD_ATRMASK rgAtrMasks, DWORD cAtrs, LPSCARD_READERSTATE rgReaderStates, DWORD cReaders)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "rgAtrMasks", "cAtrs", "rgReaderStates", "cReaders"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardReadCache(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardReadCache(SCARDCONTEXT hContext, UUID* CardIdentifier, DWORD FreshnessCounter, LPTSTR LookupName, PBYTE Data, DWORD* DataLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "CardIdentifier", "FreshnessCounter", "LookupName", "Data", "DataLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardReconnect(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardReconnect(SCARDHANDLE hCard, DWORD dwShareMode, DWORD dwPreferredProtocols, DWORD dwInitialization, LPDWORD pdwActiveProtocol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCard", "dwShareMode", "dwPreferredProtocols", "dwInitialization", "pdwActiveProtocol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardReleaseContext(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardReleaseContext(SCARDCONTEXT hContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardReleaseStartedEvent(jitter):
    """"
    [WinSCard.dll] void SCardReleaseStartedEvent()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardRemoveReaderFromGroup(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardRemoveReaderFromGroup(SCARDCONTEXT hContext, LPCTSTR szReaderName, LPCTSTR szGroupName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szReaderName", "szGroupName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardSetAttrib(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardSetAttrib(SCARDHANDLE hCard, DWORD dwAttrId, LPCBYTE pbAttr, DWORD cbAttrLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCard", "dwAttrId", "pbAttr", "cbAttrLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardSetCardTypeProviderName(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardSetCardTypeProviderName(SCARDCONTEXT hContext, LPCTSTR szCardName, DWORD dwProviderId, LPCTSTR szProvider)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "szCardName", "dwProviderId", "szProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardState(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardState(SCARDHANDLE hCard, LPDWORD pdwState, LPDWORD pdwProtocol, LPBYTE pbAtr, LPDWORD pcbAtrLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCard", "pdwState", "pdwProtocol", "pbAtr", "pcbAtrLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardStatus(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardStatus(SCARDHANDLE hCard, LPTSTR szReaderName, LPDWORD pcchReaderLen, LPDWORD pdwState, LPDWORD pdwProtocol, LPBYTE pbAtr, LPDWORD pcbAtrLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCard", "szReaderName", "pcchReaderLen", "pdwState", "pdwProtocol", "pbAtr", "pcbAtrLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardTransmit(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardTransmit(SCARDHANDLE hCard, LPCSCARD_IO_REQUEST pioSendPci, LPCBYTE pbSendBuffer, DWORD cbSendLength, LPSCARD_IO_REQUEST pioRecvPci, LPBYTE pbRecvBuffer, LPDWORD pcbRecvLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCard", "pioSendPci", "pbSendBuffer", "cbSendLength", "pioRecvPci", "pbRecvBuffer", "pcbRecvLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winscard_SCardWriteCache(jitter):
    """"
    [WinSCard.dll] [SCARD_ERROR] SCardWriteCache(SCARDCONTEXT hContext, UUID* CardIdentifier, DWORD FreshnessCounter, LPTSTR LookupName, PBYTE Data, DWORD DataLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hContext", "CardIdentifier", "FreshnessCounter", "LookupName", "Data", "DataLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
