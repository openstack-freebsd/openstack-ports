# $FreeBSD: head/devel/py-keystoneauth1/Makefile 432516 2017-01-26 15:37:28Z novel $

PORTNAME=	keystoneauth1
PORTVERSION=	3.1.0
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Authentication Library for OpenStack Identity

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}iso8601>=0.1.11:devel/py-iso8601 \
		${PYTHON_PKGNAMEPREFIX}positional>=1.1.1:devel/py-positional \
		${PYTHON_PKGNAMEPREFIX}requests>=2.14.0:www/py-requests \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}stevedore>=1.20.0:devel/py-stevedore

NO_ARCH=	yes

USES=		python:2.7+
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
