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
    ; 17) (c+c-a)-(d+d)-b === (17128 + 17128 - 31) - (12421 + 12421) - 1241 = 
    ;a - byte, b - word, c - double word, d - qword - Interpretare fara semn
    
    a DB 31
    b DW 1241
    c DD 17128
    d DQ 12421

; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        ; (c + c - a)
        MOV EAX, [c] ; EAX = c
        ADD EAX, EAX ; EAX = c + c
        SUB AL, [a] ; EAX = c + c - a

        ; (d + d)
        MOV EBX, [d] ; EBX = inferior de d
        ADD EBX, [d] ; EBX = EBX + [d]
        ADC ECX, [d+4] ; ECX = ECX + [d] + carry
        MOV ECX, [d+4] ; ECX = superior de d

        ; (c + c - a) - (d + d)
        SUB EAX, EBX ; Scade partea inferioara
        SUB EDX, ECX ; Scade partea superioara, cu imprumut 

        ; - b
        MOV EBX, 0
        MOV BX, [b] ; BX = b
        SUB EAX, EBX ; Scade partea inferioara
        SUB EDX, 0 ; Scade partea superioara (cu imprumut, daca exista)

        ; Rezultatul final este acum în EDX:EAX
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
