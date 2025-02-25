#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE 1024

void vigenere_cipher(char *text, const char *key, int decrypt) {
    int text_len = strlen(text), key_len = strlen(key);
    for (int i = 0, j = 0; i < text_len; i++) {
        if (text[i] >= 'A' && text[i] <= 'Z') { 
            text[i] = 'A' + (text[i] - 'A' + (decrypt ? -1 : 1) * (key[j % key_len] - 'A')) % 26;
            if (text[i] < 'A') text[i] += 26;
            j++;
        } else if (text[i] >= 'a' && text[i] <= 'z') {
            text[i] = 'a' + (text[i] - 'a' + (decrypt ? -1 : 1) * (key[j % key_len] - 'a')) % 26;
            if (text[i] < 'a') text[i] += 26;
            j++;
        }
    }
}

void encrypt() {
    FILE *file = fopen("tmp.txt", "r");
    if (!file) {
        perror("Error opening file");
        return;
    }
    
    char key[MAX_LINE], text[MAX_LINE];
    if (!fgets(key, MAX_LINE, file) || !fgets(text, MAX_LINE, file)) {
        fclose(file);
        perror("Error reading file");
        return;
    }
    key[strcspn(key, "\n")] = 0;
    text[strcspn(text, "\n")] = 0;
    fclose(file);
    
    vigenere_cipher(text, key, 0);
    
    file = fopen("tmp.txt", "w");
    if (!file) {
        perror("Error writing to file");
        return;
    }
    fprintf(file, "%s\n%s\n", key, text);
    fclose(file);
}

void decrypt() {
    FILE *file = fopen("tmp.txt", "r");
    if (!file) {
        perror("Error opening file");
        return;
    }
    
    char key[MAX_LINE], text[MAX_LINE];
    if (!fgets(key, MAX_LINE, file) || !fgets(text, MAX_LINE, file)) {
        fclose(file);
        perror("Error reading file");
        return;
    }
    key[strcspn(key, "\n")] = 0;
    text[strcspn(text, "\n")] = 0;
    fclose(file);
    
    vigenere_cipher(text, key, 1);
    
    file = fopen("tmp.txt", "w");
    if (!file) {
        perror("Error writing to file");
        return;
    }
    fprintf(file, "%s\n%s\n", key, text);
    fclose(file);
}
