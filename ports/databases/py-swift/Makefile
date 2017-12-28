# Created by: Gea-Suan Lin <gslin@gslin.org>
# $FreeBSD: head/databases/py-swift/Makefile 455210 2017-11-30 15:50:30Z mat $

PORTNAME=	swift
PORTVERSION=	2.15.1
CATEGORIES=	databases python
MASTER_SITES=	https://fossies.org/linux/misc/openstack/
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	Highly available, distributed, eventually consistent object/blob store

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}dnspython>=1.14.0:dns/py-dnspython \
		${PYTHON_PKGNAMEPREFIX}eventlet19>=0.18.2:net/py-eventlet19 \
		${PYTHON_PKGNAMEPREFIX}greenlet>=0.3.2:devel/py-greenlet \
		${PYTHON_PKGNAMEPREFIX}netifaces>=0.5:net/py-netifaces \
		${PYTHON_PKGNAMEPREFIX}PasteDeploy>=1.3.3:www/py-pastedeploy \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}xattr>=0.4:devel/py-xattr \
		${PYTHON_PKGNAMEPREFIX}PyECLib>=1.3.1:devel/py-pyeclib \
		${PYTHON_PKGNAMEPREFIX}cryptography>=1.6:security/py-cryptography

USES=		python:2.7
USE_PYTHON=	distutils autoplist
USE_RC_SUBR=	swift
USERS=		swift
GROUPS=		swift

post-extract:
	@(cd ${WRKSRC}/etc; \
	for f in *-sample; do\
	${MV} $${f} $${f%%-sample}.sample;\
	done)

post-patch:
	@${REINPLACE_CMD} -e "s|/etc/swift|${PREFIX}/etc/${PORTNAME}|" \
		-e "s|conf-sample|conf.sample|" \
		-e "s|types-sample|types.sample|" \
		${WRKSRC}/bin/swift-account-audit \
		${WRKSRC}/bin/swift-account-info \
		${WRKSRC}/bin/swift-container-info \
		${WRKSRC}/bin/swift-dispersion-populate \
		${WRKSRC}/bin/swift-dispersion-report \
		${WRKSRC}/bin/swift-get-nodes \
		${WRKSRC}/bin/swift-object-info \
		${WRKSRC}/bin/swift-recon \
		${WRKSRC}/bin/swift-recon-cron \
		${WRKSRC}/bin/swift-reconciler-enqueue \
		${WRKSRC}/doc/manpages/account-server.conf.5 \
		${WRKSRC}/doc/manpages/container-server.conf.5 \
		${WRKSRC}/doc/manpages/dispersion.conf.5 \
		${WRKSRC}/doc/manpages/object-expirer.conf.5 \
		${WRKSRC}/doc/manpages/object-server.conf.5 \
		${WRKSRC}/doc/manpages/proxy-server.conf.5 \
		${WRKSRC}/doc/manpages/swift-dispersion-populate.1 \
		${WRKSRC}/doc/manpages/swift-dispersion-report.1 \
		${WRKSRC}/doc/manpages/swift-get-nodes.1 \
		${WRKSRC}/doc/manpages/swift-recon.1 \
		${WRKSRC}/etc/account-server.conf.sample \
		${WRKSRC}/etc/container-reconciler.conf.sample \
		${WRKSRC}/etc/container-server.conf.sample \
		${WRKSRC}/etc/dispersion.conf.sample \
		${WRKSRC}/etc/object-expirer.conf.sample \
		${WRKSRC}/etc/object-server.conf.sample \
		${WRKSRC}/etc/proxy-server.conf.sample \
		${WRKSRC}/etc/swift.conf.sample \
		${WRKSRC}/swift.egg-info/SOURCES.txt \
		${WRKSRC}/swift/account/reaper.py \
		${WRKSRC}/swift/cli/info.py \
		${WRKSRC}/swift/cli/recon.py \
		${WRKSRC}/swift/common/constraints.py \
		${WRKSRC}/swift/common/db_replicator.py \
		${WRKSRC}/swift/common/manager.py \
		${WRKSRC}/swift/common/middleware/account_quotas.py \
		${WRKSRC}/swift/common/middleware/container_quotas.py \
		${WRKSRC}/swift/common/middleware/container_sync.py \
		${WRKSRC}/swift/common/middleware/gatekeeper.py \
		${WRKSRC}/swift/common/middleware/list_endpoints.py \
		${WRKSRC}/swift/common/middleware/memcache.py \
		${WRKSRC}/swift/common/middleware/recon.py \
		${WRKSRC}/swift/common/middleware/staticweb.py \
		${WRKSRC}/swift/common/middleware/tempauth.py \
		${WRKSRC}/swift/common/utils.py \
		${WRKSRC}/swift/container/reconciler.py \
		${WRKSRC}/swift/container/server.py \
		${WRKSRC}/swift/container/sync.py \
		${WRKSRC}/swift/container/updater.py \
		${WRKSRC}/swift/obj/expirer.py \
		${WRKSRC}/swift/obj/replicator.py \
		${WRKSRC}/swift/obj/server.py \
		${WRKSRC}/swift/obj/updater.py \
		${WRKSRC}/swift/proxy/server.py \
		${WRKSRC}/test/__init__.py \
		${WRKSRC}/test/functional/tests.py \
		${WRKSRC}/test/probe/common.py \
		${WRKSRC}/test/sample.conf \
		${WRKSRC}/test/unit/common/middleware/test_memcache.py
	@${FIND} ${WRKSRC} -type f -name "*.bak" -delete

post-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/etc/${PORTNAME}
	${CP} -R ${WRKSRC}/etc/ ${STAGEDIR}${PREFIX}/etc/${PORTNAME}
.for n in 1 5
	${INSTALL_MAN} ${WRKSRC}/doc/manpages/*.${n} \
	    ${STAGEDIR}${MANPREFIX}/man/man${n}
.endfor

.include <bsd.port.mk>
