library(ggplot2)

ggplot(mtcars,aes(factor(cyl),mpg))+geom_boxplot()+
  geom_point(aes(color=factor(am),shape=factor(am)),position=position_dodge(width=0.5))