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
    a db 10
    b db 11
    c db 12
    d db 13
    ;c-(a+d)+(b+d)
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov al, [a]  ; al = a
        mov bl, [b]  ; bl = b
        mov cl, [c]  ; cl = c
        mov dl, [d]  ; dl = d
        
        ; Calculăm (a + d)
        add al, dl  ; al = a + d

        ; Calculăm (b + d)
        add bl, dl  ; bl = b + d

        ; Calculăm c - (a + d)
        sub cl, al  ; cl = c - (a + d)

        ; Calculăm c - (a + d) + (b + d)
        add cl, bl  ; cl = c - (a + d) + (b + d)
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
