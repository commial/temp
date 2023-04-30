
def icmui_SetupColorMatching(jitter, get_str, set_str):
    """
    BOOL SetupColorMatching(
        PCOLORMATCHSETUP pcms
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcms"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icmui_SetupColorMatchingA(jitter):
    icmui_SetupColorMatching(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def icmui_SetupColorMatchingW(jitter):
    icmui_SetupColorMatching(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
