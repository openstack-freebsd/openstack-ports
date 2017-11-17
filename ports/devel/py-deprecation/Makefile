# Created by: Sung Gon Yi <skonmeme@gmail.com>
# $FreeBSD$

PORTNAME=	deprecation
PORTVERSION=	1.0.1
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	A library to handle automated deprecations

LICENSE=	APACHE20

USES=		python
USE_PYTHON=	distutils autoplist
NO_ARCH=	yes

post-patch:
	@${REINPLACE_CMD} -e 's,install_requires.*,,' ${WRKSRC}/setup.py

.include <bsd.port.mk>
