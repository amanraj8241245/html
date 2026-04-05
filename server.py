"""
server.py — Flask Web Server for Render Deployment
Runs the Telegram bot in the background with HTTP health check endpoint.
"""

import os
import asyncio
import threading
from flask import Flask, jsonify

from main import app as bot_app

# ── Flask App ──────────────────────────────────────────────────────────────────
flask_app = Flask(__name__)

# ── Status tracker ─────────────────────────────────────────────────────────────
bot_running = {"status": False, "error": None}


def run_bot():
    """Run the Telegram bot in a background thread."""
    try:
        # Create a new event loop for this thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        bot_running["status"] = True
        print("✅ Telegram Bot Started")
        
        # Run the bot indefinitely
        loop.run_until_complete(bot_app.run())
        
    except Exception as e:
        bot_running["status"] = False
        bot_running["error"] = str(e)
        print(f"❌ Bot Error: {e}")


# ── Routes ─────────────────────────────────────────────────────────────────────
@flask_app.route("/", methods=["GET"])
def health_check():
    """Health check endpoint for Render."""
    return jsonify({
        "status": "healthy",
        "bot_running": bot_running["status"],
        "service": "HTML↔TXT Converter Bot"
    }), 200


@flask_app.route("/status", methods=["GET"])
def status():
    """Bot status endpoint."""
    if bot_running["error"]:
        return jsonify({"status": "error", "error": bot_running["error"]}), 500
    
    return jsonify({
        "status": "running" if bot_running["status"] else "stopped",
        "bot_running": bot_running["status"]
    }), 200


# ── Start Bot on App Startup ──────────────────────────────────────────────────
def start_bot_thread():
    """Start bot in a daemon thread."""
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    print("🤖 Bot thread started")


# ── Main ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Start bot in background
    start_bot_thread()
    
    # Get port from environment or default to 5000
    port = int(os.environ.get("PORT", 5000))
    
    # Run Flask server
    print(f"🚀 Flask Server running on port {port}")
    flask_app.run(host="0.0.0.0", port=port, debug=False, threaded=True)
