db.providers.find({
  addresses: {
    $elemMatch: {
      state: "MA",
      addressType: "PRACTICE",
      endDate: { $gt: new Date() }
    }
  }
})
