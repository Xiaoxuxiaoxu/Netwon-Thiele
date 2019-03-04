"""
牛顿Taylor插值算法
"""
class Taylor:
    def Interpolate_Taylor(self,X,Y,value):
        def num_order_difference_quotient(x, y):
            # 记录计算差商
            i = 0
            Num = len(x)
            quotient = []
            for k in range(Num):
                quotient.append(0)
            while i < (Num - 1):
                j = (Num - 1)
                while j > i:
                    if i == 0:
                        quotient[j] = ((y[j] - y[j - 1]) / (x[j] - x[j - 1]))
                    else:
                        quotient[j] = (quotient[j] - quotient[j - 1]) / (x[j] - x[j - 1 - i])
                    j -= 1
                i += 1
            return quotient;

        def function(data, parameters, x, y):
            number = len(x)
            sum = 1
            final_result = 0
            for j in range(len(parameters) - 1):
                for i in range(number - (j + 1)):
                    sum = sum * (data - x[i])
                sum = parameters[i + 1] * sum
                final_result = final_result + sum
                sum = 1
            final_result = final_result + y[0]
            return final_result

        def calculate_data(x, parameters, X, Y):
            returnData = (function(x, parameters, X, Y))
            return returnData

        parameters = num_order_difference_quotient(X, Y)
        result = calculate_data(value, parameters, X, Y)
        return result


