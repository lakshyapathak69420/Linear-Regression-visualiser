class linear_regression:
    '''
    writing linear regression for data with single feature (only x)
    m -> weight 
    c -> bais
    alpha -> learning rate
    number_of_iteration -> number of iteration for gradient descent to run
    output -> prediction made by algorithms
    '''
    def __init__(self, alpha = 0.01, number_of_interation = 100):
        self.m = 0 # weight for the linear regression or the slope of the line
        self.c = 0 # baises fot  the linear regression or the intercept
        self.alpha = alpha
        self.number_of_iteration = number_of_interation

    def fit(self, x , y):
            _x = list(x)
            _y = list(y)
            # optimising the weights and baises
            
            for _ in range(self.number_of_iteration):
                __sum__ = 0
                
                # calculating the gradient that sum over all values of (signed error)*the_value for "b"
                for j in range(len(y)):
                    __signed_error__ = (self.m *_x[j] + self.c - _y[j])
                    __sum__ = __sum__ + __signed_error__ * _x[j]
                
                self.m = self.m - self.alpha * __sum__
            
            for _ in range(self.number_of_iteration):
                __sum__ = 0
                # calculating the gradient that sum over all values of (signed error)*the_value for "c"
                for j in range(len(y)):
                    __signed_error__ = (self.m *_x[j] + self.c - _y[j])
                    __sum__ = __sum__ + __signed_error__
                
                self.c = self.c - self.alpha * __sum__
            

    def predict(self , x):
        _x = list(x)
        output = []
        for i in range(len(x)):
            h = self.m * _x[i] + self.c
            output.append(h)
            
        return output
         