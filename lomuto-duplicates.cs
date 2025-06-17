public class Solution {
    Random random = new Random();

    public int[] rand_part(int[] arr, int low, int high) {
        int r = random.Next(high - low + 1) + low;
        int pivot = arr[r];
        int l, h;
        l = low;
        h = low;
        for(int c = low; c <= high; c++){
            if(arr[c] < pivot){
                int tmp = arr[c];
                arr[c] = arr[h];
                arr[h] = arr[l];
                arr[l] = tmp;
                l++;
                h++;
            }else if(arr[c] == pivot){
                int temp = arr[h];
                arr[h] = arr[c];
                arr[c] = temp;
                h++;
        }
        }
        return [l, h];
    }

    public void qsort(int[] arr, int l, int h) {
        if (l < h) {
            int[] p = rand_part(arr, l, h);
            if(p[0] > 0){
                qsort(arr, l, p[0] - 1);
            }
            qsort(arr, p[1], h);
        }
    }

    public int[] SortArray(int[] nums) {
        qsort(nums, 0, nums.Length - 1);
        return nums;
    }
}


