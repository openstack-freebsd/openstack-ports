# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD: head/devel/py-oslo.db/Makefile 432715 2017-01-29 10:58:30Z novel $

PORTNAME=	oslo.db
PORTVERSION=	4.25.0
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Oslo Database library

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}alembic>=0.8.10:databases/py-alembic \
		${PYTHON_PKGNAMEPREFIX}debtcollector>=1.2.0:devel/py-debtcollector \
		${PYTHON_PKGNAMEPREFIX}oslo.i18n>=2.1.0:devel/py-oslo.i18n \
		${PYTHON_PKGNAMEPREFIX}oslo.config>=4.0.0:devel/py-oslo.config \
		${PYTHON_PKGNAMEPREFIX}oslo.utils>=3.20.0:devel/py-oslo.utils \
		${PYTHON_PKGNAMEPREFIX}sqlalchemy11>=1.0.10:databases/py-sqlalchemy11 \
		${PYTHON_PKGNAMEPREFIX}sqlalchemy-migrate>=0.11.0:databases/py-sqlalchemy-migrate \
		${PYTHON_PKGNAMEPREFIX}stevedore>=1.20.1:devel/py-stevedore \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six

NO_ARCH=	yes

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
