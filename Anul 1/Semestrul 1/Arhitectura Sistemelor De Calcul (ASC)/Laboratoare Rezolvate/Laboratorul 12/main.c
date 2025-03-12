#include <stdio.h>
unsigned int asmMax(unsigned int arr[], int size);

int main() {
    unsigned int arr[100];
    int n, i;
    unsigned int max_val;

    FILE *fout = fopen("max.txt", "w"); // Deschid fisierul

    printf("Introduceti numarul de elemente din sir: ");
    scanf("%d", &n);

    printf("Introduceti sirul de numere (separate prin spatiu):\n");
    for (i = 0; i < n; i++) {
        scanf("%u", &arr[i]);
    }

    max_val = asmMax(arr, n); // Apelez functia asmMax

    fprintf(fout, "Valoarea maxima in baza 16: %X\n", max_val); // Scriem in fisier
    printf("Valoarea maxima a fost salvata in fisierul max.txt.\n");

    fclose(fout); // Inchid fisierul
    return 0;
}