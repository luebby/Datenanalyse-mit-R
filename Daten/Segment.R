# Basierend auf den R Code aus:
# R for Marketing Research and Analytics, Chapter 5
# http://r-marketing.r-forge.r-project.org/code/chapter5-ChapmanFeit.R
#
# Authors:  Chris Chapman               Elea McDonnell Feit
#           cnchapman+rbook@gmail.com   efeit@drexel.edu
#
# Copyright 2015, Springer 
#
# Last update: January 7, 2015
# Version: 1.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Übersetzung und Anpassung: Karsten Lübke karsten@statistix.org

#### Create the data

# Names of the variables we will define for each segment
segVars <- c("Alter", "Geschlecht", "Einkommen", "Kinder", "Eigenheim", "Mitgliedschaft")

# the data type for each segment
segVarType <- c("norm", "binom", "norm", "pois", "binom", "binom")

# names of the segments
segNames <- c("Gemischte Vorstadt", "Hippe Innenstadt", "Pendler", "Aufsteiger")

# the size of each segment (N)
segSize <- c(100, 50, 80, 70)

# the means for each variable for each segment
segMeans <- matrix( c(
  40, .5, 55000, 2, .5, .1,
  24, .7, 21000, 1, .2, .2,
  58, .5, 64000, 0, .7, .05,
  36, .3, 52000, 2, .3, .2  ), ncol=length(segVars), byrow=TRUE)

# the standard deviations for each segment (NA = not applicable for the variable)
segSDs <- matrix( c(
  5, NA, 12000, NA, NA, NA,
  2, NA,  5000, NA, NA, NA,
  8, NA, 21000, NA, NA, NA,
  4, NA, 10000, NA, NA, NA  ), ncol=length(segVars), byrow=TRUE)


# make sure we're starting our dataset from a known state
seg.df <- NULL
set.seed(1896)

# iterate over all the segments and create data for each
for (i in seq_along(segNames)) {    
  cat(i, segNames[i], "\n")
  
  # create an empty matrix to hold this particular segment's data
  this.seg <- data.frame(matrix(NA, nrow=segSize[i], ncol=length(segVars)))
  
  # within a segment, iterate over the variables and draw appropriate random data
  for (j in seq_along(segVars)) {    # and iterate over each variable
    if (segVarType[j] == "norm") {   # draw random normals
      this.seg[, j] <- rnorm(segSize[i], mean=segMeans[i, j], sd=segSDs[i, j])
    } else if (segVarType[j] == "pois") {    # draw counts
      this.seg[, j] <- rpois(segSize[i], lambda=segMeans[i, j])
    } else if (segVarType[j] == "binom") {   # draw binomials
      this.seg[, j] <- rbinom(segSize[i], size=1, prob=segMeans[i, j])
    } else {
      stop("Bad segment data type: ", segVarType[j])
    }
  }
  # add this segment to the total dataset
  seg.df <- rbind(seg.df, this.seg)     
}
# make the data frame names match what we defined
names(seg.df) <- segVars
# add segment membership for each row
seg.df$Segment   <- factor(rep(segNames, times=segSize))
# convert the binomial variables to nicely labeled factors
seg.df$Eigenheim    <- factor(seg.df$Eigenheim , labels=c("Nein", "Ja"))
seg.df$Geschlecht    <- factor(seg.df$Geschlecht, labels=c("Frau", "Mann"))
seg.df$Mitgliedschaft  <- factor(seg.df$Mitgliedschaft, labels=c("Nein", "Ja"))

# check the data and confirm it
summary(seg.df)