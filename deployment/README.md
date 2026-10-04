# Deployment

The challenger deploys independently of the current production scanner. Production-control services are not replaced or disabled during buildout.

Recommended deployment sequence: test -> shadow -> prospective evaluation -> promotion approval -> immutable release. Keep prior release available for rollback.
