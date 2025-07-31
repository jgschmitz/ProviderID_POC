db.providers.find({
  affiliations: {
    $elemMatch: {
      orgId: "HOSP123",
      type: "HOSPITAL",
      endDate: { $gt: new Date() }
    }
  }
})
