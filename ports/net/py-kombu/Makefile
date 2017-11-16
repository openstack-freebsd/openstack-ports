# Created by: Cheng-Lung Sung <clsung@FreeBSD.org>
# $FreeBSD: head/net/py-kombu/Makefile 429600 2016-12-27 11:44:49Z rene $

PORTNAME=	kombu
PORTVERSION=	4.1.0
CATEGORIES=	net python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	skonmeme@gmail.com
COMMENT=	AMQP messaging framework for Python

LICENSE=	BSD3CLAUSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}amqp>=2.1.4:net/py-amqp \
		${PYTHON_PKGNAMEPREFIX}anyjson>=0.3.3:devel/py-anyjson

#OPTIONS_DEFINE=	QPID REDIS MONGDB ZOOKEEPER MSGPACK YAML SQLALCHEMY LIBRABBITMQ SLMQ CONSUL COUCHDB ETCD PYRO REDIS
#
#QPID_DESC=	Include Apache Qpid support
#REDIS_DESC=	Include Redis transport support
#MONGODB_DESC=	Include MongoDB transport support
#SQS_DESC=	Include AWS transport support
#ZOOKEEPER_DESC=	Include ZooKeeper transport support
#MSGPACK_DESC=	Include In memory transport support
#YAML_DESC=	Include YaML transport support
#SQLALCHEMY_DESC=	Include SQLAlchemy transport support
#LIBRABBITMQ_DESC=	Inlucde RabbitMQ transport support
#SLMQ_DESC=	Include SoftLayer Messaging Queue Control transport support
#CONSUL_DESC=	Include Consul transport support
#COUCHDB_DESC=	Include CouchDB transport support
#ETCD_DESC=	Include CoreOS etcd transport support
#PYRO_DESC=	Include Pyro transport support
#REDIS_DESC=	Include Redis transport support
#
#QPID_RUN_DEPENDS =	${PYTHON_PKGNAMEPREFIX}qpid>=0.26:devel/py-qpid
#REDIS_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}redis>=2.10.5:databases/py-redis
#MONGODB_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pymongo>=2.6.2:databases/py-mongo2
#SQS_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}boto3>=1.4.4:devel/py-boto3 \
#			${PYTHON_PKGNAMEPREFIX}pycurl>0:devel/py-pycurl
#ZOOKEEPER_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}kazoo>=1.3.1:devel/py-kazoo
#MSGPACK_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}msgpack-python>=0.4.7:devel/py-msgpack-python
#YAML_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}yaml>=3.10:devel/py-yaml
#SQLALCHEMY_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sqlalchemy11>0:databases/py-sqlalchemy11
#LIBRABBITMQ_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}librabbitmq>=1.5.2:net/py-librabbitmq
#SLMQ_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}softlayer_messaing>=1.0.3:devel/py-softlayer_messagnig
#CONSUL_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}consul>=0.6.0:sysutils/py-consul
#COUCHDB_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}couchdb>0:databases/py-couchdb
#ETCD_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}etcd>=0.4.3:devel/py-etcd
#PYRO_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pyro>0:devel/py-pyro
#REDIS_RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}redis>=2.10.5:databases/py-redis

USES=		python
USE_PYTHON=	autoplist distutils
NO_ARCH=	yes

.include <bsd.port.mk>
