###### Enums ######
_SQL_DRIVER_COMPLETION_ = {
    "SQL_DRIVER_NOPROMPT": 0,
    "SQL_DRIVER_COMPLETE": 1,
    "SQL_DRIVER_PROMPT": 2,
    "SQL_DRIVER_COMPLETE_REQUIRED": 3,
}
_SQL_DRIVER_COMPLETION__INV = {
    0: "SQL_DRIVER_NOPROMPT",
    1: "SQL_DRIVER_COMPLETE",
    2: "SQL_DRIVER_PROMPT",
    3: "SQL_DRIVER_COMPLETE_REQUIRED",
}
_SQL_ENDTRAN_OPTION_ = {
    "SQL_COMMIT": 0,
    "SQL_ROLLBACK": 1,
}
_SQL_ENDTRAN_OPTION__INV = {
    0: "SQL_COMMIT",
    1: "SQL_ROLLBACK",
}
_SQL_FETCH_TYPE_ = {
    "SQL_FETCH_NEXT": 1,
    "SQL_FETCH_FIRST": 2,
    "SQL_FETCH_LAST": 3,
    "SQL_FETCH_PRIOR": 4,
    "SQL_FETCH_ABSOLUTE": 5,
    "SQL_FETCH_RELATIVE": 6,
}
_SQL_FETCH_TYPE__INV = {
    1: "SQL_FETCH_NEXT",
    2: "SQL_FETCH_FIRST",
    3: "SQL_FETCH_LAST",
    4: "SQL_FETCH_PRIOR",
    5: "SQL_FETCH_ABSOLUTE",
    6: "SQL_FETCH_RELATIVE",
}
_SQL_HANDLE_TYPE_ = {
    "SQL_HANDLE_ENV": 1,
    "SQL_HANDLE_DBC": 2,
    "SQL_HANDLE_STMT": 3,
    "SQL_HANDLE_DESC": 4,
}
_SQL_HANDLE_TYPE__INV = {
    1: "SQL_HANDLE_ENV",
    2: "SQL_HANDLE_DBC",
    3: "SQL_HANDLE_STMT",
    4: "SQL_HANDLE_DESC",
}
_SQL_FREESTMT_OPTION_ = {
    "SQL_CLOSE": 0,
    "SQL_DROP": 1,
    "SQL_UNBIND": 2,
    "SQL_RESET_PARAMS": 3,
}
_SQL_FREESTMT_OPTION__INV = {
    0: "SQL_CLOSE",
    1: "SQL_DROP",
    2: "SQL_UNBIND",
    3: "SQL_RESET_PARAMS",
}

###################

###### Types ######
SQLSMALLINT = short
SQLSMALLINT_PTR = Ptr("<I", SQLSMALLINT())
SQLUSMALLINT = unsigned_short
SQLUSMALLINT_PTR = Ptr("<I", SQLUSMALLINT())
SQLPOINTER = void_PTR
SQLPOINTER_PTR = Ptr("<I", SQLPOINTER())
SQLINTEGER = long
SQLINTEGER_PTR = Ptr("<I", SQLINTEGER())
SQLLEN = INT_PTR
SQLLEN_PTR = Ptr("<I", SQLLEN())
SQLULEN = UINT_PTR
SQLULEN_PTR = Ptr("<I", SQLULEN())
SQLSETPOSIROW = UINT_PTR
SQLHWND = HWND
SQLHANDLE = void_PTR
SQLHANDLE_PTR = Ptr("<I", SQLHANDLE())
SQLHENV = SQLHANDLE
SQLHENV_PTR = Ptr("<I", SQLHENV())
SQLHDBC = SQLHANDLE
SQLHDBC_PTR = Ptr("<I", SQLHDBC())
SQLHSTMT = SQLHANDLE
SQLHSTMT_PTR = Ptr("<I", SQLHSTMT())
SQLHDESC = SQLHANDLE
SQLCHAR = unsigned_char
SQLCHAR_PTR = LPSTR
SQLTCHAR = TCHAR
SQLTCHAR_PTR = Ptr("<I", LPTSTR())
_SQL_DRIVER_COMPLETION_ = SQLUSMALLINT
_SQL_ENDTRAN_OPTION_ = SQLSMALLINT
_SQL_FETCH_TYPE_ = SQLSMALLINT
_SQL_HANDLE_TYPE_ = SQLSMALLINT
_SQL_FREESTMT_OPTION_ = SQLUSMALLINT

###################

###### Functions ######

