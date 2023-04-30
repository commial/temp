###### Enums ######
_AUXCAPS_TECH_ = {
    "AUXCAPS_CDAUDIO": 1,
    "AUXCAPS_AUXIN": 2,
}
_AUXCAPS_TECH__INV = {
    1: "AUXCAPS_CDAUDIO",
    2: "AUXCAPS_AUXIN",
}
_MIDIOUTCAPS_TECH_ = {
    "MOD_MIDIPORT": 1,
    "MOD_SYNTH": 2,
    "MOD_SQSYNTH": 3,
    "MOD_FMSYNTH": 4,
    "MOD_MAPPER": 5,
    "MOD_WAVETABLE": 6,
    "MOD_SWSYNTH": 7,
}
_MIDIOUTCAPS_TECH__INV = {
    1: "MOD_MIDIPORT",
    2: "MOD_SYNTH",
    3: "MOD_SQSYNTH",
    4: "MOD_FMSYNTH",
    5: "MOD_MAPPER",
    6: "MOD_WAVETABLE",
    7: "MOD_SWSYNTH",
}
_MIXERCONTROL_CT_CLASS_ = {
    "MIXERCONTROL_CT_CLASS_CUSTOM": 0x00000000,
    "MIXERCONTROL_CT_CLASS_METER": 0x10000000,
    "MIXERCONTROL_CT_CLASS_SWITCH": 0x20000000,
    "MIXERCONTROL_CT_CLASS_NUMBER": 0x30000000,
    "MIXERCONTROL_CT_CLASS_SLIDER": 0x40000000,
    "MIXERCONTROL_CT_CLASS_FADER": 0x50000000,
    "MIXERCONTROL_CT_CLASS_TIME": 0x60000000,
    "MIXERCONTROL_CT_CLASS_LIST": 0x70000000,
}
_MIXERCONTROL_CT_CLASS__INV = {
    0x00000000: "MIXERCONTROL_CT_CLASS_CUSTOM",
    0x10000000: "MIXERCONTROL_CT_CLASS_METER",
    0x20000000: "MIXERCONTROL_CT_CLASS_SWITCH",
    0x30000000: "MIXERCONTROL_CT_CLASS_NUMBER",
    0x40000000: "MIXERCONTROL_CT_CLASS_SLIDER",
    0x50000000: "MIXERCONTROL_CT_CLASS_FADER",
    0x60000000: "MIXERCONTROL_CT_CLASS_TIME",
    0x70000000: "MIXERCONTROL_CT_CLASS_LIST",
}
_MIXERLINE_COMPONENTTYPE_ = {
    "MIXERLINE_COMPONENTTYPE_DST_UNDEFINED": 0,
    "MIXERLINE_COMPONENTTYPE_DST_DIGITAL": 1,
    "MIXERLINE_COMPONENTTYPE_DST_LINE": 2,
    "MIXERLINE_COMPONENTTYPE_DST_MONITOR": 3,
    "MIXERLINE_COMPONENTTYPE_DST_SPEAKERS": 4,
    "MIXERLINE_COMPONENTTYPE_DST_HEADPHONES": 5,
    "MIXERLINE_COMPONENTTYPE_DST_TELEPHONE": 6,
    "MIXERLINE_COMPONENTTYPE_DST_WAVEIN": 7,
    "MIXERLINE_COMPONENTTYPE_DST_VOICEIN": 8,
    "MIXERLINE_COMPONENTTYPE_SRC_UNDEFINED": 0x00001000,
    "MIXERLINE_COMPONENTTYPE_SRC_DIGITAL": 0x00001001,
    "MIXERLINE_COMPONENTTYPE_SRC_LINE": 0x00001002,
    "MIXERLINE_COMPONENTTYPE_SRC_MICROPHONE": 0x00001003,
    "MIXERLINE_COMPONENTTYPE_SRC_SYNTHESIZER": 0x00001004,
    "MIXERLINE_COMPONENTTYPE_SRC_COMPACTDISC": 0x00001005,
    "MIXERLINE_COMPONENTTYPE_SRC_TELEPHONE": 0x00001006,
    "MIXERLINE_COMPONENTTYPE_SRC_PCSPEAKER": 0x00001007,
    "MIXERLINE_COMPONENTTYPE_SRC_WAVEOUT": 0x00001008,
    "MIXERLINE_COMPONENTTYPE_SRC_AUXILIARY": 0x00001009,
    "MIXERLINE_COMPONENTTYPE_SRC_ANALOG": 0x0000100A,
}
_MIXERLINE_COMPONENTTYPE__INV = {
    0: "MIXERLINE_COMPONENTTYPE_DST_UNDEFINED",
    1: "MIXERLINE_COMPONENTTYPE_DST_DIGITAL",
    2: "MIXERLINE_COMPONENTTYPE_DST_LINE",
    3: "MIXERLINE_COMPONENTTYPE_DST_MONITOR",
    4: "MIXERLINE_COMPONENTTYPE_DST_SPEAKERS",
    5: "MIXERLINE_COMPONENTTYPE_DST_HEADPHONES",
    6: "MIXERLINE_COMPONENTTYPE_DST_TELEPHONE",
    7: "MIXERLINE_COMPONENTTYPE_DST_WAVEIN",
    8: "MIXERLINE_COMPONENTTYPE_DST_VOICEIN",
    0x00001000: "MIXERLINE_COMPONENTTYPE_SRC_UNDEFINED",
    0x00001001: "MIXERLINE_COMPONENTTYPE_SRC_DIGITAL",
    0x00001002: "MIXERLINE_COMPONENTTYPE_SRC_LINE",
    0x00001003: "MIXERLINE_COMPONENTTYPE_SRC_MICROPHONE",
    0x00001004: "MIXERLINE_COMPONENTTYPE_SRC_SYNTHESIZER",
    0x00001005: "MIXERLINE_COMPONENTTYPE_SRC_COMPACTDISC",
    0x00001006: "MIXERLINE_COMPONENTTYPE_SRC_TELEPHONE",
    0x00001007: "MIXERLINE_COMPONENTTYPE_SRC_PCSPEAKER",
    0x00001008: "MIXERLINE_COMPONENTTYPE_SRC_WAVEOUT",
    0x00001009: "MIXERLINE_COMPONENTTYPE_SRC_AUXILIARY",
    0x0000100A: "MIXERLINE_COMPONENTTYPE_SRC_ANALOG",
}
_MIXERLINE_TARGETTYPE_ = {
    "MIXERLINE_TARGETTYPE_UNDEFINED": 0,
    "MIXERLINE_TARGETTYPE_WAVEOUT": 1,
    "MIXERLINE_TARGETTYPE_WAVEIN": 2,
    "MIXERLINE_TARGETTYPE_MIDIOUT": 3,
    "MIXERLINE_TARGETTYPE_MIDIIN": 4,
    "MIXERLINE_TARGETTYPE_AUX": 5,
}
_MIXERLINE_TARGETTYPE__INV = {
    0: "MIXERLINE_TARGETTYPE_UNDEFINED",
    1: "MIXERLINE_TARGETTYPE_WAVEOUT",
    2: "MIXERLINE_TARGETTYPE_WAVEIN",
    3: "MIXERLINE_TARGETTYPE_MIDIOUT",
    4: "MIXERLINE_TARGETTYPE_MIDIIN",
    5: "MIXERLINE_TARGETTYPE_AUX",
}
_JoyPov_ = {
    "JOY_POVCENTERED": 0xFFFF,
    "JOY_POVFORWARD": 0,
    "JOY_POVRIGHT": 9000,
    "JOY_POVBACKWARD": 18000,
    "JOY_POVLEFT": 27000,
}
_JoyPov__INV = {
    0xFFFF: "JOY_POVCENTERED",
    0: "JOY_POVFORWARD",
    9000: "JOY_POVRIGHT",
    18000: "JOY_POVBACKWARD",
    27000: "JOY_POVLEFT",
}
MCIERROR = {
    "MCIERR_INVALID_DEVICE_ID": 257,
    "MCIERR_UNRECOGNIZED_KEYWORD": 259,
    "MCIERR_UNRECOGNIZED_COMMAND": 261,
    "MCIERR_HARDWARE": 262,
    "MCIERR_INVALID_DEVICE_NAME": 263,
    "MCIERR_OUT_OF_MEMORY": 264,
    "MCIERR_DEVICE_OPEN": 265,
    "MCIERR_CANNOT_LOAD_DRIVER": 266,
    "MCIERR_MISSING_COMMAND_STRING": 267,
    "MCIERR_PARAM_OVERFLOW": 268,
    "MCIERR_MISSING_STRING_ARGUMENT": 269,
    "MCIERR_BAD_INTEGER": 270,
    "MCIERR_PARSER_INTERNAL": 271,
    "MCIERR_DRIVER_INTERNAL": 272,
    "MCIERR_MISSING_PARAMETER": 273,
    "MCIERR_UNSUPPORTED_FUNCTION": 274,
    "MCIERR_FILE_NOT_FOUND": 275,
    "MCIERR_DEVICE_NOT_READY": 276,
    "MCIERR_INTERNAL": 277,
    "MCIERR_DRIVER": 278,
    "MCIERR_CANNOT_USE_ALL": 279,
    "MCIERR_MULTIPLE": 280,
    "MCIERR_EXTENSION_NOT_FOUND": 281,
    "MCIERR_OUTOFRANGE": 282,
    "MCIERR_FLAGS_NOT_COMPATIBLE": 284,
    "MCIERR_FILE_NOT_SAVED": 286,
    "MCIERR_DEVICE_TYPE_REQUIRED": 287,
    "MCIERR_DEVICE_LOCKED": 288,
    "MCIERR_DUPLICATE_ALIAS": 289,
    "MCIERR_BAD_CONSTANT": 290,
    "MCIERR_MUST_USE_SHAREABLE": 291,
    "MCIERR_MISSING_DEVICE_NAME": 292,
    "MCIERR_BAD_TIME_FORMAT": 293,
    "MCIERR_NO_CLOSING_QUOTE": 294,
    "MCIERR_DUPLICATE_FLAGS": 295,
    "MCIERR_INVALID_FILE": 296,
    "MCIERR_NULL_PARAMETER_BLOCK": 297,
    "MCIERR_UNNAMED_RESOURCE": 298,
    "MCIERR_NEW_REQUIRES_ALIAS": 299,
    "MCIERR_NOTIFY_ON_AUTO_OPEN": 300,
    "MCIERR_NO_ELEMENT_ALLOWED": 301,
    "MCIERR_NONAPPLICABLE_FUNCTION": 302,
    "MCIERR_ILLEGAL_FOR_AUTO_OPEN": 303,
    "MCIERR_FILENAME_REQUIRED": 304,
    "MCIERR_EXTRA_CHARACTERS": 305,
    "MCIERR_DEVICE_NOT_INSTALLED": 306,
    "MCIERR_GET_CD": 307,
    "MCIERR_SET_CD": 308,
    "MCIERR_SET_DRIVE": 309,
    "MCIERR_DEVICE_LENGTH": 310,
    "MCIERR_DEVICE_ORD_LENGTH": 311,
    "MCIERR_NO_INTEGER": 312,
    "MCIERR_WAVE_OUTPUTSINUSE": 320,
    "MCIERR_WAVE_SETOUTPUTINUSE": 321,
    "MCIERR_WAVE_INPUTSINUSE": 322,
    "MCIERR_WAVE_SETINPUTINUSE": 323,
    "MCIERR_WAVE_OUTPUTUNSPECIFIED": 324,
    "MCIERR_WAVE_INPUTUNSPECIFIED": 325,
    "MCIERR_WAVE_OUTPUTSUNSUITABLE": 326,
    "MCIERR_WAVE_SETOUTPUTUNSUITABLE": 327,
    "MCIERR_WAVE_INPUTSUNSUITABLE": 328,
    "MCIERR_WAVE_SETINPUTUNSUITABLE": 329,
    "MCIERR_SEQ_DIV_INCOMPATIBLE": 336,
    "MCIERR_SEQ_PORT_INUSE": 337,
    "MCIERR_SEQ_PORT_NONEXISTENT": 338,
    "MCIERR_SEQ_PORT_MAPNODEVICE": 339,
    "MCIERR_SEQ_PORT_MISCERROR": 340,
    "MCIERR_SEQ_TIMER": 341,
    "MCIERR_SEQ_PORTUNSPECIFIED": 342,
    "MCIERR_SEQ_NOMIDIPRESENT": 343,
    "MCIERR_NO_WINDOW": 346,
    "MCIERR_CREATEWINDOW": 347,
    "MCIERR_FILE_READ": 348,
    "MCIERR_FILE_WRITE": 349,
    "MCIERR_NO_IDENTITY": 350,
}
MCIERROR_INV = {
    257: "MCIERR_INVALID_DEVICE_ID",
    259: "MCIERR_UNRECOGNIZED_KEYWORD",
    261: "MCIERR_UNRECOGNIZED_COMMAND",
    262: "MCIERR_HARDWARE",
    263: "MCIERR_INVALID_DEVICE_NAME",
    264: "MCIERR_OUT_OF_MEMORY",
    265: "MCIERR_DEVICE_OPEN",
    266: "MCIERR_CANNOT_LOAD_DRIVER",
    267: "MCIERR_MISSING_COMMAND_STRING",
    268: "MCIERR_PARAM_OVERFLOW",
    269: "MCIERR_MISSING_STRING_ARGUMENT",
    270: "MCIERR_BAD_INTEGER",
    271: "MCIERR_PARSER_INTERNAL",
    272: "MCIERR_DRIVER_INTERNAL",
    273: "MCIERR_MISSING_PARAMETER",
    274: "MCIERR_UNSUPPORTED_FUNCTION",
    275: "MCIERR_FILE_NOT_FOUND",
    276: "MCIERR_DEVICE_NOT_READY",
    277: "MCIERR_INTERNAL",
    278: "MCIERR_DRIVER",
    279: "MCIERR_CANNOT_USE_ALL",
    280: "MCIERR_MULTIPLE",
    281: "MCIERR_EXTENSION_NOT_FOUND",
    282: "MCIERR_OUTOFRANGE",
    284: "MCIERR_FLAGS_NOT_COMPATIBLE",
    286: "MCIERR_FILE_NOT_SAVED",
    287: "MCIERR_DEVICE_TYPE_REQUIRED",
    288: "MCIERR_DEVICE_LOCKED",
    289: "MCIERR_DUPLICATE_ALIAS",
    290: "MCIERR_BAD_CONSTANT",
    291: "MCIERR_MUST_USE_SHAREABLE",
    292: "MCIERR_MISSING_DEVICE_NAME",
    293: "MCIERR_BAD_TIME_FORMAT",
    294: "MCIERR_NO_CLOSING_QUOTE",
    295: "MCIERR_DUPLICATE_FLAGS",
    296: "MCIERR_INVALID_FILE",
    297: "MCIERR_NULL_PARAMETER_BLOCK",
    298: "MCIERR_UNNAMED_RESOURCE",
    299: "MCIERR_NEW_REQUIRES_ALIAS",
    300: "MCIERR_NOTIFY_ON_AUTO_OPEN",
    301: "MCIERR_NO_ELEMENT_ALLOWED",
    302: "MCIERR_NONAPPLICABLE_FUNCTION",
    303: "MCIERR_ILLEGAL_FOR_AUTO_OPEN",
    304: "MCIERR_FILENAME_REQUIRED",
    305: "MCIERR_EXTRA_CHARACTERS",
    306: "MCIERR_DEVICE_NOT_INSTALLED",
    307: "MCIERR_GET_CD",
    308: "MCIERR_SET_CD",
    309: "MCIERR_SET_DRIVE",
    310: "MCIERR_DEVICE_LENGTH",
    311: "MCIERR_DEVICE_ORD_LENGTH",
    312: "MCIERR_NO_INTEGER",
    320: "MCIERR_WAVE_OUTPUTSINUSE",
    321: "MCIERR_WAVE_SETOUTPUTINUSE",
    322: "MCIERR_WAVE_INPUTSINUSE",
    323: "MCIERR_WAVE_SETINPUTINUSE",
    324: "MCIERR_WAVE_OUTPUTUNSPECIFIED",
    325: "MCIERR_WAVE_INPUTUNSPECIFIED",
    326: "MCIERR_WAVE_OUTPUTSUNSUITABLE",
    327: "MCIERR_WAVE_SETOUTPUTUNSUITABLE",
    328: "MCIERR_WAVE_INPUTSUNSUITABLE",
    329: "MCIERR_WAVE_SETINPUTUNSUITABLE",
    336: "MCIERR_SEQ_DIV_INCOMPATIBLE",
    337: "MCIERR_SEQ_PORT_INUSE",
    338: "MCIERR_SEQ_PORT_NONEXISTENT",
    339: "MCIERR_SEQ_PORT_MAPNODEVICE",
    340: "MCIERR_SEQ_PORT_MISCERROR",
    341: "MCIERR_SEQ_TIMER",
    342: "MCIERR_SEQ_PORTUNSPECIFIED",
    343: "MCIERR_SEQ_NOMIDIPRESENT",
    346: "MCIERR_NO_WINDOW",
    347: "MCIERR_CREATEWINDOW",
    348: "MCIERR_FILE_READ",
    349: "MCIERR_FILE_WRITE",
    350: "MCIERR_NO_IDENTITY",
}
_mmioSeekOffset_ = {
    "SEEK_SET": 0,
    "SEEK_CUR": 1,
    "SEEK_END": 2,
}
_mmioSeekOffset__INV = {
    0: "SEEK_SET",
    1: "SEEK_CUR",
    2: "SEEK_END",
}
_MMTIME_TYPE_ = {
    "TIME_MS": 0x0001,
    "TIME_SAMPLES": 0x0002,
    "TIME_BYTES": 0x0004,
    "TIME_SMPTE": 0x0008,
    "TIME_MIDI": 0x0010,
    "TIME_TICKS": 0x0020,
}
_MMTIME_TYPE__INV = {
    0x0001: "TIME_MS",
    0x0002: "TIME_SAMPLES",
    0x0004: "TIME_BYTES",
    0x0008: "TIME_SMPTE",
    0x0010: "TIME_MIDI",
    0x0020: "TIME_TICKS",
}
_SND_FLAGS_ = {
    "SND_SYNC": 0x0000,
    "SND_ASYNC": 0x0001,
    "SND_NODEFAULT": 0x0002,
    "SND_MEMORY": 0x0004,
    "SND_LOOP": 0x0008,
    "SND_NOSTOP": 0x0010,
    "SND_NOWAIT": 0x00002000,
    "SND_ALIAS": 0x00010000,
    "SND_ALIAS_ID": 0x00110000,
    "SND_FILENAME": 0x00020000,
    "SND_RESOURCE": 0x00040004,
    "SND_PURGE": 0x0040,
    "SND_APPLICATION": 0x0080,
    "SND_SENTRY": 0x00080000,
    "SND_RING": 0x00100000,
    "SND_SYSTEM": 0x00200000,
}
_SND_FLAGS__INV = {
    0x0000: "SND_SYNC",
    0x0001: "SND_ASYNC",
    0x0002: "SND_NODEFAULT",
    0x0004: "SND_MEMORY",
    0x0008: "SND_LOOP",
    0x0010: "SND_NOSTOP",
    0x00002000: "SND_NOWAIT",
    0x00010000: "SND_ALIAS",
    0x00110000: "SND_ALIAS_ID",
    0x00020000: "SND_FILENAME",
    0x00040004: "SND_RESOURCE",
    0x0040: "SND_PURGE",
    0x0080: "SND_APPLICATION",
    0x00080000: "SND_SENTRY",
    0x00100000: "SND_RING",
    0x00200000: "SND_SYSTEM",
}

