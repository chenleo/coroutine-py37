#!/usr/bin/env python3
# encoding: utf-8
# await_demo.py in coroutine-py37
# Created by maverick on 2019-03-28, 14:21
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: await_demo.py
@time: 2019-03-28 14:21
"""

import asyncio
import time

async def say_after(delay: int, what: str) -> None:
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

if __name__ == '__main__':
    asyncio.run(main())