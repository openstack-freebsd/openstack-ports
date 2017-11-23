# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD: head/devel/py-glance-store/Makefile 439605 2017-04-28 12:34:53Z miwi $

PORTNAME=	glance-store
PORTVERSION=	0.22.0
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DISTNAME=	glance_store-${PORTVERSION}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	OpenStack Image Service Store Library

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}oslo.config>=4.0.0:devel/py-oslo.config \
		${PYTHON_PKGNAMEPREFIX}oslo.i18n>=2.1.0:devel/py-oslo.i18n \
		${PYTHON_PKGNAMEPREFIX}oslo.serialization>=1.10.0:devel/py-oslo.serialization \
		${PYTHON_PKGNAMEPREFIX}oslo.utils>=3.20.0:devel/py-oslo.utils \
		${PYTHON_PKGNAMEPREFIX}oslo.concurrency>=3.8.0:devel/py-oslo.concurrency \
		${PYTHON_PKGNAMEPREFIX}stevedore>=1.20.0:devel/py-stevedore \
		${PYTHON_PKGNAMEPREFIX}enum34>=0:devel/py-enum34 \
		${PYTHON_PKGNAMEPREFIX}stevedore>=1.17.1:devel/py-stevedore \
		${PYTHON_PKGNAMEPREFIX}eventlet19>=0.18.2:net/py-eventlet19 \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}jsonschema>=2.0.0:devel/py-jsonschema \
		${PYTHON_PKGNAMEPREFIX}keystoneauth1>=3.1.0:devel/py-keystoneauth1 \
		${PYTHON_PKGNAMEPREFIX}python-keystoneclient>=3.8.0:net/py-python-keystoneclient \
		${PYTHON_PKGNAMEPREFIX}requests>=2.14.2:www/py-requests \

NO_ARCH=	yes

USES=		python shebangfix
USE_PYTHON=	autoplist distutils
SHEBANG_FILES=	glance_store/tests/functional/hooks/post_test_hook.sh \
		glance_store/tests/functional/hooks/gate_hook.sh

.include <bsd.port.mk>
