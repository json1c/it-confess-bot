from aiogram import Router


def get_handlers_router():
    from . import inline
    
    router = Router()
    
    inline_router = inline.get_inline_router()
    
    router.include_router(inline_router)
    
    return router
