bits 32
global start        

extern exit, printf   
import exit msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    ; Se da un sir de octeti S de lungime l. Sa se construiasca sirul 
    ;D de lungime l-1 astfel incat elementele din D sa reprezinte produsul 
    ;dintre fiecare 2 elemente consecutive S(i) si S(i+1) din S.
    s db 1, 2, 3, 4
    l equ ($-s)
    d times (l-1) db 0
segment code use32 class=code
    start:
        ; ...
        mov eax, 0
        mov ebx, 0
        mov esi, 0 
        mov ecx, 0
        
        mov esi, s
        
        mov edi, d
        
        mov ecx, l-1
        
        bulca:
            mov al, [esi]
            inc esi
            mov bl, [esi]
            add al, bl
            mov [edi], al
            inc edi
        loop bulca
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
