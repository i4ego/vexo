import app
import threading

import webview

PORT = 8947

if __name__ == "__main__":
    appthread = threading.Thread(target=app.run, args=(PORT,), daemon=True)
    appthread.start()

    webview.create_window("test", f"http://localhost:{PORT}/")

    webview.start()