###################

###### Types ######
MCIDEVICEID = UINT
YIELDPROC = LPVOID
HMIDI = HANDLE
HMIDIOUT = HANDLE
LPHMIDIOUT = Ptr("<I", HMIDIOUT())
HMIDIIN = HANDLE
LPHMIDIIN = Ptr("<I", HMIDIIN())
HMIDISTRM = HANDLE
LPHMIDISTRM = Ptr("<I", HMIDISTRM())
HMIXER = HANDLE
LPHMIXER = Ptr("<I", HMIXER())
HMIXEROBJ = HMIXER
HMMIO = HANDLE
LPMMIOPROC = LPVOID
HPSTR = LPVOID
HWAVEIN = HANDLE
LPHWAVEIN = Ptr("<I", HWAVEIN())
HWAVEOUT = HANDLE
LPHWAVEOUT = Ptr("<I", HWAVEOUT())
LPTIMECALLBACK = LPVOID
MMVERSION = UINT
HDRVR = HANDLE
DRIVERMSGPROC = LPVOID
LPTASKCALLBACK = LPVOID
DWORD__6_ = Array(DWORD, 6)
DWORD_PTR__8_ = Array(DWORD_PTR, 8)
TCHAR__MAXPNAMELEN_ = Array(TCHAR, 32)
TCHAR__MIXER_SHORT_NAME_CHARS_ = Array(TCHAR, 16)
TCHAR__MIXER_LONG_NAME_CHARS_ = Array(TCHAR, 64)
TCHAR__MAX_JOYSTICKOEMVXDNAME_ = Array(TCHAR, 260)
_WAVE_FORMAT_ = DWORD
_AUXCAPS_TECH_ = WORD
_AUXCAPS_SUPPORT_ = DWORD

