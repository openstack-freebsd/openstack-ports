# $FreeBSD: head/devel/py-oslo.i18n/Makefile 429376 2016-12-24 17:15:12Z novel $

PORTNAME=	oslo.i18n
PORTVERSION=	3.17.0
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Oslo i18n library

LICENSE=	APACHE20

BUILD_DEPENDS=	${PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}Babel>=2.3.4:devel/py-babel \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six

NO_ARCH=	yes

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
