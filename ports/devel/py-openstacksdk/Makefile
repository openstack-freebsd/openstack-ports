# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD: head/devel/py-openstacksdk/Makefile 427198 2016-11-27 08:48:42Z novel $

PORTNAME=	openstacksdk
PORTVERSION=	0.9.18
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Unified SDK for OpenStack

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}jsonpatch>=1.1:devel/py-jsonpatch \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}stevedore>=1.20.0:devel/py-stevedore \
		${PYTHON_PKGNAMEPREFIX}os-client-config>=1.28.0:devel/py-os-client-config \
		${PYTHON_PKGNAMEPREFIX}keystoneauth1>=3.1.0:devel/py-keystoneauth1 \
		${PYTHON_PKGNAMEPREFIX}deprecation>=1.0:devel/py-deprecation

USES=		python
USE_PYTHON=	distutils autoplist noegginfo
NO_ARCH=	yes

post-patch:
	@${REINPLACE_CMD} -e 's,install_requires.*,,' ${WRKSRC}/setup.py

.include <bsd.port.mk>
