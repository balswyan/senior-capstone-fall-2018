library(plyr)
library(plotly)

load("~/Gits/senior-capstone-fall-2018/Data/R/data.Rda")

state_vs_people <- count(data, vars="State.Territory")

f <- list(
  family = "Courier New, monospace",
  size = 18
)
x <- list(
  title = "State or Territory",
  titlefont = f
)
y <- list(
  title = "Missing People",
  titlefont = f
)


missing_people_per_state <- plot_ly(
  x = state_vs_people$State,
  y = state_vs_people$freq,
  type = "bar"
) %>% 
  layout(title = "Missing People per State",
         xaxis = x,
         yaxis = y
  )
