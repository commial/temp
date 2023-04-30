
def slcext_SLAcquireGenuineTicket(jitter):
    """
    HRESULT SLAcquireGenuineTicket(
        void** ppTicketBlob,
        UINT* pcbTicketBlob,
        PCWSTR pwszTemplateId,
        PCWSTR pwszServerUrl,
        PCWSTR pwszClientToken
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppTicketBlob", "pcbTicketBlob", "pwszTemplateId", "pwszServerUrl", "pwszClientToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
