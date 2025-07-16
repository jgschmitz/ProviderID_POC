# 🩺 Provider Entity MongoDB Migration

This repository contains the ETL pipeline, schema model, and infrastructure-as-code needed to migrate the normalized RDBMS `provider` entity into a denormalized MongoDB document model.

---

## 📌 Project Objective

Transform the following SQL Server tables into a nested MongoDB collection named `providerEntity` under `providerDB`. This enables high-throughput NPI lookups, flexible filtering (e.g., by orgId, zip, status), and long-term archiving of inactive records.

---

## 📂 Relational-to-Document Mapping

The following tables are merged into a single JSON document using `prov_enty_sk` as the join key:

| Table               | Join Key       | Embedded As                               |
|---------------------|----------------|--------------------------------------------|
| `D_PROV_ENTY`        | `prov_enty_sk` | Root document                              |
| `A_PROV_ENTY_AFFIL`  | `prov_enty_sk` | `affiliations[]`                           |
| `A_PROV_ENTY_EXTR_ID`| `prov_enty_sk` | `externalIds[]`                            |
| `A_PROV_ENTY_ADR`    | `prov_enty_sk` | `addresses[]`                              |
| `A_PROV_ENTY_CLB`    | `prov_enty_sk` | `clubs[]`                                  |
| `BV_PROV_DTL`        | `prov_enty_sk` | Extended fields (e.g., `npi`, `roleCd`, `fax`) |

---

## 🚀 Contents

```bash
.
├── etl/
│   ├── export.sql.ps1           # PowerShell script to export source tables to CSV
│   ├── transform.py             # Python ETL: merge CSVs into providerEntity JSON
│   └── providerEntity.json      # Output JSON file ready for mongoimport
├── schema/
│   ├── validator.json           # MongoDB $jsonSchema validator
│   └── indexes.js               # Index creation script
├── terraform/
│   └── ...                      # MongoDB Atlas cluster provisioning
├── load/
│   └── import.sh                # mongoimport commands
└── README.md
