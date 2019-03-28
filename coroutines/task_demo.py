#!/usr/bin/env python3
# encoding: utf-8
# task_demo.py in coroutine-py37
# Created by maverick on 2019-03-28, 14:24
# 

"""
@version: ??
@author: Leo Chen
@contact: maverickcc@gmail.com
@file: task_demo.py
@time: 2019-03-28 14:24
"""

import asyncio
import time

async def say_after(delay: int, what: str) -> None:
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"started at {time.strftime('%X')}")

if __name__ == '__main__':
    asyncio.run(main())