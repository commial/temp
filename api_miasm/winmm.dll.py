
def winmm_auxGetDevCaps(jitter):
    """"
    [Winmm.dll] MMRESULT auxGetDevCaps(UINT_PTR uDeviceID, LPAUXCAPS lpCaps, UINT cbCaps)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "lpCaps", "cbCaps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_auxGetNumDevs(jitter):
    """"
    [Winmm.dll] UINT auxGetNumDevs()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_auxGetVolume(jitter):
    """"
    [Winmm.dll] MMRESULT auxGetVolume(UINT uDeviceID, LPDWORD lpdwVolume)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "lpdwVolume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_auxOutMessage(jitter):
    """"
    [Winmm.dll] MMRESULT auxOutMessage(UINT uDeviceID, UINT uMsg, DWORD_PTR dwParam1, DWORD_PTR dwParam2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "uMsg", "dwParam1", "dwParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_auxSetVolume(jitter):
    """"
    [Winmm.dll] MMRESULT auxSetVolume(UINT uDeviceID, DWORD dwVolume)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "dwVolume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyConfigChanged(jitter):
    """"
    [Winmm.dll] MMRESULT joyConfigChanged(DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyGetDevCaps(jitter):
    """"
    [Winmm.dll] MMRESULT joyGetDevCaps(UINT_PTR uJoyID, LPJOYCAPS pjc, UINT cbjc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uJoyID", "pjc", "cbjc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyGetNumDevs(jitter):
    """"
    [Winmm.dll] UINT joyGetNumDevs()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyGetPos(jitter):
    """"
    [Winmm.dll] MMRESULT joyGetPos(UINT uJoyID, LPJOYINFO pji)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uJoyID", "pji"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyGetPosEx(jitter):
    """"
    [Winmm.dll] MMRESULT joyGetPosEx(UINT uJoyID, LPJOYINFOEX pji)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uJoyID", "pji"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyGetThreshold(jitter):
    """"
    [Winmm.dll] MMRESULT joyGetThreshold(UINT uJoyID, LPUINT puThreshold)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uJoyID", "puThreshold"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joyReleaseCapture(jitter):
    """"
    [Winmm.dll] MMRESULT joyReleaseCapture(UINT uJoyID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uJoyID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joySetCapture(jitter):
    """"
    [Winmm.dll] MMRESULT joySetCapture(HWND hwnd, UINT uJoyID, UINT uPeriod, BOOL fChanged)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "uJoyID", "uPeriod", "fChanged"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_joySetThreshold(jitter):
    """"
    [Winmm.dll] MMRESULT joySetThreshold(UINT uJoyID, UINT uThreshold)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uJoyID", "uThreshold"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciExecute(jitter):
    """"
    [Winmm.dll] BOOL mciExecute(LPCSTR pszCommand)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszCommand"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciGetCreatorTask(jitter):
    """"
    [Winmm.dll] HANDLE mciGetCreatorTask(MCIDEVICEID IDDevice)
    """"
    ret_ad, args = jitter.func_args_stdcall(["IDDevice"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciGetDeviceID(jitter):
    """"
    [Winmm.dll] MCIDEVICEID mciGetDeviceID(LPCTSTR lpszDevice)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszDevice"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciGetDeviceIDFromElementID(jitter):
    """"
    [Winmm.dll] MCIDEVICEID mciGetDeviceIDFromElementID(DWORD dwElementID, LPCTSTR lpstrType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwElementID", "lpstrType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciGetErrorString(jitter):
    """"
    [Winmm.dll] BOOL mciGetErrorString(DWORD fdwError, LPTSTR lpszErrorText, UINT cchErrorText)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fdwError", "lpszErrorText", "cchErrorText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciGetYieldProc(jitter):
    """"
    [Winmm.dll] YIELDPROC mciGetYieldProc(MCIDEVICEID IDDevice, LPDWORD lpdwYieldData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["IDDevice", "lpdwYieldData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciSendCommand(jitter):
    """"
    [Winmm.dll] MCIERROR mciSendCommand(MCIDEVICEID IDDevice, UINT uMsg, DWORD fdwCommand, DWORD_PTR dwParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["IDDevice", "uMsg", "fdwCommand", "dwParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciSendString(jitter):
    """"
    [Winmm.dll] MCIERROR mciSendString(LPCTSTR lpszCommand, LPTSTR lpszReturnString, UINT cchReturn, HANDLE hwndCallback)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszCommand", "lpszReturnString", "cchReturn", "hwndCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mciSetYieldProc(jitter):
    """"
    [Winmm.dll] UINT mciSetYieldProc(MCIDEVICEID IDDevice, YIELDPROC yp, DWORD dwYieldData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["IDDevice", "yp", "dwYieldData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiConnect(jitter):
    """"
    [Winmm.dll] MMRESULT midiConnect(HMIDI hMidi, HMIDIOUT hmo, LPVOID pReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMidi", "hmo", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiDisconnect(jitter):
    """"
    [Winmm.dll] MMRESULT midiDisconnect(HMIDI hMidi, HMIDIOUT hmo, LPVOID pReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMidi", "hmo", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInAddBuffer(jitter):
    """"
    [Winmm.dll] MMRESULT midiInAddBuffer(HMIDIIN hMidiIn, LPMIDIHDR lpMidiInHdr, UINT cbMidiInHdr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn", "lpMidiInHdr", "cbMidiInHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInClose(jitter):
    """"
    [Winmm.dll] MMRESULT midiInClose(HMIDIIN hMidiIn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInGetDevCaps(jitter):
    """"
    [Winmm.dll] MMRESULT midiInGetDevCaps(UINT_PTR uDeviceID, LPMIDIINCAPS lpMidiInCaps, UINT cbMidiInCaps)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "lpMidiInCaps", "cbMidiInCaps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInGetErrorText(jitter):
    """"
    [Winmm.dll] MMRESULT midiInGetErrorText(MMRESULT wError, LPTSTR lpText, UINT cchText)
    """"
    ret_ad, args = jitter.func_args_stdcall(["wError", "lpText", "cchText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInGetID(jitter):
    """"
    [Winmm.dll] MMRESULT midiInGetID(HMIDIIN hmi, LPUINT puDeviceID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmi", "puDeviceID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInGetNumDevs(jitter):
    """"
    [Winmm.dll] UINT midiInGetNumDevs()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInMessage(jitter):
    """"
    [Winmm.dll] MMRESULT midiInMessage(HMIDIIN deviceID, UINT msg, DWORD_PTR dw1, DWORD_PTR dw2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["deviceID", "msg", "dw1", "dw2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInOpen(jitter):
    """"
    [Winmm.dll] MMRESULT midiInOpen(LPHMIDIIN lphMidiIn, UINT_PTR uDeviceID, DWORD_PTR dwCallback, DWORD_PTR dwCallbackInstance, [midiInOutOpenFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lphMidiIn", "uDeviceID", "dwCallback", "dwCallbackInstance", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInPrepareHeader(jitter):
    """"
    [Winmm.dll] MMRESULT midiInPrepareHeader(HMIDIIN hMidiIn, LPMIDIHDR lpMidiInHdr, UINT cbMidiInHdr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn", "lpMidiInHdr", "cbMidiInHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInReset(jitter):
    """"
    [Winmm.dll] MMRESULT midiInReset(HMIDIIN hMidiIn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInStart(jitter):
    """"
    [Winmm.dll] MMRESULT midiInStart(HMIDIIN hMidiIn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInStop(jitter):
    """"
    [Winmm.dll] MMRESULT midiInStop(HMIDIIN hMidiIn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiInUnprepareHeader(jitter):
    """"
    [Winmm.dll] MMRESULT midiInUnprepareHeader(HMIDIIN hMidiIn, LPMIDIHDR lpMidiInHdr, UINT cbMidiInHdr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMidiIn", "lpMidiInHdr", "cbMidiInHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutCacheDrumPatches(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutCacheDrumPatches(HMIDIOUT hmo, UINT wPatch, WORD* lpKeyArray, UINT wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmo", "wPatch", "lpKeyArray", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutCachePatches(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutCachePatches(HMIDIOUT hmo, UINT wBank, WORD* lpPatchArray, UINT wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmo", "wBank", "lpPatchArray", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutClose(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutClose(HMIDIOUT hmo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutGetDevCaps(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutGetDevCaps(UINT_PTR uDeviceID, LPMIDIOUTCAPS lpMidiOutCaps, UINT cbMidiOutCaps)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "lpMidiOutCaps", "cbMidiOutCaps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutGetErrorText(jitter):
    """"
    [Winmm.dll] UINT midiOutGetErrorText(MMRESULT mmrError, LPTSTR lpText, UINT cchText)
    """"
    ret_ad, args = jitter.func_args_stdcall(["mmrError", "lpText", "cchText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutGetID(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutGetID(HMIDIOUT hmo, LPUINT puDeviceID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmo", "puDeviceID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutGetNumDevs(jitter):
    """"
    [Winmm.dll] UINT midiOutGetNumDevs()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutGetVolume(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutGetVolume(HMIDIOUT hmo, LPDWORD lpdwVolume)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmo", "lpdwVolume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutLongMsg(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutLongMsg(HMIDIOUT hmo, LPMIDIHDR lpMidiOutHdr, UINT cbMidiOutHdr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmo", "lpMidiOutHdr", "cbMidiOutHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutMessage(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutMessage(HMIDIOUT deviceID, UINT msg, DWORD_PTR dw1, DWORD_PTR dw2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["deviceID", "msg", "dw1", "dw2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutOpen(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutOpen(LPHMIDIOUT lphmo, UINT_PTR uDeviceID, DWORD_PTR dwCallback, DWORD_PTR dwCallbackInstance, [midiInOutOpenFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lphmo", "uDeviceID", "dwCallback", "dwCallbackInstance", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutPrepareHeader(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutPrepareHeader(HMIDIOUT hmo, LPMIDIHDR lpMidiOutHdr, UINT cbMidiOutHdr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmo", "lpMidiOutHdr", "cbMidiOutHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutReset(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutReset(HMIDIOUT hmo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutSetVolume(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutSetVolume(HMIDIOUT hmo, DWORD dwVolume)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmo", "dwVolume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutShortMsg(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutShortMsg(HMIDIOUT hmo, DWORD dwMsg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmo", "dwMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiOutUnprepareHeader(jitter):
    """"
    [Winmm.dll] MMRESULT midiOutUnprepareHeader(HMIDIOUT hmo, LPMIDIHDR lpMidiOutHdr, UINT cbMidiOutHdr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmo", "lpMidiOutHdr", "cbMidiOutHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamClose(jitter):
    """"
    [Winmm.dll] MMRESULT midiStreamClose(HMIDISTRM hStream)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hStream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamOpen(jitter):
    """"
    [Winmm.dll] MMRESULT midiStreamOpen(LPHMIDISTRM lphStream, LPUINT puDeviceID, DWORD cMidi, DWORD_PTR dwCallback, DWORD_PTR dwInstance, DWORD fdwOpen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lphStream", "puDeviceID", "cMidi", "dwCallback", "dwInstance", "fdwOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamOut(jitter):
    """"
    [Winmm.dll] MMRESULT midiStreamOut(HMIDISTRM hMidiStream, LPMIDIHDR lpMidiHdr, UINT cbMidiHdr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hMidiStream", "lpMidiHdr", "cbMidiHdr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamPause(jitter):
    """"
    [Winmm.dll] MMRESULT midiStreamPause(HMIDISTRM hms)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hms"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamPosition(jitter):
    """"
    [Winmm.dll] MMRESULT midiStreamPosition(HMIDISTRM hms, LPMMTIME pmmt, UINT cbmmt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hms", "pmmt", "cbmmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamProperty(jitter):
    """"
    [Winmm.dll] MMRESULT midiStreamProperty(HMIDISTRM hm, LPBYTE lppropdata, DWORD dwProperty)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hm", "lppropdata", "dwProperty"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamRestart(jitter):
    """"
    [Winmm.dll] MMRESULT midiStreamRestart(HMIDISTRM hms)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hms"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_midiStreamStop(jitter):
    """"
    [Winmm.dll] MMRESULT midiStreamStop(HMIDISTRM hms)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hms"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerClose(jitter):
    """"
    [Winmm.dll] MMRESULT mixerClose(HMIXER hmx)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerGetControlDetails(jitter):
    """"
    [Winmm.dll] MMRESULT mixerGetControlDetails(HMIXEROBJ hmxobj, LPMIXERCONTROLDETAILS pmxcd, DWORD fdwDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmxobj", "pmxcd", "fdwDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerGetDevCaps(jitter):
    """"
    [Winmm.dll] MMRESULT mixerGetDevCaps(UINT_PTR uMxId, LPMIXERCAPS pmxcaps, UINT cbmxcaps)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uMxId", "pmxcaps", "cbmxcaps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerGetID(jitter):
    """"
    [Winmm.dll] MMRESULT mixerGetID(HMIXEROBJ hmxobj, UINT* puMxId, DWORD fdwId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmxobj", "puMxId", "fdwId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerGetLineControls(jitter):
    """"
    [Winmm.dll] MMRESULT mixerGetLineControls(HMIXEROBJ hmxobj, LPMIXERLINECONTROLS pmxlc, DWORD fdwControls)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmxobj", "pmxlc", "fdwControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerGetLineInfo(jitter):
    """"
    [Winmm.dll] MMRESULT mixerGetLineInfo(HMIXEROBJ hmxobj, LPMIXERLINE pmxl, DWORD fdwInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmxobj", "pmxl", "fdwInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerGetNumDevs(jitter):
    """"
    [Winmm.dll] UINT mixerGetNumDevs()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerMessage(jitter):
    """"
    [Winmm.dll] DWORD mixerMessage(HMIXER driverID, UINT uMsg, DWORD_PTR dwParam1, DWORD_PTR dwParam2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["driverID", "uMsg", "dwParam1", "dwParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerOpen(jitter):
    """"
    [Winmm.dll] MMRESULT mixerOpen(LPHMIXER phmx, UINT uMxId, DWORD_PTR dwCallback, DWORD_PTR dwInstance, DWORD fdwOpen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phmx", "uMxId", "dwCallback", "dwInstance", "fdwOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mixerSetControlDetails(jitter):
    """"
    [Winmm.dll] MMRESULT mixerSetControlDetails(HMIXEROBJ hmxobj, LPMIXERCONTROLDETAILS pmxcd, DWORD fdwDetails)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmxobj", "pmxcd", "fdwDetails"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioAdvance(jitter):
    """"
    [Winmm.dll] MMRESULT mmioAdvance(HMMIO hmmio, LPMMIOINFO lpmmioinfo, UINT wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lpmmioinfo", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioAscend(jitter):
    """"
    [Winmm.dll] MMRESULT mmioAscend(HMMIO hmmio, LPMMCKINFO lpck, UINT wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lpck", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioClose(jitter):
    """"
    [Winmm.dll] MMRESULT mmioClose(HMMIO hmmio, [mmioCloseFlags] wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioCreateChunk(jitter):
    """"
    [Winmm.dll] MMRESULT mmioCreateChunk(HMMIO hmmio, LPMMCKINFO lpck, [mmioCreateChunkFlags] wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lpck", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioDescend(jitter):
    """"
    [Winmm.dll] MMRESULT mmioDescend(HMMIO hmmio, LPMMCKINFO lpck, LPMMCKINFO lpckParent, [mmioDescendFlags] wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lpck", "lpckParent", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioFlush(jitter):
    """"
    [Winmm.dll] MMRESULT mmioFlush(HMMIO hmmio, [mmioFlushFlags] fuFlush)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "fuFlush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioGetInfo(jitter):
    """"
    [Winmm.dll] MMRESULT mmioGetInfo(HMMIO hmmio, LPMMIOINFO lpmmioinfo, UINT wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lpmmioinfo", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioInstallIOProc(jitter):
    """"
    [Winmm.dll] LPMMIOPROC mmioInstallIOProc(FOURCC fccIOProc, LPMMIOPROC pIOProc, [mmioInstallIOProcFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["fccIOProc", "pIOProc", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioOpen(jitter):
    """"
    [Winmm.dll] HMMIO mmioOpen(LPTSTR szFilename, LPMMIOINFO lpmmioinfo, DWORD dwOpenFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szFilename", "lpmmioinfo", "dwOpenFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioRead(jitter):
    """"
    [Winmm.dll] LONG mmioRead(HMMIO hmmio, HPSTR pch, LONG cch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "pch", "cch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioRename(jitter):
    """"
    [Winmm.dll] MMRESULT mmioRename(LPCTSTR szFilename, LPCTSTR szNewFilename, const LPMMIOINFO lpmmioinfo, DWORD dwRenameFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szFilename", "szNewFilename", "lpmmioinfo", "dwRenameFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioSeek(jitter):
    """"
    [Winmm.dll] LONG mmioSeek(HMMIO hmmio, LONG lOffset, [mmioSeekOffset] iOrigin)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lOffset", "iOrigin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioSendMessage(jitter):
    """"
    [Winmm.dll] LRESULT mmioSendMessage(HMMIO hmmio, UINT wMsg, LPARAM lParam1, LPARAM lParam2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "wMsg", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioSetBuffer(jitter):
    """"
    [Winmm.dll] MMRESULT mmioSetBuffer(HMMIO hmmio, LPSTR pchBuffer, LONG cchBuffer, UINT wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "pchBuffer", "cchBuffer", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioSetInfo(jitter):
    """"
    [Winmm.dll] MMRESULT mmioSetInfo(HMMIO hmmio, LPMMIOINFO lpmmioinfo, UINT wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "lpmmioinfo", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioStringToFOURCC(jitter):
    """"
    [Winmm.dll] FOURCC mmioStringToFOURCC(LPCTSTR sz, [mmioStringToFOURCCFlags] wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sz", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmioWrite(jitter):
    """"
    [Winmm.dll] LONG mmioWrite(HMMIO hmmio, [LPVOID|char*] pch, LONG cch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hmmio", "pch", "cch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeBeginPeriod(jitter):
    """"
    [Winmm.dll] MMRESULT timeBeginPeriod(UINT uPeriod)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uPeriod"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeEndPeriod(jitter):
    """"
    [Winmm.dll] MMRESULT timeEndPeriod(UINT uPeriod)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uPeriod"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeGetDevCaps(jitter):
    """"
    [Winmm.dll] MMRESULT timeGetDevCaps(LPTIMECAPS ptc, UINT cbtc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ptc", "cbtc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeGetSystemTime(jitter):
    """"
    [Winmm.dll] MMRESULT timeGetSystemTime(LPMMTIME pmmt, UINT cbmmt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pmmt", "cbmmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeGetTime(jitter):
    """"
    [Winmm.dll] DWORD timeGetTime()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeKillEvent(jitter):
    """"
    [Winmm.dll] MMRESULT timeKillEvent(UINT uTimerID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uTimerID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_timeSetEvent(jitter):
    """"
    [Winmm.dll] MMRESULT timeSetEvent(UINT uDelay, UINT uResolution, LPTIMECALLBACK lpTimeProc, DWORD_PTR dwUser, UINT fuEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uDelay", "uResolution", "lpTimeProc", "dwUser", "fuEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInAddBuffer(jitter):
    """"
    [Winmm.dll] MMRESULT waveInAddBuffer(HWAVEIN hwi, LPWAVEHDR pwh, UINT cbwh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwi", "pwh", "cbwh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInClose(jitter):
    """"
    [Winmm.dll] MMRESULT waveInClose(HWAVEIN hwi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInGetDevCaps(jitter):
    """"
    [Winmm.dll] MMRESULT waveInGetDevCaps(UINT_PTR uDeviceID, LPWAVEINCAPS pwic, UINT cbwic)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "pwic", "cbwic"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInGetErrorText(jitter):
    """"
    [Winmm.dll] MMRESULT waveInGetErrorText(MMRESULT mmrError, LPTSTR pszText, UINT cchText)
    """"
    ret_ad, args = jitter.func_args_stdcall(["mmrError", "pszText", "cchText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInGetID(jitter):
    """"
    [Winmm.dll] MMRESULT waveInGetID(HWAVEIN hwi, LPUINT puDeviceID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwi", "puDeviceID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInGetNumDevs(jitter):
    """"
    [Winmm.dll] UINT waveInGetNumDevs()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInGetPosition(jitter):
    """"
    [Winmm.dll] MMRESULT waveInGetPosition(HWAVEIN hwi, LPMMTIME pmmt, UINT cbmmt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwi", "pmmt", "cbmmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInMessage(jitter):
    """"
    [Winmm.dll] MMRESULT waveInMessage(HWAVEIN deviceID, UINT uMsg, DWORD_PTR dwParam1, DWORD_PTR dwParam2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["deviceID", "uMsg", "dwParam1", "dwParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInOpen(jitter):
    """"
    [Winmm.dll] MMRESULT waveInOpen(LPHWAVEIN phwi, UINT_PTR uDeviceID, LPWAVEFORMATEX pwfx, DWORD_PTR dwCallback, DWORD_PTR dwCallbackInstance, [waveInOutOpenFlags] fdwOpen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phwi", "uDeviceID", "pwfx", "dwCallback", "dwCallbackInstance", "fdwOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInPrepareHeader(jitter):
    """"
    [Winmm.dll] MMRESULT waveInPrepareHeader(HWAVEIN hwi, LPWAVEHDR pwh, UINT cbwh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwi", "pwh", "cbwh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInReset(jitter):
    """"
    [Winmm.dll] MMRESULT waveInReset(HWAVEIN hwi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInStart(jitter):
    """"
    [Winmm.dll] MMRESULT waveInStart(HWAVEIN hwi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInStop(jitter):
    """"
    [Winmm.dll] MMRESULT waveInStop(HWAVEIN hwi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveInUnprepareHeader(jitter):
    """"
    [Winmm.dll] MMRESULT waveInUnprepareHeader(HWAVEIN hwi, LPWAVEHDR pwh, UINT cbwh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwi", "pwh", "cbwh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutBreakLoop(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutBreakLoop(HWAVEOUT hwo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutClose(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutClose(HWAVEOUT hwo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetDevCaps(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutGetDevCaps(UINT_PTR uDeviceID, LPWAVEOUTCAPS pwoc, UINT cbwoc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uDeviceID", "pwoc", "cbwoc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetErrorText(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutGetErrorText(MMRESULT mmrError, LPTSTR pszText, UINT cchText)
    """"
    ret_ad, args = jitter.func_args_stdcall(["mmrError", "pszText", "cchText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetID(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutGetID(HWAVEOUT hwo, LPUINT puDeviceID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo", "puDeviceID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetNumDevs(jitter):
    """"
    [Winmm.dll] UINT waveOutGetNumDevs()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetPitch(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutGetPitch(HWAVEOUT hwo, LPDWORD pdwPitch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pdwPitch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetPlaybackRate(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutGetPlaybackRate(HWAVEOUT hwo, LPDWORD pdwRate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pdwRate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetPosition(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutGetPosition(HWAVEOUT hwo, LPMMTIME pmmt, UINT cbmmt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pmmt", "cbmmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutGetVolume(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutGetVolume(HWAVEOUT hwo, LPDWORD pdwVolume)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pdwVolume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutMessage(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutMessage(HWAVEOUT deviceID, UINT uMsg, DWORD_PTR dwParam1, DWORD_PTR dwParam2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["deviceID", "uMsg", "dwParam1", "dwParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutOpen(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutOpen(LPHWAVEOUT phwo, UINT_PTR uDeviceID, LPWAVEFORMATEX pwfx, DWORD_PTR dwCallback, DWORD_PTR dwCallbackInstance, [waveInOutOpenFlags] fdwOpen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phwo", "uDeviceID", "pwfx", "dwCallback", "dwCallbackInstance", "fdwOpen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutPause(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutPause(HWAVEOUT hwo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutPrepareHeader(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutPrepareHeader(HWAVEOUT hwo, LPWAVEHDR pwh, UINT cbwh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pwh", "cbwh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutReset(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutReset(HWAVEOUT hwo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutRestart(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutRestart(HWAVEOUT hwo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutSetPitch(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutSetPitch(HWAVEOUT hwo, DWORD dwPitch)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo", "dwPitch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutSetPlaybackRate(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutSetPlaybackRate(HWAVEOUT hwo, DWORD dwRate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo", "dwRate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutSetVolume(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutSetVolume(HWAVEOUT hwo, DWORD dwVolume)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo", "dwVolume"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutUnprepareHeader(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutUnprepareHeader(HWAVEOUT hwo, LPWAVEHDR pwh, UINT cbwh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pwh", "cbwh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_waveOutWrite(jitter):
    """"
    [Winmm.dll] MMRESULT waveOutWrite(HWAVEOUT hwo, LPWAVEHDR pwh, UINT cbwh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwo", "pwh", "cbwh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_PlaySound(jitter):
    """"
    [Winmm.dll] BOOL PlaySound(LPCTSTR pszSound, HMODULE hmod, [SND_FLAGS] fdwSound)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszSound", "hmod", "fdwSound"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_sndPlaySound(jitter):
    """"
    [Winmm.dll] BOOL sndPlaySound(LPCTSTR lpszSound, [SND_FLAGS] fuSound)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpszSound", "fuSound"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_CloseDriver(jitter):
    """"
    [Winmm.dll] LRESULT CloseDriver(HDRVR hDriver, LPARAM lParam1, LPARAM lParam2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDriver", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_DefDriverProc(jitter):
    """"
    [Winmm.dll] LRESULT DefDriverProc(DWORD_PTR dwDriverIdentifier, HDRVR hdrvr, UINT uMsg, LPARAM lParam1, LPARAM lParam2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDriverIdentifier", "hdrvr", "uMsg", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_DriverCallback(jitter):
    """"
    [Winmm.dll] BOOL DriverCallback(DWORD_PTR dwCallback, [DCB_FLAGS] dwFlags, HDRVR hDevice, DWORD dwMsg, DWORD_PTR dwUser, DWORD_PTR dwParam1, DWORD_PTR dwParam2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCallback", "dwFlags", "hDevice", "dwMsg", "dwUser", "dwParam1", "dwParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_DrvGetModuleHandle(jitter):
    """"
    [Winmm.dll] HMODULE DrvGetModuleHandle(HDRVR hDriver)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDriver"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_GetDriverModuleHandle(jitter):
    """"
    [Winmm.dll] HMODULE GetDriverModuleHandle(HDRVR hDriver)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDriver"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_OpenDriver(jitter):
    """"
    [Winmm.dll] HDRVR OpenDriver(LPCWSTR szDriverName, LPCWSTR szSectionName, LPARAM lParam2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szDriverName", "szSectionName", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_SendDriverMessage(jitter):
    """"
    [Winmm.dll] LRESULT SendDriverMessage(HDRVR hDriver, UINT message, LPARAM lParam1, LPARAM lParam2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDriver", "message", "lParam1", "lParam2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmDrvInstall(jitter):
    """"
    [Winmm.dll] UINT mmDrvInstall(HDRVR hDriver, LPCWSTR wszDrvEntry, DRIVERMSGPROC drvMessage, UINT wFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDriver", "wszDrvEntry", "drvMessage", "wFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmGetCurrentTask(jitter):
    """"
    [Winmm.dll] DWORD mmGetCurrentTask()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmTaskBlock(jitter):
    """"
    [Winmm.dll] VOID mmTaskBlock(DWORD h)
    """"
    ret_ad, args = jitter.func_args_stdcall(["h"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmTaskCreate(jitter):
    """"
    [Winmm.dll] UINT mmTaskCreate(LPTASKCALLBACK lpfn, HANDLE* lph, DWORD_PTR dwInst)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpfn", "lph", "dwInst"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmTaskSignal(jitter):
    """"
    [Winmm.dll] BOOL mmTaskSignal(DWORD h)
    """"
    ret_ad, args = jitter.func_args_stdcall(["h"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winmm_mmTaskYield(jitter):
    """"
    [Winmm.dll] VOID mmTaskYield()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
