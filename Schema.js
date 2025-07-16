{
  "_id": NumberLong(<D_PROV_ENTY_SK>),          // from D_PROV_ENTY
  "npi": "1234567890",                           // from BV_PROV_DTL → NPI
  "name": {
    "first": "John",
    "middle": "Q",
    "last": "Smith",
    "suffix": "MD"
  },
  "status": "ACTIVE",                            // provEntyPricpStsCd
  "roleCode": "PHYSICIAN",                       // provEntyRoleCd
  "specialty": "Cardiology",                     // provEntSpclCd or related
  "contact": {
    "email": "jsmith@provider.com",
    "phone": "555-555-5555",
    "fax": "555-555-0000"
  },
  "addresses": [
    {
      "addressType": "PRACTICE",
      "line1": "123 Main St",
      "line2": "Suite 200",
      "city": "Boston",
      "state": "MA",
      "postalCode": "02116",
      "country": "USA",
      "effectiveDate": ISODate("2020-01-01"),
      "endDate": ISODate("9999-12-31")
    }
  ],
  "affiliations": [
    {
      "orgId": "HOSP123",
      "type": "HOSPITAL",
      "effectiveDate": ISODate("2019-01-01"),
      "endDate": ISODate("9999-12-31")
    }
  ],
  "externalIds": [
    {
      "system": "OPTUM",
      "value": "OPT1234",
      "effectiveDate": ISODate("2021-06-01"),
      "endDate": ISODate("9999-12-31")
    }
  ],
  "clubs": [
    {
      "clbId": "CARDIO01",
      "subClbId": "SUB001"
    }
  ],
  "metadata": {
    "createdAt": ISODate("2025-07-16T00:00:00Z"),
    "updatedAt": ISODate("2025-07-16T00:00:00Z"),
    "createdBy": "system",
    "updatedBy": "system"
  }
}
