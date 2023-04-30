###### Enums ######
_HFILE = {
    "_CRTDBG_INVALID_HFILE": -1,
    "_CRTDBG_HFILE_ERROR": -2,
    "_CRTDBG_FILE_STDOUT": -4,
    "_CRTDBG_FILE_STDERR": -5,
    "_CRTDBG_REPORT_FILE": -6,
}
_HFILE_INV = {
    -1: "_CRTDBG_INVALID_HFILE",
    -2: "_CRTDBG_HFILE_ERROR",
    -4: "_CRTDBG_FILE_STDOUT",
    -5: "_CRTDBG_FILE_STDERR",
    -6: "_CRTDBG_REPORT_FILE",
}
errno_t = {
    "EPERM": 1,
    "ENOENT": 2,
    "ESRCH": 3,
    "EINTR": 4,
    "EIO": 5,
    "ENXIO": 6,
    "E2BIG": 7,
    "ENOEXEC": 8,
    "EBADF": 9,
    "ECHILD": 10,
    "EAGAIN": 11,
    "ENOMEM": 12,
    "EACCES": 13,
    "EFAULT": 14,
    "EBUSY": 16,
    "EEXIST": 17,
    "EXDEV": 18,
    "ENODEV": 19,
    "ENOTDIR": 20,
    "EISDIR": 21,
    "EINVAL": 22,
    "ENFILE": 23,
    "EMFILE": 24,
    "ENOTTY": 25,
    "EFBIG": 27,
    "ENOSPC": 28,
    "ESPIPE": 29,
    "EROFS": 30,
    "EMLINK": 31,
    "EPIPE": 32,
    "EDOM": 33,
    "ERANGE": 34,
    "EDEADLK": 36,
    "ENAMETOOLONG": 38,
    "ENOLCK": 39,
    "ENOSYS": 40,
    "ENOTEMPTY": 41,
    "EILSEQ": 42,
    "STRUNCATE": 80,
    "EADDRINUSE": 100,
    "EADDRNOTAVAIL": 101,
    "EAFNOSUPPORT": 102,
    "EALREADY": 103,
    "EBADMSG": 104,
    "ECANCELED": 105,
    "ECONNABORTED": 106,
    "ECONNREFUSED": 107,
    "ECONNRESET": 108,
    "EDESTADDRREQ": 109,
    "EHOSTUNREACH": 110,
    "EIDRM": 111,
    "EINPROGRESS": 112,
    "EISCONN": 113,
    "ELOOP": 114,
    "EMSGSIZE": 115,
    "ENETDOWN": 116,
    "ENETRESET": 117,
    "ENETUNREACH": 118,
    "ENOBUFS": 119,
    "ENODATA": 120,
    "ENOLINK": 121,
    "ENOMSG": 122,
    "ENOPROTOOPT": 123,
    "ENOSR": 124,
    "ENOSTR": 125,
    "ENOTCONN": 126,
    "ENOTRECOVERABLE": 127,
    "ENOTSOCK": 128,
    "ENOTSUP": 129,
    "EOPNOTSUPP": 130,
    "EOTHER": 131,
    "EOVERFLOW": 132,
    "EOWNERDEAD": 133,
    "EPROTO": 134,
    "EPROTONOSUPPORT": 135,
    "EPROTOTYPE": 136,
    "ETIME": 137,
    "ETIMEDOUT": 138,
    "ETXTBSY": 139,
    "EWOULDBLOCK": 140,
}
errno_t_INV = {
    1: "EPERM",
    2: "ENOENT",
    3: "ESRCH",
    4: "EINTR",
    5: "EIO",
    6: "ENXIO",
    7: "E2BIG",
    8: "ENOEXEC",
    9: "EBADF",
    10: "ECHILD",
    11: "EAGAIN",
    12: "ENOMEM",
    13: "EACCES",
    14: "EFAULT",
    16: "EBUSY",
    17: "EEXIST",
    18: "EXDEV",
    19: "ENODEV",
    20: "ENOTDIR",
    21: "EISDIR",
    22: "EINVAL",
    23: "ENFILE",
    24: "EMFILE",
    25: "ENOTTY",
    27: "EFBIG",
    28: "ENOSPC",
    29: "ESPIPE",
    30: "EROFS",
    31: "EMLINK",
    32: "EPIPE",
    33: "EDOM",
    34: "ERANGE",
    36: "EDEADLK",
    38: "ENAMETOOLONG",
    39: "ENOLCK",
    40: "ENOSYS",
    41: "ENOTEMPTY",
    42: "EILSEQ",
    80: "STRUNCATE",
    100: "EADDRINUSE",
    101: "EADDRNOTAVAIL",
    102: "EAFNOSUPPORT",
    103: "EALREADY",
    104: "EBADMSG",
    105: "ECANCELED",
    106: "ECONNABORTED",
    107: "ECONNREFUSED",
    108: "ECONNRESET",
    109: "EDESTADDRREQ",
    110: "EHOSTUNREACH",
    111: "EIDRM",
    112: "EINPROGRESS",
    113: "EISCONN",
    114: "ELOOP",
    115: "EMSGSIZE",
    116: "ENETDOWN",
    117: "ENETRESET",
    118: "ENETUNREACH",
    119: "ENOBUFS",
    120: "ENODATA",
    121: "ENOLINK",
    122: "ENOMSG",
    123: "ENOPROTOOPT",
    124: "ENOSR",
    125: "ENOSTR",
    126: "ENOTCONN",
    127: "ENOTRECOVERABLE",
    128: "ENOTSOCK",
    129: "ENOTSUP",
    130: "EOPNOTSUPP",
    131: "EOTHER",
    132: "EOVERFLOW",
    133: "EOWNERDEAD",
    134: "EPROTO",
    135: "EPROTONOSUPPORT",
    136: "EPROTOTYPE",
    137: "ETIME",
    138: "ETIMEDOUT",
    139: "ETXTBSY",
    140: "EWOULDBLOCK",
}
EXCEPTION_DISPOSITION = {
    "ExceptionContinueExecution": 0,
    "ExceptionContinueSearch": 1,
    "ExceptionNestedException": 2,
    "ExceptionCollidedUnwind": 3,
}
EXCEPTION_DISPOSITION_INV = {
    0: "ExceptionContinueExecution",
    1: "ExceptionContinueSearch",
    2: "ExceptionNestedException",
    3: "ExceptionCollidedUnwind",
}
_SIGNAL_ = {
    "SIGINT": 2,
    "SIGILL": 4,
    "SIGABRT_COMPAT": 6,
    "SIGFPE": 8,
    "SIGSEGV": 11,
    "SIGTERM": 15,
    "SIGBREAK": 21,
    "SIGABRT": 22,
}
_SIGNAL__INV = {
    2: "SIGINT",
    4: "SIGILL",
    6: "SIGABRT_COMPAT",
    8: "SIGFPE",
    11: "SIGSEGV",
    15: "SIGTERM",
    21: "SIGBREAK",
    22: "SIGABRT",
}
_SIGNAL_FUNC_ = {
    "SIG_DFL": 0,
    "SIG_IGN": 1,
    "SIG_GET": 2,
    "SIG_SGE": 3,
    "SIG_ACK": 4,
    "SIG_DIE": 5,
    "SIG_ERR": -1,
}
_SIGNAL_FUNC__INV = {
    0: "SIG_DFL",
    1: "SIG_IGN",
    2: "SIG_GET",
    3: "SIG_SGE",
    4: "SIG_ACK",
    5: "SIG_DIE",
    -1: "SIG_ERR",
}
_C_APP_TYPE_ = {
    "_UNKNOWN_APP": 0,
    "_CONSOLE_APP": 1,
    "_GUI_APP": 2,
}
_C_APP_TYPE__INV = {
    0: "_UNKNOWN_APP",
    1: "_CONSOLE_APP",
    2: "_GUI_APP",
}
_HEAP_RESULT_ = {
    "_HEAPEMPTY": -1,
    "_HEAPOK": -2,
    "_HEAPBADBEGIN": -3,
    "_HEAPBADNODE": -4,
    "_HEAPEND": -5,
    "_HEAPBADPTR": -6,
}
_HEAP_RESULT__INV = {
    -1: "_HEAPEMPTY",
    -2: "_HEAPOK",
    -3: "_HEAPBADBEGIN",
    -4: "_HEAPBADNODE",
    -5: "_HEAPEND",
    -6: "_HEAPBADPTR",
}
_HEAP_USE_FLAG_ = {
    "_FREEENTRY": 0,
    "_USEDENTRY": 1,
}
_HEAP_USE_FLAG__INV = {
    0: "_FREEENTRY",
    1: "_USEDENTRY",
}
_exception_type_ = {
    "_DOMAIN": 1,
    "_SING": 2,
    "_OVERFLOW": 3,
    "_UNDERFLOW": 4,
    "_TLOSS": 5,
    "_PLOSS": 6,
}
_exception_type__INV = {
    1: "_DOMAIN",
    2: "_SING",
    3: "_OVERFLOW",
    4: "_UNDERFLOW",
    5: "_TLOSS",
    6: "_PLOSS",
}
_lconv_val_ = {
    "CHAR_MAX": 127,
}
_lconv_val__INV = {
    127: "CHAR_MAX",
}
_LOCK_NUM_ = {
    "_SIGNAL_LOCK": 0,
    "_IOB_SCAN_LOCK": 1,
    "_TMPNAM_LOCK": 2,
    "_CONIO_LOCK": 3,
    "_HEAP_LOCK": 4,
    "_UNDNAME_LOCK": 5,
    "_TIME_LOCK": 6,
    "_ENV_LOCK": 7,
    "_EXIT_LOCK1": 8,
    "_POPEN_LOCK": 9,
    "_LOCKTAB_LOCK": 10,
    "_OSFHND_LOCK": 11,
    "_SETLOCALE_LOCK": 12,
    "_MB_CP_LOCK": 13,
    "_TYPEINFO_LOCK": 14,
    "_DEBUG_LOCK": 15,
    "_STREAM_LOCKS": 16,
}
_LOCK_NUM__INV = {
    0: "_SIGNAL_LOCK",
    1: "_IOB_SCAN_LOCK",
    2: "_TMPNAM_LOCK",
    3: "_CONIO_LOCK",
    4: "_HEAP_LOCK",
    5: "_UNDNAME_LOCK",
    6: "_TIME_LOCK",
    7: "_ENV_LOCK",
    8: "_EXIT_LOCK1",
    9: "_POPEN_LOCK",
    10: "_LOCKTAB_LOCK",
    11: "_OSFHND_LOCK",
    12: "_SETLOCALE_LOCK",
    13: "_MB_CP_LOCK",
    14: "_TYPEINFO_LOCK",
    15: "_DEBUG_LOCK",
    16: "_STREAM_LOCKS",
}
_output_format_ = {
    "_TWO_DIGIT_EXPONENT": 0x1,
}
_output_format__INV = {
    0x1: "_TWO_DIGIT_EXPONENT",
}
_byte_type_ = {
    "_MBC_SINGLE": 0,
    "_MBC_LEAD": 1,
    "_MBC_TRAIL": 2,
    "_MBC_ILLEGAL": -1,
}
_byte_type__INV = {
    0: "_MBC_SINGLE",
    1: "_MBC_LEAD",
    2: "_MBC_TRAIL",
    -1: "_MBC_ILLEGAL",
}
_CRT_REPORT_TYPE_ = {
    "_CRT_WARN": 0,
    "_CRT_ERROR": 1,
    "_CRT_ASSERT": 2,
    "_CRT_ERRCNT": 3,
}
_CRT_REPORT_TYPE__INV = {
    0: "_CRT_WARN",
    1: "_CRT_ERROR",
    2: "_CRT_ASSERT",
    3: "_CRT_ERRCNT",
}
_CRT_RPTHOOK_MODE_ = {
    "_CRT_RPTHOOK_INSTALL": 0,
    "_CRT_RPTHOOK_REMOVE": 1,
}
_CRT_RPTHOOK_MODE__INV = {
    0: "_CRT_RPTHOOK_INSTALL",
    1: "_CRT_RPTHOOK_REMOVE",
}
_DBG_BLOCK_TYPE_ = {
    "_FREE_BLOCK": 0,
    "_NORMAL_BLOCK": 1,
    "_CRT_BLOCK": 2,
    "_IGNORE_BLOCK": 3,
    "_CLIENT_BLOCK": 4,
    "_MAX_BLOCKS": 5,
}
_DBG_BLOCK_TYPE__INV = {
    0: "_FREE_BLOCK",
    1: "_NORMAL_BLOCK",
    2: "_CRT_BLOCK",
    3: "_IGNORE_BLOCK",
    4: "_CLIENT_BLOCK",
    5: "_MAX_BLOCKS",
}
_set_error_mode_ = {
    "_OUT_TO_DEFAULT": 0,
    "_OUT_TO_STDERR": 1,
    "_OUT_TO_MSGBOX": 2,
    "_REPORT_ERRMODE": 3,
}
_set_error_mode__INV = {
    0: "_OUT_TO_DEFAULT",
    1: "_OUT_TO_STDERR",
    2: "_OUT_TO_MSGBOX",
    3: "_REPORT_ERRMODE",
}
_disposition_type_ = {
    "DISPOSITION_DISMISS": 0,
    "DISPOSITION_CONTINUE_SEARCH": 1,
    "DISPOSITION_NESTED_EXCEPTION": 2,
    "DISPOSITION_COLLIDED_UNWIND": 3,
}
_disposition_type__INV = {
    0: "DISPOSITION_DISMISS",
    1: "DISPOSITION_CONTINUE_SEARCH",
    2: "DISPOSITION_NESTED_EXCEPTION",
    3: "DISPOSITION_COLLIDED_UNWIND",
}
_xcpt_num_ = {
    "STATUS_ACCESS_VIOLATION": 0xC0000005,
    "STATUS_ILLEGAL_INSTRUCTION": 0xC000001D,
    "STATUS_PRIVILEGED_INSTRUCTION": 0xC0000096,
    "STATUS_FLOAT_DENORMAL_OPERAND": 0xC000008D,
    "STATUS_FLOAT_DIVIDE_BY_ZERO": 0xC000008E,
    "STATUS_FLOAT_INEXACT_RESULT": 0xC000008F,
    "STATUS_FLOAT_INVALID_OPERATION": 0xC0000090,
    "STATUS_FLOAT_OVERFLOW": 0xC0000091,
    "STATUS_FLOAT_STACK_CHECK": 0xC0000092,
    "STATUS_FLOAT_UNDERFLOW": 0xC0000093,
}
_xcpt_num__INV = {
    0xC0000005: "STATUS_ACCESS_VIOLATION",
    0xC000001D: "STATUS_ILLEGAL_INSTRUCTION",
    0xC0000096: "STATUS_PRIVILEGED_INSTRUCTION",
    0xC000008D: "STATUS_FLOAT_DENORMAL_OPERAND",
    0xC000008E: "STATUS_FLOAT_DIVIDE_BY_ZERO",
    0xC000008F: "STATUS_FLOAT_INEXACT_RESULT",
    0xC0000090: "STATUS_FLOAT_INVALID_OPERATION",
    0xC0000091: "STATUS_FLOAT_OVERFLOW",
    0xC0000092: "STATUS_FLOAT_STACK_CHECK",
    0xC0000093: "STATUS_FLOAT_UNDERFLOW",
}
_xcpt_action_ = {
    "EXCEPTION_EXECUTE_HANDLER": 1,
    "EXCEPTION_CONTINUE_SEARCH": 0,
    "EXCEPTION_CONTINUE_EXECUTION": -1,
}
_xcpt_action__INV = {
    1: "EXCEPTION_EXECUTE_HANDLER",
    0: "EXCEPTION_CONTINUE_SEARCH",
    -1: "EXCEPTION_CONTINUE_EXECUTION",
}
__LK_MODE_ = {
    "_LK_UNLCK": 0,
    "_LK_LOCK": 1,
    "_LK_NBLCK": 2,
    "_LK_RLCK": 3,
    "_LK_NBRLCK": 4,
}
__LK_MODE__INV = {
    0: "_LK_UNLCK",
    1: "_LK_LOCK",
    2: "_LK_NBLCK",
    3: "_LK_RLCK",
    4: "_LK_NBRLCK",
}
_control_mask_ = {
    "_MCW_DN": 0x03000000,
    "_MCW_EM": 0x0008001f,
    "_MCW_RC": 0x00000300,
    "_MCW_IC": 0x00040000,
    "_MCW_PC": 0x00030000,
}
_control_mask__INV = {
    0x03000000: "_MCW_DN",
    0x0008001f: "_MCW_EM",
    0x00000300: "_MCW_RC",
    0x00040000: "_MCW_IC",
    0x00030000: "_MCW_PC",
}
_file_translation_mode_ = {
    "_O_TEXT": 0x4000,
    "_O_BINARY": 0x8000,
    "_O_WTEXT": 0x10000,
    "_O_U16TEXT": 0x20000,
    "_O_U8TEXT": 0x40000,
}
_file_translation_mode__INV = {
    0x4000: "_O_TEXT",
    0x8000: "_O_BINARY",
    0x10000: "_O_WTEXT",
    0x20000: "_O_U16TEXT",
    0x40000: "_O_U8TEXT",
}
_RET_EOF_ = {
    "EOF": -1,
}
_RET_EOF__INV = {
    -1: "EOF",
}
_RET_WEOF_ = {
    "WEOF": -1,
}
_RET_WEOF__INV = {
    -1: "WEOF",
}
_RET_WEOF_INT_ = {
    "WEOF": -1,
}
_RET_WEOF_INT__INV = {
    -1: "WEOF",
}
_buffer_mode_ = {
    "_IOFBF": 0x0000,
    "_IOLBF": 0x0040,
    "_IONBF": 0x0004,
}
_buffer_mode__INV = {
    0x0000: "_IOFBF",
    0x0040: "_IOLBF",
    0x0004: "_IONBF",
}
_locale_category_ = {
    "LC_ALL": 0,
    "LC_COLLATE": 1,
    "LC_CTYPE": 2,
    "LC_MONETARY": 3,
    "LC_NUMERIC": 4,
    "LC_TIME": 5,
}
_locale_category__INV = {
    0: "LC_ALL",
    1: "LC_COLLATE",
    2: "LC_CTYPE",
    3: "LC_MONETARY",
    4: "LC_NUMERIC",
    5: "LC_TIME",
}
_thread_locale_type_ = {
    "_ENABLE_PER_THREAD_LOCALE": 0x1,
    "_DISABLE_PER_THREAD_LOCALE": 0x2,
}
_thread_locale_type__INV = {
    0x1: "_ENABLE_PER_THREAD_LOCALE",
    0x2: "_DISABLE_PER_THREAD_LOCALE",
}
__MB_CP_TYPE_ = {
    "_MB_CP_SBCS": 0,
    "_MB_CP_OEM": -2,
    "_MB_CP_ANSI": -3,
    "_MB_CP_LOCALE": -4,
}
__MB_CP_TYPE__INV = {
    0: "_MB_CP_SBCS",
    -2: "_MB_CP_OEM",
    -3: "_MB_CP_ANSI",
    -4: "_MB_CP_LOCALE",
}
_thread_initflag_ = {
    "CREATE_SUSPENDED": 0x00000004,
}
_thread_initflag__INV = {
    0x00000004: "CREATE_SUSPENDED",
}
_spawn_mode_ = {
    "_P_WAIT": 0,
    "_P_NOWAIT": 1,
    "_P_OVERLAY": 2,
    "_P_NOWAITO": 3,
    "_P_DETACH": 4,
}
_spawn_mode__INV = {
    0: "_P_WAIT",
    1: "_P_NOWAIT",
    2: "_P_OVERLAY",
    3: "_P_NOWAITO",
    4: "_P_DETACH",
}
__NLSCMPERROR_ = {
    "_NLSCMPERROR": 0x7FFFFFFF,
}
__NLSCMPERROR__INV = {
    0x7FFFFFFF: "_NLSCMPERROR",
}
_size_t_INT_MAX_ = {
    "INT_MAX": 0x7FFFFFFF,
}
_size_t_INT_MAX__INV = {
    0x7FFFFFFF: "INT_MAX",
}

###################

###### Types ######
_locale_t = LPVOID
_CrtMemState_PTR = LPVOID
const__CrtMemState_PTR = LPVOID
struct__stati64_PTR = LPVOID
struct__finddata_t_PTR = LPVOID
struct__finddatai64_t_PTR = LPVOID
struct__wfinddata_t_PTR = LPVOID
struct__wfinddatai64_t_PTR = LPVOID
unsigned = unsigned_int
unsigned_PTR = Ptr("<I", unsigned())
long_int = long
FILE_PTR = LPVOID
FILE_PTR_PTR = Ptr("<I", FILE_PTR())
const_unsigned_char_PTR = Ptr("<I", unsigned_char())
wint_t = unsigned_short
_CRT_ALLOC_HOOK = LPVOID
_CRT_DUMP_CLIENT = LPVOID
_CRT_REPORT_HOOK = LPVOID
_CRT_REPORT_HOOKW = LPVOID
_se_translator_function = LPVOID
terminate_function = LPVOID
unexpected_function = LPVOID
intptr_t = INT_PTR
__time32_t = long
__time32_t_PTR = Ptr("<I", __time32_t())
const___time32_t_PTR = Ptr("<I", __time32_t())
__time64_t = __int64
__time64_t_PTR = Ptr("<I", __time64_t())
const___time64_t_PTR = Ptr("<I", __time64_t())
wchar = WCHAR
const_wchar_PTR = Ptr("<I", wchar())
_PNH = LPVOID
uintptr_t = UINT_PTR
_onexit_t = LPVOID
clock_t = long
char_PTR_PTR_PTR = Ptr("<I", char_PTR_PTR())
wchar_t_PTR_PTR_PTR = Ptr("<I", wchar_t_PTR_PTR())
_PVFV = LPVOID
_PVFV_PTR = Ptr("<I", _PVFV())
_PVFV_PTR_PTR = Ptr("<I", _PVFV_PTR())
mbstate_t = int
mbstate_t_PTR = Ptr("<I", mbstate_t())
const_unsigned_short_PTR = Ptr("<I", unsigned_short())
_HANDLE_MATH_ERROR = LPVOID
_invalid_parameter_handler = LPVOID
PEXCEPTION_REGISTRATION = LPVOID
EHExceptionRecord_PTR = LPVOID
EHRegistrationNode_PTR = LPVOID
DispatcherContext_PTR = LPVOID
_dev_t = unsigned_int
_ino_t = unsigned_short
_off_t = long
_fsize_t = unsigned_long
fpos_t = __int64
fpos_t_PTR = Ptr("<I", fpos_t())
const_fpos_t_PTR = Ptr("<I", fpos_t())
_purecall_handler = LPVOID
struct__EXCEPTION_POINTERS_PTR = Ptr("<I", EXCEPTION_POINTERS())
wchar_t__260_ = Array(wchar_t, 260)
unsigned_char_10_ = Array(unsigned_char, 10)
_HFILE = void_PTR
errno_t = int

