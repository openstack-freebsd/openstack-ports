# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD: head/devel/py-oslo.service/Makefile 432740 2017-01-29 13:23:22Z novel $

PORTNAME=	oslo.service
PORTVERSION=	1.25.0
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Oslo.service library

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}webob>=1.7.1:www/py-webob \
		${PYTHON_PKGNAMEPREFIX}eventlet19>=0.19.0:net/py-eventlet19 \
		${PYTHON_PKGNAMEPREFIX}greenlet>=0.3.2:devel/py-greenlet \
		${PYTHON_PKGNAMEPREFIX}monotonic>=0.6:devel/py-monotonic \
		${PYTHON_PKGNAMEPREFIX}oslo.utils>=3.20.0:devel/py-oslo.utils \
		${PYTHON_PKGNAMEPREFIX}oslo.concurrency>=3.8.0:devel/py-oslo.concurrency \
		${PYTHON_PKGNAMEPREFIX}oslo.config>=4.0.0:devel/py-oslo.config \
		${PYTHON_PKGNAMEPREFIX}oslo.log>=3.22.0:devel/py-oslo.log \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}oslo.i18n>=2.1.0:devel/py-oslo.i18n \
		${PYTHON_PKGNAMEPREFIX}PasteDeploy>=1.5.0:www/py-pastedeploy \
		${PYTHON_PKGNAMEPREFIX}routes>=2.3.1:www/py-routes \
		${PYTHON_PKGNAMEPREFIX}Paste>0:www/py-paste

NO_ARCH=	yes

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
