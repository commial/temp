
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
