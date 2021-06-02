# The Kaprekar's procedure
The Kaprekar's procedure is the routine that takes a non-negative integer of 4
digits maximum to obtain 2 numbers, the first number is obtained by arranging
the digits of the starting number in descending number, while the second number
is obtained by arranging the digits of the starting number in ascending order.
Then the second number is subtracted from the first, then the procedure is
repeated until it converges into the Kaprekar's constant (6174). If the process
is repeated on 6174, it will result in that same number. For instance, taking the number 1023:
1. Start with the number 1023
2. Get the first number: 1023 -> 3210
2. Get the second number: 1023 -> 0123 (123)
3. Subtract the second number from the first: 3210 - 123 = 3087
4. Repeat process on 3087
2. Get the first number: 3087 -> 8730
2. Get the second number: 3087 -> 0378 (378)
3. Subtract the second number from the first: 8730 - 378 = 8352
4. Repeat process on 8352
2. Get the first number: 8352 -> 8532
2. Get the second number: 8352 -> 2358
3. Subtract the second number from the first: 8532 - 2358 = 6174
4. Repeat process on 6174 (this will repeat forever)
2. Get the first number: 6174 -> 7641
2. Get the second number: 6174 -> 1467
3. Subtract the second number from the first: 7641 - 1467 = 6174
