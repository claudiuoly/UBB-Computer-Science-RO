bits 32
global start        
extern exit
import exit msvcrt.dll

segment data use32 class=data
    a db 5
    b db 5
    c db 8
    d db 4
    ;(a+d+d)-c+(b+b)
    
segment code use32 class=code
    start:
        ; ...
        mov ecx, 0
        mov eax, 0
        mov ebx, 0
        mov al, [a]  ; al = a
        mov bl, [b]  ; bl = b
        mov cl, [c]  ; cl = c
        mov dl, [d]  ; dl = d
        
        add al, dl
        add al, dl
        sub al, cl
        add al, bl
        add al, bl
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
