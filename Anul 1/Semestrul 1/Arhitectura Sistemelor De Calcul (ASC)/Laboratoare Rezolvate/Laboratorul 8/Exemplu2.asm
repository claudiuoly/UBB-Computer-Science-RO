bits 32
global start        
extern exit, printf, scanf, fopen, fprintf, fclose, fread
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll

segment data use32 class=data
    text times 100 db 0        ; buffer pentru text input
    buffer times 100 db 0      ; buffer pentru citire din fisier
    descriptor_fis dd -1       ; descriptor fisier
    
    nume_fisier db "text.txt", 0
    mod_scriere db "w", 0      ; mod scriere fisier
    mod_citire db "r", 0       ; mod citire fisier
    
    msg_input db "Introduceti un text: ", 0
    msg_output db "Textul citit din fisier este: %s", 0
    format_citire db "%s", 0
    msg_eroare db "Eroare la deschiderea fisierului!", 0

segment code use32 class=code
    start:
        ; Afisare mesaj pentru input
        push dword msg_input
        call [printf]
        add esp, 4
        
        ; Citire text de la tastatura
        push dword text
        push dword format_citire
        call [scanf]
        add esp, 4*2
        
        ; Deschidere fisier pentru scriere
        push dword mod_scriere
        push dword nume_fisier
        call [fopen]
        add esp, 4*2
        
        ; Verificare deschidere fisier
        cmp eax, 0
        je eroare
        
        mov [descriptor_fis], eax
        
        ; Scriere in fisier
        push dword text
        push dword format_citire
        push dword [descriptor_fis]
        call [fprintf]
        add esp, 4*3
        
        ; Inchidere fisier
        push dword [descriptor_fis]
        call [fclose]
        add esp, 4
        
        ; Deschidere fisier pentru citire
        push dword mod_citire
        push dword nume_fisier
        call [fopen]
        add esp, 4*2
        
        mov [descriptor_fis], eax
        
        ; Citire din fisier
        push dword [descriptor_fis]
        push dword 100        ; numar maxim de caractere
        push dword 1         ; dimensiunea unui element (1 byte)
        push dword buffer
        call [fread]
        add esp, 4*4
        
        ; Afisare text citit din fisier
        push dword buffer
        push dword msg_output
        call [printf]
        add esp, 4*2
        
        ; Inchidere fisier
        push dword [descriptor_fis]
        call [fclose]
        add esp, 4
        
        jmp final
        
    eroare:
        push dword msg_eroare
        call [printf]
        add esp, 4
        
    final:
        push dword 0
        call [exit]