# Created by: elvstone@gmail.com
# $FreeBSD: head/databases/py-sqlalchemy-migrate/Makefile 436207 2017-03-15 10:59:09Z lwhsu $

PORTNAME=	sqlalchemy-migrate
PORTVERSION=	0.11.0
CATEGORIES=	databases python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Database schema migrations for SQLAlchemy

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/COPYING

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=1.3:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}Tempita>=0.4:textproc/py-Tempita \
		${PYTHON_PKGNAMEPREFIX}decorator>0:devel/py-decorator \
		${PYTHON_PKGNAMEPREFIX}sqlparse>0:databases/py-sqlparse \
		${PYTHON_PKGNAMEPREFIX}six>=1.7.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}pbr>=1.3:devel/py-pbr

# Options for SQLAlchemy 0.11
OPTIONS_DEFINE=		SQLALCHEMY11
OPTIONS_DEFAULT=	SQLALCHEMY11
SQLALCHEMY11_DESC=	Use sqlalchemy 1.1.x instead of sqlalchemy 1.0.x
SQLALCHEMY11_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sqlalchemy11>=0.7.8:databases/py-sqlalchemy11
SQLALCHEMY11_RUN_DEPENDS_OFF=	${PYTHON_PKGNAMEPREFIX}sqlalchemy10>=0.7.8:databases/py-sqlalchemy10

USES=		python
USE_PYTHON=	distutils concurrent autoplist

NO_ARCH=	yes

.include <bsd.port.mk>
