# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD: head/devel/py-taskflow/Makefile 433312 2017-02-04 14:31:09Z novel $

PORTNAME=	taskflow
PORTVERSION=	2.14.0
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Taskflow structured state management library

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}enum34>0:devel/py-enum34 \
		${PYTHON_PKGNAMEPREFIX}futurist>=0.11.0:devel/py-futurist \
		${PYTHON_PKGNAMEPREFIX}fasteners>=0.7:devel/py-fasteners \
		${PYTHON_PKGNAMEPREFIX}networkx>=1.10:math/py-networkx \
		${PYTHON_PKGNAMEPREFIX}contextlib2>=0.4.0:devel/py-contextlib2 \
		${PYTHON_PKGNAMEPREFIX}stevedore>=1.20.0:devel/py-stevedore \
		${PYTHON_PKGNAMEPREFIX}futures>=3.0:devel/py-futures \
		${PYTHON_PKGNAMEPREFIX}jsonschema>=2.0.0:devel/py-jsonschema \
		${PYTHON_PKGNAMEPREFIX}automaton>=0.5.0:devel/py-automaton \
		${PYTHON_PKGNAMEPREFIX}oslo.utils>=3.20.0:devel/py-oslo.utils \
		${PYTHON_PKGNAMEPREFIX}oslo.serialization>=1.10.0:devel/py-oslo.serialization \
		${PYTHON_PKGNAMEPREFIX}tenacity>=3.2.1:devel/py-tenacity \
		${PYTHON_PKGNAMEPREFIX}cachetools>=1.1.0:devel/py-cachetools \
		${PYTHON_PKGNAMEPREFIX}debtcollector>=1.2.0:devel/py-debtcollector

NO_ARCH=	yes

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
