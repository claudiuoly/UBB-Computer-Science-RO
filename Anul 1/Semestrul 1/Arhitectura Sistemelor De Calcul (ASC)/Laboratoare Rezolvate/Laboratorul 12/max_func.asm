bits 32

global _asmMax
segment data public data use32
segment code public code use32
;Se citeste de la tastatura un sir de numere in baza 10 fara semn.
;Sa se determine valoarea maxima din sir si sa se afiseze in fisierul max.txt (fisierul va fi creat)
; valoarea maxima, in baza 16
; unsigned int asmMax(unsigned int arr[], int size)
_asmMax:
    ;Creare cadru de stiva
    push ebp
    mov ebp, esp

    ;Parametrii funcției
    mov esi, [ebp + 8]    ; esi = arr (adresa de inceput a sirului)
    mov ecx, [ebp + 12]   ; ecx = size (dimensiunea sirului)

    ; Initializez valoarea max
    mov eax, [esi]        ; eax = primul element al sirului
    add esi, 4            ; trecem la urmatorul element

.loop:
    cmp ecx, 1            ; Verific daca mai sunt elemente
    jle .done            ; Daca nu, gata

    mov ebx, [esi]        ; ebx = urmatorul element al sirului
    cmp eax, ebx         ; Compar eax cu ebx
    jge .skip            ; Daca eax >= ebx, trec la urmatorul

    mov eax, ebx         ; Actualizez maximul

.skip:
    add esi, 4            ; Trec la urmatorul
    dec ecx               ; --numarul de elemente
    jmp .loop            ; Continuam

.done:
    mov esp, ebp
    pop ebp
    ret