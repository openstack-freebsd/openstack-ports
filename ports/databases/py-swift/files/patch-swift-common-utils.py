--- swift/common/utils.py.orig	2017-08-21 22:47:42.000000000 +0900
+++ swift/common/utils.py	2018-01-04 15:47:39.659772000 +0900
@@ -831,12 +831,12 @@
     """
     global _posix_fadvise
     if _posix_fadvise is None:
-        _posix_fadvise = load_libc_function('posix_fadvise64')
+        _posix_fadvise = load_libc_function('posix_fadvise')
     # 4 means "POSIX_FADV_DONTNEED"
     ret = _posix_fadvise(fd, ctypes.c_uint64(offset),
                          ctypes.c_uint64(length), 4)
     if ret != 0:
-        logging.warning("posix_fadvise64(%(fd)s, %(offset)s, %(length)s, 4) "
+        logging.warning("posix_fadvise(%(fd)s, %(offset)s, %(length)s, 4) "
                         "-> %(ret)s", {'fd': fd, 'offset': offset,
                                        'length': length, 'ret': ret})
 
