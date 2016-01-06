:: Script to import DATASET to mongodb

:: Just before running this script you need to go to script directory
:: and run import_dataset_1.cmd

@echo off
:: set mongodb connection details
::mongo ds035995.mongolab.com:35995/testdb_mongolab -u <dbuser> -p <dbpassword>
set MONGODB_PATH=E:\apps\mongodb\bin
set MONGODB_HOST=ds035995.mongolab.com:35995
set MONGODB_USER=testdb

if not defined MONGODB_PASSWORD (
    echo MONGODB_PASSWORD is not defined
    exit /b
)

::set parameters for mongoimport command
set DATABASE=testdb_mongolab
set DATASET=datasets\primer-dataset.json
set COLLECTION=restaurants

::set mongodb path
set PATH=%PATH%;%MONGODB_PATH%

mongoimport --host %MONGODB_HOST% --db %DATABASE% --collection %COLLECTION% --drop --file %DATASET% ^
--username %MONGODB_USER% --password %MONGODB_PASSWORD%