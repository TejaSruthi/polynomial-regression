#load the dataset
datset = read.csv('Position_Salaries.csv')
datset = datset[2:3]

#fitting linear model to datset
lin_reg = lm(formula = Salary ~ .,data = datset )

#fitting polinomial regression to dataset
datset$level2 = datset$Level^2
datset$level3 = datset$Level^3
datset$level4 = datset$Level^4
poly_reg = lm(formula = Salary ~ ., data = datset)

#visualizing the linear regression result
library('ggplot2')
ggplot() +
  geom_point(aes(x = datset$Level, y = datset$Salary),
             color = 'red')+
  geom_line(aes(x = datset$Level, y= predict(lin_reg, newdata = datset)),
            color = 'blue') +
  ggtitle('Truth vs Bluff(Linear Regression)') +
  xlab('Position levels') +
  ylab('Salary')

#visualizing the polynomial regression result
x_small_points = seq(min(datset$Level),max(datset$Level),0.1)
ggplot()+
  geom_point(aes(x = datset$Level, y= datset$Salary),
             color = 'pink')+
  geom_line(aes(x = x_small_points, y = predict(poly_reg, newdata = data.frame(Level = x_small_points,
                                                                               level2 = x_small_points^2,
                                                                               level3 = x_small_points^3,
                                                                               level4 = x_small_points^4))),
            color = 'black')+
  ggtitle('Truth or bluff(Polynomial regression)')+
  xlab('Position Levels')+
  ylab('Salary')

#predict a new result for linear regression
y_lin = predict(lin_reg,data.frame(Level = 6.5))

# predict a new result for polynomial regression
y_poly = predict(poly_reg, data.frame(Level = 6.5, level2 = 6.5^2,
                                      level3 = 6.5^3, level4 = 6.5^4))