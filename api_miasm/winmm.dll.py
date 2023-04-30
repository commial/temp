
def winmm_auxGetDevCaps(jitter, get_str, set_str):
    """
    MMRESULT auxGetDevCaps(
        UINT_PTR uDeviceID,
        LPAUXCAPS lpCaps,
        UINT cbCaps
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "lpCaps", "cbCaps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_auxGetDevCapsA(jitter):
    winmm_auxGetDevCaps(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_auxGetDevCapsW(jitter):
    winmm_auxGetDevCaps(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_auxGetNumDevs(jitter):
    """
    UINT auxGetNumDevs()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_auxGetVolume(jitter):
    """
    MMRESULT auxGetVolume(
        UINT uDeviceID,
        LPDWORD lpdwVolume
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "lpdwVolume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_auxOutMessage(jitter):
    """
    MMRESULT auxOutMessage(
        UINT uDeviceID,
        UINT uMsg,
        DWORD_PTR dwParam1,
        DWORD_PTR dwParam2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "uMsg", "dwParam1", "dwParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_auxSetVolume(jitter):
    """
    MMRESULT auxSetVolume(
        UINT uDeviceID,
        DWORD dwVolume
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "dwVolume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyConfigChanged(jitter):
    """
    MMRESULT joyConfigChanged(
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyGetDevCaps(jitter, get_str, set_str):
    """
    MMRESULT joyGetDevCaps(
        UINT_PTR uJoyID,
        LPJOYCAPS pjc,
        UINT cbjc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uJoyID", "pjc", "cbjc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyGetDevCapsA(jitter):
    winmm_joyGetDevCaps(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_joyGetDevCapsW(jitter):
    winmm_joyGetDevCaps(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_joyGetNumDevs(jitter):
    """
    UINT joyGetNumDevs()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyGetPos(jitter):
    """
    MMRESULT joyGetPos(
        UINT uJoyID,
        LPJOYINFO pji
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uJoyID", "pji"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyGetPosEx(jitter):
    """
    MMRESULT joyGetPosEx(
        UINT uJoyID,
        LPJOYINFOEX pji
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uJoyID", "pji"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyGetThreshold(jitter):
    """
    MMRESULT joyGetThreshold(
        UINT uJoyID,
        LPUINT puThreshold
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uJoyID", "puThreshold"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyReleaseCapture(jitter):
    """
    MMRESULT joyReleaseCapture(
        UINT uJoyID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uJoyID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joySetCapture(jitter):
    """
    MMRESULT joySetCapture(
        HWND hwnd,
        UINT uJoyID,
        UINT uPeriod,
        BOOL fChanged
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "uJoyID", "uPeriod", "fChanged"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joySetThreshold(jitter):
    """
    MMRESULT joySetThreshold(
        UINT uJoyID,
        UINT uThreshold
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uJoyID", "uThreshold"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciExecute(jitter):
    """
    BOOL mciExecute(
        LPCSTR pszCommand
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszCommand"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciGetCreatorTask(jitter):
    """
    HANDLE mciGetCreatorTask(
        MCIDEVICEID IDDevice
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IDDevice"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciGetDeviceID(jitter, get_str, set_str):
    """
    MCIDEVICEID mciGetDeviceID(
        LPCTSTR lpszDevice
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDevice"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciGetDeviceIDA(jitter):
    winmm_mciGetDeviceID(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_mciGetDeviceIDW(jitter):
    winmm_mciGetDeviceID(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_mciGetDeviceIDFromElementID(jitter, get_str, set_str):
    """
    MCIDEVICEID mciGetDeviceIDFromElementID(
        DWORD dwElementID,
        LPCTSTR lpstrType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwElementID", "lpstrType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciGetDeviceIDFromElementIDA(jitter):
    winmm_mciGetDeviceIDFromElementID(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_mciGetDeviceIDFromElementIDW(jitter):
    winmm_mciGetDeviceIDFromElementID(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_mciGetErrorString(jitter, get_str, set_str):
    """
    BOOL mciGetErrorString(
        DWORD fdwError,
        LPTSTR lpszErrorText,
        UINT cchErrorText
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fdwError", "lpszErrorText", "cchErrorText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciGetErrorStringA(jitter):
    winmm_mciGetErrorString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_mciGetErrorStringW(jitter):
    winmm_mciGetErrorString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_mciGetYieldProc(jitter):
    """
    YIELDPROC mciGetYieldProc(
        MCIDEVICEID IDDevice,
        LPDWORD lpdwYieldData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IDDevice", "lpdwYieldData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciSendCommand(jitter, get_str, set_str):
    """
    MCIERROR mciSendCommand(
        MCIDEVICEID IDDevice,
        UINT uMsg,
        DWORD fdwCommand,
        DWORD_PTR dwParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IDDevice", "uMsg", "fdwCommand", "dwParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciSendCommandA(jitter):
    winmm_mciSendCommand(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_mciSendCommandW(jitter):
    winmm_mciSendCommand(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_mciSendString(jitter, get_str, set_str):
    """
    MCIERROR mciSendString(
        LPCTSTR lpszCommand,
        LPTSTR lpszReturnString,
        UINT cchReturn,
        HANDLE hwndCallback
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszCommand", "lpszReturnString", "cchReturn", "hwndCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciSendStringA(jitter):
    winmm_mciSendString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_mciSendStringW(jitter):
    winmm_mciSendString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_mciSetYieldProc(jitter):
    """
    UINT mciSetYieldProc(
        MCIDEVICEID IDDevice,
        YIELDPROC yp,
        DWORD dwYieldData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IDDevice", "yp", "dwYieldData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiConnect(jitter):
    """
    MMRESULT midiConnect(
        HMIDI hMidi,
        HMIDIOUT hmo,
        LPVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMidi", "hmo", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiDisconnect(jitter):
    """
    MMRESULT midiDisconnect(
        HMIDI hMidi,
        HMIDIOUT hmo,
        LPVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMidi", "hmo", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInAddBuffer(jitter):
    """
    MMRESULT midiInAddBuffer(
        HMIDIIN hMidiIn,
        LPMIDIHDR lpMidiInHdr,
        UINT cbMidiInHdr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn", "lpMidiInHdr", "cbMidiInHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInClose(jitter):
    """
    MMRESULT midiInClose(
        HMIDIIN hMidiIn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInGetDevCaps(jitter, get_str, set_str):
    """
    MMRESULT midiInGetDevCaps(
        UINT_PTR uDeviceID,
        LPMIDIINCAPS lpMidiInCaps,
        UINT cbMidiInCaps
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "lpMidiInCaps", "cbMidiInCaps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInGetDevCapsA(jitter):
    winmm_midiInGetDevCaps(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_midiInGetDevCapsW(jitter):
    winmm_midiInGetDevCaps(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_midiInGetErrorText(jitter, get_str, set_str):
    """
    MMRESULT midiInGetErrorText(
        MMRESULT wError,
        LPTSTR lpText,
        UINT cchText
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wError", "lpText", "cchText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInGetErrorTextA(jitter):
    winmm_midiInGetErrorText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_midiInGetErrorTextW(jitter):
    winmm_midiInGetErrorText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_midiInGetID(jitter):
    """
    MMRESULT midiInGetID(
        HMIDIIN hmi,
        LPUINT puDeviceID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmi", "puDeviceID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInGetNumDevs(jitter):
    """
    UINT midiInGetNumDevs()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInMessage(jitter):
    """
    MMRESULT midiInMessage(
        HMIDIIN deviceID,
        UINT msg,
        DWORD_PTR dw1,
        DWORD_PTR dw2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["deviceID", "msg", "dw1", "dw2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInOpen(jitter):
    """
    MMRESULT midiInOpen(
        LPHMIDIIN lphMidiIn,
        UINT_PTR uDeviceID,
        DWORD_PTR dwCallback,
        DWORD_PTR dwCallbackInstance,
        [midiInOutOpenFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lphMidiIn", "uDeviceID", "dwCallback", "dwCallbackInstance", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInPrepareHeader(jitter):
    """
    MMRESULT midiInPrepareHeader(
        HMIDIIN hMidiIn,
        LPMIDIHDR lpMidiInHdr,
        UINT cbMidiInHdr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn", "lpMidiInHdr", "cbMidiInHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInReset(jitter):
    """
    MMRESULT midiInReset(
        HMIDIIN hMidiIn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInStart(jitter):
    """
    MMRESULT midiInStart(
        HMIDIIN hMidiIn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInStop(jitter):
    """
    MMRESULT midiInStop(
        HMIDIIN hMidiIn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInUnprepareHeader(jitter):
    """
    MMRESULT midiInUnprepareHeader(
        HMIDIIN hMidiIn,
        LPMIDIHDR lpMidiInHdr,
        UINT cbMidiInHdr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn", "lpMidiInHdr", "cbMidiInHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutCacheDrumPatches(jitter):
    """
    MMRESULT midiOutCacheDrumPatches(
        HMIDIOUT hmo,
        UINT wPatch,
        WORD* lpKeyArray,
        UINT wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmo", "wPatch", "lpKeyArray", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutCachePatches(jitter):
    """
    MMRESULT midiOutCachePatches(
        HMIDIOUT hmo,
        UINT wBank,
        WORD* lpPatchArray,
        UINT wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmo", "wBank", "lpPatchArray", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutClose(jitter):
    """
    MMRESULT midiOutClose(
        HMIDIOUT hmo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutGetDevCaps(jitter, get_str, set_str):
    """
    MMRESULT midiOutGetDevCaps(
        UINT_PTR uDeviceID,
        LPMIDIOUTCAPS lpMidiOutCaps,
        UINT cbMidiOutCaps
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "lpMidiOutCaps", "cbMidiOutCaps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutGetDevCapsA(jitter):
    winmm_midiOutGetDevCaps(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_midiOutGetDevCapsW(jitter):
    winmm_midiOutGetDevCaps(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_midiOutGetErrorText(jitter, get_str, set_str):
    """
    UINT midiOutGetErrorText(
        MMRESULT mmrError,
        LPTSTR lpText,
        UINT cchText
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["mmrError", "lpText", "cchText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutGetErrorTextA(jitter):
    winmm_midiOutGetErrorText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_midiOutGetErrorTextW(jitter):
    winmm_midiOutGetErrorText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_midiOutGetID(jitter):
    """
    MMRESULT midiOutGetID(
        HMIDIOUT hmo,
        LPUINT puDeviceID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmo", "puDeviceID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutGetNumDevs(jitter):
    """
    UINT midiOutGetNumDevs()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutGetVolume(jitter):
    """
    MMRESULT midiOutGetVolume(
        HMIDIOUT hmo,
        LPDWORD lpdwVolume
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmo", "lpdwVolume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutLongMsg(jitter):
    """
    MMRESULT midiOutLongMsg(
        HMIDIOUT hmo,
        LPMIDIHDR lpMidiOutHdr,
        UINT cbMidiOutHdr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmo", "lpMidiOutHdr", "cbMidiOutHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutMessage(jitter):
    """
    MMRESULT midiOutMessage(
        HMIDIOUT deviceID,
        UINT msg,
        DWORD_PTR dw1,
        DWORD_PTR dw2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["deviceID", "msg", "dw1", "dw2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutOpen(jitter):
    """
    MMRESULT midiOutOpen(
        LPHMIDIOUT lphmo,
        UINT_PTR uDeviceID,
        DWORD_PTR dwCallback,
        DWORD_PTR dwCallbackInstance,
        [midiInOutOpenFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lphmo", "uDeviceID", "dwCallback", "dwCallbackInstance", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutPrepareHeader(jitter):
    """
    MMRESULT midiOutPrepareHeader(
        HMIDIOUT hmo,
        LPMIDIHDR lpMidiOutHdr,
        UINT cbMidiOutHdr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmo", "lpMidiOutHdr", "cbMidiOutHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutReset(jitter):
    """
    MMRESULT midiOutReset(
        HMIDIOUT hmo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutSetVolume(jitter):
    """
    MMRESULT midiOutSetVolume(
        HMIDIOUT hmo,
        DWORD dwVolume
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmo", "dwVolume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutShortMsg(jitter):
    """
    MMRESULT midiOutShortMsg(
        HMIDIOUT hmo,
        DWORD dwMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmo", "dwMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutUnprepareHeader(jitter):
    """
    MMRESULT midiOutUnprepareHeader(
        HMIDIOUT hmo,
        LPMIDIHDR lpMidiOutHdr,
        UINT cbMidiOutHdr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmo", "lpMidiOutHdr", "cbMidiOutHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamClose(jitter):
    """
    MMRESULT midiStreamClose(
        HMIDISTRM hStream
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hStream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamOpen(jitter):
    """
    MMRESULT midiStreamOpen(
        LPHMIDISTRM lphStream,
        LPUINT puDeviceID,
        DWORD cMidi,
        DWORD_PTR dwCallback,
        DWORD_PTR dwInstance,
        DWORD fdwOpen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lphStream", "puDeviceID", "cMidi", "dwCallback", "dwInstance", "fdwOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamOut(jitter):
    """
    MMRESULT midiStreamOut(
        HMIDISTRM hMidiStream,
        LPMIDIHDR lpMidiHdr,
        UINT cbMidiHdr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMidiStream", "lpMidiHdr", "cbMidiHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamPause(jitter):
    """
    MMRESULT midiStreamPause(
        HMIDISTRM hms
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hms"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamPosition(jitter):
    """
    MMRESULT midiStreamPosition(
        HMIDISTRM hms,
        LPMMTIME pmmt,
        UINT cbmmt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hms", "pmmt", "cbmmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamProperty(jitter):
    """
    MMRESULT midiStreamProperty(
        HMIDISTRM hm,
        LPBYTE lppropdata,
        DWORD dwProperty
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hm", "lppropdata", "dwProperty"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamRestart(jitter):
    """
    MMRESULT midiStreamRestart(
        HMIDISTRM hms
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hms"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamStop(jitter):
    """
    MMRESULT midiStreamStop(
        HMIDISTRM hms
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hms"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerClose(jitter):
    """
    MMRESULT mixerClose(
        HMIXER hmx
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerGetControlDetails(jitter, get_str, set_str):
    """
    MMRESULT mixerGetControlDetails(
        HMIXEROBJ hmxobj,
        LPMIXERCONTROLDETAILS pmxcd,
        DWORD fdwDetails
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmxobj", "pmxcd", "fdwDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerGetControlDetailsA(jitter):
    winmm_mixerGetControlDetails(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_mixerGetControlDetailsW(jitter):
    winmm_mixerGetControlDetails(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_mixerGetDevCaps(jitter, get_str, set_str):
    """
    MMRESULT mixerGetDevCaps(
        UINT_PTR uMxId,
        LPMIXERCAPS pmxcaps,
        UINT cbmxcaps
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uMxId", "pmxcaps", "cbmxcaps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerGetDevCapsA(jitter):
    winmm_mixerGetDevCaps(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_mixerGetDevCapsW(jitter):
    winmm_mixerGetDevCaps(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_mixerGetID(jitter):
    """
    MMRESULT mixerGetID(
        HMIXEROBJ hmxobj,
        UINT* puMxId,
        DWORD fdwId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmxobj", "puMxId", "fdwId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerGetLineControls(jitter, get_str, set_str):
    """
    MMRESULT mixerGetLineControls(
        HMIXEROBJ hmxobj,
        LPMIXERLINECONTROLS pmxlc,
        DWORD fdwControls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmxobj", "pmxlc", "fdwControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerGetLineControlsA(jitter):
    winmm_mixerGetLineControls(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_mixerGetLineControlsW(jitter):
    winmm_mixerGetLineControls(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_mixerGetLineInfo(jitter, get_str, set_str):
    """
    MMRESULT mixerGetLineInfo(
        HMIXEROBJ hmxobj,
        LPMIXERLINE pmxl,
        DWORD fdwInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmxobj", "pmxl", "fdwInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerGetLineInfoA(jitter):
    winmm_mixerGetLineInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_mixerGetLineInfoW(jitter):
    winmm_mixerGetLineInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_mixerGetNumDevs(jitter):
    """
    UINT mixerGetNumDevs()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerMessage(jitter):
    """
    DWORD mixerMessage(
        HMIXER driverID,
        UINT uMsg,
        DWORD_PTR dwParam1,
        DWORD_PTR dwParam2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["driverID", "uMsg", "dwParam1", "dwParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerOpen(jitter):
    """
    MMRESULT mixerOpen(
        LPHMIXER phmx,
        UINT uMxId,
        DWORD_PTR dwCallback,
        DWORD_PTR dwInstance,
        DWORD fdwOpen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phmx", "uMxId", "dwCallback", "dwInstance", "fdwOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerSetControlDetails(jitter):
    """
    MMRESULT mixerSetControlDetails(
        HMIXEROBJ hmxobj,
        LPMIXERCONTROLDETAILS pmxcd,
        DWORD fdwDetails
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmxobj", "pmxcd", "fdwDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioAdvance(jitter):
    """
    MMRESULT mmioAdvance(
        HMMIO hmmio,
        LPMMIOINFO lpmmioinfo,
        UINT wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lpmmioinfo", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioAscend(jitter):
    """
    MMRESULT mmioAscend(
        HMMIO hmmio,
        LPMMCKINFO lpck,
        UINT wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lpck", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioClose(jitter):
    """
    MMRESULT mmioClose(
        HMMIO hmmio,
        [mmioCloseFlags] wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioCreateChunk(jitter):
    """
    MMRESULT mmioCreateChunk(
        HMMIO hmmio,
        LPMMCKINFO lpck,
        [mmioCreateChunkFlags] wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lpck", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioDescend(jitter):
    """
    MMRESULT mmioDescend(
        HMMIO hmmio,
        LPMMCKINFO lpck,
        LPMMCKINFO lpckParent,
        [mmioDescendFlags] wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lpck", "lpckParent", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioFlush(jitter):
    """
    MMRESULT mmioFlush(
        HMMIO hmmio,
        [mmioFlushFlags] fuFlush
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "fuFlush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioGetInfo(jitter):
    """
    MMRESULT mmioGetInfo(
        HMMIO hmmio,
        LPMMIOINFO lpmmioinfo,
        UINT wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lpmmioinfo", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioInstallIOProc(jitter, get_str, set_str):
    """
    LPMMIOPROC mmioInstallIOProc(
        FOURCC fccIOProc,
        LPMMIOPROC pIOProc,
        [mmioInstallIOProcFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fccIOProc", "pIOProc", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioInstallIOProcA(jitter):
    winmm_mmioInstallIOProc(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_mmioInstallIOProcW(jitter):
    winmm_mmioInstallIOProc(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_mmioOpen(jitter, get_str, set_str):
    """
    HMMIO mmioOpen(
        LPTSTR szFilename,
        LPMMIOINFO lpmmioinfo,
        DWORD dwOpenFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szFilename", "lpmmioinfo", "dwOpenFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioOpenA(jitter):
    winmm_mmioOpen(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_mmioOpenW(jitter):
    winmm_mmioOpen(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_mmioRead(jitter):
    """
    LONG mmioRead(
        HMMIO hmmio,
        HPSTR pch,
        LONG cch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "pch", "cch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioRename(jitter, get_str, set_str):
    """
    MMRESULT mmioRename(
        LPCTSTR szFilename,
        LPCTSTR szNewFilename,
        const LPMMIOINFO lpmmioinfo,
        DWORD dwRenameFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szFilename", "szNewFilename", "lpmmioinfo", "dwRenameFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioRenameA(jitter):
    winmm_mmioRename(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_mmioRenameW(jitter):
    winmm_mmioRename(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_mmioSeek(jitter):
    """
    LONG mmioSeek(
        HMMIO hmmio,
        LONG lOffset,
        [mmioSeekOffset] iOrigin
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lOffset", "iOrigin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioSendMessage(jitter):
    """
    LRESULT mmioSendMessage(
        HMMIO hmmio,
        UINT wMsg,
        LPARAM lParam1,
        LPARAM lParam2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "wMsg", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioSetBuffer(jitter):
    """
    MMRESULT mmioSetBuffer(
        HMMIO hmmio,
        LPSTR pchBuffer,
        LONG cchBuffer,
        UINT wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "pchBuffer", "cchBuffer", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioSetInfo(jitter):
    """
    MMRESULT mmioSetInfo(
        HMMIO hmmio,
        LPMMIOINFO lpmmioinfo,
        UINT wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lpmmioinfo", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioStringToFOURCC(jitter, get_str, set_str):
    """
    FOURCC mmioStringToFOURCC(
        LPCTSTR sz,
        [mmioStringToFOURCCFlags] wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sz", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioStringToFOURCCA(jitter):
    winmm_mmioStringToFOURCC(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_mmioStringToFOURCCW(jitter):
    winmm_mmioStringToFOURCC(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_mmioWrite(jitter):
    """
    LONG mmioWrite(
        HMMIO hmmio,
        [LPVOID|char*] pch,
        LONG cch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "pch", "cch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeBeginPeriod(jitter):
    """
    MMRESULT timeBeginPeriod(
        UINT uPeriod
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uPeriod"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeEndPeriod(jitter):
    """
    MMRESULT timeEndPeriod(
        UINT uPeriod
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uPeriod"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeGetDevCaps(jitter):
    """
    MMRESULT timeGetDevCaps(
        LPTIMECAPS ptc,
        UINT cbtc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ptc", "cbtc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeGetSystemTime(jitter):
    """
    MMRESULT timeGetSystemTime(
        LPMMTIME pmmt,
        UINT cbmmt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pmmt", "cbmmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeGetTime(jitter):
    """
    DWORD timeGetTime()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeKillEvent(jitter):
    """
    MMRESULT timeKillEvent(
        UINT uTimerID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uTimerID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeSetEvent(jitter):
    """
    MMRESULT timeSetEvent(
        UINT uDelay,
        UINT uResolution,
        LPTIMECALLBACK lpTimeProc,
        DWORD_PTR dwUser,
        UINT fuEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uDelay", "uResolution", "lpTimeProc", "dwUser", "fuEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInAddBuffer(jitter):
    """
    MMRESULT waveInAddBuffer(
        HWAVEIN hwi,
        LPWAVEHDR pwh,
        UINT cbwh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwi", "pwh", "cbwh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInClose(jitter):
    """
    MMRESULT waveInClose(
        HWAVEIN hwi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInGetDevCaps(jitter, get_str, set_str):
    """
    MMRESULT waveInGetDevCaps(
        UINT_PTR uDeviceID,
        LPWAVEINCAPS pwic,
        UINT cbwic
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "pwic", "cbwic"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInGetDevCapsA(jitter):
    winmm_waveInGetDevCaps(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_waveInGetDevCapsW(jitter):
    winmm_waveInGetDevCaps(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_waveInGetErrorText(jitter, get_str, set_str):
    """
    MMRESULT waveInGetErrorText(
        MMRESULT mmrError,
        LPTSTR pszText,
        UINT cchText
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["mmrError", "pszText", "cchText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInGetErrorTextA(jitter):
    winmm_waveInGetErrorText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_waveInGetErrorTextW(jitter):
    winmm_waveInGetErrorText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_waveInGetID(jitter):
    """
    MMRESULT waveInGetID(
        HWAVEIN hwi,
        LPUINT puDeviceID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwi", "puDeviceID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInGetNumDevs(jitter):
    """
    UINT waveInGetNumDevs()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInGetPosition(jitter):
    """
    MMRESULT waveInGetPosition(
        HWAVEIN hwi,
        LPMMTIME pmmt,
        UINT cbmmt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwi", "pmmt", "cbmmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInMessage(jitter):
    """
    MMRESULT waveInMessage(
        HWAVEIN deviceID,
        UINT uMsg,
        DWORD_PTR dwParam1,
        DWORD_PTR dwParam2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["deviceID", "uMsg", "dwParam1", "dwParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInOpen(jitter):
    """
    MMRESULT waveInOpen(
        LPHWAVEIN phwi,
        UINT_PTR uDeviceID,
        LPWAVEFORMATEX pwfx,
        DWORD_PTR dwCallback,
        DWORD_PTR dwCallbackInstance,
        [waveInOutOpenFlags] fdwOpen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phwi", "uDeviceID", "pwfx", "dwCallback", "dwCallbackInstance", "fdwOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInPrepareHeader(jitter):
    """
    MMRESULT waveInPrepareHeader(
        HWAVEIN hwi,
        LPWAVEHDR pwh,
        UINT cbwh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwi", "pwh", "cbwh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInReset(jitter):
    """
    MMRESULT waveInReset(
        HWAVEIN hwi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInStart(jitter):
    """
    MMRESULT waveInStart(
        HWAVEIN hwi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInStop(jitter):
    """
    MMRESULT waveInStop(
        HWAVEIN hwi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInUnprepareHeader(jitter):
    """
    MMRESULT waveInUnprepareHeader(
        HWAVEIN hwi,
        LPWAVEHDR pwh,
        UINT cbwh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwi", "pwh", "cbwh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutBreakLoop(jitter):
    """
    MMRESULT waveOutBreakLoop(
        HWAVEOUT hwo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutClose(jitter):
    """
    MMRESULT waveOutClose(
        HWAVEOUT hwo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetDevCaps(jitter, get_str, set_str):
    """
    MMRESULT waveOutGetDevCaps(
        UINT_PTR uDeviceID,
        LPWAVEOUTCAPS pwoc,
        UINT cbwoc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "pwoc", "cbwoc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetDevCapsA(jitter):
    winmm_waveOutGetDevCaps(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_waveOutGetDevCapsW(jitter):
    winmm_waveOutGetDevCaps(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_waveOutGetErrorText(jitter, get_str, set_str):
    """
    MMRESULT waveOutGetErrorText(
        MMRESULT mmrError,
        LPTSTR pszText,
        UINT cchText
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["mmrError", "pszText", "cchText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetErrorTextA(jitter):
    winmm_waveOutGetErrorText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_waveOutGetErrorTextW(jitter):
    winmm_waveOutGetErrorText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_waveOutGetID(jitter):
    """
    MMRESULT waveOutGetID(
        HWAVEOUT hwo,
        LPUINT puDeviceID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo", "puDeviceID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetNumDevs(jitter):
    """
    UINT waveOutGetNumDevs()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetPitch(jitter):
    """
    MMRESULT waveOutGetPitch(
        HWAVEOUT hwo,
        LPDWORD pdwPitch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pdwPitch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetPlaybackRate(jitter):
    """
    MMRESULT waveOutGetPlaybackRate(
        HWAVEOUT hwo,
        LPDWORD pdwRate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pdwRate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetPosition(jitter):
    """
    MMRESULT waveOutGetPosition(
        HWAVEOUT hwo,
        LPMMTIME pmmt,
        UINT cbmmt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pmmt", "cbmmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetVolume(jitter):
    """
    MMRESULT waveOutGetVolume(
        HWAVEOUT hwo,
        LPDWORD pdwVolume
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pdwVolume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutMessage(jitter):
    """
    MMRESULT waveOutMessage(
        HWAVEOUT deviceID,
        UINT uMsg,
        DWORD_PTR dwParam1,
        DWORD_PTR dwParam2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["deviceID", "uMsg", "dwParam1", "dwParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutOpen(jitter):
    """
    MMRESULT waveOutOpen(
        LPHWAVEOUT phwo,
        UINT_PTR uDeviceID,
        LPWAVEFORMATEX pwfx,
        DWORD_PTR dwCallback,
        DWORD_PTR dwCallbackInstance,
        [waveInOutOpenFlags] fdwOpen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phwo", "uDeviceID", "pwfx", "dwCallback", "dwCallbackInstance", "fdwOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutPause(jitter):
    """
    MMRESULT waveOutPause(
        HWAVEOUT hwo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutPrepareHeader(jitter):
    """
    MMRESULT waveOutPrepareHeader(
        HWAVEOUT hwo,
        LPWAVEHDR pwh,
        UINT cbwh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pwh", "cbwh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutReset(jitter):
    """
    MMRESULT waveOutReset(
        HWAVEOUT hwo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutRestart(jitter):
    """
    MMRESULT waveOutRestart(
        HWAVEOUT hwo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutSetPitch(jitter):
    """
    MMRESULT waveOutSetPitch(
        HWAVEOUT hwo,
        DWORD dwPitch
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo", "dwPitch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutSetPlaybackRate(jitter):
    """
    MMRESULT waveOutSetPlaybackRate(
        HWAVEOUT hwo,
        DWORD dwRate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo", "dwRate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutSetVolume(jitter):
    """
    MMRESULT waveOutSetVolume(
        HWAVEOUT hwo,
        DWORD dwVolume
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo", "dwVolume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutUnprepareHeader(jitter):
    """
    MMRESULT waveOutUnprepareHeader(
        HWAVEOUT hwo,
        LPWAVEHDR pwh,
        UINT cbwh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pwh", "cbwh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutWrite(jitter):
    """
    MMRESULT waveOutWrite(
        HWAVEOUT hwo,
        LPWAVEHDR pwh,
        UINT cbwh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pwh", "cbwh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_PlaySound(jitter, get_str, set_str):
    """
    BOOL PlaySound(
        LPCTSTR pszSound,
        HMODULE hmod,
        [SND_FLAGS] fdwSound
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSound", "hmod", "fdwSound"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_PlaySoundA(jitter):
    winmm_PlaySound(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_PlaySoundW(jitter):
    winmm_PlaySound(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_sndPlaySound(jitter, get_str, set_str):
    """
    BOOL sndPlaySound(
        LPCTSTR lpszSound,
        [SND_FLAGS] fuSound
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszSound", "fuSound"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_sndPlaySoundA(jitter):
    winmm_sndPlaySound(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winmm_sndPlaySoundW(jitter):
    winmm_sndPlaySound(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winmm_CloseDriver(jitter):
    """
    LRESULT CloseDriver(
        HDRVR hDriver,
        LPARAM lParam1,
        LPARAM lParam2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDriver", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_DefDriverProc(jitter):
    """
    LRESULT DefDriverProc(
        DWORD_PTR dwDriverIdentifier,
        HDRVR hdrvr,
        UINT uMsg,
        LPARAM lParam1,
        LPARAM lParam2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwDriverIdentifier", "hdrvr", "uMsg", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_DriverCallback(jitter):
    """
    BOOL DriverCallback(
        DWORD_PTR dwCallback,
        [DCB_FLAGS] dwFlags,
        HDRVR hDevice,
        DWORD dwMsg,
        DWORD_PTR dwUser,
        DWORD_PTR dwParam1,
        DWORD_PTR dwParam2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwCallback", "dwFlags", "hDevice", "dwMsg", "dwUser", "dwParam1", "dwParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_DrvGetModuleHandle(jitter):
    """
    HMODULE DrvGetModuleHandle(
        HDRVR hDriver
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDriver"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_GetDriverModuleHandle(jitter):
    """
    HMODULE GetDriverModuleHandle(
        HDRVR hDriver
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDriver"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_OpenDriver(jitter):
    """
    HDRVR OpenDriver(
        LPCWSTR szDriverName,
        LPCWSTR szSectionName,
        LPARAM lParam2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szDriverName", "szSectionName", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_SendDriverMessage(jitter):
    """
    LRESULT SendDriverMessage(
        HDRVR hDriver,
        UINT message,
        LPARAM lParam1,
        LPARAM lParam2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDriver", "message", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmDrvInstall(jitter):
    """
    UINT mmDrvInstall(
        HDRVR hDriver,
        LPCWSTR wszDrvEntry,
        DRIVERMSGPROC drvMessage,
        UINT wFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDriver", "wszDrvEntry", "drvMessage", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmGetCurrentTask(jitter):
    """
    DWORD mmGetCurrentTask()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmTaskBlock(jitter):
    """
    VOID mmTaskBlock(
        DWORD h
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["h"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmTaskCreate(jitter):
    """
    UINT mmTaskCreate(
        LPTASKCALLBACK lpfn,
        HANDLE* lph,
        DWORD_PTR dwInst
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpfn", "lph", "dwInst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmTaskSignal(jitter):
    """
    BOOL mmTaskSignal(
        DWORD h
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["h"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmTaskYield(jitter):
    """
    VOID mmTaskYield()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
