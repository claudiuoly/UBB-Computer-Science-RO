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
    l1 equ ($-s1) ; daca era s1 dw => ($-s1) / 2 si tot asa, dd => /4, dq => 8
    s2 db 5, 6, 7
    l2 equ ($-s2)
    d times (l1+l2) db 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov eax, 0 
        mov ebx, 0
        mov ecx, 0
        mov edx, 0
        mov esi, 0
        mov edi, 0
        
        ;Punem in ecx lungimea sirului d
        mov ecx, l1
        mov ebx, l2
        add ecx, ebx
        
        mov edx, s2
        mov esi, s1
        mov edi, d
        

        loopy:
            cmp ecx, l2
            jbe sirul2
            mov al, [esi]
            mov [edi], al
            inc esi ; daca era dw  increment by 2 bytes (1 word) daca era dd inc by 4 daca era dq inc by 8
            inc edi ; daca era dw icrement by 2 bytes (1 word)
            loop loopy
            
            sirul2:
            mov al, [edx] ; si mai era si aici de modifacat, +4 daca era dq
            mov [edi], al
            inc edx ; daca era dw  increment by 2 bytes (1 word)
            inc edi  ; daca era dw icrement by 2 bytes (1 word)
            loop loopy
            
            
    
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
