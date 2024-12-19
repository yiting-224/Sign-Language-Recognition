solidity=0
extent=0
Area=0
aspectRatio = 0
if solidity >= 0.95:
    if Area > 28:
        shape = "# 萬"
    elif Area > 15:
        shape = "# 0"
    elif Area > 13:
        shape = "# B"
    elif Area > 10:
        shape = "# E"
elif solidity >= 0.9:
    if Area > 40:
        shape = "# 40"
    elif Area > 38:
        if extent > 0.73:
            shape = "# 90"
        else:
            shape = "# 20"
    elif Area > 37:
        shape = "# 30"
    elif Area > 35:
        shape = "# 50"
    elif Area > 33:
        shape = "# 10"
    elif Area > 32:
        shape = "# 千"
    elif Area > 11:
        shape = "# F"
    elif Area > 10:
        if extent > 0.6:
            shape = "# A"
        else:
            shape = "# D"
    elif Area > 8:
        if extent > 0.6:
            shape = "# M"
        else:
            shape = "# O"
    else:
        shape = "# S"  
elif solidity >= 0.85:
    if Area > 30:
        shape = "# 60"
    elif Area > 10:
        shape = "# 兄"
    elif Area > 8:
        shape = "# N"
    elif Area > 7:
        if aspectRatio > 0.5:
            shape = "# H"
        else:
            shape = "# U"
    else:
        shape = "# J"
elif solidity >= 0.8:
    if Area >= 30:
        shape = "# 百"
    elif Area >= 27:
        shape = "# 9"
    elif Area >= 26:
        shape = "# 8"
    elif Area >= 20:
        shape = "# 1"
    elif Area >= 10:
        shape = "# C"
    elif Area >= 7:
        shape = "# R"
    else:
        if aspectRatio > 0.5:
            shape = "# I"
        else:
            shape = "# X" 
elif solidity >= 0.75:
    if Area >= 25:
        shape = "# 6"
    elif Area >= 8:
        shape = "# W"
    elif Area >= 7.7:
        if aspectRatio > 1.4:
            shape = "# T"
        else:
            shape = "# P"
    elif Area >= 7.4:
        shape = "# G"
    elif Area >= 7:
        shape = "# Z"
    else:
        shape = "# K"
elif solidity >= 0.7:
    if Area >= 27:
        shape = "# 4"
    elif Area >= 25:
        shape = "# 7"
    elif Area >= 20:
        shape = "# 2"
    elif Area >= 8:
        shape = "# Y"
    else:
        shape = "# V"    
elif solidity >= 0.6:
    if Area >= 30:
        shape = "# 5"
    elif Area >= 25:
        shape = "# 3"
    elif Area >= 20:
        shape = "# Love"
    elif Area >= 6:
        shape = "# L"
    else:
        shape = "# Q"
elif solidity >= 0.5:
    shape = "# 70"
else:
    shape = "# 80"