# Created by: Mikolaj Golub <trociny@FreeBSD.org>
# $FreeBSD: head/databases/py-python-swiftclient/Makefile 455210 2017-11-30 15:50:30Z mat $

PORTNAME=	python-swiftclient
PORTVERSION=	3.4.0
PORTREVISION=   1
CATEGORIES=	databases python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Python client library for OpenStack Object Storage (Swift)

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}futures>0:devel/py-futures \
		${PYTHON_PKGNAMEPREFIX}requests>=1.1:www/py-requests \
		${PYTHON_PKGNAMEPREFIX}six>=1.5.2:devel/py-six

USES=		python
USE_PYTHON=	distutils autoplist

post-install:
	${INSTALL_MAN} ${WRKSRC}/doc/manpages/swift.1 \
	    ${STAGEDIR}${MANPREFIX}/man/man1

.include <bsd.port.mk>
