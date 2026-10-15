# Database pair quickstart

`lt_database` connects BlackICE server bundles to `lt-database-api`. The API stores data in PostgreSQL, MySQL/MariaDB
or MongoDB. This guide covers that pair; it can be used on any BlackICE server you control.

## 1. Run the API and a database

For a disposable local trial, install Docker and Compose:

```sh
git clone https://github.com/LandminenTester/lt-database-api
cd lt-database-api
cp .env.example .env
# Replace the example API secret and database password with random values.
docker compose --profile postgres up --build -d
curl http://127.0.0.1:8080/v1/health
```

Use `mysql` or `mongodb` instead of `postgres` for another engine. Health GET is public and does not verify database access;
the signed health operation does. Follow [deployment](lt-database-api/docs/DEPLOYMENT.md) for production, TLS,
least-privilege database users, backups and service installation. Keep the trial port on loopback.

## 2. Install lt_database

Download the [bundle release](https://github.com/LandminenTester/lt-database/releases), then extract it into
`<server>/data/ugc/lt_database/`. Follow [installation](lt-database/docs/INSTALL.md) to allow the API host in `config.toml`,
create private `vfs/database.json` and `vfs/database.secret` files, and restrict namespaces on both sides.
The key ID and secret must match the API configuration.

```text
start lt_database
lt-db-health
```

A signed health result with `database: true` verifies the connector, signing and database connection. Start consumer
bundles after the connector and keep that order in `server.cfg` when configuring automatic startup.

## 3. Add a consumer

Follow [usage](lt-database/docs/USAGE.md) to include the shared contracts and helper in your server project.
Declare the schema with `Db.Sync` and wait for success before writing. Use the [compiled recipes](lt-database/docs/RECIPES.md)
for CRUD, paging, counters and error handling. [Reference](lt-database/docs/REFERENCE.md) lists the exports and builders.

## 4. Choose live or buffered writes

Writes are live by default. To buffer them, configure [write-behind](lt-database-api/docs/WRITE-BEHIND.md) on the API.
For fixed times only, set `FlushIntervalSeconds: 0` and `FlushThreshold: 0`, then configure `FlushAt` and `TimeZone`.

Queued receipts do not contain generated IDs or affected counts. Check `Db.IsQueued(result)`, and use `Db.Flush` or
`immediate: true` when current data is required. Protect the journal and monitor pending and rejected writes.
Delivery across crashes is at least once; prefer idempotent updates and stable unique keys.

## 5. Validate and maintain

Run the [38-step smoke scenario](lt-database/examples/smoke/README.md) against a disposable live namespace.
Run the API's test suite with Docker available for all three engine suites. Back up databases and pending journals,
test restoration, and follow each product's operations guide for upgrades and key rotation.
