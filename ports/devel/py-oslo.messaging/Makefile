# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD: head/devel/py-oslo.messaging/Makefile 432747 2017-01-29 14:17:43Z novel $

PORTNAME=	oslo.messaging
PORTVERSION=	5.30.1
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Oslo Messaging API

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}futurist>=0.11.0:devel/py-futurist \
		${PYTHON_PKGNAMEPREFIX}oslo.config>=4.0.0:devel/py-oslo.config \
		${PYTHON_PKGNAMEPREFIX}oslo.log>=3.22.0:devel/py-oslo.log \
		${PYTHON_PKGNAMEPREFIX}oslo.utils>=3.20.0:devel/py-oslo.utils \
		${PYTHON_PKGNAMEPREFIX}oslo.serialization>=1.10.0:devel/py-oslo.serialization \
		${PYTHON_PKGNAMEPREFIX}oslo.service>=1.10.0:devel/py-oslo.service \
		${PYTHON_PKGNAMEPREFIX}oslo.i18n>=2.1.0:devel/py-oslo.i18n \
		${PYTHON_PKGNAMEPREFIX}stevedore>=1.20.0:devel/py-stevedore \
		${PYTHON_PKGNAMEPREFIX}debtcollector>=1.2.0:devel/py-debtcollector \
		${PYTHON_PKGNAMEPREFIX}monotonic>=0.6:devel/py-monotonic \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}cachetools>=1.1.0:devel/py-cachetools \
		${PYTHON_PKGNAMEPREFIX}webob>=1.7.1:www/py-webob \
		${PYTHON_PKGNAMEPREFIX}yaml>=3.10.0:devel/py-yaml \
		${PYTHON_PKGNAMEPREFIX}amqp>=2.1.0:net/py-amqp \
		${PYTHON_PKGNAMEPREFIX}kombu>=4.0.0:net/py-kombu \
		${PYTHON_PKGNAMEPREFIX}pika>=0.10.0:devel/py-pika \
		${PYTHON_PKGNAMEPREFIX}pika-pool>=0.1.3:devel/py-pika-pool \
		${PYTHON_PKGNAMEPREFIX}futures>=3.0:devel/py-futures \
		${PYTHON_PKGNAMEPREFIX}tenacity>=3.2.1:devel/py-tenacity \
		${PYTHON_PKGNAMEPREFIX}oslo.middleware>=3.0.0:devel/py-oslo.middleware

NO_ARCH=	yes

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
