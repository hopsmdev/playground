@echo off
set MONGODB_PATH=E:\apps\mongodb\bin
set PATH=%PATH%;%MONGODB_PATH%
mongod.exe --dbpath E:\mongodb\data --storageEngine=mmapv1