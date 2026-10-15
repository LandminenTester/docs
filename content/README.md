# LandminenTester documentation

Public guides for installing, configuring, building, maintaining and using the BlackICE server tools.

| Product | Start here | Reference |
|---|---|---|
| BlackICE Server Panel | [Install and overview](webpanel/README.md) | [Operations](webpanel/docs/operations.md), [HTTP API](webpanel/API.md) |
| lt-database | [Bundle overview](lt-database/README.md), [Install](lt-database/docs/INSTALL.md) | [C# helper and exports](lt-database/docs/REFERENCE.md), [compiled recipes](lt-database/docs/RECIPES.md) |
| lt-database-api | [API overview](lt-database-api/README.md), [Deployment](lt-database-api/docs/DEPLOYMENT.md) | [HTTP API](lt-database-api/docs/API.md), [OpenAPI](lt-database-api/docs/openapi.yaml) |

## How the pieces fit together

The panel starts and maintains one BlackICE server. Server-side game bundles call `lt-database` exports; that connector
sends signed HTTPS requests to `lt-database-api`. The API stores data in PostgreSQL, MySQL/MariaDB or MongoDB.
The panel is optional for using the database pair. Players never receive the API secret.

Start with the [end-to-end setup](getting-started.md). **Writes are live by default.** Enable the optional
[write-behind mode](lt-database-api/docs/WRITE-BEHIND.md) to buffer validated writes until an interval, fixed time,
threshold or explicit flush. Schema synchronization is a separate operation and runs immediately.

The repository name is `lt-database`. Existing consumers retain the `WestwoodDb` / `WestwoodDbClient` namespaces and
the default bundle folder `westwood_database`; [installation](lt-database/docs/INSTALL.md#folder-name) explains changing
the folder without breaking consumers.

## Source, support and versions

Documentation is imported from the public product repositories. [Source revisions](sources.md) identify exactly which
commits it describes. Read stable releases for production and the experimental panel guide when using experimental features.

Report product bugs in the corresponding repository:
[Panel](https://github.com/LandminenTester/blackice-server-panel/issues),
[Bundle](https://github.com/LandminenTester/lt-database/issues),
[API](https://github.com/LandminenTester/lt-database-api/issues).
Use each product's security policy for sensitive findings.

Older Brewery script documentation remains preserved in the
[documentation repository](https://github.com/LandminenTester/docs/tree/main/scripts).
