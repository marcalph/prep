# Notes

## relationnal DB vs NoSQL

### relational DB limits (Postgres, cloud sql, cloud spanner)

- sparse rows
- attribute tables
- serialized json/yaml in columns
- many to many joins or recursive trees
- schema chanegs
- write bottleneck
- data volume

### KV stores (Redis,  gcloud memorystore, dynamo db)

low latency, high throughput best for

- caching
- session storage
- key based retirval

### document store (mongo, )

querying within nested fields in documents, filtering and agg

- user profiles or cms (evolving schemas)
- complex nested queries

### column store (big table)

for large analytical workloads, high write throughput scenarios (time series, logs)

### graph (neo4j)

handle queries with transitive relationship (friend of a friend)
many to many relationships and hierarchical data

- KG
- social
- recommendation engine
- fraud

### db replication

- multi master (when write heavy but harder to maintain consistency when conflict)
- circular (ring topolgy for smaller clusters + adds latency)

### caching strategies

- write heavy, read light (logs)
- write light, read heavy (user profile, news) 
- unicity of data (search queries)



read-thourgh + write through -> perfect consistency

| Caching Strategy            | Description                                                                                                      | Suitable For Data Type                | Example Use Cases                                     |
|-----------------------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------|-------------------------------------------------------|
| Cache-Aside (Lazy Loading)  | The application checks the cache first. If data is missing, it loads from the DB and then caches it. [complexity in cache consistency]             | Read-Intensive or Mixed (low write frequency) | Contracts (infrequent updates, frequent reads); Chat history (mostly reads); product catalogs |
| Read-Through                | The cache automatically loads missing data from the DB during read requests, making the process transparent. [complexity on cache consistency]     | Read-Intensive                        | Logs (frequent analytical queries); Web content; product catalog delivery             |
| Write-Through               | Every write operation updates both the cache and the DB synchronously, ensuring strong consistency.              | Write-Intensive or Mixed              | Payments (critical, consistent transactions); Contracts (high consistency) |
| Write-Around | Writes bypass the cache and go directly to the database; the cache is updated only when a subsequent read occurs.  | First read incurs higher latency due to cache miss; increased load on the DB for initial reads. | Infrequently read product updates, certain log data ingestion. |
| Write-Behind (Write-Back)   | Writes update the cache immediately and are asynchronously flushed to the DB later, improving write performance - eventual consistency. [Risk of data loss on failure; complexity in handling asynchronous persistence]  | Write-Intensive                       | Chat messages (rapid, high-volume writes); Logs (massive ingestion); analytics data; notifications?  |
| Refresh-Ahead               | The cache proactively refreshes data before it expires based on access patterns, keeping data fresh for reads.     | Read-Intensive (with predictable patterns) | Contracts (ensuring up-to-date information for compliance); Dashboards for Logs |
|Read-Through + Write-Through| A combination where both read and write operations pass through the cache ensures data is consistent and up-to-date, suitable for applications |Mixed|(like payments) that require strong consistency on both reads and writes


### db scaling

- sharding, but needs consistent hashing for reasharding
- celebrity problem

## scaling strategy

- Keep web tier stateless
- Build redundancy at every tier
- Cache data as much as you can
- Support multiple data centers
- Host static assets in CDN
- Scale your data tier by sharding
- Split tiers into individual services
- Monitor your system and use automation tools
