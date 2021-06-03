#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int N;
    
    scanf("%d", &N);
    
    long long D[N-1], C[N];
    
    for(int i = 0; i < N-1; i++)
        scanf("%lld", &D[i]);
    for(int i = 0; i < N; i++) 
        scanf("%lld", &C[i]);
    
    long long M, T, Total = 0;
    
    M = C[0];
    T = D[0];
    
    for(int i = 1; i < N-1; i++)
    {
        if(C[i] < M)
        {
            Total += M*T;
            M = C[i];
            T = D[i];
        }
        else
            T += D[i];
    }
    
    Total += M*T;
    printf("%lld\n", Total);
    
    return 0;
}
