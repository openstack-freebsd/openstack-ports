# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD: head/net/py-python-neutronclient/Makefile 428767 2016-12-17 15:31:09Z novel $

PORTNAME=	python-neutronclient
PORTVERSION=	6.5.0
CATEGORIES=	net python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Client for the OpenStack Neutron API

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}cliff>=2.8.0:devel/py-cliff \
		${PYTHON_PKGNAMEPREFIX}debtcollector>=1.2.0:devel/py-debtcollector \
		${PYTHON_PKGNAMEPREFIX}iso8601>=0.1.11:devel/py-iso8601 \
		${PYTHON_PKGNAMEPREFIX}netaddr>=0.7.13:net/py-netaddr \
		${PYTHON_PKGNAMEPREFIX}osc-lib>=1.7.0:devel/py-osc-lib \
		${PYTHON_PKGNAMEPREFIX}oslo.i18n>=2.1.0:devel/py-oslo.i18n \
		${PYTHON_PKGNAMEPREFIX}oslo.serialization>=1.10.0:devel/py-oslo.serialization \
		${PYTHON_PKGNAMEPREFIX}oslo.utils>=3.20.0:devel/py-oslo.utils \
		${PYTHON_PKGNAMEPREFIX}os-client-config>=1.28.0:devel/py-os-client-config \
		${PYTHON_PKGNAMEPREFIX}keystoneauth1>=3.0.1:devel/py-keystoneauth1 \
		${PYTHON_PKGNAMEPREFIX}python-keystoneclient>=3.8.0:net/py-python-keystoneclient \
		${PYTHON_PKGNAMEPREFIX}requests>=2.14.2:www/py-requests \
		${PYTHON_PKGNAMEPREFIX}simplejson>=2.2.0:devel/py-simplejson \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}Babel>=2.3.4:devel/py-babel

USES=		python shebangfix
SHEBANG_FILES=	neutronclient/tests/functional/hooks/post_test_hook.sh
USE_PYTHON=	distutils autoplist noegginfo
NO_ARCH=	yes

post-patch:
	@${REINPLACE_CMD} -e 's,install_requires.*,,' ${WRKSRC}/setup.py

.include <bsd.port.mk>