class AUXCAPS(MemStruct):
    fields = [
        ("wMid", WORD()),
        ("wPid", WORD()),
        ("vDriverVersion", MMVERSION()),
        ("szPname", TCHAR__MAXPNAMELEN_()),
        ("wTechnology", _AUXCAPS_TECH_()),
        ("wReserved1", WORD()),
        ("dwSupport", _AUXCAPS_SUPPORT_()),
    ]

LPAUXCAPS = Ptr("<I", AUXCAPS())
_JOYCAPS_FLAGS_ = UINT

class JOYCAPS(MemStruct):
    fields = [
        ("wMid", WORD()),
        ("wPid", WORD()),
        ("szPname", TCHAR__MAXPNAMELEN_()),
        ("wXmin", UINT()),
        ("wXmax", UINT()),
        ("wYmin", UINT()),
        ("wYmax", UINT()),
        ("wZmin", UINT()),
        ("wZmax", UINT()),
        ("wNumButtons", UINT()),
        ("wPeriodMin", UINT()),
        ("wPeriodMax", UINT()),
        ("wRmin", UINT()),
        ("wRmax", UINT()),
        ("wUmin", UINT()),
        ("wUmax", UINT()),
        ("wVmin", UINT()),
        ("wVmax", UINT()),
        ("wCaps", _JOYCAPS_FLAGS_()),
        ("wMaxAxes", UINT()),
        ("wNumAxes", UINT()),
        ("wMaxButtons", UINT()),
        ("szRegKey", TCHAR__MAXPNAMELEN_()),
        ("szOEMVxD", TCHAR__MAX_JOYSTICKOEMVXDNAME_()),
    ]

