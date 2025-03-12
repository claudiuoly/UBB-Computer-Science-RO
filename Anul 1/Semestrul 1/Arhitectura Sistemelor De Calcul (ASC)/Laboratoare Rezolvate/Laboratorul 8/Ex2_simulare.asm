bits 32
global start        

extern exit, scanf, printf, fprintf, fopen, fclose
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll
import fprintf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll

segment data use32 class=data

    ;
;    Sa se citeasca de la tastatura un numar n urmat de mai multe numere pozitive (ultimul numar citit va fi 0). Sa se scrie in fisierul output.txt numai numerele ;care contin exact N cifre impare

;    Input:
 ;   3
  ;  123 5124 1000 555 0

   ; Output in fisier:
    ;555
    n dd 0                          
    numar dd 0                     
    format_n db "%d", 0            
    format_numar db "%d", 0       
    nume_fisier db "output.txt", 0 
    mod_scriere db "w", 0         
    descriptor dd -1              
    format_scriere db "%d", 10, 0  
    temp dd 0                      

segment code use32 class=code
    start:
        ; Citește n
        push dword n
        push dword format_n
        call [scanf]
        add esp, 4*2
        
        ; Deschide fișierul pentru scriere
        push dword mod_scriere
        push dword nume_fisier
        call [fopen]
        add esp, 4*2
        
        mov [descriptor], eax      ; Salvează descriptorul fișierului
        
    citeste_numere:
        ; Citește următorul număr
        push dword numar
        push dword format_numar
        call [scanf]
        add esp, 4*2
        
        ; Verifică dacă numărul este 0 (condiție de oprire)
        mov eax, [numar]
        cmp eax, 0
        je final
        
        ; Numără cifrele impare
        mov ecx, 0                ; contor pentru cifre impare
        mov eax, [numar]          ; pune numărul în eax
        mov [temp], eax          ; salvează numărul original
        
    numara_cifre_impare:
        cmp eax, 0
        je verifica_n
        
        mov edx, 0               ; pregătește pentru div
        mov ebx, 10
        div ebx                  ; eax = eax / 10, edx = eax % 10
        
        ; Verifică dacă cifra (în edx) este impară
        test edx, 1
        jz cifra_para           ; sari dacă cifra e pară
        inc ecx                 ; incrementează contorul de cifre impare
        
    cifra_para:
        jmp numara_cifre_impare
        
    verifica_n:
        ; Verifică dacă numărul de cifre impare este egal cu N
        mov edx, [n]
        cmp ecx, edx
        jne citeste_numere      ; dacă nu sunt egale, citește următorul număr
        
        ; Scrie numărul în fișier
        push dword [temp]       ; numărul original
        push dword format_scriere
        push dword [descriptor]
        call [fprintf]
        add esp, 4*3
        
        jmp citeste_numere
        
    final:
        ; Închide fișierul
        push dword [descriptor]
        call [fclose]
        add esp, 4
        
        ; Termină programul
        push dword 0
        call [exit]