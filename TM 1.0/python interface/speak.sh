#!/bin/bash
PID=$$
aplay $1
kill -9 $PID