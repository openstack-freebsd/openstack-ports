# Created by: Sung Gon Yi <skonmeme@gmail.com>
# $FreeBSD$

PORTNAME=	liberasurecode
PORTVERSION=	1.5.0
CATEGORIES=	devel
MASTER_SITES=	SOURCEWARE/${PORTNAME}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Erasure Code API library written in C with pluggable Erasure Code backends.

LICENSE=	BSD2CLAUSE
LICENSE_FILE=	${WRKSRC}/COPYING

USES=		autoreconf libtool
USE_LDCONFIG=	yes
GNU_CONFIGURE=	yes
USE_GCC=	any

USE_GITHUB=	yes
GH_ACCOUNT=	openstack

#---------- not yet
#https://github.com/openstack/liberasurecode/archive/1.5.0.tar.gz
#
#INSTALL_TARGET=	install-strip
#INFO=		libffi
#PLIST_SUB=	PORTVERSION=${PORTVERSION}
#TEST_TARGET=	check
#
#post-patch:
#	@${REINPLACE_CMD} -e 's| -Wno-psabi||g' \
#		${WRKSRC}/testsuite/lib/libffi.exp
#
#post-install:
#	@${LN} -sf ../lib/libffi-${PORTVERSION}/include/ffi.h \
#	    ${STAGEDIR}${PREFIX}/include/
#	@${LN} -sf ../lib/libffi-${PORTVERSION}/include/ffitarget.h \
#	    ${STAGEDIR}${PREFIX}/include/

.include <bsd.port.mk>
