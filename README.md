# Algos from scratch
The intenetion behind this codeing block is to help us get an understanding of the working of the algorithm by coding the core.

Please note that this wont be the most optimized code and for implementation purposes, one should always consider using libraries like sklearn. 

# Gradient Descent
### Prediction
>$\widehat{y} = \beta _{0} + \beta {_1} X$

### Cost function
>$J(\theta) = (y - \widehat{y})^{2}$

>$\Rightarrow J(\theta) = (y - (\beta _{0} + \beta _{1}X))^{2}$

where:

>$ \beta _{0} \rightarrow intercept $ 

>$ \beta _{1} \rightarrow slope $ 

>$ \alpha \rightarrow learning rate $ 


### Gradients
>$ \frac{dl}{d\beta _{1}} = 2 \times X \times (y - (\beta _{0} + \beta _{1}X))$

>$ \frac{dl}{d\beta _{0}} = 2 \times (y - (\beta _{0} + \beta _{1}X))$

### Updates
>$ \beta _{0} = \beta _{0} - (\alpha \times \frac{1}{N} \times \frac{dl}{d\beta _{0}}) $

>$ \beta _{1} = \beta _{1} - (\alpha \times \frac{1}{N} \times \frac{dl}{d\beta _{1}}) $

# k-means clustering
```python
NotImplementedError
```

