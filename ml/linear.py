import numpy as np


class Linear:
    def __init__(self):
        self.w = None

    def __call__(self, X):
        X_bias = np.c_[np.ones(X.shape[0]), X]
        return self.w@X_bias.T
    
    def fit(self, X, y, method = 'normal'):
        n = X.shape[0]
        X_bias = np.c_[np.ones(n), X]
        if method == 'normal':
            # self.w = np.linalg.inv(X_bias.T @ X_bias) @ X_bias @ y
            self.w = np.linalg.pinv(X_bias) @ y
        elif method == 'gd':
            self.lr, self.max_iter, self.tol = 3e-4, 100000, 1e-6
            self.w = np.random.rand(X_bias.shape[1])
            for _ in range(self.max_iter):
                # chain rule:
                # let e = (X_bias*w - y)
                # C = (1/n) * sum(e^2)
                # dL/df = 2e, and de/dw = X_bias (by linearity).
                # => dC/dw = (1/m) * X_bias^T * f.
                grad = 2/n * X_bias.T @ (X_bias @ self.w - y)
                new_weights = self.w - self.lr * grad
                if np.linalg.norm(new_weights - self.w) < self.tol:
                    self.w = new_weights
                    print(f"Converged after {_+1} iterations")
                    break
                self.w = new_weights



        else:
            raise ValueError('method should be normal or gd')



    def __repr__(self):
        return f'Linear(w={self.w}, b={self.b})'
    

X = np.arange(1, 13).reshape(6, 2)
y = np.arange(6)

print(X)
model = Linear()
model.fit(X, y)
print(model(X))
model.fit(X, y, "gd")
print(model(X))