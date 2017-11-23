# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD: head/devel/py-castellan/Makefile 439170 2017-04-22 12:45:43Z miwi $

PORTNAME=	castellan
PORTVERSION=	0.12.1
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmai.com
COMMENT=	Generic Key Manager interface for OpenStack

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}Babel>=2.3.4:devel/py-babel \
		${PYTHON_PKGNAMEPREFIX}cryptography>=1.6:security/py-cryptography \
		${PYTHON_PKGNAMEPREFIX}python-barbicanclient>=4.0.0:net/py-python-barbicanclient \
		${PYTHON_PKGNAMEPREFIX}oslo.config>=4.0.0:devel/py-oslo.config \
		${PYTHON_PKGNAMEPREFIX}oslo.context>=2.14.0:devel/py-oslo.context \
		${PYTHON_PKGNAMEPREFIX}oslo.i18n>=2.1.0:devel/py-oslo.i18n \
		${PYTHON_PKGNAMEPREFIX}oslo.log>=3.22.0:devel/py-oslo.log \
		${PYTHON_PKGNAMEPREFIX}oslo.utils>=3.20.0:devel/py-oslo.utils \
		${PYTHON_PKGNAMEPREFIX}keystoneauth1>=3.1.0:devel/py-keystoneauth1

NO_ARCH=	yes

USES=		python shebangfix
USE_PYTHON=	autoplist distutils
SHEBANG_FILES=	castellan/tests/contrib/*.sh

.include <bsd.port.mk>
