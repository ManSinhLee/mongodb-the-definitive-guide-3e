db.movies.updateOne({"genre" : "Horror"},
{"$push" : {"top10" : {"$each" : [{"name" : "Nightmare on Elm Street",
"rating" : 6.6},
{"name" : "Saw", "rating" : 4.3}],
"$slice" : -10,
"$sort" : {"rating" : -1}}}})