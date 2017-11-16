# $FreeBSD: head/databases/py-alembic/Makefile 438496 2017-04-14 07:50:29Z lwhsu $

PORTNAME=	alembic
PORTVERSION=	0.9.6
CATEGORIES=	databases python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Database migration tool for SQLAlchemy

LICENSE=	MIT

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sqlalchemy11>=0.7.6:databases/py-sqlalchemy11 \
		${PYTHON_PKGNAMEPREFIX}mako>0:textproc/py-mako \
		${PYTHON_PKGNAMEPREFIX}python-editor>=0.3:devel/py-python-editor \
		${PYTHON_PKGNAMEPREFIX}dateutil>0:devel/py-dateutil

USES=		python
USE_PYTHON=	distutils autoplist

.include <bsd.port.mk>
