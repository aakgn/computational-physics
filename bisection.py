# @author: ali.akgun
# @date: 29.04.2021
# @brief: Bisection root finding algorithm.
# @parameters:
# x1, x2: represents root searching interval. (x1 < x2)
# N: Represents iteration number.(equal to complexity)
# error_margin: Represents error margin of computation.
# @to do:
# Two dimensional root finding !!!
# @bugs:


class Bisection:
    
    def __init__ (self, x1, x2, N, error_margin, function):
        self.x1 = x1
        self.x2 = x2
        self.N = N
        self.error_margin = error_margin
        self.function = function
        
    def broot (self, x1, x2, N, error_margin):
        for i in range(0, N):
            
            x = (x1 + x2) / 2
            
            if (function(x1) * function(x2) > 0):
                x2 = x         
            else:
               x2 = x
            
            if (abs(function(x) < error_margin)):
                break
        
        return x



error_margin = 1e-7
x1 = 1
x2 = 10
N = 1000


user_input = "x*x - 4"
function = lambda x: eval(user_input)
root1 = Bisection(x1, x2, N, error_margin, function)
print(root1.broot(x1, x2, N, error_margin))
