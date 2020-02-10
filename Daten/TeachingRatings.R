data(TeachingRatings, package="AER")
library(dplyr)
set.seed(1896)
TeachingRatings <- TeachingRatings %>%
  group_by(prof) %>%
  sample_n(size = 1) %>%
  ungroup()
