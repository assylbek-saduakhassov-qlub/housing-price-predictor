def gradient_descent(alpha, num_iters, data):
    x1_list, x2_list, y_list = data
    m = len(y_list)
    w0, w1, w2 = 0.0, 0.0, 0.0  # Initialize weights
    J_history = []

    for _ in range(num_iters):
        # Compute the hypothesis for all training examples
        y_pred = [w0 + w1 * x1 + w2 * x2 for x1, x2 in zip(x1_list, x2_list)]
        
        # Compute the errors
        errors = [y_hat - y for y_hat, y in zip(y_pred, y_list)]
        
        # Compute the cost function J(w)
        J = sum(e ** 2 for e in errors) / (2 * m)
        J_history.append(J)
        
        # Compute gradients (partial derivatives)
        w0_grad = sum(errors) / m
        w1_grad = sum(e * x1 for e, x1 in zip(errors, x1_list)) / m
        w2_grad = sum(e * x2 for e, x2 in zip(errors, x2_list)) / m
        
        # Update the weights
        w0 -= alpha * w0_grad
        w1 -= alpha * w1_grad
        w2 -= alpha * w2_grad

    return w0, w1, w2, J_history
