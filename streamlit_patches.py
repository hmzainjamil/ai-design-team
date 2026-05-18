from streamlit.web.server.server import Server
from streamlit.runtime.scriptrunner import ScriptRunner
from streamlit.web.server.browser_websocket_handler import BrowserWebSocketHandler
import tornado.websocket

def patch_streamlit_websocket():
    """Patch Streamlit's WebSocket handling for secure connections"""
    
    original_handle = BrowserWebSocketHandler._handle_websocket
    original_get_value = BrowserWebSocketHandler.get_value
    
    async def secure_handle_websocket(self, *args, **kwargs):
        """Force secure WebSocket handling"""
        if hasattr(self.request, 'headers'):
            # Force secure headers
            self.request.headers.update({
                'X-Forwarded-Proto': 'https',
                'X-Forwarded-Port': '443',
                'Upgrade': 'websocket',
                'Connection': 'Upgrade',
                'Sec-WebSocket-Version': '13'
            })
            
            # Update origin if present
            if 'Origin' in self.request.headers:
                origin = self.request.headers['Origin']
                if origin.startswith('http://'):
                    self.request.headers['Origin'] = origin.replace('http://', 'https://')

            # Update WebSocket URL
            if hasattr(self.request, 'uri'):
                self.request.uri = self.request.uri.replace('ws://', 'wss://')

        return await original_handle(self, *args, **kwargs)
    
    def secure_get_value(self):
        """Ensure WebSocket values are secure"""
        value = original_get_value(self)
        if isinstance(value, str):
            value = value.replace('ws://', 'wss://')
        return value
    
    # Apply patches
    BrowserWebSocketHandler._handle_websocket = secure_handle_websocket
    BrowserWebSocketHandler.get_value = secure_get_value 