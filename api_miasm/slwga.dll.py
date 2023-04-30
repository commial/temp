
def slwga_SLIsGenuineLocal(jitter):
    """
    HRESULT SLIsGenuineLocal(
        const SLID* pAppId,
        SL_GENUINE_STATE* pGenuineState,
        SL_NONGENUINE_UI_OPTIONS* pUIOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppId", "pGenuineState", "pUIOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def slwga_SLIsGenuineLocalEx(jitter):
    """
    HRESULT SLIsGenuineLocalEx(
        const SLID* pAppId,
        const SLID* pSkuId,
        SL_GENUINE_STATE* pGenuineState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppId", "pSkuId", "pGenuineState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
