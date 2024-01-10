// Given 2 strings s1 and s2, modify string s1 such  that all the common characters of s1 and s2 is to  be removed aand the uncommon of s1 and s2 is to be concatenated.
// str1 = aacdb
// str2 = cbgf
#include <stdio.h>
#include <string.h>

int main()
{
    char str1[] = "aacbd";
    char str2[] = "cbgf";
    char strAns[] = "";
    for (int i = 0; i < strlen(str1) + 1; i++)
    {
        int count = 0;
        for (int j = 0; strlen(str2) + 1; j++)
        {
            if (str1[i] == str2[j])
            {
                count += 1;
            }
        }
        printf("%c", str1[i]);
    }
    return 0;
}