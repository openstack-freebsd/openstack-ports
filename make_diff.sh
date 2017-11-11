#!/bin/sh

TARGET=ports
BASE=`pwd`
SVN=${BASE}/svn
DIFF=${BASE}/diff

mkdir -p ${SVN}
mkdir -p ${DIFF}

cd ${TARGET}
mkdir -p ${DIFF}

# download original ports & make diff files
for A in */*; do
	echo $A
	CATEGORY=`dirname $A`
	PORT=`basename $A`
	mkdir -p ${SVN}/${CATEGORY}
	svn checkout http://svn.freebsd.org/ports/head/${A} ${SVN}/${CATEGORY}/${PORT}
	cp -Rp ${A}/* ${SVN}/${CATEGORY}/${PORT}
	svn diff ${SVN}/${CATEGORY}/${PORT} > ${DIFF}/${PORT}.diff
done
rm -rf ${SVN}

# remove zero size diff files
find ${DIFF} -size 0 -delete

cd ${BASE}

