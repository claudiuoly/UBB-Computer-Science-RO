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
    
    ;17) Se dau cuvantul A si octetul B. Sa se obtina dublucuvatul C:
        ;bitii 0-3 ai lui C au valoarea 1
        ;bitii 4-7 ai lui C coincid cu bitii 0-3 ai lui A
        ;bitii 8-13 ai lui C au valoarea 0
        ;bitii 14-23 ai lui C coincid cu bitii 4-13 ai lui A
        ;bitii 24-29 ai lui C coincid cu bitii 2-7 ai lui B
        ;bitii 30-31 au valoarea 1
        
   ; 1000 0101 0101 0010 0011 0000 0100 1111 = 8 5 5 2 3 0 4 F
    
   ; A = 0001 0010 0011 0100
   ; B = 0000 0000 0101 0110

    A DW 1234h      ; Cuvantul A (exemplu)
    B DB 56h        ; Octetul B (exemplu)
    C DD 0          ; Dublucuvântul C (initializat cu 0)

; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        ; Initializez C cu valoarea 1 pe bitii 0-3
        MOV EAX, 0Fh
        MOV DWORD [C], EAX

        ; Extrag bitii 0-3 din A si ii pun in C (bitii 4-7)
        MOV AX, [A]
        AND AX, 0Fh         ; Masca pentru a pastra doar bitii 0-3
        SHL EAX, 4          ; Shift la stanga cu 4 pozitii
        OR DWORD [C], EAX  ; Combin cu valoarea existenta in C

        ; Extrag bitii 4-13 din A si ii pun in C (bitii 14-23)
        MOV AX, [A]
        SHR AX, 4          ; Shift la dreapta cu 4 pozitii
        AND AX, 3FFh       ; Masca pentru a pastra doar bitii 4-13
        SHL EAX, 14         ; Shift la stanga cu 14 poziții
        OR DWORD [C], EAX  ; Combin cu valoarea existenta in C

        ; Extrag bitii 2-7 din B si ii pun in C (bitii 24-29)
        MOV AL, [B]
        SHR AL, 2          ; Shift la dreapta cu 2 pozitii
        AND AL, 3Fh        ; Masca pentru a pastra doar bitii 2-7
        SHL EAX, 24         ; Shift la stanga cu 24 pozitii
        OR DWORD [C], EAX  ; Combin cu valoarea existenta in C

        ; Setam bitii 30-31 la 1
        OR DWORD [C], 0C0000000h 
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
