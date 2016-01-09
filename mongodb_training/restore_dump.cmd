
@echo off
set MONGODB_PATH=E:\apps\mongodb\bin
set MONGODB_HOST=ds035995.mongolab.com:35995
set MONGODB_USER=testdb
set DATABASE=testdb_mongolab

set DUMP_DIR=%1

if not defined MONGODB_PASSWORD (
    echo MONGODB_PASSWORD is not defined
    exit /b
)
set PATH=%PATH%;%MONGODB_PATH%

mongorestore --host %MONGODB_HOST% --username %MONGODB_USER% --password %MONGODB_PASSWORD% -d %DATABASE% %DUMP_DIR%