LPJOYCAPS = Ptr("<I", JOYCAPS())
_MIDIHDR_FLAGS_ = DWORD

class MIDIHDR(MemStruct):
    fields = [
        ("lpData", LPVOID()),
        ("dwBufferLength", DWORD()),
        ("dwBytesRecorded", DWORD()),
        ("dwUser", DWORD_PTR()),
        ("dwFlags", _MIDIHDR_FLAGS_()),
        ("lpNext", LPVOID()),
        ("reserved", DWORD_PTR()),
        ("dwOffset", DWORD()),
        ("dwReserved", DWORD_PTR__8_()),
    ]

LPMIDIHDR = Ptr("<I", MIDIHDR())

class MIDIINCAPS(MemStruct):
    fields = [
        ("wMid", WORD()),
        ("wPid", WORD()),
        ("vDriverVersion", MMVERSION()),
        ("szPname", TCHAR__MAXPNAMELEN_()),
        ("dwSupport", DWORD()),
    ]

LPMIDIINCAPS = Ptr("<I", MIDIINCAPS())
_MIDIOUTCAPS_TECH_ = WORD
_MIDICAPS_FLAGS_ = DWORD

class MIDIOUTCAPS(MemStruct):
    fields = [
        ("wMid", WORD()),
        ("wPid", WORD()),
        ("vDriverVersion", MMVERSION()),
        ("szPname", TCHAR__MAXPNAMELEN_()),
        ("wTechnology", _MIDIOUTCAPS_TECH_()),
        ("wVoices", WORD()),
        ("wNotes", WORD()),
        ("wChannelMask", WORD()),
        ("dwSupport", _MIDICAPS_FLAGS_()),
    ]

