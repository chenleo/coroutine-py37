#!/usr/bin/env python3
# encoding: utf-8
# coroutines.py.py in coroutine-py37
# Created by maverick on 2019-03-28, 09:58
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: coroutines.py.py
@time: 2019-03-28 09:58
"""

import asyncio

async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")

if __name__ == '__main__':
    asyncio.run(main())
