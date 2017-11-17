# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD: head/net/py-python-glanceclient/Makefile 428767 2016-12-17 15:31:09Z novel $

PORTNAME=	python-glanceclient
PORTVERSION=	2.8.0
PORTREVISION=	1
CATEGORIES=	net python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Client for the OpenStack Glance API

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}Babel>=2.3.4:devel/py-babel \
		${PYTHON_PKGNAMEPREFIX}prettytable>=0.7.1:devel/py-prettytable \
		${PYTHON_PKGNAMEPREFIX}python-keystoneclient>=3.0.1:net/py-python-keystoneclient \
		${PYTHON_PKGNAMEPREFIX}requests>=2.14.2:www/py-requests \
		${PYTHON_PKGNAMEPREFIX}warlock>=1.0.1:devel/py-warlock \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}oslo.utils>=3.20.0:devel/py-oslo.utils \
		${PYTHON_PKGNAMEPREFIX}oslo.i18n>=2.1.0:devel/py-oslo.i18n \
		${PYTHON_PKGNAMEPREFIX}wrapt>=1.7.0:devel/py-wrapt \
		${PYTHON_PKGNAMEPREFIX}openssl>=0.14:security/py-openssl		

USES=		python shebangfix
SHEBANG_FILES=	glanceclient/tests/functional/hooks/post_test_hook.sh
USE_PYTHON=	distutils autoplist noegginfo
NO_ARCH=	yes

post-patch:
	@${REINPLACE_CMD} -e 's,install_requires.*,,' ${WRKSRC}/setup.py

.include <bsd.port.mk>
