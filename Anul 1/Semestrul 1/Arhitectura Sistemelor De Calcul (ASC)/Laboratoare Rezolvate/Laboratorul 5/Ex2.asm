bits 32 
global start         

extern exit               
import exit msvcrt.dll    

segment data use32 class=data 
    s db '+', '4', '2', 'a', '@', '3', '$', '*'
    l equ ($-s) 
    d times l db 0 

segment code use32 class=code 
    start:
        mov eax, 0 
        mov ebx, 0 
        mov esi, 0  
        mov ecx, l ; Inițializăm ecx cu lungimea șirului

        mov esi, s 
        mov edi, d

        bucla: 
            mov al, [esi] 
            
            cmp al, 32 
            jb move
            
            cmp al, 47
            ja move
            
            mov [edi], al ; Mutăm caracterul special în șirul d
            inc edi 
            
        move: 
            inc esi       ; Incrementăm esi indiferent dacă am mutat sau nu un caracter
            loop bucla   ; Decrementăm ecx și sărim la bucla

        final: 
        push    dword 0 
        call    [exit]