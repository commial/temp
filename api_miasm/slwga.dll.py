###### Enums ######
SL_GENUINE_STATE = {
    "SL_GEN_STATE_IS_GENUINE": 0,
    "SL_GEN_STATE_INVALID_LICENSE": 1,
    "SL_GEN_STATE_TAMPERED": 2,
    "SL_GEN_STATE_LAST": 3,
}
SL_GENUINE_STATE_INV = {
    0: "SL_GEN_STATE_IS_GENUINE",
    1: "SL_GEN_STATE_INVALID_LICENSE",
    2: "SL_GEN_STATE_TAMPERED",
    3: "SL_GEN_STATE_LAST",
}

###################

###### Types ######
SL_GENUINE_STATE = UINT
SL_GENUINE_STATE_PTR = Ptr("<I", SL_GENUINE_STATE())

class SL_NONGENUINE_UI_OPTIONS(MemStruct):
    fields = [
        ("cbSize", DWORD()),
        ("pComponentId", CONST_SLID_PTR()),
        ("hResultUI", HRESULT()),
    ]

SL_NONGENUINE_UI_OPTIONS_PTR = Ptr("<I", SL_NONGENUINE_UI_OPTIONS())

###################

###### Functions ######

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
