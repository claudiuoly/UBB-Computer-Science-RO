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
    ;Interpretare cu semn
    a DB 5
    b DD 10
    c DB 2
    x DQ 100

; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        ; c / a 
        MOV AL, [c] ; AL = c
        CBW ; Extind c cu semn la 16 biti (AX = c)
        MOV bl, [a] ; bl = a
        CBW ; Extinde a cu semn la 16 biti (bx = a) 
        CWD ; Extinde ax la 32 biti (dx:ax = c)
        IDIV bx ; ax = c / a, dx = c % a

        ; a + c / a
        ADD ax, bx ; ax = a + c / a

        ; a * a
        IMUL bx, bx ; bx = a * a

        ; a * a + b
        CWDE ; Extinde a * a cu semn la 32 biți (eax = a * a)
        ADD eax, [b] ; eax = a * a + b

        ; (a * a + b) / (a + c / a)
        CWD ; Extinde eax la 32 biți (dx:eax = a * a + b)
        IDIV word AX ; ax = (a * a + b) / (a + c / a), dx = restul

        ; x - (a * a + b) / (a + c / a)
        MOV EDX, [x+4] ; EDX = partea superioara a lui x
        MOV EAX, [x] ; EAX = partea inferioara a lui x
        SUB EAX, AX ; EAX = x - rezultat

        ; Rezultatul cu semn este in EDX:EAX

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
