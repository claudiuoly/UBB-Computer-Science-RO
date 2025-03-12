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
    
    ;17) 300-[5*(d-2*a)-1]
    a db 10 ; exemplu de valoare pentru a (byte)
    d dw 30 ; exemplu de valoare pentru d (word)
    five dw 5 ; atribui lui five 5 (word)

; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        MOV AX, 0
    
        MOV AL, [a] ; AL = a
        MOV BX, [d] ; BX = b
        
        ADD AX, AX ;AX = 2*a      

        SUB BX, AX ; BX = (d - 2*a)  

        MOV AX, BX ; AX = BX
        MUL WORD [five] ; DX:AX = 5*(d-2*a)
        MOV BX, AX ; BX = AX

        SUB BX, 1 ; BX = 5*(d-2*a)-1

        MOV AX, 300 ; AX = 300
        SUB AX, BX ; AX = 300-[5*(d-2*a)-1]
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
