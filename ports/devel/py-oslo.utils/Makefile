# $FreeBSD: head/devel/py-oslo.utils/Makefile 429375 2016-12-24 17:14:19Z novel $

PORTNAME=	oslo.utils
PORTVERSION=	3.28.0
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Oslo Utility library

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS:=	${BUILD_DEPENDS}
RUN_DEPENDS+=	${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}funcsigs>=0.4:devel/py-funcsigs \
		${PYTHON_PKGNAMEPREFIX}iso8601>=0.1.11:devel/py-iso8601 \
		${PYTHON_PKGNAMEPREFIX}oslo.i18n>=2.1.0:devel/py-oslo.i18n \
		${PYTHON_PKGNAMEPREFIX}monotonic>=0.6:devel/py-monotonic \
		${PYTHON_PKGNAMEPREFIX}pytz>=2013.6:devel/py-pytz \
		${PYTHON_PKGNAMEPREFIX}netaddr>=0.7.13:net/py-netaddr \
		${PYTHON_PKGNAMEPREFIX}debtcollector>=1.2.0:devel/py-debtcollector \
		${PYTHON_PKGNAMEPREFIX}pyparsing>=2.1.0:devel/py-pyparsing

NO_ARCH=	yes

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