LPMIDIOUTCAPS = Ptr("<I", MIDIOUTCAPS())
_MIXERCONTROLDETAILS_u_ = Union([
    ("hwndOwner", HWND),
    ("cMultipleItems", DWORD),
])

class MIXERCONTROLDETAILS(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwControlID", DWORD()),
        ("cChannels", DWORD()),
        (None, _MIXERCONTROLDETAILS_u_()),
        ("cbDetails", DWORD()),
        ("paDetails", LPVOID()),
    ]

LPMIXERCONTROLDETAILS = Ptr("<I", MIXERCONTROLDETAILS())

class MIXERCAPS(MemStruct):
    fields = [
        ("wMid", WORD()),
        ("wPid", WORD()),
        ("vDriverVersion", MMVERSION()),
        ("szPname", TCHAR__MAXPNAMELEN_()),
        ("fdwSupport", DWORD()),
        ("cDestinations", DWORD()),
    ]

LPMIXERCAPS = Ptr("<I", MIXERCAPS())
_MIXERLINECONTROLS_u_ = Union([
    ("dwControlID", DWORD),
    ("dwControlType", DWORD),
])

class _MIXERCONTROL_u1_s1_(MemStruct):
    fields = [
        ("lMinimum", LONG()),
        ("lMaximum", LONG()),
    ]


