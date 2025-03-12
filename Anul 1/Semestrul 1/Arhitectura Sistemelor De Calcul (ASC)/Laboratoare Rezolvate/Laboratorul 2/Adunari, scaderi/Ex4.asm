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
    a db 12
    b db 10
    c db 12
    d db 2
    ;(a-b)+(c-b-d)+d
; our code starts here
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
        
      
        sub al, bl
        sub cl, bl
        sub cl, dl
        add al, cl
        add al, dl
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
