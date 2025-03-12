bits 32
global start    

extern exit, fopen, fprintf, fclose, fread, fscanf, printf         
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll
import fscanf msvcrt.dll
import printf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; Se dau in segmentul de date un nume de fisier si un text (poate contine orice tip de caracter). Sa se calculeze suma cifrelor din text. Sa se creeze un fisier cu numele dat si sa se scrie suma obtinuta in fisier.
    ;rez = 19
    
     nume_fisier_afisare db "rezultat_19.txt", 0
     nume_fisier_citire db "citire_19.txt", 0
     mod_citire db "r", 0
     mod_scriere db "w", 0
     descriptor_scriere dd -1
     descriptor dd -1
     format db "%d", 0
     nr dd 0
     len equ 100
     text times (len+1) db 0
     
     rez dd 0
     
; our code starts here
segment code use32 class=code
    start:
    
        ; Deschidere fisier pentru citire
        push dword mod_citire
        push dword nume_fisier_citire
        call [fopen]
        add esp, 4*2
        
        mov [descriptor], eax 
        
        cmp eax, 0
        je final
        
        push dword [descriptor]
        push dword len
        push dword 1
        push dword text
        call [fread]
        add esp, 4*4
        
        ; Deschidere fisier pentru scriere
        push dword mod_scriere
        push dword nume_fisier_afisare
        call [fopen]
        add esp, 4*2
        
        mov [descriptor_scriere], eax
        cmp eax, 0
        je final
        
        mov esi, text
        mov eax, 0
        mov ebx, 0
        
        loop_start:
            mov bl, [esi]  ; Citește caracterul curent în BL
            cmp bl, 0      ; Verifică dacă am ajuns la sfârșitul șirului
            je loop_end

            cmp bl, 48  ; Verifică dacă este mai mic decât '0'
            jb not_digit
            cmp bl, 57  ; Verifică dacă este mai mare decât '9'
            ja not_digit

        ; Este o cifră:
        sub bl, '0'  ; Convertește la valoare numerică
        add al, bl

    not_digit:
        inc esi       ; Incrementează indexul
        jmp loop_start

    loop_end:
        mov [rez], eax
        ;Scriere in fisier
        push dword [rez]
        push dword format
        push dword [descriptor_scriere]
        call [fprintf]
        add esp, 4*3
        
        ;Inchidere fisier de citire
        push dword [descriptor]
        call [fclose]
        add esp, 4
        ;Inchidere fisier de scriere
        push dword [descriptor_scriere]
        call [fclose]
        add esp, 4
        
        
        
        final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
