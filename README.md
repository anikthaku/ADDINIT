## __ADD INITials To code (ADDINIT)__ 
---

Got an assignment to write Fibonacci numbers in C/C++. Easy right!

```C
int main() 
{
   int fib1 = 0, fib2 = 1, temp;
   printf("%d\n", fib1);
   printf("%d\n", fib2);   
   for(int i = 2; i <= 10; i++)
   {
       temp = fib2;
       fib2 = fib1 + fib2;
       fib1 = temp;
       printf("%d\n", fib2);
   }
   return 0;
}
```
However, you are scared that despite of solving the problem on your own, you might still get flagged for plagiarism with automatic plagiarism checker. One possible way could be adding initials to all the variable and function names in your code.

This is a simple tool based on python which adds your initials/id as suffix to each of the variable/function names in a given C/C++ code.

Lets take initial as "_sj" for "Sam Johnson" , then you can automatically generate the following code:
```C
int main()
{
   int fib1_sj = 0, fib2_sj = 1, temp_sj;
   printf("%d\n", fib1_sj);
   printf("%d\n", fib2_sj);
   for(int i_sj = 2; i_sj <= 10; i_sj++)
   {
       temp_sj = fib2_sj;
       fib2_sj = fib1_sj + fib2_sj;
       fib1_sj = temp_sj;
       printf("%d\n", fib2_sj);
   }
   return 0;
}
```

### **HOW TO USE**
---

- It only works for C and C++ codes.
- Change the contents of the variables, `codes_as_string` and `initials`, in the python code with your C/C++ code and initials/id, and then run the tool using `python addinit.py` on your bash/powershell.
- If you don't want to add your initials to a few variable/function names, then add those in the `keywords` list in the python code.

```Python
code_as_string = r"""
int main() 
{
   int fib1 = 0, fib2 = 1, temp;
   printf("%d\n", fib1);
   printf("%d\n", fib2);   
   for(int i = 2; i <= 10; i++)
   {
       temp = fib2;
       fib2 = fib1 + fib2;
       fib1 = temp;
       printf("%d\n", fib2);
   }
   return 0;
}
"""
initials = "_sj"   # Enter your initials/id here which you want to add

#......
#......
```

### **DON'TS**
---

- Don't paste the Preprocessor directive along with your C/C++ code.
- Add macro names in the `keyword` list.
- The tool adds initials in comment line too, so if needed, edit the comment line in the generated code.

### **UNDERLYING IDEA**
---

It uses regex to distinguish between the C/C++ keywords, variables and functions.