class _MIXERCONTROL_u1_s2_(MemStruct):
    fields = [
        ("dwMinimum", DWORD()),
        ("dwMaximum", DWORD()),
    ]

_MIXERCONTROL_u1_ = Union([
    (None, _MIXERCONTROL_u1_s1_),
    (None, _MIXERCONTROL_u1_s2_),
    ("dwReserved", DWORD__6_),
])
_MIXERCONTROL_u2_ = Union([
    ("cSteps", DWORD),
    ("cbCustomData", DWORD),
    ("dwReserved", DWORD__6_),
])
_MIXERCONTROL_CT_CLASS_ = DWORD
_MIXERCONTROL_CONTROLF_ = DWORD

class MIXERCONTROL(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwControlID", DWORD()),
        ("dwControlType", _MIXERCONTROL_CT_CLASS_()),
        ("fdwControl", _MIXERCONTROL_CONTROLF_()),
        ("cMultipleItems", DWORD()),
        ("szShortName", TCHAR__MIXER_SHORT_NAME_CHARS_()),
        ("szName", TCHAR__MIXER_LONG_NAME_CHARS_()),
        ("Bounds", _MIXERCONTROL_u1_()),
        ("Metrics", _MIXERCONTROL_u2_()),
    ]

LPMIXERCONTROL = Ptr("<I", MIXERCONTROL())

