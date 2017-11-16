# $FreeBSD: head/security/py-keystone/Makefile 428767 2016-12-17 15:31:09Z novel $

PORTNAME=	keystone
PORTVERSION=	12.0.0
CATEGORIES=	security python
MASTER_SITES=	https://fossies.org/linux/misc/openstack/
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	OpenStack Keystone

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pbr>=2.0.0:devel/py-pbr
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}Babel>=2.3.4:devel/py-babel \
		${PYTHON_PKGNAMEPREFIX}webob>=1.7.1:www/py-webob \
		${PYTHON_PKGNAMEPREFIX}PasteDeploy>=1.5.0:www/py-pastedeploy \
		${PYTHON_PKGNAMEPREFIX}Paste>0:www/py-paste \
		${PYTHON_PKGNAMEPREFIX}routes>=2.3.1:www/py-routes \
		${PYTHON_PKGNAMEPREFIX}cryptography>=1.6:security/py-cryptography \
		${PYTHON_PKGNAMEPREFIX}six>=1.9.0:devel/py-six \
		${PYTHON_PKGNAMEPREFIX}sqlalchemy11>=1.0.10:databases/py-sqlalchemy10 \
		${PYTHON_PKGNAMEPREFIX}sqlalchemy-migrate>=0.11.0:databases/py-sqlalchemy-migrate \
		${PYTHON_PKGNAMEPREFIX}stevedore>=1.20.0:devel/py-stevedore \
		${PYTHON_PKGNAMEPREFIX}passlib>=1.7.0:security/py-passlib \
		${PYTHON_PKGNAMEPREFIX}python-keystoneclient>=3.8.0:net/py-python-keystoneclient \
		${PYTHON_PKGNAMEPREFIX}keystonemiddleware>=4.12.0:devel/py-keystonemiddleware \
		${PYTHON_PKGNAMEPREFIX}bcrypt>=3.1.3:security/py-bcrypt \
		${PYTHON_PKGNAMEPREFIX}scrypt>=0.8.0:security/py-scrypt \
		${PYTHON_PKGNAMEPREFIX}oslo.cache>=1.5.0:devel/py-oslo.cache \
		${PYTHON_PKGNAMEPREFIX}oslo.concurrency>=3.8.0:devel/py-oslo.concurrency \
		${PYTHON_PKGNAMEPREFIX}oslo.config>=4.0.0:devel/py-oslo.config \
		${PYTHON_PKGNAMEPREFIX}oslo.context>=2.14.0:devel/py-oslo.context \
		${PYTHON_PKGNAMEPREFIX}oslo.messaging>=5.24.2:devel/py-oslo.messaging \
		${PYTHON_PKGNAMEPREFIX}oslo.db>=4.24.0:devel/py-oslo.db \
		${PYTHON_PKGNAMEPREFIX}oslo.i18n>=2.1.0:devel/py-oslo.i18n \
		${PYTHON_PKGNAMEPREFIX}oslo.log>=3.22.0:devel/py-oslo.log \
		${PYTHON_PKGNAMEPREFIX}oslo.middleware>=3.27.0:devel/py-oslo.middleware \
		${PYTHON_PKGNAMEPREFIX}oslo.policy>=1.23.0:devel/py-oslo.policy \
		${PYTHON_PKGNAMEPREFIX}oslo.serialization>=1.10.0:devel/py-oslo.serialization \
		${PYTHON_PKGNAMEPREFIX}oslo.utils>=3.20.0:devel/py-oslo.utils \
		${PYTHON_PKGNAMEPREFIX}oauthlib>=0.6:security/py-oauthlib \
		${PYTHON_PKGNAMEPREFIX}pysaml2>=2.4.0:security/py-pysaml2 \
		${PYTHON_PKGNAMEPREFIX}dogpile.cache>=0.6.2:devel/py-dogpile.cache \
		${PYTHON_PKGNAMEPREFIX}jsonschema>=2.0.0:devel/py-jsonschema \
		${PYTHON_PKGNAMEPREFIX}pycadf>=1.1.0:devel/py-pycadf \
		${PYTHON_PKGNAMEPREFIX}msgpack-python>=0.4.0:devel/py-msgpack-python \
		${PYTHON_PKGNAMEPREFIX}osprofiler>=1.4.0:devel/py-osprofiler \
		${PYTHON_PKGNAMEPREFIX}pytz>=2013.6:devel/py-pytz

