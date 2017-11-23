# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD: head/net/py-python-barbicanclient/Makefile 428780 2016-12-17 16:38:26Z novel $

PORTNAME=	python-barbicanclient
PORTVERSION=	4.5.2
CATEGORIES=	net python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Client Library for OpenStack Barbican Key Management API

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}requests>=2.14.2:www/py-requests \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}cliff>=2.8.0:devel/py-cliff \
		${PYTHON_PKGNAMEPREFIX}keystoneauth1>=3.0.1:devel/py-keystoneauth1 \
		${PYTHON_PKGNAMEPREFIX}oslo.i18n>=2.1.0:devel/py-oslo.i18n \
		${PYTHON_PKGNAMEPREFIX}oslo.serialization>=1.10.0:devel/py-oslo.serialization \
		${PYTHON_PKGNAMEPREFIX}oslo.utils>=3.20.0:devel/py-oslo.utils

NO_ARCH=	yes

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
