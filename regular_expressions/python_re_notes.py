#!/usr/bin/python3
"""
Pythons look behind mechanism is fundamentally different to the look ahead.
Look behinds are only able to match fixed-width patterns.
Fixed width patterns do not contain variable length matches such as quantifiers.
Alternations are allowed, but only if the alternatives have the same length.
"""
import re
print ("\nRegular Expression Quantifiers")
print(".", "\t\t\tAny character except new line")
print("*", "\t\t\t0 or more")
print("+", "\t\t\t1 or more")
print("?", "\t\t\t0 or 1")
print("{2}", "\t\t\tExactly 2")
print("{2,5}", "\t\t\tBetween 2 and 5")
print("{,5}", "\t\t\tUp to 5")

print ("\nRegular Expression Character Classes")
print(r"[ab-d]", "\t\t\tA single character of any 'a', 'b', 'c' or 'd'")
print(r"[^ab-d]", "\t\tA single character except any of 'a', 'b', 'c' or 'd'")
print(r"[\b]", "\t\t\tBackspace character")
print(r"\d", "\t\t\tA single digit")
print(r"\D", "\t\t\tA single non-digit")
print(r"\s", "\t\t\tA single space")
print(r"\S", "\t\t\tA single non-space")
print(r"\w", "\t\t\tA single word")
print(r"\W", "\t\t\tA single non-word")

print ("\nRegular Expression Groups")
print(r"(...)", "\t\t\tCapturing group")
print(r"(?P<Y>...)", "\t\tCapturing group named Y")
print(r"(?:...)", "\t\tNon-capturing group")
print(r"\Y", "\t\tMatch the Y'th captured group")
print(r"?P=Y", "\t\tMatch the named group Y")
print(r"(?#...)", "\t\tComment")

print("\nRegular Expression Assertions")
print(r"^", "\t\t\tStart of a string")
print(r"$", "\t\t\tEnd of a string")
print(r"\A", "\t\t\tStart of a string, ignores M flag")
print(r"\Z", "\t\t\tEnd of a string, ignores M flag")
print(r"\b", "\t\t\tWord boundary")
print(r"\B", "\t\t\tNon-word boundary")
print(r"?=...", "\t\t\tPositive look ahead")
print(r"?!...", "\t\t\tNegative look ahead")
print(__doc__)
print(r"?<=...", "\t\t\tPositive look behind")
print(r"?<!...", "\t\t\tNegative look behind")
print(r"?()|", "\t\t\tConditional")

print("\nRegular Expression Special Characters")
print(r"\n", "\t\t\tNew line")
print(r"\r", "\t\t\tCarraige Return")
print(r"\t", "\t\t\tTab")
print(r"\YYY", "\t\t\tOctal character YYY")
print(r"\xYY", "\t\t\tHexadecimal charcater YY")

print("\nRegular Expression Sepcial Group Characters")
print(r"\g<0>", "\t\t\tInsert entire match")
print(r"\g<Y>", "\t\t\tInsert match Y (name or number)")
print(r"\Y", "\t\t\tInsert group numbered Y")

