bits 32
global start        

extern exit, scanf, printf, fopen, fclose, fprintf
import exit msvcrt.dll    
import scanf msvcrt.dll    
import printf msvcrt.dll    
import fopen msvcrt.dll     
import fclose msvcrt.dll    
import fprintf msvcrt.dll

segment data use32 class=data
; Se citesc cifre de la tastatura pana la intalnirea caracterului !. Sa se determine cel mai mare numar format prin folosirea fiecarei cifre impare citite o singura data. SCrieti numarul optiunut intr-un fisier numit result.txt
    caracter db 0              ; pentru citirea caracterelor
    format_char db "%c", 0     ; format pentru citire caracter
    cifre_impare times 10 db 0 ; array pentru a marca cifrele impare găsite (0-9)
    nume_fisier db "result.txt", 0
    mod_scriere db "w", 0
    descriptor dd -1
    format_scriere db "%d", 0
    counter dd 0               ; numără câte cifre impare unice avem

segment code use32 class=code
    start:
        ; Deschide fișierul pentru scriere
        push dword mod_scriere
        push dword nume_fisier
        call [fopen]
        add esp, 4*2
        mov [descriptor], eax
        
    citeste_caractere:
        ; Citește următorul caracter
        push dword caracter
        push dword format_char
        call [scanf]
        add esp, 4*2
        
        ; Verifică dacă e '!'
        mov al, [caracter]
        cmp al, '!'
        je construieste_numar
        
        ; Verifică dacă e cifră (între '0' și '9')
        cmp al, '0'
        jb citeste_caractere
        cmp al, '9'
        ja citeste_caractere
        
        ; Convertește din ASCII în valoare numerică
        sub al, '0'
        
        ; Verifică dacă e impară
        test al, 1
        jz citeste_caractere    ; dacă e pară, ignoră
        
        mov ebx, 0
        ; Marchează cifra în array (dacă nu e deja marcată)
        mov ebx, eax          ; pune cifra în ebx
        cmp byte [cifre_impare + ebx], 0
        jne citeste_caractere  ; dacă cifra există deja, citește următorul caracter
        mov byte [cifre_impare + ebx], 1
        inc dword [counter]    ; incrementează contorul de cifre unice
        
        jmp citeste_caractere
        
    construieste_numar:
        ; Verifică dacă avem cifre impare
        cmp dword [counter], 0
        je final               ; dacă nu avem cifre, termină programul
        
        ; Parcurge array-ul de la 9 la 0 și scrie cifrele în fișier
        mov ecx, 9            ; începe de la cea mai mare cifră
        
    scrie_cifre:
        cmp byte [cifre_impare + ecx], 0
        je next_digit
        
        ; Scrie cifra în fișier
        push ecx              ; salvează ecx
        push ecx             
        push dword format_scriere
        push dword [descriptor]
        call [fprintf]
        add esp, 4*3
        pop ecx               ; restaurează ecx
        
    next_digit:
        dec ecx
        cmp ecx, -1
        jne scrie_cifre
        
    final:
        ; Închide fișierul
        push dword [descriptor]
        call [fclose]
        add esp, 4
        
        ; Termină programul
        push dword 0
        call [exit]