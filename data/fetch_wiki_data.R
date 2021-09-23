#!/usr/bin/env Rscript

library(rvest)
library(stringr)

URL = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"

html = read_html(URL)

tables = html_table(html, fill = TRUE)


length(tables)

lapply(tables, names)

tbl = tables[[5]]
str(tbl)

tbl = tbl[c("City", "State[c]", "2020census", "2010census", "2020 land area")]
names(tbl) = c("city", "state", "pop2020", "pop2010", "area2020")

tbl[] = lapply(tbl, function(x) {
  # Strip out footnotes
  str_replace_all(x, "\\[.{0,3}\\]", "")
})

cols = c("pop2010", "pop2020")
tbl[cols] = lapply(tbl[cols], \(x) as.numeric(str_replace_all(x, ",", "")))

tbl$area2020 = str_replace_all(tbl$area2020, ",", "")
tbl$area2020 = str_replace(tbl$area2020, "\\ssq\\smi", "")
tbl$area2020 = as.numeric(tbl$area2020)

write.csv(tbl, "city_state_lookup.csv", row.names = FALSE)
