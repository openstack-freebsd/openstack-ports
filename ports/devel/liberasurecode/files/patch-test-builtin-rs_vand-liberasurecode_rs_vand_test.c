--- test/builtin/rs_vand/liberasurecode_rs_vand_test.c.orig	2017-12-27 19:05:41.344751000 +0900
+++ test/builtin/rs_vand/liberasurecode_rs_vand_test.c	2017-12-27 19:05:29.620143000 +0900
@@ -29,6 +29,7 @@
 #include <string.h>
 #include <unistd.h>
 #include <fcntl.h>
+#include <sys/stat.h>
 #include <time.h>
 #include <liberasurecode_rs_vand.h>
 
