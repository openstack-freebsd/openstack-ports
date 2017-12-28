--- swift/common/utils.py.orig	2017-08-21 22:47:42.000000000 +0900
+++ swift/common/utils.py	2017-12-26 18:40:01.290242000 +0900
@@ -830,14 +830,18 @@
     :param length: length
     """
     global _posix_fadvise
+    suffix64 = ''
+    if platform.system() == 'Linux':
+        suffix64 = '64'
     if _posix_fadvise is None:
-        _posix_fadvise = load_libc_function('posix_fadvise64')
+        _posix_fadvise = load_libc_function('posix_fadvise' + suffix64)
     # 4 means "POSIX_FADV_DONTNEED"
     ret = _posix_fadvise(fd, ctypes.c_uint64(offset),
                          ctypes.c_uint64(length), 4)
     if ret != 0:
-        logging.warning("posix_fadvise64(%(fd)s, %(offset)s, %(length)s, 4) "
-                        "-> %(ret)s", {'fd': fd, 'offset': offset,
+        logging.warning("posix_fadvise%(s64)(%(fd)s, %(offset)s, %(length)s, 4) "
+                        "-> %(ret)s", {'s64': suffix64, 
+                                       'fd': fd, 'offset': offset,
                                        'length': length, 'ret': ret})
 
 
