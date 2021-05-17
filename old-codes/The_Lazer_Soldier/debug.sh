#!/bin/bash

clear

read -p "LazerInt: " li
read -p "DinamitInt: " di

python3 main.py dbg_mode $li $di
