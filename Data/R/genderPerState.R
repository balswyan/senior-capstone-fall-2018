library(plyr)
library(plotly)
options(max.print = .Machine$integer.max)

load("~/Gits/senior-capstone-fall-2018/Data/R/data.Rda")

state_vs_gender <- as.data.frame.matrix(table(data$State,data$Gender))
state_vs_gender <- cbind(rownames(state_vs_gender), state_vs_gender)
rownames(state_vs_gender) <- NULL
colnames(state_vs_gender) <- c("State","Female","Male","Unknown")

# Graph state vs male & female

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

gender_per_state <- plot_ly(
  state_vs_gender, 
  x = state_vs_gender$State, 
  y = state_vs_gender$Female, 
  type = 'bar', 
  name = 'Female') %>%
  
  add_trace(
    y = state_vs_gender$Male, 
    name = 'Male') %>%
  
  add_trace(
    y = state_vs_gender$Unknown, 
    name = 'Unknown') %>%
  
  layout(title = "Missing People per State by Gender",
         xaxis = x,
         yaxis = y
  )