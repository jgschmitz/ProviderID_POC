<#
.SYNOPSIS
  Export Provider Entity tables from SQL Server to CSV using BCP.

.PARAMETER SqlInstance
  SQL Server instance name (e.g. "SQL01").

.PARAMETER DbName
  Database name (e.g. "PROVIDER_DB").

.PARAMETER OutDir
  Output directory for CSV files.
#>

param(
  [string]$SqlInstance,
  [string]$DbName,
  [string]$OutDir = "./csv"
)

$tables = @(
  @{ Name = 'D_PROV_ENTY';        File = 'd_prov_enty.csv' },
  @{ Name = 'A_PROV_ENTY_AFFIL';  File = 'a_prov_enty_affil.csv' },
  @{ Name = 'A_PROV_ENTY_EXTR_ID';File = 'a_prov_enty_extr_id.csv' },
  @{ Name = 'A_PROV_ENTY_ADR';    File = 'a_prov_enty_adr.csv' },
  @{ Name = 'A_PROV_ENTY_CLB';    File = 'a_prov_enty_clb.csv' },
  @{ Name = 'BV_PROV_DTL';        File = 'bv_prov_dtl.csv' }
)

if (-not (Test-Path $OutDir)) {
  New-Item -ItemType Directory -Path $OutDir | Out-Null
}

foreach ($table in $tables) {
  $path = Join-Path $OutDir $table.File
  Write-Host "📤 Exporting $($table.Name) → $path"
  bcp "$DbName.dbo.$($table.Name)" out $path -c -t"," -S $SqlInstance -T
}

Write-Host "`n✅ Export complete. Files saved to $OutDir"
