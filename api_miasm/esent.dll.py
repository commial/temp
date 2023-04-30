
def esent_JetAddColumn(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetAddColumn(JET_SESID sesid, JET_TABLEID tableid, JET_PCSTR szColumnName, const JET_COLUMNDEF* pcolumndef, const void* pvDefault, unsigned long cbDefault, JET_COLUMNID* pcolumnid)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "szColumnName", "pcolumndef", "pvDefault", "cbDefault", "pcolumnid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetAddColumnA(jitter):
    esent_JetAddColumn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetAddColumnW(jitter):
    esent_JetAddColumn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetAttachDatabase(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetAttachDatabase(JET_SESID sesid, JET_PCSTR szFilename, [JetOpenDatabaseFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "szFilename", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetAttachDatabaseA(jitter):
    esent_JetAttachDatabase(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetAttachDatabaseW(jitter):
    esent_JetAttachDatabase(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetAttachDatabase2(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetAttachDatabase2(JET_SESID sesid, JET_PCSTR szFilename, const unsigned long cpgDatabaseSizeMax, [JetOpenDatabaseFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "szFilename", "cpgDatabaseSizeMax", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetAttachDatabase2A(jitter):
    esent_JetAttachDatabase2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetAttachDatabase2W(jitter):
    esent_JetAttachDatabase2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetBackup(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetBackup(JET_PCSTR szBackupPath, [JetBackupFlags] grbit, JET_PFNSTATUS pfnStatus)
    """
    ret_ad, args = jitter.func_args_stdcall(["szBackupPath", "grbit", "pfnStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetBackupA(jitter):
    esent_JetBackup(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetBackupW(jitter):
    esent_JetBackup(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetBackupInstance(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetBackupInstance(JET_INSTANCE instance, JET_PCSTR szBackupPath, [JetBackupFlags] grbit, JET_PFNSTATUS pfnStatus)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "szBackupPath", "grbit", "pfnStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetBackupInstanceA(jitter):
    esent_JetBackupInstance(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetBackupInstanceW(jitter):
    esent_JetBackupInstance(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetBeginExternalBackup(jitter):
    """
    [esent.dll] JET_ERR JetBeginExternalBackup([JetBackupFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetBeginExternalBackupInstance(jitter):
    """
    [esent.dll] JET_ERR JetBeginExternalBackupInstance(JET_INSTANCE instance, [JetBackupFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetBeginSession(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetBeginSession(JET_INSTANCE instance, JET_SESID* psesid, JET_PCSTR szUserName, JET_PCSTR szPassword)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "psesid", "szUserName", "szPassword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetBeginSessionA(jitter):
    esent_JetBeginSession(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetBeginSessionW(jitter):
    esent_JetBeginSession(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetBeginTransaction(jitter):
    """
    [esent.dll] JET_ERR JetBeginTransaction(JET_SESID sesid)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetBeginTransaction2(jitter):
    """
    [esent.dll] JET_ERR JetBeginTransaction2(JET_SESID sesid, [JetBeginTransaction2Flags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCloseDatabase(jitter):
    """
    [esent.dll] JET_ERR JetCloseDatabase(JET_SESID sesid, JET_DBID dbid, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCloseFile(jitter):
    """
    [esent.dll] JET_ERR JetCloseFile(JET_HANDLE hfFile)
    """
    ret_ad, args = jitter.func_args_stdcall(["hfFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCloseFileInstance(jitter):
    """
    [esent.dll] JET_ERR JetCloseFileInstance(JET_INSTANCE instance, JET_HANDLE hfFile)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "hfFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCloseTable(jitter):
    """
    [esent.dll] JET_ERR JetCloseTable(JET_SESID sesid, JET_TABLEID tableid)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCommitTransaction(jitter):
    """
    [esent.dll] JET_ERR JetCommitTransaction(JET_SESID sesid, [JetCommitTransactionFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCompact(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCompact(JET_SESID sesid, JET_PCSTR szDatabaseSrc, JET_PCSTR szDatabaseDest, JET_PFNSTATUS pfnStatus, JET_CONVERT* pconvert, [JetCompactFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "szDatabaseSrc", "szDatabaseDest", "pfnStatus", "pconvert", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCompactA(jitter):
    esent_JetCompact(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCompactW(jitter):
    esent_JetCompact(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetComputeStats(jitter):
    """
    [esent.dll] JET_ERR JetComputeStats(JET_SESID sesid, JET_TABLEID tableid)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateDatabase(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCreateDatabase(JET_SESID sesid, JET_PCSTR szFilename, JET_PCSTR szConnect, JET_DBID* pdbid, [JetCreateDatabaseFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "szFilename", "szConnect", "pdbid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateDatabaseA(jitter):
    esent_JetCreateDatabase(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCreateDatabaseW(jitter):
    esent_JetCreateDatabase(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetCreateDatabase2(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCreateDatabase2(JET_SESID sesid, JET_PCSTR szFilename, const unsigned long cpgDatabaseSizeMax, JET_DBID* pdbid, [JetCreateDatabaseFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "szFilename", "cpgDatabaseSizeMax", "pdbid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateDatabase2A(jitter):
    esent_JetCreateDatabase2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCreateDatabase2W(jitter):
    esent_JetCreateDatabase2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetCreateIndex(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCreateIndex(JET_SESID sesid, JET_TABLEID tableid, JET_PCSTR szIndexName, [JetCreateIndexFlags] grbit, JET_PCSTR szKey, unsigned long cbKey, unsigned long lDensity)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "szIndexName", "grbit", "szKey", "cbKey", "lDensity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateIndexA(jitter):
    esent_JetCreateIndex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCreateIndexW(jitter):
    esent_JetCreateIndex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetCreateIndex2(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCreateIndex2(JET_SESID sesid, JET_TABLEID tableid, JET_INDEXCREATE* pindexcreate, unsigned long cIndexCreate)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pindexcreate", "cIndexCreate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateIndex2A(jitter):
    esent_JetCreateIndex2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCreateIndex2W(jitter):
    esent_JetCreateIndex2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetCreateInstance(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCreateInstance(JET_INSTANCE* pinstance, JET_PCSTR szInstanceName)
    """
    ret_ad, args = jitter.func_args_stdcall(["pinstance", "szInstanceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateInstanceA(jitter):
    esent_JetCreateInstance(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCreateInstanceW(jitter):
    esent_JetCreateInstance(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetCreateInstance2(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCreateInstance2(JET_INSTANCE* pinstance, JET_PCSTR szInstanceName, JET_PCSTR szDisplayName, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["pinstance", "szInstanceName", "szDisplayName", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateInstance2A(jitter):
    esent_JetCreateInstance2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCreateInstance2W(jitter):
    esent_JetCreateInstance2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetCreateTable(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCreateTable(JET_SESID sesid, JET_DBID dbid, JET_PCSTR szTableName, unsigned long lPages, unsigned long lDensity, JET_TABLEID* ptableid)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "szTableName", "lPages", "lDensity", "ptableid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateTableA(jitter):
    esent_JetCreateTable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCreateTableW(jitter):
    esent_JetCreateTable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetCreateTableColumnIndex(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCreateTableColumnIndex(JET_SESID sesid, JET_DBID dbid, JET_TABLECREATE* ptablecreate)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "ptablecreate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateTableColumnIndexA(jitter):
    esent_JetCreateTableColumnIndex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCreateTableColumnIndexW(jitter):
    esent_JetCreateTableColumnIndex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetCreateTableColumnIndex2(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCreateTableColumnIndex2(JET_SESID sesid, JET_DBID dbid, JET_TABLECREATE2* ptablecreate)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "ptablecreate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateTableColumnIndex2A(jitter):
    esent_JetCreateTableColumnIndex2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCreateTableColumnIndex2W(jitter):
    esent_JetCreateTableColumnIndex2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetDefragment(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetDefragment(JET_SESID sesid, JET_DBID dbid, JET_PCSTR szTableName, unsigned long* pcPasses, unsigned long* pcSeconds, [JetDefragmentFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "szTableName", "pcPasses", "pcSeconds", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetDefragmentA(jitter):
    esent_JetDefragment(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetDefragmentW(jitter):
    esent_JetDefragment(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetDefragment2(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetDefragment2(JET_SESID sesid, JET_DBID dbid, JET_PCSTR szTableName, unsigned long* pcPasses, unsigned long* pcSeconds, JET_CALLBACK callback, [JetDefragmentFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "szTableName", "pcPasses", "pcSeconds", "callback", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetDefragment2A(jitter):
    esent_JetDefragment2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetDefragment2W(jitter):
    esent_JetDefragment2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetDelete(jitter):
    """
    [esent.dll] JET_ERR JetDelete(JET_SESID sesid, JET_TABLEID tableid)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetDeleteColumn(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetDeleteColumn(JET_SESID sesid, JET_TABLEID tableid, JET_PCSTR szColumnName)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "szColumnName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetDeleteColumnA(jitter):
    esent_JetDeleteColumn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetDeleteColumnW(jitter):
    esent_JetDeleteColumn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetDeleteColumn2(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetDeleteColumn2(JET_SESID sesid, JET_TABLEID tableid, JET_PCSTR szColumnName, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "szColumnName", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetDeleteColumn2A(jitter):
    esent_JetDeleteColumn2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetDeleteColumn2W(jitter):
    esent_JetDeleteColumn2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetDeleteIndex(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetDeleteIndex(JET_SESID sesid, JET_TABLEID tableid, JET_PCSTR szIndexName)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "szIndexName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetDeleteIndexA(jitter):
    esent_JetDeleteIndex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetDeleteIndexW(jitter):
    esent_JetDeleteIndex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetDeleteTable(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetDeleteTable(JET_SESID sesid, JET_DBID dbid, JET_PCSTR szTableName)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "szTableName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetDeleteTableA(jitter):
    esent_JetDeleteTable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetDeleteTableW(jitter):
    esent_JetDeleteTable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetDetachDatabase(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetDetachDatabase(JET_SESID sesid, JET_PCSTR szFilename)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "szFilename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetDetachDatabaseA(jitter):
    esent_JetDetachDatabase(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetDetachDatabaseW(jitter):
    esent_JetDetachDatabase(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetDetachDatabase2(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetDetachDatabase2(JET_SESID sesid, JET_PCSTR szFilename, [JetDetachDatabase2Flags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "szFilename", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetDetachDatabase2A(jitter):
    esent_JetDetachDatabase2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetDetachDatabase2W(jitter):
    esent_JetDetachDatabase2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetDupCursor(jitter):
    """
    [esent.dll] JET_ERR JetDupCursor(JET_SESID sesid, JET_TABLEID tableid, JET_TABLEID* ptableid, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "ptableid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetDupSession(jitter):
    """
    [esent.dll] JET_ERR JetDupSession(JET_SESID sesid, JET_SESID* psesid)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "psesid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetEnableMultiInstance(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetEnableMultiInstance(JET_SETSYSPARAM* psetsysparam, unsigned long csetsysparam, unsigned long* pcsetsucceed)
    """
    ret_ad, args = jitter.func_args_stdcall(["psetsysparam", "csetsysparam", "pcsetsucceed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetEnableMultiInstanceA(jitter):
    esent_JetEnableMultiInstance(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetEnableMultiInstanceW(jitter):
    esent_JetEnableMultiInstance(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetEndExternalBackup(jitter):
    """
    [esent.dll] JET_ERR JetEndExternalBackup()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetEndExternalBackupInstance(jitter):
    """
    [esent.dll] JET_ERR JetEndExternalBackupInstance(JET_INSTANCE instance)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetEndExternalBackupInstance2(jitter):
    """
    [esent.dll] JET_ERR JetEndExternalBackupInstance2(JET_INSTANCE instance, [JetEndExternalBackupInstance2Flags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetEndSession(jitter):
    """
    [esent.dll] JET_ERR JetEndSession(JET_SESID sesid, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetEnumerateColumns(jitter):
    """
    [esent.dll] JET_ERR JetEnumerateColumns(JET_SESID sesid, JET_TABLEID tableid, unsigned long cEnumColumnId, JET_ENUMCOLUMNID* rgEnumColumnId, unsigned long* pcEnumColumn, JET_ENUMCOLUMN** prgEnumColumn, JET_PFNREALLOC pfnRealloc, void* pvReallocContext, unsigned long cbDataMost, [JetEnumerateColumnsFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "cEnumColumnId", "rgEnumColumnId", "pcEnumColumn", "prgEnumColumn", "pfnRealloc", "pvReallocContext", "cbDataMost", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetEscrowUpdate(jitter):
    """
    [esent.dll] JET_ERR JetEscrowUpdate(JET_SESID sesid, JET_TABLEID tableid, JET_COLUMNID columnid, void* pv, unsigned long cbMax, void* pvOld, unsigned long cbOldMax, unsigned long* pcbOldActual, [JetEscrowUpdateFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "columnid", "pv", "cbMax", "pvOld", "cbOldMax", "pcbOldActual", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetExternalRestore(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetExternalRestore(JET_PSTR szCheckpointFilePath, JET_PSTR szLogPath, JET_RSTMAP* rgrstmap, long crstfilemap, JET_PSTR szBackupLogPath, long genLow, long genHigh, JET_PFNSTATUS pfn)
    """
    ret_ad, args = jitter.func_args_stdcall(["szCheckpointFilePath", "szLogPath", "rgrstmap", "crstfilemap", "szBackupLogPath", "genLow", "genHigh", "pfn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetExternalRestoreA(jitter):
    esent_JetExternalRestore(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetExternalRestoreW(jitter):
    esent_JetExternalRestore(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetExternalRestore2(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetExternalRestore2(JET_PSTR szCheckpointFilePath, JET_PSTR szLogPath, JET_RSTMAP* rgrstmap, long crstfilemap, JET_PSTR szBackupLogPath, JET_LOGINFO* pLogInfo, JET_PSTR szTargetInstanceName, JET_PSTR szTargetInstanceLogPath, JET_PSTR szTargetInstanceCheckpointPath, JET_PFNSTATUS pfn)
    """
    ret_ad, args = jitter.func_args_stdcall(["szCheckpointFilePath", "szLogPath", "rgrstmap", "crstfilemap", "szBackupLogPath", "pLogInfo", "szTargetInstanceName", "szTargetInstanceLogPath", "szTargetInstanceCheckpointPath", "pfn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetExternalRestore2A(jitter):
    esent_JetExternalRestore2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetExternalRestore2W(jitter):
    esent_JetExternalRestore2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetFreeBuffer(jitter):
    """
    [esent.dll] JET_ERR JetFreeBuffer(char* pbBuf)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbBuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetAttachInfo(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetAttachInfo(tchar* szz, unsigned long cbMax, unsigned long* pcbActual)
    """
    ret_ad, args = jitter.func_args_stdcall(["szz", "cbMax", "pcbActual"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetAttachInfoA(jitter):
    esent_JetGetAttachInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetAttachInfoW(jitter):
    esent_JetGetAttachInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetAttachInfoInstance(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetAttachInfoInstance(JET_INSTANCE instance, tchar* szz, unsigned long cbMax, unsigned long* pcbActual)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "szz", "cbMax", "pcbActual"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetAttachInfoInstanceA(jitter):
    esent_JetGetAttachInfoInstance(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetAttachInfoInstanceW(jitter):
    esent_JetGetAttachInfoInstance(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetBookmark(jitter):
    """
    [esent.dll] JET_ERR JetGetBookmark(JET_SESID sesid, JET_TABLEID tableid, void* pvBookmark, unsigned long cbMax, unsigned long* pcbActual)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pvBookmark", "cbMax", "pcbActual"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetColumnInfo(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetColumnInfo(JET_SESID sesid, JET_DBID dbid, JET_PCSTR szTableName, JET_PCSTR szColumnName, void* pvResult, unsigned long cbMax, unsigned long InfoLevel)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "szTableName", "szColumnName", "pvResult", "cbMax", "InfoLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetColumnInfoA(jitter):
    esent_JetGetColumnInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetColumnInfoW(jitter):
    esent_JetGetColumnInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetCurrentIndex(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetCurrentIndex(JET_SESID sesid, JET_TABLEID tableid, JET_PSTR szIndexName, unsigned long cchIndexName)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "szIndexName", "cchIndexName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetCurrentIndexA(jitter):
    esent_JetGetCurrentIndex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetCurrentIndexW(jitter):
    esent_JetGetCurrentIndex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetCursorInfo(jitter):
    """
    [esent.dll] JET_ERR JetGetCursorInfo(JET_SESID sesid, JET_TABLEID tableid, void* pvResult, unsigned long cbMax, unsigned long InfoLevel)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pvResult", "cbMax", "InfoLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetDatabaseFileInfo(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetDatabaseFileInfo(JET_PCSTR szDatabaseName, void* pvResult, unsigned long cbMax, unsigned long InfoLevel)
    """
    ret_ad, args = jitter.func_args_stdcall(["szDatabaseName", "pvResult", "cbMax", "InfoLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetDatabaseFileInfoA(jitter):
    esent_JetGetDatabaseFileInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetDatabaseFileInfoW(jitter):
    esent_JetGetDatabaseFileInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetDatabaseInfo(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetDatabaseInfo(JET_SESID sesid, JET_DBID dbid, void* pvResult, unsigned long cbMax, unsigned long InfoLevel)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "pvResult", "cbMax", "InfoLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetDatabaseInfoA(jitter):
    esent_JetGetDatabaseInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetDatabaseInfoW(jitter):
    esent_JetGetDatabaseInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetIndexInfo(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetIndexInfo(JET_SESID sesid, JET_DBID dbid, JET_PCSTR szTableName, JET_PCSTR szIndexName, void* pvResult, unsigned long cbResult, unsigned long InfoLevel)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "szTableName", "szIndexName", "pvResult", "cbResult", "InfoLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetIndexInfoA(jitter):
    esent_JetGetIndexInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetIndexInfoW(jitter):
    esent_JetGetIndexInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetInstanceInfo(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetInstanceInfo(unsigned long* pcInstanceInfo, JET_INSTANCE_INFO** paInstanceInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["pcInstanceInfo", "paInstanceInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetInstanceInfoA(jitter):
    esent_JetGetInstanceInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetInstanceInfoW(jitter):
    esent_JetGetInstanceInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetInstanceMiscInfo(jitter):
    """
    [esent.dll] JET_ERR JetGetInstanceMiscInfo(JET_INSTANCE instance, void* pvResult, unsigned long cbMax, unsigned long InfoLevel)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "pvResult", "cbMax", "InfoLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetLock(jitter):
    """
    [esent.dll] JET_ERR JetGetLock(JET_SESID sesid, JET_TABLEID tableid, [JetGetLockFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetLogInfo(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetLogInfo(tchar* szz, unsigned long cbMax, unsigned long* pcbActual)
    """
    ret_ad, args = jitter.func_args_stdcall(["szz", "cbMax", "pcbActual"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetLogInfoA(jitter):
    esent_JetGetLogInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetLogInfoW(jitter):
    esent_JetGetLogInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetLogInfoInstance(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetLogInfoInstance(JET_INSTANCE instance, tchar* szz, unsigned long cbMax, unsigned long* pcbActual)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "szz", "cbMax", "pcbActual"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetLogInfoInstanceA(jitter):
    esent_JetGetLogInfoInstance(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetLogInfoInstanceW(jitter):
    esent_JetGetLogInfoInstance(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetLogInfoInstance2(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetLogInfoInstance2(JET_INSTANCE instance, tchar* szz, unsigned long cbMax, unsigned long* pcbActual, JET_LOGINFO* pLogInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "szz", "cbMax", "pcbActual", "pLogInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetLogInfoInstance2A(jitter):
    esent_JetGetLogInfoInstance2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetLogInfoInstance2W(jitter):
    esent_JetGetLogInfoInstance2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetLS(jitter):
    """
    [esent.dll] JET_ERR JetGetLS(JET_SESID sesid, JET_TABLEID tableid, JET_LS* pls, [JetGetLSFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pls", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetObjectInfo(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetObjectInfo(JET_SESID sesid, JET_DBID dbid, JET_OBJTYP objtyp, JET_PCSTR szContainerName, JET_PCSTR szObjectName, void* pvResult, unsigned long cbMax, unsigned long InfoLevel)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "objtyp", "szContainerName", "szObjectName", "pvResult", "cbMax", "InfoLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetObjectInfoA(jitter):
    esent_JetGetObjectInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetObjectInfoW(jitter):
    esent_JetGetObjectInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetRecordPosition(jitter):
    """
    [esent.dll] JET_ERR JetGetRecordPosition(JET_SESID sesid, JET_TABLEID tableid, JET_RECPOS* precpos, unsigned long cbRecpos)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "precpos", "cbRecpos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetRecordSize(jitter):
    """
    [esent.dll] JET_ERR JetGetRecordSize(JET_SESID sesid, JET_TABLEID tableid, JET_RECSIZE* precsize, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "precsize", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetSecondaryIndexBookmark(jitter):
    """
    [esent.dll] JET_ERR JetGetSecondaryIndexBookmark(JET_SESID sesid, JET_TABLEID tableid, void* pvSecondaryKey, unsigned long cbSecondaryKeyMax, unsigned long* pcbSecondaryKeyActual, void* pvPrimaryBookmark, unsigned long cbPrimaryBookmarkMax, unsigned long* pcbPrimaryKeyActual, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pvSecondaryKey", "cbSecondaryKeyMax", "pcbSecondaryKeyActual", "pvPrimaryBookmark", "cbPrimaryBookmarkMax", "pcbPrimaryKeyActual", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetSystemParameter(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetSystemParameter(JET_INSTANCE instance, JET_SESID sesid, [JET_param] paramid, JET_API_PTR* plParam, JET_PSTR szParam, unsigned long cbMax)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "sesid", "paramid", "plParam", "szParam", "cbMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetSystemParameterA(jitter):
    esent_JetGetSystemParameter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetSystemParameterW(jitter):
    esent_JetGetSystemParameter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetTableColumnInfo(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetTableColumnInfo(JET_SESID sesid, JET_TABLEID tableid, JET_PCSTR szColumnName, void* pvResult, unsigned long cbMax, unsigned long InfoLevel)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "szColumnName", "pvResult", "cbMax", "InfoLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetTableColumnInfoA(jitter):
    esent_JetGetTableColumnInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetTableColumnInfoW(jitter):
    esent_JetGetTableColumnInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetTableIndexInfo(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetTableIndexInfo(JET_SESID sesid, JET_TABLEID tableid, JET_PCSTR szIndexName, void* pvResult, unsigned long cbResult, unsigned long InfoLevel)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "szIndexName", "pvResult", "cbResult", "InfoLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetTableIndexInfoA(jitter):
    esent_JetGetTableIndexInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetTableIndexInfoW(jitter):
    esent_JetGetTableIndexInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetTableInfo(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetTableInfo(JET_SESID sesid, JET_TABLEID tableid, void* pvResult, unsigned long cbMax, unsigned long InfoLevel)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pvResult", "cbMax", "InfoLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetTableInfoA(jitter):
    esent_JetGetTableInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetTableInfoW(jitter):
    esent_JetGetTableInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetThreadStats(jitter):
    """
    [esent.dll] JET_ERR JetGetThreadStats(void* pvResult, unsigned long cbMax)
    """
    ret_ad, args = jitter.func_args_stdcall(["pvResult", "cbMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetTruncateLogInfoInstance(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetGetTruncateLogInfoInstance(JET_INSTANCE instance, tchar* szz, unsigned long cbMax, unsigned long* pcbActual)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "szz", "cbMax", "pcbActual"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetTruncateLogInfoInstanceA(jitter):
    esent_JetGetTruncateLogInfoInstance(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetGetTruncateLogInfoInstanceW(jitter):
    esent_JetGetTruncateLogInfoInstance(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetVersion(jitter):
    """
    [esent.dll] JET_ERR JetGetVersion(JET_SESID sesid, unsigned long* pwVersion)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "pwVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGotoBookmark(jitter):
    """
    [esent.dll] JET_ERR JetGotoBookmark(JET_SESID sesid, JET_TABLEID tableid, void* pvBookmark, unsigned long cbBookmark)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pvBookmark", "cbBookmark"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGotoPosition(jitter):
    """
    [esent.dll] JET_ERR JetGotoPosition(JET_SESID sesid, JET_TABLEID tableid, JET_RECPOS* precpos)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "precpos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGotoSecondaryIndexBookmark(jitter):
    """
    [esent.dll] JET_ERR JetGotoSecondaryIndexBookmark(JET_SESID sesid, JET_TABLEID tableid, void* pvSecondaryKey, unsigned long cbSecondaryKey, void* pvPrimaryBookmark, unsigned long cbPrimaryBookmark, [JetGotoSecondaryIndexBookmarkFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pvSecondaryKey", "cbSecondaryKey", "pvPrimaryBookmark", "cbPrimaryBookmark", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGrowDatabase(jitter):
    """
    [esent.dll] JET_ERR JetGrowDatabase(JET_SESID sesid, JET_DBID dbid, unsigned long cpg, unsigned long* pcpgReal)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "cpg", "pcpgReal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetIdle(jitter):
    """
    [esent.dll] JET_ERR JetIdle(JET_SESID sesid, [JetIdleFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetIndexRecordCount(jitter):
    """
    [esent.dll] JET_ERR JetIndexRecordCount(JET_SESID sesid, JET_TABLEID tableid, unsigned long* pcrec, unsigned long crecMax)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pcrec", "crecMax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetInit(jitter):
    """
    [esent.dll] JET_ERR JetInit(JET_INSTANCE* pinstance)
    """
    ret_ad, args = jitter.func_args_stdcall(["pinstance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetInit2(jitter):
    """
    [esent.dll] JET_ERR JetInit2(JET_INSTANCE* pinstance, [JetInitFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["pinstance", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetInit3(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetInit3(JET_INSTANCE* pinstance, JET_RSTINFO* prstInfo, [JetInitFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["pinstance", "prstInfo", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetInit3A(jitter):
    esent_JetInit3(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetInit3W(jitter):
    esent_JetInit3(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetIntersectIndexes(jitter):
    """
    [esent.dll] JET_ERR JetIntersectIndexes(JET_SESID sesid, JET_INDEXRANGE* rgindexrange, unsigned long cindexrange, JET_RECORDLIST* precordlist, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "rgindexrange", "cindexrange", "precordlist", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetMakeKey(jitter):
    """
    [esent.dll] JET_ERR JetMakeKey(JET_SESID sesid, JET_TABLEID tableid, const void* pvData, unsigned long cbData, [JetMakeKeyFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pvData", "cbData", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetMove(jitter):
    """
    [esent.dll] JET_ERR JetMove(JET_SESID sesid, JET_TABLEID tableid, [JetMoveRow] cRow, [JetMoveFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "cRow", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOpenDatabase(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetOpenDatabase(JET_SESID sesid, JET_PCSTR szFilename, JET_PCSTR szConnect, JET_DBID* pdbid, [JetOpenDatabaseFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "szFilename", "szConnect", "pdbid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOpenDatabaseA(jitter):
    esent_JetOpenDatabase(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetOpenDatabaseW(jitter):
    esent_JetOpenDatabase(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetOpenFile(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetOpenFile(JET_PCSTR szFileName, JET_HANDLE* phfFile, unsigned long* pulFileSizeLow, unsigned long* pulFileSizeHigh)
    """
    ret_ad, args = jitter.func_args_stdcall(["szFileName", "phfFile", "pulFileSizeLow", "pulFileSizeHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOpenFileA(jitter):
    esent_JetOpenFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetOpenFileW(jitter):
    esent_JetOpenFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetOpenFileInstance(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetOpenFileInstance(JET_INSTANCE instance, JET_PCSTR szFileName, JET_HANDLE* phfFile, unsigned long* pulFileSizeLow, unsigned long* pulFileSizeHigh)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "szFileName", "phfFile", "pulFileSizeLow", "pulFileSizeHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOpenFileInstanceA(jitter):
    esent_JetOpenFileInstance(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetOpenFileInstanceW(jitter):
    esent_JetOpenFileInstance(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetOpenTable(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetOpenTable(JET_SESID sesid, JET_DBID dbid, JET_PCSTR szTableName, const void* pvParameters, unsigned long cbParameters, [JetOpenTableFlags] grbit, JET_TABLEID* ptableid)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "szTableName", "pvParameters", "cbParameters", "grbit", "ptableid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOpenTableA(jitter):
    esent_JetOpenTable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetOpenTableW(jitter):
    esent_JetOpenTable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetOpenTemporaryTable(jitter):
    """
    [esent.dll] JET_ERR JetOpenTemporaryTable(JET_SESID sesid, JET_OPENTEMPORARYTABLE* popentemporarytable)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "popentemporarytable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOpenTempTable(jitter):
    """
    [esent.dll] JET_ERR JetOpenTempTable(JET_SESID sesid, const JET_COLUMNDEF* prgcolumndef, unsigned long ccolumn, [JetOpenTempTableFlags] grbit, JET_TABLEID* ptableid, JET_COLUMNID* prgcolumnid)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "prgcolumndef", "ccolumn", "grbit", "ptableid", "prgcolumnid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOpenTempTable2(jitter):
    """
    [esent.dll] JET_ERR JetOpenTempTable2(JET_SESID sesid, const JET_COLUMNDEF* prgcolumndef, unsigned long ccolumn, unsigned long lcid, [JetOpenTempTableFlags] grbit, JET_TABLEID* ptableid, JET_COLUMNID* prgcolumnid)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "prgcolumndef", "ccolumn", "lcid", "grbit", "ptableid", "prgcolumnid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOpenTempTable3(jitter):
    """
    [esent.dll] JET_ERR JetOpenTempTable3(JET_SESID sesid, const JET_COLUMNDEF* prgcolumndef, unsigned long ccolumn, JET_UNICODEINDEX* pidxunicode, [JetOpenTempTableFlags] grbit, JET_TABLEID* ptableid, JET_COLUMNID* prgcolumnid)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "prgcolumndef", "ccolumn", "pidxunicode", "grbit", "ptableid", "prgcolumnid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOSSnapshotAbort(jitter):
    """
    [esent.dll] JET_ERR JetOSSnapshotAbort(const JET_OSSNAPID snapId, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["snapId", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOSSnapshotEnd(jitter):
    """
    [esent.dll] JET_ERR JetOSSnapshotEnd(const JET_OSSNAPID snapId, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["snapId", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOSSnapshotFreeze(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetOSSnapshotFreeze(const JET_OSSNAPID snapId, unsigned long* pcInstanceInfo, JET_INSTANCE_INFO** paInstanceInfo, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["snapId", "pcInstanceInfo", "paInstanceInfo", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOSSnapshotFreezeA(jitter):
    esent_JetOSSnapshotFreeze(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetOSSnapshotFreezeW(jitter):
    esent_JetOSSnapshotFreeze(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetOSSnapshotGetFreezeInfo(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetOSSnapshotGetFreezeInfo(const JET_OSSNAPID snapId, unsigned long* pcInstanceInfo, JET_INSTANCE_INFO** paInstanceInfo, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["snapId", "pcInstanceInfo", "paInstanceInfo", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOSSnapshotGetFreezeInfoA(jitter):
    esent_JetOSSnapshotGetFreezeInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetOSSnapshotGetFreezeInfoW(jitter):
    esent_JetOSSnapshotGetFreezeInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetOSSnapshotPrepare(jitter):
    """
    [esent.dll] JET_ERR JetOSSnapshotPrepare(JET_OSSNAPID* psnapId, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["psnapId", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOSSnapshotPrepareInstance(jitter):
    """
    [esent.dll] JET_ERR JetOSSnapshotPrepareInstance(JET_OSSNAPID snapId, JET_INSTANCE instance, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["snapId", "instance", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOSSnapshotThaw(jitter):
    """
    [esent.dll] JET_ERR JetOSSnapshotThaw(const JET_OSSNAPID snapId, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["snapId", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOSSnapshotTruncateLog(jitter):
    """
    [esent.dll] JET_ERR JetOSSnapshotTruncateLog(const JET_OSSNAPID snapId, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["snapId", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetOSSnapshotTruncateLogInstance(jitter):
    """
    [esent.dll] JET_ERR JetOSSnapshotTruncateLogInstance(const JET_OSSNAPID snapId, JET_INSTANCE instance, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["snapId", "instance", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetPrepareUpdate(jitter):
    """
    [esent.dll] JET_ERR JetPrepareUpdate(JET_SESID sesid, JET_TABLEID tableid, [JetPrepareUpdateOption] prep)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "prep"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetReadFile(jitter):
    """
    [esent.dll] JET_ERR JetReadFile(JET_HANDLE hfFile, void* pv, unsigned long cb, unsigned long* pcbActual)
    """
    ret_ad, args = jitter.func_args_stdcall(["hfFile", "pv", "cb", "pcbActual"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetReadFileInstance(jitter):
    """
    [esent.dll] JET_ERR JetReadFileInstance(JET_INSTANCE instance, JET_HANDLE hfFile, void* pv, unsigned long cb, unsigned long* pcb)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "hfFile", "pv", "cb", "pcb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetRegisterCallback(jitter):
    """
    [esent.dll] JET_ERR JetRegisterCallback(JET_SESID sesid, JET_TABLEID tableid, JET_CBTYP cbtyp, JET_CALLBACK pCallback, void* pvContext, JET_HANDLE* phCallbackId)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "cbtyp", "pCallback", "pvContext", "phCallbackId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetRenameColumn(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetRenameColumn(JET_SESID sesid, JET_TABLEID tableid, JET_PCSTR szName, JET_PCSTR szNameNew, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "szName", "szNameNew", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetRenameColumnA(jitter):
    esent_JetRenameColumn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetRenameColumnW(jitter):
    esent_JetRenameColumn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetRenameTable(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetRenameTable(JET_SESID sesid, JET_DBID dbid, JET_PCSTR szName, JET_PCSTR szNameNew)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "szName", "szNameNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetRenameTableA(jitter):
    esent_JetRenameTable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetRenameTableW(jitter):
    esent_JetRenameTable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetResetSessionContext(jitter):
    """
    [esent.dll] JET_ERR JetResetSessionContext(JET_SESID sesid)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetResetTableSequential(jitter):
    """
    [esent.dll] JET_ERR JetResetTableSequential(JET_SESID sesid, JET_TABLEID tableid, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetRestore(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetRestore(JET_PCSTR sz, JET_PFNSTATUS pfn)
    """
    ret_ad, args = jitter.func_args_stdcall(["sz", "pfn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetRestoreA(jitter):
    esent_JetRestore(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetRestoreW(jitter):
    esent_JetRestore(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetRestore2(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetRestore2(JET_PCSTR sz, JET_PCSTR szDest, JET_PFNSTATUS pfn)
    """
    ret_ad, args = jitter.func_args_stdcall(["sz", "szDest", "pfn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetRestore2A(jitter):
    esent_JetRestore2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetRestore2W(jitter):
    esent_JetRestore2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetRestoreInstance(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetRestoreInstance(JET_INSTANCE instance, JET_PCSTR sz, JET_PCSTR szDest, JET_PFNSTATUS pfn)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "sz", "szDest", "pfn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetRestoreInstanceA(jitter):
    esent_JetRestoreInstance(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetRestoreInstanceW(jitter):
    esent_JetRestoreInstance(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetRetrieveColumn(jitter):
    """
    [esent.dll] JET_ERR JetRetrieveColumn(JET_SESID sesid, JET_TABLEID tableid, JET_COLUMNID columnid, void* pvData, unsigned long cbData, unsigned long* pcbActual, [JetRetrieveColumnFlags] grbit, JET_RETINFO* pretinfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "columnid", "pvData", "cbData", "pcbActual", "grbit", "pretinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetRetrieveColumns(jitter):
    """
    [esent.dll] JET_ERR JetRetrieveColumns(JET_SESID sesid, JET_TABLEID tableid, JET_RETRIEVECOLUMN* pretrievecolumn, unsigned long cretrievecolumn)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pretrievecolumn", "cretrievecolumn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetRetrieveKey(jitter):
    """
    [esent.dll] JET_ERR JetRetrieveKey(JET_SESID sesid, JET_TABLEID tableid, void* pvData, unsigned long cbMax, unsigned long* pcbActual, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pvData", "cbMax", "pcbActual", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetRollback(jitter):
    """
    [esent.dll] JET_ERR JetRollback(JET_SESID sesid, [JetRollbackFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSeek(jitter):
    """
    [esent.dll] JET_ERR JetSeek(JET_SESID sesid, JET_TABLEID tableid, [JetSeekFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetColumn(jitter):
    """
    [esent.dll] JET_ERR JetSetColumn(JET_SESID sesid, JET_TABLEID tableid, JET_COLUMNID columnid, const void* pvData, unsigned long cbData, [JetSetColumnFlags] grbit, JET_SETINFO* psetinfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "columnid", "pvData", "cbData", "grbit", "psetinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetColumnDefaultValue(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetSetColumnDefaultValue(JET_SESID sesid, JET_DBID dbid, JET_PCSTR szTableName, JET_PCSTR szColumnName, const void* pvData, const unsigned long cbData, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "szTableName", "szColumnName", "pvData", "cbData", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetColumnDefaultValueA(jitter):
    esent_JetSetColumnDefaultValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetSetColumnDefaultValueW(jitter):
    esent_JetSetColumnDefaultValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetSetColumns(jitter):
    """
    [esent.dll] JET_ERR JetSetColumns(JET_SESID sesid, JET_TABLEID tableid, JET_SETCOLUMN* psetcolumn, unsigned long csetcolumn)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "psetcolumn", "csetcolumn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetCurrentIndex(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetSetCurrentIndex(JET_SESID sesid, JET_TABLEID tableid, JET_PCSTR szIndexName)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "szIndexName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetCurrentIndexA(jitter):
    esent_JetSetCurrentIndex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetSetCurrentIndexW(jitter):
    esent_JetSetCurrentIndex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetSetCurrentIndex2(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetSetCurrentIndex2(JET_SESID sesid, JET_TABLEID tableid, JET_PCSTR szIndexName, [JetSetCurrentIndexFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "szIndexName", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetCurrentIndex2A(jitter):
    esent_JetSetCurrentIndex2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetSetCurrentIndex2W(jitter):
    esent_JetSetCurrentIndex2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetSetCurrentIndex3(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetSetCurrentIndex3(JET_SESID sesid, JET_TABLEID tableid, JET_PCSTR szIndexName, [JetSetCurrentIndexFlags] grbit, unsigned long itagSequence)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "szIndexName", "grbit", "itagSequence"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetCurrentIndex3A(jitter):
    esent_JetSetCurrentIndex3(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetSetCurrentIndex3W(jitter):
    esent_JetSetCurrentIndex3(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetSetCurrentIndex4(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetSetCurrentIndex4(JET_SESID sesid, JET_TABLEID tableid, JET_PCSTR szIndexName, JET_INDEXID* pindexid, [JetSetCurrentIndexFlags] grbit, unsigned long itagSequence)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "szIndexName", "pindexid", "grbit", "itagSequence"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetCurrentIndex4A(jitter):
    esent_JetSetCurrentIndex4(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetSetCurrentIndex4W(jitter):
    esent_JetSetCurrentIndex4(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetSetDatabaseSize(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetSetDatabaseSize(JET_SESID sesid, JET_PCSTR szDatabaseName, unsigned long cpg, unsigned long* pcpgReal)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "szDatabaseName", "cpg", "pcpgReal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetDatabaseSizeA(jitter):
    esent_JetSetDatabaseSize(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetSetDatabaseSizeW(jitter):
    esent_JetSetDatabaseSize(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetSetIndexRange(jitter):
    """
    [esent.dll] JET_ERR JetSetIndexRange(JET_SESID sesid, JET_TABLEID tableidSrc, [JetSetIndexRangeFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableidSrc", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetLS(jitter):
    """
    [esent.dll] JET_ERR JetSetLS(JET_SESID sesid, JET_TABLEID tableid, JET_LS ls, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "ls", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetSessionContext(jitter):
    """
    [esent.dll] JET_ERR JetSetSessionContext(JET_SESID sesid, JET_API_PTR ulContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "ulContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetSystemParameter(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetSetSystemParameter(JET_INSTANCE* pinstance, JET_SESID sesid, [JET_param] paramid, JET_API_PTR lParam, JET_PCSTR szParam)
    """
    ret_ad, args = jitter.func_args_stdcall(["pinstance", "sesid", "paramid", "lParam", "szParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetSystemParameterA(jitter):
    esent_JetSetSystemParameter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetSetSystemParameterW(jitter):
    esent_JetSetSystemParameter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetSetTableSequential(jitter):
    """
    [esent.dll] JET_ERR JetSetTableSequential(JET_SESID sesid, JET_TABLEID tableid, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetStopBackup(jitter):
    """
    [esent.dll] JET_ERR JetStopBackup()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetStopBackupInstance(jitter):
    """
    [esent.dll] JET_ERR JetStopBackupInstance(JET_INSTANCE instance)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetStopService(jitter):
    """
    [esent.dll] JET_ERR JetStopService()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetStopServiceInstance(jitter):
    """
    [esent.dll] JET_ERR JetStopServiceInstance(JET_INSTANCE instance)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetTerm(jitter):
    """
    [esent.dll] JET_ERR JetTerm(JET_INSTANCE instance)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetTerm2(jitter):
    """
    [esent.dll] JET_ERR JetTerm2(JET_INSTANCE instance, [JetTerm2Flags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetTruncateLog(jitter):
    """
    [esent.dll] JET_ERR JetTruncateLog()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetTruncateLogInstance(jitter):
    """
    [esent.dll] JET_ERR JetTruncateLogInstance(JET_INSTANCE instance)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetUnregisterCallback(jitter):
    """
    [esent.dll] JET_ERR JetUnregisterCallback(JET_SESID sesid, JET_TABLEID tableid, JET_CBTYP cbtyp, JET_HANDLE hCallbackId)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "cbtyp", "hCallbackId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetUpdate(jitter):
    """
    [esent.dll] JET_ERR JetUpdate(JET_SESID sesid, JET_TABLEID tableid, void* pvBookmark, unsigned long cbBookmark, unsigned long* pcbActual)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pvBookmark", "cbBookmark", "pcbActual"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetUpdate2(jitter):
    """
    [esent.dll] JET_ERR JetUpdate2(JET_SESID sesid, JET_TABLEID tableid, void* pvBookmark, unsigned long cbBookmark, unsigned long* pcbActual, [JetUpdateFlags] grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pvBookmark", "cbBookmark", "pcbActual", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetBeginTransaction3(jitter):
    """
    [esent.dll] JET_ERR JetBeginTransaction3(JET_SESID sesid, __int64 trxid, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "trxid", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCommitTransaction2(jitter):
    """
    [esent.dll] JET_ERR JetCommitTransaction2(JET_SESID sesid, JET_GRBIT grbit, DWORD cmsecDurableCommit, JET_COMMIT_ID* pCommitID)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "grbit", "cmsecDurableCommit", "pCommitID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateIndex3(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCreateIndex3(JET_SESID sesid, JET_TABLEID tableid, JET_INDEXCREATE2* pindexcreate, unsigned long cIndexCreate)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pindexcreate", "cIndexCreate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateIndex3A(jitter):
    esent_JetCreateIndex3(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCreateIndex3W(jitter):
    esent_JetCreateIndex3(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetCreateIndex4(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCreateIndex4(JET_SESID sesid, JET_TABLEID tableid, JET_INDEXCREATE2* pindexcreate, unsigned long cIndexCreate)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "pindexcreate", "cIndexCreate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateIndex4A(jitter):
    esent_JetCreateIndex4(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCreateIndex4W(jitter):
    esent_JetCreateIndex4(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetCreateTableColumnIndex3(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCreateTableColumnIndex3(JET_SESID sesid, JET_DBID dbid, JET_TABLECREATE3* ptablecreate)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "ptablecreate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateTableColumnIndex3A(jitter):
    esent_JetCreateTableColumnIndex3(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCreateTableColumnIndex3W(jitter):
    esent_JetCreateTableColumnIndex3(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetCreateTableColumnIndex4(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetCreateTableColumnIndex4(JET_SESID sesid, JET_DBID dbid, JET_TABLECREATE3* ptablecreate)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "ptablecreate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetCreateTableColumnIndex4A(jitter):
    esent_JetCreateTableColumnIndex4(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetCreateTableColumnIndex4W(jitter):
    esent_JetCreateTableColumnIndex4(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetGetErrorInfoW(jitter):
    """
    [esent.dll] JET_ERR JetGetErrorInfoW(void* pvContext, void* pvResult, unsigned long cbMax, unsigned long InfoLevel, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["pvContext", "pvResult", "cbMax", "InfoLevel", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetRecordSize2(jitter):
    """
    [esent.dll] JET_ERR JetGetRecordSize2(JET_SESID sesid, JET_TABLEID tableid, JET_RECSIZE2* precsize, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "precsize", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetGetSessionParameter(jitter):
    """
    [esent.dll] JET_ERR JetGetSessionParameter(JET_SESID sesid, unsigned long sesparamid, void* pvParam, unsigned long cbParamMax, unsigned long pcbParamActual)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "sesparamid", "pvParam", "cbParamMax", "pcbParamActual"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetPrereadIndexRanges(jitter):
    """
    [esent.dll] JET_ERR JetPrereadIndexRanges(JET_SESID sesid, JET_TABLEID tableid, const JET_INDEX_RANGE* const rgIndexRanges, const unsigned long cIndexRanges, unsigned long* const pcRangesPreread, const JET_COLUMNID* const rgcolumnidPreread, const unsigned long ccolumnidPreread, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "rgIndexRanges", "cIndexRanges", "pcRangesPreread", "rgcolumnidPreread", "ccolumnidPreread", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetPrereadKeys(jitter):
    """
    [esent.dll] JET_ERR JetPrereadKeys(JET_SESID sesid, JET_TABLEID tableid, const void** rgpvKeys, const unsigned long* rgcbKeys, long ckeys, long* pckeysPreread, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "rgpvKeys", "rgcbKeys", "ckeys", "pckeysPreread", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetResizeDatabase(jitter):
    """
    [esent.dll] JET_ERR JetResizeDatabase(JET_SESID sesid, JET_DBID dbid, unsigned long cpg, unsigned long* pcpgActual, const JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "dbid", "cpg", "pcpgActual", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetCursorFilter(jitter):
    """
    [esent.dll] JET_ERR JetSetCursorFilter(JET_SESID sesid, JET_TABLEID tableid, JET_INDEX_COLUMN* rgFilters, DWORD cFilters, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "tableid", "rgFilters", "cFilters", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetSetSessionParameter(jitter):
    """
    [esent.dll] JET_ERR JetSetSessionParameter(JET_SESID sesid, unsigned long sesparamid, void* pvParam, unsigned long cbParam)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "sesparamid", "pvParam", "cbParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetStopServiceInstance2(jitter):
    """
    [esent.dll] JET_ERR JetStopServiceInstance2(JET_INSTANCE instance)
    """
    ret_ad, args = jitter.func_args_stdcall(["instance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetDefragment3(jitter, get_str, set_str):
    """
    [esent.dll] JET_ERR JetDefragment3(JET_SESID sesid, JET_PCSTR szDatabaseName, JET_PCSTR szTableName, unsigned long* pcPasses, unsigned long* pcSeconds, JET_CALLBACK callback, void* pvContext, JET_GRBIT grbit)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "szDatabaseName", "szTableName", "pcPasses", "pcSeconds", "callback", "pvContext", "grbit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def esent_JetDefragment3A(jitter):
    esent_JetDefragment3(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def esent_JetDefragment3W(jitter):
    esent_JetDefragment3(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def esent_JetOpenTemporaryTable2(jitter):
    """
    [esent.dll] JET_ERR JetOpenTemporaryTable2(JET_SESID sesid, JET_OPENTEMPORARYTABLE2* popentemporarytable)
    """
    ret_ad, args = jitter.func_args_stdcall(["sesid", "popentemporarytable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
