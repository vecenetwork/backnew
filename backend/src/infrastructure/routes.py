from typing import TYPE_CHECKING

from infrastructure.api.auth import (
    login,
    register,
    barrier,
    reset_password,
    waitlist,
)
from infrastructure.api import (
    countries,
    demo,
    users,
    user_image,
    subscriptions,
    hashtags,
    questions,
    similarity,
    search,
)


if TYPE_CHECKING:
    from fastapi import FastAPI

API_PREFIX = "/api"

routers = [
    register.router,
    login.router,
    demo.router,
    barrier.router,
    users.router,
    user_image.router,
    reset_password.router,
    subscriptions.router,
    hashtags.router,
    questions.router,
    countries.router,
    similarity.router,
    waitlist.router,
    search.router,
]


def register_routes(app: "FastAPI"):
    for router in routers:
        if API_PREFIX:
            app.include_router(router, prefix=API_PREFIX)
        else:
            app.include_router(router)
