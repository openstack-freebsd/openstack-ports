# Created by: Nicola Vitale <nivit@FreeBSD.org>
# $FreeBSD: head/devel/py-stevedore/Makefile 425128 2016-11-02 09:28:48Z lwhsu $

PORTNAME=	stevedore
PORTVERSION=	1.25.0
CATEGORIES=	devel
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Manage dynamic plugins for Python applications

LICENSE=	APACHE20

BUILD_DEPENDS=	${PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS:=	${BUILD_DEPENDS}
RUN_DEPENDS+=	${PKGNAMEPREFIX}six>=1.9.0:devel/py-six

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
