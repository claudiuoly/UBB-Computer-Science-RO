bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...

    ;17) a+13-c+d-7+b
    a DB 10        ; exemplu de valoare pentru a
    b DB 5         ; exemplu de valoare pentru b
    c DB 3         ; exemplu de valoare pentru c
    d DB 7         ; exemplu de valoare pentru d
    
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        MOV AL, [a]       ; AL = a
        
        ADD AL, 13        ; AL = a + 13
        
        SUB AL, [c]       ; AL = a + 13 - c
        
        ADD AL, [d]       ; AL = a + 13 - c + d
        
        SUB AL, 7         ; AL = a + 13 - c + d - 7
        
        ADD AL, [b]       ; AL = a + 13 - c + d - 7 + b  
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
