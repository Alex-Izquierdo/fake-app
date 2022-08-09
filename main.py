from aiohttp import web
from os import environ
from aiohttp.web_request import Request
from aiohttp.web_response import Response

routes = web.RouteTableDef()

BROKEN = False


@routes.get("/health")
async def health(request: Request) -> Response:
    global BROKEN
    if BROKEN:
        return web.json_response({"status": "ERROR: application unavailable"}, status=503)

    return web.json_response({"status": "RUNNING"})


@routes.get("/down")
async def down(request: Request) -> Response:
    global BROKEN
    BROKEN = True
    return web.json_response({"result": "application outage started"})


@routes.get("/up")
async def up(request: Request) -> Response:
    global BROKEN
    BROKEN = False
    return web.json_response({"result": "application outage finished"})


if __name__ == "__main__":
    app = web.Application()
    app.add_routes(routes)
    port = int(environ.get("HTTP_PORT", 5080))
    web.run_app(app=app, port=port)
