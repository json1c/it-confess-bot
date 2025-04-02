from aiogram import Router


def get_inline_router():
    from . import query
    
    router = Router()
    router.include_router(query.router)
    
    return router
