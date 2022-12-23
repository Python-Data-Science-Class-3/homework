
# Write a function that outputs the transcription of an input number with two digits.

# Example:
# 28---------------->Twenty Eight


n = int(input("Enter a nummer : "))
nums = ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen",
            "twenty", "twenty one", "twenty two",
            "twenty three", "twenty four",
            "twenty five", "twenty six", "twenty seven",
            "twenty eight", "twenty nine"]


for index_num, transcription  in enumerate(nums):       # to get a counter and the value from the iterable!
    if index_num == n :
       print()
       print(f' Number Entered was: {index_num:4} \n The transcription : {transcription}')
       print(f'\n {index_num:23} ---------------->   {transcription:10}''\n')
       print('\n')