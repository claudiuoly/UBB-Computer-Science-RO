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
    ;Se dau 2 siruri de octeti S1 si S2 de aceeasi lungime. 
    ;Sa se construiasca sirul D astfel incat fiecare element din D sa reprezinte maximul dintre elementele de pe pozitiile 
    ;corespunzatoare din S1 si S2.
            ; Exemplu:
            ;  S1: 1, 3, 6, 2, 3, 7
            ;  S2: 6, 3, 8, 1, 2, 5
            ;  D: 6, 3, 8, 2, 3, 7
           
    S1 db 1, 3, 6, 2, 3, 7
    lenS1 equ $-S1
    S2 db 6, 3, 8, 1, 2, 5
    D  times lenS1 db 0

; our code starts here
segment code use32 class=code
    start:
        ;ESI = 0
        MOV ESI, 0
        
    calc_max:
        ; Verific daca am ajuns la sfarsitul lui S1
        CMP ESI, lenS1
        JAE end ;Daca indexul depaseste lungimea, iesim din bucla (JAE este >= pentru valorile fara semn JGE --> pentru cele cu semn)

        ; AL = S1
        MOV AL, [S1 + ESI]
        
        ; BL = S2
        MOV BL, [S2 + ESI]
        
        ; Comparam AL cu BL
        CMP AL, BL
        JGE pune_in_D ;Daca AL >= BL, punem AL in D
        
        ; Daca BL > AL, copiem BL în AL pentru a retine valoarea mai mare
        MOV AL, BL
        
    pune_in_D:
        ; Punem maximul in D
        MOV [D + ESI], AL
        
        ; ESI ++
        INC ESI
        JMP calc_max

    end:
        push dword 0            ; parametru pentru exit (0)
        call [exit]             ; apelăm exit
