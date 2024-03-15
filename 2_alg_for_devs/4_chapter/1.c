#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long get_divided_by_number(int number)
{
    long count = 0;

    for (int i = 1; i <= 100000000; i++)
    {
        if (i % number == 0)
        {
            count++;
        }
    }
    return count;
}

long get_odd_number_count(long numbers[], long length){

    long count = 0;
    for(int i = 0; i < length; i++){
        if(numbers[i] % 2 != 0){
            count++;
        }
    }
    return count;
}

void get_random_number_in_array(long *numbers, long length){
    for(int i = 0; i < length; i++){
        numbers[i] = rand();
    }
}

int main()
{   
    clock_t begin = clock();
    
    long numbers[100000];
    long length = sizeof(numbers) / sizeof(numbers[0]);

    get_random_number_in_array(numbers, length);



    long res = get_odd_number_count(numbers, length);


    // long res = get_divided_by_number(3);
    printf("%ld", res);
    clock_t end = clock();

    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    
    printf("\nTime spent: %.4f seconds", time_spent);
    return 0;
}