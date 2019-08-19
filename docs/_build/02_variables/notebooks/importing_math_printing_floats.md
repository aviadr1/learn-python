---
redirect_from:
  - "/02-variables/notebooks/importing-math-printing-floats"
interact_link: content/02_variables/notebooks/importing_math_printing_floats.ipynb
kernel_name: python3
has_widgets: false
title: 'Importing Math Printing Floats'
prev_page:
  url: /02_variables/notebooks/dictionary.html
  title: 'Dictionary'
next_page:
  url: /02_variables/notebooks/lists.html
  title: 'Lists'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-python/blob/master/content/02_variables/notebooks/importing_math_printing_floats.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import math

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
help(math)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(x, y, /)
        greatest common divisor of x and y
    
    hypot(x, y, /)
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
math.pi

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
3.141592653589793
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
math.sin

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
<function math.sin(x, /)>
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
math.cos(math.pi)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
-1.0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
math.tan(0)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0.0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
deg = 30
rad = deg * math.pi/180
print(math.sin(rad))


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-14-7079bc87c0ce> in <module>
          1 deg = 30
          2 rad = deg * math.pi/180
    ----> 3 print(decimal(math.sin(rad)))
    

    NameError: name 'decimal' is not defined


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import decimal

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
decimal.getcontext().prec =2

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(decimal.Decimal(math.sin(rad)))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0.499999999999999944488848768742172978818416595458984375
```
</div>
</div>
</div>

