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
    s1 db 1, 2, 3, 4
    l1 equ ($-s1)
    s2 db 5, 6, 7, 8
    l2 equ ($-s2)
    d times l1 db 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        
        mov esi, s1
        mov edi, s2
        mov eax, d
        
        mov ecx, l1
        
        loopy:
            mov ebx, ecx
            and ebx, 000000000000000000000000000000001b
            
            cmp ebx, 1
            je impar
            
            mov dl, [esi]
            add dl, [edi]
            mov [eax], dl
            inc esi
            inc edi
            inc eax
            loop loopy
            
            impar:
                mov dl, [esi]
                sub dl, [edi]
                mov [eax], dl
                inc esi
                inc edi
                inc eax
                loop loopy
        
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
