#!/usr/bin/env python3
"""
Transform and merge normalized provider CSVs into MongoDB JSON format.
"""

import csv, json, argparse, pathlib, collections
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--csv-dir', default='csv')
parser.add_argument('--out', default='providerEntity.json')
args = parser.parse_args()

csv_dir = pathlib.Path(args.csv_dir)

# Group child rows by prov_enty_sk
affils = collections.defaultdict(list)
extr_ids = collections.defaultdict(list)
addresses = collections.defaultdict(list)
clubs = collections.defaultdict(list)
details = {}

# Load affiliations
with open(csv_dir / 'a_prov_enty_affil.csv') as f:
    for row in csv.DictReader(f):
        sk = int(row['prov_enty_sk'])
        affils[sk].append({
            'orgId': row['org_id'],
            'type': row['type'],
            'effectiveDate': row['eff_dt'],
            'endDate': row['end_dt']
        })

# Load external IDs
with open(csv_dir / 'a_prov_enty_extr_id.csv') as f:
    for row in csv.DictReader(f):
        sk = int(row['prov_enty_sk'])
        extr_ids[sk].append({
            'system': row['sys'],
            'value': row['val'],
            'effectiveDate': row['eff_dt'],
            'endDate': row['end_dt']
        })

# Load addresses
with open(csv_dir / 'a_prov_enty_adr.csv') as f:
    for row in csv.DictReader(f):
        sk = int(row['prov_enty_sk'])
        addresses[sk].append({
            'addressType': row['type'],
            'line1': row['line1'],
            'line2': row['line2'] or None,
            'city': row['city'],
            'state': row['state'],
            'postalCode': row['zip'],
            'country': row['country'],
            'effectiveDate': row['eff_dt'],
            'endDate': row['end_dt']
        })

# Load clubs
with open(csv_dir / 'a_prov_enty_clb.csv') as f:
    for row in csv.DictReader(f):
        sk = int(row['prov_enty_sk'])
        clubs[sk].append({
            'clbId': row['prov_clb_sk'],
            'subClbId': row['sub_clb_sk']
        })

# Load provider details
with open(csv_dir / 'bv_prov_dtl.csv') as f:
    for row in csv.DictReader(f):
        sk = int(row['prov_enty_sk'])
        details[sk] = {
            'npi': row.get('npi'),
            'roleCd': row.get('prov_enty_role_cd'),
            'fax': row.get('fax_num_txt'),
            'phone': row.get('tel_num_txt')
        }

# Merge into providerEntity JSON
with open(csv_dir / 'd_prov_enty.csv') as fin, open(args.out, 'w') as fout:
    for row in csv.DictReader(fin):
        sk = int(row['prov_enty_sk'])
        doc = {
            '_id': sk,
            'name': {
                'first': row.get('prov_fst_nm'),
                'middle': row.get('prov_midl_nm'),
                'last': row.get('prov_lst_nm'),
                'suffix': row.get('prov_sufx_nm')
            },
            'status': row.get('prov_prtcp_sts_cd'),
            'affiliations': affils.get(sk, []),
            'externalIds': extr_ids.get(sk, []),
            'addresses': addresses.get(sk, []),
            'clubs': clubs.get(sk, []),
            'metadata': {
                'createdAt': datetime.utcnow().isoformat() + 'Z',
                'updatedAt': datetime.utcnow().isoformat() + 'Z'
            }
        }
        doc.update(details.get(sk, {}))  # Inject npi, roleCd, etc.
        fout.write(json.dumps(doc) + '\n')

print(f"✅ Wrote JSON docs to {args.out}")
