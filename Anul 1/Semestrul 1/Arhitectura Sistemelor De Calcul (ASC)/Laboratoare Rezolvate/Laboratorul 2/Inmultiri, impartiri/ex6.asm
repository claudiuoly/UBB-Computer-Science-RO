bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; a,b,c,d-byte, e,f,g,h-word
    ;(e+g-2*b)/c
    a db 1
    b db 6
    c db 3
    d db 2
    e dw 12
    f dw 13
    g dw 15
    h dw 14
; our codestarts here
segment code use32 class=code
    start:
        ; ...
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        mov ax, [e]
        mov bx, [g]
        
        add ax, bx
        
        mov bx, 0
        mov bl, [b]
        add bl, bl
        
        sub ax, bx
        
        mov cl, [c]
        
        div cx
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
