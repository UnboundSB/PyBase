#include <unordered_map>
#include <random>
#include <string>
#include <vector>
#include <stdexcept>
#include <algorithm>
#include <iostream>
#include <cstring>  // For C string handling

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

class Crypter {
private:
    std::unordered_map<char, std::string> encryption_map;
    std::unordered_map<std::string, char> decryption_map;
    std::default_random_engine generator;
    std::uniform_int_distribution<int> distribution;

    void generate_mapping() {
        std::vector<int> used_values;
        for (char c = 32; c <= 126; ++c) {  // Printable ASCII characters
            int value;
            do {
                value = distribution(generator);
            } while (std::find(used_values.begin(), used_values.end(), value) != used_values.end());

            used_values.push_back(value);
            std::string enc_value = std::to_string(value);
            encryption_map[c] = enc_value;
            decryption_map[enc_value] = c;
        }
    }

public:
    Crypter() : distribution(10, 999) { // Random values between 10 and 999
        std::random_device rd;
        generator.seed(rd());
        generate_mapping();
    }

    std::string encrypt(const std::string& plaintext) {
        std::string ciphertext;
        for (char c : plaintext) {
            ciphertext += encryption_map[c] + " ";
        }
        return ciphertext;
    }

    std::string decrypt(const std::string& ciphertext) {
        std::string decrypted;
        size_t pos = 0, next_pos;
        while ((next_pos = ciphertext.find(' ', pos)) != std::string::npos) {
            std::string enc_char = ciphertext.substr(pos, next_pos - pos);
            if (decryption_map.find(enc_char) == decryption_map.end()) {
                throw std::runtime_error("Decryption failed: Invalid sequence");
            }
            decrypted += decryption_map[enc_char];
            pos = next_pos + 1;
        }
        return decrypted;
    }
};

// Global crypter instance
Crypter crypter;

// C functions to expose
extern "C" {
    EXPORT const char* encrypt_text(const char* input) {
        static std::string encrypted;
        encrypted = crypter.encrypt(input);
        return encrypted.c_str();
    }

    EXPORT const char* decrypt_text(const char* input) {
        static std::string decrypted;
        decrypted = crypter.decrypt(input);
        return decrypted.c_str();
    }
}