class MIXERLINECONTROLS(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwLineID", DWORD()),
        (None, _MIXERLINECONTROLS_u_()),
        ("cControls", DWORD()),
        ("cbmxctrl", DWORD()),
        ("pamxctrl", LPMIXERCONTROL()),
    ]

LPMIXERLINECONTROLS = Ptr("<I", MIXERLINECONTROLS())
_MIXERLINE_LINEF_ = DWORD
_MIXERLINE_COMPONENTTYPE_ = DWORD
_MIXERLINE_TARGETTYPE_ = DWORD

class _MIXERLINE_s_(MemStruct):
    fields = [
        ("dwType", _MIXERLINE_TARGETTYPE_()),
        ("dwDeviceID", DWORD()),
        ("wMid", WORD()),
        ("wPid", WORD()),
        ("vDriverVersion", MMVERSION()),
        ("szPname", TCHAR__MAXPNAMELEN_()),
    ]


class MIXERLINE(MemStruct):
    fields = [
        ("cbStruct", DWORD()),
        ("dwDestination", DWORD()),
        ("dwSource", DWORD()),
        ("dwLineID", DWORD()),
        ("fdwLine", _MIXERLINE_LINEF_()),
        ("dwUser", DWORD_PTR()),
        ("dwComponentType", _MIXERLINE_COMPONENTTYPE_()),
        ("cChannels", DWORD()),
        ("cConnections", DWORD()),
        ("cControls", DWORD()),
        ("szShortName", TCHAR__MIXER_SHORT_NAME_CHARS_()),
        ("szName", TCHAR__MIXER_LONG_NAME_CHARS_()),
        ("Target", _MIXERLINE_s_()),
    ]

LPMIXERLINE = Ptr("<I", MIXERLINE())
_MMIOINFO_FLAGS_ = DWORD

class MMIOINFO(MemStruct):
    fields = [
        ("dwFlags", _MMIOINFO_FLAGS_()),
        ("fccIOProc", FOURCC()),
        ("pIOProc", LPMMIOPROC()),
        ("wErrorRet", MMRESULT()),
        ("htask", HTASK()),
        ("cchBuffer", LONG()),
        ("pchBuffer", HPSTR()),
        ("pchNext", HPSTR()),
        ("pchEndRead", HPSTR()),
        ("pchEndWrite", HPSTR()),
        ("lBufOffset", LONG()),
        ("lDiskOffset", LONG()),
        ("adwInfo", DWORD__3_()),
        ("dwReserved1", DWORD()),
        ("dwReserved2", DWORD()),
        ("hmmio", HMMIO()),
    ]

LPMMIOINFO = Ptr("<I", MMIOINFO())
const_LPMMIOINFO = Ptr("<I", MMIOINFO())
_WHDR_FLAGS_ = DWORD

class WAVEHDR(MemStruct):
    fields = [
        ("lpData", LPVOID()),
        ("dwBufferLength", DWORD()),
        ("dwBytesRecorded", DWORD()),
        ("dwUser", DWORD_PTR()),
        ("dwFlags", _WHDR_FLAGS_()),
        ("dwLoops", DWORD()),
        ("lpNext", LPVOID()),
        ("reserved", DWORD_PTR()),
    ]

