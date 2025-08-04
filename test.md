To determine whether the given first-order differential equation is linear in the indicated dependent variable, we need to analyze the equation's form.

### 1. The given differential equation is:
\[
(y^2 + 1) \, dx + x \, dy = 0
\]

### 2. Rewriting it in standard form:
First, rewrite the equation to express it as:
\[
x \, \frac{dy}{dx} = -(y^2 + 1)
\]
or equivalently:
\[
\frac{dy}{dx} = -\frac{y^2 + 1}{x}
\]

#### **Check linearity in \( y \):**

To check if the equation is linear in \( y \), it needs to be of the form:
\[
\frac{dy}{dx} + P(x)y = Q(x)
\]
where \( P(x) \) and \( Q(x) \) are functions of \( x \) alone and no powers or products of \( y \) appear other than the first power of \( y \).

In this case, the equation is:
\[
\frac{dy}{dx} = -\frac{y^2 + 1}{x}
\]
Here, we have a \( y^2 \) term, which is non-linear. Thus, **the equation is not linear in \( y \)** because of the presence of the \( y^2 \) term.

#### **Check linearity in \( x \):**

Rewriting the original equation to check for linearity in \( x \), we rearrange it as:
\[
(y^2 + 1) \, dx = -x \, dy
\]
which simplifies to:
\[
\frac{dx}{dy} = -\frac{x}{y^2 + 1}
\]

To check if the equation is linear in \( x \), it needs to be of the form:
\[
\frac{dx}{dy} + P(y)x = Q(y)
\]
where \( P(y) \) and \( Q(y) \) are functions of \( y \) alone, and \( x \) appears only to the first power.

Here, the equation is:
\[
\frac{dx}{dy} = -\frac{x}{y^2 + 1}
\]
This is in the required form, with \( P(y) = \frac{1}{y^2 + 1} \) and \( Q(y) = 0 \).

Thus, **the equation is linear in \( x \)**.

### Conclusion:
- The equation is **non-linear in \( y \)**.
- The equation is **linear in \( x \)**.