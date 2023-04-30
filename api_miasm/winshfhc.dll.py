FILE_RISK_LEVEL = {
    "FRL_NO_OPINION": 0,
    "FRL_LOW": 1,
    "FRL_MODERATE": 2,
    "FRL_HIGH": 3,
    "FRL_BLOCK": 4,
}

def winshfhc_EstimateFileRiskLevel(jitter):
    """
    HRESULT EstimateFileRiskLevel(
        LPCWSTR pszFilePath,
        LPCWSTR pszExt,
        LPCWSTR pszHandler,
        FILE_RISK_LEVEL* pfrlEstimate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszFilePath", "pszExt", "pszHandler", "pfrlEstimate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
