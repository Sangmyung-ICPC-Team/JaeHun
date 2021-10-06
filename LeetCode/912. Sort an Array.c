
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void merge_sort(int* nums, int low, int high);
void merge(int* nums, int low, int mid, int high);

int* sortArray(int* nums, int numsSize, int* returnSize)
{
    int low = 0;
    int high = numsSize-1;
    int* result =(int *)malloc(sizeof(int)*numsSize);
    
    merge_sort(nums,low,high);
    
    for(int i = 0; i < numsSize; i++)
    {
        result[i] = nums[i];
    }
    
    *returnSize=numsSize;
    return result;
}

void merge_sort(int* nums,int low,int high)
{
    if(high > low)
    {
        int mid = (low+high)/2;
        merge_sort(nums,low,mid);
        merge_sort(nums,mid+1,high);
        merge(nums,low,mid,high);
    }
}

void merge(int* nums, int low, int mid, int high)
{
    int k = low;
    int a,b;
    a = mid - low + 1;
    b = high-mid;
    int left[a], right[b];
    for(int i = 0; i < a; i++)
    {
        left[i] = nums[low + i];
    }
    for(int j = 0; j < b; j++)
    {
        right[j] = nums[mid + j + 1];
    }
    
    int i = 0;
    int j = 0;
    
    while(i < a && j < b)
    {
        if(left[i] < right[j])
        {
            nums[k] = left[i];
            i++;
        }
        else
        {
            nums[k] = right[j];
            j++;
        }
        k++;
        
    }
    while(i < a)
    {
        nums[k] = left[i];
        i++;
        k++;
        
    }
    while(j < b)
    {
        nums[k] = right[j];
        j++;
        k++;
    }
    
}
