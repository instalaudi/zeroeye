import time
from urllib.request import urlopen, Request
from socket import create_connection, timeout as SocketTimeoutError

def check_http_service(url, retries=3, backoff=2):
    for attempt in range(retries + 1):
        try:
            req = Request(url)
            response = urlopen(req)
            if response.getcode() == 200:
                return 'OK'
        except Exception as e:
            if attempt < retries:
                time.sleep(backoff * (2 ** attempt))
            else:
                return 'CRITICAL', str(e)
    return 'CRITICAL', 'All attempts failed'

def check_tcp_port(host, port, retries=3, backoff=2):
    for attempt in range(retries + 1):
        try:
            with create_connection((host, port), timeout=backoff * (2 ** attempt)) as sock:
                return 'OK'
        except SocketTimeoutError:
            if attempt < retries:
                time.sleep(backoff * (2 ** attempt))
            else:
                return 'CRITICAL', 'Connection timed out'
        except Exception as e:
            if attempt < retries:
                time.sleep(backoff * (2 ** attempt))
            else:
                return 'CRITICAL', str(e)
    return 'CRITICAL', 'All attempts failed'