(function() {
    const originalWebSocket = window.WebSocket;
    window.WebSocket = function(url, protocols) {
        // Get the current page's full hostname (including subdomain)
        const fullHostname = window.location.hostname;
        
        // Create a new URL object to properly parse the WebSocket URL
        let wsUrl;
        try {
            wsUrl = new URL(url);
            // Always use the same hostname as the page and wss://
            wsUrl.protocol = 'wss:';
            wsUrl.host = fullHostname;
            url = wsUrl.toString();
        } catch (e) {
            console.error('Failed to parse WebSocket URL:', e);
        }
        
        console.log('WebSocket attempting connection to:', url);
        return new originalWebSocket(url, protocols);
    };
})(); 