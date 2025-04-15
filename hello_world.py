#!/usr/bin/env python3
# -------------------------------------------------
# PyCharm 2024.3.5 (Professional Edition)
# Build #PY-243.26053.29, built on March 17, 2025
# Licensed to Deon Botha
# VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
# macOS 15.3.1
#
# Student : DB25020017469
#
# Task : M03T09 - Git/Github version control
# -------------------------------------------------
import time
import sys

def typewriter(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

typewriter("Git is awesome")
