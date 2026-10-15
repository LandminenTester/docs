# End-to-end setup

## 1. Run the API and a database

For a disposable local trial, install Docker and Compose, then:

```sh
git clone https://github.com/LandminenTester/lt-database-api
cd lt-database-api
cp .env.example .env
# Edit .env: replace the example API secret and database password with random values.
docker compose --profile postgres up --build -d
curl http://127.0.0.1:8080/v1/health
```

Use `mysql` or `mongodb` instead of `postgres` for another engine. Health GET is public and does not verify access to
your database; the signed health operation does. Follow [deployment](lt-database-api/docs/DEPLOYMENT.md) for production,
TLS, least-privilege database users, backup and service installation. Keep the local trial port on loopback.

## 2. Install the server and optional panel

Use a BlackICE server you control. The [panel installation guide](webpanel/README.md) covers Windows, Linux and Docker,
first-time administrator setup, game server installation and ports. Start and confirm the server before adding bundles.
Production servers should follow [panel operations](webpanel/docs/operations.md) and its HTTPS proxy instructions.

## 3. Install lt-database

Download the bundle ZIP from [releases](https://github.com/LandminenTester/lt-database/releases).
Extract into `<server>/data/ugc/westwood_database/`. Follow the [complete bundle installation](lt-database/docs/INSTALL.md)
to allow your API host in `config.toml`, create the private `vfs/database.json` and `vfs/database.secret`, and restrict
allowed namespaces on **both** sides. The key ID and secret must match the API configuration.

```text
start westwood_database
westwood-db-health
```

A successful signed health response with `database: true` verifies the connector, signing and database connection.
Start consumer bundles after the connector. Add that order to `server.cfg` for automatic startup.

## 4. Add a consumer

Follow [usage](lt-database/docs/USAGE.md) to include the shared contracts and helper in your server bundle. Declare
your schema with `Db.Sync` and wait for success before writing. Use the [compiled recipes](lt-database/docs/RECIPES.md)
for CRUD, paging, counters and error handling. [Reference](lt-database/docs/REFERENCE.md) lists every export and builder.

## 5. Choose live or buffered writes

Leave `Ldb:WriteBehind:Enabled` false for live writes. To buffer, configure the API as described in
[write-behind](lt-database-api/docs/WRITE-BEHIND.md). For **only fixed times** set `FlushIntervalSeconds: 0` and
`FlushThreshold: 0`; set `FlushAt` and `TimeZone`. Otherwise the interval or threshold may flush earlier.

Queued receipts do not contain generated IDs or affected row counts. Check `Db.IsQueued(result)`. Use `Db.Flush(ns, done)`
or `immediate: true` when current data is required. Protect the journal volume and monitor pending/dead-lettered writes.
Delivery is at least once across crashes; prefer idempotent writes and stable keys.

## 6. Validate and maintain

Run the [38-step smoke scenario](lt-database/examples/smoke/README.md) against a disposable live namespace. For API
development, run `dotnet test -c Release` with Docker running to include all three engine suites.
Back up panel state, database data and pending journals; test restoration. Flush pending writes and check the result
before database maintenance. Follow the product operations guides for key rotation, upgrades and rollback.