NO_ARCH=	yes

USES=		python
USE_PYTHON=	autoplist distutils noegginfo

USERS=		keystone
GROUPS=		keystone

post-patch:
	${REINPLACE_CMD} -e "s|/etc/keystone|${PREFIX}/etc/${PORTNAME}|g" \
		${WRKSRC}/doc/source/admin/cli-keystone-manage-services.rst \
		${WRKSRC}/doc/source/admin/federated-identity.rst \
		${WRKSRC}/doc/source/admin/identity-caching-layer.rst \
		${WRKSRC}/doc/source/admin/identity-certificates-for-pki.rst \
		${WRKSRC}/doc/source/admin/identity-concepts.rst \
		${WRKSRC}/doc/source/admin/identity-credential-encryption.rst \
		${WRKSRC}/doc/source/admin/identity-domain-specific-config.rst \
		${WRKSRC}/doc/source/admin/identity-fernet-token-faq.rst \
		${WRKSRC}/doc/source/admin/identity-integrate-with-ldap.rst \
		${WRKSRC}/doc/source/admin/identity-keystone-usage-and-features.rst \
		${WRKSRC}/doc/source/admin/identity-service-api-protection.rst \
		${WRKSRC}/doc/source/admin/identity-tokens.rst \
		${WRKSRC}/doc/source/admin/identity-token-binding.rst \
		${WRKSRC}/doc/source/admin/identity-troubleshoot.rst \
		${WRKSRC}/doc/source/admin/identity-upgrading.rst \
		${WRKSRC}/doc/source/admin/index.rst \
		${WRKSRC}/doc/source/advanced-topics/federation/configure_federation.rst \
		${WRKSRC}/doc/source/advanced-topics/event_notifications.rst \
		${WRKSRC}/doc/source/api_curl_examples.rst \
		${WRKSRC}/doc/source/configuration/config-options.rst \
		${WRKSRC}/doc/source/configuration/samples/index.rst \
		${WRKSRC}/doc/source/configuration/samples/logging-conf.rst \
		${WRKSRC}/doc/source/install/keystone-install-obs.rst \
		${WRKSRC}/doc/source/install/keystone-install-rdo.rst \
		${WRKSRC}/doc/source/install/keystone-install-ubuntu.rst \
		${WRKSRC}/doc/source/install/keystone-verify-obs.rst \
		${WRKSRC}/doc/source/install/keystone-verify-rdo.rst \
		${WRKSRC}/doc/source/install/keystone-verify-ubuntu.rst \
		${WRKSRC}/doc/source/configuration.rst \
		${WRKSRC}/etc/keystone.conf.sample \
		${WRKSRC}/keystone/conf/constants.py \
		${WRKSRC}/keystone/conf/credential.py \
		${WRKSRC}/keystone/conf/federation.py \
		${WRKSRC}/keystone/conf/fernet_tokens.py \
		${WRKSRC}/keystone/conf/identity.py \
		${WRKSRC}/keystone/conf/saml.py \
		${WRKSRC}/keystone/conf/signing.py \
		${WRKSRC}/keystone/common/profiler.py \
		${WRKSRC}/keystone/tests/unit/credential/test_fernet_provider.py \
		${WRKSRC}/keystone/tests/unit/test_cli.py \
		${WRKSRC}/keystone/tests/unit/test_ldap_tls_livetest.py

post-install:
	${MKDIR} ${STAGEDIR}${ETCDIR}
	${CP} -R ${WRKSRC}/etc/ ${STAGEDIR}${ETCDIR}

.include <bsd.port.mk>
