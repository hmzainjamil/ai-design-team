from streamlit.web.server.server_util import is_url_from_allowed_origins
from tornado.websocket import WebSocketHandler

class SecureWebSocketMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, request):
        if request.headers.get('Upgrade', '').lower() == 'websocket':
            # Force secure WebSocket
            request.headers['X-Forwarded-Proto'] = 'https'
            if not request.url.startswith('wss://'):
                request.url = request.url.replace('ws://', 'wss://')
        
        return await self.app(request) 