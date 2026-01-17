# PYTHON MODULES 

# math module
import math

print("Absolute value of -7:", abs(-7))
print("Ceil of 4.8:", math.ceil(4.8))
print("Floor of 4.7:", math.floor(4.7))
print("Truncate 4.9:", math.trunc(4.9))
print("Factorial of 5:", math.factorial(5))
print("Power 2^5:", math.pow(2, 5))
print("Square root of 16:", math.sqrt(16))

print("Natural log of 10:", math.log(10))
print("Log base 10 of 100:", math.log10(100))
print("Log base 2 of 8:", math.log2(8))

print("Sin(90°):", math.sin(math.radians(90)))
print("Cos(0°):", math.cos(math.radians(0)))
print("Tan(45°):", math.tan(math.radians(45)))

print("Convert degrees(π/2) to radians:", math.degrees(math.pi/2))
print("Convert radians(180°) to degrees:", math.radians(180))

print("Value of π:", math.pi)
print("Value of e:", math.e)
print("Tau (τ):", math.tau)
print("Infinity:", math.inf)
print("NaN (Not a Number):", math.nan)

print("GCD of 20 and 8:", math.gcd(20, 8))
print("Remainder of 10/3:", math.remainder(10, 3))
print("Is 25 finite?:", math.isfinite(25))
print("Is infinity infinite?:", math.isinf(math.inf))
print("Is NaN a number?:", math.isnan(math.nan))
print("Hypotenuse of sides 3, 4:", math.hypot(3, 4))
print("Exponential (e^3):", math.exp(3))
print("Degrees of atan(1):", math.degrees(math.atan(1)))
print("Comb(5, 2):", math.comb(5, 2))
print("Perm(5, 2):", math.perm(5, 2))
print("Next after 5 towards 10:", math.nextafter(5, 10))

# random module examples
import random

print("Random integer (1-6):", random.randint(1, 6))
print("Random float (0-1):", random.random())

colors = ['red', 'green', 'blue', 'yellow']
print("Random color:", random.choice(colors))
random.shuffle(colors)
print("Shuffled colors:", colors)
print("Sample 2 unique numbers:", random.sample(range(10), 2))
print("Two random choices with replacement:", random.choices(colors, k=2))
print("Gaussian random (mean=0, std=1):", random.gauss(0, 1))
