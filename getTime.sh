#!/bin/bash

ping -c1 $1 -W 1 | grep 'tempo=' | cut -d'=' -f4 | cut -d' ' -f1