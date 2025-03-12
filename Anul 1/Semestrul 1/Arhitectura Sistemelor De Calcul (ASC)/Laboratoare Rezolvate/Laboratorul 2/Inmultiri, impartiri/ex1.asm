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
    a db 5
    b db 10
    c db 3
    d dw 20
    ;a,b,c - byte, d - word
    ;((a+b-c)*2 + d-5)*d
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        mov al, [a]
        mov bl, [b]
        mov cl, [c]
        mov dx, [d]
        
        add al, bl
        sub al, cl
        add al, al
        
        add ax, dx
        
        sub ax, 5
        
        mul dx ; dx:ax = ax * dx
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
