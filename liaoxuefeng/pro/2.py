import asyncio
import logging

@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from asyncio.create_pool()