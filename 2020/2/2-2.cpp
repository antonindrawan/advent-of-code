#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <fstream>
#include <string>
int main()
{
    freopen("in.txt", "r", stdin);

    int lower, upper = 0;
    char valid_char;
    const auto maxLen = 40;
    char password[maxLen];

    int validPassword = 0;
    int charCounter[255];
    for (auto c : charCounter) {
        std::cout << c;
    }

    char tmp;

    while (scanf("%d-%d %c: %s\n", &lower, &upper, &valid_char, &password[0]) == 4)
    {
        memset(charCounter, 0, 255 * sizeof(int));
        auto len = strnlen(password, maxLen);

        for (int i = 0; i < len; ++i)
        {
            charCounter[password[i]]++;
        }

        int count = 0;
        if (password[lower - 1] == valid_char) count++;
        if (password[upper - 1] == valid_char) count++;

        std::cout << lower << "-" << upper << " " << valid_char << ": " << password;
        if (count == 1)
        {
            std::cout << " --> OK\n";
            validPassword++;
        }
        else
        {
            std::cout << " --> INVALID\n";
        }
    }
    fclose(stdin);

    std::cout << "The amount of valid passwords is " << validPassword << "\n";

    return 0;
}