class struct__diskfree_t(MemStruct):
    fields = [
        ("total_clusters", unsigned()),
        ("avail_clusters", unsigned()),
        ("sectors_per_cluster", unsigned()),
        ("bytes_per_sector", unsigned()),
    ]

struct__diskfree_t_PTR = Ptr("<I", struct__diskfree_t())

class _startupinfo(MemStruct):
    fields = [
        ("newmode", int()),
    ]

_startupinfo_PTR = Ptr("<I", _startupinfo())
EXCEPTION_DISPOSITION = UINT
_SIGNAL_ = int
_SIGNAL_FUNC_ = LPVOID
_C_APP_TYPE_ = int
_ST_MODE_ = unsigned_short

class struct__stat(MemStruct):
    fields = [
        ("st_dev", _dev_t()),
        ("st_ino", _ino_t()),
        ("st_mode", _ST_MODE_()),
        ("st_nlink", short()),
        ("st_uid", short()),
        ("st_gid", short()),
        ("st_rdev", _dev_t()),
        ("st_size", _off_t()),
        ("st_atime", time_t()),
        ("st_mtime", time_t()),
        ("st_ctime", time_t()),
    ]

struct__stat_PTR = Ptr("<I", struct__stat())

class struct__stat32(MemStruct):
    fields = [
        ("st_dev", _dev_t()),
        ("st_ino", _ino_t()),
        ("st_mode", _ST_MODE_()),
        ("st_nlink", short()),
        ("st_uid", short()),
        ("st_gid", short()),
        ("st_rdev", _dev_t()),
        ("st_size", _off_t()),
        ("st_atime", __time32_t()),
        ("st_mtime", __time32_t()),
        ("st_ctime", __time32_t()),
    ]

struct__stat32_PTR = Ptr("<I", struct__stat32())

class struct__stat64(MemStruct):
    fields = [
        ("st_dev", _dev_t()),
        ("st_ino", _ino_t()),
        ("st_mode", _ST_MODE_()),
        ("st_nlink", short()),
        ("st_uid", short()),
        ("st_gid", short()),
        ("st_rdev", _dev_t()),
        ("st_size", __int64()),
        ("st_atime", __time64_t()),
        ("st_mtime", __time64_t()),
        ("st_ctime", __time64_t()),
    ]

struct__stat64_PTR = Ptr("<I", struct__stat64())

class struct__stat32i64(MemStruct):
    fields = [
        ("st_dev", _dev_t()),
        ("st_ino", _ino_t()),
        ("st_mode", _ST_MODE_()),
        ("st_nlink", short()),
        ("st_uid", short()),
        ("st_gid", short()),
        ("st_rdev", _dev_t()),
        ("st_size", __int64()),
        ("st_atime", __time32_t()),
        ("st_mtime", __time32_t()),
        ("st_ctime", __time32_t()),
    ]

struct__stat32i64_PTR = Ptr("<I", struct__stat32i64())

class struct__stat64i32(MemStruct):
    fields = [
        ("st_dev", _dev_t()),
        ("st_ino", _ino_t()),
        ("st_mode", _ST_MODE_()),
        ("st_nlink", short()),
        ("st_uid", short()),
        ("st_gid", short()),
        ("st_rdev", _dev_t()),
        ("st_size", _off_t()),
        ("st_atime", __time64_t()),
        ("st_mtime", __time64_t()),
        ("st_ctime", __time64_t()),
    ]

struct__stat64i32_PTR = Ptr("<I", struct__stat64i32())

class struct__complex(MemStruct):
    fields = [
        ("x", double()),
        ("y", double()),
    ]


class _CRT_DOUBLE(MemStruct):
    fields = [
        ("x", double()),
    ]

_CRT_DOUBLE_PTR = Ptr("<I", _CRT_DOUBLE())

class _CRT_FLOAT(MemStruct):
    fields = [
        ("f", float()),
    ]

_CRT_FLOAT_PTR = Ptr("<I", _CRT_FLOAT())

class struct_tm(MemStruct):
    fields = [
        ("tm_sec", int()),
        ("tm_min", int()),
        ("tm_hour", int()),
        ("tm_mday", int()),
        ("tm_mon", int()),
        ("tm_year", int()),
        ("tm_wday", int()),
        ("tm_yday", int()),
        ("tm_isdst", int()),
    ]

struct_tm_PTR = Ptr("<I", struct_tm())
const_struct_tm_PTR = Ptr("<I", struct_tm())
_HEAP_RESULT_ = int
_HEAP_USE_FLAG_ = int

class _HEAPINFO(MemStruct):
    fields = [
        ("_pentry", int_PTR()),
        ("_size", size_t()),
        ("_useflag", _HEAP_USE_FLAG_()),
    ]

_HEAPINFO_PTR = Ptr("<I", _HEAPINFO())

class struct__timeb(MemStruct):
    fields = [
        ("time", time_t()),
        ("millitm", unsigned_short()),
        ("timezone", short()),
        ("dstflag", short()),
    ]

struct__timeb_PTR = Ptr("<I", struct__timeb())

class struct___timeb32(MemStruct):
    fields = [
        ("time", __time32_t()),
        ("millitm", unsigned_short()),
        ("timezone", short()),
        ("dstflag", short()),
    ]

struct___timeb32_PTR = Ptr("<I", struct___timeb32())

class struct___timeb64(MemStruct):
    fields = [
        ("time", __time64_t()),
        ("millitm", unsigned_short()),
        ("timezone", short()),
        ("dstflag", short()),
    ]

struct___timeb64_PTR = Ptr("<I", struct___timeb64())

class struct__utimbuf(MemStruct):
    fields = [
        ("actime", time_t()),
        ("modtime", time_t()),
    ]

struct__utimbuf_PTR = Ptr("<I", struct__utimbuf())

class struct___utimbuf32(MemStruct):
    fields = [
        ("actime", __time32_t()),
        ("modtime", __time32_t()),
    ]

struct___utimbuf32_PTR = Ptr("<I", struct___utimbuf32())

class struct___utimbuf64(MemStruct):
    fields = [
        ("actime", __time64_t()),
        ("modtime", __time64_t()),
    ]

struct___utimbuf64_PTR = Ptr("<I", struct___utimbuf64())
_FINDDATA_ATTRIB_ = unsigned

class struct__finddata32_t(MemStruct):
    fields = [
        ("attrib", _FINDDATA_ATTRIB_()),
        ("time_create", __time32_t()),
        ("time_access", __time32_t()),
        ("time_write", __time32_t()),
        ("size", _fsize_t()),
        ("name", char__260_()),
    ]

struct__finddata32_t_PTR = Ptr("<I", struct__finddata32_t())

class struct__finddata32i64_t(MemStruct):
    fields = [
        ("attrib", _FINDDATA_ATTRIB_()),
        ("time_create", __time32_t()),
        ("time_access", __time32_t()),
        ("time_write", __time32_t()),
        ("size", __int64()),
        ("name", char__260_()),
    ]

struct__finddata32i64_t_PTR = Ptr("<I", struct__finddata32i64_t())

class struct__finddata64i32_t(MemStruct):
    fields = [
        ("attrib", _FINDDATA_ATTRIB_()),
        ("time_create", __time64_t()),
        ("time_access", __time64_t()),
        ("time_write", __time64_t()),
        ("size", _fsize_t()),
        ("name", char__260_()),
    ]

struct__finddata64i32_t_PTR = Ptr("<I", struct__finddata64i32_t())

class struct___finddata64_t(MemStruct):
    fields = [
        ("attrib", _FINDDATA_ATTRIB_()),
        ("time_create", __time64_t()),
        ("time_access", __time64_t()),
        ("time_write", __time64_t()),
        ("size", __int64()),
        ("name", char__260_()),
    ]

struct___finddata64_t_PTR = Ptr("<I", struct___finddata64_t())

class struct__wfinddata32_t(MemStruct):
    fields = [
        ("attrib", _FINDDATA_ATTRIB_()),
        ("time_create", __time32_t()),
        ("time_access", __time32_t()),
        ("time_write", __time32_t()),
        ("size", _fsize_t()),
        ("name", wchar_t__260_()),
    ]

struct__wfinddata32_t_PTR = Ptr("<I", struct__wfinddata32_t())

class struct__wfinddata32i64_t(MemStruct):
    fields = [
        ("attrib", _FINDDATA_ATTRIB_()),
        ("time_create", __time32_t()),
        ("time_access", __time32_t()),
        ("time_write", __time32_t()),
        ("size", __int64()),
        ("name", wchar_t__260_()),
    ]

struct__wfinddata32i64_t_PTR = Ptr("<I", struct__wfinddata32i64_t())

class struct__wfinddata64i32_t(MemStruct):
    fields = [
        ("attrib", _FINDDATA_ATTRIB_()),
        ("time_create", __time64_t()),
        ("time_access", __time64_t()),
        ("time_write", __time64_t()),
        ("size", _fsize_t()),
        ("name", wchar_t__260_()),
    ]

struct__wfinddata64i32_t_PTR = Ptr("<I", struct__wfinddata64i32_t())

class struct__wfinddata64_t(MemStruct):
    fields = [
        ("attrib", _FINDDATA_ATTRIB_()),
        ("time_create", __time64_t()),
        ("time_access", __time64_t()),
        ("time_write", __time64_t()),
        ("size", __int64()),
        ("name", wchar_t__260_()),
    ]

struct__wfinddata64_t_PTR = Ptr("<I", struct__wfinddata64_t())
wctype_t = unsigned_short
_ctype_t = wctype_t
_exception_type_ = int

class struct__exception(MemStruct):
    fields = [
        ("type", _exception_type_()),
        ("name", char_PTR()),
        ("arg1", double()),
        ("arg2", double()),
        ("retval", double()),
    ]

struct__exception_PTR = Ptr("<I", struct__exception())

class div_t(MemStruct):
    fields = [
        ("quot", int()),
        ("rem", int()),
    ]


class ldiv_t(MemStruct):
    fields = [
        ("quot", long()),
        ("rem", long()),
    ]


class _LDOUBLE(MemStruct):
    fields = [
        ("ld", unsigned_char_10_()),
    ]

_LDOUBLE_PTR = Ptr("<I", _LDOUBLE())
_lconv_val_ = UINT8

class struct_lconv(MemStruct):
    fields = [
        ("decimal_point", char_PTR()),
        ("thousands_sep", char_PTR()),
        ("grouping", char_PTR()),
        ("int_curr_symbol", char_PTR()),
        ("currency_symbol", char_PTR()),
        ("mon_decimal_point", char_PTR()),
        ("mon_thousands_sep", char_PTR()),
        ("mon_grouping", char_PTR()),
        ("positive_sign", char_PTR()),
        ("negative_sign", char_PTR()),
        ("int_frac_digits", _lconv_val_()),
        ("frac_digits", _lconv_val_()),
        ("p_cs_precedes", _lconv_val_()),
        ("p_sep_by_space", _lconv_val_()),
        ("n_cs_precedes", _lconv_val_()),
        ("n_sep_by_space", _lconv_val_()),
        ("p_sign_posn", _lconv_val_()),
        ("n_sign_posn", _lconv_val_()),
        ("_W_decimal_point", wchar_t_PTR()),
        ("_W_thousands_sep", wchar_t_PTR()),
        ("_W_int_curr_symbol", wchar_t_PTR()),
        ("_W_currency_symbol", wchar_t_PTR()),
        ("_W_mon_decimal_point", wchar_t_PTR()),
        ("_W_mon_thousands_sep", wchar_t_PTR()),
        ("_W_positive_sign", wchar_t_PTR()),
        ("_W_negative_sign", wchar_t_PTR()),
    ]

struct_lconv_PTR = Ptr("<I", struct_lconv())
_LOCK_NUM_ = int
_output_format_ = unsigned_int
_compare_function_ = LPVOID
_compare_s_function_ = LPVOID
_open_flag_ = unsigned_int
_share_flag_ = unsigned_int
_perm_mode_ = unsigned_int
_perm_mode_PTR_ = Ptr("<I", _perm_mode_())
_byte_type_ = int
_CRT_REPORT_TYPE_ = int
_CRTDBG_FLAG_ = unsigned_int
_CRT_RPTHOOK_MODE_ = int
_CRTDBG_MODE_ = unsigned_int
_DBG_BLOCK_TYPE_ = int
_set_error_mode_ = int
_disposition_type_ = int
_xcpt_num_ = unsigned_long
_xcpt_action_ = int
__LK_MODE_ = int
__SW_FLOAT_ = unsigned_int
_control_bits_ = unsigned_int
_control_mask_ = unsigned_int
__FPCLASS_ = unsigned_int
_file_translation_mode_ = int
_file_translation_mode_PTR_ = Ptr("<I", _file_translation_mode_())
_RET_EOF_ = int
_RET_WEOF_ = wint_t
_RET_WEOF_INT_ = int
_buffer_mode_ = int
_locale_category_ = int
_thread_locale_type_ = int
__MB_CP_TYPE_ = int
_thread_initflag_ = unsigned
_spawn_mode_ = int
__NLSCMPERROR_ = int
_size_t_INT_MAX_ = size_t
_abort_flag_ = unsigned_int

###################

###### Functions ######

