
data <- read.csv("~/Documents/gitrepos/garminRunning/csvs/3195035949.csv")
hist(data$cadence,xlab="Cadence per minute", ylab="Count")

# great distribution of distances to show the training
hist(data$distance, xlab="Miles Run",ylab="Count")

# speed
hist(data$enhanced_speed, xlab = "Speed", ylab = "Count")

# heartrate
hist(data$heart_rate, xlab = "Heart Rate", ylab = "Count")

