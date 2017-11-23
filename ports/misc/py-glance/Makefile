# Created by: Alexander Nusov <alexander.nusov@nfvexpress.com>
# $FreeBSD: head/misc/py-glance/Makefile 428767 2016-12-17 15:31:09Z novel $

PORTNAME=	glance
PORTVERSION=	15.0.0
CATEGORIES=	misc python
MASTER_SITES=	https://fossies.org/linux/misc/openstack/
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	OpenStack Image Service

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sqlalchemy11>=1.0.10:databases/py-sqlalchemy11 \
		${PYTHON_PKGNAMEPREFIX}eventlet19>=0.18.2:net/py-eventlet19 \
		${PYTHON_PKGNAMEPREFIX}PasteDeploy>=1.5.0:www/py-pastedeploy \
		${PYTHON_PKGNAMEPREFIX}routes>=2.3.1:www/py-routes \
		${PYTHON_PKGNAMEPREFIX}webob>=1.7.1:www/py-webob \
		${PYTHON_PKGNAMEPREFIX}sqlalchemy-migrate>=0.9.6:databases/py-sqlalchemy-migrate \
		${PYTHON_PKGNAMEPREFIX}sqlparse>=0.2.2:databases/py-sqlparse \
		${PYTHON_PKGNAMEPREFIX}httplib2>=0.7.5:www/py-httplib2 \
		${PYTHON_PKGNAMEPREFIX}oslo.config>=4.0.0:devel/py-oslo.config \
		${PYTHON_PKGNAMEPREFIX}oslo.concurrency>=3.8.0:devel/py-oslo.concurrency \
		${PYTHON_PKGNAMEPREFIX}oslo.context>=2.14.0:devel/py-oslo.context \
		${PYTHON_PKGNAMEPREFIX}oslo.utils>=3.20.0:devel/py-oslo.utils \
		${PYTHON_PKGNAMEPREFIX}stevedore>=1.20.0:devel/py-stevedore \
		${PYTHON_PKGNAMEPREFIX}futurist>=0.11.0:devel/py-futurist \
		${PYTHON_PKGNAMEPREFIX}taskflow>=2.7.0:devel/py-taskflow \
		${PYTHON_PKGNAMEPREFIX}keystoneauth1>=3.1.0:devel/py-keystoneauth1 \
		${PYTHON_PKGNAMEPREFIX}keystonemiddleware>=4.12.0:devel/py-keystonemiddleware \
		${PYTHON_PKGNAMEPREFIX}wsme>=0.8:devel/py-wsme \
		${PYTHON_PKGNAMEPREFIX}prettytable>=0.7.1:devel/py-prettytable \
		${PYTHON_PKGNAMEPREFIX}Paste>0:www/py-paste \
		${PYTHON_PKGNAMEPREFIX}jsonschema>=2.0.0:devel/py-jsonschema \
		${PYTHON_PKGNAMEPREFIX}python-keystoneclient>=3.8.0:net/py-python-keystoneclient \
		${PYTHON_PKGNAMEPREFIX}openssl>=0.14:security/py-openssl \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}oslo.db>=4.24.0:devel/py-oslo.db \
		${PYTHON_PKGNAMEPREFIX}oslo.i18n>=2.1.0:devel/py-oslo.i18n \
		${PYTHON_PKGNAMEPREFIX}oslo.log>=3.22.0:devel/py-oslo.log \
		${PYTHON_PKGNAMEPREFIX}oslo.messaging>=5.24.2:devel/py-oslo.messaging \
		${PYTHON_PKGNAMEPREFIX}oslo.middleware>=3.27.0:devel/py-oslo.middleware \
		${PYTHON_PKGNAMEPREFIX}oslo.policy>=1.23.0:devel/py-oslo.policy \
		${PYTHON_PKGNAMEPREFIX}retrying>=1.2.3:devel/py-retrying \
		${PYTHON_PKGNAMEPREFIX}osprofiler>=1.4.0:devel/py-osprofiler \
		${PYTHON_PKGNAMEPREFIX}glance-store>=0.22.0:devel/py-glance-store \
		${PYTHON_PKGNAMEPREFIX}debtcollector>=1.2.0:devel/py-debtcollector \
		${PYTHON_PKGNAMEPREFIX}cryptography>=1.6:security/py-cryptography \
		${PYTHON_PKGNAMEPREFIX}cursive>=0.1.2:devel/py-cursive \
		${PYTHON_PKGNAMEPREFIX}iso8601>=0.1.11:devel/py-iso8601 \
		${PYTHON_PKGNAMEPREFIX}monotonic>=0.6:devel/py-monotonic

NO_ARCH=	yes

USES=		python
USE_PYTHON=	autoplist distutils noegginfo

USE_RC_SUBR=	glance-api glance-registry glance-scrubber
USERS=		glance
GROUPS=		glance

post-extract:
	@(cd ${WRKSRC}/etc; for f in *.conf; do ${MV} $${f} $${f}.sample; done)

post-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/etc/${PORTNAME}
	${CP} -R ${WRKSRC}/etc/ ${STAGEDIR}${PREFIX}/etc/${PORTNAME}

.include <bsd.port.mk>
