# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD: head/net/py-python-openstackclient/Makefile 438824 2017-04-19 06:17:17Z miwi $

PORTNAME=	python-openstackclient
PORTVERSION=	3.12.0
CATEGORIES=	net python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Client for the OpenStack

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}Babel>=2.3.4:devel/py-babel \
		${PYTHON_PKGNAMEPREFIX}cliff>=2.8.0:devel/py-cliff \
		${PYTHON_PKGNAMEPREFIX}keystoneauth1>=3.0.1:devel/py-keystoneauth1 \
		${PYTHON_PKGNAMEPREFIX}openstacksdk>=0.9.17:devel/py-openstacksdk \
		${PYTHON_PKGNAMEPREFIX}osc-lib>=1.7.0:devel/py-osc-lib \
		${PYTHON_PKGNAMEPREFIX}oslo.i18n>=2.1.0:devel/py-oslo.i18n \
		${PYTHON_PKGNAMEPREFIX}oslo.utils>=3.20.0:devel/py-oslo.utils \
		${PYTHON_PKGNAMEPREFIX}python-glanceclient>=2.7.0:net/py-python-glanceclient \
		${PYTHON_PKGNAMEPREFIX}python-keystoneclient>=3.8.0:net/py-python-keystoneclient \
		${PYTHON_PKGNAMEPREFIX}python-novaclient>=9.0.0:net/py-python-novaclient \
		${PYTHON_PKGNAMEPREFIX}python-cinderclient>=3.0.0:net/py-python-cinderclient \
		${PYTHON_PKGNAMEPREFIX}python-neutronclient>0:net/py-python-neutronclient

USES=		python shebangfix
USE_PYTHON=	distutils autoplist noegginfo
NO_ARCH=	yes
SHEBANG_FILES=	openstackclient/tests/functional/post_test_hook.sh \
		openstackclient/tests/functional/post_test_hook_tips.sh

.include <bsd.port.mk>
