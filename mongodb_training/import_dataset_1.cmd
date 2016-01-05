:: Script to import DATASET to mongodb

:: set mongodb connection details
::mongo ds035995.mongolab.com:35995/testdb_mongolab -u <dbuser> -p <dbpassword>
SET MONGODB_PATH=E:\apps\mongodb\bin
SET MONGODB_HOST=ds035995.mongolab.com
SET MONGODB_PORT=3595
SET MONGODB_USER=testdb

IF DEFINED MONGODB_PASSWORD (ECHO MONGODB_PASSWORD IS defined) ELSE (ECHO MONGODB_PASSWORD is NOT defined)

::set parameters for mongoimport command
SET DATABASE=test
SET DATASET=primer-dataset.json
SET COLLECTION=restaurants

::set mongodb path
SET PATH=%PATH%;%MONGODB_PATH%

mongoimport --db %DATABASE% --collection %COLLECTION% --drop --file %$DATASET%^
 --host %MONGODB_HOST% --port %MONGODB_PORT% --username %MONGODB_USER% --password %MONGODB_PASSWORD%