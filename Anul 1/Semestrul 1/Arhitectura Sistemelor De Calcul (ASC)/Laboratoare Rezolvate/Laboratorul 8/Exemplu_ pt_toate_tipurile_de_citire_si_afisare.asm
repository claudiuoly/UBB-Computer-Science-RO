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
    num1 dd 0       ; primul numar
    num2 dd 0       ; al doilea numar
    suma dd 0       ; suma numerelor
    descriptor_fis dd -1
    
    nume_fisier db "rezultate.txt", 0
    mod_scriere db "w", 0
    
    msg_num1 db "Introduceti primul numar: ", 0
    msg_num2 db "Introduceti al doilea numar: ", 0
    msg_suma db "Suma numerelor este: %d", 10, 0
    msg_salvare db "Rezultatul a fost salvat in fisierul rezultate.txt", 10, 0
    format_nr db "%d", 0
    format_fisier db "Primul numar: %d", 10, "Al doilea numar: %d", 10, "Suma lor este: %d", 10, 0

segment code use32 class=code
    start:
        ; Citim primul numar
        push dword msg_num1
        call [printf]
        add esp, 4
        
        push dword num1
        push dword format_nr
        call [scanf]
        add esp, 4*2
        
        ; Citim al doilea numar
        push dword msg_num2
        call [printf]
        add esp, 4
        
        push dword num2
        push dword format_nr
        call [scanf]
        add esp, 4*2
        
        ; Calculam suma
        mov eax, [num1]
        add eax, [num2]
        mov [suma], eax
        
        ; Afisam suma pe ecran
        push dword [suma]
        push dword msg_suma
        call [printf]
        add esp, 4*2
        
        ; Deschidem fisierul pentru a salva rezultatele
        push dword mod_scriere
        push dword nume_fisier
        call [fopen]
        add esp, 4*2
        
        mov [descriptor_fis], eax
        
        ; Scriem rezultatele in fisier
        push dword [suma]
        push dword [num2]
        push dword [num1]
        push dword format_fisier
        push dword [descriptor_fis]
        call [fprintf]
        add esp, 4*5
        
        ; Inchidem fisierul
        push dword [descriptor_fis]
        call [fclose]
        add esp, 4
        
        ; Afisam mesaj de confirmare
        push dword msg_salvare
        call [printf]
        add esp, 4
        
        push dword 0
        call [exit]