#!/bin/sh

TARGET=ports
BASE=`pwd`
SVN=${BASE}/svn
DIFF=${BASE}/diff

rm -rf ${SVN} ${DIFF}
mkdir -p ${SVN}
mkdir -p ${DIFF}

cd ${TARGET}
mkdir -p ${DIFF}

# download original ports & make diff files
for A in */*; do
	echo -n "${A}: "
	CATEGORY=`dirname $A`
	PORT=`basename $A`
	mkdir -p ${SVN}/${CATEGORY}
	svn checkout -q http://svn.freebsd.org/ports/head/${A} ${SVN}/${CATEGORY}/${PORT}
	if [ $? -gt 0 ]; then
		echo " new port tar"
		(cd ${CATEGORY}; tar cf ${DIFF}/${CATEGORY}_${PORT}.tar ${PORT})
	else
		echo " svn diff"
		cp -Rp ${A}/* ${SVN}/${CATEGORY}/${PORT}
		svn diff ${SVN}/${CATEGORY}/${PORT} > ${DIFF}/${CATEGORY}_${PORT}.diff
	fi
done
rm -rf ${SVN}

# remove zero size diff files
find ${DIFF} -size 0 -delete

cd ${BASE}

