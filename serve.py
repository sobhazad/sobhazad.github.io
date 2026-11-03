#!/usr/bin/env python3
"""Tiny local preview server WITH HTTP Range support (needed for video seeking, and for Safari to play video at all).
Usage:  python3 serve.py      then open http://localhost:8000
Python's built-in `python3 -m http.server` does not support Range requests, so videos cannot be seeked there."""
import http.server, os, re, socketserver, sys
class H(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        rng = self.headers.get('Range'); path = self.translate_path(self.path)
        if not rng or not os.path.isfile(path): return super().send_head()
        m = re.match(r'bytes=(\d*)-(\d*)', rng); size = os.path.getsize(path)
        if not m: return super().send_head()
        a, b = m.groups()
        start = int(a) if a else max(size - int(b), 0); end = int(b) if (a and b) else size - 1
        end = min(end, size - 1)
        if start > end: self.send_error(416); return None
        f = open(path, 'rb'); f.seek(start)
        self.send_response(206); self.send_header('Content-Type', self.guess_type(path))
        self.send_header('Content-Range', f'bytes {start}-{end}/{size}'); self.send_header('Content-Length', str(end - start + 1))
        self.send_header('Accept-Ranges', 'bytes'); self.end_headers(); self._left = end - start + 1; return f
    def copyfile(self, src, dst):
        n = getattr(self, '_left', None)
        if n is None: return super().copyfile(src, dst)
        while n > 0:
            chunk = src.read(min(65536, n))
            if not chunk: break
            try: dst.write(chunk)
            except (BrokenPipeError, ConnectionResetError): break
            n -= len(chunk)
        self._left = None
    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes'); super().end_headers()
    def log_message(self, *a): pass
os.chdir(os.path.dirname(os.path.abspath(__file__)))
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
socketserver.ThreadingTCPServer.allow_reuse_address = True
print(f'Serving on http://localhost:{port}  (Ctrl+C to stop)')
socketserver.ThreadingTCPServer(('', port), H).serve_forever()
