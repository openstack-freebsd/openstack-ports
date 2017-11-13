# $FreeBSD: head/devel/py-oslo.serialization/Makefile 424531 2016-10-23 16:35:29Z novel $

PORTNAME=	oslo.serialization
PORTVERSION=	2.20.0
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Oslo Serialization library

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS:=	${BUILD_DEPENDS}
RUN_DEPENDS+=	${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}msgpack-python>=0.4.0:devel/py-msgpack-python \
		${PYTHON_PKGNAMEPREFIX}oslo.utils>=3.20.0:devel/py-oslo.utils \
		${PYTHON_PKGNAMEPREFIX}pytz>=2013.6:devel/py-pytz

NO_ARCH=	yes

USES=		python
USE_PYTHON=	autoplist concurrent distutils

.include <bsd.port.mk>
