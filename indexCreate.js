// Indexes for providerEntity collection
use providerDB;

// Unique NPI
db.providerEntity.createIndex(
  { npi: 1 },
  { unique: true, name: "uk_npi" }
);

// External ID compound index
db.providerEntity.createIndex(
  { npi: 1, "externalIds.value": 1 },
  { name: "idx_npi_external_value" }
);

// Org ID index for affiliations
db.providerEntity.createIndex(
  { "affiliations.orgId": 1 },
  { name: "idx_affiliations_orgId" }
);

// TTL index on inactiveAt (7 years = 220,752,000 seconds)
db.providerEntity.createIndex(
  { inactiveAt: 1 },
  { expireAfterSeconds: 220752000, name: "ttl_inactiveAt" }
);
