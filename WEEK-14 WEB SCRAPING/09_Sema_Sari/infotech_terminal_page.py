"""resentation of both small and\n                  large-scale data.(Matplotlib, Plotly, Seaborn)'}
2023-03-16 10:26:03 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '', 'topic': 'Machine Learning', 'description': 'Get the key element of Supervised and Unsupervised learning.'}
2023-03-16 10:26:03 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '', 'topic': 'NLP and Recomendation Systems', 'description': 'Learn Recommender systems (RS) that have evolved into a\n                    fundamental tool for helping users make informed decisions\n                    and choices.'}
2023-03-16 10:26:03 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '', 'topic': 'Data Science Project', 'description': "Let's bring it all together: combine your forces to build a\n                    data science project!"}
2023-03-16 10:26:03 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '', 'topic': 'GRADUATION', 'description': 'Collect your certification to became data scientist!'}
2023-03-16 10:26:03 [scrapy.core.scraper] ERROR: Spider error processing <GET https://infotechacademy.eu/data_science> (referer: None)
Traceback (most recent call last):
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\defer.py", line 257, in iter_errback
    yield next(it)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\python.py", line 312, in __next__
    return next(self.data)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\python.py", line 312, in __next__
    return next(self.data)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\offsite.py", line 28, in <genexpr>
    return (r for r in result or () if self._filter(r, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\referer.py", line 353, in <genexpr>
    return (self._set_referer(r, response) for r in result or ())
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\urllength.py", line 27, in <genexpr>
    return (r for r in result or () if self._filter(r, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\depth.py", line 31, in <genexpr>
    return (r for r in result or () if self._filter(r, response, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "C:\Users\admin\Desktop\scrapy_odev_info\infotech\infotech\spiders\infotechweb.py", line 18, in parse
    description = description.strip()
AttributeError: 'NoneType' object has no attribute 'strip'
2023-03-16 10:26:03 [scrapy.core.engine] INFO: Closing spider (finished)
2023-03-16 10:26:03 [scrapy.utils.signal] ERROR: Error caught on signal handler: <function Spider.close at 0x00000199CE5C3C10>
Traceback (most recent call last):
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\defer.py", line 312, in maybeDeferred_coro
    result = f(*args, **kw)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\pydispatch\robustapply.py", line 55, in robustApply
    return receiver(*arguments, **named)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spiders\__init__.py", line 92, in close
    return closed(reason)
  File "C:\Users\admin\Desktop\scrapy_odev_info\infotech\infotech\spiders\infotechweb.py", line 26, in closed
    data = list(self.parse(self.start_urls[0]))
  File "C:\Users\admin\Desktop\scrapy_odev_info\infotech\infotech\spiders\infotechweb.py", line 11, in parse
    for course in response.css('div.col-lg-4.col-sm-6'):
AttributeError: 'str' object has no attribute 'css'
2023-03-16 10:26:03 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 458,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 6016,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 1,
2023-03-16 10:26:03 [scrapy.core.engine] INFO: Spider closed (finished)
(.venv) PS C:\Users\admin\Desktop\scrapy_odev_info\infotech> scrapy crawl infotechweb
2023-03-16 10:41:45 [scrapy.utils.log] INFO: Scrapy 2.8.0 started (bot: infotech)
2023-03-16 10:41:45 [scrapy.utils.log] INFO: Versions: lxml 4.9.2.0, libxml2 2.9.12, cssselect 1.2.0, parsel 1.7.0, w3lib 2.1.1, Twisted 22.10.0, Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)], pyOpenSSL 23.0.0 (OpenSSL 3.0.8 7 Feb 2023), cryptography 39.0.2, Platform Windows-10-10.0.22621-SP0
2023-03-16 10:41:45 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'infotech',
 'FEED_EXPORT_ENCODING': 'utf-8',
 'NEWSPIDER_MODULE': 'infotech.spiders',
 'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['infotech.spiders'],
 'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'}
2023-03-16 10:41:45 [asyncio] DEBUG: Using selector: SelectSelector
2023-03-16 10:41:45 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.asyncioreactor.AsyncioSelectorReactor
2023-03-16 10:41:45 [scrapy.utils.log] DEBUG: Using asyncio event loop: asyncio.windows_events._WindowsSelectorEventLoop
2023-03-16 10:41:45 [scrapy.extensions.telnet] INFO: Telnet Password: 3911f630a0e32e6b
2023-03-16 10:41:45 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']
2023-03-16 10:41:45 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2023-03-16 10:41:45 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2023-03-16 10:41:45 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2023-03-16 10:41:45 [scrapy.core.engine] INFO: Spider opened
2023-03-16 10:41:45 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2023-03-16 10:41:45 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2023-03-16 10:41:46 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://infotechacademy.eu/robots.txt> (referer: None)
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 8 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 11 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 12 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 13 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 14 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 15 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 16 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 20 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 21 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 22 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 26 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 27 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 28 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 29 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 30 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 31 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 32 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 36 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 37 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 38 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 39 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 40 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 41 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 42 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 43 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 44 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 45 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 49 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 50 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 51 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 56 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 57 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 60 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 61 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 62 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 65 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 69 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 70 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 85 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 91 without any user agent to enforce it on.
2023-03-16 10:41:46 [protego] DEBUG: Rule at line 98 without any user agent to enforce it on.
2023-03-16 10:41:46 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://infotechacademy.eu/data_science> (referer: None)
2023-03-16 10:41:46 [scrapy.core.scraper] ERROR: Spider error processing <GET https://infotechacademy.eu/data_science> (referer: None)
Traceback (most recent call last):
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\defer.py", line 257, in iter_errback
    yield next(it)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\python.py", line 312, in __next__
    return next(self.data)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\python.py", line 312, in __next__
    return next(self.data)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\offsite.py", line 28, in <genexpr>
    return (r for r in result or () if self._filter(r, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\referer.py", line 353, in <genexpr>
    return (self._set_referer(r, response) for r in result or ())
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\urllength.py", line 27, in <genexpr>
    return (r for r in result or () if self._filter(r, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\depth.py", line 31, in <genexpr>
    return (r for r in result or () if self._filter(r, response, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "C:\Users\admin\Desktop\scrapy_odev_info\infotech\infotech\spiders\infotechweb.py", line 16, in parse
    week = re.sub('[^0-9]', '', week)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python39\lib\re.py", line 210, in sub
    return _compile(pattern, flags).sub(repl, string, count)
TypeError: expected string or bytes-like object
2023-03-16 10:41:46 [scrapy.core.engine] INFO: Closing spider (finished)
2023-03-16 10:41:46 [scrapy.utils.signal] ERROR: Error caught on signal handler: <function Spider.close at 0x0000027D0EB33C10>
Traceback (most recent call last):
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\defer.py", line 312, in maybeDeferred_coro
    result = f(*args, **kw)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\pydispatch\robustapply.py", line 55, in robustApply
    return receiver(*arguments, **named)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spiders\__init__.py", line 92, in close
    return closed(reason)
  File "C:\Users\admin\Desktop\scrapy_odev_info\infotech\infotech\spiders\infotechweb.py", line 26, in closed
    data = list(self.parse(self.start_urls[0]))
  File "C:\Users\admin\Desktop\scrapy_odev_info\infotech\infotech\spiders\infotechweb.py", line 11, in parse
    for course in response.css('div.col-lg-4.col-sm-6'):
AttributeError: 'str' object has no attribute 'css'
2023-03-16 10:41:46 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 458,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 6015,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/404': 1,
 'elapsed_time_seconds': 0.407705,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2023, 3, 16, 9, 41, 46, 341068),
 'httpcompression/response_bytes': 26077,
 'httpcompression/response_count': 2,
 'log_count/DEBUG': 46,
 'log_count/ERROR': 2,
 'log_count/INFO': 10,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'spider_exceptions/TypeError': 1,
 'start_time': datetime.datetime(2023, 3, 16, 9, 41, 45, 933363)}
2023-03-16 10:41:46 [scrapy.core.engine] INFO: Spider closed (finished)
(.venv) PS C:\Users\admin\Desktop\scrapy_odev_info\infotech> scrapy crawl infotechweb
2023-03-16 10:43:43 [scrapy.utils.log] INFO: Scrapy 2.8.0 started (bot: infotech)
2023-03-16 10:43:43 [scrapy.utils.log] INFO: Versions: lxml 4.9.2.0, libxml2 2.9.12, cssselect 1.2.0, parsel 1.7.0, w3lib 2.1.1, Twisted 22.10.0, Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)], pyOpenSSL 23.0.0 (OpenSSL 3.0.8 7 Feb 2023), cryptography 39.0.2, Platform Windows-10-10.0.22621-SP0
2023-03-16 10:43:43 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'infotech',
 'FEED_EXPORT_ENCODING': 'utf-8',
 'NEWSPIDER_MODULE': 'infotech.spiders',
 'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['infotech.spiders'],
 'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'}
2023-03-16 10:43:43 [asyncio] DEBUG: Using selector: SelectSelector
2023-03-16 10:43:43 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.asyncioreactor.AsyncioSelectorReactor
2023-03-16 10:43:43 [scrapy.utils.log] DEBUG: Using asyncio event loop: asyncio.windows_events._WindowsSelectorEventLoop
2023-03-16 10:43:44 [scrapy.extensions.telnet] INFO: Telnet Password: 21ffdefc8301c233
2023-03-16 10:43:44 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']
2023-03-16 10:43:44 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2023-03-16 10:43:44 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2023-03-16 10:43:44 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2023-03-16 10:43:44 [scrapy.core.engine] INFO: Spider opened
2023-03-16 10:43:44 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2023-03-16 10:43:44 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2023-03-16 10:43:44 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://infotechacademy.eu/robots.txt> (referer: None)
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 8 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 11 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 12 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 13 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 14 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 15 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 16 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 20 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 21 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 22 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 26 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 27 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 28 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 29 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 30 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 31 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 32 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 36 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 37 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 38 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 39 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 40 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 41 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 42 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 43 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 44 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 45 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 49 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 50 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 51 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 56 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 57 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 60 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 61 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 62 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 65 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 69 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 70 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 85 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 91 without any user agent to enforce it on.
2023-03-16 10:43:44 [protego] DEBUG: Rule at line 98 without any user agent to enforce it on.
2023-03-16 10:43:44 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://infotechacademy.eu/data_science> (referer: None)
2023-03-16 10:43:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '15', 'topic': 'Python Programming', 'description': 'Make your entrance into the wonderful world of programming\n                  with Python!'}    
2023-03-16 10:43:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '67', 'topic': 'Object-Oriented Programming', 'description': 'You will learn Object-oriented programming (OOP) that is a\n                  method of structuring a program by bundling related properties\n                  and behaviors into individual objects.'}
2023-03-16 10:43:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '89', 'topic': 'GUI Programming', 'description': 'Combine your Python programming knowledge with your GUI design\n                  by using PYQT-5'}
2023-03-16 10:43:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '1011', 'topic': 'Database', 'description': 'You will learn to store data securely and use it whenever you\n                  want. (SQL/ NonSQL)'}  
2023-03-16 10:43:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '1213', 'topic': "Web Scraping, HTTP Request and API's", 'description': 'You will learn to scrape information from the internet and use\n            
      this information (Beautiful Soup, Selenium, Scrapy)'}
2023-03-16 10:43:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '14', 'topic': 'Statistics for Data Science', 'description': 'You will earn the basic statistical information to use when\n                  processing data.'}
2023-03-16 10:43:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '1517', 'topic': 'Exploring Data', 'description': 'You will learn about Exploratory Data Analysis or (EDA) that\n                  is understanding the data sets by summarizing their main\n                  characteristics often plotting them visually.(NumP, Pandas)'}
2023-03-16 10:43:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '1820', 'topic': 'Data Visualization', 'description': 'You will learn about Data Visualization that plays an\n                  essential role in the representation of both small and\n                  large-scale data.(Matplotlib, Plotly, Seaborn)'}
2023-03-16 10:43:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '2125', 'topic': 'Machine Learning', 'description': 'Get the key element of Supervised and Unsupervised learning.'}
2023-03-16 10:43:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '26', 'topic': 'NLP and Recomendation Systems', 'description': 'Learn Recommender systems (RS) that have evolved into a\n                    fundamental tool for helping users make informed decisions\n                    and choices.'}
2023-03-16 10:43:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '2730', 'topic': 'Data Science Project', 'description': "Let's bring it all together: combine your forces to build a\n                    data science project!"}
2023-03-16 10:43:45 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': '31', 'topic': 'GRADUATION', 'description': 'Collect your certification to became data scientist!'}
2023-03-16 10:43:45 [scrapy.core.scraper] ERROR: Spider error processing <GET https://infotechacademy.eu/data_science> (referer: None)
Traceback (most recent call last):
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\defer.py", line 257, in iter_errback
    yield next(it)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\python.py", line 312, in __next__
    return next(self.data)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\python.py", line 312, in __next__
    return next(self.data)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\offsite.py", line 28, in <genexpr>
    return (r for r in result or () if self._filter(r, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\referer.py", line 353, in <genexpr>
    return (self._set_referer(r, response) for r in result or ())
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\urllength.py", line 27, in <genexpr>
    return (r for r in result or () if self._filter(r, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\depth.py", line 31, in <genexpr>
    return (r for r in result or () if self._filter(r, response, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "C:\Users\admin\Desktop\scrapy_odev_info\infotech\infotech\spiders\infotechweb.py", line 16, in parse
    week = re.sub('[^0-9]', '', week)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python39\lib\re.py", line 210, in sub
    return _compile(pattern, flags).sub(repl, string, count)
TypeError: expected string or bytes-like object
2023-03-16 10:43:45 [scrapy.core.engine] INFO: Closing spider (finished)
2023-03-16 10:43:45 [scrapy.utils.signal] ERROR: Error caught on signal handler: <function Spider.close at 0x000002665C5B2C10>
Traceback (most recent call last):
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\defer.py", line 312, in maybeDeferred_coro
    result = f(*args, **kw)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\pydispatch\robustapply.py", line 55, in robustApply
    return receiver(*arguments, **named)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spiders\__init__.py", line 92, in close
    return closed(reason)
  File "C:\Users\admin\Desktop\scrapy_odev_info\infotech\infotech\spiders\infotechweb.py", line 26, in closed
    data = list(self.parse(self.start_urls[0]))
  File "C:\Users\admin\Desktop\scrapy_odev_info\infotech\infotech\spiders\infotechweb.py", line 11, in parse
    for course in response.css('div.col-lg-4.col-sm-6'):
AttributeError: 'str' object has no attribute 'css'
2023-03-16 10:43:45 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 458,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 6015,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/404': 1,
 'elapsed_time_seconds': 0.447711,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2023, 3, 16, 9, 43, 45, 99457),
 'httpcompression/response_bytes': 26077,
 'httpcompression/response_count': 2,
 'item_scraped_count': 12,
 'log_count/DEBUG': 58,
 'log_count/ERROR': 2,
 'log_count/INFO': 10,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'spider_exceptions/TypeError': 1,
 'start_time': datetime.datetime(2023, 3, 16, 9, 43, 44, 651746)}
2023-03-16 10:43:45 [scrapy.core.engine] INFO: Spider closed (finished)
(.venv) PS C:\Users\admin\Desktop\scrapy_odev_info\infotech> scrapy crawl infotechweb
2023-03-16 10:46:03 [scrapy.utils.log] INFO: Scrapy 2.8.0 started (bot: infotech)
2023-03-16 10:46:03 [scrapy.utils.log] INFO: Versions: lxml 4.9.2.0, libxml2 2.9.12, cssselect 1.2.0, parsel 1.7.0, w3lib 2.1.1, Twisted 22.10.0, Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)], pyOpenSSL 23.0.0 (OpenSSL 3.0.8 7 Feb 2023), cryptography 39.0.2, Platform Windows-10-10.0.22621-SP0
2023-03-16 10:46:03 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'infotech',
 'FEED_EXPORT_ENCODING': 'utf-8',
 'NEWSPIDER_MODULE': 'infotech.spiders',
 'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['infotech.spiders'],
 'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'}
2023-03-16 10:46:03 [asyncio] DEBUG: Using selector: SelectSelector
2023-03-16 10:46:03 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.asyncioreactor.AsyncioSelectorReactor
2023-03-16 10:46:03 [scrapy.utils.log] DEBUG: Using asyncio event loop: asyncio.windows_events._WindowsSelectorEventLoop
2023-03-16 10:46:03 [scrapy.extensions.telnet] INFO: Telnet Password: afeb5e907af41be9
2023-03-16 10:46:03 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']
2023-03-16 10:46:03 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2023-03-16 10:46:03 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2023-03-16 10:46:03 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2023-03-16 10:46:03 [scrapy.core.engine] INFO: Spider opened
2023-03-16 10:46:04 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2023-03-16 10:46:04 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2023-03-16 10:46:04 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://infotechacademy.eu/robots.txt> (referer: None)
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 8 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 11 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 12 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 13 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 14 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 15 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 16 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 20 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 21 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 22 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 26 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 27 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 28 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 29 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 30 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 31 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 32 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 36 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 37 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 38 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 39 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 40 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 41 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 42 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 43 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 44 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 45 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 49 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 50 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 51 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 56 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 57 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 60 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 61 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 62 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 65 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 69 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 70 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 85 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 91 without any user agent to enforce it on.
2023-03-16 10:46:04 [protego] DEBUG: Rule at line 98 without any user agent to enforce it on.
2023-03-16 10:46:04 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://infotechacademy.eu/data_science> (referer: None)
2023-03-16 10:46:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 1 - 5', 'topic': 'Python Programming', 'description': 'Make your entrance into the wonderful world of programming\n                  with Python!'}
2023-03-16 10:46:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 6 - 7', 'topic': 'Object-Oriented Programming', 'description': 'You will learn Object-oriented programming (OOP) that is a\n                  method of structuring a program by bundling related properties\n                  and behaviors into individual objects.'}
2023-03-16 10:46:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 8 - 9', 'topic': 'GUI Programming', 'description': 'Combine your Python programming knowledge with your GUI design\n                  by using PYQT-5'}
2023-03-16 10:46:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 10 - 11', 'topic': 'Database', 'description': 'You will learn to store data securely and use it whenever you\n                  want. (SQL/ NonSQL)'}
2023-03-16 10:46:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 12- 13', 'topic': "Web Scraping, HTTP Request and API's", 'description': 'You will learn to scrape information from the internet and use\n                  this information (Beautiful Soup, Selenium, Scrapy)'}
2023-03-16 10:46:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 14', 'topic': 'Statistics for Data Science', 'description': 'You will earn the basic statistical information to use when\n                  processing data.'}
2023-03-16 10:46:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 15 - 17', 'topic': 'Exploring Data', 'description': 'You will learn about Exploratory Data Analysis or (EDA) that\n                  is understanding the data sets by summarizing their main\n                  characteristics often plotting them visually.(NumP, Pandas)'}
2023-03-16 10:46:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 18- 20', 'topic': 'Data Visualization', 'description': 'You will learn about Data Visualization that plays an\n                  essential role in the representation of both small and\n                  large-scale data.(Matplotlib, Plotly, Seaborn)'}
2023-03-16 10:46:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 21 - 25', 'topic': 'Machine Learning', 'description': 'Get the key element of Supervised and Unsupervised learning.'}
2023-03-16 10:46:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 26', 'topic': 'NLP and Recomendation Systems', 'description': 'Learn Recommender systems (RS) that have evolved into a\n                    fundamental tool for helping users make informed decisions\n                    and choices.'}
2023-03-16 10:46:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 27 - 30', 'topic': 'Data Science Project', 'description': "Let's bring it all together: combine your forces to build a\n                    data science project!"}
2023-03-16 10:46:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 31', 'topic': 'GRADUATION', 'description': 'Collect your certification to became data scientist!'}
2023-03-16 10:46:04 [scrapy.core.scraper] ERROR: Spider error processing <GET https://infotechacademy.eu/data_science> (referer: None)
Traceback (most recent call last):
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\defer.py", line 257, in iter_errback
    yield next(it)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\python.py", line 312, in __next__
    return next(self.data)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\python.py", line 312, in __next__
    return next(self.data)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\offsite.py", line 28, in <genexpr>
    return (r for r in result or () if self._filter(r, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\referer.py", line 353, in <genexpr>
    return (self._set_referer(r, response) for r in result or ())
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\urllength.py", line 27, in <genexpr>
    return (r for r in result or () if self._filter(r, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\depth.py", line 31, in <genexpr>
    return (r for r in result or () if self._filter(r, response, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "C:\Users\admin\Desktop\scrapy_odev_info\infotech\infotech\spiders\infotechweb.py", line 17, in parse
    week=week.strip()
AttributeError: 'NoneType' object has no attribute 'strip'
2023-03-16 10:46:04 [scrapy.core.engine] INFO: Closing spider (finished)
2023-03-16 10:46:04 [scrapy.utils.signal] ERROR: Error caught on signal handler: <function Spider.close at 0x000001D5525D3C10>
Traceback (most recent call last):
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\defer.py", line 312, in maybeDeferred_coro
    result = f(*args, **kw)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\pydispatch\robustapply.py", line 55, in robustApply
    return receiver(*arguments, **named)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spiders\__init__.py", line 92, in close
    return closed(reason)
  File "C:\Users\admin\Desktop\scrapy_odev_info\infotech\infotech\spiders\infotechweb.py", line 27, in closed
    data = list(self.parse(self.start_urls[0]))
  File "C:\Users\admin\Desktop\scrapy_odev_info\infotech\infotech\spiders\infotechweb.py", line 11, in parse
    for course in response.css('div.col-lg-4.col-sm-6'):
AttributeError: 'str' object has no attribute 'css'
2023-03-16 10:46:04 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 458,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 6016,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/404': 1,
 'elapsed_time_seconds': 0.435838,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2023, 3, 16, 9, 46, 4, 461592),
 'httpcompression/response_bytes': 26077,
 'httpcompression/response_count': 2,
 'item_scraped_count': 12,
 'log_count/DEBUG': 58,
 'log_count/ERROR': 2,
 'log_count/INFO': 10,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
2023-03-16 10:46:04 [scrapy.core.engine] INFO: Spider closed (finished)
(.venv) PS C:\Users\admin\Desktop\scrapy_odev_info\infotech> scrapy crawl infotechweb -o 1.json
2023-03-16 10:48:07 [scrapy.utils.log] INFO: Scrapy 2.8.0 started (bot: infotech)
2023-03-16 10:48:07 [scrapy.utils.log] INFO: Versions: lxml 4.9.2.0, libxml2 2.9.12, cssselect 1.2.0, parsel 1.7.0, w3lib 2.1.1, Twisted 22.10.0, Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)], pyOpenSSL 23.0.0 (OpenSSL 3.0.8 7 Feb 2023), cryptography 39.0.2, Platform Windows-10-10.0.22621-SP0
2023-03-16 10:48:07 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'infotech',
 'FEED_EXPORT_ENCODING': 'utf-8',
 'NEWSPIDER_MODULE': 'infotech.spiders',
 'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['infotech.spiders'],
 'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'}
2023-03-16 10:48:07 [asyncio] DEBUG: Using selector: SelectSelector
2023-03-16 10:48:07 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.asyncioreactor.AsyncioSelectorReactor
2023-03-16 10:48:07 [scrapy.utils.log] DEBUG: Using asyncio event loop: asyncio.windows_events._WindowsSelectorEventLoop
2023-03-16 10:48:07 [scrapy.extensions.telnet] INFO: Telnet Password: 58056d502274c5f1
2023-03-16 10:48:07 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2023-03-16 10:48:08 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2023-03-16 10:48:08 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2023-03-16 10:48:08 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2023-03-16 10:48:08 [scrapy.core.engine] INFO: Spider opened
2023-03-16 10:48:08 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2023-03-16 10:48:08 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2023-03-16 10:48:08 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://infotechacademy.eu/robots.txt> (referer: None)
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 8 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 11 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 12 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 13 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 14 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 15 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 16 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 20 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 21 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 22 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 26 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 27 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 28 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 29 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 30 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 31 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 32 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 36 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 37 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 38 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 39 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 40 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 41 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 42 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 43 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 44 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 45 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 49 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 50 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 51 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 56 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 57 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 60 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 61 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 62 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 65 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 69 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 70 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 85 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 91 without any user agent to enforce it on.
2023-03-16 10:48:08 [protego] DEBUG: Rule at line 98 without any user agent to enforce it on.
2023-03-16 10:48:08 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://infotechacademy.eu/data_science> (referer: None)
2023-03-16 10:48:08 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 1 - 5', 'topic': 'Python Programming', 'description': 'Make your entrance into the wonderful world of programming\n                  with Python!'}
2023-03-16 10:48:08 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 6 - 7', 'topic': 'Object-Oriented Programming', 'description': 'You will learn Object-oriented programming (OOP) that is a\n                  method of structuring a program by bundling related properties\n                  and behaviors into individual objects.'}
2023-03-16 10:48:08 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 8 - 9', 'topic': 'GUI Programming', 'description': 'Combine your Python programming knowledge with your GUI design\n                  by using PYQT-5'}
2023-03-16 10:48:08 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 10 - 11', 'topic': 'Database', 'description': 'You will learn to store data securely and use it whenever you\n                  want. (SQL/ NonSQL)'}
2023-03-16 10:48:08 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 12- 13', 'topic': "Web Scraping, HTTP Request and API's", 'description': 'You will learn to scrape information from the internet and use\n                  this information (Beautiful Soup, Selenium, Scrapy)'}
2023-03-16 10:48:08 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 14', 'topic': 'Statistics for Data Science', 'description': 'You will earn the basic statistical information to use when\n                  processing data.'}
2023-03-16 10:48:08 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 15 - 17', 'topic': 'Exploring Data', 'description': 'You will learn about Exploratory Data Analysis or (EDA) that\n                  is understanding the data sets by summarizing their main\n                  characteristics often plotting them visually.(NumP, Pandas)'}
2023-03-16 10:48:08 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 18- 20', 'topic': 'Data Visualization', 'description': 'You will learn about Data Visualization that plays an\n                  essential role in the representation of both small and\n                  large-scale data.(Matplotlib, Plotly, Seaborn)'}
2023-03-16 10:48:08 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 21 - 25', 'topic': 'Machine Learning', 'description': 'Get the key element of Supervised and Unsupervised learning.'}
2023-03-16 10:48:08 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 26', 'topic': 'NLP and Recomendation Systems', 'description': 'Learn Recommender systems (RS) that have evolved into a\n                    fundamental tool for helping users make informed decisions\n                    and choices.'}
2023-03-16 10:48:08 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 27 - 30', 'topic': 'Data Science Project', 'description': "Let's bring it all together: combine your forces to build a\n                    data science project!"}
2023-03-16 10:48:08 [scrapy.core.scraper] DEBUG: Scraped from <200 https://infotechacademy.eu/data_science>
{'week': 'Week 31', 'topic': 'GRADUATION', 'description': 'Collect your certification to became data scientist!'}
2023-03-16 10:48:08 [scrapy.core.scraper] ERROR: Spider error processing <GET https://infotechacademy.eu/data_science> (referer: None)
Traceback (most recent call last):
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\defer.py", line 257, in iter_errback
    yield next(it)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\python.py", line 312, in __next__
    return next(self.data)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\utils\python.py", line 312, in __next__
    return next(self.data)
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\offsite.py", line 28, in <genexpr>
    return (r for r in result or () if self._filter(r, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\referer.py", line 353, in <genexpr>
    return (self._set_referer(r, response) for r in result or ())
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\urllength.py", line 27, in <genexpr>
    return (r for r in result or () if self._filter(r, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\spidermiddlewares\depth.py", line 31, in <genexpr>
    return (r for r in result or () if self._filter(r, response, spider))
  File "c:\users\admin\desktop\scrapy_odev_info\.venv\lib\site-packages\scrapy\core\spidermw.py", line 104, in process_sync
    for r in iterable:
  File "C:\Users\admin\Desktop\scrapy_odev_info\infotech\infotech\spiders\infotechweb.py", line 17, in parse
    week=week.strip()
AttributeError: 'NoneType' object has no attribute 'strip'
2023-03-16 10:48:08 [scrapy.core.engine] INFO: Closing spider (finished)
2023-03-16 10:48:08 [scrapy.extensions.feedexport] INFO: Stored json feed (12 items) in: 1.json
2023-03-16 10:48:08 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 458,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 6015,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/404': 1,
 'elapsed_time_seconds': 0.433253,
 'feedexport/success_count/FileFeedStorage': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2023, 3, 16, 9, 48, 8, 959012),
 'httpcompression/response_bytes': 26077,
 'httpcompression/response_count': 2,
 'item_scraped_count': 12,
 'log_count/DEBUG': 58,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'spider_exceptions/AttributeError': 1,
 'start_time': datetime.datetime(2023, 3, 16, 9, 48, 8, 525759)}
2023-03-16 10:48:08 [scrapy.core.engine] INFO: Spider closed (finished)
(.venv) PS C:\Users\admin\Desktop\scrapy_odev_info\infotech> scrapy crawl infotechweb
2023-03-16 11:01:43 [scrapy.utils.log] INFO: Scrapy 2.8.0 started (bot: infotech)
2023-03-16 11:01:43 [scrapy.utils.log] INFO: Versions: lxml 4.9.2.0, libxml2 2.9.12, cssselect 1.2.0, parsel 1.7.0, w3lib 2.1.1, Twisted 22.10.0, Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)], pyOpenSSL 23.0.0 (OpenSSL 3.0.8 7 Feb 2023), cryptography 39.0.2, Platform Windows-10-10.0.22621-SP0
2023-03-16 11:01:43 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'infotech',
 'FEED_EXPORT_ENCODING': 'utf-8',
 'NEWSPIDER_MODULE': 'infotech.spiders',
 'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['infotech.spiders'],
 'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'}
2023-03-16 11:01:43 [asyncio] DEBUG: Using selector: SelectSelector
2023-03-16 11:01:43 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.asyncioreactor.AsyncioSelectorReactor
2023-03-16 11:01:43 [scrapy.utils.log] DEBUG: Using asyncio event loop: asyncio.windows_events._WindowsSelectorEventLoop
2023-03-16 11:01:43 [scrapy.extensions.telnet] INFO: Telnet Password: 1ee031f6bbeb1433
2023-03-16 11:01:43 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']
2023-03-16 11:01:44 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2023-03-16 11:01:44 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2023-03-16 11:01:44 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2023-03-16 11:01:44 [scrapy.core.engine] INFO: Spider opened
2023-03-16 11:01:44 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2023-03-16 11:01:44 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2023-03-16 11:01:44 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://infotechacademy.eu/robots.txt> (referer: None)
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 8 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 11 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 12 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 13 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 14 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 15 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 16 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 20 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 21 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 22 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 26 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 27 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 28 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 29 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 30 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 31 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 32 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 36 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 37 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 38 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 39 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 40 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 41 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 42 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 43 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 44 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 45 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 49 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 50 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 51 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 56 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 57 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 60 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 61 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 62 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 65 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 69 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 70 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 85 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 91 without any user agent to enforce it on.
2023-03-16 11:01:44 [protego] DEBUG: Rule at line 98 without any user agent to enforce it on.
2023-03-16 11:01:44 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://infotechacademy.eu/data_science> (referer: None)
2023-03-16 11:01:44 [scrapy.core.engine] INFO: Closing spider (finished)
2023-03-16 11:01:44 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 458,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 6016,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/404': 1,
 'elapsed_time_seconds': 0.399753,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2023, 3, 16, 10, 1, 44, 737473),
 'httpcompression/response_bytes': 26077,
 'httpcompression/response_count': 2,
 'log_count/DEBUG': 46,
 'log_count/INFO': 10,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2023, 3, 16, 10, 1, 44, 337720)}
2023-03-16 11:01:44 [scrapy.core.engine] INFO: Spider closed (finished)
(.venv) PS C:\Users\admin\Desktop\scrapy_odev_info\infotech> scrapy crawl infotechweb -o 2.json
2023-03-16 11:02:16 [scrapy.utils.log] INFO: Scrapy 2.8.0 started (bot: infotech)
2023-03-16 11:02:16 [scrapy.utils.log] INFO: Versions: lxml 4.9.2.0, libxml2 2.9.12, cssselect 1.2.0, parsel 1.7.0, w3lib 2.1.1, Twisted 22.10.0, Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)], pyOpenSSL 23.0.0 (OpenSSL 3.0.8 7 Feb 2023), cryptography 39.0.2, Platform Windows-10-10.0.22621-SP0
2023-03-16 11:02:16 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'infotech',
 'FEED_EXPORT_ENCODING': 'utf-8',
 'NEWSPIDER_MODULE': 'infotech.spiders',
 'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['infotech.spiders'],
 'TWISTED_REACTOR': 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'}
2023-03-16 11:02:16 [asyncio] DEBUG: Using selector: SelectSelector
2023-03-16 11:02:16 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.asyncioreactor.AsyncioSelectorReactor
2023-03-16 11:02:16 [scrapy.utils.log] DEBUG: Using asyncio event loop: asyncio.windows_events._WindowsSelectorEventLoop
2023-03-16 11:02:16 [scrapy.extensions.telnet] INFO: Telnet Password: c4fe3692775d373d
2023-03-16 11:02:16 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2023-03-16 11:02:17 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2023-03-16 11:02:17 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2023-03-16 11:02:17 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2023-03-16 11:02:17 [scrapy.core.engine] INFO: Spider opened
2023-03-16 11:02:17 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2023-03-16 11:02:17 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2023-03-16 11:02:17 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://infotechacademy.eu/robots.txt> (referer: None)
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 8 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 11 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 12 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 13 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 14 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 15 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 16 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 20 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 21 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 22 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 26 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 27 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 28 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 29 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 30 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 31 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 32 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 36 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 37 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 38 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 39 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 40 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 41 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 42 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 43 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 44 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 45 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 49 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 50 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 51 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 56 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 57 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 60 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 61 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 62 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 65 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 69 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 70 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 85 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 91 without any user agent to enforce it on.
2023-03-16 11:02:17 [protego] DEBUG: Rule at line 98 without any user agent to enforce it on.
2023-03-16 11:02:17 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://infotechacademy.eu/data_science> (referer: None)
2023-03-16 11:02:17 [scrapy.core.engine] INFO: Closing spider (finished)
2023-03-16 11:02:17 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 458,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 6015,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/404': 1,
 'elapsed_time_seconds': 0.39482,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2023, 3, 16, 10, 2, 17, 808345),
 'httpcompression/response_bytes': 26077,
 'httpcompression/response_count': 2,
 'log_count/DEBUG': 46,
 'log_count/INFO': 10,
 'response_received_count': 2,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 1,
 'scheduler/dequeued/memory': 1,
 'scheduler/enqueued': 1,
 'scheduler/enqueued/memory': 1,
 'start_time': datetime.datetime(2023, 3, 16, 10, 2, 17, 413525)}
2023-03-16 11:02:17 [scrapy.core.engine] INFO: Spider closed (finished)
(.venv) PS C:\Users\admin\Desktop\scrapy_odev_info\infotech> """