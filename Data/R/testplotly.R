library(plotly)
options(max.print = .Machine$integer.max)

load("~/Gits/senior-capstone-fall-2018/Data/R/dataframe.Rda")
load("~/Gits/senior-capstone-fall-2018/Data/R/missing_in_state.Rda")
load("~/Gits/senior-capstone-fall-2018/Data/R/state_vs_gender.Rda")

# Graph state vs number of people
missing_people_per_state <- plot_ly(
  x = missing_in_states$`State/Territory`,
  y = missing_in_states$`Missing People`,
  name = "Missing People Per State",
  type = "bar"
)

# Graph state vs male & female
gender_per_state <- plot_ly(state_vs_gender, x = state_vs_gender$`States/Territory`, y = state_vs_gender$Female, type = 'bar', name = 'Female') %>%
  add_trace(y = state_vs_gender$Male, name = 'Male') %>%
  add_trace(y = state_vs_gender$Unknown, name = 'Unknown') %>%
  layout(yaxis = list(title = 'Count'), barmode = 'group')

