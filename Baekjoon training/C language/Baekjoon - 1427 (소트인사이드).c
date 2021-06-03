#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char str[11];

    gets(str);

    for (int i = 0; i < str[i] != NULL; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (str[i] > str[j])
            {
                char tmp;
                tmp = str[i];
                str[i] = str[j];
                str[j] = tmp;
            }
        }
    }
    puts(str);
    return 0;
}