LPWAVEHDR = Ptr("<I", WAVEHDR())

class WAVEINCAPS(MemStruct):
    fields = [
        ("wMid", WORD()),
        ("wPid", WORD()),
        ("vDriverVersion", MMVERSION()),
        ("szPname", TCHAR__MAXPNAMELEN_()),
        ("dwFormats", _WAVE_FORMAT_()),
        ("wChannels", WORD()),
        ("wReserved1", WORD()),
    ]

LPWAVEINCAPS = Ptr("<I", WAVEINCAPS())
_WAVEOUTCAPS_SUPPORT_ = DWORD

class WAVEOUTCAPS(MemStruct):
    fields = [
        ("wMid", WORD()),
        ("wPid", WORD()),
        ("vDriverVersion", MMVERSION()),
        ("szPname", TCHAR__MAXPNAMELEN_()),
        ("dwFormats", _WAVE_FORMAT_()),
        ("wChannels", WORD()),
        ("wReserved1", WORD()),
        ("dwSupport", _WAVEOUTCAPS_SUPPORT_()),
    ]

LPWAVEOUTCAPS = Ptr("<I", WAVEOUTCAPS())
_JoyButton_ = UINT

class JOYINFO(MemStruct):
    fields = [
        ("wXpos", UINT()),
        ("wYpos", UINT()),
        ("wZpos", UINT()),
        ("wButtons", _JoyButton_()),
    ]

LPJOYINFO = Ptr("<I", JOYINFO())
_JoyPov_ = DWORD
_JoyButtonAll_ = DWORD
_JOYINFOEX_Flags_ = DWORD

class JOYINFOEX(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("dwFlags", _JOYINFOEX_Flags_()),
        ("dwXpos", DWORD()),
        ("dwYpos", DWORD()),
        ("dwZpos", DWORD()),
        ("dwRpos", DWORD()),
        ("dwUpos", DWORD()),
        ("dwVpos", DWORD()),
        ("dwButtons", _JoyButtonAll_()),
        ("dwButtonNumber", DWORD()),
        ("dwPOV", _JoyPov_()),
        ("dwReserved1", DWORD()),
        ("dwReserved2", DWORD()),
    ]

LPJOYINFOEX = Ptr("<I", JOYINFOEX())
_MMCKINFO_Flags_ = DWORD

class MMCKINFO(MemStruct):
    fields = [
        ("ckid", FOURCC()),
        ("cksize", DWORD()),
        ("fccType", FOURCC()),
        ("dwDataOffset", DWORD()),
        ("dwFlags", _MMCKINFO_Flags_()),
    ]

LPMMCKINFO = Ptr("<I", MMCKINFO())

class TIMECAPS(MemStruct):
    fields = [
        ("wPeriodMin", UINT()),
        ("wPeriodMax", UINT()),
    ]

LPTIMECAPS = Ptr("<I", TIMECAPS())
MCIERROR = DWORD
_waveInOutOpenFlags_ = DWORD
_midiInOutOpenFlags_ = DWORD
_mmioInstallIOProcFlags_ = DWORD
_mmioCloseFlags_ = UINT
_mmioFlushFlags_ = UINT
_mmioStringToFOURCCFlags_ = UINT
_mmioDescendFlags_ = UINT
_mmioCreateChunkFlags_ = UINT
_mmioSeekOffset_ = int

class _MMTIME_u_s1_(MemStruct):
    fields = [
        ("hour", BYTE()),
        ("min", BYTE()),
        ("sec", BYTE()),
        ("frame", BYTE()),
        ("fps", BYTE()),
        ("dummy", BYTE()),
        ("pad", BYTE__2_()),
    ]


class _MMTIME_u_s2_(MemStruct):
    fields = [
        ("songptrpos", DWORD()),
    ]

_MMTIME_u_ = Union([
    ("ms", DWORD),
    ("sample", DWORD),
    ("cb", DWORD),
    ("ticks", DWORD),
    ("smpte", _MMTIME_u_s1_),
    ("midi", _MMTIME_u_s2_),
])
_MMTIME_TYPE_ = UINT

class MMTIME(MemStruct):
    fields = [
        ("wType", _MMTIME_TYPE_()),
        ("u", _MMTIME_u_()),
    ]

LPMMTIME = Ptr("<I", MMTIME())
_SND_FLAGS_ = DWORD
_DCB_FLAGS_ = DWORD

###################

###### Functions ######

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
