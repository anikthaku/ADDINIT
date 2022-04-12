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

keywords = ["alignas",
"double",
"reinterpret_cast",
"alignof",
"dynamic_cast",
"requires",
"and",
"else",
"return",
"and_eq",
"enum",
"short",
"asm",
"explicit",
"signed",
"atomic_cancel TM TS",
"export",
"sizeof",
"atomic_commit TM TS",
"extern",
"static",
"atomic_noexcept TM TS",
"false",
"static_assert ",
"auto",
"float",
"static_cast",
"bitand",
"for",
"struct",
"bitor",
"friend",
"switch",
"bool",
"goto",
"synchronized TM TS",
"break",
"if",
"template",
"case",
"import modules TS",
"this",
"catch",
"inline",
"thread_local",
"char",
"int",
"throw",
"char16_t",
"long",
"true",
"char32_t",
"module modules TS",
"try",
"class",
"mutable",
"typedef",
"compl",
"namespace",
"typeid",
"concept",
"new",
"typename",
"const",
"noexcept",
"union",
"constexpr",
"not",
"unsigned",
"const_cast",
"not_eq",
"using",
"continue",
"nullptr ",
"virtual",
"co_await coroutines TS",
"operator",
"void",
"co_return coroutines TS",
"or",
"volatile",
"co_yield coroutines TS",
"or_eq",
"wchar_t",
"decltype",
"private",
"while",
"default",
"protected",
"xor",
"delete",
"public",
"xor_eq",
"do",
"main",
"scanf",
"printf",
"cin",
"cout",
"#include",
"std",
"free",
"malloc",
"calloc",
"realloc",
"MIN",
"MAX",
"NULL",
"strcpy",
"getchar",
"endl",
"exit",
"gets",
"puts"
]

import re

id_reg = r'[A-Za-z_][A-Za-z0-9_]*'
all_ids = re.finditer(id_reg, code_as_string)
new_code = ""
idx = 0

def skip_commas(idx):
    global new_code, code_as_string
    if code_as_string[idx] == "'":
        symb = "'"
    elif code_as_string[idx] == '"':
        symb = '"'
    else:
        return idx
    s = [code_as_string[idx]]
    new_code += code_as_string[idx]
    idx += 1
    while idx < len(code_as_string) and code_as_string[idx] != symb:
        new_code += code_as_string[idx]
        s.append(code_as_string[idx])
        idx += 1
    new_code += code_as_string[idx]
    idx += 1
    return idx

for id in all_ids:
    start, end = id.span()
    starting_detected = False
    ending_detected = False
    while idx < start:
        idx = skip_commas(idx)
        if idx >= start:
            break
        new_code += code_as_string[idx]
        idx += 1
    if idx > start:
        continue
    orig = code_as_string[start:end]
    if orig not in keywords and abs(ord(orig[0]) - ord('0')) > 10:
        new_code += code_as_string[start:end] + initials
    else:
        while idx < end:
            new_code += code_as_string[idx]
            idx += 1
    idx = end
if idx < len(code_as_string):
    while idx < len(code_as_string):
        new_code += code_as_string[idx]
        idx += 1
print(new_code)