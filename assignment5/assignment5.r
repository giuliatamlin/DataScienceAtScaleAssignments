library(caret)
library(ggplot2)

data = read.csv('seaflow_21min.csv')

#preliminary look at the data

nrow(data) #useful to decide on partitioning in test/validation/train sets
#questions 1 and 2
summary(data) # 7 time windows,32081 cells, crypto label less frequent by approx
# two orders of magnitude

#question 3

set.seed(000)
train_ind = createDataPartition(data$pop,p=0.5)[[1]]#must access the first (and only) element
#of the list to be used as an index array
train = data[train_ind,]
test = data[-train_ind,]

ans = mean(train[,'time'])
