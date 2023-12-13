#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：fast-api-template
@File    ：__init__.py.py
@Author  ：Mr.LiuQHui
@Date    ：2023/11/13 18:25 
"""
from fastapi import FastAPI
from .usetime_middleware import UseTimeMiddleware
from .token_middleware import TokenMiddleware
from .test_middleware import TestMiddleware

# 定义注册顺序
middlewareList = [
    UseTimeMiddleware,  # 添加耗时请求中间件
    TokenMiddleware,  # 添加token验证中间件
    TestMiddleware  # 测试中间件
]


def registerMiddlewareHandle(server: FastAPI):
    """ 注册中间件 """
    # 倒序中间件
    middlewareList.reverse()
    # 遍历注册
    for middleware in middlewareList:
        server.add_middleware(middleware)
