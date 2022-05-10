# Kaprekar-s-constant


Playing around with Kaprekar's constant. I found the idea and had to try it out in practice for myself.

The idea of Kaprekar's constant is to take any 4 digit number and do one simple step at most 7 times. 
The steps are: 
    1) Organize the digits from highest to lowest --> Results in new 4 digit number
    2) Organize the digits from lowest to highest --> Results in new 4 digit number
    3) Subtract second from the first. Highest - lowest ==> new number
    4) Repeat the steps for the new number. 
  Repeat all of that at most 7 times and you will end up with Kaprekar's constant of 6174 each time. 
  
  
For some numbers it gets to 6174 quicker. But it will stay there because: 
           6174 
           7641  Highest to lowest 
           1467   Lowest to highest
           New number = 7641 - 1467 = 6174
           
           
 However. The 4 digit number cannot have four numbers to be exactly the same. There has to be atleast two different digits and leading 0 are allowed. 
 So if number gets below 1000, we would have a 0 in front such as 0999 or 0123. Multiple leading zeros are also allowed. 
 
 I will play around more with this constant by creating random testing and trying out different edge cases. This is fascinating. 
