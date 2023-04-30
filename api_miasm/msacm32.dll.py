
def msacm32_acmDriverAdd(jitter, get_str, set_str):
    """"
    [msacm32.dll] MMRESULT acmDriverAdd(LPHACMDRIVERID phadid, HINSTANCE hinstModule, LPARAM lParam, DWORD dwPriority, DWORD fdwAdd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phadid", "hinstModule", "lParam", "dwPriority", "fdwAdd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmDriverAddA(jitter):
    msacm32_acmDriverAdd(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msacm32_acmDriverAddW(jitter):
    msacm32_acmDriverAdd(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msacm32_acmDriverClose(jitter):
    """"
    [msacm32.dll] MMRESULT acmDriverClose(HACMDRIVER had, DWORD fdwClose)
    """"
    ret_ad, args = jitter.func_args_stdcall(["had", "fdwClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmDriverDetails(jitter, get_str, set_str):
    """"
    [msacm32.dll] MMRESULT acmDriverDetails(HACMDRIVERID hadid, LPACMDRIVERDETAILS padd, DWORD fdwDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hadid", "padd", "fdwDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmDriverDetailsA(jitter):
    msacm32_acmDriverDetails(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msacm32_acmDriverDetailsW(jitter):
    msacm32_acmDriverDetails(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msacm32_acmDriverEnum(jitter):
    """"
    [msacm32.dll] MMRESULT acmDriverEnum(ACMDRIVERENUMCB fnCallback, DWORD_PTR dwInstance, DWORD fdwEnum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fnCallback", "dwInstance", "fdwEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmDriverID(jitter):
    """"
    [msacm32.dll] MMRESULT acmDriverID(HACMOBJ hao, LPHACMDRIVERID phadid, DWORD fdwDriverID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hao", "phadid", "fdwDriverID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmDriverMessage(jitter):
    """"
    [msacm32.dll] LRESULT acmDriverMessage(HACMDRIVER had, UINT uMsg, LPARAM lParam1, LPARAM lParam2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["had", "uMsg", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmDriverOpen(jitter):
    """"
    [msacm32.dll] MMRESULT acmDriverOpen(LPHACMDRIVER phad, HACMDRIVERID hadid, DWORD fdwOpen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phad", "hadid", "fdwOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmDriverPriority(jitter):
    """"
    [msacm32.dll] MMRESULT acmDriverPriority(HACMDRIVERID hadid, DWORD dwPriority, DWORD fdwPriority)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hadid", "dwPriority", "fdwPriority"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmDriverRemove(jitter):
    """"
    [msacm32.dll] MMRESULT acmDriverRemove(HACMDRIVERID hadid, DWORD fdwRemove)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hadid", "fdwRemove"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmFilterChoose(jitter, get_str, set_str):
    """"
    [msacm32.dll] MMRESULT acmFilterChoose(LPACMFILTERCHOOSE pafltrc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pafltrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmFilterChooseA(jitter):
    msacm32_acmFilterChoose(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msacm32_acmFilterChooseW(jitter):
    msacm32_acmFilterChoose(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msacm32_acmFilterDetails(jitter, get_str, set_str):
    """"
    [msacm32.dll] MMRESULT acmFilterDetails(HACMDRIVER had, LPACMFILTERDETAILS pafd, DWORD fdwDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["had", "pafd", "fdwDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmFilterDetailsA(jitter):
    msacm32_acmFilterDetails(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msacm32_acmFilterDetailsW(jitter):
    msacm32_acmFilterDetails(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msacm32_acmFilterEnum(jitter, get_str, set_str):
    """"
    [msacm32.dll] MMRESULT acmFilterEnum(HACMDRIVER had, LPACMFILTERDETAILS pafd, ACMFILTERENUMCB fnCallback, DWORD_PTR dwInstance, [ACM_FILTERENUMF] fdwEnum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["had", "pafd", "fnCallback", "dwInstance", "fdwEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmFilterEnumA(jitter):
    msacm32_acmFilterEnum(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msacm32_acmFilterEnumW(jitter):
    msacm32_acmFilterEnum(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msacm32_acmFilterTagDetails(jitter, get_str, set_str):
    """"
    [msacm32.dll] MMRESULT acmFilterTagDetails(HACMDRIVER had, LPACMFILTERTAGDETAILS paftd, DWORD_PTR fdwDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["had", "paftd", "fdwDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmFilterTagDetailsA(jitter):
    msacm32_acmFilterTagDetails(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msacm32_acmFilterTagDetailsW(jitter):
    msacm32_acmFilterTagDetails(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msacm32_acmFilterTagEnum(jitter, get_str, set_str):
    """"
    [msacm32.dll] MMRESULT acmFilterTagEnum(HACMDRIVER had, LPACMFILTERTAGDETAILS paftd, ACMFILTERTAGENUMCB fnCallback, DWORD_PTR dwInstance, DWORD fdwEnum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["had", "paftd", "fnCallback", "dwInstance", "fdwEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmFilterTagEnumA(jitter):
    msacm32_acmFilterTagEnum(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msacm32_acmFilterTagEnumW(jitter):
    msacm32_acmFilterTagEnum(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msacm32_acmFormatChoose(jitter, get_str, set_str):
    """"
    [msacm32.dll] MMRESULT acmFormatChoose(LPACMFORMATCHOOSE pfmtc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pfmtc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmFormatChooseA(jitter):
    msacm32_acmFormatChoose(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msacm32_acmFormatChooseW(jitter):
    msacm32_acmFormatChoose(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msacm32_acmFormatDetails(jitter, get_str, set_str):
    """"
    [msacm32.dll] MMRESULT acmFormatDetails(HACMDRIVER had, LPACMFORMATDETAILS pafd, DWORD fdwDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["had", "pafd", "fdwDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmFormatDetailsA(jitter):
    msacm32_acmFormatDetails(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msacm32_acmFormatDetailsW(jitter):
    msacm32_acmFormatDetails(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msacm32_acmFormatEnum(jitter, get_str, set_str):
    """"
    [msacm32.dll] MMRESULT acmFormatEnum(HACMDRIVER had, LPACMFORMATDETAILS pafd, ACMFORMATENUMCB fnCallback, DWORD_PTR dwInstance, DWORD fdwEnum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["had", "pafd", "fnCallback", "dwInstance", "fdwEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmFormatEnumA(jitter):
    msacm32_acmFormatEnum(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msacm32_acmFormatEnumW(jitter):
    msacm32_acmFormatEnum(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msacm32_acmFormatSuggest(jitter):
    """"
    [msacm32.dll] MMRESULT acmFormatSuggest(HACMDRIVER had, LPWAVEFORMATEX pwfxSrc, LPWAVEFORMATEX pwfxDst, DWORD cbwfxDst, DWORD fdwSuggest)
    """"
    ret_ad, args = jitter.func_args_stdcall(["had", "pwfxSrc", "pwfxDst", "cbwfxDst", "fdwSuggest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmFormatTagDetails(jitter, get_str, set_str):
    """"
    [msacm32.dll] MMRESULT acmFormatTagDetails(HACMDRIVER had, LPACMFORMATTAGDETAILS paftd, DWORD fdwDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["had", "paftd", "fdwDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmFormatTagDetailsA(jitter):
    msacm32_acmFormatTagDetails(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msacm32_acmFormatTagDetailsW(jitter):
    msacm32_acmFormatTagDetails(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msacm32_acmFormatTagEnum(jitter, get_str, set_str):
    """"
    [msacm32.dll] MMRESULT acmFormatTagEnum(HACMDRIVER had, LPACMFORMATTAGDETAILS paftd, ACMFORMATTAGENUMCB fnCallback, DWORD_PTR dwInstance, DWORD fdwEnum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["had", "paftd", "fnCallback", "dwInstance", "fdwEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmFormatTagEnumA(jitter):
    msacm32_acmFormatTagEnum(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def msacm32_acmFormatTagEnumW(jitter):
    msacm32_acmFormatTagEnum(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def msacm32_acmGetVersion(jitter):
    """"
    [msacm32.dll] DWORD acmGetVersion()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmMetrics(jitter):
    """"
    [msacm32.dll] MMRESULT acmMetrics(HACMOBJ hao, UINT uMetric, LPVOID pMetric)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hao", "uMetric", "pMetric"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmStreamClose(jitter):
    """"
    [msacm32.dll] MMRESULT acmStreamClose(HACMSTREAM has, DWORD fdwClose)
    """"
    ret_ad, args = jitter.func_args_stdcall(["has", "fdwClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmStreamConvert(jitter):
    """"
    [msacm32.dll] MMRESULT acmStreamConvert(HACMSTREAM has, LPACMSTREAMHEADER pash, DWORD fdwConvert)
    """"
    ret_ad, args = jitter.func_args_stdcall(["has", "pash", "fdwConvert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmStreamMessage(jitter):
    """"
    [msacm32.dll] MMRESULT acmStreamMessage(HACMSTREAM has, UINT uMsg, LPARAM lParam1, LPARAM lParam2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["has", "uMsg", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmStreamOpen(jitter):
    """"
    [msacm32.dll] MMRESULT acmStreamOpen(LPHACMSTREAM phas, HACMDRIVER had, LPWAVEFORMATEX pwfxSrc, LPWAVEFORMATEX pwfxDst, LPWAVEFILTER pwfltr, DWORD_PTR dwCallback, DWORD_PTR dwInstance, DWORD fdwOpen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phas", "had", "pwfxSrc", "pwfxDst", "pwfltr", "dwCallback", "dwInstance", "fdwOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmStreamPrepareHeader(jitter):
    """"
    [msacm32.dll] MMRESULT acmStreamPrepareHeader(HACMSTREAM has, LPACMSTREAMHEADER pash, DWORD fdwPrepare)
    """"
    ret_ad, args = jitter.func_args_stdcall(["has", "pash", "fdwPrepare"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmStreamReset(jitter):
    """"
    [msacm32.dll] MMRESULT acmStreamReset(HACMSTREAM has, DWORD fdwReset)
    """"
    ret_ad, args = jitter.func_args_stdcall(["has", "fdwReset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmStreamSize(jitter):
    """"
    [msacm32.dll] MMRESULT acmStreamSize(HACMSTREAM has, DWORD cbInput, LPDWORD pdwOutputBytes, DWORD fdwSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["has", "cbInput", "pdwOutputBytes", "fdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msacm32_acmStreamUnprepareHeader(jitter):
    """"
    [msacm32.dll] MMRESULT acmStreamUnprepareHeader(HACMSTREAM has, LPACMSTREAMHEADER pash, DWORD fdwUnprepare)
    """"
    ret_ad, args = jitter.func_args_stdcall(["has", "pash", "fdwUnprepare"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
