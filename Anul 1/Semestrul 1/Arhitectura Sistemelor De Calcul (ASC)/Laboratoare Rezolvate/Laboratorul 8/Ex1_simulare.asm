bits 32
global start        

extern exit, scanf, printf, fopen, fclose, fread
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll

segment data use32 class=data
    msg_input db "Introduceti numele fisierului din care sa se citeasca: ", 0
    nume_fisier times 51 db 0  ; 50 caractere + null terminator
    format db "%s", 0
    mod_citire db "r", 0
    descriptor dd -1
    format_afisare db "Numarul de consoane (hex) este: %x", 0
    
    len equ 100
    text times (len+1) db 0
    
segment code use32 class=code
    start:
        ; Afisare mesaj pentru input
        push dword msg_input
        call [printf]
        add esp, 4
        
        ; Introducere nume fisier
        push dword nume_fisier
        push dword format
        call [scanf]
        add esp, 4*2
        
        ; Deschidere fisier pentru citire
        push dword mod_citire
        push dword nume_fisier
        call [fopen]
        add esp, 4*2
        
        ; Verifică dacă fișierul s-a deschis cu succes
        mov [descriptor], eax
        cmp eax, 0
        je final
        
        ; Citește conținutul fișierului
        push dword [descriptor]
        push dword len
        push dword 1
        push dword text
        call [fread]
        add esp, 4*4
        
        ; Procesare text
        mov esi, text
        mov ecx, 0  ; contor pentru consoane
        
    loop_start:
        mov al, byte [esi]  ; Citește caracterul curent
        cmp al, 0              ; Verifică sfârșitul șirului
        je afisare
        
        ; Convertește la uppercase pentru simplificare
        cmp al, 'a'
        jb skip_to_check
        cmp al, 'z'
        ja skip_to_check
        sub al, 32          ; convertește la uppercase
        
    skip_to_check:
        ; Verifică dacă e literă
        cmp al, 'A'
        jb not_consoana
        cmp al, 'Z'
        ja not_consoana
        
        ; Verifică dacă NU e vocală
        cmp al, 'A'
        je not_consoana
        cmp al, 'E'
        je not_consoana
        cmp al, 'I'
        je not_consoana
        cmp al, 'O'
        je not_consoana
        cmp al, 'U'
        je not_consoana
        
        ; Dacă am ajuns aici, e consoană
        inc ecx
        
    not_consoana:
        inc esi
        jmp loop_start
        
    afisare:
        push ecx
        push dword format_afisare
        call [printf]
        add esp, 4*2
        
        ; Închide fișierul
        push dword [descriptor]
        call [fclose]
        add esp, 4
        
    final:
        push dword 0
        call [exit]