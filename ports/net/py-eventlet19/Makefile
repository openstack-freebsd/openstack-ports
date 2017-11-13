# Created by: Sung Gon Yi <skonmeme@gmail.com>
# $FreeBSD: head/net/py-eventlet/Makefile 446111 2017-07-17 20:10:47Z mmokhi $

PORTNAME=	eventlet
PORTVERSION=	0.19.0
CATEGORIES=	net python
MASTER_SITES=	CHEESESHOP
PKGNAMESUFFIX=  19
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Concurrent networking library for Python

LICENSE=	MIT

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}greenlet>=0.3.2:devel/py-greenlet \
		${PYTHON_PKGNAMEPREFIX}enum-compat>=0.0.2:devel/py-enum-compat \
		${PYTHON_PKGNAMEPREFIX}enum34>=1.1.6:devel/py-enum34
TEST_DEPENDS=	${PYTHON_PKGNAMEPREFIX}nose>0:devel/py-nose

USES=		python
USE_PYTHON=	distutils autoplist

regression-test: build
	@cd ${WRKSRC} && ${PYTHON_CMD} ${PYSETUP} test

.include <bsd.port.mk>
