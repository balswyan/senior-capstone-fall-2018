library(plyr)
library(plotly)

load("~/Gits/senior-capstone-fall-2018/Data/R/data.Rda")

people_vs_year <- count(data[1:14770,], c("Year"))

f <- list(
  family = "Courier New, monospace",
  size = 18
)
x <- list(
  title = "Year",
  titlefont = f
)
y <- list(
  title = "Missing People",
  titlefont = f
)

people_per_year <- plot_ly(
  people_vs_year, x = people_vs_year$Year, 
  y = people_vs_year$freq, 
  type = 'scatter', mode = 'lines') %>%
  
  layout(title = "Missing People per Year",
         xaxis = x,
         yaxis = y
  )

