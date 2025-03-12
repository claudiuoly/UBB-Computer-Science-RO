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
    ;(e+g-h)/3+b*c
    a db 1
    b db 1
    c db 2
    d db 1
    
    e dw 1
    f dw 1
    g dw 3
    h dw 1
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        
        mov bx, [e]
        mov cx, [g]
        mov dx, [h]
        
        add bx, cx
        sub bx, dx
        
        mov edx, 0
        mov ax, bx
        mov bx, 3
        div bx
        
        mov bx, ax
        
        mov eax, 0
        mov al, [b]
        mov cl, [c]
        mul cx
        
        add bx, ax
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
