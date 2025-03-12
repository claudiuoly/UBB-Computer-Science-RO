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
    
    s1 db 1, 3, 5, 7
    l1 equ ($-s1)
    
    s2 db 2, 6, 9, 4
    l2 equ ($-s1)
    
    d times (l1+l2) db 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
    
        mov eax, 0
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
       
        mov esi, s1
        mov edx, s2
        mov edi, d
        
        mov ecx, l1
        
        loopy:
            mov al, [esi]
            mov [edi], al
            inc edi
            mov al, [edx]
            mov [edi], al
            inc esi
            inc edx
            inc edi
        loop loopy
        
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
