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
    ;17) x-(a*a+b)/(a+c/a); a,c-byte; b-doubleword; x-qword
    ;Interpretare fara semn
    a DB 5
    b DD 10
    c DB 2
    x DQ 100

; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        ; c / a
        MOV AL, [c]
        MOV AH, 0
        DIV byte [a]

        ; a + c / a
        ADD AL, [a]

        ; a * a
        MOV BL, [a]
        MUL byte [a]

        ; a * a + b
        ADD EAX, [b]

        ; (a * a + b) / (a + c / a)
        DIV byte al

        ; x - (a * a + b) / (a + c / a)
        MOV EDX, [x+4]
        MOV EAX, [x]
        SUB EAX, AL

        ; Rezultatul fara semn este in EDX:EAX

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
