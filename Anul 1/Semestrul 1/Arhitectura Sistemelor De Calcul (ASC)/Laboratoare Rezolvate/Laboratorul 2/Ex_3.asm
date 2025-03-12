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
    
    ;17) a+a-b-c-(d+d)
    
    a DW 10        ; exemplu de valoare pentru a (word)
    b DW 5         ; exemplu de valoare pentru b (word)
    c DW 3         ; exemplu de valoare pentru c (word)
    d DW 7         ; exemplu de valoare pentru d (word)

; our code starts here
segment code use32 class=code
    start:
        ; ...
    
        MOV AX, [a]         ; AX = a
    
        ADD AX, [a]         ; AX = a + a
        
        SUB AX, [b]         ; AX = a + a - b
        
        SUB AX, [c]         ; AX = a + a - b - c
        
        MOV BX, [d]         ; BX = d
        
        ADD BX, [d]         ; BX = d + d
        
        SUB AX, BX          ; AX = a + a - b - c - (d + d)    
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
