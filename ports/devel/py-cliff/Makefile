# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD: head/devel/py-cliff/Makefile 432754 2017-01-29 15:02:50Z novel $

PORTNAME=	cliff
PORTVERSION=	2.8.0
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Command Line Interface Formulation Framework

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}cmd2>=0.6.7:devel/py-cmd2 \
		${PYTHON_PKGNAMEPREFIX}prettytable>=0.7.1:devel/py-prettytable \
		${PYTHON_PKGNAMEPREFIX}pyparsing>=2.1.0:devel/py-pyparsing \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}stevedore>=1.20.0:devel/py-stevedore \
		${PYTHON_PKGNAMEPREFIX}unicodecsv>=0.8.0:devel/py-unicodecsv \
		${PYTHON_PKGNAMEPREFIX}yaml>=3.10.0:devel/py-yaml

NO_ARCH=	yes

USES=		python:2.7+
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