def msvcrxx__memccpy(jitter):
    """
    void* _memccpy(
        void* dest,
        const void* src,
        int c,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "src", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memchr(jitter):
    """
    void* memchr(
        const void* buf,
        int c,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buf", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memcmp(jitter):
    """
    int memcmp(
        const void* buf1,
        const void* buf2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buf1", "buf2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memcpy(jitter):
    """
    void* memcpy(
        void* dest,
        const void* src,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memcpy_s(jitter):
    """
    errno_t memcpy_s(
        void* dest,
        size_t numberOfElements,
        const void* src,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "numberOfElements", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wmemcpy_s(jitter):
    """
    errno_t wmemcpy_s(
        wchar_t* dest,
        size_t numberOfElements,
        const wchar_t* src,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "numberOfElements", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__memicmp(jitter):
    """
    int _memicmp(
        const void* buf1,
        const void* buf2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buf1", "buf2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__memicmp_l(jitter):
    """
    int _memicmp_l(
        const void* buf1,
        const void* buf2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buf1", "buf2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memmove(jitter):
    """
    void* memmove(
        void* dest,
        const void* src,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memmove_s(jitter):
    """
    errno_t memmove_s(
        void* dest,
        size_t numberOfElements,
        const void* src,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "numberOfElements", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wmemmove_s(jitter):
    """
    errno_t wmemmove_s(
        wchar_t* dest,
        size_t numberOfElements,
        const wchar_t* src,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "numberOfElements", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memset(jitter):
    """
    void* memset(
        void* dest,
        int c,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swab(jitter):
    """
    void _swab(
        char* src,
        char* dest,
        int n
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["src", "dest", "n"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isleadbyte(jitter):
    """
    int isleadbyte(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isleadbyte_l(jitter):
    """
    int _isleadbyte_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbalnum(jitter):
    """
    int _ismbbalnum(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbalnum_l(jitter):
    """
    int _ismbbalnum_l(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbalpha(jitter):
    """
    int _ismbbalpha(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbalpha_l(jitter):
    """
    int _ismbbalpha_l(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbgraph(jitter):
    """
    int _ismbbgraph(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbgraph_l(jitter):
    """
    int _ismbbgraph_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkalnum(jitter):
    """
    int _ismbbkalnum(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkalnum_l(jitter):
    """
    int _ismbbkalnum_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkana(jitter):
    """
    int _ismbbkana(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkana_l(jitter):
    """
    int _ismbbkana_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkprint(jitter):
    """
    int _ismbbkprint(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkprint_l(jitter):
    """
    int _ismbbkprint_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkpunct(jitter):
    """
    int _ismbbkpunct(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkpunct_l(jitter):
    """
    int _ismbbkpunct_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbblead(jitter):
    """
    int _ismbblead(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbblead_l(jitter):
    """
    int _ismbblead_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbprint(jitter):
    """
    int _ismbbprint(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbprint_l(jitter):
    """
    int _ismbbprint_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbpunct(jitter):
    """
    int _ismbbpunct(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbpunct_l(jitter):
    """
    int _ismbbpunct_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbtrail(jitter):
    """
    int _ismbbtrail(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbtrail_l(jitter):
    """
    int _ismbbtrail_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbslead(jitter):
    """
    int _ismbslead(
        const unsigned char* str,
        const unsigned char* current
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "current"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbstrail(jitter):
    """
    int _ismbstrail(
        const unsigned char* str,
        const unsigned char* current
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "current"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbslead_l(jitter):
    """
    int _ismbslead_l(
        const unsigned char* str,
        const unsigned char* current,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "current", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbstrail_l(jitter):
    """
    int _ismbstrail_l(
        const unsigned char* str,
        const unsigned char* current,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "current", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbbtype(jitter):
    """
    [byte_type] _mbbtype(
        unsigned char c,
        int type
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbbtype_l(jitter):
    """
    [byte_type] _mbbtype_l(
        unsigned char c,
        int type,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "type", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsbtype(jitter):
    """
    [byte_type] _mbsbtype(
        const unsigned char* mbstr,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsbtype_l(jitter):
    """
    [byte_type] _mbsbtype_l(
        const unsigned char* mbstr,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isalnum(jitter):
    """
    int isalnum(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswalnum(jitter):
    """
    int iswalnum(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isalnum_l(jitter):
    """
    int _isalnum_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswalnum_l(jitter):
    """
    int _iswalnum_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcalnum(jitter):
    """
    int _ismbcalnum(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcalnum_l(jitter):
    """
    int _ismbcalnum_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcalpha(jitter):
    """
    int _ismbcalpha(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcalpha_l(jitter):
    """
    int _ismbcalpha_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcdigit(jitter):
    """
    int _ismbcdigit(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcdigit_l(jitter):
    """
    int _ismbcdigit_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isalpha(jitter):
    """
    int isalpha(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswalpha(jitter):
    """
    int iswalpha(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isalpha_l(jitter):
    """
    int _isalpha_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswalpha_l(jitter):
    """
    int _iswalpha_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___isascii(jitter):
    """
    int __isascii(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswascii(jitter):
    """
    int iswascii(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iscntrl(jitter):
    """
    int iscntrl(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswcntrl(jitter):
    """
    int iswcntrl(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iscntrl_l(jitter):
    """
    int _iscntrl_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswcntrl_l(jitter):
    """
    int _iswcntrl_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___iscsym(jitter):
    """
    int __iscsym(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___iswcsym(jitter):
    """
    int __iswcsym(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___iscsymf(jitter):
    """
    int __iscsymf(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___iswcsymf(jitter):
    """
    int __iswcsymf(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswcsym_l(jitter):
    """
    int _iswcsym_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswcsymf_l(jitter):
    """
    int _iswcsymf_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isdigit(jitter):
    """
    int isdigit(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswdigit(jitter):
    """
    int iswdigit(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isdigit_l(jitter):
    """
    int _isdigit_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswdigit_l(jitter):
    """
    int _iswdigit_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isgraph(jitter):
    """
    int isgraph(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswgraph(jitter):
    """
    int iswgraph(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isgraph_l(jitter):
    """
    int _isgraph_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswgraph_l(jitter):
    """
    int _iswgraph_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcgraph(jitter):
    """
    int _ismbcgraph(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcgraph_l(jitter):
    """
    int _ismbcgraph_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcprint(jitter):
    """
    int _ismbcprint(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcprint_l(jitter):
    """
    int _ismbcprint_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcpunct(jitter):
    """
    int _ismbcpunct(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcpunct_l(jitter):
    """
    int _ismbcpunct_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcspace(jitter):
    """
    int _ismbcspace(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcspace_l(jitter):
    """
    int _ismbcspace_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_islower(jitter):
    """
    int islower(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswlower(jitter):
    """
    int iswlower(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__islower_l(jitter):
    """
    int _islower_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswlower_l(jitter):
    """
    int _iswlower_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbclower(jitter):
    """
    int _ismbclower(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbclower_l(jitter):
    """
    int _ismbclower_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcupper(jitter):
    """
    int _ismbcupper(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcupper_l(jitter):
    """
    int _ismbcupper_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbchira(jitter):
    """
    int _ismbchira(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbchira_l(jitter):
    """
    int _ismbchira_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbckata(jitter):
    """
    int _ismbckata(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbckata_l(jitter):
    """
    int _ismbckata_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbclegal(jitter):
    """
    int _ismbclegal(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbclegal_l(jitter):
    """
    int _ismbclegal_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcsymbol(jitter):
    """
    int _ismbcsymbol(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcsymbol_l(jitter):
    """
    int _ismbcsymbol_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcl0(jitter):
    """
    int _ismbcl0(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcl0_l(jitter):
    """
    int _ismbcl0_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcl1(jitter):
    """
    int _ismbcl1(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcl1_l(jitter):
    """
    int _ismbcl1_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcl2(jitter):
    """
    int _ismbcl2(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcl2_l(jitter):
    """
    int _ismbcl2_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isprint(jitter):
    """
    int isprint(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswprint(jitter):
    """
    int iswprint(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isprint_l(jitter):
    """
    int _isprint_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswprint_l(jitter):
    """
    int _iswprint_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ispunct(jitter):
    """
    int ispunct(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswpunct(jitter):
    """
    int iswpunct(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ispunct_l(jitter):
    """
    int _ispunct_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswpunct_l(jitter):
    """
    int _iswpunct_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isspace(jitter):
    """
    int isspace(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswspace(jitter):
    """
    int iswspace(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isspace_l(jitter):
    """
    int _isspace_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswspace_l(jitter):
    """
    int _iswspace_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isupper(jitter):
    """
    int isupper(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isupper_l(jitter):
    """
    int _isupper_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswupper(jitter):
    """
    int iswupper(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswupper_l(jitter):
    """
    int _iswupper_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isctype(jitter):
    """
    int _isctype(
        int c,
        _ctype_t mask
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isctype_l(jitter):
    """
    int _isctype_l(
        int c,
        _ctype_t mask,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "mask", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswctype(jitter):
    """
    int iswctype(
        wint_t c,
        wctype_t mask
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_is_wctype(jitter):
    """
    int is_wctype(
        wint_t c,
        wctype_t mask
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswctype_l(jitter):
    """
    int _iswctype_l(
        wint_t c,
        wctype_t mask,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "mask", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isxdigit(jitter):
    """
    int isxdigit(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswxdigit(jitter):
    """
    int iswxdigit(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isxdigit_l(jitter):
    """
    int _isxdigit_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswxdigit_l(jitter):
    """
    int _iswxdigit_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctype(jitter):
    """
    wctype_t _wctype(
        const char* property
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["property"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___pctype_func(jitter):
    """
    const unsigned short* __pctype_func()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_free(jitter):
    """
    void _aligned_free(
        void* memblock
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_free_dbg(jitter):
    """
    void _aligned_free_dbg(
        void* memblock
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_malloc(jitter):
    """
    void* _aligned_malloc(
        size_t size,
        size_t alignment
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["size", "alignment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_malloc_dbg(jitter):
    """
    void* _aligned_malloc_dbg(
        size_t size,
        size_t alignment,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["size", "alignment", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_msize(jitter):
    """
    size_t _aligned_msize(
        void* memblock,
        size_t alignment,
        size_t offset
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "alignment", "offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_msize_dbg(jitter):
    """
    size_t _aligned_msize_dbg(
        void* memblock,
        size_t alignment,
        size_t offset
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "alignment", "offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_offset_malloc(jitter):
    """
    void* _aligned_offset_malloc(
        size_t size,
        size_t alignment,
        size_t offset
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["size", "alignment", "offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_offset_malloc_dbg(jitter):
    """
    void* _aligned_offset_malloc_dbg(
        size_t size,
        size_t alignment,
        size_t offset,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["size", "alignment", "offset", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_offset_realloc(jitter):
    """
    void* _aligned_offset_realloc(
        void* memblock,
        size_t size,
        size_t alignment,
        size_t offset
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size", "alignment", "offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_offset_realloc_dbg(jitter):
    """
    void* _aligned_offset_realloc_dbg(
        void* memblock,
        size_t size,
        size_t alignment,
        size_t offset,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size", "alignment", "offset", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_offset_recalloc(jitter):
    """
    void* _aligned_offset_recalloc(
        void* memblock,
        size_t num,
        size_t size,
        size_t alignment,
        size_t offset
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "num", "size", "alignment", "offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_offset_recalloc_dbg(jitter):
    """
    void* _aligned_offset_recalloc_dbg(
        void* memblock,
        size_t num,
        size_t size,
        size_t alignment,
        size_t offset,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "num", "size", "alignment", "offset", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_realloc(jitter):
    """
    void* _aligned_realloc(
        void* memblock,
        size_t size,
        size_t alignment
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size", "alignment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_realloc_dbg(jitter):
    """
    void* _aligned_realloc_dbg(
        void* memblock,
        size_t size,
        size_t alignment,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size", "alignment", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_recalloc(jitter):
    """
    void* _aligned_recalloc(
        void* memblock,
        size_t num,
        size_t size,
        size_t alignment
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "num", "size", "alignment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_recalloc_dbg(jitter):
    """
    void* _aligned_recalloc_dbg(
        void* memblock,
        size_t num,
        size_t size,
        size_t alignment,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "num", "size", "alignment", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_abs(jitter):
    """
    int abs(
        int n
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["n"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__abs64(jitter):
    """
    __int64 _abs64(
        __int64 n
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["n"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtof(jitter):
    """
    double _wtof(
        const wchar_t* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtof_l(jitter):
    """
    double _wtof_l(
        const wchar_t* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtoi(jitter):
    """
    int _wtoi(
        const wchar_t* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtoi_l(jitter):
    """
    int _wtoi_l(
        const wchar_t* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtol(jitter):
    """
    long _wtol(
        const wchar_t* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtol_l(jitter):
    """
    long _wtol_l(
        const wchar_t* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__itoa(jitter):
    """
    char* _itoa(
        int value,
        char* str,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__i64toa(jitter):
    """
    char* _i64toa(
        __int64 value,
        char* str,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ui64toa(jitter):
    """
    char* _ui64toa(
        unsigned __int64 value,
        char* str,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__itow(jitter):
    """
    wchar_t* _itow(
        int value,
        wchar_t* str,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__i64tow(jitter):
    """
    wchar_t* _i64tow(
        __int64 value,
        wchar_t* str,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ui64tow(jitter):
    """
    wchar_t* _ui64tow(
        unsigned __int64 value,
        wchar_t* str,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__itoa_s(jitter):
    """
    errno_t _itoa_s(
        int value,
        char* buffer,
        size_t sizeInCharacters,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "buffer", "sizeInCharacters", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__i64toa_s(jitter):
    """
    errno_t _i64toa_s(
        __int64 value,
        char* buffer,
        size_t sizeInCharacters,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "buffer", "sizeInCharacters", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ui64toa_s(jitter):
    """
    errno_t _ui64toa_s(
        unsigned __int64 value,
        char* buffer,
        size_t sizeInCharacters,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "buffer", "sizeInCharacters", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__itow_s(jitter):
    """
    errno_t _itow_s(
        int value,
        wchar_t* buffer,
        size_t sizeInCharacters,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "buffer", "sizeInCharacters", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__i64tow_s(jitter):
    """
    errno_t _i64tow_s(
        __int64 value,
        wchar_t* buffer,
        size_t sizeInCharacters,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "buffer", "sizeInCharacters", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ui64tow_s(jitter):
    """
    errno_t _ui64tow_s(
        unsigned __int64 value,
        wchar_t* buffer,
        size_t sizeInCharacters,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "buffer", "sizeInCharacters", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_labs(jitter):
    """
    long labs(
        long n
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["n"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ltoa(jitter):
    """
    char* _ltoa(
        long value,
        char* str,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ltow(jitter):
    """
    wchar_t* _ltow(
        long value,
        wchar_t* str,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ltoa_s(jitter):
    """
    errno_t _ltoa_s(
        long value,
        char* str,
        size_t sizeOfstr,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "sizeOfstr", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ltow_s(jitter):
    """
    errno_t _ltow_s(
        long value,
        wchar_t* str,
        size_t sizeOfstr,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "sizeOfstr", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbbtombc(jitter):
    """
    unsigned int _mbbtombc(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbbtombc_l(jitter):
    """
    unsigned int _mbbtombc_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbcjistojms(jitter):
    """
    unsigned int _mbcjistojms(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbcjistojms_l(jitter):
    """
    unsigned int _mbcjistojms_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbcjmstojis(jitter):
    """
    unsigned int _mbcjmstojis(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbcjmstojis_l(jitter):
    """
    unsigned int _mbcjmstojis_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctohira(jitter):
    """
    unsigned int _mbctohira(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctohira_l(jitter):
    """
    unsigned int _mbctohira_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctokata(jitter):
    """
    unsigned int _mbctokata(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctokata_l(jitter):
    """
    unsigned int _mbctokata_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctombb(jitter):
    """
    unsigned int _mbctombb(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctombb_l(jitter):
    """
    unsigned int _mbctombb_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___toascii(jitter):
    """
    int __toascii(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tolower(jitter):
    """
    int tolower(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__tolower(jitter):
    """
    int _tolower(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_towlower(jitter):
    """
    int towlower(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__tolower_l(jitter):
    """
    int _tolower_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__towlower_l(jitter):
    """
    int _towlower_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_toupper(jitter):
    """
    int toupper(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__toupper(jitter):
    """
    int _toupper(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_towupper(jitter):
    """
    int towupper(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__toupper_l(jitter):
    """
    int _toupper_l(
        int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__towupper_l(jitter):
    """
    int _towupper_l(
        wint_t c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ultoa(jitter):
    """
    char* _ultoa(
        unsigned long value,
        char* str,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ultow(jitter):
    """
    wchar_t* _ultow(
        unsigned long value,
        wchar_t* str,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ultoa_s(jitter):
    """
    errno_t _ultoa_s(
        unsigned long value,
        char* str,
        size_t sizeOfstr,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "sizeOfstr", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ultow_s(jitter):
    """
    errno_t _ultow_s(
        unsigned long value,
        wchar_t* str,
        size_t sizeOfstr,
        int radix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "sizeOfstr", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fcvt(jitter):
    """
    char* _fcvt(
        double value,
        int count,
        int* dec,
        int* sign
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "count", "dec", "sign"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fcvt_s(jitter):
    """
    errno_t _fcvt_s(
        char* buffer,
        size_t sizeInBytes,
        double value,
        int count,
        int* dec,
        int* sign
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeInBytes", "value", "count", "dec", "sign"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__gcvt(jitter):
    """
    char* _gcvt(
        double value,
        int digits,
        char* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "digits", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__gcvt_s(jitter):
    """
    errno_t _gcvt_s(
        char* buffer,
        size_t sizeInBytes,
        double value,
        int digits
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeInBytes", "value", "digits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atol_l(jitter):
    """
    long _atol_l(
        const char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoi_l(jitter):
    """
    int _atoi_l(
        const char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atof(jitter):
    """
    double atof(
        const char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atof_l(jitter):
    """
    double _atof_l(
        const char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoi64_l(jitter):
    """
    __int64 _atoi64_l(
        const char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atoi(jitter):
    """
    int atoi(
        const char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoi64(jitter):
    """
    __int64 _atoi64(
        const char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atol(jitter):
    """
    long atol(
        const char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atodbl(jitter):
    """
    int _atodbl(
        _CRT_DOUBLE* value,
        char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atodbl_l(jitter):
    """
    int _atodbl_l(
        _CRT_DOUBLE* value,
        char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoldbl(jitter):
    """
    int _atoldbl(
        _LDOUBLE* value,
        char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoldbl_l(jitter):
    """
    int _atoldbl_l(
        _LDOUBLE* value,
        char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoflt(jitter):
    """
    int _atoflt(
        _CRT_FLOAT* value,
        char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoflt_l(jitter):
    """
    int _atoflt_l(
        _CRT_FLOAT* value,
        char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtoi64(jitter):
    """
    __int64 _wtoi64(
        const wchar_t* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtoi64_l(jitter):
    """
    __int64 _wtoi64_l(
        const wchar_t* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strtoul(jitter):
    """
    unsigned long strtoul(
        const char* nptr,
        char** endptr,
        int base
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtoul_l(jitter):
    """
    unsigned long _strtoul_l(
        const char* nptr,
        char** endptr,
        int base,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstoul(jitter):
    """
    unsigned long wcstoul(
        const wchar_t* nptr,
        wchar_t** endptr,
        int base
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstoul_l(jitter):
    """
    unsigned long _wcstoul_l(
        const wchar_t* nptr,
        wchar_t** endptr,
        int base,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strtod(jitter):
    """
    double strtod(
        const char* nptr,
        char** endptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtod_l(jitter):
    """
    double _strtod_l(
        const char* nptr,
        char** endptr,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstod(jitter):
    """
    double wcstod(
        const wchar_t* nptr,
        wchar_t** endptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstod_l(jitter):
    """
    double _wcstod_l(
        const wchar_t* nptr,
        wchar_t** endptr,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strtol(jitter):
    """
    long strtol(
        const char* nptr,
        char** endptr,
        int base
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstol(jitter):
    """
    long wcstol(
        const wchar_t* nptr,
        wchar_t** endptr,
        int base
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtol_l(jitter):
    """
    long _strtol_l(
        const char* nptr,
        char** endptr,
        int base,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstol_l(jitter):
    """
    long _wcstol_l(
        const wchar_t* nptr,
        wchar_t** endptr,
        int base,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbtowc(jitter):
    """
    int mbtowc(
        wchar_t* wchar,
        const char* mbchar,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["wchar", "mbchar", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbtowc_l(jitter):
    """
    int _mbtowc_l(
        wchar_t* wchar,
        const char* mbchar,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["wchar", "mbchar", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbstowcs(jitter):
    """
    size_t mbstowcs(
        wchar_t* wcstr,
        const char* mbstr,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["wcstr", "mbstr", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstowcs_l(jitter):
    """
    size_t _mbstowcs_l(
        wchar_t* wcstr,
        const char* mbstr,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["wcstr", "mbstr", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbstowcs_s(jitter):
    """
    errno_t mbstowcs_s(
        size_t* pReturnValue,
        wchar_t* wcstr,
        size_t sizeInWords,
        const char* mbstr,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "wcstr", "sizeInWords", "mbstr", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstowcs_s_l(jitter):
    """
    errno_t _mbstowcs_s_l(
        size_t* pReturnValue,
        wchar_t* wcstr,
        size_t sizeInWords,
        const char* mbstr,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "wcstr", "sizeInWords", "mbstr", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstombs(jitter):
    """
    size_t wcstombs(
        char* mbstr,
        const wchar_t* wcstr,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "wcstr", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstombs_l(jitter):
    """
    size_t _wcstombs_l(
        char* mbstr,
        const wchar_t* wcstr,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "wcstr", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstombs_s(jitter):
    """
    errno_t wcstombs_s(
        size_t* pReturnValue,
        char* mbstr,
        size_t sizeInBytes,
        const wchar_t* wcstr,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "mbstr", "sizeInBytes", "wcstr", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstombs_s_l(jitter):
    """
    errno_t _wcstombs_s_l(
        size_t* pReturnValue,
        char* mbstr,
        size_t sizeInBytes,
        const wchar_t* wcstr,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "mbstr", "sizeInBytes", "wcstr", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wctomb(jitter):
    """
    int wctomb(
        char* mbchar,
        wchar_t wchar
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mbchar", "wchar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctomb_l(jitter):
    """
    int _wctomb_l(
        char* mbchar,
        wchar_t wchar,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mbchar", "wchar", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wctomb_s(jitter):
    """
    errno_t wctomb_s(
        int* pRetValue,
        char* mbchar,
        size_t sizeInBytes,
        wchar_t wchar
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pRetValue", "mbchar", "sizeInBytes", "wchar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctomb_s_l(jitter):
    """
    errno_t _wctomb_s_l(
        int* pRetValue,
        char* mbchar,
        size_t sizeInBytes,
        wchar_t wchar,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pRetValue", "mbchar", "sizeInBytes", "wchar", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctoupper_l(jitter):
    """
    unsigned int _mbctoupper_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctoupper(jitter):
    """
    unsigned int _mbctoupper(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctolower(jitter):
    """
    unsigned int _mbctolower(
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctolower_l(jitter):
    """
    unsigned int _mbctolower_l(
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ecvt(jitter):
    """
    char* _ecvt(
        double value,
        int count,
        int* dec,
        int* sign
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "count", "dec", "sign"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ecvt_s(jitter):
    """
    errno_t _ecvt_s(
        char* _Buffer,
        size_t _SizeInBytes,
        double _Value,
        int _Count,
        int* _Dec,
        int* _Sign
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["_Buffer", "_SizeInBytes", "_Value", "_Count", "_Dec", "_Sign"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbrtowc(jitter):
    """
    size_t mbrtowc(
        wchar_t* wchar,
        const char* mbchar,
        size_t count,
        mbstate_t mbstate
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["wchar", "mbchar", "count", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbsrtowcs(jitter):
    """
    size_t mbsrtowcs(
        wchar_t* wcstr,
        const char** mbstr,
        size_t count,
        mbstate_t* mbstate
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["wcstr", "mbstr", "count", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbsrtowcs_s(jitter):
    """
    errno_t mbsrtowcs_s(
        size_t* pReturnValue,
        wchar_t* wcstr,
        size_t sizeInWords,
        const char** mbstr,
        size_t count,
        mbstate_t* mbstate
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "wcstr", "sizeInWords", "mbstr", "count", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtoi64(jitter):
    """
    __int64 _strtoi64(
        const char* nptr,
        char** endptr,
        int base
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstoi64(jitter):
    """
    __int64 _wcstoi64(
        const wchar_t* nptr,
        wchar_t** endptr,
        int base
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtoi64_l(jitter):
    """
    __int64 _strtoi64_l(
        const char* nptr,
        char** endptr,
        int base,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstoi64_l(jitter):
    """
    __int64 _wcstoi64_l(
        const wchar_t* nptr,
        wchar_t** endptr,
        int base,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtoui64(jitter):
    """
    unsigned __int64 _strtoui64(
        const char* nptr,
        char** endptr,
        int base
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstoui64(jitter):
    """
    unsigned __int64 _wcstoui64(
        const wchar_t* nptr,
        wchar_t** endptr,
        int base
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtoui64_l(jitter):
    """
    unsigned __int64 _strtoui64_l(
        const char* nptr,
        char** endptr,
        int base,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstoui64_l(jitter):
    """
    unsigned __int64 _wcstoui64_l(
        const wchar_t* nptr,
        wchar_t** endptr,
        int base,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcrtomb(jitter):
    """
    size_t wcrtomb(
        char* mbchar,
        wchar_t wchar,
        mbstate_t* mbstate
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mbchar", "wchar", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcrtomb_s(jitter):
    """
    errno_t wcrtomb_s(
        size_t* pReturnValue,
        char* mbchar,
        size_t sizeOfmbchar,
        wchar_t* wchar,
        mbstate_t* mbstate
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "mbchar", "sizeOfmbchar", "wchar", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsrtombs(jitter):
    """
    size_t wcsrtombs(
        char* mbstr,
        const wchar_t** wcstr,
        size_t count,
        mbstate_t* mbstate
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "wcstr", "count", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsrtombs_s(jitter):
    """
    errno_t wcsrtombs_s(
        size_t* pReturnValue,
        char* mbstr,
        size_t sizeInBytes,
        const wchar_t** wcstr,
        size_t count,
        mbstate_t* mbstate
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "mbstr", "sizeInBytes", "wcstr", "count", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wctob(jitter):
    """
    int wctob(
        wint_t wchar
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["wchar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__byteswap_ushort(jitter):
    """
    unsigned short _byteswap_ushort(
        unsigned short val
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["val"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__byteswap_ulong(jitter):
    """
    unsigned long _byteswap_ulong(
        unsigned long val
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["val"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__byteswap_uint64(jitter):
    """
    unsigned __int64 _byteswap_uint64(
        unsigned __int64 val
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["val"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_btowc(jitter):
    """
    wint_t btowc(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtCheckMemory(jitter):
    """
    int _CrtCheckMemory()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtDbgBreak(jitter):
    """
    void _CrtDbgBreak()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtDbgReport(jitter):
    """
    int _CrtDbgReport(
        [CRT_REPORT_TYPE] reportType,
        const char* filename,
        int linenumber,
        const char* moduleName,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["reportType", "filename", "linenumber", "moduleName", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtDbgReportW(jitter):
    """
    int _CrtDbgReportW(
        [CRT_REPORT_TYPE] reportType,
        const wchar_t* filename,
        int linenumber,
        const wchar_t* moduleName,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["reportType", "filename", "linenumber", "moduleName", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtDoForAllClientObjects(jitter):
    """
    void _CrtDoForAllClientObjects(
        void* pfn,
        void* context
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pfn", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtDumpMemoryLeaks(jitter):
    """
    int _CrtDumpMemoryLeaks()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtIsMemoryBlock(jitter):
    """
    int _CrtIsMemoryBlock(
        const void* userData,
        unsigned int size,
        long* requestNumber,
        char** filename,
        int* linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["userData", "size", "requestNumber", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtIsValidHeapPointer(jitter):
    """
    int _CrtIsValidHeapPointer(
        const void* userData
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["userData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtIsValidPointer(jitter):
    """
    int _CrtIsValidPointer(
        const void* address,
        unsigned int size,
        int access
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["address", "size", "access"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtMemCheckpoint(jitter):
    """
    void _CrtMemCheckpoint(
        _CrtMemState* state
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtMemDifference(jitter):
    """
    int _CrtMemDifference(
        _CrtMemState* stateDiff,
        const _CrtMemState* oldState,
        const _CrtMemState* newState
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stateDiff", "oldState", "newState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtMemDumpAllObjectsSince(jitter):
    """
    void _CrtMemDumpAllObjectsSince(
        const _CrtMemState* state
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtMemDumpStatistics(jitter):
    """
    void _CrtMemDumpStatistics(
        const _CrtMemState* state
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtReportBlockType(jitter):
    """
    int _CrtReportBlockType(
        const void* pBlock
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pBlock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetAllocHook(jitter):
    """
    _CRT_ALLOC_HOOK _CrtSetAllocHook(
        _CRT_ALLOC_HOOK allocHook
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["allocHook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetBreakAlloc(jitter):
    """
    long _CrtSetBreakAlloc(
        long lBreakAlloc
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["lBreakAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetDbgFlag(jitter):
    """
    int _CrtSetDbgFlag(
        [CRTDBG_FLAG] newFlag
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["newFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetDumpClient(jitter):
    """
    _CRT_DUMP_CLIENT _CrtSetDumpClient(
        _CRT_DUMP_CLIENT dumpClient
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dumpClient"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetReportFile(jitter):
    """
    _HFILE _CrtSetReportFile(
        [CRT_REPORT_TYPE] reportType,
        _HFILE reportFile
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["reportType", "reportFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetReportHook(jitter):
    """
    _CRT_REPORT_HOOK _CrtSetReportHook(
        _CRT_REPORT_HOOK reportHook
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["reportHook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetReportHook2(jitter):
    """
    int _CrtSetReportHook2(
        [CRT_RPTHOOK_MODE] mode,
        _CRT_REPORT_HOOK pfnNewHook
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "pfnNewHook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetReportHookW2(jitter):
    """
    int _CrtSetReportHookW2(
        [CRT_RPTHOOK_MODE] mode,
        _CRT_REPORT_HOOKW pfnNewHook
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "pfnNewHook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetReportMode(jitter):
    """
    [CRTDBG_MODE] _CrtSetReportMode(
        [CRT_REPORT_TYPE] reportType,
        [CRTDBG_MODE] reportMode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["reportType", "reportMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtGetAllocHook(jitter):
    """
    _CRT_ALLOC_HOOK _CrtGetAllocHook()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtGetDumpClient(jitter):
    """
    _CRT_DUMP_CLIENT _CrtGetDumpClient()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtGetReportHook(jitter):
    """
    _CRT_REPORT_HOOK _CrtGetReportHook()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetDebugFillThreshold(jitter):
    """
    size_t _CrtSetDebugFillThreshold(
        size_t _NewThreshold
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["_NewThreshold"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chdir(jitter):
    """
    int _chdir(
        const char* dirname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dirname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wchdir(jitter):
    """
    int _wchdir(
        const wchar_t* dirname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dirname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chdrive(jitter):
    """
    int _chdrive(
        int drive
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["drive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getcwd(jitter):
    """
    char* _getcwd(
        char* buffer,
        int maxlen
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "maxlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getcwd_dbg(jitter):
    """
    char* _getcwd_dbg(
        char* buffer,
        int maxlen,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "maxlen", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetcwd(jitter):
    """
    wchar_t* _wgetcwd(
        wchar_t* buffer,
        int maxlen
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "maxlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetcwd_dbg(jitter):
    """
    wchar_t* _wgetcwd_dbg(
        wchar_t* buffer,
        int maxlen,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "maxlen", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdcwd(jitter):
    """
    char* _getdcwd(
        int drive,
        char* buffer,
        int maxlen
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["drive", "buffer", "maxlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdcwd_dbg(jitter):
    """
    char* _getdcwd_dbg(
        int drive,
        char* buffer,
        int maxlen,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["drive", "buffer", "maxlen", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetdcwd(jitter):
    """
    wchar_t* _wgetdcwd(
        int drive,
        wchar_t* buffer,
        int maxlen
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["drive", "buffer", "maxlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetdcwd_dbg(jitter):
    """
    wchar_t* _wgetdcwd_dbg(
        int drive,
        wchar_t* buffer,
        int maxlen,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["drive", "buffer", "maxlen", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdiskfree(jitter):
    """
    errno_t _getdiskfree(
        unsigned drive,
        struct _diskfree_t* driveinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["drive", "driveinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdrive(jitter):
    """
    int _getdrive()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdrives(jitter):
    """
    unsigned long _getdrives()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mkdir(jitter):
    """
    int _mkdir(
        const char* dirname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dirname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wmkdir(jitter):
    """
    int _wmkdir(
        const wchar_t* dirname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dirname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__rmdir(jitter):
    """
    int _rmdir(
        const char* dirname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dirname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wrmdir(jitter):
    """
    int _wrmdir(
        const wchar_t* dirname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dirname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__searchenv(jitter):
    """
    void _searchenv(
        const char* filename,
        const char* varname,
        char* pathname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "varname", "pathname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsearchenv(jitter):
    """
    void _wsearchenv(
        const wchar_t* filename,
        const wchar_t* varname,
        wchar_t* pathname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "varname", "pathname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__searchenv_s(jitter):
    """
    errno_t _searchenv_s(
        const char* filename,
        const char* varname,
        char* pathname,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "varname", "pathname", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsearchenv_s(jitter):
    """
    errno_t _wsearchenv_s(
        const wchar_t* filename,
        const wchar_t* varname,
        wchar_t* pathname,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "varname", "pathname", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_error_mode(jitter):
    """
    [set_error_mode] _set_error_mode(
        [set_error_mode] modeval
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["modeval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__seterrormode(jitter):
    """
    [set_error_mode] _seterrormode(
        [set_error_mode] mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__purecall(jitter):
    """
    void _purecall()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_purecall_handler(jitter):
    """
    _purecall_handler _set_purecall_handler(
        _purecall_handler function
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["function"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_doserrno(jitter):
    """
    errno_t _get_doserrno(
        int* pValue
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_errno(jitter):
    """
    errno_t _get_errno(
        int* pValue
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_doserrno(jitter):
    """
    errno_t _set_doserrno(
        int value
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_errno(jitter):
    """
    errno_t _set_errno(
        int value
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_abort_behavior(jitter):
    """
    [abort_flag] _set_abort_behavior(
        [abort_flag] flags,
        [abort_flag] mask
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["flags", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_invalid_parameter_handler(jitter):
    """
    _invalid_parameter_handler _get_invalid_parameter_handler()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_invalid_parameter_handler(jitter):
    """
    _invalid_parameter_handler _set_invalid_parameter_handler(
        _invalid_parameter_handler pNew
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__amsg_exit(jitter):
    """
    void _amsg_exit(
        int rterrnum
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["rterrnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?_set_se_translator@@YAP6AXIPAU_EXCEPTION_POINTERS@@@ZP6AXI0@Z@Z(jitter):
    """
    _se_translator_function ?_set_se_translator@@YAP6AXIPAU_EXCEPTION_POINTERS@@@ZP6AXI0@Z@Z(
        _se_translator_function seTransFunction
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["seTransFunction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_terminate(jitter):
    """
    terminate_function _get_terminate()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?set_terminate@@YAP6AXXZP6AXXZ@Z(jitter):
    """
    terminate_function ?set_terminate@@YAP6AXXZP6AXXZ@Z(
        terminate_function termFunction
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["termFunction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_unexpected(jitter):
    """
    unexpected_function _get_unexpected()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?set_unexpected@@YAP6AXXZP6AXXZ@Z(jitter):
    """
    unexpected_function ?set_unexpected@@YAP6AXXZP6AXXZ@Z(
        unexpected_function unexpFunction
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["unexpFunction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?terminate@@YAXXZ(jitter):
    """
    void ?terminate@@YAXXZ()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?unexpected@@YAXXZ(jitter):
    """
    void ?unexpected@@YAXXZ()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___CxxFrameHandler(jitter):
    """
    EXCEPTION_DISPOSITION __CxxFrameHandler(
        EHExceptionRecord* pExcept,
        EHRegistrationNode* pRN,
        void* pContext,
        DispatcherContext* pDC
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pExcept", "pRN", "pContext", "pDC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__except_handler3(jitter):
    """
    [disposition_type] _except_handler3(
        PEXCEPTION_RECORD exception_record,
        PEXCEPTION_REGISTRATION registration,
        PCONTEXT context,
        PEXCEPTION_REGISTRATION dispatcher
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["exception_record", "registration", "context", "dispatcher"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___uncaught_exception(jitter):
    """
    bool __uncaught_exception()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__XcptFilter(jitter):
    """
    [xcpt_action] _XcptFilter(
        [xcpt_num] xcptnum,
        PEXCEPTION_POINTERS pxcptinfoptrs
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["xcptnum", "pxcptinfoptrs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__resetstkoflw(jitter):
    """
    int _resetstkoflw()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__abnormal_termination(jitter):
    """
    int _abnormal_termination()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chsize(jitter):
    """
    int _chsize(
        int fd,
        long size
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chsize_s(jitter):
    """
    errno_t _chsize_s(
        int fd,
        __int64 size
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__filelength(jitter):
    """
    long _filelength(
        int fd
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__filelengthi64(jitter):
    """
    __int64 _filelengthi64(
        int fd
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fstat(jitter):
    """
    int _fstat(
        int fd,
        struct _stat* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fstat32(jitter):
    """
    int _fstat32(
        int fd,
        struct _stat32* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fstat64(jitter):
    """
    int _fstat64(
        int fd,
        struct _stat64* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fstati64(jitter):
    """
    int _fstati64(
        int fd,
        struct _stati64* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fstat32i64(jitter):
    """
    int _fstat32i64(
        int fd,
        struct _stat32i64* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fstat64i32(jitter):
    """
    int _fstat64i32(
        int fd,
        struct _stat64i32* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_osfhandle(jitter):
    """
    intptr_t _get_osfhandle(
        int fd
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isatty(jitter):
    """
    int _isatty(
        int fd
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__locking(jitter):
    """
    int _locking(
        int fd,
        [_LK_MODE] mode,
        long nbytes
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "mode", "nbytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__open_osfhandle(jitter):
    """
    int _open_osfhandle(
        intptr_t osfhandle,
        int flags
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["osfhandle", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__access(jitter):
    """
    int _access(
        const char* path,
        int mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__waccess(jitter):
    """
    int _waccess(
        const wchar_t* path,
        int mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__access_s(jitter):
    """
    errno_t _access_s(
        const char* path,
        int mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__waccess_s(jitter):
    """
    errno_t _waccess_s(
        const wchar_t* path,
        int mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chmod(jitter):
    """
    int _chmod(
        const char* filename,
        [perm_mode] pmode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wchmod(jitter):
    """
    int _wchmod(
        const wchar_t* filename,
        [perm_mode] pmode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fullpath(jitter):
    """
    char* _fullpath(
        char* absPath,
        const char* relPath,
        size_t maxLength
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["absPath", "relPath", "maxLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fullpath_dbg(jitter):
    """
    char* _fullpath_dbg(
        char* absPath,
        const char* relPath,
        size_t maxLength,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["absPath", "relPath", "maxLength", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfullpath(jitter):
    """
    wchar_t* _wfullpath(
        wchar_t* absPath,
        const wchar_t* relPath,
        size_t maxLength
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["absPath", "relPath", "maxLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfullpath_dbg(jitter):
    """
    wchar_t* _wfullpath_dbg(
        wchar_t* absPath,
        const wchar_t* relPath,
        size_t maxLength,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["absPath", "relPath", "maxLength", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__makepath(jitter):
    """
    void _makepath(
        char* path,
        const char* drive,
        const char* dir,
        const char* fname,
        const char* ext
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "drive", "dir", "fname", "ext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wmakepath(jitter):
    """
    void _wmakepath(
        wchar_t* path,
        const wchar_t* drive,
        const wchar_t* dir,
        const wchar_t* fname,
        const wchar_t* ext
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "drive", "dir", "fname", "ext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__makepath_s(jitter):
    """
    errno_t _makepath_s(
        char* path,
        size_t sizeInBytes,
        const char* drive,
        const char* dir,
        const char* fname,
        const char* ext
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "sizeInBytes", "drive", "dir", "fname", "ext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wmakepath_s(jitter):
    """
    errno_t _wmakepath_s(
        wchar_t* path,
        size_t sizeInWords,
        const wchar_t* drive,
        const wchar_t* dir,
        const wchar_t* fname,
        const wchar_t* ext
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "sizeInWords", "drive", "dir", "fname", "ext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mktemp(jitter):
    """
    char* _mktemp(
        char* template
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["template"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wmktemp(jitter):
    """
    wchar_t* _wmktemp(
        wchar_t* template
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["template"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mktemp_s(jitter):
    """
    errno_t _mktemp_s(
        char* template,
        size_t sizeInChars
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["template", "sizeInChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wmktemp_s(jitter):
    """
    errno_t _wmktemp_s(
        wchar_t* template,
        size_t sizeInChars
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["template", "sizeInChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_remove(jitter):
    """
    int remove(
        const char* path
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wremove(jitter):
    """
    int _wremove(
        const wchar_t* path
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_rename(jitter):
    """
    int rename(
        const char* oldname,
        const char* newname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["oldname", "newname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wrename(jitter):
    """
    int _wrename(
        const wchar_t* oldname,
        const wchar_t* newname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["oldname", "newname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__splitpath(jitter):
    """
    void _splitpath(
        const char* path,
        char* drive,
        char* dir,
        char* fname,
        char* ext
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "drive", "dir", "fname", "ext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsplitpath(jitter):
    """
    void _wsplitpath(
        const wchar_t* path,
        wchar_t* drive,
        wchar_t* dir,
        wchar_t* fname,
        wchar_t* ext
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "drive", "dir", "fname", "ext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__splitpath_s(jitter):
    """
    errno_t _splitpath_s(
        const char* path,
        char* drive,
        size_t driveNumberOfElements,
        char* dir,
        size_t dirNumberOfElements,
        char* fname,
        size_t nameNumberOfElements,
        char* ext,
        size_t extNumberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "drive", "driveNumberOfElements", "dir", "dirNumberOfElements", "fname", "nameNumberOfElements", "ext", "extNumberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsplitpath_s(jitter):
    """
    errno_t _wsplitpath_s(
        const wchar_t* path,
        wchar_t* drive,
        size_t driveNumberOfElements,
        wchar_t* dir,
        size_t dirNumberOfElements,
        wchar_t* fname,
        size_t nameNumberOfElements,
        wchar_t* ext,
        size_t extNumberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "drive", "driveNumberOfElements", "dir", "dirNumberOfElements", "fname", "nameNumberOfElements", "ext", "extNumberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stat(jitter):
    """
    int _stat(
        const char* path,
        struct _stat* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stat32(jitter):
    """
    int _stat32(
        const char* path,
        struct _stat32* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stat64(jitter):
    """
    int _stat64(
        const char* path,
        struct _stat64* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stati64(jitter):
    """
    int _stati64(
        const char* path,
        struct _stati64* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stat32i64(jitter):
    """
    int _stat32i64(
        const char* path,
        struct _stat32i64* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stat64i32(jitter):
    """
    int _stat64i32(
        const char* path,
        struct _stat64i32* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstat(jitter):
    """
    int _wstat(
        const wchar_t* path,
        struct _stat* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstat32(jitter):
    """
    int _wstat32(
        const wchar_t* path,
        struct _stat32* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstat64(jitter):
    """
    int _wstat64(
        const wchar_t* path,
        struct _stat64* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstati64(jitter):
    """
    int _wstati64(
        const wchar_t* path,
        struct _stati64* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstat32i64(jitter):
    """
    int _wstat32i64(
        const wchar_t* path,
        struct _stat32i64* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstat64i32(jitter):
    """
    int _wstat64i32(
        const wchar_t* path,
        struct _stat64i32* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__unlink(jitter):
    """
    int _unlink(
        const char* filename
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wunlink(jitter):
    """
    int _wunlink(
        const wchar_t* filename
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_acos(jitter):
    """
    double acos(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_acosf(jitter):
    """
    float acosf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_asin(jitter):
    """
    double asin(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_asinf(jitter):
    """
    float asinf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atan(jitter):
    """
    double atan(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atan2(jitter):
    """
    double atan2(
        double y,
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["y", "x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atanf(jitter):
    """
    float atanf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atan2f(jitter):
    """
    float atan2f(
        float y,
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["y", "x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cabs(jitter):
    """
    double _cabs(
        struct _complex z
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["z"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ceil(jitter):
    """
    double ceil(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ceilf(jitter):
    """
    float ceilf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chgsign(jitter):
    """
    double _chgsign(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chgsignf(jitter):
    """
    float _chgsignf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__clearfp(jitter):
    """
    [_SW_FLOAT] _clearfp()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__control87(jitter):
    """
    unsigned int _control87(
        [control_bits] new,
        [control_mask] mask
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["new", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__controlfp(jitter):
    """
    unsigned int _controlfp(
        [control_bits] new,
        [control_mask] mask
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["new", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___control87_2(jitter):
    """
    int __control87_2(
        [control_bits] new,
        [control_mask] mask,
        unsigned int* x86_cw,
        unsigned int* sse2_cw
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["new", "mask", "x86_cw", "sse2_cw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__controlfp_s(jitter):
    """
    errno_t _controlfp_s(
        unsigned int* currentControl,
        [control_bits] newControl,
        [control_mask] mask
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["currentControl", "newControl", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__copysign(jitter):
    """
    double _copysign(
        double x,
        double y
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__copysignf(jitter):
    """
    float _copysignf(
        float x,
        float y
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_cos(jitter):
    """
    double cos(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_cosf(jitter):
    """
    float cosf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_cosh(jitter):
    """
    double cosh(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_coshf(jitter):
    """
    float coshf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_div(jitter):
    """
    div_t div(
        int numer,
        int denom
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["numer", "denom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_exp(jitter):
    """
    double exp(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_expf(jitter):
    """
    float expf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fabs(jitter):
    """
    double fabs(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__finite(jitter):
    """
    int _finite(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_floor(jitter):
    """
    double floor(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_floorf(jitter):
    """
    float floorf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fmod(jitter):
    """
    double fmod(
        double x,
        double y
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fmodf(jitter):
    """
    float fmodf(
        float x,
        float y
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fpclass(jitter):
    """
    [_FPCLASS] _fpclass(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fpieee_flt(jitter):
    """
    int _fpieee_flt(
        unsigned long excCode,
        struct _EXCEPTION_POINTERS* excInfo,
        void* handler
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["excCode", "excInfo", "handler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fpreset(jitter):
    """
    void _fpreset()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_frexp(jitter):
    """
    double frexp(
        double x,
        int* expptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "expptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__hypot(jitter):
    """
    double _hypot(
        double x,
        double y
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__hypotf(jitter):
    """
    float _hypotf(
        float x,
        float y
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isnan(jitter):
    """
    int _isnan(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ldexp(jitter):
    """
    double ldexp(
        double x,
        int exp
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "exp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ldiv(jitter):
    """
    ldiv_t ldiv(
        long int numer,
        long int denom
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["numer", "denom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_log(jitter):
    """
    double log(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_logf(jitter):
    """
    float logf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_log10(jitter):
    """
    double log10(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_log10f(jitter):
    """
    float log10f(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__logb(jitter):
    """
    double _logb(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lrotl(jitter):
    """
    unsigned long _lrotl(
        unsigned long value,
        int shift
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "shift"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lrotr(jitter):
    """
    unsigned long _lrotr(
        unsigned long value,
        int shift
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "shift"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__matherr(jitter):
    """
    int _matherr(
        struct _exception* except
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["except"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___setusermatherr(jitter):
    """
    void __setusermatherr(
        _HANDLE_MATH_ERROR pf
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_modf(jitter):
    """
    double modf(
        double x,
        double* intptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "intptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_modff(jitter):
    """
    float modff(
        float x,
        float* intptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "intptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__nextafter(jitter):
    """
    double _nextafter(
        double x,
        double y
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_pow(jitter):
    """
    double pow(
        double x,
        double y
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_powf(jitter):
    """
    float powf(
        float x,
        float y
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_rand(jitter):
    """
    int rand()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_rand_s(jitter):
    """
    errno_t rand_s(
        unsigned int* randomValue
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["randomValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__rotl(jitter):
    """
    unsigned int _rotl(
        unsigned int value,
        int shift
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "shift"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__rotl64(jitter):
    """
    unsigned __int64 _rotl64(
        unsigned __int64 value,
        int shift
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "shift"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__rotr(jitter):
    """
    unsigned int _rotr(
        unsigned int value,
        int shift
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "shift"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__rotr64(jitter):
    """
    unsigned __int64 _rotr64(
        unsigned __int64 value,
        int shift
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value", "shift"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scalb(jitter):
    """
    double _scalb(
        double x,
        long exp
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x", "exp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_controlfp(jitter):
    """
    void _set_controlfp(
        unsigned int newControl,
        unsigned int mask
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["newControl", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sin(jitter):
    """
    double sin(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sinf(jitter):
    """
    float sinf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sinh(jitter):
    """
    double sinh(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sinhf(jitter):
    """
    float sinhf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sqrt(jitter):
    """
    double sqrt(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sqrtf(jitter):
    """
    float sqrtf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_srand(jitter):
    """
    void srand(
        unsigned int seed
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["seed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__statusfp(jitter):
    """
    unsigned int _statusfp()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tan(jitter):
    """
    double tan(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tanf(jitter):
    """
    float tanf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tanh(jitter):
    """
    double tanh(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tanhf(jitter):
    """
    float tanhf(
        float x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__y0(jitter):
    """
    double _y0(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__y1(jitter):
    """
    double _y1(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__yn(jitter):
    """
    double _yn(
        int n,
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["n", "x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__j0(jitter):
    """
    double _j0(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__j1(jitter):
    """
    double _j1(
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__jn(jitter):
    """
    double _jn(
        int n,
        double x
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["n", "x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_SSE2_enable(jitter):
    """
    int _set_SSE2_enable(
        int flag
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["flag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_fmode(jitter):
    """
    errno_t _set_fmode(
        [file_translation_mode] mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_fmode(jitter):
    """
    errno_t _get_fmode(
        [file_translation_mode*] pmode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__setmode(jitter):
    """
    [file_translation_mode] _setmode(
        int fd,
        [file_translation_mode] mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___p__fmode(jitter):
    """
    [file_translation_mode*] __p__fmode()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_clearerr(jitter):
    """
    void clearerr(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_clearerr_s(jitter):
    """
    errno_t clearerr_s(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fclose(jitter):
    """
    [RET_EOF] fclose(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fcloseall(jitter):
    """
    [RET_EOF] _fcloseall()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fdopen(jitter):
    """
    FILE* _fdopen(
        int fd,
        const char* mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfdopen(jitter):
    """
    FILE* _wfdopen(
        int fd,
        const wchar_t* mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_feof(jitter):
    """
    int feof(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ferror(jitter):
    """
    int ferror(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fflush(jitter):
    """
    [RET_EOF] fflush(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fgetc(jitter):
    """
    [RET_EOF] fgetc(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fgetwc(jitter):
    """
    [RET_WEOF] fgetwc(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fgetpos(jitter):
    """
    int fgetpos(
        FILE* stream,
        fpos_t* pos
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "pos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fgets(jitter):
    """
    char* fgets(
        char* str,
        int n,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "n", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fgetws(jitter):
    """
    wchar_t* fgetws(
        wchar_t* str,
        int n,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "n", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fileno(jitter):
    """
    int _fileno(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__flushall(jitter):
    """
    int _flushall()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fopen(jitter):
    """
    FILE* fopen(
        const char* filename,
        const char* mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfopen(jitter):
    """
    FILE* _wfopen(
        const wchar_t* filename,
        const wchar_t* mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fopen_s(jitter):
    """
    errno_t fopen_s(
        FILE** pFile,
        const char* filename,
        const char* mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pFile", "filename", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfopen_s(jitter):
    """
    errno_t _wfopen_s(
        FILE** pFile,
        const wchar_t* filename,
        const wchar_t* mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pFile", "filename", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fprintf(jitter):
    """
    int fprintf(
        FILE* stream,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fprintf_l(jitter):
    """
    int _fprintf_l(
        FILE* stream,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fwprintf(jitter):
    """
    int fwprintf(
        FILE* stream,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwprintf_l(jitter):
    """
    int _fwprintf_l(
        FILE* stream,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fprintf_s(jitter):
    """
    int fprintf_s(
        FILE* stream,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fprintf_s_l(jitter):
    """
    int _fprintf_s_l(
        FILE* stream,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fwprintf_s(jitter):
    """
    int fwprintf_s(
        FILE* stream,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwprintf_s_l(jitter):
    """
    int _fwprintf_s_l(
        FILE* stream,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fputc(jitter):
    """
    [RET_EOF] fputc(
        int c,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fputwc(jitter):
    """
    [RET_WEOF] fputwc(
        wchar_t c,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fputs(jitter):
    """
    [RET_EOF] fputs(
        const char* str,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fputws(jitter):
    """
    [RET_WEOF_INT] fputws(
        const wchar_t* str,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fread(jitter):
    """
    size_t fread(
        void* buffer,
        size_t size,
        size_t count,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "size", "count", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_freopen(jitter):
    """
    FILE* freopen(
        const char* path,
        const char* mode,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "mode", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfreopen(jitter):
    """
    FILE* _wfreopen(
        const wchar_t* path,
        const wchar_t* mode,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["path", "mode", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_freopen_s(jitter):
    """
    errno_t freopen_s(
        FILE** pFile,
        const char* path,
        const char* mode,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pFile", "path", "mode", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfreopen_s(jitter):
    """
    errno_t _wfreopen_s(
        FILE** pFile,
        const wchar_t* path,
        const wchar_t* mode,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pFile", "path", "mode", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fscanf(jitter):
    """
    [RET_EOF] fscanf(
        FILE* stream,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fscanf_l(jitter):
    """
    [RET_EOF] _fscanf_l(
        FILE* stream,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fwscanf(jitter):
    """
    [RET_EOF] fwscanf(
        FILE* stream,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwscanf_l(jitter):
    """
    [RET_EOF] _fwscanf_l(
        FILE* stream,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fscanf_s(jitter):
    """
    [RET_EOF] fscanf_s(
        FILE* stream,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fscanf_s_l(jitter):
    """
    [RET_EOF] _fscanf_s_l(
        FILE* stream,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fwscanf_s(jitter):
    """
    [RET_EOF] fwscanf_s(
        FILE* stream,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwscanf_s_l(jitter):
    """
    [RET_EOF] _fwscanf_s_l(
        FILE* stream,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fseek(jitter):
    """
    int fseek(
        FILE* stream,
        long offset,
        [SEEK_TYPE] origin
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "offset", "origin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fseeki64(jitter):
    """
    int _fseeki64(
        FILE* stream,
        __int64 offset,
        [SEEK_TYPE] origin
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "offset", "origin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fsetpos(jitter):
    """
    int fsetpos(
        FILE* stream,
        const fpos_t* pos
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "pos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fsopen(jitter):
    """
    FILE* _fsopen(
        const char* filename,
        const char* mode,
        [share_flag] shflag
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "mode", "shflag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfsopen(jitter):
    """
    FILE* _wfsopen(
        const wchar_t* filename,
        const wchar_t* mode,
        [share_flag] shflag
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "mode", "shflag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ftell(jitter):
    """
    long ftell(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftelli64(jitter):
    """
    __int64 _ftelli64(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fwrite(jitter):
    """
    size_t fwrite(
        const void* buffer,
        size_t size,
        size_t count,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "size", "count", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_getc(jitter):
    """
    [RET_EOF] getc(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_getwc(jitter):
    """
    [RET_WEOF] getwc(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getmaxstdio(jitter):
    """
    int _getmaxstdio()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_gets(jitter):
    """
    char* gets(
        char* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getws(jitter):
    """
    wchar_t* _getws(
        wchar_t* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_gets_s(jitter):
    """
    char* gets_s(
        char* buffer,
        size_t sizeInCharacters
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeInCharacters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getws_s(jitter):
    """
    wchar_t* _getws_s(
        wchar_t* buffer,
        size_t sizeInCharacters
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeInCharacters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getw(jitter):
    """
    [RET_EOF] _getw(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_putc(jitter):
    """
    [RET_EOF] putc(
        int c,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_putwc(jitter):
    """
    [RET_WEOF] putwc(
        wchar_t c,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_puts(jitter):
    """
    [RET_EOF] puts(
        const char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putws(jitter):
    """
    [RET_WEOF_INT] _putws(
        const wchar_t* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putw(jitter):
    """
    [RET_EOF] _putw(
        int binint,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["binint", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_rewind(jitter):
    """
    void rewind(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__rmtmp(jitter):
    """
    int _rmtmp()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_setbuf(jitter):
    """
    void setbuf(
        FILE* stream,
        char* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__setmaxstdio(jitter):
    """
    int _setmaxstdio(
        int newmax
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["newmax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_setvbuf(jitter):
    """
    int setvbuf(
        FILE* stream,
        char* buffer,
        [buffer_mode] mode,
        size_t size
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "buffer", "mode", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__tempnam(jitter):
    """
    char* _tempnam(
        const char* dir,
        const char* prefix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dir", "prefix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__tempnam_dbg(jitter):
    """
    char* _tempnam_dbg(
        const char* dir,
        const char* prefix,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dir", "prefix", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtempnam(jitter):
    """
    wchar_t* _wtempnam(
        const wchar_t* dir,
        const wchar_t* prefix
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dir", "prefix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtempnam_dbg(jitter):
    """
    wchar_t* _wtempnam_dbg(
        const wchar_t* dir,
        const wchar_t* prefix,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dir", "prefix", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tmpnam(jitter):
    """
    char* tmpnam(
        char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtmpnam(jitter):
    """
    wchar_t* _wtmpnam(
        wchar_t* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tmpfile(jitter):
    """
    FILE* tmpfile()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tmpfile_s(jitter):
    """
    errno_t tmpfile_s(
        FILE** pFilePtr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pFilePtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tmpnam_s(jitter):
    """
    errno_t tmpnam_s(
        char* str,
        size_t sizeInChars
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "sizeInChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtmpnam_s(jitter):
    """
    errno_t _wtmpnam_s(
        wchar_t* str,
        size_t sizeInChars
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "sizeInChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ungetc(jitter):
    """
    [RET_EOF] ungetc(
        int c,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ungetwc(jitter):
    """
    [RET_WEOF] ungetwc(
        wint_t c,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcprintf_s(jitter):
    """
    int _vcprintf_s(
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcprintf_s_l(jitter):
    """
    int _vcprintf_s_l(
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcwprintf_s(jitter):
    """
    int _vcwprintf_s(
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcwprintf_s_l(jitter):
    """
    int _vcwprintf_s_l(
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vfprintf_s(jitter):
    """
    int vfprintf_s(
        FILE* stream,
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfprintf_s_l(jitter):
    """
    int _vfprintf_s_l(
        FILE* stream,
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vfwprintf_s(jitter):
    """
    int vfwprintf_s(
        FILE* stream,
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfwprintf_s_l(jitter):
    """
    int _vfwprintf_s_l(
        FILE* stream,
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vprintf_s(jitter):
    """
    int vprintf_s(
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vprintf_s_l(jitter):
    """
    int _vprintf_s_l(
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vwprintf_s(jitter):
    """
    int vwprintf_s(
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vwprintf_s_l(jitter):
    """
    int _vwprintf_s_l(
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_printf(jitter):
    """
    int printf(
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__printf_l(jitter):
    """
    int _printf_l(
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wprintf(jitter):
    """
    int wprintf(
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wprintf_l(jitter):
    """
    int _wprintf_l(
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_printf_s(jitter):
    """
    int printf_s(
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__printf_s_l(jitter):
    """
    int _printf_s_l(
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wprintf_s(jitter):
    """
    int wprintf_s(
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wprintf_s_l(jitter):
    """
    int _wprintf_s_l(
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_scanf(jitter):
    """
    [RET_EOF] scanf(
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scanf_l(jitter):
    """
    [RET_EOF] _scanf_l(
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wscanf(jitter):
    """
    [RET_EOF] wscanf(
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wscanf_l(jitter):
    """
    [RET_EOF] _wscanf_l(
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_scanf_s(jitter):
    """
    [RET_EOF] scanf_s(
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scanf_s_l(jitter):
    """
    [RET_EOF] _scanf_s_l(
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wscanf_s(jitter):
    """
    [RET_EOF] wscanf_s(
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wscanf_s_l(jitter):
    """
    [RET_EOF] _wscanf_s_l(
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcprintf(jitter):
    """
    int _vcprintf(
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcprintf_l(jitter):
    """
    int _vcprintf_l(
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcwprintf(jitter):
    """
    int _vcwprintf(
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcwprintf_l(jitter):
    """
    int _vcwprintf_l(
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcprintf_p(jitter):
    """
    int _vcprintf_p(
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcprintf_p_l(jitter):
    """
    int _vcprintf_p_l(
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcwprintf_p(jitter):
    """
    int _vcwprintf_p(
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcwprintf_p_l(jitter):
    """
    int _vcwprintf_p_l(
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vfprintf(jitter):
    """
    int vfprintf(
        FILE* stream,
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfprintf_l(jitter):
    """
    int _vfprintf_l(
        FILE* stream,
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vfwprintf(jitter):
    """
    int vfwprintf(
        FILE* stream,
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfwprintf_l(jitter):
    """
    int _vfwprintf_l(
        FILE* stream,
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfprintf_p(jitter):
    """
    int _vfprintf_p(
        FILE* stream,
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfprintf_p_l(jitter):
    """
    int _vfprintf_p_l(
        FILE* stream,
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfwprintf_p(jitter):
    """
    int _vfwprintf_p(
        FILE* stream,
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfwprintf_p_l(jitter):
    """
    int _vfwprintf_p_l(
        FILE* stream,
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vprintf(jitter):
    """
    int vprintf(
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vprintf_l(jitter):
    """
    int _vprintf_l(
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vwprintf(jitter):
    """
    int vwprintf(
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vwprintf_l(jitter):
    """
    int _vwprintf_l(
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vprintf_p(jitter):
    """
    int _vprintf_p(
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vprintf_p_l(jitter):
    """
    int _vprintf_p_l(
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vwprintf_p(jitter):
    """
    int _vwprintf_p(
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vwprintf_p_l(jitter):
    """
    int _vwprintf_p_l(
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscprintf(jitter):
    """
    int _vscprintf(
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscprintf_l(jitter):
    """
    int _vscprintf_l(
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscwprintf(jitter):
    """
    int _vscwprintf(
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscwprintf_l(jitter):
    """
    int _vscwprintf_l(
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscprintf_p(jitter):
    """
    int _vscprintf_p(
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscprintf_p_l(jitter):
    """
    int _vscprintf_p_l(
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscwprintf_p(jitter):
    """
    int _vscwprintf_p(
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscwprintf_p_l(jitter):
    """
    int _vscwprintf_p_l(
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wprintf_p(jitter):
    """
    int _wprintf_p(
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wprintf_p_l(jitter):
    """
    int _wprintf_p_l(
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fprintf_p(jitter):
    """
    int _fprintf_p(
        FILE* stream,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fprintf_p_l(jitter):
    """
    int _fprintf_p_l(
        FILE* stream,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwprintf_p(jitter):
    """
    int _fwprintf_p(
        FILE* stream,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwprintf_p_l(jitter):
    """
    int _fwprintf_p_l(
        FILE* stream,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__printf_p(jitter):
    """
    int _printf_p(
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__printf_p_l(jitter):
    """
    int _printf_p_l(
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_putchar(jitter):
    """
    [RET_EOF] putchar(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_putwchar(jitter):
    """
    [RET_WEOF] putwchar(
        wchar_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_getchar(jitter):
    """
    [RET_EOF] getchar()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_getwchar(jitter):
    """
    [RET_WEOF] getwchar()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fgetchar(jitter):
    """
    [RET_EOF] _fgetchar()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fgetwchar(jitter):
    """
    [RET_WEOF] _fgetwchar()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fputchar(jitter):
    """
    [RET_EOF] _fputchar(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fputwchar(jitter):
    """
    [RET_WEOF] _fputwchar(
        wchar_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lock_file(jitter):
    """
    void _lock_file(
        FILE* file
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["file"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__unlock_file(jitter):
    """
    void _unlock_file(
        FILE* file
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["file"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__close(jitter):
    """
    int _close(
        int fd
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__commit(jitter):
    """
    int _commit(
        int fd
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__creat(jitter):
    """
    int _creat(
        const char* filename,
        [perm_mode] pmode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcreat(jitter):
    """
    int _wcreat(
        const wchar_t* filename,
        [perm_mode] pmode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__dup(jitter):
    """
    int _dup(
        int fd
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__dup2(jitter):
    """
    int _dup2(
        int fd1,
        int fd2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd1", "fd2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__eof(jitter):
    """
    int _eof(
        int fd
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lseek(jitter):
    """
    long _lseek(
        int fd,
        long offset,
        [SEEK_TYPE] origin
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "offset", "origin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lseeki64(jitter):
    """
    __int64 _lseeki64(
        int fd,
        __int64 offset,
        [SEEK_TYPE] origin
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "offset", "origin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__open(jitter):
    """
    int _open(
        const char* filename,
        [open_flag] oflag,
        [perm_mode] pmode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "oflag", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wopen(jitter):
    """
    int _wopen(
        const wchar_t* filename,
        [open_flag] oflag,
        [perm_mode] pmode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "oflag", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__read(jitter):
    """
    int _read(
        int fd,
        void* buffer,
        unsigned int count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sopen(jitter):
    """
    int _sopen(
        const char* filename,
        [open_flag] oflag,
        [share_flag] shflag,
        [perm_mode] pmode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "oflag", "shflag", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsopen(jitter):
    """
    int _wsopen(
        const wchar_t* filename,
        [open_flag] oflag,
        [share_flag] shflag,
        [perm_mode] pmode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "oflag", "shflag", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sopen_s(jitter):
    """
    errno_t _sopen_s(
        int* pfh,
        const char* filename,
        [open_flag] oflag,
        [share_flag] shflag,
        [perm_mode] pmode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pfh", "filename", "oflag", "shflag", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsopen_s(jitter):
    """
    errno_t _wsopen_s(
        int* pfh,
        const wchar_t* filename,
        [open_flag] oflag,
        [share_flag] shflag,
        [perm_mode] pmode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pfh", "filename", "oflag", "shflag", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__tell(jitter):
    """
    long _tell(
        int handle
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__telli64(jitter):
    """
    __int64 _telli64(
        int handle
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__umask(jitter):
    """
    [perm_mode] _umask(
        [perm_mode] pmode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__umask_s(jitter):
    """
    errno_t _umask_s(
        [perm_mode] mode,
        [perm_mode*] pOldMode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "pOldMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__write(jitter):
    """
    int _write(
        int fd,
        const void* buffer,
        unsigned int count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cgets(jitter):
    """
    char* _cgets(
        char* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cgetws(jitter):
    """
    wchar_t* _cgetws(
        wchar_t* buffer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cgets_s(jitter):
    """
    errno_t _cgets_s(
        char* buffer,
        size_t numberOfElements,
        size_t* pSizeRead
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "pSizeRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cgetws_s(jitter):
    """
    errno_t _cgetws_s(
        wchar_t* buffer,
        size_t* pSizeRead
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "pSizeRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cprintf(jitter):
    """
    int _cprintf(
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cprintf_l(jitter):
    """
    int _cprintf_l(
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwprintf(jitter):
    """
    int _cwprintf(
        const wchar* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwprintf_l(jitter):
    """
    int _cwprintf_l(
        const wchar* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cprintf_s(jitter):
    """
    int _cprintf_s(
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cprintf_s_l(jitter):
    """
    int _cprintf_s_l(
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwprintf_s(jitter):
    """
    int _cwprintf_s(
        const wchar* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwprintf_s_l(jitter):
    """
    int _cwprintf_s_l(
        const wchar* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cputs(jitter):
    """
    int _cputs(
        const char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cputws(jitter):
    """
    int _cputws(
        const wchar_t* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cscanf(jitter):
    """
    [RET_EOF] _cscanf(
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cscanf_l(jitter):
    """
    [RET_EOF] _cscanf_l(
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwscanf(jitter):
    """
    [RET_EOF] _cwscanf(
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwscanf_l(jitter):
    """
    [RET_EOF] _cwscanf_l(
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cscanf_s(jitter):
    """
    [RET_EOF] _cscanf_s(
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cscanf_s_l(jitter):
    """
    [RET_EOF] _cscanf_s_l(
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwscanf_s(jitter):
    """
    [RET_EOF] _cwscanf_s(
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwscanf_s_l(jitter):
    """
    [RET_EOF] _cwscanf_s_l(
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getch(jitter):
    """
    int _getch()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getwch(jitter):
    """
    wint_t _getwch()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getche(jitter):
    """
    int _getche()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getwche(jitter):
    """
    wint_t _getwche()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__inp(jitter):
    """
    int _inp(
        unsigned short port
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["port"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__inpw(jitter):
    """
    unsigned short _inpw(
        unsigned short port
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["port"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__inpd(jitter):
    """
    unsigned long _inpd(
        unsigned short port
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["port"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__kbhit(jitter):
    """
    int _kbhit()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__outp(jitter):
    """
    int _outp(
        unsigned short port,
        int databyte
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["port", "databyte"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__outpw(jitter):
    """
    unsigned short _outpw(
        unsigned short port,
        unsigned short dataword
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["port", "dataword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__outpd(jitter):
    """
    unsigned long _outpd(
        unsigned short port,
        unsigned long dataword
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["port", "dataword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putch(jitter):
    """
    [RET_EOF] _putch(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putwch(jitter):
    """
    [RET_WEOF] _putwch(
        wchar_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ungetch(jitter):
    """
    [RET_EOF] _ungetch(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ungetwch(jitter):
    """
    [RET_WEOF] _ungetwch(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cprintf_p(jitter):
    """
    int _cprintf_p(
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cprintf_p_l(jitter):
    """
    int _cprintf_p_l(
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwprintf_p(jitter):
    """
    int _cwprintf_p(
        const wchar* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwprintf_p_l(jitter):
    """
    int _cwprintf_p_l(
        const wchar* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fclose_nolock(jitter):
    """
    [RET_EOF] _fclose_nolock(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fflush_nolock(jitter):
    """
    [RET_EOF] _fflush_nolock(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fgetwc_nolock(jitter):
    """
    [RET_WEOF] _fgetwc_nolock(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fread_nolock(jitter):
    """
    size_t _fread_nolock(
        void* buffer,
        size_t size,
        size_t count,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "size", "count", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fseek_nolock(jitter):
    """
    int _fseek_nolock(
        FILE* stream,
        long offset,
        [SEEK_TYPE] origin
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "offset", "origin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fseeki64_nolock(jitter):
    """
    int _fseeki64_nolock(
        FILE* stream,
        __int64 offset,
        [SEEK_TYPE] origin
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream", "offset", "origin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftell_nolock(jitter):
    """
    long _ftell_nolock(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftelli64_nolock(jitter):
    """
    __int64 _ftelli64_nolock(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwrite_nolock(jitter):
    """
    size_t _fwrite_nolock(
        const void* buffer,
        size_t size,
        size_t count,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "size", "count", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getc_nolock(jitter):
    """
    [RET_EOF] _getc_nolock(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getch_nolock(jitter):
    """
    int _getch_nolock()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getwch_nolock(jitter):
    """
    wint_t _getwch_nolock()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getche_nolock(jitter):
    """
    int _getche_nolock()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getwche_nolock(jitter):
    """
    wint_t _getwche_nolock()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdcwd_nolock(jitter):
    """
    char* _getdcwd_nolock(
        int drive,
        char* buffer,
        int maxlen
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["drive", "buffer", "maxlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetdcwd_nolock(jitter):
    """
    wchar_t* _wgetdcwd_nolock(
        int drive,
        wchar_t* buffer,
        int maxlen
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["drive", "buffer", "maxlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putch_nolock(jitter):
    """
    [RET_EOF] _putch_nolock(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putwch_nolock(jitter):
    """
    [RET_WEOF] _putwch_nolock(
        wchar_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ungetc_nolock(jitter):
    """
    [RET_EOF] _ungetc_nolock(
        int c,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ungetwc_nolock(jitter):
    """
    [RET_WEOF] _ungetwc_nolock(
        wint_t c,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ungetch_nolock(jitter):
    """
    [RET_EOF] _ungetch_nolock(
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ungetwch_nolock(jitter):
    """
    [RET_WEOF] _ungetwch_nolock(
        wint_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fputwc_nolock(jitter):
    """
    [RET_WEOF] _fputwc_nolock(
        wchar_t c,
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_setlocale(jitter):
    """
    char* setlocale(
        [locale_category] category,
        const char* locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["category", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsetlocale(jitter):
    """
    wchar_t* _wsetlocale(
        [locale_category] category,
        const wchar_t* locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["category", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__create_locale(jitter):
    """
    _locale_t _create_locale(
        [locale_category] category,
        const char* locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["category", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___create_locale(jitter):
    """
    _locale_t __create_locale(
        [locale_category] category,
        const char* locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["category", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__free_locale(jitter):
    """
    void _free_locale(
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___free_locale(jitter):
    """
    void __free_locale(
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_current_locale(jitter):
    """
    _locale_t _get_current_locale()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___get_current_locale(jitter):
    """
    _locale_t __get_current_locale()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__configthreadlocale(jitter):
    """
    [thread_locale_type] _configthreadlocale(
        [thread_locale_type] type
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_localeconv(jitter):
    """
    struct lconv* localeconv()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbccpy(jitter):
    """
    void _mbccpy(
        unsigned char* dest,
        const unsigned char* src
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "src"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbccpy_l(jitter):
    """
    void _mbccpy_l(
        unsigned char* dest,
        const unsigned char* src,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "src", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbccpy_s(jitter):
    """
    errno_t _mbccpy_s(
        unsigned char* dest,
        size_t buffSizeInBytes,
        int* pCopied,
        const unsigned char* src
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "buffSizeInBytes", "pCopied", "src"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbccpy_s_l(jitter):
    """
    errno_t _mbccpy_s_l(
        unsigned char* dest,
        size_t buffSizeInBytes,
        int* pCopied,
        const unsigned char* src,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "buffSizeInBytes", "pCopied", "src", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getmbcp(jitter):
    """
    int _getmbcp()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__setmbcp(jitter):
    """
    int _setmbcp(
        [_MB_CP_TYPE] codepage
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["codepage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx____mb_cur_max_func(jitter):
    """
    int ___mb_cur_max_func()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___mb_cur_max(jitter):
    """
    int __mb_cur_max()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx____lc_codepage_func(jitter):
    """
    UINT ___lc_codepage_func()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx____lc_handle_func(jitter):
    """
    LCID* ___lc_handle_func()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___crtLCMapStringW(jitter):
    """
    int __crtLCMapStringW(
        LCID Locale,
        [LocaleMappingFlags] dwMapFlags,
        LPCWSTR lpSrcStr,
        int cchSrc,
        LPWSTR lpDestStr,
        int cchDest
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["Locale", "dwMapFlags", "lpSrcStr", "cchSrc", "lpDestStr", "cchDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_calloc(jitter):
    """
    void* calloc(
        size_t num,
        size_t size
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["num", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??3@YAXPAX@Z(jitter):
    """
    void ??3@YAXPAX@Z(
        void* object
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??3@YAXPEAX@Z(jitter):
    """
    void ??3@YAXPEAX@Z(
        void* object
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??_V@YAXPAX@Z(jitter):
    """
    void ??_V@YAXPAX@Z(
        void* object
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??_V@YAXPEAX@Z(jitter):
    """
    void ??_V@YAXPEAX@Z(
        void* object
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__expand(jitter):
    """
    void* _expand(
        void* memblock,
        size_t size
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_free(jitter):
    """
    void free(
        void* memblock
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__freea(jitter):
    """
    void _freea(
        void* memblock
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_heap_handle(jitter):
    """
    intptr_t _get_heap_handle()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_sbh_threshold(jitter):
    """
    size_t _get_sbh_threshold()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__heapadd(jitter):
    """
    int _heapadd(
        void* memblock,
        size_t size
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__heapchk(jitter):
    """
    [HEAP_RESULT] _heapchk()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__heapmin(jitter):
    """
    int _heapmin()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__heapset(jitter):
    """
    [HEAP_RESULT] _heapset(
        unsigned int fill
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fill"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__heapwalk(jitter):
    """
    [HEAP_RESULT] _heapwalk(
        _HEAPINFO* entryinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["entryinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_malloc(jitter):
    """
    void* malloc(
        size_t size
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__msize(jitter):
    """
    size_t _msize(
        void* memblock
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??2@YAPAXI@Z(jitter):
    """
    void* ??2@YAPAXI@Z(
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??2@YAPEAX_K@Z(jitter):
    """
    void* ??2@YAPEAX_K@Z(
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??_U@YAPAXI@Z(jitter):
    """
    void* ??_U@YAPAXI@Z(
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??_U@YAPEAX_K@Z(jitter):
    """
    void* ??_U@YAPEAX_K@Z(
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?_query_new_handler@@YAP6AHI@ZXZ(jitter):
    """
    _PNH ?_query_new_handler@@YAP6AHI@ZXZ()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?_query_new_mode@@YAHXZ(jitter):
    """
    int ?_query_new_mode@@YAHXZ()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_realloc(jitter):
    """
    void* realloc(
        void* memblock,
        size_t size
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__callnewh(jitter):
    """
    int _callnewh(
        size_t size
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?_set_new_handler@@YAP6AHI@ZP6AHI@Z@Z(jitter):
    """
    _PNH ?_set_new_handler@@YAP6AHI@ZP6AHI@Z@Z(
        _PNH pNewHandler
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pNewHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?_set_new_mode@@YAHH@Z(jitter):
    """
    int ?_set_new_mode@@YAHH@Z(
        int newhandlermode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["newhandlermode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__expand_dbg(jitter):
    """
    void* _expand_dbg(
        void* userData,
        size_t newSize,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["userData", "newSize", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__calloc_dbg(jitter):
    """
    void* _calloc_dbg(
        size_t num,
        size_t size,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["num", "size", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__free_dbg(jitter):
    """
    void _free_dbg(
        void* userData,
        [DBG_BLOCK_TYPE] blockType
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["userData", "blockType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__malloc_dbg(jitter):
    """
    void* _malloc_dbg(
        size_t size,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["size", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__msize_dbg(jitter):
    """
    size_t _msize_dbg(
        void* userData,
        [DBG_BLOCK_TYPE] blockType
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["userData", "blockType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__realloc_dbg(jitter):
    """
    void* _realloc_dbg(
        void* userData,
        size_t newSize,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["userData", "newSize", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__recalloc(jitter):
    """
    void* _recalloc(
        void* memblock,
        size_t size
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__recalloc_dbg(jitter):
    """
    void* _recalloc_dbg(
        void* userData,
        size_t num,
        size_t size,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["userData", "num", "size", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_amblksiz(jitter):
    """
    errno_t _get_amblksiz(
        size_t* blockSize
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["blockSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_amblksiz(jitter):
    """
    errno_t _set_amblksiz(
        size_t blockSize
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["blockSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_sbh_threshold(jitter):
    """
    int _set_sbh_threshold(
        size_t size
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_abort(jitter):
    """
    void abort()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atexit(jitter):
    """
    int atexit(
        void* func
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["func"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__beginthread(jitter):
    """
    uintptr_t _beginthread(
        void* start_address,
        unsigned stack_size,
        void* arglist
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["start_address", "stack_size", "arglist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__beginthreadex(jitter):
    """
    uintptr_t _beginthreadex(
        void* security,
        unsigned stack_size,
        void* start_address,
        void* arglist,
        [thread_initflag] initflag,
        unsigned* thrdaddr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["security", "stack_size", "start_address", "arglist", "initflag", "thrdaddr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cexit(jitter):
    """
    void _cexit()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__c_exit(jitter):
    """
    void _c_exit()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwait(jitter):
    """
    intptr_t _cwait(
        int* termstat,
        intptr_t procHandle,
        int action
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["termstat", "procHandle", "action"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__endthread(jitter):
    """
    void _endthread()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__endthreadex(jitter):
    """
    void _endthreadex(
        unsigned retval
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["retval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execl(jitter):
    """
    intptr_t _execl(
        const char* cmdname,
        const char* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexecl(jitter):
    """
    intptr_t _wexecl(
        const wchar_t* cmdname,
        const wchar_t* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execle(jitter):
    """
    intptr_t _execle(
        const char* cmdname,
        const char* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexecle(jitter):
    """
    intptr_t _wexecle(
        const wchar_t* cmdname,
        const wchar_t* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execlp(jitter):
    """
    intptr_t _execlp(
        const char* cmdname,
        const char* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexeclp(jitter):
    """
    intptr_t _wexeclp(
        const wchar_t* cmdname,
        const wchar_t* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execlpe(jitter):
    """
    intptr_t _execlpe(
        const char* cmdname,
        const char* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexeclpe(jitter):
    """
    intptr_t _wexeclpe(
        const wchar_t* cmdname,
        const wchar_t* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execv(jitter):
    """
    intptr_t _execv(
        const char* cmdname,
        const char** argv
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexecv(jitter):
    """
    intptr_t _wexecv(
        const wchar_t* cmdname,
        const wchar_t** argv
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execve(jitter):
    """
    intptr_t _execve(
        const char* cmdname,
        const char** argv,
        const char** envp
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexecve(jitter):
    """
    intptr_t _wexecve(
        const wchar_t* cmdname,
        const wchar_t** argv,
        const wchar_t** envp
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execvp(jitter):
    """
    intptr_t _execvp(
        const char* cmdname,
        const char** argv
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexecvp(jitter):
    """
    intptr_t _wexecvp(
        const wchar_t* cmdname,
        const wchar_t** argv
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execvpe(jitter):
    """
    intptr_t _execvpe(
        const char* cmdname,
        const char** argv,
        const char** envp
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexecvpe(jitter):
    """
    intptr_t _wexecvpe(
        const wchar_t* cmdname,
        const wchar_t** argv,
        const wchar_t** envp
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_exit(jitter):
    """
    void exit(
        int status
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__exit(jitter):
    """
    void _exit(
        int status
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_getenv(jitter):
    """
    char* getenv(
        const char* varname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["varname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetenv(jitter):
    """
    wchar_t* _wgetenv(
        const wchar_t* varname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["varname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_getenv_s(jitter):
    """
    errno_t getenv_s(
        size_t* pReturnValue,
        char* buffer,
        size_t numberOfElements,
        const char* varname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "buffer", "numberOfElements", "varname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetenv_s(jitter):
    """
    errno_t _wgetenv_s(
        size_t* pReturnValue,
        wchar_t* buffer,
        size_t numberOfElements,
        const wchar_t* varname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "buffer", "numberOfElements", "varname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getpid(jitter):
    """
    int _getpid()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__onexit(jitter):
    """
    _onexit_t _onexit(
        _onexit_t function
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["function"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__pclose(jitter):
    """
    int _pclose(
        FILE* stream
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_perror(jitter):
    """
    void perror(
        const char* string
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wperror(jitter):
    """
    void _wperror(
        const wchar_t* string
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__pipe(jitter):
    """
    int _pipe(
        int* pfds,
        unsigned int psize,
        [open_flag] textmode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pfds", "psize", "textmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__popen(jitter):
    """
    FILE* _popen(
        const char* command,
        const char* mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["command", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wpopen(jitter):
    """
    FILE* _wpopen(
        const wchar_t* command,
        const wchar_t* mode
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["command", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putenv(jitter):
    """
    int _putenv(
        const char* envstring
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["envstring"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wputenv(jitter):
    """
    int _wputenv(
        const wchar_t* envstring
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["envstring"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putenv_s(jitter):
    """
    errno_t _putenv_s(
        const char* name,
        const char* value
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["name", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wputenv_s(jitter):
    """
    errno_t _wputenv_s(
        const wchar_t* name,
        const wchar_t* value
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["name", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_raise(jitter):
    """
    int raise(
        [SIGNAL] sig
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["sig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_signal(jitter):
    """
    [SIGNAL_FUNC] signal(
        [SIGNAL] sig,
        [SIGNAL_FUNC] func
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["sig", "func"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnl(jitter):
    """
    intptr_t _spawnl(
        [spawn_mode] mode,
        const char* cmdname,
        const char* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnl(jitter):
    """
    intptr_t _wspawnl(
        [spawn_mode] mode,
        const wchar_t* cmdname,
        const wchar_t* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnle(jitter):
    """
    intptr_t _spawnle(
        [spawn_mode] mode,
        const char* cmdname,
        const char* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnle(jitter):
    """
    intptr_t _wspawnle(
        [spawn_mode] mode,
        const wchar_t* cmdname,
        const wchar_t* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnlp(jitter):
    """
    intptr_t _spawnlp(
        [spawn_mode] mode,
        const char* cmdname,
        const char* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnlp(jitter):
    """
    intptr_t _wspawnlp(
        [spawn_mode] mode,
        const wchar_t* cmdname,
        const wchar_t* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnlpe(jitter):
    """
    intptr_t _spawnlpe(
        [spawn_mode] mode,
        const char* cmdname,
        const char* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnlpe(jitter):
    """
    intptr_t _wspawnlpe(
        [spawn_mode] mode,
        const wchar_t* cmdname,
        const wchar_t* args,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnv(jitter):
    """
    intptr_t _spawnv(
        [spawn_mode] mode,
        const char* cmdname,
        const char** argv
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnv(jitter):
    """
    intptr_t _wspawnv(
        [spawn_mode] mode,
        const wchar_t* cmdname,
        const wchar_t** argv
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnve(jitter):
    """
    intptr_t _spawnve(
        [spawn_mode] mode,
        const char* cmdname,
        const char** argv,
        const char** envp
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnve(jitter):
    """
    intptr_t _wspawnve(
        [spawn_mode] mode,
        const wchar_t* cmdname,
        const wchar_t** argv,
        const wchar_t** envp
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnvp(jitter):
    """
    intptr_t _spawnvp(
        [spawn_mode] mode,
        const char* cmdname,
        const char** argv
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnvp(jitter):
    """
    intptr_t _wspawnvp(
        [spawn_mode] mode,
        const wchar_t* cmdname,
        const wchar_t** argv
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnvpe(jitter):
    """
    intptr_t _spawnvpe(
        [spawn_mode] mode,
        const char* cmdname,
        const char** argv,
        const char** envp
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnvpe(jitter):
    """
    intptr_t _wspawnvpe(
        [spawn_mode] mode,
        const wchar_t* cmdname,
        const wchar_t** argv,
        const wchar_t** envp
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_system(jitter):
    """
    int system(
        const char* command
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsystem(jitter):
    """
    int _wsystem(
        const wchar_t* command
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__dupenv_s(jitter):
    """
    errno_t _dupenv_s(
        char** buffer,
        size_t* numberOfElements,
        const char* varname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "varname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wdupenv_s(jitter):
    """
    errno_t _wdupenv_s(
        wchar_t** buffer,
        size_t* numberOfElements,
        const wchar_t* varname
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "varname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__dupenv_s_dbg(jitter):
    """
    errno_t _dupenv_s_dbg(
        char** buffer,
        size_t* numberOfElements,
        const char* varname,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "varname", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wdupenv_s_dbg(jitter):
    """
    errno_t _wdupenv_s_dbg(
        wchar_t** buffer,
        size_t* numberOfElements,
        const wchar_t* varname,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "varname", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___getmainargs(jitter):
    """
    int __getmainargs(
        int* _Argc,
        char*** _Argv,
        char*** _Env,
        int _DoWildCard,
        _startupinfo* _StartInfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["_Argc", "_Argv", "_Env", "_DoWildCard", "_StartInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___wgetmainargs(jitter):
    """
    int __wgetmainargs(
        int* _Argc,
        wchar_t*** _Argv,
        wchar_t*** _Env,
        int _DoWildCard,
        _startupinfo* _StartInfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["_Argc", "_Argv", "_Env", "_DoWildCard", "_StartInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_pgmptr(jitter):
    """
    errno_t _get_pgmptr(
        char** pValue
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_wpgmptr(jitter):
    """
    errno_t _get_wpgmptr(
        wchar_t** pValue
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_fileinfo(jitter):
    """
    errno_t _get_fileinfo(
        int* pFileInfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pFileInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_fileinfo(jitter):
    """
    errno_t _set_fileinfo(
        int value
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___set_app_type(jitter):
    """
    void __set_app_type(
        [C_APP_TYPE] at
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["at"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___dllonexit(jitter):
    """
    _onexit_t __dllonexit(
        _onexit_t func,
        _PVFV** pbegin,
        _PVFV** pend
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["func", "pbegin", "pend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sleep(jitter):
    """
    void _sleep(
        unsigned long duration
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["duration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__loaddll(jitter):
    """
    intptr_t _loaddll(
        char* filename
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__unloaddll(jitter):
    """
    int _unloaddll(
        intptr_t handle
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdllprocaddr(jitter):
    """
    void* _getdllprocaddr(
        intptr_t handle,
        char* procedureName,
        intptr_t ordinal
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle", "procedureName", "ordinal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_bsearch(jitter):
    """
    void* bsearch(
        const void* key,
        const void* base,
        size_t num,
        size_t width,
        [compare_function] compare
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["key", "base", "num", "width", "compare"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_bsearch_s(jitter):
    """
    void* bsearch_s(
        const void* key,
        const void* base,
        size_t num,
        size_t width,
        [compare_s_function] compare,
        void* context
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["key", "base", "num", "width", "compare", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lfind(jitter):
    """
    void* _lfind(
        const void* key,
        const void* base,
        unsigned int* num,
        unsigned int width,
        [compare_function] compare
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["key", "base", "num", "width", "compare"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lfind_s(jitter):
    """
    void* _lfind_s(
        const void* key,
        const void* base,
        unsigned int* num,
        size_t size,
        [compare_s_function] compare,
        void* context
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["key", "base", "num", "size", "compare", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lsearch(jitter):
    """
    void* _lsearch(
        const void* key,
        void* base,
        unsigned int* num,
        unsigned int width,
        [compare_function] compare
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["key", "base", "num", "width", "compare"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lsearch_s(jitter):
    """
    void* _lsearch_s(
        const void* key,
        void* base,
        unsigned int* num,
        size_t size,
        [compare_s_function] compare,
        void* context
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["key", "base", "num", "size", "compare", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_qsort(jitter):
    """
    void qsort(
        void* base,
        size_t num,
        size_t width,
        [compare_s_function] compare
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["base", "num", "width", "compare"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_qsort_s(jitter):
    """
    void qsort_s(
        void* base,
        size_t num,
        size_t width,
        [compare_s_function] compare,
        void* context
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["base", "num", "width", "compare", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsdec(jitter):
    """
    unsigned char* _mbsdec(
        const unsigned char* start,
        const unsigned char* current
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["start", "current"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsdec_l(jitter):
    """
    unsigned char* _mbsdec_l(
        const unsigned char* start,
        const unsigned char* current,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["start", "current", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsinc(jitter):
    """
    unsigned char* _mbsinc(
        const unsigned char* current
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["current"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsinc_l(jitter):
    """
    unsigned char* _mbsinc_l(
        const unsigned char* current,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["current", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcat(jitter):
    """
    unsigned char* _mbsnbcat(
        unsigned char* dest,
        const unsigned char* src,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcat_l(jitter):
    """
    unsigned char* _mbsnbcat_l(
        unsigned char* dest,
        const unsigned char* src,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "src", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcat_s(jitter):
    """
    errno_t _mbsnbcat_s(
        unsigned char* dest,
        size_t sizeInBytes,
        const unsigned char* src,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "sizeInBytes", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcat_s_l(jitter):
    """
    errno_t _mbsnbcat_s_l(
        unsigned char* dest,
        size_t sizeInBytes,
        const unsigned char* src,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["dest", "sizeInBytes", "src", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcmp(jitter):
    """
    [_NLSCMPERROR] _mbsnbcmp(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcmp_l(jitter):
    """
    [_NLSCMPERROR] _mbsnbcmp_l(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcnt(jitter):
    """
    size_t _mbsnbcnt(
        const unsigned char* str,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcnt_l(jitter):
    """
    size_t _mbsnbcnt_l(
        const unsigned char* str,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnccnt(jitter):
    """
    size_t _mbsnccnt(
        const unsigned char* str,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnccnt_l(jitter):
    """
    size_t _mbsnccnt_l(
        const unsigned char* str,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___strncnt(jitter):
    """
    size_t __strncnt(
        const char* str,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___wcsncnt(jitter):
    """
    size_t __wcsncnt(
        const wchar_t* str,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcpy(jitter):
    """
    unsigned char* _mbsnbcpy(
        unsigned char* strDest,
        const unsigned char* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcpy_l(jitter):
    """
    unsigned char* _mbsnbcpy_l(
        unsigned char* strDest,
        const unsigned char* strSource,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcpy_s(jitter):
    """
    errno_t _mbsnbcpy_s(
        unsigned char* strDest,
        size_t sizeInBytes,
        const unsigned char* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "sizeInBytes", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcpy_s_l(jitter):
    """
    errno_t _mbsnbcpy_s_l(
        unsigned char* strDest,
        size_t sizeInBytes,
        const unsigned char* strSource,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "sizeInBytes", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbicmp(jitter):
    """
    [_NLSCMPERROR] _mbsnbicmp(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbset(jitter):
    """
    unsigned char* _mbsnbset(
        unsigned char* str,
        unsigned int c,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbset_l(jitter):
    """
    unsigned char* _mbsnbset_l(
        unsigned char* str,
        unsigned int c,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnextc(jitter):
    """
    unsigned int _mbsnextc(
        const unsigned char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnextc_l(jitter):
    """
    unsigned int _mbsnextc_l(
        const unsigned char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsninc(jitter):
    """
    unsigned char* _mbsninc(
        const unsigned char* str,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsninc_l(jitter):
    """
    unsigned char* _mbsninc_l(
        const unsigned char* str,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsspnp(jitter):
    """
    unsigned char* _mbsspnp(
        const unsigned char* str,
        const unsigned char* charset
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "charset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsspnp_l(jitter):
    """
    unsigned char* _mbsspnp_l(
        const unsigned char* str,
        const unsigned char* charset,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "charset", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scprintf(jitter):
    """
    int _scprintf(
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scprintf_l(jitter):
    """
    int _scprintf_l(
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scwprintf(jitter):
    """
    int _scwprintf(
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scwprintf_l(jitter):
    """
    int _scwprintf_l(
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snscanf(jitter):
    """
    [RET_EOF] _snscanf(
        const char* input,
        size_t length,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snscanf_l(jitter):
    """
    [RET_EOF] _snscanf_l(
        const char* input,
        size_t length,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwscanf(jitter):
    """
    [RET_EOF] _snwscanf(
        const wchar_t* input,
        size_t length,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwscanf_l(jitter):
    """
    [RET_EOF] _snwscanf_l(
        const wchar_t* input,
        size_t length,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sscanf(jitter):
    """
    [RET_EOF] sscanf(
        const char* buffer,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sscanf_l(jitter):
    """
    [RET_EOF] _sscanf_l(
        const char* buffer,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_swscanf(jitter):
    """
    [RET_EOF] swscanf(
        const wchar_t* buffer,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swscanf_l(jitter):
    """
    [RET_EOF] _swscanf_l(
        const wchar_t* buffer,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sprintf(jitter):
    """
    int sprintf(
        char* buffer,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sprintf_l(jitter):
    """
    int _sprintf_l(
        char* buffer,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_swprintf(jitter):
    """
    int swprintf(
        wchar_t* buffer,
        size_t count,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swprintf(jitter):
    """
    int _swprintf(
        wchar_t* buffer,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___swprintf_l(jitter):
    """
    int __swprintf_l(
        wchar_t* buffer,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sprintf_p(jitter):
    """
    int _sprintf_p(
        char* buffer,
        size_t sizeOfBuffer,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sprintf_p_l(jitter):
    """
    int _sprintf_p_l(
        char* buffer,
        size_t sizeOfBuffer,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swprintf_p(jitter):
    """
    int _swprintf_p(
        wchar_t* buffer,
        size_t sizeOfBuffer,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swprintf_p_l(jitter):
    """
    int _swprintf_p_l(
        wchar_t* buffer,
        size_t sizeOfBuffer,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcat(jitter):
    """
    char* strcat(
        char* strDestination,
        const char* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscat(jitter):
    """
    wchar_t* wcscat(
        wchar_t* strDestination,
        const wchar_t* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscat(jitter):
    """
    unsigned char* _mbscat(
        unsigned char* strDestination,
        const unsigned char* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcat_s(jitter):
    """
    errno_t strcat_s(
        char* strDestination,
        size_t numberOfElements,
        const char* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "numberOfElements", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscat_s(jitter):
    """
    errno_t wcscat_s(
        wchar_t* strDestination,
        size_t numberOfElements,
        const wchar_t* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "numberOfElements", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscat_s(jitter):
    """
    errno_t _mbscat_s(
        unsigned char* strDestination,
        size_t numberOfElements,
        const unsigned char* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "numberOfElements", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strchr(jitter):
    """
    char* strchr(
        const char* str,
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcschr(jitter):
    """
    wchar_t* wcschr(
        const wchar_t* str,
        wchar_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbschr(jitter):
    """
    unsigned char* _mbschr(
        const unsigned char* str,
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbschr_l(jitter):
    """
    unsigned char* _mbschr_l(
        const unsigned char* str,
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcmp(jitter):
    """
    int strcmp(
        const char* string1,
        const char* string2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscmp(jitter):
    """
    int wcscmp(
        const wchar_t* string1,
        const wchar_t* string2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscmp(jitter):
    """
    [_NLSCMPERROR] _mbscmp(
        const unsigned char* string1,
        const unsigned char* string2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcpy(jitter):
    """
    char* strcpy(
        char* strDestination,
        const char* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscpy(jitter):
    """
    wchar_t* wcscpy(
        wchar_t* strDestination,
        const wchar_t* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscpy(jitter):
    """
    unsigned char* _mbscpy(
        unsigned char* strDestination,
        const unsigned char* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcpy_s(jitter):
    """
    errno_t strcpy_s(
        char* strDestination,
        size_t numberOfElements,
        const char* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "numberOfElements", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscpy_s(jitter):
    """
    errno_t wcscpy_s(
        wchar_t* strDestination,
        size_t numberOfElements,
        const wchar_t* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "numberOfElements", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscpy_s(jitter):
    """
    errno_t _mbscpy_s(
        unsigned char* strDestination,
        size_t numberOfElements,
        const unsigned char* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "numberOfElements", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcspn(jitter):
    """
    size_t strcspn(
        const char* str,
        const char* strCharSet
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscspn(jitter):
    """
    size_t wcscspn(
        const wchar_t* str,
        const wchar_t* strCharSet
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscspn(jitter):
    """
    size_t _mbscspn(
        const unsigned char* str,
        const unsigned char* strCharSet
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscspn_l(jitter):
    """
    size_t _mbscspn_l(
        const unsigned char* str,
        const unsigned char* strCharSet,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strdup(jitter):
    """
    char* _strdup(
        const char* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsdup(jitter):
    """
    wchar_t* _wcsdup(
        const wchar_t* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsdup(jitter):
    """
    unsigned char* _mbsdup(
        const unsigned char* strSource
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strerror(jitter):
    """
    char* strerror(
        int errnum
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["errnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strerror(jitter):
    """
    char* _strerror(
        const char* strErrMsg
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strErrMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcserror(jitter):
    """
    wchar_t* _wcserror(
        int errnum
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["errnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___wcserror(jitter):
    """
    wchar_t* __wcserror(
        const wchar_t* strErrMsg
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strErrMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strerror_s(jitter):
    """
    errno_t strerror_s(
        char* buffer,
        size_t numberOfElements,
        int errnum
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "errnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strerror_s(jitter):
    """
    errno_t _strerror_s(
        char* buffer,
        size_t numberOfElements,
        const char* strErrMsg
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "strErrMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcserror_s(jitter):
    """
    errno_t _wcserror_s(
        wchar_t* buffer,
        size_t numberOfElements,
        int errnum
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "errnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___wcserror_s(jitter):
    """
    errno_t __wcserror_s(
        wchar_t* buffer,
        size_t numberOfElements,
        const wchar_t* strErrMsg
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "strErrMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strnlen(jitter):
    """
    size_t strnlen(
        const char* str,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsnlen(jitter):
    """
    size_t wcsnlen(
        const wchar_t* str,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnlen(jitter):
    """
    size_t _mbsnlen(
        const unsigned char* str,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnlen_l(jitter):
    """
    size_t _mbsnlen_l(
        const unsigned char* str,
        size_t numberOfElements,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstrnlen(jitter):
    """
    size_t _mbstrnlen(
        const char* str,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstrnlen_l(jitter):
    """
    size_t _mbstrnlen_l(
        const char* str,
        size_t numberOfElements,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strlwr(jitter):
    """
    char* _strlwr(
        char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcslwr(jitter):
    """
    wchar_t* _wcslwr(
        wchar_t* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbslwr(jitter):
    """
    unsigned char* _mbslwr(
        unsigned char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strlwr_l(jitter):
    """
    char* _strlwr_l(
        char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcslwr_l(jitter):
    """
    wchar_t* _wcslwr_l(
        wchar_t* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbslwr_l(jitter):
    """
    unsigned char* _mbslwr_l(
        unsigned char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strncat(jitter):
    """
    char* strncat(
        char* strDest,
        const char* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsncat(jitter):
    """
    wchar_t* wcsncat(
        wchar_t* strDest,
        const wchar_t* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncat(jitter):
    """
    unsigned char* _mbsncat(
        unsigned char* strDest,
        const unsigned char* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncat_l(jitter):
    """
    unsigned char* _mbsncat_l(
        unsigned char* strDest,
        const unsigned char* strSource,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strncat_s(jitter):
    """
    errno_t strncat_s(
        char* strDest,
        size_t numberOfElements,
        const char* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsncat_s(jitter):
    """
    errno_t wcsncat_s(
        wchar_t* strDest,
        size_t numberOfElements,
        const wchar_t* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncat_s(jitter):
    """
    errno_t _mbsncat_s(
        unsigned char* strDest,
        size_t numberOfElements,
        const unsigned char* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncat_s_l(jitter):
    """
    errno_t _mbsncat_s_l(
        unsigned char* strDest,
        size_t numberOfElements,
        const unsigned char* strSource,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strncmp(jitter):
    """
    int strncmp(
        const char* string1,
        const char* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsncmp(jitter):
    """
    int wcsncmp(
        const wchar_t* string1,
        const wchar_t* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncmp(jitter):
    """
    [_NLSCMPERROR] _mbsncmp(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncmp_l(jitter):
    """
    [_NLSCMPERROR] _mbsncmp_l(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strncpy(jitter):
    """
    char* strncpy(
        char* strDest,
        const char* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsncpy(jitter):
    """
    wchar_t* wcsncpy(
        wchar_t* strDest,
        const wchar_t* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncpy(jitter):
    """
    unsigned char* _mbsncpy(
        unsigned char* strDest,
        const unsigned char* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncpy_l(jitter):
    """
    unsigned char* _mbsncpy_l(
        unsigned char* strDest,
        const unsigned char* strSource,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strncpy_s(jitter):
    """
    errno_t strncpy_s(
        char* strDest,
        size_t numberOfElements,
        const char* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsncpy_s(jitter):
    """
    errno_t wcsncpy_s(
        wchar_t* strDest,
        size_t numberOfElements,
        const wchar_t* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncpy_s(jitter):
    """
    errno_t _mbsncpy_s(
        unsigned char* strDest,
        size_t numberOfElements,
        const unsigned char* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncpy_s_l(jitter):
    """
    errno_t _mbsncpy_s_l(
        unsigned char* strDest,
        size_t numberOfElements,
        const unsigned char* strSource,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strnset(jitter):
    """
    char* _strnset(
        char* str,
        int c,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsnset(jitter):
    """
    wchar_t* _wcsnset(
        wchar_t* str,
        wchar_t c,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnset(jitter):
    """
    unsigned char* _mbsnset(
        unsigned char* str,
        unsigned int c,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnset_l(jitter):
    """
    unsigned char* _mbsnset_l(
        unsigned char* str,
        unsigned int c,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strpbrk(jitter):
    """
    char* strpbrk(
        const char* str,
        const char* strCharSet
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcspbrk(jitter):
    """
    wchar_t* wcspbrk(
        const wchar_t* str,
        const wchar_t* strCharSet
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbspbrk(jitter):
    """
    unsigned char* _mbspbrk(
        const unsigned char* str,
        const unsigned char* strCharSet
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbspbrk_l(jitter):
    """
    unsigned char* _mbspbrk_l(
        const unsigned char* str,
        const unsigned char* strCharSet,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strrchr(jitter):
    """
    char* strrchr(
        const char* str,
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsrchr(jitter):
    """
    wchar_t* wcsrchr(
        const wchar_t* str,
        wchar_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsrchr(jitter):
    """
    unsigned char* _mbsrchr(
        const unsigned char* str,
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsrchr_l(jitter):
    """
    unsigned char* _mbsrchr_l(
        const unsigned char* str,
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strrev(jitter):
    """
    char* _strrev(
        char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsrev(jitter):
    """
    wchar_t* _wcsrev(
        wchar_t* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsrev(jitter):
    """
    unsigned char* _mbsrev(
        unsigned char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsrev_l(jitter):
    """
    unsigned char* _mbsrev_l(
        unsigned char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strset(jitter):
    """
    char* _strset(
        char* str,
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsset(jitter):
    """
    wchar_t* _wcsset(
        wchar_t* str,
        wchar_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsset(jitter):
    """
    unsigned char* _mbsset(
        unsigned char* str,
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsset_l(jitter):
    """
    unsigned char* _mbsset_l(
        unsigned char* str,
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strspn(jitter):
    """
    size_t strspn(
        const char* str,
        const char* strCharSet
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsspn(jitter):
    """
    size_t wcsspn(
        const wchar_t* str,
        const wchar_t* strCharSet
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsspn(jitter):
    """
    size_t _mbsspn(
        const unsigned char* str,
        const unsigned char* strCharSet
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsspn_l(jitter):
    """
    size_t _mbsspn_l(
        const unsigned char* str,
        const unsigned char* strCharSet,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strstr(jitter):
    """
    char* strstr(
        const char* str,
        const char* strSearch
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strSearch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsstr(jitter):
    """
    wchar_t* wcsstr(
        const wchar_t* str,
        const wchar_t* strSearch
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strSearch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsstr(jitter):
    """
    unsigned char* _mbsstr(
        const unsigned char* str,
        const unsigned char* strSearch
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strSearch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsstr_l(jitter):
    """
    unsigned char* _mbsstr_l(
        const unsigned char* str,
        const unsigned char* strSearch,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "strSearch", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strtok(jitter):
    """
    char* strtok(
        char* strToken,
        const char* strDelimit
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstok(jitter):
    """
    wchar_t* wcstok(
        wchar_t* strToken,
        const wchar_t* strDelimit
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstok(jitter):
    """
    unsigned char* _mbstok(
        unsigned char* strToken,
        const unsigned char* strDelimit
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstok_l(jitter):
    """
    unsigned char* _mbstok_l(
        unsigned char* strToken,
        const unsigned char* strDelimit,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strtok_s(jitter):
    """
    char* strtok_s(
        char* strToken,
        const char* strDelimit,
        char** context
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstok_s(jitter):
    """
    wchar_t* wcstok_s(
        wchar_t* strToken,
        const wchar_t* strDelimit,
        wchar_t** context
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstok_s(jitter):
    """
    unsigned char* _mbstok_s(
        unsigned char* strToken,
        const unsigned char* strDelimit,
        char** context
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstok_s_l(jitter):
    """
    unsigned char* _mbstok_s_l(
        unsigned char* strToken,
        const unsigned char* strDelimit,
        char** context,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit", "context", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strupr(jitter):
    """
    char* _strupr(
        char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsupr(jitter):
    """
    wchar_t* _wcsupr(
        wchar_t* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsupr(jitter):
    """
    unsigned char* _mbsupr(
        unsigned char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strupr_l(jitter):
    """
    char* _strupr_l(
        char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsupr_l(jitter):
    """
    wchar_t* _wcsupr_l(
        wchar_t* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsupr_l(jitter):
    """
    unsigned char* _mbsupr_l(
        unsigned char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vsprintf(jitter):
    """
    int vsprintf(
        char* buffer,
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsprintf_l(jitter):
    """
    int _vsprintf_l(
        char* buffer,
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vswprintf(jitter):
    """
    int vswprintf(
        wchar_t* buffer,
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vswprintf(jitter):
    """
    int _vswprintf(
        wchar_t* buffer,
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vswprintf_l(jitter):
    """
    int _vswprintf_l(
        wchar_t* buffer,
        size_t count,
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___vswprintf_l(jitter):
    """
    int __vswprintf_l(
        wchar_t* buffer,
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsprintf_p(jitter):
    """
    int _vsprintf_p(
        char* buffer,
        size_t sizeInBytes,
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeInBytes", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsprintf_p_l(jitter):
    """
    int _vsprintf_p_l(
        char* buffer,
        size_t sizeInBytes,
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeInBytes", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vswprintf_p(jitter):
    """
    int _vswprintf_p(
        wchar_t* buffer,
        size_t count,
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vswprintf_p_l(jitter):
    """
    int _vswprintf_p_l(
        wchar_t* buffer,
        size_t count,
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vsnprintf(jitter):
    """
    int vsnprintf(
        char* buffer,
        size_t count,
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnprintf(jitter):
    """
    int _vsnprintf(
        char* buffer,
        size_t count,
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnprintf_l(jitter):
    """
    int _vsnprintf_l(
        char* buffer,
        size_t count,
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnwprintf(jitter):
    """
    int _vsnwprintf(
        wchar_t* buffer,
        size_t count,
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnwprintf_l(jitter):
    """
    int _vsnwprintf_l(
        wchar_t* buffer,
        size_t count,
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strlen(jitter):
    """
    size_t strlen(
        const char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbslen(jitter):
    """
    size_t _mbslen(
        const unsigned char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbslen_l(jitter):
    """
    size_t _mbslen_l(
        const unsigned char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstrlen(jitter):
    """
    size_t _mbstrlen(
        const char* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstrlen_l(jitter):
    """
    size_t _mbstrlen_l(
        const char* str,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcslen(jitter):
    """
    size_t wcslen(
        const wchar_t* str
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbclen(jitter):
    """
    size_t _mbclen(
        const unsigned char* c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mblen(jitter):
    """
    int mblen(
        const char* mbstr,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mblen_l(jitter):
    """
    int _mblen_l(
        const char* mbstr,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcoll(jitter):
    """
    [_NLSCMPERROR] strcoll(
        const char* string1,
        const char* string2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscoll(jitter):
    """
    [_NLSCMPERROR] wcscoll(
        const wchar_t* string1,
        const wchar_t* string2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscoll(jitter):
    """
    [_NLSCMPERROR] _mbscoll(
        const unsigned char* string1,
        const unsigned char* string2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strcoll_l(jitter):
    """
    [_NLSCMPERROR] _strcoll_l(
        const char* string1,
        const char* string2,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcscoll_l(jitter):
    """
    [_NLSCMPERROR] _wcscoll_l(
        const wchar_t* string1,
        const wchar_t* string2,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscoll_l(jitter):
    """
    [_NLSCMPERROR] _mbscoll_l(
        const unsigned char* string1,
        const unsigned char* string2,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stricoll(jitter):
    """
    [_NLSCMPERROR] _stricoll(
        const char* string1,
        const char* string2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsicoll(jitter):
    """
    [_NLSCMPERROR] _wcsicoll(
        const wchar_t* string1,
        const wchar_t* string2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsicoll(jitter):
    """
    [_NLSCMPERROR] _mbsicoll(
        const unsigned char* string1,
        const unsigned char* string2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stricoll_l(jitter):
    """
    [_NLSCMPERROR] _stricoll_l(
        const char* string1,
        const char* string2,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsicoll_l(jitter):
    """
    [_NLSCMPERROR] _wcsicoll_l(
        const wchar_t* string1,
        const wchar_t* string2,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsicoll_l(jitter):
    """
    [_NLSCMPERROR] _mbsicoll_l(
        const unsigned char* string1,
        const unsigned char* string2,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strncoll(jitter):
    """
    [_NLSCMPERROR] _strncoll(
        const char* string1,
        const char* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsncoll(jitter):
    """
    [_NLSCMPERROR] _wcsncoll(
        const wchar_t* string1,
        const wchar_t* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncoll(jitter):
    """
    [_NLSCMPERROR] _mbsncoll(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strncoll_l(jitter):
    """
    [_NLSCMPERROR] _strncoll_l(
        const char* string1,
        const char* string2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsncoll_l(jitter):
    """
    [_NLSCMPERROR] _wcsncoll_l(
        const wchar_t* string1,
        const wchar_t* string2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncoll_l(jitter):
    """
    [_NLSCMPERROR] _mbsncoll_l(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strnicoll(jitter):
    """
    [_NLSCMPERROR] _strnicoll(
        const char* string1,
        const char* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsnicoll(jitter):
    """
    [_NLSCMPERROR] _wcsnicoll(
        const wchar_t* string1,
        const wchar_t* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnicoll(jitter):
    """
    [_NLSCMPERROR] _mbsnicoll(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strnicoll_l(jitter):
    """
    [_NLSCMPERROR] _strnicoll_l(
        const char* string1,
        const char* string2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsnicoll_l(jitter):
    """
    [_NLSCMPERROR] _wcsnicoll_l(
        const wchar_t* string1,
        const wchar_t* string2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnicoll_l(jitter):
    """
    [_NLSCMPERROR] _mbsnicoll_l(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strcmpi(jitter):
    """
    [_NLSCMPERROR] _strcmpi(
        const char* string1,
        const char* string2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stricmp(jitter):
    """
    [_NLSCMPERROR] _stricmp(
        const char* string1,
        const char* string2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsicmp(jitter):
    """
    [_NLSCMPERROR] _wcsicmp(
        const wchar_t* string1,
        const wchar_t* string2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsicmp(jitter):
    """
    [_NLSCMPERROR] _mbsicmp(
        const unsigned char* string1,
        const unsigned char* string2
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stricmp_l(jitter):
    """
    [_NLSCMPERROR] _stricmp_l(
        const char* string1,
        const char* string2,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsicmp_l(jitter):
    """
    [_NLSCMPERROR] _wcsicmp_l(
        const wchar_t* string1,
        const wchar_t* string2,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsicmp_l(jitter):
    """
    [_NLSCMPERROR] _mbsicmp_l(
        const unsigned char* string1,
        const unsigned char* string2,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsnicmp_l(jitter):
    """
    [_NLSCMPERROR] _wcsnicmp_l(
        const wchar_t* string1,
        const wchar_t* string2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnicmp_l(jitter):
    """
    [_NLSCMPERROR] _mbsnicmp_l(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnicmp(jitter):
    """
    [_NLSCMPERROR] _mbsnicmp(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strnicmp_l(jitter):
    """
    [_NLSCMPERROR] _strnicmp_l(
        const char* string1,
        const char* string2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsnicmp(jitter):
    """
    [_NLSCMPERROR] _wcsnicmp(
        const wchar_t* string1,
        const wchar_t* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strnicmp(jitter):
    """
    [_NLSCMPERROR] _strnicmp(
        const char* string1,
        const char* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strupr_s(jitter):
    """
    errno_t _strupr_s(
        char* str,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsupr_s(jitter):
    """
    errno_t _wcsupr_s(
        wchar_t* str,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strupr_s_l(jitter):
    """
    errno_t _strupr_s_l(
        char* str,
        size_t numberOfElements,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsupr_s_l(jitter):
    """
    errno_t _wcsupr_s_l(
        wchar_t* str,
        size_t numberOfElements,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsupr_s(jitter):
    """
    errno_t _mbsupr_s(
        unsigned char* str,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsupr_s_l(jitter):
    """
    errno_t _mbsupr_s_l(
        unsigned char* str,
        size_t numberOfElements,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strlwr_s(jitter):
    """
    errno_t _strlwr_s(
        char* str,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strlwr_s_l(jitter):
    """
    errno_t _strlwr_s_l(
        char* str,
        size_t numberOfElements,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbslwr_s(jitter):
    """
    errno_t _mbslwr_s(
        unsigned char* str,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbslwr_s_l(jitter):
    """
    errno_t _mbslwr_s_l(
        unsigned char* str,
        size_t numberOfElements,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcslwr_s(jitter):
    """
    errno_t _wcslwr_s(
        wchar_t* str,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcslwr_s_l(jitter):
    """
    errno_t _wcslwr_s_l(
        wchar_t* str,
        size_t numberOfElements,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snscanf_s(jitter):
    """
    [RET_EOF] _snscanf_s(
        const char* input,
        size_t length,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snscanf_s_l(jitter):
    """
    [RET_EOF] _snscanf_s_l(
        const char* input,
        size_t length,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwscanf_s(jitter):
    """
    [RET_EOF] _snwscanf_s(
        const wchar_t* input,
        size_t length,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwscanf_s_l(jitter):
    """
    [RET_EOF] _snwscanf_s_l(
        const wchar_t* input,
        size_t length,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnprintf_s(jitter):
    """
    int _vsnprintf_s(
        char* buffer,
        size_t sizeOfBuffer,
        size_t count,
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnprintf_s_l(jitter):
    """
    int _vsnprintf_s_l(
        char* buffer,
        size_t sizeOfBuffer,
        size_t count,
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnwprintf_s(jitter):
    """
    int _vsnwprintf_s(
        wchar_t* buffer,
        size_t sizeOfBuffer,
        size_t count,
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnwprintf_s_l(jitter):
    """
    int _vsnwprintf_s_l(
        wchar_t* buffer,
        size_t sizeOfBuffer,
        size_t count,
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_swprintf_s(jitter):
    """
    int swprintf_s(
        wchar_t* buffer,
        size_t sizeOfBuffer,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swprintf_s_l(jitter):
    """
    int _swprintf_s_l(
        wchar_t* buffer,
        size_t sizeOfBuffer,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sprintf_s_l(jitter):
    """
    int _sprintf_s_l(
        char* buffer,
        size_t sizeOfBuffer,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sprintf_s(jitter):
    """
    int sprintf_s(
        char* buffer,
        size_t sizeOfBuffer,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swscanf_s_l(jitter):
    """
    [RET_EOF] _swscanf_s_l(
        const wchar_t* buffer,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_swscanf_s(jitter):
    """
    [RET_EOF] swscanf_s(
        const wchar_t* buffer,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sscanf_s_l(jitter):
    """
    [RET_EOF] _sscanf_s_l(
        const char* buffer,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sscanf_s(jitter):
    """
    [RET_EOF] sscanf_s(
        const char* buffer,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vswprintf_s(jitter):
    """
    int vswprintf_s(
        wchar_t* buffer,
        size_t numberOfElements,
        const wchar_t* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vswprintf_s_l(jitter):
    """
    int _vswprintf_s_l(
        wchar_t* buffer,
        size_t numberOfElements,
        const wchar_t* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsprintf_s_l(jitter):
    """
    int _vsprintf_s_l(
        char* buffer,
        size_t numberOfElements,
        const char* format,
        _locale_t locale,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vsprintf_s(jitter):
    """
    int vsprintf_s(
        char* buffer,
        size_t numberOfElements,
        const char* format,
        va_list argptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strdup_dbg(jitter):
    """
    char* _strdup_dbg(
        const char* strSource,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strSource", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsdup_dbg(jitter):
    """
    wchar_t* _wcsdup_dbg(
        const wchar_t* strSource,
        [DBG_BLOCK_TYPE] blockType,
        const char* filename,
        int linenumber
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strSource", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strxfrm(jitter):
    """
    [size_t_INT_MAX] strxfrm(
        char* strDest,
        const char* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsxfrm(jitter):
    """
    [size_t_INT_MAX] wcsxfrm(
        wchar_t* strDest,
        const wchar_t* strSource,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strxfrm_l(jitter):
    """
    [size_t_INT_MAX] _strxfrm_l(
        char* strDest,
        const char* strSource,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsxfrm_l(jitter):
    """
    [size_t_INT_MAX] _wcsxfrm_l(
        wchar_t* strDest,
        const wchar_t* strSource,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbrlen(jitter):
    """
    size_t mbrlen(
        const char* str,
        size_t maxSize,
        mbstate_t mbstate
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "maxSize", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcoll(jitter):
    """
    [_NLSCMPERROR] _mbsnbcoll(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcoll_l(jitter):
    """
    [_NLSCMPERROR] _mbsnbcoll_l(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbicoll(jitter):
    """
    [_NLSCMPERROR] _mbsnbicoll(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbicoll_l(jitter):
    """
    [_NLSCMPERROR] _mbsnbicoll_l(
        const unsigned char* string1,
        const unsigned char* string2,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbset_s(jitter):
    """
    errno_t _mbsnbset_s(
        unsigned char* str,
        size_t size,
        unsigned int c,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "size", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbset_s_l(jitter):
    """
    errno_t _mbsnbset_s_l(
        unsigned char* str,
        size_t size,
        unsigned int c,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "size", "c", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scprintf_p(jitter):
    """
    int _scprintf_p(
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scprintf_p_l(jitter):
    """
    int _scprintf_p_l(
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scwprintf_p(jitter):
    """
    int _scwprintf_p(
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scwprintf_p_l(jitter):
    """
    int _scwprintf_p_l(
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snprintf_s(jitter):
    """
    int _snprintf_s(
        char* buffer,
        size_t sizeOfBuffer,
        size_t count,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snprintf_s_l(jitter):
    """
    int _snprintf_s_l(
        char* buffer,
        size_t sizeOfBuffer,
        size_t count,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwprintf_s(jitter):
    """
    int _snwprintf_s(
        wchar_t* buffer,
        size_t sizeOfBuffer,
        size_t count,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwprintf_s_l(jitter):
    """
    int _snwprintf_s_l(
        wchar_t* buffer,
        size_t sizeOfBuffer,
        size_t count,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snprintf(jitter):
    """
    int _snprintf(
        char* buffer,
        size_t count,
        const char* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snprintf_l(jitter):
    """
    int _snprintf_l(
        char* buffer,
        size_t count,
        const char* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwprintf(jitter):
    """
    int _snwprintf(
        wchar_t* buffer,
        size_t count,
        const wchar_t* format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwprintf_l(jitter):
    """
    int _snwprintf_l(
        wchar_t* buffer,
        size_t count,
        const wchar_t* format,
        _locale_t locale,
        ...
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strnset_s(jitter):
    """
    errno_t _strnset_s(
        char* str,
        size_t numberOfElements,
        int c,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsnset_s(jitter):
    """
    errno_t _wcsnset_s(
        wchar_t* str,
        size_t numberOfElements,
        wchar_t c,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnset_s(jitter):
    """
    errno_t _mbsnset_s(
        unsigned char* str,
        size_t numberOfElements,
        unsigned int c,
        size_t count
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnset_s_l(jitter):
    """
    errno_t _mbsnset_s_l(
        unsigned char* str,
        size_t numberOfElements,
        unsigned int c,
        size_t count,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strset_s(jitter):
    """
    errno_t _strset_s(
        char* str,
        size_t numberOfElements,
        int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsset_s(jitter):
    """
    errno_t _wcsset_s(
        wchar_t* str,
        size_t numberOfElements,
        wchar_t c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsset_s(jitter):
    """
    errno_t _mbsset_s(
        unsigned char* str,
        size_t numberOfElements,
        unsigned int c
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsset_s_l(jitter):
    """
    errno_t _mbsset_s_l(
        unsigned char* str,
        size_t numberOfElements,
        unsigned int c,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findclose(jitter):
    """
    int _findclose(
        intptr_t handle
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findfirst(jitter):
    """
    intptr_t _findfirst(
        const char* filespec,
        struct _finddata_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findfirst32(jitter):
    """
    intptr_t _findfirst32(
        const char* filespec,
        struct _finddata32_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findfirst64(jitter):
    """
    intptr_t _findfirst64(
        const char* filespec,
        struct __finddata64_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findfirsti64(jitter):
    """
    intptr_t _findfirsti64(
        const char* filespec,
        struct _finddatai64_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findfirst32i64(jitter):
    """
    intptr_t _findfirst32i64(
        const char* filespec,
        struct _finddata32i64_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findfirst64i32(jitter):
    """
    intptr_t _findfirst64i32(
        const char* filespec,
        struct _finddata64i32_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindfirst(jitter):
    """
    intptr_t _wfindfirst(
        const wchar_t* filespec,
        struct _wfinddata_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindfirst32(jitter):
    """
    intptr_t _wfindfirst32(
        const wchar_t* filespec,
        struct _wfinddata32_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindfirst64(jitter):
    """
    intptr_t _wfindfirst64(
        const wchar_t* filespec,
        struct _wfinddata64_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindfirsti64(jitter):
    """
    intptr_t _wfindfirsti64(
        const wchar_t* filespec,
        struct _wfinddatai64_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindfirst32i64(jitter):
    """
    intptr_t _wfindfirst32i64(
        const wchar_t* filespec,
        struct _wfinddata32i64_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindfirst64i32(jitter):
    """
    intptr_t _wfindfirst64i32(
        const wchar_t* filespec,
        struct _wfinddata64i32_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findnext(jitter):
    """
    int _findnext(
        intptr_t handle,
        struct _finddata_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findnext32(jitter):
    """
    int _findnext32(
        intptr_t handle,
        struct _finddata32_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findnext64(jitter):
    """
    int _findnext64(
        intptr_t handle,
        struct __finddata64_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findnexti64(jitter):
    """
    int _findnexti64(
        intptr_t handle,
        struct _finddatai64_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findnext32i64(jitter):
    """
    int _findnext32i64(
        intptr_t handle,
        struct _finddata32i64_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findnext64i32(jitter):
    """
    int _findnext64i32(
        intptr_t handle,
        struct _finddata64i32_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindnext(jitter):
    """
    int _wfindnext(
        intptr_t handle,
        struct _wfinddata_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindnext32(jitter):
    """
    int _wfindnext32(
        intptr_t handle,
        struct _wfinddata32_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindnext64(jitter):
    """
    int _wfindnext64(
        intptr_t handle,
        struct _wfinddata64_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindnexti64(jitter):
    """
    int _wfindnexti64(
        intptr_t handle,
        struct _wfinddatai64_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindnext32i64(jitter):
    """
    int _wfindnext32i64(
        intptr_t handle,
        struct _wfinddatai64_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindnext64i32(jitter):
    """
    int _wfindnext64i32(
        intptr_t handle,
        struct _wfinddata64i32_t* fileinfo
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_asctime(jitter):
    """
    char* asctime(
        const struct tm* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wasctime(jitter):
    """
    wchar_t* _wasctime(
        const struct tm* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_asctime_s(jitter):
    """
    errno_t asctime_s(
        char* buffer,
        size_t numberOfElements,
        const struct tm* _tm
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "_tm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wasctime_s(jitter):
    """
    errno_t _wasctime_s(
        wchar_t* buffer,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_clock(jitter):
    """
    clock_t clock()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ctime(jitter):
    """
    char* ctime(
        const time_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ctime32(jitter):
    """
    char* _ctime32(
        const __time32_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ctime64(jitter):
    """
    char* _ctime64(
        const __time64_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctime(jitter):
    """
    wchar_t* _wctime(
        const time_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctime32(jitter):
    """
    wchar_t* _wctime32(
        const __time32_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctime64(jitter):
    """
    wchar_t* _wctime64(
        const __time64_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ctime32_s(jitter):
    """
    errno_t _ctime32_s(
        char* buffer,
        size_t numberOfElements,
        const __time32_t* time
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ctime64_s(jitter):
    """
    errno_t _ctime64_s(
        char* buffer,
        size_t numberOfElements,
        const __time64_t* time
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctime32_s(jitter):
    """
    errno_t _wctime32_s(
        wchar_t* buffer,
        size_t numberOfElements,
        const __time32_t* time
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctime64_s(jitter):
    """
    errno_t _wctime64_s(
        wchar_t* buffer,
        size_t numberOfElements,
        const __time64_t* time
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftime(jitter):
    """
    void _ftime(
        struct _timeb* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftime32(jitter):
    """
    void _ftime32(
        struct __timeb32* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftime64(jitter):
    """
    void _ftime64(
        struct __timeb64* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftime32_s(jitter):
    """
    errno_t _ftime32_s(
        struct __timeb32* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftime64_s(jitter):
    """
    errno_t _ftime64_s(
        struct __timeb64* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__futime(jitter):
    """
    int _futime(
        int fd,
        struct _utimbuf* filetime
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "filetime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__futime32(jitter):
    """
    int _futime32(
        int fd,
        struct __utimbuf32* filetime
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "filetime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__futime64(jitter):
    """
    int _futime64(
        int fd,
        struct __utimbuf64* filetime
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["fd", "filetime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_gmtime(jitter):
    """
    struct tm* gmtime(
        const time_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__gmtime32(jitter):
    """
    struct tm* _gmtime32(
        const __time32_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__gmtime64(jitter):
    """
    struct tm* _gmtime64(
        const __time64_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__gmtime32_s(jitter):
    """
    errno_t _gmtime32_s(
        struct tm* _tm,
        const __time32_t* time
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["_tm", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__gmtime64_s(jitter):
    """
    errno_t _gmtime64_s(
        struct tm* _tm,
        const __time64_t* time
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["_tm", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_localtime(jitter):
    """
    struct tm* localtime(
        const time_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__localtime32(jitter):
    """
    struct tm* _localtime32(
        const __time32_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__localtime64(jitter):
    """
    struct tm* _localtime64(
        const __time64_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__localtime32_s(jitter):
    """
    errno_t _localtime32_s(
        struct tm* _tm,
        const __time32_t* time
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["_tm", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__localtime64_s(jitter):
    """
    errno_t _localtime64_s(
        struct tm* _tm,
        const __time64_t* time
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["_tm", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mkgmtime(jitter):
    """
    time_t _mkgmtime(
        struct tm* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mkgmtime32(jitter):
    """
    __time32_t _mkgmtime32(
        struct tm* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mkgmtime64(jitter):
    """
    __time64_t _mkgmtime64(
        struct tm* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mktime(jitter):
    """
    time_t mktime(
        struct tm* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mktime32(jitter):
    """
    __time32_t _mktime32(
        struct tm* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mktime64(jitter):
    """
    __time64_t _mktime64(
        struct tm* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strdate(jitter):
    """
    char* _strdate(
        char* datestr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["datestr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstrdate(jitter):
    """
    wchar_t* _wstrdate(
        wchar_t* datestr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["datestr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strdate_s(jitter):
    """
    errno_t _strdate_s(
        char* buffer,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstrdate_s(jitter):
    """
    errno_t _wstrdate_s(
        wchar_t* buffer,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtime(jitter):
    """
    char* _strtime(
        char* timestr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timestr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstrtime(jitter):
    """
    wchar_t* _wstrtime(
        wchar_t* timestr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timestr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtime_s(jitter):
    """
    errno_t _strtime_s(
        char* buffer,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstrtime_s(jitter):
    """
    errno_t _wstrtime_s(
        wchar_t* buffer,
        size_t numberOfElements
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_time(jitter):
    """
    time_t time(
        time_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__time32(jitter):
    """
    __time32_t _time32(
        __time32_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__time64(jitter):
    """
    __time64_t _time64(
        __time64_t* timer
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__tzset(jitter):
    """
    void _tzset()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__utime(jitter):
    """
    int _utime(
        const char* filename,
        struct _utimbuf* times
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "times"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__utime32(jitter):
    """
    int _utime32(
        const char* filename,
        struct __utimbuf32* times
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "times"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__utime64(jitter):
    """
    int _utime64(
        const char* filename,
        struct __utimbuf64* times
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "times"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wutime(jitter):
    """
    int _wutime(
        const wchar_t* filename,
        struct _utimbuf* times
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "times"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wutime32(jitter):
    """
    int _wutime32(
        const wchar_t* filename,
        struct __utimbuf32* times
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "times"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wutime64(jitter):
    """
    int _wutime64(
        const wchar_t* filename,
        struct __utimbuf64* times
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["filename", "times"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__difftime32(jitter):
    """
    double _difftime32(
        __time32_t timer1,
        __time32_t timer0
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer1", "timer0"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__difftime64(jitter):
    """
    double _difftime64(
        __time64_t timer1,
        __time64_t timer0
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer1", "timer0"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_difftime(jitter):
    """
    double difftime(
        time_t timer1,
        time_t timer0
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["timer1", "timer0"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strftime(jitter):
    """
    size_t strftime(
        char* strDest,
        size_t maxsize,
        const char* format,
        const struct tm* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "maxsize", "format", "timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strftime_l(jitter):
    """
    size_t _strftime_l(
        char* strDest,
        size_t maxsize,
        const char* format,
        const struct tm* timeptr,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "maxsize", "format", "timeptr", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsftime(jitter):
    """
    size_t wcsftime(
        wchar_t* strDest,
        size_t maxsize,
        const wchar_t* format,
        const struct tm* timeptr
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "maxsize", "format", "timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsftime_l(jitter):
    """
    size_t _wcsftime_l(
        wchar_t* strDest,
        size_t maxsize,
        const wchar_t* format,
        const struct tm* timeptr,
        _locale_t locale
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["strDest", "maxsize", "format", "timeptr", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_dstbias(jitter):
    """
    errno_t _get_dstbias(
        int* seconds
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["seconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_daylight(jitter):
    """
    errno_t _get_daylight(
        int* hours
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["hours"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_timezone(jitter):
    """
    errno_t _get_timezone(
        long* seconds
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["seconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_tzname(jitter):
    """
    errno_t _get_tzname(
        size_t* pReturnValue,
        char* timeZoneName,
        size_t sizeInBytes,
        int index
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "timeZoneName", "sizeInBytes", "index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getsystime(jitter):
    """
    unsigned _getsystime(
        struct tm* _tm
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["_tm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__setsystime(jitter):
    """
    unsigned _setsystime(
        struct tm* _tm,
        unsigned millisec
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["_tm", "millisec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_output_format(jitter):
    """
    [output_format] _get_output_format()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_output_format(jitter):
    """
    [output_format] _set_output_format(
        [output_format] format
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_printf_count_output(jitter):
    """
    int _get_printf_count_output()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_printf_count_output(jitter):
    """
    int _set_printf_count_output(
        int enable
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["enable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lock(jitter):
    """
    void _lock(
        [LOCK_NUM] locknum
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["locknum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__unlock(jitter):
    """
    void _unlock(
        [LOCK_NUM] locknum
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["locknum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__initterm(jitter):
    """
    void _initterm(
        _PVFV* pfbegin,
        _PVFV* pfend
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pfbegin", "pfend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__initterm_e(jitter):
    """
    int _initterm_e(
        _PVFV* pfbegin,
        _PVFV* pfend
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["pfbegin", "pfend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___RTDynamicCast(jitter):
    """
    PVOID __RTDynamicCast(
        PVOID inptr,
        LONG VfDelta,
        PVOID SrcType,
        PVOID TargetType,
        BOOL isReference
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["inptr", "VfDelta", "SrcType", "TargetType", "isReference"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___p__commode(jitter):
    """
    int* __p__commode()
    """
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__beep(jitter):
    """
    void _beep(
        unsigned frequency,
        unsigned duration
    )
    """
    ret_ad, args = jitter.func_args_cdecl(["frequency", "duration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)