def odbc32_SQLAllocConnect(jitter):
    """
    SQLRETURN SQLAllocConnect(
        SQLHENV EnvironmentHandle,
        SQLHDBC* ConnectionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnvironmentHandle", "ConnectionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLAllocEnv(jitter):
    """
    SQLRETURN SQLAllocEnv(
        SQLHENV* EnvironmentHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnvironmentHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLAllocHandle(jitter):
    """
    SQLRETURN SQLAllocHandle(
        [SQL_HANDLE_TYPE] HandleType,
        SQLHANDLE InputHandle,
        SQLHANDLE* OutputHandlePtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleType", "InputHandle", "OutputHandlePtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLAllocStmt(jitter):
    """
    SQLRETURN SQLAllocStmt(
        SQLHDBC ConnectionHandle,
        SQLHSTMT* StatementHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "StatementHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLBindCol(jitter):
    """
    SQLRETURN SQLBindCol(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT ColumnNumber,
        SQLSMALLINT TargetType,
        SQLPOINTER TargetValuePtr,
        SQLLEN BufferLength,
        SQLLEN* StrLen_or_Ind
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "ColumnNumber", "TargetType", "TargetValuePtr", "BufferLength", "StrLen_or_Ind"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLBindParam(jitter):
    """
    SQLRETURN SQLBindParam(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT ParameterNumber,
        SQLSMALLINT ValueType,
        SQLSMALLINT ParameterType,
        SQLULEN LengthPrecision,
        SQLSMALLINT ParameterScale,
        SQLPOINTER ParameterValue,
        SQLLEN* StrLen_or_IndPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "ParameterNumber", "ValueType", "ParameterType", "LengthPrecision", "ParameterScale", "ParameterValue", "StrLen_or_IndPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLBindParameter(jitter):
    """
    SQLRETURN SQLBindParameter(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT ParameterNumber,
        SQLSMALLINT InputOutputType,
        SQLSMALLINT ValueType,
        SQLSMALLINT ParameterType,
        SQLULEN ColumnSize,
        SQLSMALLINT DecimalDigits,
        SQLPOINTER ParameterValuePtr,
        SQLLEN BufferLength,
        SQLLEN* StrLen_or_IndPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "ParameterNumber", "InputOutputType", "ValueType", "ParameterType", "ColumnSize", "DecimalDigits", "ParameterValuePtr", "BufferLength", "StrLen_or_IndPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLBrowseConnect(jitter):
    """
    SQLRETURN SQLBrowseConnect(
        SQLHDBC ConnectionHandle,
        SQLCHAR* InConnectionString,
        SQLSMALLINT StringLength1,
        SQLCHAR* OutConnectionString,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* StringLength2Ptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "InConnectionString", "StringLength1", "OutConnectionString", "BufferLength", "StringLength2Ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLBrowseConnect(jitter, get_str, set_str):
    """
    SQLRETURN SQLBrowseConnect(
        SQLHDBC ConnectionHandle,
        SQLTCHAR* InConnectionString,
        SQLSMALLINT StringLength1,
        SQLTCHAR* OutConnectionString,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* StringLength2Ptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "InConnectionString", "StringLength1", "OutConnectionString", "BufferLength", "StringLength2Ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLBrowseConnectA(jitter):
    odbc32_SQLBrowseConnect(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLBrowseConnectW(jitter):
    odbc32_SQLBrowseConnect(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLBulkOperations(jitter):
    """
    SQLRETURN SQLBulkOperations(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT Operation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "Operation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLCancel(jitter):
    """
    SQLRETURN SQLCancel(
        SQLHSTMT StatementHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLCancelHandle(jitter):
    """
    SQLRETURN SQLCancelHandle(
        [SQL_HANDLE_TYPE] HandleType,
        SQLHANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleType", "Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLCloseCursor(jitter):
    """
    SQLRETURN SQLCloseCursor(
        SQLHSTMT StatementHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLColAttribute(jitter):
    """
    SQLRETURN SQLColAttribute(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT ColumnNumber,
        SQLUSMALLINT FieldIdentifier,
        SQLPOINTER CharacterAttributePtr,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* StringLengthPtr,
        SQLLEN* NumericAttributePtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "ColumnNumber", "FieldIdentifier", "CharacterAttributePtr", "BufferLength", "StringLengthPtr", "NumericAttributePtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLColAttribute(jitter, get_str, set_str):
    """
    SQLRETURN SQLColAttribute(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT ColumnNumber,
        SQLUSMALLINT FieldIdentifier,
        SQLPOINTER CharacterAttributePtr,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* StringLengthPtr,
        SQLLEN* NumericAttributePtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "ColumnNumber", "FieldIdentifier", "CharacterAttributePtr", "BufferLength", "StringLengthPtr", "NumericAttributePtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLColAttributeA(jitter):
    odbc32_SQLColAttribute(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLColAttributeW(jitter):
    odbc32_SQLColAttribute(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLColAttributes(jitter):
    """
    SQLRETURN SQLColAttributes(
        SQLHSTMT hstmt,
        SQLUSMALLINT icol,
        SQLUSMALLINT fDescType,
        SQLPOINTER rgbDesc,
        SQLSMALLINT cbDescMax,
        SQLSMALLINT* pcbDesc,
        SQLLEN* pfDesc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hstmt", "icol", "fDescType", "rgbDesc", "cbDescMax", "pcbDesc", "pfDesc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLColAttributes(jitter, get_str, set_str):
    """
    SQLRETURN SQLColAttributes(
        SQLHSTMT hstmt,
        SQLUSMALLINT icol,
        SQLUSMALLINT fDescType,
        SQLPOINTER rgbDesc,
        SQLSMALLINT cbDescMax,
        SQLSMALLINT* pcbDesc,
        SQLLEN* pfDesc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hstmt", "icol", "fDescType", "rgbDesc", "cbDescMax", "pcbDesc", "pfDesc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLColAttributesA(jitter):
    odbc32_SQLColAttributes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLColAttributesW(jitter):
    odbc32_SQLColAttributes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLColumnPrivileges(jitter):
    """
    SQLRETURN SQLColumnPrivileges(
        SQLHSTMT StatementHandle,
        SQLCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLCHAR* TableName,
        SQLSMALLINT NameLength3,
        SQLCHAR* ColumnName,
        SQLSMALLINT NameLength4
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3", "ColumnName", "NameLength4"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLColumnPrivileges(jitter, get_str, set_str):
    """
    SQLRETURN SQLColumnPrivileges(
        SQLHSTMT StatementHandle,
        SQLTCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLTCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLTCHAR* TableName,
        SQLSMALLINT NameLength3,
        SQLTCHAR* ColumnName,
        SQLSMALLINT NameLength4
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3", "ColumnName", "NameLength4"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLColumnPrivilegesA(jitter):
    odbc32_SQLColumnPrivileges(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLColumnPrivilegesW(jitter):
    odbc32_SQLColumnPrivileges(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLColumns(jitter):
    """
    SQLRETURN SQLColumns(
        SQLHSTMT StatementHandle,
        SQLCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLCHAR* TableName,
        SQLSMALLINT NameLength3,
        SQLCHAR* ColumnName,
        SQLSMALLINT NameLength4
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3", "ColumnName", "NameLength4"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLColumns(jitter, get_str, set_str):
    """
    SQLRETURN SQLColumns(
        SQLHSTMT StatementHandle,
        SQLTCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLTCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLTCHAR* TableName,
        SQLSMALLINT NameLength3,
        SQLTCHAR* ColumnName,
        SQLSMALLINT NameLength4
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3", "ColumnName", "NameLength4"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLColumnsA(jitter):
    odbc32_SQLColumns(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLColumnsW(jitter):
    odbc32_SQLColumns(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLCompleteAsync(jitter):
    """
    SQLRETURN SQLCompleteAsync(
        SQLSMALLINT HandleType,
        SQLHANDLE Handle,
        RETCODE* AsyncRetCodePtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleType", "Handle", "AsyncRetCodePtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLConnect(jitter):
    """
    SQLRETURN SQLConnect(
        SQLHDBC ConnectionHandle,
        SQLCHAR* ServerName,
        SQLSMALLINT NameLength1,
        SQLCHAR* UserName,
        SQLSMALLINT NameLength2,
        SQLCHAR* Authentication,
        SQLSMALLINT NameLength3
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "ServerName", "NameLength1", "UserName", "NameLength2", "Authentication", "NameLength3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLConnect(jitter, get_str, set_str):
    """
    SQLRETURN SQLConnect(
        SQLHDBC ConnectionHandle,
        SQLTCHAR* ServerName,
        SQLSMALLINT NameLength1,
        SQLTCHAR* UserName,
        SQLSMALLINT NameLength2,
        SQLTCHAR* Authentication,
        SQLSMALLINT NameLength3
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "ServerName", "NameLength1", "UserName", "NameLength2", "Authentication", "NameLength3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLConnectA(jitter):
    odbc32_SQLConnect(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLConnectW(jitter):
    odbc32_SQLConnect(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLCopyDesc(jitter):
    """
    SQLRETURN SQLCopyDesc(
        SQLHDESC SourceDescHandle,
        SQLHDESC TargetDescHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceDescHandle", "TargetDescHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLDataSources(jitter):
    """
    SQLRETURN SQLDataSources(
        SQLHENV EnvironmentHandle,
        SQLUSMALLINT Direction,
        SQLCHAR* ServerName,
        SQLSMALLINT BufferLength1,
        SQLSMALLINT* NameLength1Ptr,
        SQLCHAR* Description,
        SQLSMALLINT BufferLength2,
        SQLSMALLINT* NameLength2Ptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnvironmentHandle", "Direction", "ServerName", "BufferLength1", "NameLength1Ptr", "Description", "BufferLength2", "NameLength2Ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLDataSources(jitter, get_str, set_str):
    """
    SQLRETURN SQLDataSources(
        SQLHENV EnvironmentHandle,
        SQLUSMALLINT Direction,
        SQLTCHAR* ServerName,
        SQLSMALLINT BufferLength1,
        SQLSMALLINT* NameLength1Ptr,
        SQLTCHAR* Description,
        SQLSMALLINT BufferLength2,
        SQLSMALLINT* NameLength2Ptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnvironmentHandle", "Direction", "ServerName", "BufferLength1", "NameLength1Ptr", "Description", "BufferLength2", "NameLength2Ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLDataSourcesA(jitter):
    odbc32_SQLDataSources(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLDataSourcesW(jitter):
    odbc32_SQLDataSources(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLDescribeCol(jitter):
    """
    SQLRETURN SQLDescribeCol(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT ColumnNumber,
        SQLCHAR* ColumnName,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* NameLengthPtr,
        SQLSMALLINT* DataTypePtr,
        SQLULEN* ColumnSizePtr,
        SQLSMALLINT* DecimalDigitsPtr,
        SQLSMALLINT* NullablePtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "ColumnNumber", "ColumnName", "BufferLength", "NameLengthPtr", "DataTypePtr", "ColumnSizePtr", "DecimalDigitsPtr", "NullablePtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLDescribeCol(jitter, get_str, set_str):
    """
    SQLRETURN SQLDescribeCol(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT ColumnNumber,
        SQLTCHAR* ColumnName,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* NameLengthPtr,
        SQLSMALLINT* DataTypePtr,
        SQLULEN* ColumnSizePtr,
        SQLSMALLINT* DecimalDigitsPtr,
        SQLSMALLINT* NullablePtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "ColumnNumber", "ColumnName", "BufferLength", "NameLengthPtr", "DataTypePtr", "ColumnSizePtr", "DecimalDigitsPtr", "NullablePtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLDescribeColA(jitter):
    odbc32_SQLDescribeCol(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLDescribeColW(jitter):
    odbc32_SQLDescribeCol(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLDescribeParam(jitter):
    """
    SQLRETURN SQLDescribeParam(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT ParameterNumber,
        SQLSMALLINT* DataTypePtr,
        SQLULEN* ParameterSizePtr,
        SQLSMALLINT* DecimalDigitsPtr,
        SQLSMALLINT* NullablePtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "ParameterNumber", "DataTypePtr", "ParameterSizePtr", "DecimalDigitsPtr", "NullablePtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLDisconnect(jitter):
    """
    SQLRETURN SQLDisconnect(
        SQLHDBC ConnectionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLDriverConnect(jitter):
    """
    SQLRETURN SQLDriverConnect(
        SQLHDBC ConnectionHandle,
        SQLHWND WindowHandle,
        SQLCHAR* InConnectionString,
        SQLSMALLINT StringLength1,
        SQLCHAR* OutConnectionString,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* StringLength2Ptr,
        [SQL_DRIVER_COMPLETION] DriverCompletion
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "WindowHandle", "InConnectionString", "StringLength1", "OutConnectionString", "BufferLength", "StringLength2Ptr", "DriverCompletion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLDriverConnect(jitter, get_str, set_str):
    """
    SQLRETURN SQLDriverConnect(
        SQLHDBC ConnectionHandle,
        SQLHWND WindowHandle,
        SQLTCHAR* InConnectionString,
        SQLSMALLINT StringLength1,
        SQLTCHAR* OutConnectionString,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* StringLength2Ptr,
        [SQL_DRIVER_COMPLETION] DriverCompletion
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "WindowHandle", "InConnectionString", "StringLength1", "OutConnectionString", "BufferLength", "StringLength2Ptr", "DriverCompletion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLDriverConnectA(jitter):
    odbc32_SQLDriverConnect(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLDriverConnectW(jitter):
    odbc32_SQLDriverConnect(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLDrivers(jitter):
    """
    SQLRETURN SQLDrivers(
        SQLHENV EnvironmentHandle,
        SQLUSMALLINT Direction,
        SQLCHAR* DriverDescription,
        SQLSMALLINT BufferLength1,
        SQLSMALLINT* DescriptionLengthPtr,
        SQLCHAR* DriverAttributes,
        SQLSMALLINT BufferLength2,
        SQLSMALLINT* AttributesLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnvironmentHandle", "Direction", "DriverDescription", "BufferLength1", "DescriptionLengthPtr", "DriverAttributes", "BufferLength2", "AttributesLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLDrivers(jitter, get_str, set_str):
    """
    SQLRETURN SQLDrivers(
        SQLHENV EnvironmentHandle,
        SQLUSMALLINT Direction,
        SQLTCHAR* DriverDescription,
        SQLSMALLINT BufferLength1,
        SQLSMALLINT* DescriptionLengthPtr,
        SQLTCHAR* DriverAttributes,
        SQLSMALLINT BufferLength2,
        SQLSMALLINT* AttributesLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnvironmentHandle", "Direction", "DriverDescription", "BufferLength1", "DescriptionLengthPtr", "DriverAttributes", "BufferLength2", "AttributesLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLDriversA(jitter):
    odbc32_SQLDrivers(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLDriversW(jitter):
    odbc32_SQLDrivers(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLEndTran(jitter):
    """
    SQLRETURN SQLEndTran(
        [SQL_HANDLE_TYPE] HandleType,
        SQLHANDLE Handle,
        [SQL_ENDTRAN_OPTION] CompletionType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleType", "Handle", "CompletionType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLError(jitter):
    """
    SQLRETURN SQLError(
        SQLHENV EnvironmentHandle,
        SQLHDBC ConnectionHandle,
        SQLHSTMT StatementHandle,
        SQLCHAR* SQLState,
        SQLINTEGER* NativeError,
        SQLCHAR* MessageText,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* TextLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnvironmentHandle", "ConnectionHandle", "StatementHandle", "SQLState", "NativeError", "MessageText", "BufferLength", "TextLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLError(jitter, get_str, set_str):
    """
    SQLRETURN SQLError(
        SQLHENV EnvironmentHandle,
        SQLHDBC ConnectionHandle,
        SQLHSTMT StatementHandle,
        SQLTCHAR* SQLState,
        SQLINTEGER* NativeError,
        SQLTCHAR* MessageText,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* TextLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnvironmentHandle", "ConnectionHandle", "StatementHandle", "SQLState", "NativeError", "MessageText", "BufferLength", "TextLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLErrorA(jitter):
    odbc32_SQLError(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLErrorW(jitter):
    odbc32_SQLError(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLExecDirect(jitter):
    """
    SQLRETURN SQLExecDirect(
        SQLHSTMT StatementHandle,
        SQLCHAR* StatementText,
        SQLINTEGER TextLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "StatementText", "TextLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLExecDirect(jitter, get_str, set_str):
    """
    SQLRETURN SQLExecDirect(
        SQLHSTMT StatementHandle,
        SQLTCHAR* StatementText,
        SQLINTEGER TextLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "StatementText", "TextLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLExecDirectA(jitter):
    odbc32_SQLExecDirect(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLExecDirectW(jitter):
    odbc32_SQLExecDirect(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLExecute(jitter):
    """
    SQLRETURN SQLExecute(
        SQLHSTMT StatementHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLExtendedFetch(jitter):
    """
    SQLRETURN SQLExtendedFetch(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT FetchOrientation,
        SQLLEN FetchOffset,
        SQLULEN* RowCountPtr,
        SQLUSMALLINT* RowStatusArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "FetchOrientation", "FetchOffset", "RowCountPtr", "RowStatusArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLFetch(jitter):
    """
    SQLRETURN SQLFetch(
        SQLHSTMT StatementHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLFetchScroll(jitter):
    """
    SQLRETURN SQLFetchScroll(
        SQLHSTMT StatementHandle,
        [SQL_FETCH_TYPE] FetchOrientation,
        SQLLEN FetchOffset
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "FetchOrientation", "FetchOffset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLForeignKeys(jitter):
    """
    SQLRETURN SQLForeignKeys(
        SQLHSTMT StatementHandle,
        SQLCHAR* PKCatalogName,
        SQLSMALLINT NameLength1,
        SQLCHAR* PKSchemaName,
        SQLSMALLINT NameLength2,
        SQLCHAR* PKTableName,
        SQLSMALLINT NameLength3,
        SQLCHAR* FKCatalogName,
        SQLSMALLINT NameLength4,
        SQLCHAR* FKSchemaName,
        SQLSMALLINT NameLength5,
        SQLCHAR* FKTableName,
        SQLSMALLINT NameLength6
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "PKCatalogName", "NameLength1", "PKSchemaName", "NameLength2", "PKTableName", "NameLength3", "FKCatalogName", "NameLength4", "FKSchemaName", "NameLength5", "FKTableName", "NameLength6"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLForeignKeys(jitter, get_str, set_str):
    """
    SQLRETURN SQLForeignKeys(
        SQLHSTMT StatementHandle,
        SQLTCHAR* PKCatalogName,
        SQLSMALLINT NameLength1,
        SQLTCHAR* PKSchemaName,
        SQLSMALLINT NameLength2,
        SQLTCHAR* PKTableName,
        SQLSMALLINT NameLength3,
        SQLTCHAR* FKCatalogName,
        SQLSMALLINT NameLength4,
        SQLTCHAR* FKSchemaName,
        SQLSMALLINT NameLength5,
        SQLTCHAR* FKTableName,
        SQLSMALLINT NameLength6
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "PKCatalogName", "NameLength1", "PKSchemaName", "NameLength2", "PKTableName", "NameLength3", "FKCatalogName", "NameLength4", "FKSchemaName", "NameLength5", "FKTableName", "NameLength6"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLForeignKeysA(jitter):
    odbc32_SQLForeignKeys(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLForeignKeysW(jitter):
    odbc32_SQLForeignKeys(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLFreeConnect(jitter):
    """
    SQLRETURN SQLFreeConnect(
        SQLHDBC ConnectionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLFreeEnv(jitter):
    """
    SQLRETURN SQLFreeEnv(
        SQLHENV EnvironmentHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnvironmentHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLFreeHandle(jitter):
    """
    SQLRETURN SQLFreeHandle(
        [SQL_HANDLE_TYPE] HandleType,
        SQLHANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleType", "Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLFreeStmt(jitter):
    """
    SQLRETURN SQLFreeStmt(
        SQLHSTMT StatementHandle,
        [SQL_FREESTMT_OPTION] Option
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "Option"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetConnectAttr(jitter):
    """
    SQLRETURN SQLGetConnectAttr(
        SQLHDBC ConnectionHandle,
        SQLINTEGER Attribute,
        SQLPOINTER ValuePtr,
        SQLINTEGER BufferLength,
        SQLINTEGER* StringLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "Attribute", "ValuePtr", "BufferLength", "StringLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetConnectAttr(jitter, get_str, set_str):
    """
    SQLRETURN SQLGetConnectAttr(
        SQLHDBC ConnectionHandle,
        SQLINTEGER Attribute,
        SQLPOINTER ValuePtr,
        SQLINTEGER BufferLength,
        SQLINTEGER* StringLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "Attribute", "ValuePtr", "BufferLength", "StringLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetConnectAttrA(jitter):
    odbc32_SQLGetConnectAttr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLGetConnectAttrW(jitter):
    odbc32_SQLGetConnectAttr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLGetConnectOption(jitter):
    """
    SQLRETURN SQLGetConnectOption(
        SQLHDBC ConnectionHandle,
        SQLUSMALLINT Option,
        SQLPOINTER Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "Option", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetConnectOption(jitter, get_str, set_str):
    """
    SQLRETURN SQLGetConnectOption(
        SQLHDBC ConnectionHandle,
        SQLUSMALLINT Option,
        SQLPOINTER Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "Option", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetConnectOptionA(jitter):
    odbc32_SQLGetConnectOption(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLGetConnectOptionW(jitter):
    odbc32_SQLGetConnectOption(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLGetCursorName(jitter):
    """
    SQLRETURN SQLGetCursorName(
        SQLHSTMT StatementHandle,
        SQLCHAR* CursorName,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* NameLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CursorName", "BufferLength", "NameLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetCursorName(jitter, get_str, set_str):
    """
    SQLRETURN SQLGetCursorName(
        SQLHSTMT StatementHandle,
        SQLTCHAR* CursorName,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* NameLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CursorName", "BufferLength", "NameLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetCursorNameA(jitter):
    odbc32_SQLGetCursorName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLGetCursorNameW(jitter):
    odbc32_SQLGetCursorName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLGetData(jitter):
    """
    SQLRETURN SQLGetData(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT Col_or_Param_Num,
        SQLSMALLINT TargetType,
        SQLPOINTER TargetValuePtr,
        SQLLEN BufferLength,
        SQLLEN* StrLen_or_IndPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "Col_or_Param_Num", "TargetType", "TargetValuePtr", "BufferLength", "StrLen_or_IndPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetDescField(jitter):
    """
    SQLRETURN SQLGetDescField(
        SQLHDESC DescriptorHandle,
        SQLSMALLINT RecNumber,
        SQLSMALLINT FieldIdentifier,
        SQLPOINTER ValuePtr,
        SQLINTEGER BufferLength,
        SQLINTEGER* StringLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DescriptorHandle", "RecNumber", "FieldIdentifier", "ValuePtr", "BufferLength", "StringLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetDescField(jitter, get_str, set_str):
    """
    SQLRETURN SQLGetDescField(
        SQLHDESC DescriptorHandle,
        SQLSMALLINT RecNumber,
        SQLSMALLINT FieldIdentifier,
        SQLPOINTER ValuePtr,
        SQLINTEGER BufferLength,
        SQLINTEGER* StringLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DescriptorHandle", "RecNumber", "FieldIdentifier", "ValuePtr", "BufferLength", "StringLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetDescFieldA(jitter):
    odbc32_SQLGetDescField(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLGetDescFieldW(jitter):
    odbc32_SQLGetDescField(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLGetDescRec(jitter):
    """
    SQLRETURN SQLGetDescRec(
        SQLHDESC DescriptorHandle,
        SQLSMALLINT RecNumber,
        SQLCHAR* Name,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* StringLengthPtr,
        SQLSMALLINT* TypePtr,
        SQLSMALLINT* SubTypePtr,
        SQLLEN* LengthPtr,
        SQLSMALLINT* PrecisionPtr,
        SQLSMALLINT* ScalePtr,
        SQLSMALLINT* NullablePtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DescriptorHandle", "RecNumber", "Name", "BufferLength", "StringLengthPtr", "TypePtr", "SubTypePtr", "LengthPtr", "PrecisionPtr", "ScalePtr", "NullablePtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetDescRec(jitter, get_str, set_str):
    """
    SQLRETURN SQLGetDescRec(
        SQLHDESC DescriptorHandle,
        SQLSMALLINT RecNumber,
        SQLTCHAR* Name,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* StringLengthPtr,
        SQLSMALLINT* TypePtr,
        SQLSMALLINT* SubTypePtr,
        SQLLEN* LengthPtr,
        SQLSMALLINT* PrecisionPtr,
        SQLSMALLINT* ScalePtr,
        SQLSMALLINT* NullablePtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DescriptorHandle", "RecNumber", "Name", "BufferLength", "StringLengthPtr", "TypePtr", "SubTypePtr", "LengthPtr", "PrecisionPtr", "ScalePtr", "NullablePtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetDescRecA(jitter):
    odbc32_SQLGetDescRec(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLGetDescRecW(jitter):
    odbc32_SQLGetDescRec(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLGetDiagField(jitter):
    """
    SQLRETURN SQLGetDiagField(
        [SQL_HANDLE_TYPE] HandleType,
        SQLHANDLE Handle,
        SQLSMALLINT RecNumber,
        SQLSMALLINT DiagIdentifier,
        SQLPOINTER DiagInfoPtr,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* StringLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleType", "Handle", "RecNumber", "DiagIdentifier", "DiagInfoPtr", "BufferLength", "StringLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetDiagField(jitter, get_str, set_str):
    """
    SQLRETURN SQLGetDiagField(
        [SQL_HANDLE_TYPE] HandleType,
        SQLHANDLE Handle,
        SQLSMALLINT RecNumber,
        SQLSMALLINT DiagIdentifier,
        SQLPOINTER DiagInfoPtr,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* StringLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleType", "Handle", "RecNumber", "DiagIdentifier", "DiagInfoPtr", "BufferLength", "StringLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetDiagFieldA(jitter):
    odbc32_SQLGetDiagField(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLGetDiagFieldW(jitter):
    odbc32_SQLGetDiagField(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLGetDiagRec(jitter):
    """
    SQLRETURN SQLGetDiagRec(
        [SQL_HANDLE_TYPE] HandleType,
        SQLHANDLE Handle,
        SQLSMALLINT RecNumber,
        SQLCHAR* SQLState,
        SQLINTEGER* NativeErrorPtr,
        SQLCHAR* MessageText,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* TextLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleType", "Handle", "RecNumber", "SQLState", "NativeErrorPtr", "MessageText", "BufferLength", "TextLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetDiagRec(jitter, get_str, set_str):
    """
    SQLRETURN SQLGetDiagRec(
        [SQL_HANDLE_TYPE] HandleType,
        SQLHANDLE Handle,
        SQLSMALLINT RecNumber,
        SQLTCHAR* SQLState,
        SQLINTEGER* NativeErrorPtr,
        SQLTCHAR* MessageText,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* TextLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleType", "Handle", "RecNumber", "SQLState", "NativeErrorPtr", "MessageText", "BufferLength", "TextLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetDiagRecA(jitter):
    odbc32_SQLGetDiagRec(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLGetDiagRecW(jitter):
    odbc32_SQLGetDiagRec(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLGetEnvAttr(jitter):
    """
    SQLRETURN SQLGetEnvAttr(
        SQLHENV EnvironmentHandle,
        SQLINTEGER Attribute,
        SQLPOINTER ValuePtr,
        SQLINTEGER BufferLength,
        SQLINTEGER* StringLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnvironmentHandle", "Attribute", "ValuePtr", "BufferLength", "StringLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetFunctions(jitter):
    """
    SQLRETURN SQLGetFunctions(
        SQLHDBC ConnectionHandle,
        SQLUSMALLINT FunctionId,
        SQLUSMALLINT* SupportedPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "FunctionId", "SupportedPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetInfo(jitter):
    """
    SQLRETURN SQLGetInfo(
        SQLHDBC ConnectionHandle,
        SQLUSMALLINT InfoType,
        SQLPOINTER InfoValuePtr,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* StringLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "InfoType", "InfoValuePtr", "BufferLength", "StringLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetInfo(jitter, get_str, set_str):
    """
    SQLRETURN SQLGetInfo(
        SQLHDBC ConnectionHandle,
        SQLUSMALLINT InfoType,
        SQLPOINTER InfoValuePtr,
        SQLSMALLINT BufferLength,
        SQLSMALLINT* StringLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "InfoType", "InfoValuePtr", "BufferLength", "StringLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetInfoA(jitter):
    odbc32_SQLGetInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLGetInfoW(jitter):
    odbc32_SQLGetInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLGetStmtAttr(jitter):
    """
    SQLRETURN SQLGetStmtAttr(
        SQLHSTMT StatementHandle,
        SQLINTEGER Attribute,
        SQLPOINTER ValuePtr,
        SQLINTEGER BufferLength,
        SQLINTEGER* StringLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "Attribute", "ValuePtr", "BufferLength", "StringLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetStmtAttr(jitter, get_str, set_str):
    """
    SQLRETURN SQLGetStmtAttr(
        SQLHSTMT StatementHandle,
        SQLINTEGER Attribute,
        SQLPOINTER ValuePtr,
        SQLINTEGER BufferLength,
        SQLINTEGER* StringLengthPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "Attribute", "ValuePtr", "BufferLength", "StringLengthPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetStmtAttrA(jitter):
    odbc32_SQLGetStmtAttr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLGetStmtAttrW(jitter):
    odbc32_SQLGetStmtAttr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLGetStmtOption(jitter):
    """
    SQLRETURN SQLGetStmtOption(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT Option,
        SQLPOINTER Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "Option", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetTypeInfo(jitter):
    """
    SQLRETURN SQLGetTypeInfo(
        SQLHSTMT StatementHandle,
        SQLSMALLINT DataType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "DataType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetTypeInfo(jitter, get_str, set_str):
    """
    SQLRETURN SQLGetTypeInfo(
        SQLHSTMT StatementHandle,
        SQLSMALLINT DataType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "DataType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLGetTypeInfoA(jitter):
    odbc32_SQLGetTypeInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLGetTypeInfoW(jitter):
    odbc32_SQLGetTypeInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLMoreResults(jitter):
    """
    SQLRETURN SQLMoreResults(
        SQLHSTMT StatementHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLNativeSql(jitter):
    """
    SQLRETURN SQLNativeSql(
        SQLHDBC ConnectionHandle,
        SQLCHAR* InStatementText,
        SQLINTEGER TextLength1,
        SQLCHAR* OutStatementText,
        SQLINTEGER BufferLength,
        SQLINTEGER* TextLength2Ptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "InStatementText", "TextLength1", "OutStatementText", "BufferLength", "TextLength2Ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLNativeSql(jitter, get_str, set_str):
    """
    SQLRETURN SQLNativeSql(
        SQLHDBC ConnectionHandle,
        SQLTCHAR* InStatementText,
        SQLINTEGER TextLength1,
        SQLTCHAR* OutStatementText,
        SQLINTEGER BufferLength,
        SQLINTEGER* TextLength2Ptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "InStatementText", "TextLength1", "OutStatementText", "BufferLength", "TextLength2Ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLNativeSqlA(jitter):
    odbc32_SQLNativeSql(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLNativeSqlW(jitter):
    odbc32_SQLNativeSql(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLNumParams(jitter):
    """
    SQLRETURN SQLNumParams(
        SQLHSTMT StatementHandle,
        SQLSMALLINT* ParameterCountPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "ParameterCountPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLNumResultCols(jitter):
    """
    SQLRETURN SQLNumResultCols(
        SQLHSTMT StatementHandle,
        SQLSMALLINT* ColumnCountPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "ColumnCountPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLParamData(jitter):
    """
    SQLRETURN SQLParamData(
        SQLHSTMT StatementHandle,
        SQLPOINTER* ValuePtrPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "ValuePtrPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLParamOptions(jitter):
    """
    SQLRETURN SQLParamOptions(
        SQLHSTMT hstmt,
        SQLULEN crow,
        SQLULEN* pirow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hstmt", "crow", "pirow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLPrepare(jitter):
    """
    SQLRETURN SQLPrepare(
        SQLHSTMT StatementHandle,
        SQLCHAR* StatementText,
        SQLINTEGER TextLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "StatementText", "TextLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLPrepare(jitter, get_str, set_str):
    """
    SQLRETURN SQLPrepare(
        SQLHSTMT StatementHandle,
        SQLTCHAR* StatementText,
        SQLINTEGER TextLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "StatementText", "TextLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLPrepareA(jitter):
    odbc32_SQLPrepare(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLPrepareW(jitter):
    odbc32_SQLPrepare(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLPrimaryKeys(jitter):
    """
    SQLRETURN SQLPrimaryKeys(
        SQLHSTMT StatementHandle,
        SQLCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLCHAR* TableName,
        SQLSMALLINT NameLength3
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLPrimaryKeys(jitter, get_str, set_str):
    """
    SQLRETURN SQLPrimaryKeys(
        SQLHSTMT StatementHandle,
        SQLTCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLTCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLTCHAR* TableName,
        SQLSMALLINT NameLength3
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLPrimaryKeysA(jitter):
    odbc32_SQLPrimaryKeys(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLPrimaryKeysW(jitter):
    odbc32_SQLPrimaryKeys(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLProcedureColumns(jitter):
    """
    SQLRETURN SQLProcedureColumns(
        SQLHSTMT StatementHandle,
        SQLCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLCHAR* ProcName,
        SQLSMALLINT NameLength3,
        SQLCHAR* ColumnName,
        SQLSMALLINT NameLength4
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "ProcName", "NameLength3", "ColumnName", "NameLength4"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLProcedureColumns(jitter, get_str, set_str):
    """
    SQLRETURN SQLProcedureColumns(
        SQLHSTMT StatementHandle,
        SQLTCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLTCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLTCHAR* ProcName,
        SQLSMALLINT NameLength3,
        SQLTCHAR* ColumnName,
        SQLSMALLINT NameLength4
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "ProcName", "NameLength3", "ColumnName", "NameLength4"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLProcedureColumnsA(jitter):
    odbc32_SQLProcedureColumns(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLProcedureColumnsW(jitter):
    odbc32_SQLProcedureColumns(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLProcedures(jitter):
    """
    SQLRETURN SQLProcedures(
        SQLHSTMT StatementHandle,
        SQLCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLCHAR* ProcName,
        SQLSMALLINT NameLength3
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "ProcName", "NameLength3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLProcedures(jitter, get_str, set_str):
    """
    SQLRETURN SQLProcedures(
        SQLHSTMT StatementHandle,
        SQLTCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLTCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLTCHAR* ProcName,
        SQLSMALLINT NameLength3
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "ProcName", "NameLength3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLProceduresA(jitter):
    odbc32_SQLProcedures(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLProceduresW(jitter):
    odbc32_SQLProcedures(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLPutData(jitter):
    """
    SQLRETURN SQLPutData(
        SQLHSTMT StatementHandle,
        SQLPOINTER DataPtr,
        SQLLEN StrLen_or_Ind
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "DataPtr", "StrLen_or_Ind"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLRowCount(jitter):
    """
    SQLRETURN SQLRowCount(
        SQLHSTMT StatementHandle,
        SQLLEN* RowCountPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "RowCountPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetConnectAttr(jitter):
    """
    SQLRETURN SQLSetConnectAttr(
        SQLHDBC ConnectionHandle,
        SQLINTEGER Attribute,
        SQLPOINTER ValuePtr,
        SQLINTEGER StringLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "Attribute", "ValuePtr", "StringLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetConnectAttr(jitter, get_str, set_str):
    """
    SQLRETURN SQLSetConnectAttr(
        SQLHDBC ConnectionHandle,
        SQLINTEGER Attribute,
        SQLPOINTER ValuePtr,
        SQLINTEGER StringLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "Attribute", "ValuePtr", "StringLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetConnectAttrA(jitter):
    odbc32_SQLSetConnectAttr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLSetConnectAttrW(jitter):
    odbc32_SQLSetConnectAttr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLSetConnectOption(jitter):
    """
    SQLRETURN SQLSetConnectOption(
        SQLHDBC ConnectionHandle,
        SQLUSMALLINT Option,
        SQLULEN Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "Option", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetConnectOption(jitter, get_str, set_str):
    """
    SQLRETURN SQLSetConnectOption(
        SQLHDBC ConnectionHandle,
        SQLUSMALLINT Option,
        SQLULEN Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "Option", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetConnectOptionA(jitter):
    odbc32_SQLSetConnectOption(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLSetConnectOptionW(jitter):
    odbc32_SQLSetConnectOption(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLSetCursorName(jitter):
    """
    SQLRETURN SQLSetCursorName(
        SQLHSTMT StatementHandle,
        SQLCHAR* CursorName,
        SQLSMALLINT NameLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CursorName", "NameLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetCursorName(jitter, get_str, set_str):
    """
    SQLRETURN SQLSetCursorName(
        SQLHSTMT StatementHandle,
        SQLTCHAR* CursorName,
        SQLSMALLINT NameLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CursorName", "NameLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetCursorNameA(jitter):
    odbc32_SQLSetCursorName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLSetCursorNameW(jitter):
    odbc32_SQLSetCursorName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLSetDescField(jitter):
    """
    SQLRETURN SQLSetDescField(
        SQLHDESC DescriptorHandle,
        SQLSMALLINT RecNumber,
        SQLSMALLINT FieldIdentifier,
        SQLPOINTER ValuePtr,
        SQLINTEGER BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DescriptorHandle", "RecNumber", "FieldIdentifier", "ValuePtr", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetDescField(jitter, get_str, set_str):
    """
    SQLRETURN SQLSetDescField(
        SQLHDESC DescriptorHandle,
        SQLSMALLINT RecNumber,
        SQLSMALLINT FieldIdentifier,
        SQLPOINTER ValuePtr,
        SQLINTEGER BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DescriptorHandle", "RecNumber", "FieldIdentifier", "ValuePtr", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetDescFieldA(jitter):
    odbc32_SQLSetDescField(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLSetDescFieldW(jitter):
    odbc32_SQLSetDescField(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLSetDescRec(jitter):
    """
    SQLRETURN SQLSetDescRec(
        SQLHDESC DescriptorHandle,
        SQLSMALLINT RecNumber,
        SQLSMALLINT Type,
        SQLSMALLINT SubType,
        SQLLEN Length,
        SQLSMALLINT Precision,
        SQLSMALLINT Scale,
        SQLPOINTER DataPtr,
        SQLLEN* StringLengthPtr,
        SQLLEN* IndicatorPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DescriptorHandle", "RecNumber", "Type", "SubType", "Length", "Precision", "Scale", "DataPtr", "StringLengthPtr", "IndicatorPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetEnvAttr(jitter):
    """
    SQLRETURN SQLSetEnvAttr(
        SQLHENV EnvironmentHandle,
        SQLINTEGER Attribute,
        SQLPOINTER ValuePtr,
        SQLINTEGER StringLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnvironmentHandle", "Attribute", "ValuePtr", "StringLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetParam(jitter):
    """
    SQLRETURN SQLSetParam(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT ParameterNumber,
        SQLSMALLINT ValueType,
        SQLSMALLINT ParameterType,
        SQLULEN LengthPrecision,
        SQLSMALLINT ParameterScale,
        SQLPOINTER ParameterValue,
        SQLLEN* StrLen_or_Ind
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "ParameterNumber", "ValueType", "ParameterType", "LengthPrecision", "ParameterScale", "ParameterValue", "StrLen_or_Ind"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetPos(jitter):
    """
    SQLRETURN SQLSetPos(
        SQLHSTMT StatementHandle,
        SQLSETPOSIROW RowNumber,
        SQLUSMALLINT Operation,
        SQLUSMALLINT LockType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "RowNumber", "Operation", "LockType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetScrollOptions(jitter):
    """
    SQLRETURN SQLSetScrollOptions(
        SQLHSTMT hstmt,
        SQLUSMALLINT fConcurrency,
        SQLLEN crowKeyset,
        SQLUSMALLINT crowRowset
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hstmt", "fConcurrency", "crowKeyset", "crowRowset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetStmtAttr(jitter):
    """
    SQLRETURN SQLSetStmtAttr(
        SQLHSTMT StatementHandle,
        SQLINTEGER Attribute,
        SQLPOINTER ValuePtr,
        SQLINTEGER StringLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "Attribute", "ValuePtr", "StringLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetStmtAttr(jitter, get_str, set_str):
    """
    SQLRETURN SQLSetStmtAttr(
        SQLHSTMT StatementHandle,
        SQLINTEGER Attribute,
        SQLPOINTER ValuePtr,
        SQLINTEGER StringLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "Attribute", "ValuePtr", "StringLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSetStmtAttrA(jitter):
    odbc32_SQLSetStmtAttr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLSetStmtAttrW(jitter):
    odbc32_SQLSetStmtAttr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLSetStmtOption(jitter):
    """
    SQLRETURN SQLSetStmtOption(
        SQLHSTMT StatementHandle,
        SQLUSMALLINT Option,
        SQLULEN Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "Option", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSpecialColumns(jitter):
    """
    SQLRETURN SQLSpecialColumns(
        SQLHSTMT StatementHandle,
        SQLSMALLINT IdentifierType,
        SQLCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLCHAR* TableName,
        SQLSMALLINT NameLength3,
        SQLSMALLINT Scope,
        SQLSMALLINT Nullable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "IdentifierType", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3", "Scope", "Nullable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSpecialColumns(jitter, get_str, set_str):
    """
    SQLRETURN SQLSpecialColumns(
        SQLHSTMT StatementHandle,
        SQLSMALLINT IdentifierType,
        SQLTCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLTCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLTCHAR* TableName,
        SQLSMALLINT NameLength3,
        SQLSMALLINT Scope,
        SQLSMALLINT Nullable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "IdentifierType", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3", "Scope", "Nullable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLSpecialColumnsA(jitter):
    odbc32_SQLSpecialColumns(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLSpecialColumnsW(jitter):
    odbc32_SQLSpecialColumns(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLStatistics(jitter):
    """
    SQLRETURN SQLStatistics(
        SQLHSTMT StatementHandle,
        SQLCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLCHAR* TableName,
        SQLSMALLINT NameLength3,
        SQLUSMALLINT Unique,
        SQLUSMALLINT Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3", "Unique", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLStatistics(jitter, get_str, set_str):
    """
    SQLRETURN SQLStatistics(
        SQLHSTMT StatementHandle,
        SQLTCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLTCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLTCHAR* TableName,
        SQLSMALLINT NameLength3,
        SQLUSMALLINT Unique,
        SQLUSMALLINT Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3", "Unique", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLStatisticsA(jitter):
    odbc32_SQLStatistics(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLStatisticsW(jitter):
    odbc32_SQLStatistics(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLTablePrivileges(jitter):
    """
    SQLRETURN SQLTablePrivileges(
        SQLHSTMT StatementHandle,
        SQLCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLCHAR* TableName,
        SQLSMALLINT NameLength3
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLTablePrivileges(jitter, get_str, set_str):
    """
    SQLRETURN SQLTablePrivileges(
        SQLHSTMT StatementHandle,
        SQLTCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLTCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLTCHAR* TableName,
        SQLSMALLINT NameLength3
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLTablePrivilegesA(jitter):
    odbc32_SQLTablePrivileges(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLTablePrivilegesW(jitter):
    odbc32_SQLTablePrivileges(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLTables(jitter):
    """
    SQLRETURN SQLTables(
        SQLHSTMT StatementHandle,
        SQLCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLCHAR* TableName,
        SQLSMALLINT NameLength3,
        SQLCHAR* TableType,
        SQLSMALLINT NameLength4
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3", "TableType", "NameLength4"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLTables(jitter, get_str, set_str):
    """
    SQLRETURN SQLTables(
        SQLHSTMT StatementHandle,
        SQLTCHAR* CatalogName,
        SQLSMALLINT NameLength1,
        SQLTCHAR* SchemaName,
        SQLSMALLINT NameLength2,
        SQLTCHAR* TableName,
        SQLSMALLINT NameLength3,
        SQLTCHAR* TableType,
        SQLSMALLINT NameLength4
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatementHandle", "CatalogName", "NameLength1", "SchemaName", "NameLength2", "TableName", "NameLength3", "TableType", "NameLength4"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def odbc32_SQLTablesA(jitter):
    odbc32_SQLTables(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def odbc32_SQLTablesW(jitter):
    odbc32_SQLTables(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def odbc32_SQLTransact(jitter):
    """
    SQLRETURN SQLTransact(
        SQLHENV EnvironmentHandle,
        SQLHDBC ConnectionHandle,
        SQLUSMALLINT CompletionType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnvironmentHandle", "ConnectionHandle", "CompletionType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
